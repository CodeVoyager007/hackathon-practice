import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

# Local model (dim=384, no API)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Qdrant setup (dim=384)
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

def embed_chunks(chunks):
    texts = [chunk.page_content for chunk in chunks]
    embeddings = model.encode(texts)
    return embeddings.tolist()

def main():
    # Load MDX from book
    loader = DirectoryLoader('../frontend/docs', glob="**/*.mdx")
    docs = loader.load()
    print(f"Loaded {len(docs)} documents.")

    # Split
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks.")

    # Embed local
    embeddings = embed_chunks(chunks)

    # Store in Qdrant (dim=384)
    qdrant = Qdrant.from_documents(
        chunks, embeddings, 
        url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"),
        collection_name="book_vectors"
    )
    print("Ingested successfully!")

if __name__ == "__main__":
    main()