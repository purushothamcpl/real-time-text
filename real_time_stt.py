import os
os.environ["PYTHONUNBUFFERED"] = "1"

import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import speech_recognition as sr
import av

st.set_page_config(page_title="Real-Time Speech-to-Text", layout="wide")
st.title("🎤 Real-Time Speech-to-Text (Online Version)")

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recv_audio(self, frames, sample_rate):
        audio = av.AudioFrame.from_ndarray(frames.to_ndarray(), layout="mono")
        data = audio.to_ndarray().tobytes()

        try:
            # recognize speech from audio chunk
            audio_data = sr.AudioData(data, sample_rate, 2)
            text = self.recognizer.recognize_google(audio_data)
            st.write("📝 Text:", text)
        except:
            pass

        return frames

webrtc_streamer(
    key="speech",
    mode="recvonly",
    audio_processor_factory=AudioProcessor
)
