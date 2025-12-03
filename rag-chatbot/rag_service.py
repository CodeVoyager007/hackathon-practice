from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.http import models
import google.generativeai as genai
from settings import settings
from database import get_qdrant_client
import uuid
import os

class RAGService:
    def __init__(self):
        # OpenAI SDK for embeddings
        self.openai_client = OpenAI(
            api_key=settings.GEMINI_API_KEY,
            base_url=settings.GEMINI_BASE_URL
        )
        # Native Google SDK for chat
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.gemini_model = genai.GenerativeModel(settings.CHAT_MODEL)
        
        self.qdrant_client = get_qdrant_client()
        self.collection_name = "documents"

    def generate_embedding(self, text: str) -> list[float]:
        response = self.openai_client.embeddings.create(
            model=settings.EMBEDDING_MODEL,
            input=text
        )
        return response.data[0].embedding

    def upsert_document_from_file(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Chunk the content
        chunk_size = 500
        chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
        
        points = []
        for chunk in chunks:
            embedding = self.generate_embedding(chunk)
            point_id = str(uuid.uuid4())
            points.append(
                models.PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload={"text": chunk, "filename": os.path.basename(file_path)}
                )
            )
        
        self.qdrant_client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        return len(points)

    def search(self, query: str, limit: int = 3) -> list[dict]:
        query_embedding = self.generate_embedding(query)
        
        search_result = self.qdrant_client.query_points(
            collection_name=self.collection_name,
            query=query_embedding,
            limit=limit
        )
        
        return [hit.payload for hit in search_result.points]

    def generate_answer(self, query: str, context: str = None) -> str:
        # Step 1: Synthesize a factual answer from the context.
        search_query = context if context else query
        context_payloads = self.search(search_query)

        retrieved_context_str = "\n\n".join([f"Source: {p.get('filename', 'N/A')}\nContent: {p.get('text', '')}" for p in context_payloads])

        synthesis_context = ""
        if context:
            synthesis_context += f"User provided context:\n{context}\n\n"
        if retrieved_context_str:
            synthesis_context += f"Retrieved from book:\n{retrieved_context_str}"

        if not synthesis_context.strip():
            synthesis_context = "No information was found."

        synthesis_prompt = f"""Synthesize the following information into a concise, factual summary that directly answers the user's question.

Information:
---
{synthesis_context}
---

User's Question: {query}

Factual Summary:"""
        
        synthesis_response = self.gemini_model.generate_content(synthesis_prompt)
        factual_summary = synthesis_response.text

        # Step 2: Convert the factual summary into a conversational response.
        persona_prompt = f"""You are a friendly and knowledgeable AI assistant specializing in the content of the book "A Textbook for Teaching Physical AI & Humanoid Robotics". Your personality is helpful, engaging, and you speak like a human expert.

Your goal is to rephrase the following "Factual Summary" into a natural, conversational answer to the "Original User Question".

**CRITICAL INSTRUCTIONS:**
- NEVER mention that you are using a summary or information provided to you.
- Answer the question directly and conversationally, as if you are an expert on the topic.
- If the Factual Summary indicates that no information was found, simply say that you don't have enough information on that topic, and perhaps offer a related thought if appropriate.

Original User Question: {query}

Factual Summary:
---
{factual_summary}
---

Your Conversational Answer:"""

        final_response = self.gemini_model.generate_content(persona_prompt)
        return final_response.text

rag_service = RAGService()
