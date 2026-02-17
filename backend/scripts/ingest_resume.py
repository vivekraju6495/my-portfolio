from app.services.resume_ingest import ResumeIngestService

def main():
    service = ResumeIngestService()
    service.ingest_from_db()

if __name__ == "__main__":
    main()
