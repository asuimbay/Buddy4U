import streamlit as st
import time

def run():
    # ⚠️ Remove page config line since it's already in main.py
    # st.set_page_config(page_title="Buddy4U | Secure Exam Mode")

    # --- Page Title ---
    st.title("🛡️ Secure Exam Mode")
    st.markdown("""
    Enable a distraction-free, monitored mode for high-focus study or exam sessions.  
    Simulates integration with tools like **Honourlock** or **LockDown Browser**.
    """)

    # --- Focus Simulation ---
    st.markdown("---")
    focus_time = st.slider("🕒 Select focus duration (minutes):", min_value=5, max_value=90, step=5, value=25)

    if st.button("🚨 Activate Secure Mode"):
        with st.spinner(f"Launching distraction-free mode for {focus_time} minutes..."):
            time.sleep(2)
        st.success("✅ Secure Exam Mode is now active.")
        st.balloons()

        st.markdown(f"""
        ### ✍️ You're in Secure Mode!
        - ✅ Webcam simulated as active  
        - ✅ Screen locked  
        - ✅ Notifications muted (simulated)  
        - ⏳ Focus timer running: **{focus_time} minutes**
        """)

        st.info("Tip: Avoid switching tabs to stay focused!")

    else:
        st.warning("🔐 Secure Mode is off. Activate it to begin a distraction-free session.")

    # --- Footer Info ---
    st.markdown("---")
    st.caption("Note: For full proctoring features, integration with your university's system is required.")