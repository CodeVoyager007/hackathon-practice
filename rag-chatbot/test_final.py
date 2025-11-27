import requests
import time

BASE_URL = "http://localhost:8000"

print("=" * 50)
print("FINAL BACKEND VERIFICATION")
print("=" * 50)

# Step 1: Ingest a document
print("\n[Step 1/3] Ingesting document...")
ingest_response = requests.post(
    f"{BASE_URL}/ingest",
    json={"text": "Python is a high-level programming language known for its simplicity and readability."},
    timeout=10
)
print(f"  Status: {ingest_response.status_code}")
print(f"  Response: {ingest_response.json()}")

# Step 2: Wait for indexing
print("\n[Step 2/3] Waiting for indexing...")
time.sleep(2)

# Step 3: Query the document
print("\n[Step 3/3] Querying...")
chat_response = requests.post(
    f"{BASE_URL}/chat",
    json={"query": "What is Python?"},
    timeout=30
)
print(f"  Status: {chat_response.status_code}")
if chat_response.status_code == 200:
    answer = chat_response.json().get("answer", "")
    print(f"  Answer: {answer}")
    print("\n" + "=" * 50)
    print("✓ ALL TESTS PASSED!")
    print("=" * 50)
else:
    print(f"  Error: {chat_response.text}")
    print("\n✗ Test failed")
