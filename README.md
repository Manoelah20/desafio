# 📬 Classificador de E-mails com IA — Desafio AutoU

Este projeto é uma aplicação web que classifica emails como **Produtivos** ou **Improdutivos** usando técnicas de **Processamento de Linguagem Natural (NLP)**. Após a classificação, o sistema também sugere uma resposta automática adequada.

---

## 🚀 Funcionalidades

- 📎 Upload de arquivos `.txt`
- ✏️ Inserção direta de texto
- 🧠 Classificação automática como **Produtivo** ou **Improdutivo**
- 🤖 Geração de resposta automática com base na categoria
- 🌐 Interface web responsiva com design moderno (preto e amarelo)
- 📊 Sistema de pontuação inteligente para classificação

---

## 🛠 Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, Bootstrap 5, Font Awesome
- **Backend:** Python + Flask
- **IA:** Sistema de classificação baseado em palavras-chave
- **Processamento de arquivos:** Suporte a arquivos .txt
- **Hospedagem:** Render

---

## 📸 Demonstração

🔗 **Acesse a aplicação hospedada:**  
[https://desafioweb-fr28.onrender.com](https://desafioweb-fr28.onrender.com) *(pode demorar 30-50s na primeira requisição)*

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

### 3. Execute a aplicação:
```bash
python app_final.py
```

### 4. Acesse no navegador:
http://localhost:5000

---

## 📁 Estrutura do Projeto

```
desafio-web/
├── app_final.py           # Aplicação principal Flask (versão otimizada)
├── requirements.txt       # Dependências Python (apenas Flask)
├── render.yaml           # Configuração para deploy no Render
├── Procfile              # Configuração alternativa para deploy
├── start.sh              # Script de inicialização (backup)
└── README.md
```

---

## 🧠 Como Funciona

### 1. **Classificação Inteligente:**
O sistema analisa o texto procurando por palavras-chave específicas:

**Palavras Produtivas:**
- suporte, dúvida, pendência, status, requerimento
- problema, ajuda, solicitação, assistência, urgente
- preciso, necessito, falha, erro, bug, defeito
- reclamação, reembolso, cancelamento, troca

**Palavras Improdutivas:**
- spam, promoção, oferta, desconto, marketing
- newsletter, publicidade, propaganda, venda

### 2. **Sistema de Pontuação:**
- Conta as ocorrências de palavras produtivas vs improdutivas
- Em caso de empate, verifica palavras-chave fortes (urgente, problema, erro, falha)
- Toma decisão baseada na predominância

### 3. **Geração de Resposta:**
- **Produtivo:** Resposta profissional com compromisso de retorno
- **Improdutivo:** Resposta educada e disponibilidade para suporte

---

## 🚀 Deploy

O projeto está configurado para deploy automático no Render:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app_final.py`
- **Environment:** Python
- **Port:** 10000

---

## 🎯 Características Técnicas

- ✅ **Código limpo e otimizado** - Sem dependências desnecessárias
- ✅ **Deploy confiável** - Configuração simplificada para Render
- ✅ **Interface responsiva** - Design moderno com Bootstrap 5
- ✅ **Classificação precisa** - Algoritmo baseado em palavras-chave
- ✅ **Upload de arquivos** - Suporte completo a arquivos .txt
- ✅ **Respostas automáticas** - Sistema inteligente de geração

---

## 🤝 Autora

Feito com 💙 por **Manoela Harrison**  
📧 LinkedIn · GitHub

---

## 📝 Notas de Desenvolvimento

Este projeto foi desenvolvido com foco em:
- **Simplicidade:** Código limpo e fácil de manter
- **Confiabilidade:** Funcionamento estável em produção
- **Usabilidade:** Interface intuitiva e responsiva
- **Escalabilidade:** Arquitetura preparada para expansões futuras