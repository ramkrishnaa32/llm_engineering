import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key and other configurations from environment variables
load_dotenv(override=True)
apiKey = os.getenv('OPENAI_API_KEY')
orgId = os.getenv('OPENAI_ORG_ID')
projectId = os.getenv('OPENAI_PROJECT_ID')

# Check if the required environment variables are set
if not apiKey or not orgId or not projectId:
    raise ValueError("API key, Organization ID, and Project ID must be set in environment variables.")

# Initialize OpenAI
client = OpenAI(
    api_key=apiKey,
    organization=orgId,
    project=projectId
)

def call_openai(prompt, model='gpt-4o-mini', temperature=0.0):
    system_message = "You are a helpful assistant"
    message = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]

    try:
        response = client.chat.completions.create(
            model = model,
            messages = message,
            temperature = temperature
        )
    except Exception as error:
        print(f"Error calling OpenAI API: {error}")
        raise error

    return response.choices[0].message.content

def stream_openai(messages, model="gpt-4o-mini", temperature=0.0):
    try:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            stream=True
        )
    except Exception as error:
        print(f"Error calling OpenAI API: {error}")
        raise error

