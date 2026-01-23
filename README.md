# 📧 AI Email Classifier & Responder

> **Classificação inteligente e respostas automáticas para emails usando Google Gemini AI.**

![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Gemini AI](https://img.shields.io/badge/AI-Gemini_2.5_Flash-orange)

## 📖 Sobre o Projeto

O **AI Email Classifier** é uma aplicação web Full Stack desenvolvida para otimizar a produtividade no gerenciamento de emails.

A ferramenta utiliza a inteligência artificial do **Google Gemini (Modelo 2.5 Flash)** para ler o conteúdo de emails (via texto ou upload de arquivos PDF/TXT), classificar a urgência e o contexto, e gerar automaticamente uma sugestão de resposta profissional.

### ✨ Funcionalidades Principais

* **Classificação Inteligente:** Distingue automaticamente entre emails **Produtivos** (Trabalho, Projetos, Reuniões) e **Improdutivos** (Spam, Marketing, Social).
* **Geração de Respostas:** Cria rascunhos de resposta contextualizados, adotando personas profissionais (ex: Assistente Executivo ou RH).
* **Leitura de Arquivos:** Suporte para upload e análise de arquivos `.txt` e `.pdf` (extração de texto).
* **Interface Moderna:** Design responsivo com suporte a **Dark Mode** e **Light Mode**.
* **Alta Performance:** Otimizado com o modelo Gemini 2.5 Flash para respostas quase instantâneas.

---

## 📸 Screenshots


|<img src="assets/print-dark.png" width="400" alt="Dark Mode">|<img src="assets/print-light.png" width="400" alt="Light Mode">|
|:---:|:---:|
|**Dark Mode**|**Light Mode**|

---

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python, Flask
* **IA / LLM:** Google Gemini API (`google-generativeai`)
* **Manipulação de Arquivos:** PyPDF2
* **Front-end:** HTML5, CSS3 (Variáveis CSS para temas), JavaScript
* **Ambiente:** Dotenv para gestão de variáveis de ambiente

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

* Python 3.x instalado.
* Uma chave de API do Google AI Studio (Gemini).

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MateusLima909/email-classifier.git](https://github.com/MateusLima909/email-classifier.git)
    cd email-classifier
    ```

2.  **Crie um ambiente virtual (Opcional, mas recomendado):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a API Key:**
    * Crie um arquivo `.env` na raiz do projeto.
    * Adicione sua chave:
        ```env
        GEMINI_API_KEY=sua_chave_aqui_sem_aspas
        ```

5.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
    * Acesse no navegador: `http://127.0.0.1:5000`

---

## 🗺️ Roadmap (Próximos Passos)

Este projeto está em evolução constante! Aqui estão as atualizações planejadas para as próximas versões:

- [ ] **Deploy:** Publicação da aplicação em ambiente de produção (Render/Vercel).
- [ ] **Testes Automatizados:** Implementação de testes unitários para garantir a estabilidade da classificação.
- [ ] **Novas Categorias:** Adição de classificações mais granulares, como *"Lembrete de Atenção"* e *"Urgente"*.
- [ ] **Histórico:** Salvar o histórico de emails analisados localmente.
- [ ] **Upload de Imagens:** Suporte para OCR em prints de email usando a capacidade multimodal do Gemini.

---

## 🤝 Contribuição

Sugestões e pull requests são bem-vindos! Sinta-se à vontade para abrir uma issue se encontrar algum problema.

## 📝 Licença

Desenvolvido por **[Mateus Lima](https://www.linkedin.com/in/mateuslimasantos)**.