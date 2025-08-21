import anthropic
from anthropic import APIError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)
api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key is None:
    raise ValueError("The environment variable ANTHROPIC_API_KEY is not set!")

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=api_key)

def call_claude(prompt, model="claude-opus-4-1-20250805", max_tokens=1000, temperature=0.0):
    """
    Call Claude API with error handling
    Args:
        prompt (str): The user prompt
        model (str): The model to use
        max_tokens (int): Maximum tokens in response
    Returns:
        str: Claude's response or error message
    """
    try:
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return message.content[0].text

    except APIError as e:
        return f"API Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
