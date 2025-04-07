import streamlit as st
import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt

def run():
    # --- Generate Simulated Study Data ---
    today = datetime.date.today()
    dates = [today - datetime.timedelta(days=i) for i in range(29, -1, -1)]
    study_minutes = [random.choice([0, 30, 45, 60, 90]) if random.random() > 0.2 else 0 for _ in dates]

    df = pd.DataFrame({"Date": dates, "Study Minutes": study_minutes})
    df["Streak"] = df["Study Minutes"].apply(lambda x: 1 if x > 0 else 0)

    # --- Study Calculations ---
    total_minutes = df["Study Minutes"].sum()
    avg_minutes = df["Study Minutes"].mean()
    max_day = df.iloc[df["Study Minutes"].idxmax()]["Date"].strftime("%A")
    days_studied = df["Study Minutes"].astype(bool).sum()

    # --- Display Header ---
    st.title("📊 Study Insights")
    st.markdown("Track your consistency and see your study habits in action.")

    # --- Study Metrics ---
    col1, col2, col3 = st.columns(3)
    col1.metric("⏰ Total Study Time", f"{total_minutes} mins")
    col2.metric("📆 Days Studied", f"{days_studied} / 30")
    col3.metric("🔥 Top Study Day", max_day)

    # --- Line Chart for Study Time ---
    st.markdown("### 📈 Your Study Trends")
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Study Minutes"], marker='o', color='#E89C31')
    ax.set_xlabel("Date")
    ax.set_ylabel("Minutes Studied")
    ax.set_title("Study Minutes Over Time")
    ax.grid(True)
    st.pyplot(fig)

    # --- Simulated Grade Improvement ---
    st.markdown("### 🧠 Academic Performance Overview")

    weeks = [f"Week {i}" for i in range(1, 7)]
    starting_gpa = round(random.uniform(2.0, 2.8), 2)
    grade_trend = [round(starting_gpa + i * random.uniform(0.05, 0.15), 2) for i in range(6)]
    current_gpa = grade_trend[-1]
    improvement = round(current_gpa - starting_gpa, 2)

    # --- Grade Metrics ---
    col4, col5, col6 = st.columns(3)
    col4.metric("📘 Starting GPA", f"{starting_gpa}")
    col5.metric("📈 Current GPA", f"{current_gpa}")
    col6.metric("🎯 GPA Improvement", f"+{improvement}")

    # --- Grade Trend Chart ---
    fig2, ax2 = plt.subplots()
    ax2.plot(weeks, grade_trend, marker='o', color='#8C0E0F')
    ax2.set_title("GPA Trend Since Using Buddy4U")
    ax2.set_ylim(0, 4.0)
    ax2.set_ylabel("GPA")
    ax2.grid(True)
    st.pyplot(fig2)