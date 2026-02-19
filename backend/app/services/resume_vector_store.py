from typing import List
from sqlalchemy import text
from app.services.embedding_service import EmbeddingService
from app.core.database import SessionLocal


class ResumeVectorStore:
    def __init__(self):
        self.embedder = EmbeddingService()

    async def search(self, query: str, limit: int = 5, category: str | None = None) -> List[str]:
        query_embedding = await self.embedder.embed(query)

        db = SessionLocal()

        try:
            if category:
                rows = db.execute(
                    text("""
                        SELECT chunk_text
                        FROM resume_chunks
                        WHERE category = :category
                        ORDER BY embedding <-> (:embedding)::vector
                        LIMIT :limit
                    """),
                    {
                        "category": category,
                        "embedding": query_embedding,
                        "limit": limit
                    }
                ).fetchall()
            else:
                rows = db.execute(
                    text("""
                        SELECT chunk_text
                        FROM resume_chunks
                        ORDER BY embedding <-> (:embedding)::vector
                        LIMIT :limit
                    """),
                    {
                        "embedding": query_embedding,
                        "limit": limit
                    }
                ).fetchall()

            return [r.chunk_text for r in rows]

        finally:
            db.close()

