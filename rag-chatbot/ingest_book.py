import requests
import os
import glob

# Configuration
# The URL of your FastAPI application's ingest endpoint
BASE_URL = "http://localhost:8000"
INGEST_URL = f"{BASE_URL}/ingest"
# The directory where your book's markdown files are located
BOOK_DIR = "frontend/docs"

def ingest_book():
    """
    Reads all markdown files from the specified directory, splits them into paragraphs,
    and sends each paragraph to the chatbot's ingest service.
    """
    # Use glob to find all .md and .mdx files
    markdown_files = glob.glob(os.path.join(BOOK_DIR, "*.md")) + glob.glob(os.path.join(BOOK_DIR, "*.mdx"))

    if not markdown_files:
        print(f"No markdown files found in {os.path.abspath(BOOK_DIR)}")
        return

    print(f"Found {len(markdown_files)} files to ingest.")

    for file_path in markdown_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split content by paragraphs (double newline)
            chunks = [chunk.strip() for chunk in content.split('\n\n') if chunk.strip()]
            
            print(f"Ingesting {os.path.basename(file_path)} in {len(chunks)} chunks...")

            for i, chunk in enumerate(chunks):
                response = requests.post(INGEST_URL, json={"text": chunk})
                if response.status_code == 200:
                    print(f"  Successfully ingested chunk {i+1}/{len(chunks)}")
                else:
                    print(f"  Error ingesting chunk {i+1}/{len(chunks)}: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"An error occurred with file {file_path}: {e}")

if __name__ == "__main__":
    # First, check if the RAG service is running
    try:
        response = requests.get(BASE_URL)
        if response.status_code != 200:
            print(f"The RAG service does not appear to be running at {BASE_URL}")
            print("Please start the service by running 'python main.py' in the 'rag-chatbot' directory.")
        else:
            print("RAG service is running. Starting ingestion...")
            ingest_book()
            print("\nBook ingestion complete.")
    except requests.exceptions.ConnectionError:
        print(f"Could not connect to the RAG service at {BASE_URL}")
        print("Please start the service by running 'python main.py' in the 'rag-chatbot' directory.")