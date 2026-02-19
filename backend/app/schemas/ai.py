from pydantic import BaseModel, Field
from typing import List
class ResumeQuestionRequest(BaseModel):
    question: str
class JobMatchRequest(BaseModel):
    job_description: str = Field(
        ...,
        description="Paste the full job description here. Multiline text supported."
    )


class JobMatchResponse(BaseModel):
    fit_score: int
    matching_skills: List[str]
    missing_skills: List[str]
    suggestions: str

class JobMatchSwaggerInput(BaseModel):
    job_description: str
