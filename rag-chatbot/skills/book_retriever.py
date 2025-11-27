from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.http import models
from settings import settings
from database import get_qdrant_client
from .base import Skill
import uuid

class BookRetrieverSkill(Skill):
    def __init__(self):
        self.openai_client = OpenAI(
            api_key=settings.GEMINI_API_KEY,
            base_url=settings.GEMINI_BASE_URL
        )
        self.qdrant_client = get_qdrant_client()
        self.collection_name = "documents"

    def generate_embedding(self, text: str) -> list[float]:
        response = self.openai_client.embeddings.create(
            model=settings.EMBEDDING_MODEL,
            input=text
        )
        return response.data[0].embedding

    def upsert_document(self, text: str):
        embedding = self.generate_embedding(text)
        point_id = str(uuid.uuid4())
        
        self.qdrant_client.upsert(
            collection_name=self.collection_name,
            points=[
                models.PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload={"text": text}
                )
            ]
        )
        return point_id

    def execute(self, query: str, limit: int = 5) -> list[str]:
        query_embedding = self.generate_embedding(query)
        
        search_result = self.qdrant_client.query_points(
            collection_name=self.collection_name,
            query=query_embedding,
            limit=limit
        )
        
        return [hit.payload["text"] for hit in search_result.points]

    def search(self, query: str, limit: int = 5) -> list[str]:
        return self.execute(query, limit)
