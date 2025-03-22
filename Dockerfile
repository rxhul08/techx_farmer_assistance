FROM python:3.11-slim
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://ollama.com/install.sh | bash
RUN ollama --version
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
