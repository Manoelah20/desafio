import re
import random
from typing import Dict, List

# Sistema de respostas inteligentes locais
RESPOSTAS_TEMPLATES = {
    "Produtivo": {
        "suporte": [
            "Olá! Recebemos sua solicitação de suporte. Nossa equipe técnica está analisando o caso e retornaremos em breve com uma solução. Obrigado pelo contato!",
            "Agradecemos seu contato sobre o suporte solicitado. Estamos trabalhando para resolver sua questão o mais rápido possível. Em breve entraremos em contato.",
            "Recebemos sua solicitação de suporte. Nossa equipe está verificando os detalhes e retornaremos com uma resposta em até 24 horas."
        ],
        "dúvida": [
            "Obrigado por sua dúvida! Nossa equipe está analisando sua pergunta e preparando uma resposta detalhada. Retornaremos em breve.",
            "Agradecemos sua consulta. Estamos pesquisando as informações necessárias para responder adequadamente sua dúvida.",
            "Recebemos sua dúvida e estamos verificando os dados para fornecer a resposta mais precisa possível."
        ],
        "pendência": [
            "Recebemos sua mensagem sobre a pendência. Estamos verificando o status e tomando as providências necessárias. Retornaremos em breve.",
            "Agradecemos o alerta sobre a pendência. Nossa equipe está trabalhando para resolver a situação o mais rápido possível.",
            "Confirmamos o recebimento da informação sobre a pendência. Estamos analisando e tomando as medidas necessárias."
        ],
        "status": [
            "Recebemos sua consulta sobre o status. Estamos verificando as informações e retornaremos com os detalhes atualizados.",
            "Agradecemos sua pergunta sobre o status. Nossa equipe está consultando os sistemas e preparando um relatório completo.",
            "Confirmamos o recebimento da consulta de status. Estamos verificando os dados e retornaremos com as informações solicitadas."
        ],
        "requerimento": [
            "Recebemos seu requerimento. Estamos analisando a documentação e verificando os requisitos. Retornaremos com uma resposta em breve.",
            "Agradecemos o envio do requerimento. Nossa equipe está revisando os documentos e verificando a conformidade.",
            "Confirmamos o recebimento do requerimento. Estamos processando a solicitação e retornaremos com o status em até 48 horas."
        ]
    },
    "Improdutivo": {
        "saudação": [
            "Olá! Obrigada pelo contato. Caso precise de algo específico, estamos à disposição para ajudar.",
            "Oi! Agradecemos sua mensagem. Se precisar de alguma informação ou suporte, é só nos avisar.",
            "Olá! Obrigada por entrar em contato. Estamos sempre disponíveis caso precise de alguma coisa."
        ],
        "agradecimento": [
            "Obrigada pelo contato! Ficamos felizes em saber que está tudo bem. Caso precise de algo, estamos aqui.",
            "Agradecemos sua mensagem! É sempre um prazer receber notícias. Se precisar de alguma coisa, é só avisar.",
            "Obrigada pelo contato! Ficamos contentes com sua mensagem. Estamos à disposição caso precise de algo."
        ],
        "geral": [
            "Obrigada pelo contato! Caso precise de alguma informação ou suporte, estamos sempre disponíveis para ajudar.",
            "Agradecemos sua mensagem! Se precisar de algo específico, não hesite em nos contatar.",
            "Obrigada pelo contato! Estamos à disposição caso precise de alguma assistência ou informação."
        ]
    }
}

def identificar_tipo_email(texto: str, categoria: str) -> str:
    """Identifica o tipo específico do email baseado no conteúdo"""
    texto_lower = texto.lower()
    
    if categoria == "Produtivo":
        if any(palavra in texto_lower for palavra in ["suporte", "ajuda", "assistência"]):
            return "suporte"
        elif any(palavra in texto_lower for palavra in ["dúvida", "pergunta", "consulta"]):
            return "dúvida"
        elif any(palavra in texto_lower for palavra in ["pendência", "pendente", "atraso"]):
            return "pendência"
        elif any(palavra in texto_lower for palavra in ["status", "situação", "andamento"]):
            return "status"
        elif any(palavra in texto_lower for palavra in ["requerimento", "solicitação", "pedido"]):
            return "requerimento"
        else:
            return "suporte"  # padrão para produtivos
    
    else:  # Improdutivo
        if any(palavra in texto_lower for palavra in ["olá", "oi", "bom dia", "boa tarde", "boa noite"]):
            return "saudação"
        elif any(palavra in texto_lower for palavra in ["obrigado", "obrigada", "valeu", "agradeço"]):
            return "agradecimento"
        else:
            return "geral"

def gerar_resposta_inteligente(texto_original: str, categoria: str) -> str:
    """Gera uma resposta inteligente baseada no conteúdo e categoria"""
    
    tipo_email = identificar_tipo_email(texto_original, categoria)
    
    if categoria in RESPOSTAS_TEMPLATES and tipo_email in RESPOSTAS_TEMPLATES[categoria]:
        templates = RESPOSTAS_TEMPLATES[categoria][tipo_email]
        return random.choice(templates)
    else:
        # Resposta padrão se não encontrar template específico
        if categoria == "Produtivo":
            return "Recebemos sua solicitação. Nossa equipe está analisando e retornaremos em breve. Obrigado pelo contato!"
        else:
            return "Agradecemos sua mensagem! Caso precise de algo, estamos à disposição."

def resposta_automatica_por_categoria(categoria: str) -> str:
    """Retorna resposta automática simples baseada na categoria"""
    if categoria == "Produtivo":
        return "Olá! Recebemos sua solicitação e em breve retornaremos com uma solução. Obrigado pelo contato."
    else:
        return "Agradecemos sua mensagem! Caso precise de algo, estamos à disposição." 