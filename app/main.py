from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from document_search import search_documents
from llm_service import generate_answer

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

# API endpoint

@app.post("/userprompt")
def ask_document(request: QuestionRequest):
    print(f"Received in the python side : {request}")
    question = request.question
    # Search documents
    results = search_documents(question)

    if not results:
        return {
            "answer": "I could not find relevant information in the company documents.",
            "sources": []
        }

    # Prepare document context
    context = ""
    for result in results:
        context += (
            f"\nSource: {result['source']}\n"
            f"Content: {result['content']}\n"
        )

    # Send question and context to LLM
    answer = generate_answer(
        question,
        context
    )

    # Return response
    return {
        "question": question,
        "answer": answer,
        "sources": [
            result["source"] for result in results
        ]
    }
