from scripts import openai_api, gemini_api, claude_api


system_message = "you are a helpful assistant that is great at jokes"
user_prompt = "Tell a light hearted joke for an audience of data scientists"

prompts = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_prompt}
      ]

response = openai_api.call_openai(prompts)
print("OpenAI Response:", response)

response = gemini_api.call_gemini(user_prompt)
print("Gemini Response:", response)

response = claude_api.call_claude(user_prompt)
print("Claude Response:", response)