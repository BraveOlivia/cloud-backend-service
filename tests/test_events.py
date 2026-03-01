from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_create_event():
    payload = {"source_id": "sensor_001", "category": "temperature", "value": 20.5}
    r = client.post("/events", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["source_id"] == "sensor_001"
    assert data["category"] == "temperature"
    assert data["value"] == 20.5
    assert "id" in data

def test_get_events():
    r = client.get("/events")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_stats():
    r = client.get("/events/stats")
    assert r.status_code == 200
    data = r.json()
    assert "total_events" in data
