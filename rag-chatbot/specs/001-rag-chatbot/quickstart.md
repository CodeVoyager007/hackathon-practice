# Quickstart Guide: RAG Chatbot

This guide provides the necessary steps to set up and run the RAG Chatbot backend.

## 1. Prerequisites

- Python 3.11
- An account with Qdrant Cloud (free tier is sufficient)
- A Gemini API Key

## 2. Environment Setup

1.  Navigate to the root `hackathon-practice` directory (one level above the `rag-chatbot` directory).
2.  Create a file named `.env` in the `hackathon-practice` directory.
3.  Add the following environment variables to the `.env` file, replacing the placeholder values with your actual credentials:

    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    QDRANT_URL="YOUR_QDRANT_CLOUD_URL"
    QDRANT_API_KEY="YOUR_QDRANT_API_KEY"
    ```

## 3. Installation

1.  Navigate to the `rag-chatbot` directory.
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    - On Windows: `venv\Scripts\activate`
    - On macOS/Linux: `source venv/bin/activate`
4.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 4. Running the Ingestion Service

Before running the backend for the first time, you must populate the vector database with the content from the book.

**IMPORTANT**: Ensure the book's `.mdx` files are located in a `frontend/docs` directory that is a sibling to the `rag-chatbot` directory, as specified in the plan.

Run the ingestion script from the `rag-chatbot` directory:

```bash
python -m app.services.ingest
```

You should see output indicating a successful connection to Qdrant, the number of documents and chunks processed, and a final success message.

## 5. Running the Backend Server

Once the ingestion is complete, you can start the FastAPI server.

Run the server from the `rag-chatbot` directory:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can access the auto-generated documentation at `http://127.0.0.1:8000/docs`.
