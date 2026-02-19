from pydantic import BaseModel

class ResumeChatRequest(BaseModel):
    message: str

class ResumeChatResponse(BaseModel):
    reply: str
