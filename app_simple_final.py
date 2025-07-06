from flask import Flask, request, render_template

app = Flask(__name__)

# Lista simples para armazenar histórico (reinicia a cada execução)
historico = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    texto = request.form.get('texto_email') or ''
    
    # Se nenhum conteúdo foi fornecido
    if not texto.strip():
        return render_template('index.html', categoria="⚠️ Nenhum conteúdo recebido.", resposta="Por favor, insira texto.")

    # Classificação simples
    categoria = classificar_email_simples(texto)
    resposta = gerar_resposta_simples(texto, categoria)

    # Salva no histórico (em memória)
    historico.append({
        'texto': texto,
        'categoria': categoria,
        'resposta': resposta
    })

    # Exibe resultado com histórico invertido (mais recente no topo)
    return render_template(
        'index.html',
        categoria=categoria,
        resposta=resposta,
        texto_email=texto,
        historico=historico[::-1]
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
    app.run(host='0.0.0.0', port=5000) 