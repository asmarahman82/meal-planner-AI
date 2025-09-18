import requests
import os

def workout_planner(user_profile: dict):
    """
    Fetch a workout plan from WGER (free API).
    """
    try:
        base_url = os.getenv("WORKOUT_API_BASE", "https://wger.de/api/v2")
        url = f"{base_url}/exerciseinfo/?limit=5"

        resp = requests.get(url, timeout=10)
        data = resp.json()

        exercises = [
            {"name": e.get("name", ""), "sets": 3, "reps": 12}
            for e in data.get("results", [])
        ]

        return {"exercises": exercises}

    except Exception as e:
        return {"error": f"Workout API failed: {str(e)}"}
