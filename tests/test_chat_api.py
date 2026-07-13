from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ask_question_returns_grounded_answer():
    resp = client.post("/api/chat/", json={"question": "What is the vacation policy?"})
    assert resp.status_code == 200

    data = resp.json()
    assert isinstance(data["answer"], str) and data["answer"]
    assert isinstance(data["sources"], list)
    assert isinstance(data["confidence"], float)
    assert isinstance(data["latency"], float)


def test_empty_question_is_rejected():
    resp = client.post("/api/chat/", json={"question": "   "})
    assert resp.status_code == 400


def test_chat_history_endpoint_ok():
    client.post("/api/chat/", json={"question": "What is the vacation policy?"})
    resp = client.get("/api/chat/history")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
