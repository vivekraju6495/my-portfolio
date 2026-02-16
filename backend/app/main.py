from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.settings import settings
from app.core.config import setup_cors
from app.schemas.common import ResponseModel
from app.core.response import success_response, error_response

from app.api.v1.routes import (
    profile,
    skills,
    experience,
    projects,
    educations,
    certifications,
    contact_messages,
    suggestions,
    analytics,
)

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API powering my AI portfolio.",
    version="1.0.0",
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
@app.get("/health", response_model=ResponseModel)
def health():
    return success_response(
        message="Health check successful",
        data={"status": "ok"}
    )


# -----------------------------
# API Routers
# -----------------------------
app.include_router(profile.router, prefix="/api/v1/profile", tags=["Profile"])
app.include_router(skills.router, prefix="/api/v1/skills", tags=["Skills"])
app.include_router(experience.router, prefix="/api/v1/experience", tags=["Experience"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["Projects"])
app.include_router(educations.router, prefix="/api/v1/education", tags=["Educations"])
app.include_router(certifications.router, prefix="/api/v1/certifications", tags=["Certifications"])

app.include_router(contact_messages.router, prefix="/api/v1/contact", tags=["Contact Messages"])
app.include_router(suggestions.router, prefix="/api/v1/suggestions", tags=["Suggestions"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])
