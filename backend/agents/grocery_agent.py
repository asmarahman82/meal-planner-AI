import os, requests
from backend.observability.tracing import start_trace, log_event

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HF_MODEL = "facebook/bart-large-cnn"

def grocery_agent(user_input: dict):
    trace = start_trace("grocery_agent")
    try:
        # Groq / HF logic here ...
        raise Exception("Simulated failure")  # remove when APIs working

    except Exception as e:
        log_event(trace, f"Grocery Agent failed: {str(e)}")
        return {
            "grocery_list": [
                {"item": "Chicken Breast", "category": "Protein"},
                {"item": "Rice", "category": "Grains"},
                {"item": "Broccoli", "category": "Vegetables"},
                {"item": "Olive Oil", "category": "Other"},
            ]
        }



