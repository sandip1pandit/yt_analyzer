import streamlit as st
from yt import build_youtube_agent

st.title("Agno Groq Test")

agent = build_youtube_agent()

try:
    response = agent.run("Say hello and tell me which model you are using.")
    st.success("Agno is working!")
    st.write(response.content)
except Exception as e:
    st.error(f"Agno error: {e}")