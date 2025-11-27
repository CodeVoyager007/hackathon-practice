<!--
---
Sync Impact Report
---
- Version change: 1.0.0 (Initial ratification)
- Added Principles:
  - I. Technology Stack Adherence
  - II. API Specification Compliance
  - III. Modular & Reusable Intelligence
  - IV. Specification-Driven Development
- Dependent Templates Checked:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# RAG Chatbot Project Constitution

## Core Principles

### I. Technology Stack Adherence
This project MUST strictly adhere to the defined free-tier technology stack. Any deviation or addition of new dependencies requires a formal amendment to this constitution.
- **LLM**: Gemini API (gemini-1.5-flash for chat, embedding-001 for embeddings) via the OpenAI SDK wrapper.
- **Backend**: FastAPI.
- **Vector DB**: Qdrant Cloud (Free Tier), with the collection named 'book_vectors'.
- **Frontend**: OpenAI ChatKit SDK with React, embedded within the Docusaurus application.
- **Agents/Tooling**: OpenAI Agents SDK for creating reusable tools and sub-agents.
- **Ingestion**: LangChain for loading and processing `docs/*.mdx` files.

### II. API Specification Compliance
All developed APIs MUST conform to the specified contracts for requests and responses. This ensures predictable and stable integrations.
- `POST /api/chat/rag`:
  - **Input**: `{ "question": "string" }`
  - **Output**: `{ "answer": "string", "sources": ["string"] }`
- `POST /api/chat/context-only`:
  - **Input**: `{ "question": "string", "context_text": "string" }`
  - **Output**: `{ "answer": "string" }`
  - **Behavior**: MUST return a "Cannot find in book" style message if the answer is not in the `context_text`.

### III. Modular & Reusable Intelligence
Intelligence and core logic MUST be encapsulated in modular, independently testable classes to promote reusability and maintainability.
- **BookAgent**: A primary runner class responsible for orchestrating tools and agents.
- **Guardrails**: Dedicated classes for input validation and output sanitization to ensure safety and quality.

### IV. Specification-Driven Development
All development work MUST be guided by an approved feature specification (`spec.md`). Implementation should not begin until a spec is agreed upon, and the final implementation must satisfy all functional requirements and success criteria outlined in the spec.

## Governance
This constitution is the primary source of truth for project standards and technical decisions. It supersedes all other informal practices. Amendments require documentation, review, and a recorded approval. All code reviews and planning sessions must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-11-27 | **Last Amended**: 2025-11-27