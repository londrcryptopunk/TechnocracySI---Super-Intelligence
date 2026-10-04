import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv


# ============================================================
# CAMINHOS DO PROJETO
# ============================================================

ROOT = Path(__file__).resolve().parent

ASSETS = ROOT / "assets"

CAPA = ASSETS / "capa 1.jpg"
LOGO = ASSETS / "logo 1.jpg"


# ============================================================
# CONFIGURAÇÃO
# ============================================================

load_dotenv(ROOT / ".env")


# ============================================================
# STREAMLIT CLOUD SECRETS
# ============================================================

try:

    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = str(
            st.secrets["GROQ_API_KEY"]
        )

    if "GROQ_MODEL" in st.secrets:
        os.environ["GROQ_MODEL"] = str(
            st.secrets["GROQ_MODEL"]
        )

    if "GROQ_BASE_URL" in st.secrets:
        os.environ["GROQ_BASE_URL"] = str(
            st.secrets["GROQ_BASE_URL"]
        )

except Exception:
    pass


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
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

if LOGO.exists():

    st.logo(
        str(LOGO),
        icon_image=str(LOGO)
    )


# ============================================================
# ESTILO
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       BASE
       ====================================================== */

    .stApp {

        background:
            radial-gradient(
                circle at 50% -20%,
                #1a1a1a 0%,
                #090909 35%,
                #030303 75%,
                #000000 100%
            );

        color: #eeeeee;
    }


    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }


    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #080808 0%,
                #030303 100%
            );

        border-right: 1px solid #202020;
    }


    /* ======================================================
       TITULO
       ====================================================== */

    .tech-title {

        text-align: center;

        font-size: 4rem;

        font-weight: 800;

        letter-spacing: 0.18em;

        color: #f2f2f2;

        text-shadow:
            0 0 8px rgba(255,255,255,0.20),
            0 0 30px rgba(255,255,255,0.08);

        margin-top: 1rem;

        margin-bottom: 0;
    }


    .tech-subtitle {

        text-align: center;

        color: #666666;

        font-size: 0.75rem;

        letter-spacing: 0.45em;

        margin-top: 0.5rem;

        margin-bottom: 2.5rem;
    }


    /* ======================================================
       STATUS
       ====================================================== */

    .system-status {

        border: 1px solid #252525;

        background:
            linear-gradient(
                180deg,
                #0c0c0c,
                #050505
            );

        border-radius: 10px;

        padding: 0.8rem;

        text-align: center;

        color: #bdbdbd;

        font-size: 0.72rem;

        letter-spacing: 0.15em;

        box-shadow:
            0 0 25px rgba(255,255,255,0.025);

        transition: all 0.2s ease;
    }


    .system-status:hover {

        border-color: #444444;

        box-shadow:
            0 0 30px rgba(255,255,255,0.06);
    }


    /* ======================================================
       AGENTES
       ====================================================== */

    .agent-card {

        background:
            linear-gradient(
                145deg,
                #0c0c0c,
                #050505
            );

        border: 1px solid #202020;

        border-radius: 12px;

        padding: 1.2rem;

        min-height: 125px;

        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.025),
            0 8px 30px rgba(0,0,0,0.35);

        transition:
            transform 0.2s ease,
            border-color 0.2s ease;
    }


    .agent-card:hover {

        transform: translateY(-2px);

        border-color: #3a3a3a;
    }


    .agent-title {

        font-size: 0.85rem;

        font-weight: 700;

        letter-spacing: 0.16em;

        color: #e5e5e5;
    }


    .agent-description {

        color: #666666;

        font-size: 0.76rem;

        margin-top: 0.7rem;

        line-height: 1.5;
    }


    /* ======================================================
       IMAGEM DA CAPA
       ====================================================== */

    .hero-frame {

        border: 1px solid #202020;

        border-radius: 14px;

        overflow: hidden;

        background: #050505;

        box-shadow:
            0 15px 50px rgba(0,0,0,0.5);

        margin-top: 1rem;

        margin-bottom: 1rem;
    }


    /* ======================================================
       CHAT
       ====================================================== */

    [data-testid="stChatMessage"] {

        background: #070707;

        border: 1px solid #1c1c1c;

        border-radius: 12px;
    }


    [data-testid="stChatInput"] {

        border-color: #292929 !important;
    }


    /* ======================================================
       DIVISORES
       ====================================================== */

    hr {

        border-color: #1c1c1c !important;
    }


    /* ======================================================
       BOTÕES
       ====================================================== */

    .stButton > button {

        background: #0b0b0b;

        color: #dddddd;

        border: 1px solid #292929;

        border-radius: 8px;
    }


    .stButton > button:hover {

        border-color: #555555;

        color: white;

        background: #111111;
    }


    /* ======================================================
       FOOTER
       ====================================================== */

    .tech-footer {

        text-align: center;

        color: #3f3f3f;

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

    if LOGO.exists():

        st.image(
            str(LOGO),
            width=180
        )

    st.markdown("## TECHNOCRACYSI")

    st.caption(
        "COGNITIVE INTELLIGENCE SYSTEM"
    )

    st.divider()

    st.markdown("### SYSTEM")

    st.markdown(
        """
        **STATUS**

        ● ONLINE

        **ENGINE**

        Groq / OpenAI-compatible

        **ARCHITECTURE**

        Research → Analysis → Critic → Synthesis
        """
    )

    st.divider()

    st.markdown("### CORE")

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

    st.divider()

    model_name = os.getenv(
        "GROQ_MODEL",
        "modelo não configurado"
    )

    st.caption(
        f"MODEL: {model_name}"
    )


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    '<div class="tech-title">TECHNOCRACYSI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tech-subtitle">'
    'COGNITIVE INTELLIGENCE SYSTEM'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# STATUS
# ============================================================

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.markdown(
        '<div class="system-status">'
        '● SYSTEM ONLINE'
        '</div>',
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        '<div class="system-status">'
        'RESEARCH'
        '</div>',
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        '<div class="system-status">'
        'ANALYSIS'
        '</div>',
        unsafe_allow_html=True
    )


with c4:

    st.markdown(
        '<div class="system-status">'
        'SYNTHESIS'
        '</div>',
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


if CAPA.exists():

    st.markdown(
        '<div class="hero-frame">',
        unsafe_allow_html=True
    )

    st.image(
        str(CAPA),
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

else:

    st.warning(
        "Capa não encontrada: assets/capa 1.jpg"
    )


# ============================================================
# CHAT
# ============================================================

st.write("")

st.divider()


from core.brain import ask


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

            try:

                response = ask(prompt)

                if response is None:

                    response = (
                        "O sistema não retornou "
                        "uma resposta."
                    )

                response = str(response)

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                error_message = (
                    "### ERRO DO SISTEMA\n\n"
                    f"`{type(e).__name__}: {e}`"
                )

                st.error(
                    error_message
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="tech-footer">

        TECHNOCRACYSI ·
        COGNITIVE INTELLIGENCE SYSTEM

    </div>
    """,
    unsafe_allow_html=True
)
