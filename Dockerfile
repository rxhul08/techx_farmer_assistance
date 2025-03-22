# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Ollama CLI (replace with actual installation steps if necessary)
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://ollama.com/install.sh | bash

# Copy the application files into the container
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Set the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]