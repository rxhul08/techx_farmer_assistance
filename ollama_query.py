import subprocess

def query_ollama(prompt: str):
    command = ["ollama", "run", "mistral:instruct", prompt]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    user_input = input("Enter your question: ")
    response = query_ollama(user_input)
    print(f"Model Response: {response}")
