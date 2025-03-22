# Use an official Python runtime as a base image
FROM python:3.11-slim

# Install curl and other dependencies
RUN apt-get update && apt-get install -y curl

# Install Ollama CLI
RUN curl -sSL https://ollama.com/install.sh | bash

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose the necessary port (FastAPI default)
EXPOSE 8000

# Command to run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
