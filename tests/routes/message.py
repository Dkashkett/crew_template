from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_message_endpoint():
    response = client.post("/api/message", json={"user_message": "Hello"})
    assert response.status_code == 200
    assert "agent_message" in response.json()
