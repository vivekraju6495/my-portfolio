from sqlalchemy import text
from app.core.database import SessionLocal
from app.services.embedding_service import EmbeddingService
from app.services.llm_service import LLMService
class ResumeRAGService:

    def __init__(self):
        self.embedder = EmbeddingService()
        self.llm = LLMService()

    def _detect_categories(self, question: str) -> list[str]:
        q = question.lower()
        categories = []

        # Skills intent
        if any(word in q for word in [
            "skill", "skills", "tech stack", "technologies", "abilities", "expertise"
        ]):
            categories.append("skills")

        # Projects intent
        if any(word in q for word in [
            "project", "projects", "portfolio", "apps", "applications", "work i built"
        ]):
            categories.append("projects")

        # Experience intent
        if any(word in q for word in [
            "experience", "work history", "roles", "jobs", "positions"
        ]):
            categories.append("experience")

        # Education intent
        if any(word in q for word in [
            "education", "degree", "university", "college", "school"
        ]):
            categories.append("education")

        # Certifications intent
        if any(word in q for word in [
            "certification", "certifications", "certificate", "certificates", "courses"
        ]):
            categories.append("certifications")

        return categories


    async def answer_question(self, question: str) -> str:
        db = SessionLocal()

        # 1. Embed the question
        query_embedding = await self.embedder.embed(question)

        # 2. Detect categories from the question
        categories = self._detect_categories(question)

        # 3. Category-aware retrieval
        if categories:
            rows = db.execute(
                text("""
                    SELECT chunk_text
                    FROM resume_chunks
                    WHERE category = ANY(:categories)
                    ORDER BY embedding <-> (:query_embedding)::vector
                    LIMIT 25
                """),
                {"categories": categories, "query_embedding": query_embedding},
            ).fetchall()
        else:
            rows = db.execute(
                text("""
                    SELECT chunk_text
                    FROM resume_chunks
                    ORDER BY embedding <-> (:query_embedding)::vector
                    LIMIT 25
                """),
                {"query_embedding": query_embedding},
            ).fetchall()

        context = "\n".join([row.chunk_text for row in rows])

        prompt = f"""
                You are an AI assistant answering questions about Vivek's resume.
                Use ONLY the provided resume context. Do not make up information.

                Resume Context:
                {context}

                Question:
                {question}

                Answer:
                """

        answer = await self.llm.generate(prompt)

        db.close()
        return answer
