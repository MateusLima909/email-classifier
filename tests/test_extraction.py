import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import io
from unittest.mock import MagicMock
from services.extraction import allowed_file, extract_text


def test_allowed_file_aceita_txt():
    assert allowed_file("email.txt") == True

def test_allowed_file_aceita_pdf():
    assert allowed_file("documento.pdf") == True

def test_allowed_file_rejeita_extensao_invalida():
    assert allowed_file("virus.exe") == False

def test_allowed_file_rejeita_sem_extensao():
    assert allowed_file("arquivosemextensao") == False

def test_extract_text_le_arquivo_txt():
    mock_file = MagicMock()
    mock_file.filename = "email.txt"
    mock_file.read.return_value = "Conteúdo de teste".encode("utf-8")

    resultado = extract_text(mock_file)
    assert resultado == "Conteúdo de teste"

def test_extract_text_retorna_none_para_arquivo_invalido():
    mock_file = MagicMock()
    mock_file.filename = "virus.exe"

    resultado = extract_text(mock_file)
    assert resultado is None

def test_extract_text_retorna_none_se_arquivo_nulo():
    assert extract_text(None) is None