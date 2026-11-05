import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from document_search import search_documents
from llm_service import generate_answer


# load the env variables from the local .env file
load_dotenv()
app = FastAPI()

# Allow React frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Hello World"}

# API endpoint

@app.post("/userprompt")
def ask_document(request: QuestionRequest):

    question = request.question
    # Step 1: Search documents
    results = search_documents(question)

    if not results:
        return {
            "answer": "I could not find relevant information in the company documents.",
            "sources": []
        }

    # Step 2: Prepare document context
    context = ""
    for result in results:
        context += (
            f"\nSource: {result['source']}\n"
            f"Content: {result['content']}\n"
        )

    # Step 3: Send question and context to LLM
    answer = generate_answer(
        question,
        context
    )

    # Step 4: Return response
    return {
        "question": question,
        "answer": answer,
        "sources": [
            result["source"] for result in results
        ]
    }
