import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

# --- Page Config ---
st.set_page_config(
    page_title="Buddy4U - Future starts NOW!",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
<style>
    .stApp {
        background-image: url("https://media.istockphoto.com/id/1218489981/vector/puzzled-student-making-choice-about-his-future-career-path.jpg?s=612x612&w=0&k=20&c=VDlf5Fvob5gEw_OmTxB0APi4nTjFEqFagu-mH6AKaHk=");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: #ffffff;
    }
    .block-container {
        background-color: rgba(23, 23, 56, 0.85);
        padding: 2rem;
        border-radius: 18px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
    }
    h1, h2, h3, h4, h5, h6, .stMetricLabel, .stMetricValue {
        color: #DFF3E4;
    }
    .stButton > button {
        background-color: #3423A6;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 0.6em 1.2em;
    }
</style>
""", unsafe_allow_html=True)

# --- Splash Screen ---
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.markdown("""
    <div style='text-align: center;'>
        <h1>🚀 Buddy4U - Future starts NOW!</h1>
        <p style='font-size: 20px;'>Welcome to your ASU Anti-Procrastination Companion!<br>
        Track your focus. Beat procrastination. Reach your graduation goals.</p>
    </div>
    """, unsafe_allow_html=True)

    # Using st.image() for better integration with Streamlit
    st.image("https://i.ibb.co/2dPQzSf/asu-path.png", caption="From path to graduation, each step counts!", use_column_width=True)

    if st.button("✨ Enter My Dashboard"):
        st.session_state.started = True
        switch_page("home")

    st.stop()

# Fallback content if session state fails (this shouldn't run under normal flow)
st.title("Welcome to Buddy4U!")
st.write("Please use the menu on the left to navigate.")
