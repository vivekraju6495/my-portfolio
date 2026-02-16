from sqlalchemy.orm import Session
from app.models.analytics import Analytics
from datetime import datetime

class AnalyticsService:

    @staticmethod
    def get_analytics(db: Session):
        return db.query(Analytics).first()

    @staticmethod
    def increment_visitors(db: Session):
        analytics = AnalyticsService.get_analytics(db)
        analytics.visitors_count += 1
        analytics.last_updated = datetime.utcnow()
        db.commit()
        db.refresh(analytics)
        return analytics

    @staticmethod
    def increment_resume_downloads(db: Session):
        analytics = AnalyticsService.get_analytics(db)
        analytics.resume_download_count += 1
        analytics.last_updated = datetime.utcnow()
        db.commit()
        db.refresh(analytics)
        return analytics

    @staticmethod
    def increment_page_views(db: Session):
        analytics = AnalyticsService.get_analytics(db)
        analytics.page_view_count += 1
        analytics.last_updated = datetime.utcnow()
        db.commit()
        db.refresh(analytics)
        return analytics

    @staticmethod
    def increment_api_hits(db: Session):
        analytics = AnalyticsService.get_analytics(db)
        analytics.api_hit_count += 1
        analytics.last_updated = datetime.utcnow()
        db.commit()
        db.refresh(analytics)
        return analytics
