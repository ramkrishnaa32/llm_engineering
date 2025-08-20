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

def call_openai(prompt, model='gpt-4o-mini'):
    """
    Call the OpenAI API with the given prompt and model.
    Args:
        prompt (str): The input prompt for the OpenAI API.
        model (str): The model to use for the API call.

    Returns:
        str: The response from the OpenAI API.
    """
    try:
        response = client.chat.completions.create(
            model = model,
            messages = prompt
        )
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

    return response.choices[0].message.content