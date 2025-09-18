from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Routers
from backend.api.routes import router as api_router

# Observability
from backend.observability.logging_config import setup_logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---------- Startup ----------
    setup_logging()
    print("✅ Application startup complete")

    yield  # Application runs here

    # ---------- Shutdown ----------
    print("🛑 Application shutdown complete")


# Initialize FastAPI with lifespan
app = FastAPI(lifespan=lifespan)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router)



