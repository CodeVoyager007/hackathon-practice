# Act as a Senior Python Backend Engineer.

I need you to build a production-ready RAG (Retrieval-Augmented Generation) backend using FastAPI.

## Tech Stack:

Package Manager: UV (uv)

LLM Interface: OpenAI Python SDK (configured to talk to Google Gemini API).

Vector Database: Qdrant (using the qdrant-client).

Framework: FastAPI.

## Requirements:

Project Setup: Show the uv commands to initialize the project and add dependencies (fastapi, uvicorn, openai, qdrant-client, python-dotenv).

Configuration: Create a settings.py or .env handling strategy. Important: The OpenAI Client must be initialized with the base_url for Gemini (https://generativelanguage.googleapis.com/v1beta/) and the Gemini API Key.

## Vector Database Logic:

Create a module to connect to Qdrant (assume a local Docker instance or memory mode for testing).

Implement a function to generate embeddings using a Gemini embedding model (e.g., text-embedding-004) via the OpenAI SDK compatibility layer.

Implement an upsert_document function.

Implement a search function.

## RAG Logic:

Create a function that takes a user query, retrieves relevant context from Qdrant, and sends a prompt to the Gemini model (e.g., gemini-1.5-flash) via the openai.chat.completions.create method.

## API Routes:

POST /ingest: Accepts text, embeds it, and saves it to Qdrant.

POST /chat: Accepts a query, performs the RAG lookup, and returns the answer.

## Code Style: Use Python 3.12+, async/await syntax throughout, Pydantic v2 for data validation, and type hinting.

## Please provide the complete file structure and the code for main.py, rag_service.py, and database.py.

## Why this prompt works
This prompt is designed to avoid common hallucinations or architectural errors by being explicit about the integration points:

The "UV" Factor: By explicitly asking for uv commands, you ensure you get the modern workflow (uv add vs pip install), which sets up your pyproject.toml correctly.

The OpenAI/Gemini Bridge: Many models get confused when you ask for "Gemini via OpenAI SDK." By explicitly providing the base_url in the prompt (https://generativelanguage.googleapis.com/v1beta/), you force the AI to write the compatibility code correctly, rather than importing google.generativeai.

Model Specificity: Specifying text-embedding-004 and gemini-1.5-flash ensures the code uses current, efficient models rather than legacy ones.

Separation of Concerns: Asking for specific modules (rag_service.py, database.py) prevents the AI from dumping everything into one giant, unmanageable main.py file.