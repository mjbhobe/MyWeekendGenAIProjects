import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from utils import get_video_id, get_transcript, get_summary

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# -------------------------------------------------------------------

st.set_page_config(
    page_title="Generative AI Video Transcriber",
    page_icon="✨",
)

st.title("YouTube Video Transcriber 📽️💬")

video_url = st.text_input(
    "Enter (or paste) YouTube Video URL into text box below and press Enter to transcribe & summarize it:"
)


if video_url:
    video_id = get_video_id(video_url)

    if video_id:
        try:
            st.video(video_url)
            with st.spinner("Generating transcript & summary..."):
                transcript = get_transcript(video_id)
                summary = get_summary(transcript)
            
            # transcript = YouTubeTranscriptApi.get_transcript(video_id)
            # full_transcript = " ".join(
            #     [entry["text"] for entry in transcript]
            # )  # Combine into one string
            # st.write("Transcript:")
            # st.write(full_transcript)  # Display the transcript in Streamlit
            #st.markdown("---")
            with st.expander("Video Transcript", expanded=False):
                st.write(transcript)
            st.markdown("---")
            st.markdown(
                f"<h2 style='color=skyblue;'>Summary</h2>",
                unsafe_allow_html=True,
            )
            st.write(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    elif video_url:
        st.error("Invalid YouTube URL. Please enter a valid URL.")
