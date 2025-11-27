import google.generativeai as genai
from settings import settings
import sys

genai.configure(api_key=settings.GEMINI_API_KEY)

# List available models
print("Listing available models...")
try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"  - {model.name}")
except Exception as e:
    print(f"Error listing models: {e}")
    sys.exit(1)

# Test the first working model
print("\nTesting first available text generation model...")
try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            model_name = model.name.replace('models/', '')
            print(f"\nTrying: {model_name}")
            test_model = genai.GenerativeModel(model_name)
            response = test_model.generate_content("Say hello!")
            print(f"✓ SUCCESS with {model_name}")
            print(f"Response: {response.text}")
            break
except Exception as e:
    print(f"✗ Error: {e}")
