from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class AnalyticsSchema(BaseModel):
    id: int
    uuid: UUID
    visitors_count: int
    resume_download_count: int
    last_updated: datetime

    class Config:
        from_attributes = True
