from app.services.embedding_service import EmbeddingService
from app.core.database import SessionLocal
from sqlalchemy import text


class ResumeIngestService:

    def ingest_resume(self, resume_text: str):
        chunks = self._split_into_chunks(resume_text)
        embedder = EmbeddingService()

        db = SessionLocal()

        try:
            for chunk in chunks:
                embedding = embedder.embed_sync(chunk)

                db.execute(
                    text("""
                        INSERT INTO resume_chunks (chunk_text, embedding)
                        VALUES (:chunk_text, :embedding)
                    """),
                    {"chunk_text": chunk, "embedding": embedding}
                )

            db.commit()

        finally:
            db.close()

    def _split_into_chunks(self, text: str, max_tokens: int = 300):
        words = text.split()
        chunks = []
        current = []
        count = 0

        for w in words:
            current.append(w)
            count += 1

            if count >= max_tokens:
                chunks.append(" ".join(current))
                current = []
                count = 0

        if current:
            chunks.append(" ".join(current))

        return chunks
