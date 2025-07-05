import spacy

# Carrega modelo de português com tratamento de erro
try:
    nlp = spacy.load("pt_core_news_sm")
except OSError:
    print("⚠️ Modelo spaCy não encontrado. Usando classificação simples.")
    nlp = None

# Lista de palavras-chave base (mantemos sua lógica!)
palavras_produtivas = ['suporte', 'dúvida', 'pendência', 'status', 'requerimento']

def preprocessar_texto(texto):
    if nlp is None:
        # Fallback para classificação simples
        return texto.lower().split()
    
    doc = nlp(texto.lower())
    lemas = [
        token.lemma_ for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space
    ]
    return lemas

def classificar_email(texto):
    lemas = preprocessar_texto(texto)
    for palavra in palavras_produtivas:
        if palavra in lemas:
            return "Produtivo"
    return "Improdutivo"

