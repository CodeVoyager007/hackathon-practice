import os
from dotenv import load_dotenv

# Load environment variables from a .env file in the parent directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

class Settings:
    """
    Configuration settings for the application.
    """
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    QDRANT_URL: str = os.getenv("QDRANT_URL")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY")

settings = Settings()
