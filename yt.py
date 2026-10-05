import re
from textwrap import dedent

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

from agno.agent import Agent
from agno.models.groq import Groq

load_dotenv()


def get_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/|shorts/)([^&?/]+)", url)

    if not match:
        raise ValueError("Invalid YouTube URL")

    return match.group(1)


def get_transcript(url):
    video_id = get_video_id(url)

    api = YouTubeTranscriptApi()

    transcript = api.fetch(
        video_id,
        languages=["en-US", "en"]
    )

    return " ".join(snippet.text for snippet in transcript)


def build_youtube_agent():
    return Agent(
        name="YouTube Agent",
        model=Groq(id="openai/gpt-oss-120b"),
        instructions=dedent("""
            You are an expert YouTube content analyst.

            Analyze the provided YouTube transcript.

            Provide:

            1. Video Overview
            - Main topic
            - Type of video
            - Short summary

            2. Main Topics
            - Identify the major topics discussed
            - Explain each topic clearly

            3. Important Points
            - List the most important ideas
            - Mention useful examples and demonstrations

            4. Timestamp Analysis
            - Create timestamps only when timestamp information
              is actually available.
            - Never invent timestamps.

            5. Key Takeaways
            - Give the most important lessons from the video.

            Be accurate and do not hallucinate information.
        """),
        markdown=True,
    )