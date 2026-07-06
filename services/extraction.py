import io
from pathlib import Path
import PyPDF2
from config import Config

def allowed_file(filename):
    return '.' in filename and \
           Path(filename).suffix.lower() in Config.ALLOWED_EXTENSIONS

def extract_text(file):
    if not file or not allowed_file(file.filename):
        return None
    try:
        ext = Path(file.filename).suffix.lower()
        if ext == ".txt":
            return file.read().decode("utf-8")
        elif ext == ".pdf":
            reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
            return "".join(p.extract_text() or "" for p in reader.pages)
    except Exception as e:
        print(f"Erro crítico na extração do arquivo: {e}")
    return None