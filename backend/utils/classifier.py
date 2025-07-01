import spacy

# Carrega modelo de português
nlp = spacy.load("pt_core_news_sm")

# Lista de palavras-chave base (mantemos sua lógica!)
palavras_produtivas = ['suporte', 'dúvida', 'pendência', 'status', 'requerimento']

def preprocessar_texto(texto):
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

