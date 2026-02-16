from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.settings import settings
from app.core.config import setup_cors
from app.schemas.common import ResponseModel
from app.api.v1.routes import profile

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API powering my AI portfolio.",
    version="1.0.0",
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

