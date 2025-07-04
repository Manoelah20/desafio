import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

# Configuração para nova versão da OpenAI (1.0+)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "sk-sua-chave-real-aqui":
    print("⚠️ ATENÇÃO: Configure sua chave da OpenAI no arquivo .env")
    client = None
else:
    client = openai.OpenAI(api_key=api_key)

RESPOSTAS_AUTOMATICAS = {
    "Produtivo": "Olá! Recebemos sua solicitação e em breve retornaremos com uma solução. Obrigado pelo contato.",
    "Improdutivo": "Agradecemos sua mensagem! Caso precise de algo, estamos à disposição."
}

def gerar_resposta_com_gpt(texto_original):
    prompt = (
       "Considere que você é um assistente profissional respondendo a um email de forma educada, clara e objetiva.\n\n"
    "Lembre-se: emails produtivos são aqueles que geram resultados concretos e estratégicos, "
    "enquanto emails improdutivos são aqueles que consomem tempo sem retorno real. "
    "A diferença está no foco, na gestão da rotina e no impacto das tarefas executadas.\n\n"
    f"Email recebido:\n{texto_original}\n\n"
    "IMPORTANTE: Responda APENAS em PORTUGUÊS BRASILEIRO.\n\n"
    "Escreva uma resposta adequada para este conteúdo, mantendo o tom humano, respeitoso e alinhado ao contexto empresarial. "
    "Use linguagem formal mas acessível, típica de comunicação corporativa brasileira."
    )

    try:
        if client is None:
            return "⚠️ Configure sua chave da OpenAI no arquivo .env"
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        error_msg = str(e)
        if "insufficient_quota" in error_msg or "429" in error_msg:
            return "💳 Créditos da OpenAI esgotados. Usando resposta automática padrão."
        return f"[Erro ao gerar resposta: {error_msg}]"

def resposta_automatica_por_categoria(categoria):
    """
    Retorna a resposta automática baseada na categoria do email.
    """
    return RESPOSTAS_AUTOMATICAS.get(
        categoria,
        "Não foi possível sugerir uma resposta automática para esta categoria."
    )

# Função para gerar uma resposta usando o modelo GPT-3.5 Turbo
# Ela recebe o texto original do email e retorna uma resposta formatada.