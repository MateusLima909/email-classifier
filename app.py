import os
import requests
import io
from flask import Flask, render_template, request
from dotenv import load_dotenv
import PyPDF2
import google.generativeai as genai

app = Flask(__name__)

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

CLASSIFICATION_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query_api(payload, url):
    response = requests.post(url, headers=headers, json=payload)

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": f"A API retornou um status {response.status_code} com a mensagem: {response.text}"}

def classify_email(text):
    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": ["Produtivo", "Improdutivo"]},
    }
    output = query_api(payload, CLASSIFICATION_API_URL)

    if output and 'labels' in output:
        return output['labels'][0]
    elif 'error' in output:
        return f"Erro na classificação: {output['error']}"
    return "Indefinido"

def generate_response(classification, email_text):
    if classification != "Produtivo":
        return "Nenhuma resposta sugerida para e-mails que não necessitam de uma resposta de ação."

    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "Erro: A chave da API do Google não foi encontrada no arquivo .env"

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel('gemini-1.0-pro')

        prompt = f"""Com base no seguinte email, classificado como 'Produtivo', escreva uma sugestão de resposta profissional, curta e educada em português do Brasil.

Email:
---
{email_text}
---

Sugestão de Resposta:"""

        response = model.generate_content(prompt)
        
        return response.text.strip()

    except Exception as e:
        print(f"Erro ao chamar a API do Google Gemini: {e}")
        return f"Ocorreu um erro ao conectar com a IA do Google: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    classification, suggestion, email_text = None, None, ""

    if request.method == 'POST':
        email_text_from_form = request.form.get('email_text')
        email_file = request.files.get('email_file')

        if email_file and email_file.filename != '':
            if email_file.filename.endswith('.txt'):
                email_text = email_file.read().decode('utf-8')
            elif email_file.filename.endswith('.pdf'):
                try:
                    pdf_reader = PyPDF2.PdfReader(io.BytesIO(email_file.read()))
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text()
                    email_text = text
                except Exception as e:
                    email_text = f"Erro ao ler o PDF: {e}"
        else:
            email_text = email_text_from_form

        if email_text:
            classification = classify_email(email_text[:512])
            
            suggestion = generate_response(classification, email_text)

    return render_template('index.html', 
                           classification=classification, 
                           suggestion=suggestion, 
                           email_text=email_text)

if __name__ == '__main__':
    app.run(debug=True)