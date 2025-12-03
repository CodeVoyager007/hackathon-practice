from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database import init_db
from rag_service import rag_service
from ingest_local import ingest_local_docs
from typing import Optional

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB on startup
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Docusaurus default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str
    context: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/ingest-local")
async def ingest_local(background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(ingest_local_docs)
        return {"status": "success", "message": "Local ingestion process started in the background."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        print(f"Received chat request: query='{request.query}', context='{request.context}'")
        answer = rag_service.generate_answer(request.query, request.context)
        return {"answer": answer}
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
