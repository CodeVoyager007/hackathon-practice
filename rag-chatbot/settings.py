import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_URL", ":memory:")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/"
    EMBEDDING_MODEL = "text-embedding-004"
    CHAT_MODEL = "gemini-flash-lite-latest"  # Free tier available model

settings = Settings()
