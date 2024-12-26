# tests/test_inference.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_inference():
    response = client.post("/inference", json={"prompt": "Test prompt"})
    assert response.status_code == 200
    assert response.json() == {"response": "Mock response for prompt: Test prompt"}
