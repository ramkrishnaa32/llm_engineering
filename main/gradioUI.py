import gradio as gr
from scripts import openai_api, claude_api

# Simple function to demonstrate Gradio UI
def shout(text):
    print("Shout has been called with text: ", text)
    return text.upper()

def stream_mode(prompt, model):

    # Call selected model
    if model == "GPT":
        result = openai_api.stream_openai(prompt)
    elif model == "Claude":
        result = claude_api.stream_claude(prompt)
    else:
        raise ValueError("Model not supported")

    # Stream the response chunks
    for chunk in result:
        yield chunk

view = gr.Interface(
    fn=stream_mode,
    inputs=[gr.Textbox(label="Your Message:", lines=6), gr.Dropdown(["GPT", "Claude"], label="Choose Model:", value="Claude")],
    outputs=[gr.Markdown(label="Response:")],
    title="Shout It Out!",
    allow_flagging="never")

if __name__ == "__main__":
    view.launch(share=True)