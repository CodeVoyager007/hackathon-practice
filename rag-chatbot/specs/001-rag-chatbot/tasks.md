# Tasks: RAG Chatbot

**Input**: Design documents from `specs/001-rag-chatbot/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

## Phase 1: Setup

**Purpose**: Project initialization and basic structure.

- [x] T001 Create the directory structure as defined in `plan.md` (`app`, `app/agents`, `app/services`, `app/core`, `app/api/v1/endpoints`, `tests`).
- [x] T002 Create a `requirements.txt` file and add initial dependencies: `fastapi`, `uvicorn`, `pydantic`, `python-dotenv`.
- [x] T003 Create an empty `.env` file for storing API keys and environment variables. (Note: User must create this in the parent `hackathon-practice` directory).
- [x] T004 Create `app/main.py` with a boilerplate FastAPI app instance.
- [x] T005 [P] Create empty placeholder files for `app/agents/book_agent.py`, `app/services/ingest.py`, `app/core/guardrails.py`, and `app/api/v1/endpoints/chat.py`.

---

## Phase 2: Foundational (Infrastructure & Data Pipeline)

**Purpose**: Core infrastructure that MUST be complete before any user story can be implemented.

- [x] T006 [P] Implement `app/core/config.py` to load environment variables from the `.env` file.
- [x] T007 Add `qdrant-client` and `langchain` to `requirements.txt`.
- [x] T008 Implement the Qdrant connection logic in `app/services/ingest.py`, connecting to Qdrant Cloud using credentials from `config.py`.
- [x] T009 Implement the data loading logic in `app/services/ingest.py` to read all `.mdx` files from a specified local directory (`../frontend/docs`).
- [x] T010 Implement text chunking logic in `app/services/ingest.py` using LangChain's MarkdownHeaderTextSplitter.
- [x] T011 Add the Gemini API dependency (`openai`) to `requirements.txt`.
- [x] T012 Implement embedding logic in `app/services/ingest.py` to convert text chunks into vectors using the Gemini `embedding-001` model via the OpenAI SDK wrapper.
- [x] T013 Implement the storage logic in `app/services/ingest.py` to upload the document chunks and their vectors to the 'book_vectors' collection in Qdrant.
- [x] T014 Create a main execution block in `app/services/ingest.py` to run the full ingestion pipeline.

**Checkpoint**: The data ingestion pipeline is complete. The Qdrant database is populated with the book's content.

---

## Phase 3: User Story 1 - General Book Q&A (Priority: P1) 🎯 MVP

**Goal**: Allow users to ask general questions and get answers from the entire book.

**Independent Test**: Ask a question via the API that requires information from multiple parts of the book and verify the answer is correct and cites sources.

- [x] T015 [P] [US1] In `app/agents/book_agent.py`, create a `retrieval_tool` that takes a question string, queries the Qdrant database for relevant document chunks, and returns the concatenated content.
- [x] T016 [P] [US1] In `app/core/guardrails.py`, implement an `InputGuardrail` to check for prompt injection and other malicious inputs in the user's question.
- [x] T017 [US1] In `app/agents/book_agent.py`, create the `BookAgent` class. Initialize it with a Gemini `gemini-1.5-flash` client.
- [x] T018 [US1] Implement the main runner method in `BookAgent` that takes a question, applies the `InputGuardrail`, calls the `retrieval_tool`, formats the prompt with the retrieved context, and calls the Gemini LLM.
- [x] T019 [US1] In `app/core/guardrails.py`, implement an `OutputGuardrail` that checks the LLM's response for safety and adds citation information based on the sources from the `retrieval_tool`.
- [x] T020 [US1] Integrate the `OutputGuardrail` into the `BookAgent`'s runner method.
- [x] T021 [US1] In `app/api/v1/endpoints/chat.py`, create the `POST /api/chat/rag` endpoint.
- [x] T022 [US1] Implement the logic in the `/api/chat/rag` endpoint to instantiate the `BookAgent` and call its runner method with the user's question, returning the final answer. (Note: Completed as part of T021).
- [x] T023 [US1] In `app/main.py`, include the router from `app/api/v1/endpoints/chat.py`.

**Checkpoint**: The `/api/chat/rag` endpoint is fully functional and can answer general questions about the book.

---

## Phase 4: User Story 2 - Context-Only Q&A (Priority: P2)

**Goal**: Allow users to ask questions about a specific piece of selected text.

**Independent Test**: Call the API with a block of text and a question that can only be answered from that text. Verify the answer is correct and does not use outside information.

- [x] T024 [P] [US2] In `app/agents/book_agent.py`, create a `direct_qa_tool` that accepts a question and a `context_text` string.
- [x] T025 [US2] Update the `BookAgent`'s main runner method to accept an optional `context_text`. If `context_text` is provided, it should use the `direct_qa_tool` instead of the general retrieval tool. The prompt sent to the LLM should instruct it to *only* use the provided context.
- [x] T026 [US2] In `app/api/v1/endpoints/chat.py`, create the `POST /api/chat/context-only` endpoint.
- [x] T027 [US2] Implement the logic in the `/api/chat/context-only` endpoint to call the `BookAgent`'s runner method with both the question and the `context_text`. (Note: Completed as part of T026).
- [x] T028 [P] [US2] For the frontend, create a `Chatbot.tsx` React component using the OpenAI ChatKit SDK. (Note: Requires a frontend engineer).
- [x] T029 [P] [US2] In the Docusaurus frontend, implement a JavaScript snippet that listens for text selection, captures the selected text, and makes it available to the `Chatbot.tsx` component to enable the context-only mode. (Note: Requires a frontend engineer).

**Checkpoint**: The `/api/chat/context-only` endpoint is functional. The frontend can now distinguish between general and context-only questions.

---

## Phase 5: Polish & Cross-Cutting Concerns

- [x] T030 [P] Add comprehensive docstrings and comments to all new functions and classes.
- [x] T031 Create a `quickstart.md` in `specs/001-rag-chatbot/` explaining how to set up the `.env` file, install dependencies, and run the backend server.
- [x] T032 Add basic unit tests for the guardrails in `tests/unit/`.
- [x] T033 Add a basic integration test for the `/api/chat/rag` endpoint in `tests/integration/`.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL)
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: At this point, the core backend for general Q&A is functional and can be tested.

### Incremental Delivery

1.  After MVP, complete Phase 4 (User Story 2) to add the context-only feature.
2.  Finally, complete Phase 5 for polish and documentation.
