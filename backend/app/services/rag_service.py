from sqlalchemy import text
from app.core.database import SessionLocal
from app.services.embedding_service import EmbeddingService
from app.services.llm_service import LLMService  # you will create this next

class ResumeRAGService:

    async def answer_question(self, question: str) -> str:
        db = SessionLocal()
        embedder = EmbeddingService()
        llm = LLMService()

        # 1. Embed the question
        query_embedding = await embedder.embed(question)

        # 2. Retrieve top matching chunks
        rows = db.execute(
            text("""
                SELECT chunk_text
                FROM resume_chunks
                ORDER BY embedding <-> :query_embedding
                LIMIT 5
            """),
            {"query_embedding": query_embedding}
        ).fetchall()

        context = "\n".join([row.chunk_text for row in rows])

        # 3. Build prompt
        prompt = f"""
                You are an AI assistant answering questions about Vivek's resume.
                Use ONLY the provided resume context. Do not make up information.

                Resume Context:
                {context}

                Question:
                {question}

                Answer:
                """

        # 4. Get answer from LLM
        answer = await llm.generate(prompt)

        db.close()
        return answer

