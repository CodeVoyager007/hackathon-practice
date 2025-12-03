import os
from rag_service import rag_service
from pathlib import Path

def ingest_local_docs():
    script_dir = Path(__file__).parent.resolve()
    docs_path = script_dir / "../frontend/docs"
    print(f"Looking for documents in: {docs_path.resolve()}")
    
    files = list(docs_path.rglob("*.md*"))
    print(f"Found {len(files)} files to ingest.")
    
    total_points = 0
    for file_path in files:
        print(f"Ingesting {file_path}...")
        try:
            points_count = rag_service.upsert_document_from_file(str(file_path))
            total_points += points_count
            print(f"Successfully ingested {file_path}, {points_count} points.")
        except Exception as e:
            print(f"Failed to ingest {file_path}: {e}")
    print(f"\nTotal points ingested: {total_points}")

if __name__ == "__main__":
    ingest_local_docs()
