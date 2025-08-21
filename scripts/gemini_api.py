import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("The environment variable GOOGLE_API_KEY is not set!")
else:
    genai.configure(api_key=api_key)

def call_gemini(prompt, model="gemini-2.5-pro"):
    """
    Call the Gemini API with the given prompt and model.
    Args:
        prompt (str): The input prompt for the Gemini API.
        model (str): The model to use for the API call.
    Returns:
        str: The response from the Gemini API.
    """
    try:
        # Create a GenerativeModel instance
        model_instance = genai.GenerativeModel(model)
        response = model_instance.generate_content(prompt)

        if response and response.candidates:
            return response.candidates[0].content.parts[0].text
        else:
            return "No response generated."

    except Exception as e:
        return f"Error calling Gemini API: {e}"


# user_prompt = "Tell a light hearted joke for an audience of data scientists"
# response = call_gemini(user_prompt)
# print(f"Gemini Response: \n {response}")