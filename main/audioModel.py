# imports
import os
import json
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv
load_dotenv(override=True)

# Initialization
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:15]}")
else:
    print("OpenAI API Key not set")

MODEL = "gpt-4o-mini"
openai = OpenAI()

# System messag
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

def talker(message):
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",  # Also, try replacing onyx with alloy
        input=message,
    )

    audio_stream = BytesIO(response.content)
    audio = AudioSegment.from_file(audio_stream, format="mp3")
    play(audio)

talker("Well, hi there. I am your personal assistant. How can I help you?")
