from fastapi import FastAPI
from app.api.v1.endpoints import chat

app = FastAPI(
    title="RAG Chatbot API",
    description="API for the RAG Chatbot embedded in a Docusaurus book.",
    version="1.0.0",
)

app.include_router(chat.router, prefix="/api/chat", tags=["chat"])

@app.get("/")
def read_root():
    return {"Hello": "World"}