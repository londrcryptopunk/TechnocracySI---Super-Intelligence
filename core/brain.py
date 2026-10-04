import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)


load_dotenv()


# ============================================================
# CONFIGURAÇÃO
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


if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY não encontrada no arquivo .env"
    )


# ============================================================
# CLIENTE GROQ
# ============================================================

client = AsyncOpenAI(
    api_key=GROQ_API_KEY,
    base_url=GROQ_BASE_URL,
)


# ============================================================
# TRACING
# ============================================================

set_tracing_disabled(True)


# ============================================================
# MODELO
# ============================================================

model = OpenAIChatCompletionsModel(
    model=GROQ_MODEL,
    openai_client=client,
)


# ============================================================
# IDENTIDADE DA TECHNOCRACYSI
# ============================================================

SYSTEM_CORE = """

Você é a TechnocracySI.

Você é uma inteligência artificial modular orientada a:

- raciocínio;
- investigação;
- análise;
- síntese;
- crítica;
- resolução de problemas;
- aprendizagem baseada em evidências.

PRINCÍPIOS:

1. Nunca trate uma hipótese como fato.

2. Diferencie:

   FATO
   EVIDÊNCIA
   INFERÊNCIA
   HIPÓTESE
   ESPECULAÇÃO

3. Procure contradições.

4. Procure explicações alternativas.

5. Não invente informações.

6. Quando não houver evidência suficiente,
   declare explicitamente a incerteza.

7. Divida problemas complexos em partes menores.

8. Analise as premissas antes das conclusões.

9. Priorize precisão.

10. Não invente fontes ou resultados de pesquisas.

ARQUITETURA COGNITIVA:

OBSERVAÇÃO
    ↓
EVIDÊNCIAS
    ↓
HIPÓTESES
    ↓
ANÁLISE
    ↓
CONTRA-ARGUMENTOS
    ↓
SÍNTESE
    ↓
CONCLUSÃO

IDENTIDADE:

Nome: TechnocracySI

Personalidade:

- científica;
- tecnológica;
- estratégica;
- objetiva;
- investigativa;
- sofisticada;
- futurista.

Você não deve simplesmente concordar com o usuário.

Quando o usuário estiver equivocado,
explique claramente o motivo.

Quando os dados forem insuficientes,
diga:

"Não há evidência suficiente para concluir isso."

OBJETIVO:

Aumentar a qualidade do raciocínio humano.

Você não deve fingir possuir ferramentas,
dados ou informações que não possui.
"""


# ============================================================
# AGENTE PRINCIPAL
# ============================================================

technocracysi = Agent(
    name="TechnocracySI",
    instructions=SYSTEM_CORE,
    model=model,
)


# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def ask(question: str) -> str:

    result = Runner.run_sync(
        technocracysi,
        question
    )

    return result.final_output


# ============================================================
# TERMINAL
# ============================================================

def main():

    print()
    print("=" * 72)
    print("                    TECHNOCRACYSI")
    print("                  INTELLIGENCE CORE")
    print("=" * 72)
    print()
    print("Provider : Groq")
    print("Model    :", GROQ_MODEL)
    print()
    print("Digite sua pergunta.")
    print("Digite 'exit' para sair.")
    print()

    while True:

        try:

            question = input("Você > ").strip()

            if not question:
                continue

            if question.lower() in {
                "exit",
                "quit",
                "sair"
            }:

                print()
                print("TECHNOCRACYSI encerrada.")
                break

            print()
            print("TECHNOCRACYSI processando...")
            print()

            answer = ask(question)

            print("TECHNOCRACYSI >")
            print(answer)
            print()

        except KeyboardInterrupt:

            print()
            print()
            print("TECHNOCRACYSI encerrada.")
            break

        except Exception as error:

            print()
            print("ERRO")
            print("-" * 72)
            print(type(error).__name__)
            print(str(error))
            print("-" * 72)
            print()


if __name__ == "__main__":
    main()

