import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import speech_recognition as sr
import av
import numpy as np

st.title("🎤 Real-Time Speech-to-Text (Online Version)")

text_box = st.empty()

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recv_audio(self, frame: av.AudioFrame):
        audio = frame.to_ndarray()
        sample_rate = frame.sample_rate

        try:
            audio_data = sr.AudioData(audio.tobytes(), sample_rate, 2)
            text = self.recognizer.recognize_google(audio_data)
            text_box.markdown(f"### 📝 {text}")
        except:
            pass

        return frame

webrtc_streamer(
    key="speech",
    mode="recvonly",
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"audio": True, "video": False}
)
