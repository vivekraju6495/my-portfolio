import os
import uuid
import subprocess
import logging
from fastapi import APIRouter, BackgroundTasks, Header, HTTPException, status

router = APIRouter(prefix="/admin", tags=["admin"])
logger = logging.getLogger("admin_tasks")

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")  # set this in Render/GitHub/Cloud secrets

def _run_migrations_and_seed():
    try:
        logger.info("Starting alembic upgrade head")
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        logger.info("Alembic migrations completed")

        logger.info("Starting seeder module")
        # Option A: run seeder as module
        subprocess.run(["python", "-m", "app.db.seeder"], check=True)

        # Option B: import and call a function (uncomment if you prefer)
        # from app.db.seeder import run_seed
        # run_seed()

        logger.info("Seeder completed successfully")
    except subprocess.CalledProcessError as e:
                logger.exception("Command failed: %s", e)
    except Exception as e:
                logger.exception("Seeder error: %s", e)

    @router.post("/run-migrations", status_code=202)
    def run_migrations(background_tasks: BackgroundTasks, x_admin_token: str | None = Header(None)):
            """
            Trigger Alembic migrations and seeder in background.
            Provide X-ADMIN-TOKEN header with the secret value.
            """
            if not ADMIN_TOKEN:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="ADMIN_TOKEN not configured")
            if not x_admin_token or x_admin_token != ADMIN_TOKEN:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid admin token")

            job_id = str(uuid.uuid4())
            logger.info("Admin migration job started %s", job_id)
            background_tasks.add_task(_run_migrations_and_seed)
            return {"job_id": job_id, "status": "started"}
