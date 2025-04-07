# streamlit_app.py

import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv("API.env")
openai_api_key = os.getenv("openai_API_KEY")
openai.api_key = openai_api_key

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI friend..."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

st.title("Buddy4U")
user_input = st.text_input("Type your question or message:")

if user_input:
    answer = chat_with_gpt(user_input)
    st.write("**You:**", user_input)
    st.write("**AI:**", answer)
