from openai import OpenAI
from settings import settings

client = OpenAI(
    api_key=settings.GEMINI_API_KEY,
    base_url=settings.GEMINI_BASE_URL
)

# Test embedding
try:
    response = client.embeddings.create(
        model="text-embedding-004",
        input="test"
    )
    print(f"Embedding success: {len(response.data[0].embedding)} dimensions")
except Exception as e:
    print(f"Embedding error: {e}")

# Try alternative model name
try:
    response = client.embeddings.create(
        model="models/text-embedding-004",
        input="test"
    )
    print(f"Alternative model success: {len(response.data[0].embedding)} dimensions")
except Exception as e:
    print(f"Alternative model error: {e}")
