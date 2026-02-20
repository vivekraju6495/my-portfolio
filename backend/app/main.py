from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging
import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter

from app.core.settings import settings
from app.core.config import setup_cors
from app.schemas.common import ResponseModel
from app.core.response import success_response, error_response

from app.api.v1.routes import (
    resume,
    profile,
    skills,
    experience,
    projects,
    educations,
    certifications,
    contact_messages,
    suggestions,
    analytics,
    ai,
    chatbot
)

from app.admin_tasks import router as admin_router


logger = logging.getLogger("uvicorn.error")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    try:
        redisconn = redis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True
        )
        await FastAPILimiter.init(redisconn)
        app.state.redis = redisconn
        logger.info("Redis rate limiter initialized successfully")
    except Exception as e:
        app.state.redis = None
        logger.error(f"Redis connection failed: {e}")
        logger.error("Rate limiting is DISABLED until Redis becomes available")

    yield  # App runs here

    # Shutdown (optional)
    # You can close redis connection here if needed


app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API powering my AI portfolio.",
    version="1.0.0",
    lifespan=lifespan
)

# Setup CORS
setup_cors(app)

# -----------------------------
# Global Exception Handler
# -----------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=error_response(
            message=str(exc),
            status=500,
            data=None
        ).model_dump()
    )

# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def root():
    return {"service": "alive"}

@app.get("/check")
def root():
    return {"service": "alive"}


@app.get("/health", response_model=ResponseModel)
async def health(request: Request):
    redis_status = "unknown"

    redis_client = request.app.state.redis

    if redis_client:
        try:
            pong = await redis_client.ping()
            redis_status = "connected" if pong else "not responding"
        except Exception:
            redis_status = "failed"
    else:
        redis_status = "not initialized"

    return success_response(
        message="Health check successful",
        data={
            "status": "ok",
            "redis": redis_status
        }
    )

app.include_router(admin_router)

# -----------------------------
# API Routers
# -----------------------------
app.include_router(resume.router, prefix="/api/v1/resume", tags=["Resume"])

app.include_router(profile.router, prefix="/api/v1/profile", tags=["Profile"])
app.include_router(skills.router, prefix="/api/v1/skills", tags=["Skills"])
app.include_router(experience.router, prefix="/api/v1/experience", tags=["Experience"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["Projects"])
app.include_router(educations.router, prefix="/api/v1/education", tags=["Educations"])
app.include_router(certifications.router, prefix="/api/v1/certifications", tags=["Certifications"])

app.include_router(contact_messages.router, prefix="/api/v1/contact", tags=["Contact Messages"])
app.include_router(suggestions.router, prefix="/api/v1/suggestions", tags=["Suggestions"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])


app.include_router(ai.router, prefix="/api/v1/ai", tags=["AI"])
app.include_router(chatbot.router, prefix="/api/v1/ai", tags=["AI ChatBot"])

