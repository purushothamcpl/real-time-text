import streamlit as st
import speech_recognition as sr
import tempfile

st.set_page_config(page_title="Speech-to-Text", layout="centered")
st.title("🎤 Speech-to-Text (Online Version Without PyAudio / WebRTC)")

st.write("Tap below to record your voice, then convert to text.")

# Upload audio recorded from browser
audio_file = st.file_uploader("Upload recorded audio (.wav/.mp3)", type=["wav", "mp3"])

if audio_file is not None:
    st.audio(audio_file)

    recognizer = sr.Recognizer()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        temp.write(audio_file.read())
        temp_path = temp.name

    try:
        with sr.AudioFile(temp_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        st.success("📝 Transcribed Text:")
        st.write(text)
    except Exception as e:
        st.error("Could not transcribe audio.")
        st.error(str(e))
