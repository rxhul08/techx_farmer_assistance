from ollama_query import query_ollama

def start_chat():
    print("Farmer Assistant Bot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! 👋")
            break

        # Query Ollama for the response, keeping it concise
        bot_response = query_ollama(user_input)

        # Print concise bot response
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    start_chat()
