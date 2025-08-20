import os
from openai import OpenAI
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv(override=True)
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("The environment variable is not set!")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

try:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

# Print the response content
if response.choices or response.choices[0].message:
    print(response.choices[0].message.content)
else:
    print("No response received.")
    exit(1)