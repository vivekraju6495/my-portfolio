from uuid import uuid4
from app.core.database import SessionLocal

from app.models.profile import Profile
from app.models.skills import Skill
from app.models.experience import Experience
from app.models.experience_achievements import ExperienceAchievement
from app.models.projects import Project
from app.models.project_achievements import ProjectAchievement
from app.models.educations import Education
from app.models.certifications import Certification
from app.models.analytics import Analytics


def seed_profile(db):
    if db.query(Profile).first():
        return

    profile = Profile(
        uuid=uuid4(),
        name="Vivek Raju",
        title="Senior Software Engineer",
        location="Valrico, Florida, US",
        email="connect.vivek.95@gmail.com",
        phone="+1 813-498-2399",
        linkedin="https://linkedin.com/in/vivekraju95",
        github="https://github.com/vivekraju6495",
        work_auth="U.S. Permanent Resident (Green Card)",
        summary=(
            "Senior Software Engineer with 5+ years of experience building scalable REST APIs, cloud-native "
            "systems, and event-driven architectures. Strong experience in NestJS, Laravel, FastAPI, PostgreSQL, "
            "Kafka, Redis, and AWS, with hands-on experience supporting React and React Native frontends. "
            "Championed production-grade systems for SaaS, healthcare, and video platforms with a focus on secure "
            "APIs, microservices architecture, and reliable asynchronous processing."
        ),
    )
    db.add(profile)


def seed_skills(db):
    if db.query(Skill).first():
        return

    skills = [
        # Backend
        ("Backend", "NestJS"),
        ("Backend", "Node.js"),
        ("Backend", "TypeScript"),
        ("Backend", "Laravel"),
        ("Backend", "CodeIgniter"),
        ("Backend", "FastAPI"),
        ("Backend", "Odoo"),
        ("Backend", "PHP (v5.6+)"),
        ("Backend", "Python"),
        ("Backend", "JavaScript"),

        # Frontend
        ("Frontend", "React"),
        ("Frontend", "React Native"),
        ("Frontend", "Expo"),

        # Databases
        ("Databases", "PostgreSQL"),
        ("Databases", "MySQL"),
        ("Databases", "MongoDB"),
        ("Databases", "AWS RDS"),
        ("Databases", "MariaDB"),

        # Messaging & Caching
        ("Messaging", "Kafka"),
        ("Messaging", "Redis"),
        ("Messaging", "RabbitMQ"),

        # Cloud & Infra
        ("Cloud", "AWS S3"),
        ("Cloud", "AWS SQS"),
        ("Cloud", "AWS SNS"),
        ("Cloud", "AWS Lambda"),
        ("Cloud", "AWS IAM"),
        ("Cloud", "AWS CloudWatch"),
        ("Cloud", "Docker"),
        ("Cloud", "Docker Compose"),
        ("Cloud", "Infrastructure as Code"),

        # Security
        ("Security", "JWT"),
        ("Security", "OAuth2"),
        ("Security", "RBAC"),

        # Testing
        ("Testing", "Postman"),
        ("Testing", "Swagger/OpenAPI"),
        ("Testing", "Unit Testing"),
        ("Testing", "Integration Testing"),
        ("Testing", "E2E Testing"),

        # Integrations
        ("Integrations", "Stripe"),
        ("Integrations", "QuickBooks"),
        ("Integrations", "Avalara"),
        ("Integrations", "CyberSource"),
        ("Integrations", "OrbiPay"),
        ("Integrations", "Shippo"),
        ("Integrations", "Wowza"),

        # Media Processing
        ("Media", "Puppeteer"),
        ("Media", "FFmpeg"),

        # Search
        ("Search", "Elasticsearch"),

        # DevOps
        ("DevOps", "Git"),
        ("DevOps", "GitHub"),
        ("DevOps", "Bitbucket"),
        ("DevOps", "Jira"),
        ("DevOps", "Zoho Projects"),
        ("DevOps", "Confluence"),
    ]

    for category, name in skills:
        db.add(Skill(uuid=uuid4(), category=category, skill_name=name))


def seed_experience(db):
    if db.query(Experience).first():
        return

    #  IBIL Solutions — Senior Software Engineer
    exp1 = Experience(
        uuid=uuid4(),
        job_title="Senior Software Engineer",
        company="IBIL Solutions",
        start_date="2021-08-01",
        end_date="2025-10-01",
        tech_stack=(
            "NestJS, Laravel, Node.js, TypeScript, FastAPI, React/React Native, "
            "PostgreSQL, MySQL, MongoDB, Redis, Kafka, AWS (S3, SQS, SNS, RDS, Lambda), Docker"
        ),
    )
    db.add(exp1)
    db.flush()

    exp1_achievements = [
        "Architected and optimized high-performance RESTful APIs using NestJS and Laravel, resulting in a 35% improvement in average response times and a 20% reduction in server overhead.",
        "Streamlined business workflows by integrating payment, tax, and streaming services (Stripe, QuickBooks, Avalara, Wowza, Shippo), enabling automated billing processes that reduced manual operations by 60%.",
        "Strengthened system security by implementing robust JWT authentication and RBAC, which successfully decreased unauthorized access attempts by 40%.",
        "Established scalable asynchronous processing pipelines using Kafka and Redis (50k+ events/day), ensuring high system throughput and responsive frontend experiences.",
        "Drove team productivity by mentoring junior engineers and improving code quality standards, increasing team delivery velocity by 25%.",
        "Defined and documented API contracts between backend and frontend teams, reducing integration defects by 30% and accelerating feature delivery.",
        "Led technical design discussions that reduced deployment failures by 30% across 4 services.",
        "Conducted API validation and functional testing using Postman and Swagger, verifying request/response contracts, authentication flows, and error handling across development and staging environments before production releases.",
    ]

    for text in exp1_achievements:
        db.add(ExperienceAchievement(uuid=uuid4(), experience_id=exp1.id, achievement_text=text))

    # Freelance Software Engineer — Remote
    exp2 = Experience(
        uuid=uuid4(),
        job_title="Freelance Software Engineer",
        company="Remote",
        start_date="2020-12-01",
        end_date="2021-08-01",
        tech_stack="Laravel, CodeIgniter, FastAPI, React/React Native, Expo, PostgreSQL, MySQL, JWT",
    )
    db.add(exp2)
    db.flush()

    exp2_achievements = [
        "Delivered custom Laravel + React business applications that improved client operational efficiency by 40% through automation and dashboards.",
        "Engineered secure REST APIs using JWT and role-based access control (RBAC) for diverse business clients, streamlining user permission management and decreasing security-related integration defects by 30%.",
        "Deployed 15+ A/B tests on React-based landing pages, increasing conversion rates by 15% and improving user engagement metrics by 20%; findings presented directly to the CTO.",
        "Worked directly with clients to gather requirements, architect solutions, and deliver on tight timelines.",
    ]

    for text in exp2_achievements:
        db.add(ExperienceAchievement(uuid=uuid4(), experience_id=exp2.id, achievement_text=text))

    # Hafisoft Technologies — Software Engineer
    exp3 = Experience(
        uuid=uuid4(),
        job_title="Software Engineer",
        company="Hafisoft Technologies",
        start_date="2019-12-01",
        end_date="2020-12-01",
        tech_stack="Python, Odoo, CodeIgniter, PostgreSQL, MySQL, React/React Native",
    )
    db.add(exp3)
    db.flush()

    exp3_achievements = [
        "Programmed Odoo modules powering school management workflows for 10k+ students across multiple institutions.",
        "Optimized PostgreSQL/MySQL queries within AWS RDS environments, reducing user-facing report generation time by 45%.",
        "Systematized academic workflows (timetables, reports, attendance), reduced admin processing time by 30%.",
    ]

    for text in exp3_achievements:
        db.add(ExperienceAchievement(uuid=uuid4(), experience_id=exp3.id, achievement_text=text))



def seed_projects(db):
    if db.query(Project).first():
        return

    # ContractQ
    p1 = Project(
        uuid=uuid4(),
        project_name="ContractQ (AI-Powered CRM & Job Management Platform)",
        role="Senior Software Engineer",
        tech_stack="NestJS, React, PostgreSQL, MongoDB, Redis, Kafka, Stripe, QuickBooks, AWS S3, SQS, SNS, Elasticsearch",
        description="AI-powered CRM & Job Management Platform for multi-tenant business workflows.",
        project_url=None,
        github_url=None,
        doc_url=None,
    )
    db.add(p1)
    db.flush()

    p1_achievements = [
        "Designed and developed scalable REST APIs supporting multi-tenant CRM workflows for 1k+ businesses and 100k+ customer records, supporting React.js frontends.",
        "Implemented Stripe subscription billing, reducing payment failures by 40% through webhook automation.",
        "Integrated QuickBooks for real-time accounting synchronization, modernizing financial data workflows and reducing reporting errors by 50%.",
    ]

    for text in p1_achievements:
        db.add(ProjectAchievement(uuid=uuid4(), project_id=p1.id, achievement_text=text))

    # Our Child's Life
    p2 = Project(
        uuid=uuid4(),
        project_name="Our Child's Life (HIPAA-Compliant Healthcare Platform)",
        role="Senior Software Engineer",
        tech_stack="NestJS, React, React Native, Kafka, Redis, Stripe, AWS S3, PostgreSQL, MongoDB",
        description="HIPAA-compliant healthcare platform for patient onboarding and secure document workflows.",
        project_url=None,
        github_url=None,
        doc_url=None,
    )
    db.add(p2)
    db.flush()

    p2_achievements = [
        "Transformed patient onboarding by developing secure REST APIs integrated with NestJS, React.js and React Native, reducing manual data entry for providers and ensuring 100% HIPAA compliance.",
        "Built secure REST APIs with strict access controls, reduced unauthorized PHI access incidents by 60%.",
        "Leveraged Kafka and AWS S3 to automate background document processing, increasing system throughput by 30% and providing real-time status updates to users via React.js hooks.",
    ]

    for text in p2_achievements:
        db.add(ProjectAchievement(uuid=uuid4(), project_id=p2.id, achievement_text=text))

    # Lilighthouse
    p3 = Project(
        uuid=uuid4(),
        project_name="Lilighthouse (Video Social Marketplace Platform)",
        role="Software Engineer",
        tech_stack="Laravel, Node.js, FFmpeg, Wowza, Avalara, Redis, AWS S3, AWS RDS (MySQL), MongoDB, Elasticsearch",
        description="Video social marketplace platform with live streaming and background video processing.",
        project_url=None,
        github_url=None,
        doc_url=None,
    )
    db.add(p3)
    db.flush()

    p3_achievements = [
        "Orchestrated the backend infrastructure for a high-scale video platform using FFmpeg and Wowza, reducing average video transcoding time by 50%.",
        "Constructed high-performance APIs for uploads and live streaming, yielding a 50% improvement in video processing speed.",
        "Spearheaded an event-driven architecture using Kafka and Redis to process 50k+ background jobs daily, maintaining a 99.9% job completion rate and consistent system throughput.",
    ]

    for text in p3_achievements:
        db.add(ProjectAchievement(uuid=uuid4(), project_id=p3.id, achievement_text=text))


def seed_education(db):
    if db.query(Education).first():
        return

    db.add(
        Education(
            uuid=uuid4(),
            degree="Master of Computer Applications (MCA)",
            university="Bangalore University",
            start_year="2017",
            end_year="2019",
        )
    )


def seed_certifications(db):
    if db.query(Certification).first():
        return

    db.add(
        Certification(
            uuid=uuid4(),
            name="Scientific Computing with Python",
            issuer="freeCodeCamp",
            year="2020",
        )
    )


def seed_analytics(db):
    if db.query(Analytics).first():
        return

    db.add(
        Analytics(
            uuid=uuid4(),
            visitors_count=0,
            resume_download_count=0,
        )
    )


def run_seed():
    db = SessionLocal()
    try:
        seed_profile(db)
        seed_skills(db)
        seed_experience(db)
        seed_projects(db)
        seed_education(db)
        seed_certifications(db)
        seed_analytics(db)

        db.commit()
        print("✅ Seeder completed successfully.")
    except Exception as e:
        db.rollback()
        print("❌ Seeder failed:", e)
        raise
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
