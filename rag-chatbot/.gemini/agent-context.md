# RAG Chatbot Project Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-11-27

## Active Technologies

- **Language**: Python 3.11
- **Backend Framework**: FastAPI
- **Vector Database**: Qdrant
- **Frontend Framework**: React (via Docusaurus and OpenAI ChatKit SDK)
- **Orchestration/Tooling**: OpenAI Agents SDK, LangChain
- **Testing**: pytest

## Project Structure

```text
app/
├── main.py              # FastAPI application entry point
├── agents/
│   └── book_agent.py    # Core agent logic for handling questions
├── services/
│   └── ingest.py        # Script and logic for data ingestion
├── core/
│   ├── guardrails.py    # Input/output validation and safety
│   └── config.py        # Configuration management
└── api/
    └── v1/
        └── endpoints/
            └── chat.py      # API endpoints for /rag and /context-only

tests/
├── contract/
├── integration/
└── unit/
```

## Commands

- **Run backend server**: `uvicorn app.main:app --reload`
- **Run tests**: `pytest`
- **Run ingestion**: `python -m app.services.ingest`

## Code Style

- **Python**: Adhere to PEP 8. Use Black for automated code formatting. Use Pydantic for data validation in FastAPI models.

## Recent Changes

- **Feature `001-rag-chatbot`**:
  - Established the initial project architecture for the RAG chatbot.
  - Defined the core technology stack including FastAPI, Qdrant, and Gemini.
  - Created the project structure with `app` and `tests` directories.
  - Defined API contracts for chat endpoints.

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
