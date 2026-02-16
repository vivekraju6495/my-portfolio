import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    degree = Column(String(255), nullable=False)
    university = Column(String(255), nullable=True)
    start_year = Column(String(10), nullable=True)
    end_year = Column(String(10), nullable=True)
