import os
import streamlit as st
from groq import Groq

st.title("Groq Test")

api_key = os.getenv("GROQ_API_KEY")

st.write("Key exists:", bool(api_key))
st.write("Key prefix:", api_key[:4] if api_key else "None")
st.write("Key length:", len(api_key) if api_key else 0)

try:
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": "Say hello"}
        ],
    )

    st.success("Groq API is working!")
    st.write(response.choices[0].message.content)

except Exception as e:
    st.error(f"Groq authentication failed: {e}")