import streamlit as st
from openai import OpenAI
import tempfile

st.set_page_config(page_title="Speech to Text", layout="centered")
st.title("🎤 Real-Time Speech-to-Text (Whisper API)")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

audio_file = st.file_uploader("Upload audio file (.wav/.mp3)", type=["wav", "mp3"])

if audio_file:
    st.audio(audio_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        temp.write(audio_file.read())
        temp_path = temp.name

    with open(temp_path, "rb") as f:
        st.write("⏳ Transcribing...")
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-tts",
            file=f
        )

    st.success("📝 Transcription:")
    st.write(transcript.text)
