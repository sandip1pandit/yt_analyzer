import streamlit as st
from yt import build_youtube_agent
import os
st.write("GROQ key exists:", bool(os.getenv("GROQ_API_KEY")))
st.write("GROQ key prefix:", os.getenv("GROQ_API_KEY", "")[:4])
st.write("GROQ key length:", len(os.getenv("GROQ_API_KEY", "")))

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

st.title("🎥 AI Youtube Video Analyzer")


@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()

# input box
video_url = st.text_input("Enter Youtube Video Link") # str
button = st.button("Analyze Video") # True/False

if video_url and button:
    with st.spinner("Analyzing video...."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)