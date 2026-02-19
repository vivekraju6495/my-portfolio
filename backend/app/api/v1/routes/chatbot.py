from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.schemas.chat import ResumeChatRequest, ResumeChatResponse
from app.services.resume_chat_service import ResumeChatService

router = APIRouter()

resume_chat_service = ResumeChatService()

class ResumeChatRequest(BaseModel):
    message: str
    mode: str | None = "default"  # 'default' | 'recruiter' | 'kid'


@router.post("/resume", response_model=ResumeChatResponse)
async def resume_chat(payload: ResumeChatRequest):
    msg = payload.message.strip()
    if not msg:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    reply = await resume_chat_service.chat(msg, mode=payload.mode or "default")
    return ResumeChatResponse(reply=reply)
