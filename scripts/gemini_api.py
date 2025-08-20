import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("The environment variable GOOGLE_API_KEY is not set!")

# Configure the genai library
genai.configure(api_key=api_key)

# Create a GenerativeModel instance
model = genai.GenerativeModel("gemini-2.5-pro")

# Generate content
response = model.generate_content("Explain how AI works in few lines")

# print the response text
if response and response.candidates:
    print(response.candidates[0].content.parts[0].text)
else:
    print("No response generated.")
