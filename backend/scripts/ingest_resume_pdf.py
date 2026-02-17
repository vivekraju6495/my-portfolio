import asyncio
import os
from app.services.resume_ingest import ResumeIngestService
from app.utils.pdf_reader import extract_text_from_pdf

async def main():
    # Path to your PDF inside the backend folder
    pdf_path = os.path.join("app", "assets", "resume", "Vivek_Raju_Senior_Software_Engineer.pdf")

    # Extract text from PDF
    resume_text = extract_text_from_pdf(pdf_path)

    # Ingest into DB
    service = ResumeIngestService()
    await service.ingest_resume(resume_text)

asyncio.run(main())
