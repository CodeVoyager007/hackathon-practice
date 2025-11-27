import google.generativeai as genai
from settings import settings

# Configure and test native SDK
genai.configure(api_key=settings.GEMINI_API_KEY)

# Test text generation
print("Testing Gemini native SDK...")
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Say hello!")
    print(f"✓ Success: {response.text}")
except Exception as e:
    print(f"✗ Error: {e}")

# Try alternative model names
for model_name in ['gemini-pro', 'gemini-1.5-pro']:
    print(f"\nTrying {model_name}...")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Say hello!")
        print(f"  ✓ Success: {response.text}")
        break
    except Exception as e:
        print(f"  ✗ Error: {str(e)[:100]}")
