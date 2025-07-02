import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_resposta_com_gpt(texto_original):
    prompt = (
       "Considere que você é um assistente profissional respondendo a um email de forma educada, clara e objetiva.\n\n"
    "Lembre-se: emails produtivos são aqueles que geram resultados concretos e estratégicos, "
    "enquanto emails improdutivos são aqueles que consomem tempo sem retorno real. "
    "A diferença está no foco, na gestão da rotina e no impacto das tarefas executadas.\n\n"
    f"Email recebido:\n{texto_original}\n\n"
    "Escreva uma resposta adequada para este conteúdo, mantendo o tom humano, respeitoso e alinhado ao contexto empresarial."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Erro ao gerar resposta: {str(e)}]"
# Função para gerar uma resposta usando o modelo GPT-3.5 Turbo
# Ela recebe o texto original do email e retorna uma resposta formatada.