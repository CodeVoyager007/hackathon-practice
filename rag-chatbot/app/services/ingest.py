import os
import glob
import uuid
from qdrant_client import QdrantClient, models
from app.core.config import settings
from langchain_text_splitters import MarkdownHeaderTextSplitter
from openai import OpenAI

COLLECTION_NAME = "book_vectors"

def get_qdrant_client():
    """
    Returns an authenticated Qdrant client.
    """
    client = QdrantClient(
        url=settings.QDRANT_URL, 
        api_key=settings.QDRANT_API_KEY,
    )
    return client

def get_gemini_client():
    """
    Returns an authenticated Gemini client via OpenAI SDK wrapper.
    """
    return OpenAI(
        api_key=settings.GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta",
        http_client=None, # Workaround for a potential httpx proxy issue
    )

def load_mdx_files(path: str) -> list[str]:
    """
    Loads all .mdx files from the specified directory.
    """
    mdx_files = []
    for filepath in glob.glob(os.path.join(path, "**", "*.mdx"), recursive=True):
        with open(filepath, "r", encoding="utf-8") as f:
            mdx_files.append(f.read())
    return mdx_files

def chunk_documents(documents: list[str]) -> list[str]:
    """
    Chunks the documents based on markdown headers.
    """
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    
    all_chunks = []
    for doc in documents:
        chunks = markdown_splitter.split_text(doc)
        all_chunks.extend(chunks)
    return all_chunks

def embed_chunks(chunks: list) -> list[list[float]]:
    """
    Embeds the text chunks using the Gemini embedding model.
    """
    gemini_client = get_gemini_client()
    embeddings = []
    for chunk in chunks:
        # The 'content' attribute comes from the LangChain splitter
        response = gemini_client.embeddings.create(
            model="models/embedding-001",
            input=chunk.page_content
        )
        embeddings.append(response.data[0].embedding)
    return embeddings

def store_vectors(qdrant_client: QdrantClient, chunks: list, embeddings: list[list[float]]):
    """
    Uploads the document chunks and their vectors to the Qdrant collection.
    """
    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
    )
    
    qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            models.PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={"text": chunk.page_content, "metadata": chunk.metadata},
            )
            for chunk, embedding in zip(chunks, embeddings)
        ],
        wait=True,
    )

def main():
    qdrant_client = get_qdrant_client()
    
    # Verify connection and collection
    try:
        qdrant_client.get_collections()
        print("Successfully connected to Qdrant.")
    except Exception as e:
        print(f"Failed to connect to Qdrant: {e}")
        return

    # Load documents
    docs_path = os.path.join(os.path.dirname(__file__), '..', '..', 'frontend', 'docs')
    if not os.path.exists(docs_path):
        print(f"Error: The directory '{docs_path}' does not exist.")
        print("Please ensure your Docusaurus book's .mdx files are located in a 'frontend/docs' directory sibling to the 'rag-chatbot' directory.")
        return
        
    documents = load_mdx_files(docs_path)
    if not documents:
        print(f"Error: No .mdx files found in '{docs_path}'.")
        print("The ingestion script cannot proceed without source documents.")
        return
        
    print(f"Loaded {len(documents)} documents.")

    # Chunk documents
    chunks = chunk_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    # Embed chunks
    embeddings = embed_chunks(chunks)
    print(f"Created {len(embeddings)} embeddings.")

    # Store vectors
    store_vectors(qdrant_client, chunks, embeddings)
    print(f"Successfully stored {len(chunks)} vectors in the '{COLLECTION_NAME}' collection.")


if __name__ == "__main__":
    main()