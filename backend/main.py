from fastapi import FastAPI
from backend.api.routes import router as api_router
from backend.observability.logging_config import setup_logging
from backend.observability.tracing import init_tracing

app = FastAPI(title="AI Meal & Fitness Planner")

@app.on_event("startup")
async def startup_event():
    setup_logging()
    init_tracing()
    print("✅ Application startup complete")

@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 Application shutdown complete")

# Attach routes
app.include_router(api_router)



