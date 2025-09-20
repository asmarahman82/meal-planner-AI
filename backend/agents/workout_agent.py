import os, requests
from backend.observability.tracing import start_trace, log_event

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HF_MODEL = "facebook/bart-large-cnn"

def workout_agent(user_input: dict):
    trace = start_trace("workout_agent")
    try:
        # Groq / HF logic here ...
        raise Exception("Simulated failure")  # remove when APIs working

    except Exception as e:
        log_event(trace, f"Workout Agent failed: {str(e)}")
        return {
            "workout_plan": [
                {
                    "name": "Push Ups",
                    "muscle": "Chest",
                    "equipment": "Bodyweight",
                    "instructions": "Perform 3 sets of 12 reps."
                },
                {
                    "name": "Squats",
                    "muscle": "Legs",
                    "equipment": "Bodyweight",
                    "instructions": "Perform 3 sets of 15 reps."
                },
                {
                    "name": "Plank",
                    "muscle": "Core",
                    "equipment": "Bodyweight",
                    "instructions": "Hold for 60 seconds, 3 rounds."
                }
            ]
        }
