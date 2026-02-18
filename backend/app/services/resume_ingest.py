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

        skills = db.execute(text("SELECT skill_name, category FROM skills")).fetchall()

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
            blocks.append((row.summary, "profile"))


        # Experience
        for row in experience:
            text_block = f"{row.job_title} at {row.company}. Tech stack used: {row.tech_stack}"
            blocks.append((text_block, "experience"))


        # Experience achievements
        for row in experience_achievements:
            blocks.append((row.achievement_text, "experience_achievements"))

        # Education
        for row in education:
            text_block = f"{row.degree} from {row.university} ({row.start_year} - {row.end_year})"
            blocks.append((text_block, "education"))


        # Skills
        # for row in skills:
        #     blocks.append(f"{row.category}: {row.skill_name}")

        grouped = {}

        for s in skills:
            cat = s.category or "Other"
            if cat not in grouped:
                grouped[cat] = []
            grouped[cat].append(s.skill_name)

        # Create semantic chunks
        for category, items in grouped.items():
            chunk = f"{category} Skills: " + ", ".join(items)
            blocks.append((chunk, "skills"))

        # Projects
        for row in projects:
            text_block = (
                f"{row.project_name} — Role: {row.role}. "
                f"{row.description}. Tech stack: {row.tech_stack}. "
                f"Links: {row.project_url}, {row.github_url}, {row.doc_url}"
            )
            blocks.append((text_block, "projects"))


        # Project achievements
        for row in project_achievements:
            blocks.append((row.achievement_text, "project_achievements"))

        # Certifications
        for row in certifications:
            text_block = f"{row.name} issued by {row.issuer} in {row.year}"
            blocks.append((text_block, "certifications"))


        # 3. Chunk + embed + store
        for block_text, category in blocks:
            embedding = embedder.embed_sync(block_text)

            db.execute(
                text("""
                    INSERT INTO resume_chunks (chunk_text, embedding, category)
                    VALUES (:chunk_text, :embedding, :category)
                """),
                {
                    "chunk_text": block_text,
                    "embedding": embedding,
                    "category": category,
                },
            )


        db.commit()
        db.close()
