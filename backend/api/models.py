from pydantic import BaseModel

class UserProfile(BaseModel):
    weight: float          # kg
    height: float          # cm
    age: int
    activity_level: str    # sedentary, moderate, active
    goal: str              # muscle gain, weight loss, maintenance
    diet: str = "balanced" # optional
    duration: int = 7      # days
