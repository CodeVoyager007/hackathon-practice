import pytest
from fastapi.testclient import TestClient
from app.main import app

# Note: This is a very basic integration test.
# A more robust test would mock the Gemini API and Qdrant database
# to avoid external dependencies and ensure predictable results.

@pytest.fixture(scope="module")
def client():
    """
    Create a test client for the FastAPI app.
    """
    with TestClient(app) as c:
        yield c

def test_read_root(client):
    """
    Test the root endpoint.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# This test is marked to be skipped by default because it makes a live
# call to the Gemini API and requires the `.env` file to be set up correctly.
# In a real CI/CD environment, this would be handled with secrets and
# potentially a dedicated test database.
@pytest.mark.skip(reason="Requires live API keys and populated database")
def test_rag_endpoint(client):
    """
    Test the /api/chat/rag endpoint.
    This is a basic happy-path test.
    """
    response = client.post("/api/chat/rag", json={"question": "What is the main topic of the book?"})
    
    assert response.status_code == 200
    json_response = response.json()
    assert "answer" in json_response
    assert "sources" in json_response
    assert isinstance(json_response["answer"], str)
    assert isinstance(json_response["sources"], list)
