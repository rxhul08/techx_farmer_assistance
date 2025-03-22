from fastapi import FastAPI
from pydantic import BaseModel
from ollama_query import query_ollama

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    user_input = request.question
    bot_response = query_ollama(user_input)
    return {"response": bot_response}

@app.get("/")
async def root():
    return {"message": "Farmer Assistant Bot is running!"}
