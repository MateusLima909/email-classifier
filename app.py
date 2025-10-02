import os
import requests
import io
from flask import Flask, render_template, request
from dotenv import load_dotenv
import PyPDF2
from openai import OpenAI

app = Flask(__name__)

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")

print(f"!!! DEBUG: Minha chave de API carregada é: {API_TOKEN} !!!")

CLASSIFICATION_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
GENERATION_API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b-it"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query_api(payload, url):
    response = requests.post(url, headers=headers, json=payload)

    print(f"--- DEBUG DA API ---")
    print(f"URL Chamada: {url}")
    print(f"Status da Resposta: {response.status_code}")
    print(f"Conteúdo da Resposta: {response.text}")
    print(f"--- FIM DO DEBUG ---")

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
        # Pega a chave da OpenAI do ambiente e cria o cliente
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Este é o prompt otimizado para os modelos da OpenAI
        system_prompt = "Você é um assistente prestativo que escreve respostas profissionais e concisas para emails, em português do Brasil."
        user_prompt = f"Com base no email abaixo, escreva uma sugestão de resposta curta e educada:\n\n---\n{email_text}\n---"

        # Faz a chamada para a API do ChatGPT
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Modelo rápido e eficiente
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=150,
            temperature=0.5
        )

        # Retorna o conteúdo da resposta da IA
        return completion.choices[0].message.content.strip()

    except Exception as e:
        # Se algo der errado (chave inválida, etc.), retorna uma mensagem de erro clara
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return f"Ocorreu um erro ao conectar com a IA da OpenAI: {e}"

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