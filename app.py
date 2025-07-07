from flask import Flask, request, render_template_string
import spacy
import requests
import json

app = Flask(__name__)

# Carrega modelo spaCy para português
try:
    nlp = spacy.load("pt_core_news_sm")
    print("✅ Modelo spaCy carregado com sucesso!")
except OSError:
    print("⚠️ Modelo spaCy não encontrado. Usando classificação simples.")
    nlp = None

# Template HTML inline
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Classificador de E-mails com IA</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh;">
    <div class="container py-5">
        <h1 class="text-center mb-4 text-white">
            <i class="fa-solid fa-envelope-open-text text-primary"></i>
            Classificador de E-mails com IA
        </h1>

        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card shadow-sm mb-4">
                    <div class="card-body">
                        <form method="POST" action="/processar">
                            <div class="mb-3">
                                <label for="texto_email" class="form-label">Cole o conteúdo do e-mail:</label>
                                <textarea class="form-control" id="texto_email" name="texto_email" rows="6" placeholder="Digite ou cole aqui...">{{ texto_email or "" }}</textarea>
                            </div>

                            <div class="d-flex gap-2">
                                <button type="submit" class="btn btn-primary btn-lg">
                                    <i class="fa-solid fa-paper-plane"></i> Enviar para IA
                                </button>
                                <button type="button" class="btn btn-outline-secondary btn-lg" onclick="window.location.href='/'">
                                    <i class="fa-solid fa-eraser"></i> Limpar
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
                
                {% if categoria or resposta %}
                <div class="card shadow-sm mb-4">
                    <div class="card-body">
                        {% if categoria %}
                            <div class="mt-4">
                                <h4>Categoria detectada:</h4>
                                <span class="badge {% if categoria == 'Produtivo' %}bg-success{% else %}bg-secondary{% endif %} fs-4 py-2 px-4">
                                    <i class="fa-solid fa-tag"></i> {{ categoria }}
                                </span>
                            </div>
                        {% endif %}

                        {% if resposta %}
                            <div class="mt-4">
                                <h4><i class="fa-solid fa-robot text-info"></i> Resposta sugerida:</h4>
                                <div class="alert alert-info fs-5">
                                    {{ resposta }}
                                </div>
                            </div>
                        {% endif %}
                    </div>
                </div>
                {% endif %}
            </div>
        </div>

        <footer class="text-center mt-5 text-white small">
            Desenvolvido por Manoela | IA + Flask 🤖💌
        </footer>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

# Lista simples para armazenar histórico (reinicia a cada execução)
historico = []

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/processar', methods=['POST'])
def processar():
    texto = request.form.get('texto_email') or ''
    
    # Se nenhum conteúdo foi fornecido
    if not texto.strip():
        return render_template_string(HTML_TEMPLATE, categoria="⚠️ Nenhum conteúdo recebido.", resposta="Por favor, insira texto.")

    # Classificação avançada com NLP
    categoria = classificar_email_avancado(texto)
    resposta = gerar_resposta_com_ia(texto, categoria)

    # Salva no histórico (em memória)
    historico.append({
        'texto': texto,
        'categoria': categoria,
        'resposta': resposta
    })

    # Exibe resultado
    return render_template_string(
        HTML_TEMPLATE,
        categoria=categoria,
        resposta=resposta,
        texto_email=texto
    )

def classificar_email_avancado(texto):
    """Classificação avançada com spaCy"""
    if nlp is None:
        # Fallback para classificação simples
        return classificar_email_simples(texto)
    
    # Processamento com spaCy
    doc = nlp(texto.lower())
    
    # Palavras-chave produtivas com lematização
    palavras_produtivas = ['suporte', 'dúvida', 'pendência', 'status', 'requerimento', 'problema', 'ajuda', 'solicitação', 'assistência']
    
    # Extrai lemas (formas base das palavras)
    lemas = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    
    # Verifica palavras-chave nos lemas
    for palavra in palavras_produtivas:
        if palavra in lemas:
            return "Produtivo"
    
    # Análise adicional: verifica entidades nomeadas
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'PERSON', 'MONEY', 'DATE']:
            # Se tem entidades importantes, pode ser produtivo
            if any(palavra in texto.lower() for palavra in ['preciso', 'necessito', 'urgente']):
                return "Produtivo"
    
    return "Improdutivo"

def classificar_email_simples(texto):
    """Classificação simples (fallback)"""
    texto_lower = texto.lower()
    palavras_produtivas = ['suporte', 'dúvida', 'pendência', 'status', 'requerimento', 'problema', 'ajuda']
    
    for palavra in palavras_produtivas:
        if palavra in texto_lower:
            return "Produtivo"
    return "Improdutivo"

def gerar_resposta_com_ia(texto, categoria):
    """Gera resposta usando API de IA (Hugging Face)"""
    try:
        # API Hugging Face para geração de texto
        API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        
        # Prompt em português
        prompt = f"""
        Você é um assistente profissional respondendo a um email.
        Email recebido: {texto}
        Categoria: {categoria}
        
        Responda de forma educada e profissional em português brasileiro.
        Seja conciso e direto ao ponto.
        """
        
        headers = {"Content-Type": "application/json"}
        payload = {"inputs": prompt}
        
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', 'Resposta gerada com sucesso.')
            return "Resposta gerada com sucesso."
        else:
            # Fallback para resposta automática
            return gerar_resposta_automatica(categoria)
            
    except Exception as e:
        # Fallback para resposta automática
        return gerar_resposta_automatica(categoria)

def gerar_resposta_automatica(categoria):
    """Resposta automática baseada na categoria"""
    if categoria == "Produtivo":
        return "Olá! Recebemos sua solicitação e em breve retornaremos com uma solução. Nossa equipe está analisando o caso e retornaremos em até 24 horas. Obrigado pelo contato!"
    else:
        return "Agradecemos sua mensagem! Caso precise de alguma informação ou suporte, estamos sempre disponíveis para ajudar."

def gerar_resposta_simples(texto, categoria):
    """Resposta simples (fallback)"""
    if categoria == "Produtivo":
        return "Olá! Recebemos sua solicitação e em breve retornaremos com uma solução. Obrigado pelo contato."
    else:
        return "Agradecemos sua mensagem! Caso precise de algo, estamos à disposição."

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 