import os
import io
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
from pathlib import Path
import PyPDF2
import google.generativeai as genai

load_dotenv(Path(".") / ".env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("A variável GEMINI_API_KEY não foi encontrada no .env")

app = Flask(__name__)

genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

def classify_email_with_gemini(text):
    """
    Usa o Gemini para classificar o email. 
    É muito mais rápido e estável que a API gratuita da HF.
    """
    prompt = f"""
    Analise o seguinte texto de email. 
    Classifique-o estritamente como "Produtivo" (relacionado a trabalho, projetos, agendamentos, tarefas importantes) 
    ou "Improdutivo" (spam, promoções, newsletters, phishing, social irrelevante).
    
    Responda APENAS com uma única palavra: "Produtivo" ou "Improdutivo".
    
    Email:
    ---
    {text}
    ---
    """
    try:
        response = gemini_model.generate_content(prompt)
        classification = response.text.strip().replace('"', '').replace('.', '')
        
        if "Produtivo" in classification:
            return "Produtivo"
        elif "Improdutivo" in classification:
            return "Improdutivo"
        else:
            return "Produtivo"
            
    except Exception as e:
        print(f"Erro na classificação com Gemini: {e}")
        return "Produtivo"

def generate_response(classification, email_text):
    if classification == "Produtivo":
        prompt = f"""
        Você é um assistente executivo eficiente.
        Você recebeu o seguinte email de trabalho.
        
        Tarefa: Escreva uma resposta profissional, objetiva e educada em português do Brasil.
        Não invente dados (nomes, datas) que não estão no email. Deixe espaços [assim] para o usuário preencher se necessário.
        
        Email recebido:
        ---
        {email_text}
        ---
        
        Resposta sugerida:
        """
    else:
        return "Este email foi classificado como Improdutivo/Spam. Nenhuma resposta é necessária."
        
    try:
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Erro ao gerar resposta automática: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    classification = None
    suggestion = None
    email_text = ""

    if request.method == "POST":
        email_text_from_form = request.form.get("email_text")
        email_file = request.files.get("email_file")

        if email_file and email_file.filename:
            if email_file.filename.endswith(".txt"):
                email_text = email_file.read().decode("utf-8")

            elif email_file.filename.endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(io.BytesIO(email_file.read()))
                    email_text = "".join(
                        page.extract_text() or "" for page in pdf_reader.pages
                    )
                except Exception as e:
                    email_text = f"Erro ao ler PDF: {e}"
        else:
            email_text = email_text_from_form or ""

        if email_text:
            email_processed = email_text[:4000]
            
            classification = classify_email_with_gemini(email_processed)
            
            suggestion = generate_response(classification, email_processed)

    return render_template(
        "index.html",
        classification=classification,
        suggestion=suggestion,
        email_text=email_text
    )

if __name__ == "__main__":
    app.run(debug=True)