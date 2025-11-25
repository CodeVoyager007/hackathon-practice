<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- List of modified principles: N/A (Initial version)
- Added sections: Principles I, II, III, IV
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md (No changes needed, compatible)
  - ✅ .specify/templates/spec-template.md (No changes needed, compatible)
  - ✅ .specify/templates/tasks-template.md (No changes needed, compatible)
- Follow-up TODOs: None
-->
# RAG Chatbot Project Constitution

This is a high-level technical specification that will strictly guide all subsequent AI-Driven code generation for the hackathon project.

## Core Principles

### I. Core Objective & Knowledge Base
*   **Primary Objective:** Develop a RAG chatbot embedded in the published book, providing two distinct Q&A modes.
*   **Target Book URL (Knowledge Base):** `https://codevoyager007.github.io/hackathon-practice/`
*   **AI-Driven Process:** The project development will be guided by the Gemini CLI, based on this Constitution.

### II. Mandatory Technology Stack
The specific tools and models to be used are defined below. Adherence to this stack is non-negotiable.

| Component             | Required Technology | Role/Model Name          | Technical Detail                                      |
| :-------------------- | :------------------ | :----------------------- | :---------------------------------------------------- |
| **LLM/Generator**     | **OpenAI SDK**      | `gpt-3.5-turbo`          | Used for final answer generation (Chat Completions API). |
| **Embeddings**        | **OpenAI SDK**      | `text-embedding-3-small` | **Dimension Size: 768**.                               |
| **Web Framework**     | FastAPI             | Core application server. | Handles API routes and dependency injection.          |
| **Vector Database**   | Qdrant Cloud Free Tier | High-performance vector storage. | Collection dimension must be set to 768.              |
| **Frontend Integration**| Docusaurus, JS/Fetch | UI embedded in the published book. | Must handle CORS and context selection logic.         |

### III. Core API Specification
The API must be implemented using FastAPI and Pydantic to enforce strict data contracts.

#### API 3.1: Standard Book Q&A (RAG Mode)
*   **Endpoint:** `/api/chat/rag`
*   **Method:** POST
*   **Input Schema (Pydantic Model):** `QuestionRequest(question: str)`
*   **Process Flow:**
    1.  Embed `question` using `text-embedding-3-small` (dimension 768).
    2.  Search Qdrant for top **3** relevant text chunks (`k=3`).
    3.  Construct a System Prompt instructing `gpt-3.5-turbo` to answer **only** based on the retrieved context.
    4.  Call OpenAI Chat Completions API.
*   **Output Schema (Pydantic Model):** `AnswerResponse(answer: str, context_sources: list[str])`

#### API 3.2: Context-Specific Q&A (Context-Only Mode)
*   **Endpoint:** `/api/chat/context-only`
*   **Method:** POST
*   **Input Schema (Pydantic Model):** `ContextQuestionRequest(question: str, context_text: str)`
*   **Process Flow:**
    1.  **Skip all vector search.**
    2.  Construct a **highly constrained System Prompt** for `gpt-3.5-turbo` to answer the question using **ONLY** the provided `context_text`. If the answer is not in the text, the model must state that the answer cannot be found in the provided context.
    3.  Call OpenAI Chat Completions API.
*   **Output Schema (Pydantic Model):** `AnswerResponse(answer: str)`

### IV. Modular & Reusable Architecture
To satisfy the "reusable intelligence" (Agent Skills) requirement, the RAG logic must be encapsulated in modular Python classes. The main FastAPI app should only orchestrate calls to these services.

| Module/Class              | Responsibility                                                 | Key Methods                                                       |
| :------------------------ | :--------------------------------------------------------------- | :---------------------------------------------------------------- |
| **`OpenAIEmbeddingService`** | Handles all interactions with the `text-embedding-3-small` model. | `embed_query(text: str)`, `embed_documents(texts: list[str])`      |
| **`QdrantService`**       | Handles connection and retrieval logic from Qdrant.              | `search_vectors(query_vector: list[float], k: int)`               |
| **`OpenAIChatAgent`**     | Handles prompt construction and calls to `gpt-3.5-turbo`.      | `generate_rag_answer(context: str, question: str)`, `generate_constrained_answer(context: str, question: str)` |


## Governance

This Constitution is the single source of truth for project requirements and technical architecture. All development, code reviews, and automated processes must adhere to its principles. Amendments require a documented change request and approval, after which the version number must be incremented.

**Version**: 1.0.0 | **Ratified**: 2025-11-25 | **Last Amended**: 2025-11-25