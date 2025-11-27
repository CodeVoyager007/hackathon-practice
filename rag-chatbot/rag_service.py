import google.generativeai as genai
from settings import settings
from skills.book_retriever import BookRetrieverSkill

class RAGService:
    def __init__(self):
        # Native Google SDK for chat
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.gemini_model = genai.GenerativeModel(settings.CHAT_MODEL)
        
        # Initialize skills
        self.book_retriever = BookRetrieverSkill()

    def upsert_document(self, text: str):
        return self.book_retriever.upsert_document(text)

    def generate_answer(self, query: str, context: str = None) -> str:
        if context:
            context_docs = [context]
        else:
            context_docs = self.book_retriever.search(query)
        
        if not context_docs:
            return "I don't have enough information to answer that question."
        
        context_str = "\n\n".join(context_docs)
        prompt = f"""You are a helpful assistant. Use the provided context to answer the user's question.

Context:
{context_str}

Question: {query}

Answer:"""
        
        response = self.gemini_model.generate_content(prompt)
        return response.text

rag_service = RAGService()