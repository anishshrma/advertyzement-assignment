from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_banks():
    response = client.get("/api/banks/")
    assert response.status_code == 200
    assert response.json() == []

def test_get_branch():
    response = client.get("/api/branches/IFSC001")
    assert response.status_code == 404
    assert response.json() == {"detail": "Branch not found"}
