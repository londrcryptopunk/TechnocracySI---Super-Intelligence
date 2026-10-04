import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv


# ============================================================
# TECHNOCRACYSI
# SUPER INTELLIGENCE SYSTEM
# ============================================================

ROOT = Path(__file__).resolve().parent


# ============================================================
# LOCALIZAÇÃO DAS IMAGENS
# ============================================================

def encontrar_imagem(nome):
    candidatos = [
        ROOT / "assets" / nome,
        ROOT / nome,
    ]

    for caminho in candidatos:
        if caminho.exists():
            return caminho

    return None


CAPA = encontrar_imagem("capa 1.jpg")
LOGO = encontrar_imagem("logo 1.jpg")


# ============================================================
# AMBIENTE
# ============================================================

load_dotenv(ROOT / ".env")


# ============================================================
# STREAMLIT SECRETS
# ============================================================

try:
    secrets = st.secrets

    if "GROQ_API_KEY" in secrets:
        os.environ["GROQ_API_KEY"] = str(
            secrets["GROQ_API_KEY"]
        )

    if "GROQ_BASE_URL" in secrets:
        os.environ["GROQ_BASE_URL"] = str(
            secrets["GROQ_BASE_URL"]
        )

    if "GROQ_MODEL" in secrets:
        os.environ["GROQ_MODEL"] = str(
            secrets["GROQ_MODEL"]
        )

except Exception:
    pass


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="TechnocracySI",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# LOGO
# ============================================================

if LOGO is not None:

    st.logo(
        str(LOGO),
        icon_image=str(LOGO)
    )


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {

    background:
        radial-gradient(
            circle at 50% -20%,
            #1b1b1b 0%,
            #090909 35%,
            #030303 75%,
            #000000 100%
        );

    color: #eeeeee;
}


[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}


section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #090909 0%,
            #030303 100%
        );

    border-right: 1px solid #222222;
}


.tech-title {

    text-align: center;

    font-size: 4rem;

    font-weight: 800;

    letter-spacing: 0.18em;

    color: #f4f4f4;

    text-shadow:
        0 0 8px rgba(255,255,255,0.20),
        0 0 30px rgba(255,255,255,0.08);

    margin-top: 1rem;

    margin-bottom: 0;
}


.tech-subtitle {

    text-align: center;

    color: #777777;

    font-size: 0.78rem;

    letter-spacing: 0.42em;

    margin-top: 0.5rem;

    margin-bottom: 2.5rem;
}


.system-status {

    border: 1px solid #252525;

    background:
        linear-gradient(
            180deg,
            #0d0d0d,
            #050505
        );

    border-radius: 10px;

    padding: 0.8rem;

    text-align: center;

    color: #cfcfcf;

    font-size: 0.72rem;

    letter-spacing: 0.15em;
}


.agent-card {

    background:
        linear-gradient(
            145deg,
            #0d0d0d,
            #050505
        );

    border: 1px solid #222222;

    border-radius: 12px;

    padding: 1.2rem;

    min-height: 130px;

    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.025),
        0 8px 30px rgba(0,0,0,0.35);
}


.agent-title {

    font-size: 0.85rem;

    font-weight: 700;

    letter-spacing: 0.16em;

    color: #eeeeee;

    margin-bottom: 0.7rem;
}


.agent-description {

    color: #777777;

    font-size: 0.76rem;

    line-height: 1.5;
}


.hero-frame {

    border: 1px solid #222222;

    border-radius: 14px;

    overflow: hidden;

    background: #050505;

    box-shadow:
        0 15px 50px rgba(0,0,0,0.55);

    margin-top: 1rem;

    margin-bottom: 1rem;
}


[data-testid="stChatMessage"] {

    background: #070707;

    border: 1px solid #1c1c1c;

    border-radius: 12px;
}


.tech-footer {

    text-align: center;

    color: #444444;

    font-size: 0.65rem;

    letter-spacing: 0.2em;

    margin-top: 3rem;

    padding-bottom: 1rem;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    if LOGO is not None:

        st.image(
            str(LOGO),
            width=180
        )

    st.markdown(
        "## TECHNOCRACYSI"
    )

    st.caption(
        "SUPER INTELLIGENCE SYSTEM"
    )

    st.divider()

    st.markdown(
        "### SYSTEM"
    )

    st.markdown(
        """
**STATUS**

● ONLINE

**ARCHITECTURE**

Research → Analysis → Critic → Synthesis
"""
    )

    st.divider()

    st.markdown(
        "### CORE"
    )

    st.markdown(
        """
`RESEARCH`

↓

`ANALYSIS`

↓

`CRITIC`

↓

`SYNTHESIS`
"""
    )


# ============================================================
# HEADER PRINCIPAL
# ============================================================

st.markdown(
    '<div class="tech-title">TECHNOCRACYSI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tech-subtitle">'
    'SUPER INTELLIGENCE SYSTEM'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# STATUS
# ============================================================

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.markdown(
        """
<div class="system-status">
● SYSTEM ONLINE
</div>
""",
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        """
<div class="system-status">
RESEARCH
</div>
""",
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        """
<div class="system-status">
ANALYSIS
</div>
""",
        unsafe_allow_html=True
    )


with c4:

    st.markdown(
        """
<div class="system-status">
SYNTHESIS
</div>
""",
        unsafe_allow_html=True
    )


st.write("")


# ============================================================
# AGENTES
# ============================================================

a1, a2, a3, a4 = st.columns(4)


with a1:

    st.markdown(
        """
<div class="agent-card">

<div class="agent-title">
RESEARCHER
</div>

<div class="agent-description">
Pesquisa, coleta e organiza evidências
relevantes para o problema.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with a2:

    st.markdown(
        """
<div class="agent-card">

<div class="agent-title">
ANALYST
</div>

<div class="agent-description">
Examina relações, padrões, hipóteses
e possíveis explicações.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with a3:

    st.markdown(
        """
<div class="agent-card">

<div class="agent-title">
CRITIC
</div>

<div class="agent-description">
Procura contradições, inconsistências
e pontos fracos.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with a4:

    st.markdown(
        """
<div class="agent-card">

<div class="agent-title">
SYNTHESIZER
</div>

<div class="agent-description">
Integra os resultados e produz
a síntese final.
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# CAPA
# ============================================================

st.write("")


if CAPA is not None:

    st.markdown(
        '<div class="hero-frame">',
        unsafe_allow_html=True
    )

    st.image(
        str(CAPA),
        width="stretch"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CÉREBRO
# ============================================================

try:

    from core.brain import ask

except Exception:

    ask = None


# ============================================================
# MEMÓRIA DA SESSÃO
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# HISTÓRICO
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# ENTRADA
# ============================================================

prompt = st.chat_input(
    "Digite uma questão para a TechnocracySI..."
)


# ============================================================
# PROCESSAMENTO
# ============================================================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)


    with st.chat_message("assistant"):

        with st.spinner(
            "TECHNOCRACYSI PROCESSANDO..."
        ):

            if ask is None:

                response = (
                    "A TechnocracySI está "
                    "temporariamente indisponível."
                )

            else:

                try:

                    response = ask(prompt)

                    response = str(response)

                except Exception:

                    response = (
                        "Não foi possível processar "
                        "esta solicitação neste momento."
                    )


            st.markdown(response)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="tech-footer">

TECHNOCRACYSI ·
SUPER INTELLIGENCE SYSTEM

</div>
""",
    unsafe_allow_html=True
)
