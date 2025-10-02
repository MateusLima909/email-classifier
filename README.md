# 🚀 Classificador de Emails com IA - Desafio AutoU

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do processo seletivo para a vaga de estágio em Desenvolvimento na **AutoU**. O desafio consiste em criar uma aplicação web que utiliza Inteligência Artificial para classificar o conteúdo de emails em "Produtivo" ou "Improdutivo" e, com base nessa classificação, sugerir uma resposta automática adequada.

A aplicação foi construída com foco em uma experiência de usuário limpa, moderna e intuitiva, demonstrando a capacidade de resolver um problema real de forma simples e eficiente através da tecnologia.

## ✨ Funcionalidades Principais

* **Análise de Texto e Arquivos:** Permite colar o texto de um email diretamente ou fazer o upload de arquivos `.txt` e `.pdf`.
* **Classificação Inteligente:** Utiliza um modelo de Processamento de Linguagem Natural (NLP) da Hugging Face para categorizar o email.
* **Geração de Resposta com IA:** Sugere uma resposta automática profissional e contextualmente apropriada para emails produtivos.
* **Interface Moderna e Responsiva:** Design limpo, com uma ótima experiência tanto em desktop quanto em dispositivos móveis.
* **Tema Claro e Escuro (Light/Dark Mode):** Inclui um seletor de tema animado para maior conforto visual, com a preferência do usuário salva localmente.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando uma stack moderna de tecnologias web e de IA:

* **Backend:**
    * ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    * ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) - Para a construção do servidor web e da API.
* **Frontend:**
    * ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
    * ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
    * ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) - Para a interatividade do seletor de tema e do upload de arquivos.
* **Inteligência Artificial:**
    * **Hugging Face API:** Utilizada para acessar modelos pré-treinados de classificação (zero-shot) e geração de texto.
* **Deploy (Hospedagem):**
    * **Render:** Plataforma de nuvem utilizada para hospedar a aplicação.
* **Ambiente de Desenvolvimento:**
    * **GitHub Codespaces:** Ambiente de desenvolvimento na nuvem para agilidade e portabilidade.

---

## 🚀 Como Executar o Projeto Localmente

Para rodar este projeto em sua máquina, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MateusLima909/desafio-autou](https://github.com/MateusLima909/desafio-autou)
    cd desafio-autou
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Dentro dele, adicione sua chave de API da Hugging Face:
        ```
        HF_API_TOKEN=sua_chave_de_api_aqui
        ```

5.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

A aplicação estará disponível em `http://127.0.0.1:5000`.

---

## 👨‍💻 Desenvolvido por

* **[Mateus Lima](www.linkedin.com/in/mateuslima-santos)**