import streamlit as st

from yt import build_youtube_agent, get_transcript


st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout="centered"
)

st.title("🎥 AI YouTube Video Analyzer")


@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()

video_url = st.text_input("Enter YouTube Video Link")

button = st.button("Analyze Video")


if video_url and button:

    with st.spinner("Getting transcript..."):

        try:
            transcript = get_transcript(video_url)

        except Exception as e:
            st.error(f"Could not get transcript: {e}")
            st.stop()

    with st.spinner("Analyzing video..."):

        try:
            response = agent.run(
                f"""
                Analyze this YouTube video transcript:

                {transcript}
                """
            )

            st.markdown("## Analysis Report")

            st.markdown(response.content)

        except Exception as e:
            st.error(f"Analysis failed: {e}")