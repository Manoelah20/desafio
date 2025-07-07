from flask import Flask, request, render_template_string

app = Flask(__name__)

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

    # Classificação simples
    categoria = classificar_email_simples(texto)
    resposta = gerar_resposta_simples(texto, categoria)

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

def classificar_email_simples(texto):
    """Classificação simples"""
    texto_lower = texto.lower()
    palavras_produtivas = ['suporte', 'dúvida', 'pendência', 'status', 'requerimento', 'problema', 'ajuda']
    
    for palavra in palavras_produtivas:
        if palavra in texto_lower:
            return "Produtivo"
    return "Improdutivo"

def gerar_resposta_simples(texto, categoria):
    """Resposta simples"""
    if categoria == "Produtivo":
        return "Olá! Recebemos sua solicitação e em breve retornaremos com uma solução. Obrigado pelo contato."
    else:
        return "Agradecemos sua mensagem! Caso precise de algo, estamos à disposição."

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 