import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configuração para Google Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

RESPOSTAS_AUTOMATICAS = {
    "Produtivo": "Olá! Recebemos sua solicitação e em breve retornaremos com uma solução. Obrigado pelo contato.",
    "Improdutivo": "Agradecemos sua mensagem! Caso precise de algo, estamos à disposição."
}

def gerar_resposta_com_gemini(texto_original):
    """Gera resposta usando Google Gemini"""
    
    if not GEMINI_API_KEY:
        return "🤖 Usando resposta automática (Gemini não configurado)"
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""
        Você é um assistente profissional respondendo a um email.
        
        Email recebido: {texto_original}
        
        Responda de forma educada e profissional em português brasileiro.
        Seja conciso e direto ao ponto.
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

def resposta_automatica_por_categoria(categoria):
    """Retorna resposta automática baseada na categoria"""
    return RESPOSTAS_AUTOMATICAS.get(
        categoria,
        "Não foi possível sugerir uma resposta automática para esta categoria."
    ) 