import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="Speech-to-Text App", layout="centered")
st.title("🎤 Speech-to-Text (Tap to Record)")

recognizer = sr.Recognizer()

if st.button("🎙 Start Recording"):
    with st.spinner("Listening..."):
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        st.write("⏳ Processing...")
        try:
            text = recognizer.recognize_google(audio)
            st.success("📝 Text: " + text)
        except:
            st.error("❌ Could not understand audio")
