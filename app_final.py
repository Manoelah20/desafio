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
<body style="background: linear-gradient(135deg, #000000 0%, #FFD700 100%); min-height: 100vh;">
    <div class="container py-5">
        <h1 class="text-center mb-4 text-white">
            <i class="fa-solid fa-envelope-open-text text-warning"></i>
            Classificador de E-mails com IA
        </h1>

        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card shadow-sm mb-4">
                    <div class="card-body">
                        <form method="POST" action="/processar" enctype="multipart/form-data">
                            <div class="mb-3">
                                <label for="texto_email" class="form-label">Cole o conteúdo do e-mail:</label>
                                <textarea class="form-control" id="texto_email" name="texto_email" rows="6" placeholder="Digite ou cole aqui...">{{ texto_email or "" }}</textarea>
                            </div>

                            <div class="mb-3">
                                <label for="arquivo_email" class="form-label">Ou envie um arquivo (.txt):</label>
                                <input type="file" class="form-control" id="arquivo_email" name="arquivo_email" accept=".txt">
                            </div>

                            <div class="d-flex gap-2">
                                <button type="submit" class="btn btn-warning btn-lg text-dark">
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
                                <span class="badge {% if categoria == 'Produtivo' %}bg-warning text-dark{% else %}bg-dark{% endif %} fs-4 py-2 px-4">
                                    <i class="fa-solid fa-tag"></i> {{ categoria }}
                                </span>
                            </div>
                        {% endif %}

                        {% if resposta %}
                            <div class="mt-4">
                                <h4><i class="fa-solid fa-robot text-warning"></i> Resposta sugerida:</h4>
                                <div class="alert alert-warning fs-5 text-dark">
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
            Desenvolvido por Manoela Harrison | IA + Flask 🤖💌
        </footer>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/processar', methods=['POST'])
def processar():
    texto = request.form.get('texto_email') or ''
    arquivo = request.files.get('arquivo_email')

    if arquivo and arquivo.filename and arquivo.filename != '':
        if arquivo.filename.endswith('.txt'):
            try:
                texto = arquivo.read().decode('utf-8')
                if not texto.strip():
                    return render_template_string(HTML_TEMPLATE, categoria="⚠️ Arquivo vazio!", resposta="Por favor, envie um arquivo com conteúdo válido.")
            except:
                return render_template_string(HTML_TEMPLATE, categoria="⚠️ Erro ao ler arquivo!", resposta="Por favor, envie um arquivo .txt válido.")
    
    if not texto.strip():
        return render_template_string(HTML_TEMPLATE, categoria="⚠️ Nenhum conteúdo recebido.", resposta="Por favor, insira texto ou envie um arquivo.")

    categoria = classificar_email(texto)
    resposta = gerar_resposta(categoria)

    return render_template_string(
        HTML_TEMPLATE,
        categoria=categoria,
        resposta=resposta,
        texto_email=texto
    )

def classificar_email(texto):
    texto_lower = texto.lower()
    
    palavras_produtivas = [
        'suporte', 'dúvida', 'pendência', 'status', 'requerimento', 
        'problema', 'ajuda', 'solicitação', 'assistência', 'urgente',
        'preciso', 'necessito', 'falha', 'erro', 'bug', 'defeito',
        'reclamação', 'reembolso', 'cancelamento', 'troca'
    ]
    
    palavras_improdutivas = [
        'spam', 'promoção', 'oferta', 'desconto', 'marketing',
        'newsletter', 'publicidade', 'propaganda', 'venda'
    ]
    
    count_produtivo = sum(1 for palavra in palavras_produtivas if palavra in texto_lower)
    count_improdutivo = sum(1 for palavra in palavras_improdutivas if palavra in texto_lower)
    
    if count_produtivo > count_improdutivo:
        return "Produtivo"
    elif count_improdutivo > count_produtivo:
        return "Improdutivo"
    else:
        if any(palavra in texto_lower for palavra in ['urgente', 'problema', 'erro', 'falha']):
            return "Produtivo"
        return "Improdutivo"

def gerar_resposta(categoria):
    if categoria == "Produtivo":
        return "Olá! Recebemos sua solicitação e em breve retornaremos com uma solução. Nossa equipe está analisando o caso e retornaremos em até 24 horas. Obrigado pelo contato!"
    else:
        return "Agradecemos sua mensagem! Caso precise de alguma informação ou suporte, estamos sempre disponíveis para ajudar."

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Iniciando aplicação na porta {port}")
    app.run(host='0.0.0.0', port=port, debug=False) 