from pydantic import BaseModel, Field
from typing import List
class ResumeQuestionRequest(BaseModel):
    question: str
class JobMatchRequest(BaseModel):
    job_description: str = Field(
        ...,
        description="Paste the full job description here. Multiline text supported."
    )


    class Config:
        schema_extra = {
            "example": {
                "job_description": "We are hiring a Senior Backend Engineer with Java, Spring Boot, REST APIs, SQL, AWS..."
            }
        }


class JobMatchResponse(BaseModel):
    fit_score: int
    matching_skills: List[str]
    missing_skills: List[str]
    suggestions: str

    class Config:
        schema_extra = {
            "example": {
                "fit_score": 78,
                "matching_skills": ["REST APIs", "PostgreSQL", "AWS", "Docker"],
                "missing_skills": ["Java", "Spring Boot", "Kubernetes"],
                "suggestions": "You are a strong fit on backend and cloud skills, but lack core Java/Spring and Kubernetes experience."
            }
        }


class JobMatchSwaggerInput(BaseModel):
    job_description: str
