import requests

# Simple ingest test
print("Testing /ingest endpoint...")
try:
    response = requests.post(
        "http://localhost:8000/ingest",
        json={"text": "Test document"},
        timeout=10
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
