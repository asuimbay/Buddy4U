import streamlit as st
from datetime import datetime
import random

def run():
    # --- Dynamic Greeting ---
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning ☀️"
    elif current_hour < 18:
        greeting = "Good afternoon 🌤️"
    else:
        greeting = "Good evening 🌙"

    st.title(f"🎓 {greeting} and welcome to Buddy4U!")
    st.subheader("Your AI-powered anti-procrastination companion 💡")

    # --- Motivational Image ---
    st.image("./Home_img.jpg", caption="From path to graduation, each step counts!", use_column_width=True)

    # --- Study Streak Bar ---
    st.markdown("### 📅 Current Study Streak")
    current_streak = random.randint(3, 10)  # Replace with real data later
    st.progress(current_streak / 30)  # Progress bar out of 30 days
    st.info(f"You've studied {current_streak} days in a row. Keep it going! 💪")

    # --- Quick Productivity Tips ---
    st.markdown("### 🧠 Quick Tips to Stay on Track")
    tips = [
        "Use the Pomodoro technique: 25 mins focus, 5 mins break.",
        "Block social media with extensions like StayFocusd.",
        "Start with the hardest task first (Eat That Frog!).",
        "Review your to-do list each morning.",
        "Break big tasks into small steps to reduce overwhelm."
    ]
    st.success(random.choice(tips))  # Show a random tip

    # --- Mood Check-In ---
    st.markdown("### ❤️ How are you feeling today?")
    mood = st.radio("Select your current mood:", ["😊 Great", "😐 Okay", "😔 Struggling"])
    if mood == "😊 Great":
        st.success("Awesome! Keep riding that momentum! 🚀")
    elif mood == "😐 Okay":
        st.warning("You're doing alright — try a quick walk or water break!")
    else:
        st.error("It's okay to have off days. Try focusing on just 1 small win today 💛")

    # --- Section Divider ---
    st.markdown("---")

    # --- Navigation Buttons (switching tabs) ---
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📊 View My Insights"):
            st.session_state.current_tab = "insights"
    with col2:
        if st.button("🎯 Enter Exam Mode"):
            st.session_state.current_tab = "exam"
    with col3:
        if st.button("🎓 Semester Progress"):
            st.session_state.current_tab = "semester"

    # --- Motivational Quote ---
    st.markdown("---")
    st.info("\"Discipline is the bridge between goals and accomplishment.\" – Jim Rohn")
