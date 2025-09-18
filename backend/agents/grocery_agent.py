import requests
import os

def grocery_agent(user_profile: dict):
    """
    Fetch a grocery list from OpenFoodFacts (free API).
    """
    try:
        base_url = os.getenv("GROCERY_API_BASE", "https://world.openfoodfacts.org")
        url = f"{base_url}/cgi/search.pl?search_terms=milk&json=1&page_size=5"

        resp = requests.get(url, timeout=10)
        data = resp.json()

        items = [
            {"product": p.get("product_name", ""), "brand": p.get("brands", "")}
            for p in data.get("products", [])
        ]

        return items

    except Exception as e:
        return {"error": f"Grocery API failed: {str(e)}"}
