import os
import streamlit as st


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
# CARREGAR SECRET DA STREAMLIT
# ============================================================

if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

if "GROQ_MODEL" in st.secrets:
    os.environ["GROQ_MODEL"] = st.secrets["GROQ_MODEL"]

if "GROQ_BASE_URL" in st.secrets:
    os.environ["GROQ_BASE_URL"] = st.secrets["GROQ_BASE_URL"]


# Importar somente depois das variáveis existirem
from core.brain import ask


# ============================================================
# CSS — TECHNOCRACYSI
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(60,60,60,0.20),
                transparent 38%
            ),
            #050505;
        color: #e8e8e8;
    }

    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }

    [data-testid="stSidebar"] {
        background: #080808;
        border-right: 1px solid #202020;
    }

    .tech-title {
        font-family: Arial, sans-serif;
        font-size: 42px;
        font-weight: 700;
        letter-spacing: 8px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 0px;
    }

    .tech-subtitle {
        text-align: center;
        color: #777;
        letter-spacing: 5px;
        font-size: 11px;
        margin-bottom: 35px;
    }

    .status {
        text-align: center;
        color: #aaa;
        font-size: 11px;
        letter-spacing: 3px;
        margin-bottom: 25px;
    }

    .status-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #d9d9d9;
        margin-right: 8px;
        box-shadow: 0 0 12px rgba(255,255,255,0.7);
    }

    .panel {
        background: rgba(12,12,12,0.85);
        border: 1px solid #222;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }

    .panel-title {
        font-size: 11px;
        letter-spacing: 3px;
        color: #777;
        margin-bottom: 10px;
    }

    .agent-card {
        background: #0c0c0c;
        border: 1px solid #202020;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }

    .agent-name {
        font-size: 12px;
        letter-spacing: 2px;
        color: #aaa;
    }

    .agent-state {
        margin-top: 8px;
        font-size: 10px;
        color: #666;
    }

    .response {
        background: #090909;
        border-left: 2px solid #777;
        padding: 20px;
        border-radius: 4px;
        line-height: 1.7;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## TECHNOCRACYSI")

    st.markdown("---")

    st.markdown("### COGNITIVE CORE")

    st.markdown(
        """
        **● CORE ONLINE**

        **● REASONING**

        **● ANALYSIS**

        **● SYNTHESIS**

        **● CRITIQUE**
        """
    )

    st.markdown("---")

    st.markdown("### ENGINE")

    st.caption(
        os.getenv(
            "GROQ_MODEL",
            "openai/gpt-oss-120b"
        )
    )

    st.markdown("---")

    st.caption("TechnocracySI 0.2.0")

    st.caption("Experimental Intelligence Platform")


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="tech-title">TECHNOCRACYSI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tech-subtitle">COGNITIVE INTELLIGENCE SYSTEM</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="status">
        <span class="status-dot"></span>
        SYSTEM ONLINE
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# AGENTS
# ============================================================

cols = st.columns(4)

agents = [
    ("RESEARCH", "EVIDENCE"),
    ("ANALYSIS", "REASONING"),
    ("CRITIC", "VERIFICATION"),
    ("SYNTHESIS", "CONCLUSION"),
]

for col, (name, function) in zip(cols, agents):

    with col:

        st.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-name">{name}</div>
                <div class="agent-state">● {function}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown("")


# ============================================================
# CHAT
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


prompt = st.chat_input(
    "Digite uma questão para a TechnocracySI..."
)


if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner(
            "TECHNOCRACYSI ANALISANDO..."
        ):

            try:

                response = ask(prompt)

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                    }
                )

            except Exception as error:

                error_message = (
                    "Não foi possível concluir a operação.\n\n"
                    f"`{type(error).__name__}: {error}`"
                )

                st.error(error_message)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "TECHNOCRACYSI • Cognitive Intelligence System"
)
