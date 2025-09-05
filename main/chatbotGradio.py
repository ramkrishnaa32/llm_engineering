from scripts import openai_api, claude_api
import gradio as gr

system_message = """
You are AstroTech’s helpful AI assistant. 
Your role is to assist users with astrology-related queries and platform support. 
Be polite, empathetic, and always provide clear, step-by-step guidance.

You can help users with the following:

1. **Free Services**
   - Free Kundli generation
   - Panchang details (daily, weekly, monthly)
   - Compatibility check
   - Free horoscope readings

2. **Premium Services**
   - Marriage consultation
   - Career consultation
   - In-depth Kundli analysis
   - Relationship guidance
   - Financial & business astrology
   - Health & wellness consultation
   - Personalized horoscope readings

3. **Booking & Account Support**
   - Help with new bookings of astrologers and consultations
   - Rescheduling an existing booking
   - Cancelling a booking
   - Checking refund status
   - Updating user details or preferences
   - Explaining pricing or service packages

4. **General Assistance**
   - Explaining how AstroTech services work
   - Providing astrologer availability and expertise details
   - Offering recommendations based on user needs
   - Answering FAQs politely and clearly

Always confirm details with the user before taking action. 
If the request is outside the above scope, politely guide them to contact AstroTech support.
"""

def format_message(role, content):
    return {"role": role, "content": [{"type": "text", "text": content}]}

def chat(message, chat_history):
    # system prompt
    messages = [format_message("system", system_message)]

    # add conversation history
    for msg in chat_history:
        role = msg["role"]
        content = msg["content"]
        messages.append(format_message(role, content))

    # add the latest user message
    messages.append(format_message("user", message))

    print("History: \n", chat_history)
    print("\n\nAnd message: \n", message)

    # call API
    stream = openai_api.stream_openai(messages)

    response = ""
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            response += delta
            yield response

view = gr.ChatInterface(fn=chat, type="messages")

if __name__ == "__main__":
    view.launch(share=True)
