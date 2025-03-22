# Start with an official Python image
FROM python:3.11-slim

# Install dependencies (curl for downloading Ollama CLI)
RUN apt-get update && apt-get install -y curl

# Install Ollama CLI
RUN curl -sSL https://ollama.com/install.sh | bash

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose port 8000 (default port for FastAPI)
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
