from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_meal_plan():
    payload = {
        "weight": 70,
        "height": 170,
        "age": 25,
        "activity_level": "moderate",
        "goal": "weight loss",
        "diet": "balanced",
        "duration": 7
    }
    response = client.post("/plan", json=payload)
    assert response.status_code == 200
    result = response.json()

    # Ensure keys exist
    assert "meal_plan" in result
    assert "grocery_list" in result
    assert "workout_plan" in result
