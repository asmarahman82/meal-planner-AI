from fastapi import APIRouter
from backend.api.models import UserProfile
from backend.agents.combined_pipeline import run_full_pipeline
from backend.observability.metrics import get_metrics

router = APIRouter()

@router.get("/")
async def healthcheck():
    return {"status": "ok"}

@router.post("/plan")
async def generate_plan(profile: UserProfile):
    try:
        return run_full_pipeline(profile.dict())
    except Exception as e:
        import traceback
        traceback_str = traceback.format_exc()
        return {"error": str(e), "traceback": traceback_str}


@router.get("/metrics")
async def metrics():
    """
    Return application metrics (meal plans generated, response times, failures).
    """
    return get_metrics()

@router.post("/plan")
async def generate_plan(profile: UserProfile):
    try:
        return run_full_pipeline(profile.dict())
    except Exception as e:
        import traceback
        traceback_str = traceback.format_exc()
        return {"error": str(e), "traceback": traceback_str}
