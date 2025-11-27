from qdrant_client import QdrantClient
from qdrant_client.http import models
from settings import settings

def get_qdrant_client() -> QdrantClient:
    return QdrantClient(location=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY)

def init_db():
    client = get_qdrant_client()
    collection_name = "documents"
    
    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=768,  # Dimension for text-embedding-004
                distance=models.Distance.COSINE
            )
        )
        print(f"Collection '{collection_name}' created.")
    else:
        print(f"Collection '{collection_name}' already exists.")

if __name__ == "__main__":
    init_db()
