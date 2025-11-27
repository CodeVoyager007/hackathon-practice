# Data Models for RAG Chatbot

This document defines the key data entities for the RAG Chatbot application. These models are logical and do not presuppose a specific database schema or implementation.

## 1. DocumentChunk

Represents a piece of content ingested from the source `.mdx` files and stored in the vector database.

- **Attributes**:
  - `chunk_id` (string, unique): A unique identifier for the chunk.
  - `content` (string): The text content of the chunk.
  - `vector` (array of float): The embedding vector generated from the content.
  - `metadata` (object):
    - `source_file` (string): The original file path the chunk came from.
    - `headers` (array of string): The Markdown headers associated with this chunk.
    - `page_number` (integer, optional): The page number if available.

- **Validation**:
  - `content` must not be empty.

## 2. UserQuestion (API Model)

Represents a question submitted by the user through an API endpoint.

- **Attributes**:
  - `question` (string): The user's query.
  - `context_text` (string, optional): The user-selected text for context-only Q&A.

- **Validation**:
  - `question` must not be empty and should be sanitized to prevent injection attacks (Guardrail responsibility).

## 3. Answer (API Model)

Represents the answer returned to the user by the API.

- **Attributes**:
  - `answer` (string): The generated response from the LLM.
  - `sources` (array of string, optional): A list of source file names or headers that contributed to the answer.

- **Validation**:
  - `answer` must be sanitized to prevent returning malicious content (Guardrail responsibility).
  - If `sources` are provided, they must correspond to actual sources from the `DocumentChunk` metadata.

## 4. Conversation

Represents the interaction history between a user and the chatbot for a single session. This is a logical model; it may not be explicitly stored depending on the final implementation.

- **Attributes**:
  - `session_id` (string, unique): A unique identifier for the conversation session.
  - `history` (array of objects): A list of previous questions and answers.
    - `role` (string): "user" or "assistant".
    - `content` (string): The text of the message.

- **State Transitions**:
  - A conversation begins in an `active` state.
  - It can transition to a `timed_out` state after a period of inactivity.
  - It ends when the user closes the chat widget.
