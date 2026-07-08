import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import patch, MagicMock
from services.ai_analysis import analyze_email_pro, validate_analysis, fix_spacing


# --- Testes de validate_analysis ---

def test_validate_analysis_aceita_dados_corretos():
    dados = {"classification": "Produtivo", "confidence": 90, "suggestion": "Olá, tudo bem?"}
    assert validate_analysis(dados) == True

def test_validate_analysis_rejeita_classificacao_invalida():
    dados = {"classification": "Talvez", "confidence": 50, "suggestion": "x"}
    assert validate_analysis(dados) == False

def test_validate_analysis_rejeita_confianca_fora_do_range():
    dados = {"classification": "Produtivo", "confidence": 150, "suggestion": "x"}
    assert validate_analysis(dados) == False

def test_validate_analysis_rejeita_confianca_nao_inteira():
    dados = {"classification": "Produtivo", "confidence": "90", "suggestion": "x"}
    assert validate_analysis(dados) == False

def test_validate_analysis_rejeita_campo_faltando():
    dados = {"classification": "Produtivo", "confidence": 90}
    assert validate_analysis(dados) == False


# --- Testes de fix_spacing ---

def test_fix_spacing_adiciona_espaco_apos_ponto():
    assert fix_spacing("Ola.Tudo bem?") == "Ola. Tudo bem?"

def test_fix_spacing_nao_altera_texto_ja_correto():
    texto = "Ola, tudo bem? Sim, obrigado."
    assert fix_spacing(texto) == texto

def test_fix_spacing_com_acentos():
    assert fix_spacing("Perfeito.Ótimo dia!") == "Perfeito. Ótimo dia!"


# --- Testes de analyze_email_pro (mockando a chamada real ao Gemini) ---

def test_analyze_email_pro_classificacao_produtiva():
    mock_response = MagicMock()
    mock_response.text = '{"classification": "Produtivo", "confidence": 95, "suggestion": "Confirmo a reunião na quarta às 15h."}'

    with patch("services.ai_analysis.client.models.generate_content", return_value=mock_response):
        resultado = analyze_email_pro("Podemos agendar uma reunião na quarta?")
        assert resultado is not None
        assert resultado["classification"] == "Produtivo"
        assert resultado["confidence"] == 95
        assert "reunião" in resultado["suggestion"]

def test_analyze_email_pro_classificacao_improdutiva():
    mock_response = MagicMock()
    mock_response.text = '{"classification": "Improdutivo", "confidence": 88, "suggestion": "N/A"}'

    with patch("services.ai_analysis.client.models.generate_content", return_value=mock_response):
        resultado = analyze_email_pro("Promoção imperdível! Compre já!")
        assert resultado is not None
        assert resultado["classification"] == "Improdutivo"
        assert resultado["suggestion"] == "Conteúdo de baixa relevância detectado."

def test_analyze_email_pro_json_invalido_retorna_none():
    mock_response = MagicMock()
    mock_response.text = 'isso não é um JSON válido'

    with patch("services.ai_analysis.client.models.generate_content", return_value=mock_response):
        resultado = analyze_email_pro("qualquer email")
        assert resultado is None

def test_analyze_email_pro_schema_invalido_retorna_none():
    mock_response = MagicMock()
    mock_response.text = '{"classification": "Talvez", "confidence": 50, "suggestion": "x"}'

    with patch("services.ai_analysis.client.models.generate_content", return_value=mock_response):
        resultado = analyze_email_pro("qualquer email")
        assert resultado is None