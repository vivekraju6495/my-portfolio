from app.core.database import SessionLocal
from app.services.embedding_service import EmbeddingService
from sqlalchemy import text

# to run script python -m scripts.ingest_resume

class ResumeIngestService:

    def ingest_from_db(self):
        db = SessionLocal()
        embedder = EmbeddingService()

        # 0. Clear old chunks (fresh rebuild)
        # ---------------------------------------------------------
        db.execute(text("TRUNCATE TABLE resume_chunks"))
        db.commit()

        # 1. Fetch all resume-related tables (correct column names)
        profile = db.execute(text("""
            SELECT summary 
            FROM profiles
        """)).fetchall()

        experience = db.execute(text("""
            SELECT job_title, company, tech_stack 
            FROM experience
        """)).fetchall()

        experience_achievements = db.execute(text("""
            SELECT achievement_text 
            FROM experience_achievements
        """)).fetchall()

        education = db.execute(text("""
            SELECT degree, university, start_year, end_year 
            FROM educations
        """)).fetchall()

        skills = db.execute(text("""
            SELECT skill_name, category 
            FROM skills
        """)).fetchall()

        projects = db.execute(text("""
            SELECT project_name, role, description, tech_stack, project_url, github_url, doc_url 
            FROM projects
        """)).fetchall()

        project_achievements = db.execute(text("""
            SELECT achievement_text 
            FROM project_achievements
        """)).fetchall()

        certifications = db.execute(text("""
            SELECT name, issuer, year 
            FROM certifications
        """)).fetchall()

        # 2. Convert to text blocks
        blocks = []

        # Profile summary
        for row in profile:
            blocks.append(row.summary)

        # Experience
        for row in experience:
            blocks.append(
                f"{row.job_title} at {row.company}. Tech stack used: {row.tech_stack}"
            )

        # Experience achievements
        for row in experience_achievements:
            blocks.append(row.achievement_text)

        # Education
        for row in education:
            blocks.append(
                f"{row.degree} from {row.university} ({row.start_year} - {row.end_year})"
            )

        # Skills
        for row in skills:
            blocks.append(f"{row.category}: {row.skill_name}")

        # Projects
        for row in projects:
            blocks.append(
                f"{row.project_name} — Role: {row.role}. "
                f"{row.description}. Tech stack: {row.tech_stack}. "
                f"Links: {row.project_url}, {row.github_url}, {row.doc_url}"
            )

        # Project achievements
        for row in project_achievements:
            blocks.append(row.achievement_text)

        # Certifications
        for row in certifications:
            blocks.append(
                f"{row.name} issued by {row.issuer} in {row.year}"
            )

        # 3. Chunk + embed + store
        for block in blocks:
            embedding = embedder.embed_sync(block)

            db.execute(
                text("""
                    INSERT INTO resume_chunks (chunk_text, embedding)
                    VALUES (:chunk_text, :embedding)
                """),
                {"chunk_text": block, "embedding": embedding}
            )

        db.commit()
        db.close()
