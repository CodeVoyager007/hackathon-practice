# Research and Decisions for RAG Chatbot

This document records the key research findings and decisions made for the RAG Chatbot project, based on the requirements in the feature specification and the project constitution.

## 1. LLM and Embedding Model

- **Decision**: Use Gemini API via the OpenAI SDK wrapper.
  - **Chat Model**: `gemini-1.5-flash`
  - **Embedding Model**: `embedding-001` (as specified in the constitution, assuming this is the Gemini model to be used)
- **Rationale**: This adheres to the project constitution's constraint of using the free-tier Gemini API. The OpenAI SDK provides a familiar interface for interacting with the LLM.
- **Alternatives Considered**: Direct OpenAI API (rejected due to cost constraint), other open-source models (rejected as Gemini was specified).

## 2. Data Ingestion and Chunking

- **Decision**: Use LangChain for loading and processing `.mdx` files.
- **Chunking Strategy**: Chunk documents based on Markdown headers. This keeps related content together, which is crucial for providing accurate context to the RAG model. A recursive character text splitter with Markdown separators will be used.
- **Rationale**: LangChain provides robust, pre-built components for document loading and transformation, which accelerates development. Header-based chunking is a standard best practice for structured documents like a book.
- **Alternatives Considered**: Custom chunking script (rejected as it would be more time-consuming to build and maintain).

## 3. Vector Database

- **Decision**: Qdrant Cloud (Free Tier).
- **Rationale**: Qdrant is a high-performance vector database that offers a generous free tier suitable for this project's scale. It is specified in the constitution.
- **Alternatives Considered**: ChromaDB, FAISS (rejected as Qdrant Cloud meets the need for a managed, free-tier solution).

## 4. Frontend Integration

- **Decision**: Use the OpenAI ChatKit SDK with React to create a floating chat widget.
- **Integration Method**: The Docusaurus application will be "swizzled" to wrap all pages with a provider that includes the chat widget. A custom JavaScript snippet will be added to capture highlighted text and pass it to the widget.
- **Rationale**: ChatKit provides a pre-built, professional-looking UI, saving significant frontend development time. The swizzling method is the standard Docusaurus way to customize site-wide components.
- **Alternatives Considered**: Building a custom chat UI from scratch (rejected due to time constraints of the hackathon).

## 5. Agent and Tooling

- **Decision**: Use the OpenAI Agents SDK.
- **Architecture**: A main `BookAgent` will be created. This agent will have access to two tools:
    1.  A `retrieval_tool` that queries the Qdrant database for general questions.
    2.  A `direct_qa_tool` that takes user-selected text and a question for context-only Q&A.
- **Rationale**: The Agents SDK provides a structured way to build and orchestrate tools, making the logic clean and extensible. This modular approach, as required by the constitution, allows for clear separation of concerns.
- **Alternatives Considered**: A single monolithic function (rejected as it would violate the modularity principle and be harder to debug and extend).
