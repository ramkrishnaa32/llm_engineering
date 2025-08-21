from scripts import openai_api, claude_api

def main():

    print("=== GPT 🤖 x Claude 🤖 Chat ===\n")

    # Starting a message from GPT
    gpt_context = [
        {"role": "system", "content": "You are GPT. Keep your replies short, friendly, and casual."},
        {"role": "user", "content": "Start the chat by saying hi to Claude."}
    ]

    gpt_response = openai_api.call_openai(gpt_context, model="gpt-4o", temperature=0.6)
    print("GPT:", gpt_response, "\n")
    last_message = gpt_response

    # Loop for short back-and-forth
    for turn in range(5):  # 5 turns total
        claude_response = claude_api.call_claude(
            f"GPT just said: {last_message}\nReply briefly, like a friendly hello chat.",
            model="claude-3-7-sonnet-20250219",
            max_tokens=50,
            temperature=0.7
        )
        print("Claude:", claude_response, "\n")

        gpt_context.append({"role": "assistant", "content": last_message})
        gpt_context.append({"role": "user", "content": f"Claude replied: {claude_response}\nRespond briefly, keep it casual."})

        gpt_response = openai_api.call_openai(gpt_context, model="gpt-4o", temperature=0.6)
        print("GPT:", gpt_response, "\n")

        last_message = gpt_response

if __name__ == "__main__":
    main()
