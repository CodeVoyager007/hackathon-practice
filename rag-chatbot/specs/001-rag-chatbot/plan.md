# Implementation Plan: RAG Chatbot

**Branch**: `001-rag-chatbot` | **Date**: 2025-11-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-rag-chatbot/spec.md`

## Summary

This plan outlines the technical implementation for a RAG-based chatbot embedded within a Docusaurus book. The chatbot will answer general questions based on the book's content and context-specific questions based on user-selected text. The implementation will strictly follow the project constitution, using a predefined stack of free-tier services including FastAPI, Qdrant, and the Gemini API via the OpenAI SDK.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, qdrant-client, openai, langchain, pydantic
**Storage**: Qdrant Cloud (Vector DB)
**Testing**: pytest
**Target Platform**: Web (Docusaurus/React)
**Project Type**: Web Application (backend service)
**Performance Goals**: Median response time < 3 seconds. Ingestion of a 100-page book < 5 minutes.
**Constraints**: Must adhere to the free tiers of all services. The chatbot must be embeddable in an existing Docusaurus site.
**Scale/Scope**: The system will serve a single Docusaurus book and a moderate user base.

## Constitution Check

*GATE: All gates must pass. No violations are justified at this stage.*

- [x] **I. Technology Stack Adherence**: The plan uses the approved stack (Gemini, FastAPI, Qdrant, etc.).
- [x] **II. API Specification Compliance**: The project structure and API definitions align with the specified contracts.
- [x] **III. Modular & Reusable Intelligence**: The architecture includes distinct modules for the Agent (`book_agent.py`) and Guardrails (`guardrails.py`).
- [x] **IV. Specification-Driven Development**: This plan is derived directly from the `spec.md` file.

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-chatbot/
├── plan.md              # This file
├── research.md          # Research on dependencies and patterns
├── data-model.md        # Data models for the application
├── quickstart.md        # Instructions for setup and running
├── contracts/           # API contract definitions
│   └── openapi.yml
└── tasks.md             # Implementation tasks (to be generated)
```

### Source Code (repository root)

The backend will be a single application within the `rag-chatbot` directory.

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

**Structure Decision**: A single backend application structure is chosen as it's simple and sufficient for the project's scope. The frontend is a separate, existing Docusaurus project.

## Complexity Tracking

No violations of the constitution have been identified.
