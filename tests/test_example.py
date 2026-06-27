from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_get_activities_returns_200_and_contains_chess_club():
    response = client.get("/activities")

    assert response.status_code == 200
    assert "Chess Club" in response.json()
