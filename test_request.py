import requests

API_URL = "http://localhost:8000/plan"

payload = {
    "goal": "muscle gain",
    "diet": "high protein",
    "duration": 7
}

response = requests.post(API_URL, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())
