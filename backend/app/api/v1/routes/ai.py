from fastapi import APIRouter, Body, HTTPException, Request
from app.schemas.ai import JobMatchRequest, JobMatchResponse, ResumeQuestionRequest, JobMatchSwaggerInput
from app.services.rag_service import ResumeRAGService
from app.services.job_match_service import JobMatchService
from app.utils.text_format import normalize_job_description

router = APIRouter()

@router.post("/resume/ask")
async def ask_resume_question(payload: ResumeQuestionRequest):
    service = ResumeRAGService()
    answer = await service.answer_question(payload.question)
    return {"answer": answer}


job_match_service = JobMatchService()

# @router.post("/resume/job-match", response_model=JobMatchResponse)
# async def job_match(request: Request):
#     content_type = request.headers.get("content-type", "")

#     # Case 1: JSON input
#     if "application/json" in content_type:
#         try:
#             body = await request.json()
#             job_description = body.get("job_description", "")
#         except:
#             raise HTTPException(status_code=400, detail="Invalid JSON body")
    
#     # Case 2: Plain text input
#     elif "text/plain" in content_type:
#         raw = await request.body()
#         job_description = raw.decode("utf-8")

#     else:
#         raise HTTPException(
#             status_code=415,
#             detail="Unsupported content type. Use application/json or text/plain."
#         )

#     # ⭐ Normalize the input
#     job_description = normalize_job_description(job_description)

#     # ⭐ Pass clean text to your service
#     return await job_match_service.analyze(job_description)


@router.post(
    "/resume/job-match",
    response_model=JobMatchResponse,
    openapi_extra={
        "requestBody": {
            "required": True,
            "content": {
                "application/json": {
                    "schema": JobMatchSwaggerInput.model_json_schema()
                },
                "text/plain": {
                    "schema": {"type": "string"}
                }
            }
        }
    }
)
async def job_match(request: Request):
    content_type = request.headers.get("content-type", "")

    # JSON input (Swagger, frontend JSON)
    if "application/json" in content_type:
        try:
            body = await request.json()
            job_description = body.get("job_description", "")
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid JSON body")

    # Plain text input (curl, frontend)
    elif "text/plain" in content_type:
        raw = await request.body()
        job_description = raw.decode("utf-8")

    else:
        raise HTTPException(
            status_code=415,
            detail="Unsupported content type. Use application/json or text/plain."
        )

    # Normalize
    job_description = normalize_job_description(job_description)

    # Analyze
    return await job_match_service.analyze(job_description)
