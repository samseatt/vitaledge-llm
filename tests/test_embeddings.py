# tests/test_embeddings.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_embeddings():
    response = client.post("/embeddings", json={"texts": ["Test 1", "Test 2"]})
    assert response.status_code == 200
    assert response.json() == {
        "embeddings": [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]]
    }
