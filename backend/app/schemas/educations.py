from uuid import UUID
from pydantic import BaseModel


class EducationSchema(BaseModel):
    uuid: UUID
    degree: str
    university: str
    start_year: str
    end_year: str

    class Config:
        from_attributes = True
