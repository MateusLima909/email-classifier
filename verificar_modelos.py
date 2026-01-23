import google.generativeai as genai
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".") / ".env")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("🔍 Perguntando ao Google quais modelos estão disponíveis para você...")

try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Disponível: {m.name}")
except Exception as e:
    print(f"❌ Erro ao listar: {e}")