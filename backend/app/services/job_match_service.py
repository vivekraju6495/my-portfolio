from sqlalchemy import text
from app.core.database import SessionLocal
from app.services.embedding_service import EmbeddingService
from app.services.llm_service import LLMService


class JobMatchService:
    def __init__(self):
        self.embedder = EmbeddingService()
        self.llm = LLMService()

    async def analyze(self, job_description: str) -> dict:
        db = SessionLocal()

        # 1) Embed JD (for future use / ranking if needed)
        jd_embedding = await self.embedder.embed(job_description)

        # 2) Pull resume SKILLS chunks
        rows = db.execute(
            text("""
                SELECT chunk_text
                FROM resume_chunks
                WHERE category = 'skills'
                ORDER BY embedding <-> (:jd_embedding)::vector
                LIMIT 15
            """),
            {"jd_embedding": jd_embedding},
        ).fetchall()

        resume_skill_text = " ".join(r.chunk_text for r in rows) if rows else ""

        # 3) Extract skills from JD
        jd_extract_prompt = f"""
        You are an expert ATS and technical recruiter.

        Task: Extract ONLY the hard technical skills and technologies from the job description below.
        Ignore benefits, culture, company info, DEI statements, and legal text.
        Ignore soft skills like communication, leadership, collaboration, etc.

        Return the skills as a comma-separated list, with no extra text.

        Job Description:
        {job_description}
        """

        jd_skills_raw = await self.llm.generate(jd_extract_prompt)
        jd_skills = [s.strip() for s in jd_skills_raw.split(",") if s.strip()]

        # 4) Extract skills from resume
        resume_extract_prompt = f"""
        You are an expert ATS and technical recruiter.

        Task: Extract ONLY the hard technical skills and technologies from the resume text below.
        Return the skills as a comma-separated list, with no extra text.

        Resume Skills:
        {resume_skill_text}
        """

        resume_skills_raw = await self.llm.generate(resume_extract_prompt)
        resume_skills = [s.strip() for s in resume_skills_raw.split(",") if s.strip()]

        jd_lower = [s.lower() for s in jd_skills]
        resume_lower = [s.lower() for s in resume_skills]

        # 5) Matching / missing
        matching = [s for s in jd_skills if s.lower() in resume_lower]
        missing = [s for s in jd_skills if s.lower() not in resume_lower]

        # 6) Fit score
        if len(jd_skills) == 0:
            fit_score = 0
        else:
            fit_score = int((len(matching) / len(jd_skills)) * 100)

        # 7) Suggestions
        suggestion_prompt = f"""
        You are a senior technical recruiter.

        Based on the following:

        Job Description Skills: {jd_skills}
        Candidate Resume Skills: {resume_skills}
        Matching Skills: {matching}
        Missing Skills: {missing}
        Fit Score: {fit_score}%

        Write a concise, recruiter-friendly summary (4–6 sentences) explaining:

        - How well the candidate matches the role
        - Where they are strong
        - Which key skills are missing
        - Whether they seem like a reasonable fit to interview

        Do not repeat the lists verbatim. Just summarize.
        """

        suggestions = await self.llm.generate(suggestion_prompt)

        db.close()

        return {
            "fit_score": fit_score,
            "matching_skills": matching,
            "missing_skills": missing,
            "suggestions": suggestions.strip(),
        }
