import os, requests
from backend.observability.tracing import start_trace, log_event

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HF_MODEL = "facebook/bart-large-cnn"

def meal_planner(user_input: dict):
    trace = start_trace("meal_planner")
    try:
        # --- Option 1: Groq ---
        if GROQ_API_KEY:
            from groq import Groq
            client = Groq(api_key=GROQ_API_KEY)
            prompt = f"Create a {user_input['duration']}-day meal plan for a {user_input['age']} year old..."
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}],
            )
            return {"meal_plan": [
                {
                    "idMeal": "1001",
                    "strMeal": "AI Generated Meal",
                    "strCategory": "Other",
                    "strArea": "AI",
                    "strInstructions": completion.choices[0].message.content,
                }
            ]}

        # --- Option 2: Hugging Face ---
        elif HUGGINGFACE_API_KEY:
            headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
            payload = {"inputs": f"Create a {user_input['duration']}-day meal plan..."}
            response = requests.post(
                f"https://api-inference.huggingface.co/models/{HF_MODEL}",
                headers=headers, json=payload, timeout=60
            )
            if response.status_code == 200:
                text = response.json()[0]["summary_text"]
                return {"meal_plan": [
                    {
                        "idMeal": "1002",
                        "strMeal": "HF Generated Meal",
                        "strCategory": "Other",
                        "strArea": "AI",
                        "strInstructions": text,
                    }
                ]}
            else:
                raise Exception(f"Hugging Face error: {response.text}")

        else:
            raise Exception("No API key found.")

    except Exception as e:
        log_event(trace, f"Meal Planner failed: {str(e)}")
        # Fallback
        return {
            "meal_plan": [
                {
                    "idMeal": "100-fallback",
                    "strMeal": "Grilled Chicken with Rice",
                    "strCategory": "Protein",
                    "strArea": "Global",
                    "strInstructions": "Grill chicken breast and serve with boiled rice."
                }
            ]
        }
