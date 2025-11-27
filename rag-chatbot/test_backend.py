import requests
import sys

BASE_URL = "http://localhost:8000"

def test_ingest():
    print("Testing /ingest...")
    try:
        response = requests.post(f"{BASE_URL}/ingest", json={"text": "Python is a high-level, general-purpose programming language."})
        if response.status_code == 200:
            print("Ingest successful:", response.json())
            return True
        else:
            print("Ingest failed:", response.status_code, response.text)
            return False
    except Exception as e:
        print("Ingest error:", e)
        return False

def test_chat():
    print("Testing /chat...")
    try:
        response = requests.post(f"{BASE_URL}/chat", json={"query": "What is Python?"})
        if response.status_code == 200:
            print("Chat successful:", response.json())
            return True
        else:
            print("Chat failed:", response.status_code, response.text)
            return False
    except Exception as e:
        print("Chat error:", e)
        return False

if __name__ == "__main__":
    # Ensure server is running before running this test
    # This is a simple check, in a real scenario we'd wait for the server
    if test_ingest() and test_chat():
        print("All tests passed!")
        sys.exit(0)
    else:
        print("Some tests failed.")
        sys.exit(1)
