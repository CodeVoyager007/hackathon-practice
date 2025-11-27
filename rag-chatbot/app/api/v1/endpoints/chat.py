from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.book_agent import BookAgent

router = APIRouter()

class RagChatRequest(BaseModel):
    question: str

class ContextChatRequest(BaseModel):
    question: str
    context_text: str

@router.post("/rag")
async def general_book_qa(request: RagChatRequest):
    """
    Endpoint for general book Q&A.
    """
    agent = BookAgent()
    response = agent.run(question=request.question)
    return response

@router.post("/context-only")
async def context_only_qa(request: ContextChatRequest):
    """
    Endpoint for context-only Q&A.
    """
    agent = BookAgent()
    response = agent.run(question=request.question, context_text=request.context_text)
    return response
