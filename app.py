from flask import Flask, request, render_template

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

# Lista simples para armazenar histórico (reinicia a cada execução)
historico = []

# Extensões de arquivos permitidas
ALLOWED_EXTENSIONS = {'txt'}

# Verifica se a extensão do arquivo é válida
def arquivo_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    texto = request.form.get('texto_email') or ''
    arquivo = request.files.get('arquivo_email')

    # Se arquivo foi enviado e é válido
    if arquivo and arquivo.filename != '' and arquivo_permitido(arquivo.filename):
        # Se for .txt
        if arquivo.filename and arquivo.filename.endswith('.txt'):
            texto = arquivo.read().decode('utf-8')
            # Verifica se está vazio após leitura
            if not texto.strip():
                return render_template('index.html', categoria="⚠️ Arquivo vazio!", resposta="Por favor, envie um arquivo com conteúdo válido.")

    # Se nenhum conteúdo foi fornecido
    if not texto.strip():
        return render_template('index.html', categoria="⚠️ Nenhum conteúdo recebido.", resposta="Por favor, insira texto ou envie um arquivo válido.")

    # Classificação simples (sem spaCy)
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
    """Classificação simples sem spaCy"""
    texto_lower = texto.lower()
    palavras_produtivas = ['suporte', 'dúvida', 'pendência', 'status', 'requerimento', 'problema', 'ajuda']
    
    for palavra in palavras_produtivas:
        if palavra in texto_lower:
            return "Produtivo"
    return "Improdutivo"

def gerar_resposta_simples(texto, categoria):
    """Resposta simples sem dependências externas"""
    if categoria == "Produtivo":
        return "Olá! Recebemos sua solicitação e em breve retornaremos com uma solução. Obrigado pelo contato."
    else:
        return "Agradecemos sua mensagem! Caso precise de algo, estamos à disposição."

if __name__ == "__main__":
    app.run() 