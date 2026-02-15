from fastapi import FastAPI
from app.api.v1.routes import profile
from app.core.config import setup_cors
from fastapi.responses import JSONResponse
from fastapi import Request
from app.schemas.common import ResponseModel

app = FastAPI(
    title="Vivek Portfolio API",
    description="Backend API powering my AI portfolio.",
    version="1.0.0",
    openapi_tags=[
        {"name": "Profile", "description": "Resume and personal info"},
        {"name": "Experience", "description": "Work history"},
        {"name": "Projects", "description": "Portfolio projects"},
        {"name": "AI", "description": "LLM-powered tools"},
    ]
)
setup_cors(app)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=ResponseModel(
            success=False,
            message=str(exc),
            status=500,
            data=None
        ).model_dump()
    )

app.include_router(profile.router, prefix="/api/v1")

@app.get("/health", response_model=ResponseModel)
def health():
    return ResponseModel(
        success=True,
        message="Health check successful",
        status=200,
        data={"status": "ok"}
    )

