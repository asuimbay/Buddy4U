# ASU Study Companion App (Streamlit Version)
# Requirements: streamlit, pandas, matplotlib, PIL

import streamlit as st
import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt
from PIL import Image

# --- App Configuration ---
st.set_page_config(page_title="ASU Anti-Procrastination Companion", layout="centered")
st.markdown("""
<style>
    .stApp {
        background-color: #fdf6f0;
    }
    h1, h2, h3 {
        color: maroon;
    }
</style>
""", unsafe_allow_html=True)

# --- Simulate Study Data ---
today = datetime.date.today()
dates = [today - datetime.timedelta(days=i) for i in range(29, -1, -1)]
study_minutes = [random.choice([0, 30, 45, 60, 90]) if random.random() > 0.2 else 0 for _ in dates]

# Build DataFrame
df = pd.DataFrame({"Date": dates, "Study Minutes": study_minutes})
df["Studied"] = df["Study Minutes"] > 0
df["Streak"] = 0

# --- Calculate Streak ---
streak = 0
for i in range(len(df)):
    if df.loc[i, "Studied"]:
        streak += 1
    else:
        streak = 0
    df.loc[i, "Streak"] = streak

# --- Procrastination Pattern Recognition ---
df["Day"] = df["Date"].apply(lambda x: x.strftime("%A"))
procrastination_days = df[df["Study Minutes"] == 0]["Day"].value_counts()
most_skipped = procrastination_days.idxmax() if not procrastination_days.empty else "None"

# --- Stats ---
current_streak = df.iloc[-1]["Streak"]
longest_streak = df["Streak"].max()
total_minutes = df["Study Minutes"].sum()
avg_minutes = df["Study Minutes"].mean()
top_day = df.iloc[df["Study Minutes"].idxmax()]["Day"]

# --- Header + Intro ---
st.image("https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/Arizona_State_University_logo.svg/1200px-Arizona_State_University_logo.svg.png", width=150)
st.title("🎓 ASU Anti-Procrastination Companion")
st.markdown("Welcome to your personalized study tracker! Stay focused, level up, and conquer procrastination.")

# --- Disney-style ASU Pathway Intro ---
st.subheader("✨ Your Journey to Graduation")
st.image("https://i.ibb.co/2dPQzSf/asu-path.png", caption="From path to graduation, each step counts!", use_column_width=True)

# --- Stats Cards ---
st.markdown("---")
st.subheader("📊 Your Study Overview")
st.metric("🔥 Current Streak", f"{int(current_streak)} Days")
st.metric("💪 Longest Streak", f"{int(longest_streak)} Days")
st.metric("📅 Most Skipped Day", most_skipped)
st.metric("⏰ Total Study Time", f"{int(total_minutes)} Minutes")

# --- Chart ---
st.markdown("### 📈 Study Trend")
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Study Minutes"], marker='o', color='maroon')
ax.set_title("Study Minutes per Day")
ax.set_xlabel("Date")
ax.set_ylabel("Minutes")
plt.xticks(rotation=45)
st.pyplot(fig)

# --- Levels Map ---
st.markdown("### 🗺️ Streak Levels Progress")
levels = [3, 5, 7, 10]
level_titles = ["📘 Level 1", "📗 Level 2", "📙 Level 3", "🎓 Graduation"]
achieved = [current_streak >= lvl for lvl in levels]
st.write(" -> ".join([f"{lvl} ✅" if ok else f"{lvl} ❌" for lvl, ok in zip(level_titles, achieved)]))

# --- AI Habit Reminder ---
if current_streak < 2:
    st.warning("You seem to be falling behind. Try a 10-minute focus task to get back on track!")
elif current_streak >= 5:
    st.success("You're crushing it! You're only a few steps away from the next reward!")

# --- Semester Wrapped ---
st.markdown("---")
st.subheader("🎉 Semester Wrapped")
st.markdown(f"- Total Hours: {total_minutes / 60:.1f} hrs\n- Average Daily Study: {avg_minutes:.1f} mins\n- Most Productive Day: {top_day}")

# --- Honourlock-like Section (Placeholder) ---
st.markdown("---")
st.subheader("🛡️ Secure Exam Mode")
st.markdown("Enable a distraction-free, monitored mode during exams or study sessions. Integration with secure tools like Honourlock can be added here.")
st.button("Activate Secure Mode")

# --- Data Table ---
st.markdown("### 🧾 Full Study Log")
st.dataframe(df[["Date", "Study Minutes", "Streak"]].reset_index(drop=True))
