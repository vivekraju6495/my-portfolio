import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Certification(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    name = Column(String(255), nullable=False)
    issuer = Column(String(255), nullable=True)
    year = Column(String(10), nullable=True)
