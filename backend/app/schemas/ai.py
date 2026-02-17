from pydantic import BaseModel

class ResumeQuestionRequest(BaseModel):
    question: str

