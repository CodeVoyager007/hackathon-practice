import requests
import time

BASE_URL = "http://localhost:8000"

def test_full_rag_pipeline():
    print("=" * 50)
    print("COMPREHENSIVE RAG BACKEND TEST")
    print("=" * 50)
    
    # Test 1: Ingest documents
    print("\n[1/3] Testing document ingestion...")
    docs = [
        "Python is a high-level, general-purpose programming language.",
        "FastAPI is a modern, fast web framework for building APIs with Python.",
        "Qdrant is a vector database designed for similarity search."
    ]
    
    for i, doc in enumerate(docs, 1):
        try:
            response = requests.post(f"{BASE_URL}/ingest", json={"text": doc})
            if response.status_code == 200:
                print(f"  ✓ Document {i} ingested successfully")
            else:
                print(f"  ✗ Document {i} failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"  ✗ Error ingesting document {i}: {e}")
            return False
    
    # Wait for indexing
    print("\n[2/3] Waiting for indexing...")
    time.sleep(2)
    
    # Test 2: Query the system
    print("\n[3/3] Testing RAG queries...")
    queries = [
        "What is Python?",
        "Tell me about FastAPI",
        "What is Qdrant used for?"
    ]
    
    for i, query in enumerate(queries, 1):
        try:
            response = requests.post(f"{BASE_URL}/chat", json={"query": query})
            if response.status_code == 200:
                answer = response.json().get("answer", "")
                print(f"\n  Query {i}: {query}")
                print(f"  Answer: {answer[:100]}...")
            else:
                print(f"  ✗ Query {i} failed: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"  ✗ Error with query {i}: {e}")
            return False
    
    print("\n" + "=" * 50)
    print("ALL TESTS PASSED! ✓")
    print("=" * 50)
    return True

if __name__ == "__main__":
    success = test_full_rag_pipeline()
    exit(0 if success else 1)
