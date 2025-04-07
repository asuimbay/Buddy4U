# main.py

import streamlit as st
import importlib.util
import base64

# --- Page Config ---
st.set_page_config(
    page_title="Buddy4U - Future starts NOW!",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Function to dynamically load modules ---
def load_module(path):
    spec = importlib.util.spec_from_file_location("page", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# --- Load Tabs ---
Home       = load_module("Home.py")
Insights   = load_module("Insights.py")
Semester   = load_module("SemesterWrapped.py")
Exam       = load_module("ExamMode.py")
Chatbot    = load_module("Chatbot_AI.py")  # <-- New "chat" tab

# --- If we haven't chosen a tab, default to 'home' ---
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "home"

# --- Read ?tab=xxx from the URL (optional). Could skip if you don't need direct linking ---
url_tab = st.experimental_get_query_params().get("tab")
if url_tab:
    st.session_state.current_tab = url_tab[0]

# --- Render the chosen tab ---
if st.session_state.current_tab == "home":
    Home.run()
elif st.session_state.current_tab == "insights":
    Insights.run()
elif st.session_state.current_tab == "semester":
    Semester.run()
elif st.session_state.current_tab == "exam":
    Exam.run()
elif st.session_state.current_tab == "chat":
    Chatbot.run()  # <-- Renders your in-page Chatbot

# --- Bottom Nav Bar (existing code) ---
st.markdown("""
<style>
    /* Overall BG */
    .stApp {
        background-color: #031B28;
        color: #ffffff;
    }
    .block-container {
        padding-bottom: 7rem;
    }
    /* Bottom Nav */
    .bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 70px;
        background-color: #ffffff;
        border-top: 2px solid #ccc;
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 9999;
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
    }
    .nav-button {
        background: none;
        border: none;
        font-size: 12px;
        color: #031B28;
        text-align: center;
        margin: 0 10px;
        cursor: pointer;
    }
    .nav-button span {
        display: block;
        font-size: 18px;
    }
    .active {
        color: #E89C31;
        font-weight: bold;
    }
</style>
<div class="bottom-nav">
    <form action="" method="GET">
        <button name="tab" value="home" 
                class="nav-button {{ 'active' if st.session_state.current_tab == 'home' else '' }}">
            <span>🏠</span>Home
        </button>
    </form>
    <form action="" method="GET">
        <button name="tab" value="insights" 
                class="nav-button {{ 'active' if st.session_state.current_tab == 'insights' else '' }}">
            <span>📊</span>Insights
        </button>
    </form>
    <form action="" method="GET">
        <button name="tab" value="semester" 
                class="nav-button {{ 'active' if st.session_state.current_tab == 'semester' else '' }}">
            <span>🎓</span>Semester
        </button>
    </form>
    <form action="" method="GET">
        <button name="tab" value="exam" 
                class="nav-button {{ 'active' if st.session_state.current_tab == 'exam' else '' }}">
            <span>🧪</span>Exam
        </button>
    </form>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([0.85, 1])
# 1) Create the normal Streamlit button for chat
with col2:
    bubble_clicked = st.button("💬", key="bubble_to_chat")
if bubble_clicked:
    st.session_state.current_tab = "chat"
    st.experimental_set_query_params(tab="chat")

# 2) Inject CSS for the floating chat button (on the right)
st.markdown(f"""
<style>
div.stButton > button#bubble_to_chat {{
    position: fixed;
    bottom: 70px;
    right: 30px;  /* Chat button on the right */
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: #E89C31;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    color: #ffffff;
    font-size: 24px;
    border: none;
    cursor: pointer;
    z-index: 9999;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    overflow: hidden; /* Ensure the pseudo-element stays within the button */
}}

div.stButton > button#bubble_to_chat:hover {{
    background-color: #FAAA55;
}}

/* Add a pulsating dot to simulate "thinking" */
div.stButton > button#bubble_to_chat::after {{
    content: "";
    position: absolute;
    bottom: -12px;  /* Adjust to position the dot just below the button */
    left: 50%;
    transform: translateX(-50%);
    width: 10px;
    height: 10px;
    background-color: #ffffff;
    border-radius: 50%;
    animation: pulse 1.5s infinite;
}}

@keyframes pulse {{
    0% {{
        transform: translateX(-50%) scale(1);
        opacity: 0.8;
    }}
    50% {{
        transform: translateX(-50%) scale(1.5);
        opacity: 0.3;
    }}
    100% {{
        transform: translateX(-50%) scale(1);
        opacity: 0.8;
    }}
}}
</style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([0.65, 1])
with col2:
    st.image("./Chatbot2.jpg") 