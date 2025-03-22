from fastapi import FastAPI
from pydantic import BaseModel
from ollama_query import query_ollama

# Create a FastAPI app instance
app = FastAPI()

# Define a request model using Pydantic
class QueryRequest(BaseModel):
    question: str

# Define the endpoint for querying the chatbot
@app.post("/ask")
async def ask_question(request: QueryRequest):
    # Get the user query from the request
    user_input = request.question
    
    # Get the model response using the query_ollama function
    bot_response = query_ollama(user_input)
    
    # Return the response
    return {"response": bot_response}

# Root endpoint for health check
@app.get("/")
async def root():
    return {"message": "Farmer Assistant Bot is running!"}
