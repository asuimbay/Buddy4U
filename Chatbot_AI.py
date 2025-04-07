# Chatbot_AI.py

import streamlit as st
import openai
from dotenv import load_dotenv
import os

# 1) Load environment variables
load_dotenv(".env")
openai_api_key = os.getenv("openai_API_KEY")
if not openai_api_key:
    st.error("API key not found. Please check API.env")
openai.api_key = openai_api_key

def run():
    st.title("Buddy4U Chatbot")

    # Initialize chat history if it doesn't exist
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # User input
    user_input = st.text_input("Type your message here:", "")

    if st.button("Send"):
        # Add user message to the history
        st.session_state["chat_history"].append({"role": "user", "content": user_input})
        
        # Send the entire conversation to OpenAI
        try:
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an AI friend for an ASU student (presume user is an ASU student) that utilizes ASU resources to help in summaries, daily check-in, and scheduling tasks."
                        )
                    }
                ] + st.session_state["chat_history"]
            )
            # Get GPT response
            gpt_msg = completion.choices[0].message.content
            # Append to history
            st.session_state["chat_history"].append({"role": "assistant", "content": gpt_msg})
        except Exception as e:
            st.error(f"Error: {e}")

    # Display conversation
    for msg in st.session_state["chat_history"]:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**AI Buddy:** {msg['content']}")

# Optional: if you run Chatbot_AI.py directly with `streamlit run Chatbot_AI.py`
if __name__ == "__main__":
    run()