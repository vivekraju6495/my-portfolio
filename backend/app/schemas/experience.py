from uuid import UUID
from pydantic import BaseModel

class ExperienceAchievementSchema(BaseModel):
    uuid: UUID
    achievement_text: str

    class Config:
        from_attributes = True
        
class ExperienceSchema(BaseModel):
    uuid: UUID
    job_title: str
    company: str
    start_date: str
    end_date: str
    tech_stack: str
    achievements: list[ExperienceAchievementSchema]

    class Config:
        from_attributes = True
