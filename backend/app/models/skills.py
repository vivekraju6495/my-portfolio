import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    category = Column(String(255), nullable=False)
    skill_name = Column(String(255), nullable=False)
