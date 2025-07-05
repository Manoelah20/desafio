import os
try:
    import fitz  # PyMuPDF
except ImportError:
    import PyMuPDF as fitz  # Fallback
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template
app = Flask(
       __name__,
       template_folder="frontend/templates",
       static_folder="frontend/static"
   )
from backend.utils.responder_local import gerar_resposta_inteligente as gerar_resposta, resposta_automatica_por_categoria
from backend.utils.classifier import classificar_email

# Lista simples para armazenar histórico (reinicia a cada execução)
historico = []

# Extensões de arquivos permitidas
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

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
        # Verifica se está vazio
        if arquivo.content_length == 0:
            return render_template('index.html', categoria="⚠️ Arquivo vazio!", resposta="Por favor, envie um arquivo com conteúdo válido.")

        # Se for .txt
        if arquivo.filename.endswith('.txt'):
            texto = arquivo.read().decode('utf-8')

        # Se for .pdf
        elif arquivo.filename.endswith('.pdf'):
            with fitz.open(stream=arquivo.read(), filetype="pdf") as doc:
                texto = ''
                for pagina in doc:
                    texto += pagina.get_text()

    # Se nenhum conteúdo foi fornecido
    if not texto.strip():
        return render_template('index.html', categoria="⚠️ Nenhum conteúdo recebido.", resposta="Por favor, insira texto ou envie um arquivo válido.")

    # Processamento com IA
    categoria = classificar_email(texto)
    print(f"DEBUG: Categoria detectada: {categoria}")
    resposta = gerar_resposta(texto, categoria)
    print(f"DEBUG: Resposta gerada: {resposta}")

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

if __name__ == "__main__":
    app.run()
