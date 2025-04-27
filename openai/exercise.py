# imports
import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display

# Constants
OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

# Create a messages list using the same format that we used for OpenAI
messages = [
    {"role": "user", "content": "Describe some of the business applications of Generative AI"}
]

payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
print(response.json()['message']['content'])

import ollama

response = ollama.chat(model=MODEL, messages=messages)
print(response['message']['content'])

from openai import OpenAI
ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

response = ollama_via_openai.chat.completions.create(
    model=MODEL,
    messages=messages
)

print(response.choices[0].message.content)

response = ollama_via_openai.chat.completions.create(
    model="deepseek-r1:1.5b",
    messages=[{"role": "user", "content": "Please give definitions of some core concepts behind LLMs: a neural network, attention and the transformer"}]
)

print(response.choices[0].message.content)