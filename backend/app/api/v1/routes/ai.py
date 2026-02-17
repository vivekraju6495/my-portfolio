from fastapi import APIRouter
from app.schemas.ai import ResumeQuestionRequest
from app.services.rag_service import ResumeRAGService

router = APIRouter()

@router.post("/resume/ask")
async def ask_resume_question(payload: ResumeQuestionRequest):
    service = ResumeRAGService()
    answer = await service.answer_question(payload.question)
    return {"answer": answer}

