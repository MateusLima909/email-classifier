# 📧 AI Email Classifier & Responder

> **Classificação inteligente e respostas automáticas para emails com experiência SaaS e Google Gemini AI.**

![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Gemini AI](https://img.shields.io/badge/AI-Gemini_2.5_Flash-orange)
![UI](https://img.shields.io/badge/UI-Glassmorphism-blueviolet)

## 📖 Sobre o Projeto

O **AI Email Classifier** é uma aplicação web Full Stack de alto nível desenvolvida para transformar o gerenciamento de emails em uma tarefa fluida e inteligente. 

Diferente de ferramentas simples, este projeto foca em **User Experience (UX)**, utilizando uma interface inspirada em plataformas SaaS modernas. O motor é alimentado pelo **Google Gemini 2.5 Flash**, garantindo análises contextuais precisas em milissegundos.

### ✨ Funcionalidades Principais

* **Classificação Inteligente:** Distingue automaticamente entre emails **Produtivos** e **Improdutivos** com base no contexto real da mensagem.
* **Interface Premium (Glassmorphism):** Design sofisticado com efeitos de transparência, desfoque de fundo e tipografia imponente.
* **Layout Side-by-Side:** Grid de duas colunas que permite visualizar a entrada de dados e o resultado da IA simultaneamente.
* **Geração de Respostas Profissionais:** Cria rascunhos de resposta prontos para uso, mantendo o tom de voz executivo.
* **Análise Multimodal de Arquivos:** Suporte para extração e leitura de arquivos `.pdf` e `.txt`.
* **Feedback de Processamento:** Overlay de carregamento integrado para melhorar a percepção de performance durante as chamadas de IA.

---

## 📸 Screenshots

|<img src="assets/print-start.png" width="400" alt="Dashboard Inicial">|<img src="assets/print-result.png" width="400" alt="Resultado da Análise">|
|:---:|:---:|
|**Dashboard Inicial**|**Análise em Tempo Real**|

---

## 🛠️ Tecnologias Utilizadas
* **Back-end:** Python 3.12, Flask
* **IA / LLM:** Google Gemini API (`google-genai`)
* **Front-end:** HTML5, CSS3 (Glassmorphism & CSS Grid), JavaScript (Vanilla)
* **Ícones:** Lucide Icons
* **Manipulação de Arquivos:** pypdf
* **Testes:** Pytest (unitários e mocks de integração com a API)
* **Ambiente:** Dotenv para gestão de segredos e chaves de API
---
## 🚀 Como Executar o Projeto
### Pré-requisitos
* Python 3.x instalado.
* Chave de API do Google AI Studio.
### Passo a Passo
1.  **Clone o repositório:**
```bash
    git clone https://github.com/MateusLima909/email-classifier.git
    cd email-classifier
```
2.  **Ambiente Virtual:**
```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
```
3.  **Instalação:**
```bash
    pip install -r requirements.txt
```
4.  **Variáveis de Ambiente:**
    * Crie um arquivo `.env` na raiz.
    * Adicione suas chaves:
```env
        FLASK_SECRET_KEY=sua_chave_secreta_aqui
        GEMINI_API_KEY=sua_chave_aqui
```
5.  **Run:**
```bash
    python app.py
```
    * Acesse: `http://127.0.0.1:5000`

### 🧪 Rodando os Testes
```bash
python -m pytest tests/ -v
```
---
## 🗺️ Roadmap de Evolução
- [X] **Structured Output:** Respostas em JSON com schema validado (classificação, confiança e sugestão).
- [X] **Testes Automatizados:** Cobertura via Pytest para validação, formatação e integração mockada com a IA.
- [ ] **Integração com Gmail API:** Leitura direta da caixa de entrada via OAuth2.
- [ ] **Memória de Contexto (RAG):** Banco de vetores para aprender o tom de voz do usuário com base em emails passados.
- [ ] **Persistência de Dados:** Histórico de análises salvo em banco de dados local (SQLite/PostgreSQL).
- [ ] **Deploy:** Hospedagem em nuvem (Render ou Vercel).

---

## 🤝 Contribuição

Sugestões para melhorar a IA ou o design são sempre bem-vindas! Sinta-se à vontade para abrir uma issue.

## 📝 Licença

Desenvolvido por **[Mateus Lima](https://www.linkedin.com/in/mateuslima-santos)**.
