import requests

print("Testing chat endpoint ONLY...")
try:
    # First ingest a document
    ingest_resp = requests.post(
        "http://localhost:8000/ingest",
        json={"text": "Python is a programming language."},
        timeout=10
    )
    print(f"Ingest: {ingest_resp.status_code}")
    
    # Wait a moment
    import time
    time.sleep(2)
    
    # Now test chat
    chat_resp = requests.post(
        "http://localhost:8000/chat",
        json={"query": "What is Python?"},
        timeout=30
    )
    print(f"Chat Status: {chat_resp.status_code}")
    print(f"Chat Response: {chat_resp.text}")
    
    if chat_resp.status_code == 200:
        print(f"\n✓ SUCCESS! Answer: {chat_resp.json().get('answer')}")
    else:
        print(f"\n✗ FAILED")
        
except Exception as e:
    print(f"Exception: {e}")
