# imports
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import ollama
import os

load_dotenv(override=True)
apiKey = os.getenv('OPENAI_API_KEY')
orgId = os.getenv('OPENAI_ORG_ID')
projectId = os.getenv('OPENAI_PROJECT_ID')

if not apiKey or not orgId or not projectId:
    raise ValueError("API key, Organization ID, and Project ID must be set in environment variables.")

# Initialize OpenAI
client = OpenAI(
    api_key=apiKey,
    organization=orgId,
    project=projectId
)

# constants
MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

# here is the question; type over this to ask something new
question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

# prompts
system_prompt = "You are a helpful technical tutor who answers questions about python code, software engineering, data science and LLMs"
user_prompt = "Please give a detailed explanation to the following question: " + question

# messages
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# Get gpt-4o-mini to answer, with streaming
response = client.chat.completions.create(model=MODEL_GPT, messages=messages)
result = response.choices[0].message.content
print(result)

# Get Llama 3.2 to answer
response = ollama.chat(model=MODEL_LLAMA, messages=messages)
reply = response['message']['content']
print(reply)