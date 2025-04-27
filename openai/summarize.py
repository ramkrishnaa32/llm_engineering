# imports

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
import openai

my_api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-kIXSuk9NH3eKkkCNipsd2NYQ"

print(f"Using API key --> {my_api_key} <--")

openai = OpenAI()
completion = openai.chat.completions.create(
    model='gpt-4.1',
    messages=[{"role":"user", "content": "What's 2+2?"}],
)
print(completion.choices[0].message.content)
