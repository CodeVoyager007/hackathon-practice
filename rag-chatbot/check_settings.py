from settings import settings
import os

print(f"QDRANT_URL: '{settings.QDRANT_URL}'")
print(f"GEMINI_API_KEY set: {bool(settings.GEMINI_API_KEY)}")
if settings.GEMINI_API_KEY:
    print(f"GEMINI_API_KEY length: {len(settings.GEMINI_API_KEY)}")
    print(f"GEMINI_API_KEY prefix: {settings.GEMINI_API_KEY[:4]}...")

print(f"QDRANT_API_KEY set: {bool(settings.QDRANT_API_KEY)}")
