import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Configuração para Hugging Face
HF_API_KEY = os.getenv("HF_API_KEY")  # Opcional para alguns modelos
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"

RESPOSTAS_AUTOMATICAS = {
    "Produtivo": "Olá! Recebemos sua solicitação e em breve retornaremos com uma solução. Obrigado pelo contato.",
    "Improdutivo": "Agradecemos sua mensagem! Caso precise de algo, estamos à disposição."
}

def gerar_resposta_com_hf(texto_original):
    """Gera resposta usando Hugging Face"""
    
    # Se não tiver API key, usa resposta automática
    if not HF_API_KEY:
        return "🤖 Usando resposta automática (Hugging Face não configurado)"
    
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    
    # Prompt em português
    prompt = f"""
    Você é um assistente profissional respondendo a um email.
    Email recebido: {texto_original}
    
    Responda de forma educada e profissional em português brasileiro.
    """
    
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt}
        )
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', 'Resposta gerada com sucesso.')
            return "Resposta gerada com sucesso."
        else:
            return f"Erro na API: {response.status_code}"
            
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

def resposta_automatica_por_categoria(categoria):
    """Retorna resposta automática baseada na categoria"""
    return RESPOSTAS_AUTOMATICAS.get(
        categoria,
        "Não foi possível sugerir uma resposta automática para esta categoria."
    ) 