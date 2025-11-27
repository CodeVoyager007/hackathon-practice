# Feature Specification: RAG-based Chatbot

**Feature Branch**: `001-rag-chatbot`  
**Created**: 2025-11-27 
**Status**: Draft  
**Input**: User description: "I want to build a RAG-based Chatbot embedded in my Docusaurus book[](https://codevoyager007.github.io/hackathon-practice/) for GIAIC hackathon. Features (from transcript & image): 1. Standard Book Q&A: Users ask general questions (e.g., "What is AI?") – bot retrieves from full book via RAG. 2. Context-Only Q&A: User selects text on page (e.g., para highlight) – bot answers ONLY from that selected text (no full book, no hallucinations). 3. UI: Floating chat widget (like image: "Hello! How can I help you today?") using OpenAI ChatKit SDK, embedded in every chapter. 4. Backend: FastAPI API connections, OpenAI Agents SDK for tools/agents (reusable subagents for extra marks). 5. Ingestion: Pull content from Docusaurus docs/*.mdx, chunk & embed to Qdrant. User Stories: - As student, ask book questions for better understanding. - As power user, select text for focused answers. - As dev, bot says "Cannot find in book" if no context. Constraints: - Free: Gemini API via OpenAI SDK (no paid OpenAI). - Spec-Driven: Use Spec-Kit for agents/skills. - Embedded: No separate app – direct in GitHub Pages book."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - General Book Q&A (Priority: P1)

A student reading the book has a general question about a concept mentioned across multiple chapters. They open the chat widget and ask the question to get a consolidated answer based on the entire book's content.

**Why this priority**: This is the core feature that provides the primary value of having a chatbot for the book.

**Independent Test**: Can be tested by asking a question that requires knowledge from different parts of the book and verifying the answer is accurate and comprehensive.

**Acceptance Scenarios**:

1. **Given** a user is on any page of the book, **When** they open the chat widget and ask a general question (e.g., "What is the main idea of this book?"), **Then** the system provides an answer synthesized from the entire book's content.
2. **Given** a user asks a question about a topic not covered in the book, **When** they submit the query, **Then** the system responds with a message indicating the information is not available in the book.

---

### User Story 2 - Context-Only Q&A (Priority: P2)

A power user wants to understand a specific paragraph or section in detail. They highlight the text on the page, and the chat widget provides a way for them to ask a question specifically about that highlighted text.

**Why this priority**: This provides a more focused and precise user experience for in-depth learning.

**Independent Test**: Can be tested by highlighting a specific passage, asking a question relevant only to that passage, and confirming the answer is drawn exclusively from the selected context.

**Acceptance Scenarios**:

1. **Given** a user has highlighted a block of text on a page, **When** they ask a question about that text, **Then** the system provides an answer using only the highlighted text as context.
2. **Given** a user has highlighted text and asks a question that cannot be answered from that text, **When** they submit the query, **Then** the system responds with a message indicating it cannot answer from the selected context.

---

### Edge Cases

- What happens when a user highlights a very large block of text? The system should have a defined limit on the amount of text that can be selected for context-only Q&A.
- How does the system handle questions that are ambiguous or poorly phrased? It should attempt to provide the best possible answer or ask for clarification.
- How does the system behave if the underlying knowledge base (the book content) is empty or unavailable? The chat widget should display an error state.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a floating chat widget on every page of the Docusaurus book.
- **FR-002**: The system MUST be able to ingest and process all `.mdx` files from the book's documentation directory.
- **FR-003**: The system MUST support answering questions using the entire book as context.
- **FR-004**: The system MUST support answering questions using only a user-selected snippet of text as context.
- **FR-005**: The system MUST clearly state when it cannot find an answer within the provided context (either the full book or the selected text).
- **FR-006**: The chat interface MUST have a clear input area for users to type their questions.
- **FR-007**: The chat interface MUST display the conversation history between the user and the bot.

### Key Entities *(include if feature involves data)*

- **Book**: Represents the entire collection of documents that form the knowledge base.
- **Document Chunk**: A segment of text from the book, used for retrieval.
- **User Question**: The query submitted by the user.
- **Answer**: The response generated by the system.
- **Conversation**: A record of the back-and-forth interaction between a user and the chatbot.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: At least 90% of general knowledge questions based on the book's content receive a factually correct answer.
- **SC-002**: At least 95% of context-only questions are answered using *only* the selected text.
- **SC-003**: The median response time for any question is less than 3 seconds.
- **SC-004**: The system can successfully ingest and index a 100-page book in under 5 minutes.
- **SC-05**: The chat widget is successfully embedded and functional on all pages of the book.
