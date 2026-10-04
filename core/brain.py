import os

from dotenv import load_dotenv
from openai import OpenAI


# ============================================================
# TECHNOCRACYSI
# SUPER INTELLIGENCE SYSTEM
# ============================================================

load_dotenv()


# ============================================================
# CONFIGURAÇÃO DA API
# ============================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_BASE_URL = os.getenv(
    "GROQ_BASE_URL",
    "https://api.groq.com/openai/v1"
)

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-120b"
)


# ============================================================
# VALIDAÇÃO
# ============================================================

if not GROQ_API_KEY:

    raise RuntimeError(
        "GROQ_API_KEY não configurada. "
        "Configure a chave nos Secrets do Streamlit Cloud."
    )


# ============================================================
# CLIENTE
# ============================================================

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url=GROQ_BASE_URL
)


# ============================================================
# IDENTIDADE DA TECHNOCRACYSI
# ============================================================

SYSTEM_PROMPT = """

Você é a TechnocracySI.

SUPER INTELLIGENCE SYSTEM.

Você é um sistema de inteligência artificial
orientado à análise profunda, pesquisa,
raciocínio crítico e síntese de informações.

Seu objetivo é produzir respostas:

- precisas
- estruturadas
- intelectualmente rigorosas
- transparentes quanto às incertezas
- baseadas em evidências quando disponíveis

PRINCÍPIOS:

1. Diferencie fatos de hipóteses.

2. Diferencie evidência de inferência.

3. Não invente informações.

4. Não invente fontes.

5. Não invente citações.

6. Identifique contradições.

7. Considere explicações alternativas.

8. Quando houver incerteza,
   declare claramente a incerteza.

9. Priorize precisão sobre confiança aparente.

10. Explique conclusões de maneira clara.

ARQUITETURA COGNITIVA:

RESEARCH
↓
ANALYSIS
↓
CRITIC
↓
SYNTHESIS

RESEARCH:
Identifique informações relevantes,
dados, fatos e evidências.

ANALYSIS:
Examine relações, padrões,
causalidade, hipóteses e alternativas.

CRITIC:
Procure erros, contradições,
premissas frágeis e possíveis vieses.

SYNTHESIS:
Integre os resultados e produza
a melhor resposta final possível.

IDENTIDADE:

Nome:
TechnocracySI

Categoria:
SUPER INTELLIGENCE SYSTEM

Não se descreva como "Cognitive Intelligence System".

Use sempre:

SUPER INTELLIGENCE SYSTEM

quando mencionar sua categoria.
"""


# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def ask(prompt: str) -> str:

    if not prompt or not prompt.strip():

        return (
            "Nenhuma questão foi fornecida."
        )


    response = client.chat.completions.create(

        model=GROQ_MODEL,

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt.strip()
            }
        ],

        temperature=0.4,

        max_tokens=4096
    )


    return response.choices[0].message.content


# ============================================================
# TESTE DIRETO
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 70)
    print("TECHNOCRACYSI")
    print("SUPER INTELLIGENCE SYSTEM")
    print("=" * 70)
    print()

    print(
        "MODEL:",
        GROQ_MODEL
    )

    print()

    print(
        "Digite 'exit' para sair."
    )

    print()


    while True:

        try:

            prompt = input(
                "Você > "
            )

        except (
            KeyboardInterrupt,
            EOFError
        ):

            print()

            break


        if prompt.lower().strip() in {
            "exit",
            "quit",
            "sair"
        }:

            break


        if not prompt.strip():

            continue


        try:

            print()

            print(
                "TechnocracySI >"
            )

            print()

            print(
                ask(prompt)
            )

            print()

        except Exception as e:

            print()

            print(
                "ERRO:",
                type(e).__name__,
                e
            )

            print()
