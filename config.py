import os
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(".") / ".env")

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", os.urandom(24))
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024 
    ALLOWED_EXTENSIONS = {'.txt', '.pdf'}
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    @staticmethod
    def validate():
        if not Config.GEMINI_API_KEY:
            raise RuntimeError("GEMINI_API_KEY não encontrada no .env")
    
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] $(names)s: %(message)s',
        handlers=[
            logging.StreamHandler() 
        ]
    )