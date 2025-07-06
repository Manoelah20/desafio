# 📬 Classificador de Emails com IA — Desafio AutoU

Este projeto é uma aplicação web que classifica emails como **Produtivos** ou **Improdutivos** usando técnicas de **Processamento de Linguagem Natural (NLP)** e integrações com **IA generativa** (OpenAI). Após a classificação, o sistema também sugere uma resposta automática adequada.

---

## 🚀 Funcionalidades

- 📎 Upload de arquivos `.txt` e `.pdf`
- ✏️ Inserção direta de texto
- 🧠 Classificação automática como **Produtivo** ou **Improdutivo**
- 🤖 Geração de resposta automática com base no conteúdo
- 🌐 Interface web acessível, responsiva e simples de usar
- 📊 Histórico de classificações recentes

---

## 🛠 Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Backend:** Python + Flask
- **IA:** Sistema de classificação inteligente com respostas contextuais
- **Processamento de arquivos:** Suporte a arquivos .txt
- **Hospedagem:** Render

---

## 📸 Demonstração

🔗 **Acesse a aplicação hospedada:**  
[https://desafioweb-fr28.onrender.com](https://desafioweb-fr28.onrender.com)

🎥 **Vídeo de demonstração (YouTube):**  
[Link será adicionado após gravação]

---

## 💻 Como Rodar Localmente

### 1. Clone o repositório:
```bash
git clone https://github.com/Manoelah20/desafio.git
cd desafio
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente (opcional):
Crie um arquivo `.env` na raiz do projeto se quiser usar APIs externas:
```env
# Opcional - apenas se quiser usar OpenAI ou outras APIs
OPENAI_API_KEY=sua_chave_api_aqui
```

### 4. Execute a aplicação:
```bash
python app.py
```

### 5. Acesse no navegador:
http://localhost:5000

---

## 📁 Estrutura do Projeto

```
desafio-web/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── render.yaml           # Configuração para deploy no Render
├── backend/
│   ├── utils/
│   │   ├── classifier.py  # Classificador de emails
│   │   └── responder.py   # Gerador de respostas com OpenAI
│   └── arquivos_exemplo/  # Arquivos de teste
├── frontend/
│   ├── templates/
│   │   └── index.html     # Interface principal
│   └── static/
│       └── style.css      # Estilos CSS
└── README.md
```

---

## 🧠 Como Funciona

1. **Classificação:** O sistema identifica palavras-chave relacionadas a atividades produtivas (suporte, dúvida, pendência, etc.) usando análise inteligente de texto

2. **Geração de Resposta:** Utiliza um sistema de templates inteligentes que gera respostas contextuais baseadas no tipo específico de email (suporte, dúvida, pendência, status, etc.)

3. **Interface:** Interface web responsiva que permite upload de arquivos ou inserção direta de texto

---

## 🤝 Autora

Feito com 💙 por **Manoela Harrison**  
📧 LinkedIn · GitHub