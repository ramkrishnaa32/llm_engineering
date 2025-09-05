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
    system_message = "You are a helpful assistant"
    try:
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_message,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return message.content[0].text

    except APIError as e:
        raise f"API Error: {e}"
    except Exception as e:
        raise f"Unexpected error: {e}"

def stream_claude(prompt, model="claude-opus-4-1-20250805", max_tokens=1000, temperature=0.0):
    system_message = "You are a helpful assistant"
    try:
        response = client.messages.stream(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_message,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        result = ""
        with response as stream:
            for event in stream:
                if event.type == "content_block_delta":
                    result += event.delta.text
                    yield result

            yield result

    except APIError as e:
        raise RuntimeError(f"API Error: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")