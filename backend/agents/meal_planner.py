import requests
import os

def meal_planner(user_profile: dict):
    """
    Fetch a simple meal plan from TheMealDB (free API).
    """
    try:
        base_url = os.getenv("MEAL_API_BASE", "https://www.themealdb.com/api/json/v1/1")
        query = "chicken" if user_profile.get("goal") == "muscle gain" else "salad"
        url = f"{base_url}/search.php?s={query}"

        resp = requests.get(url, timeout=10)
        data = resp.json()

        return {
            "recommended_query": query,
            "meals": data.get("meals", []),
            "calories": 2200 if user_profile.get("goal") == "muscle gain" else 1800
        }

    except Exception as e:
        return {"error": f"Meal API failed: {str(e)}"}
