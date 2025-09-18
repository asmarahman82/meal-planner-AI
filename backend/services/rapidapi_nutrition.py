import os
import requests

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_NUTRITION_HOST", "calorieninjas.p.rapidapi.com")

def get_nutrition_data(food_name: str):
    """Fetch nutrition info using RapidAPI (CalorieNinjas example)."""
    url = f"https://{RAPIDAPI_HOST}/v1/nutrition"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }
    params = {"query": food_name}

    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code != 200:
        return {"food": food_name, "error": "nutrition lookup failed"}

    items = resp.json().get("items", [])
    if not items:
        return {"food": food_name, "error": "not found"}

    item = items[0]
    return {
        "food": food_name,
        "calories": item.get("calories"),
        "protein": item.get("protein_g"),
        "carbs": item.get("carbohydrates_total_g"),
        "fat": item.get("fat_total_g")
    }
