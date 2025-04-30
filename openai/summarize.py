# imports
import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
project_id = os.getenv("OPENAI_PROJECT_ID")
organization_id = os.getenv("OPENAI_ORG_ID")

client = OpenAI(
    api_key = api_key,
    project=project_id,
    organization=organization_id
)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What's 2+2?"}]
)

print(response.choices[0].message.content)
