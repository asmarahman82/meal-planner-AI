import sys, os
import pytest
from fastapi.testclient import TestClient

# Make sure backend is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.main import app

client = TestClient(app)


def test_healthcheck():
    """Simple health check for root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_meal_plan():
    """Test meal plan generation"""
    payload = {
        "goal": "muscle gain",
        "diet": "high protein",
        "duration": 7
    }
    response = client.post("/meal-plan", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "meal_plan" in data
    assert isinstance(data["meal_plan"], list)


def test_full_plan():
    """Test full pipeline: meals → groceries → workouts"""
    payload = {
        "goal": "weight loss",
        "diet": "low carb",
        "duration": 5
    }
    response = client.post("/full-plan", json=payload)
    assert response.status_code == 200
    data = response.json()
    # Expect all three parts of pipeline
    assert "meal_plan" in data
    assert "grocery_list" in data
    assert "workout_plan" in data


def test_metrics():
    """Test metrics endpoint returns JSON"""
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "meal_plans_generated" in data
    assert "avg_response_time" in data
