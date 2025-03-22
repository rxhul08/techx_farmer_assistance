import subprocess

# Function to query the Mistral model using Ollama's CLI
def query_ollama(prompt: str):
    # The command to run Ollama using the model you want (e.g., mistral:instruct)
    command = ["ollama", "run", "mistral:instruct", prompt]

    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Return the output from Ollama
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error occurred: {str(e)}"

# Example usage in the script (testing the function)
if __name__ == "__main__":
    user_input = input("Enter your question: ")
    response = query_ollama(user_input)
    print(f"Model Response: {response}")
