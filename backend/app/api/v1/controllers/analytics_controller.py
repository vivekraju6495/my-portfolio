from sqlalchemy.orm import Session
from app.schemas.analytics import AnalyticsSchema
from app.services.analytics_service import AnalyticsService

def get_analytics_controller(db: Session):
    analytics = AnalyticsService.get_analytics(db)
    if not analytics:
        raise Exception("Analytics data not found")
    return AnalyticsSchema.model_validate(analytics)

def increment_visitors_controller(db: Session):
    analytics = AnalyticsService.increment_visitors(db)
    return AnalyticsSchema.model_validate(analytics)

def increment_resume_downloads_controller(db: Session):
    analytics = AnalyticsService.increment_resume_downloads(db)
    return AnalyticsSchema.model_validate(analytics)

def increment_page_views_controller(db: Session):
    analytics = AnalyticsService.increment_page_views(db)
    return AnalyticsSchema.model_validate(analytics)

def increment_api_hits_controller(db: Session):
    analytics = AnalyticsService.increment_api_hits(db)
    return AnalyticsSchema.model_validate(analytics)
