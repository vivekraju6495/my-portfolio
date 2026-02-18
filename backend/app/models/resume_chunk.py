from sqlalchemy import Column, Integer, String, Text
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import ARRAY
from app.core.database import Base

class ResumeChunk(Base):
    __tablename__ = "resume_chunks"

    id = Column(Integer, primary_key=True, index=True)
    chunk_text = Column(Text, nullable=False)
    embedding = Column(Vector(4096))
    category = Column(String, nullable=True)

