from openai import OpenAI
from settings import settings

client = OpenAI(
    api_key=settings.GEMINI_API_KEY,
    base_url=settings.GEMINI_BASE_URL
)

# Test different model names
model_names = [
    "gemini-1.5-flash",
    "models/gemini-1.5-flash",
    "gemini-1.5-flash-latest",
    "models/gemini-1.5-flash-latest",
    "gemini-pro",
    "models/gemini-pro"
]

for model_name in model_names:
    print(f"\nTesting model: {model_name}")
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": "Say hello"}
            ]
        )
        print(f"  ✓ SUCCESS: {response.choices[0].message.content}")
        break
    except Exception as e:
        print(f"  ✗ Failed: {str(e)[:100]}")
