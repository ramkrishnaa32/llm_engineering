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

# Image generation function
import base64
from io import BytesIO
from PIL import Image

def artist(prompt: str):
    image_response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        n=1,
        response_format="b64_json",
    )

    image_base64 = image_response.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    return Image.open(BytesIO(image_data))

# Example usage:
# prompt = """An artistic digital illustration of a traditional Vedic astrology Kundli (birth chart), "
#           "with twelve houses arranged in a square pattern, filled with zodiac symbols and cosmic details. The design should be elegant, mystical,
#           and glowing with golden and celestial tones, with a subtle starry background."""

# prompt = """A professional astrologer sitting at a desk, carefully analyzing a Kundli (Vedic astrology birth chart) on a paper scroll and a laptop screen.
# The background shows bookshelves with astrology books, planets, and zodiac posters. The atmosphere is calm, spiritual, and scholarly."""

prompt = """
"An astrologer on a video call, holding a Kundli chart in front of the camera, with a neat background showing cosmic artwork and zodiac symbols, 
representing an online astrology consultation.
"""

marriage_prompt = """"An experienced astrologer in traditional attire, carefully evaluating a Kundli (Vedic birth chart) for marriage compatibility. 
The astrologer is seated with sacred texts, candles, and zodiac symbols around, 
while two overlapping Kundli charts are shown on the table, symbolizing a couple’s compatibility.
"""

one_to_one_prompt = """"An astrologer explaining a Kundli chart for marriage compatibility to a couple, 
with the chart visible on a tablet screen. The background has subtle astrological symbols, giving the feel of an online consultation session."""

astrologer_banner = """A minimal yet premium hero banner background with an astrology theme. Smooth gradient backdrop (deep navy blending into soft purple), 
with faint golden constellations, zodiac wheel outlines, and subtle planetary orbits. Modern, elegant, and calming — leaving ample empty space for text and buttons. 
The style should feel trustworthy, futuristic, and professional, avoiding clutter or cartoonish details."""

image = artist(astrologer_banner)
image.show()
