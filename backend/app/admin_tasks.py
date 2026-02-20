import os
import uuid
import subprocess
import logging
from typing import Dict
from fastapi import APIRouter, BackgroundTasks, HTTPException

router = APIRouter(prefix="/admin", tags=["admin"])
logger = logging.getLogger("admin_tasks")
logger.setLevel(logging.INFO)

# Simple in-memory job store
_job_store: Dict[str, Dict] = {}

# Optional: set where alembic.ini lives; default is repo root
PROJECT_ROOT = os.getenv("PROJECT_ROOT", ".")
ALEMBIC_CONFIG = os.getenv("ALEMBIC_CONFIG", "alembic.ini")

def _run_commands(job_id: str):
    _job_store[job_id]["status"] = "running"
    try:
        logger.info("[%s] Running alembic upgrade head", job_id)
        subprocess.run(
            ["python", "-m", "alembic", "-c", ALEMBIC_CONFIG, "upgrade", "head"],
            cwd=PROJECT_ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        logger.info("[%s] Alembic completed", job_id)

        logger.info("[%s] Running seeder", job_id)
        subprocess.run(
            ["python", "-m", "app.db.seeder"],
            cwd=PROJECT_ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        logger.info("[%s] Seeder completed", job_id)
        _job_store[job_id]["status"] = "success"
    except subprocess.CalledProcessError as e:
        logger.exception("[%s] Command failed", job_id)
        _job_store[job_id]["status"] = "failed"
        _job_store[job_id]["error"] = e.stdout if hasattr(e, "stdout") else str(e)
    except Exception as e:
        logger.exception("[%s] Unexpected error", job_id)
        _job_store[job_id]["status"] = "failed"
        _job_store[job_id]["error"] = str(e)

@router.get("/run-migrations")
def run_migrations(background_tasks: BackgroundTasks):
    """
    Public GET endpoint that triggers alembic upgrade head and the seeder in background.
    """
    job_id = str(uuid.uuid4())
    _job_store[job_id] = {"status": "queued"}
    background_tasks.add_task(_run_commands, job_id)
    return {"job_id": job_id, "status": "queued"}

@router.get("/run-migrations/status/{job_id}")
def migration_status(job_id: str):
    job = _job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
