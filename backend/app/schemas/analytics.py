import uuid
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.core.database import Base

class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    visitors_count = Column(Integer, default=0)
    resume_download_count = Column(Integer, default=0)
    last_updated = Column(DateTime, default=datetime.utcnow)
