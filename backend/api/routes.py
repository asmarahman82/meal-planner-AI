from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.agents.combined_pipeline import run_full_pipeline

router = APIRouter()

class UserInput(BaseModel):
    weight: float
    height: float
    age: int
    activity_level: str
    goal: str
    diet: str
    duration: int

@router.get("/")
def healthcheck():
    return {"status": "ok"}

@router.post("/plan")
def generate_plan(user_input: UserInput):
    try:
        result = run_full_pipeline(user_input.model_dump())
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
