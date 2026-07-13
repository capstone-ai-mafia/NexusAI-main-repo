from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint_ok():
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "healthy"}


def test_root_endpoint_ok():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "message" in resp.json()
