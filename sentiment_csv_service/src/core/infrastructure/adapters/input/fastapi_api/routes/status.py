from fastapi import APIRouter
from celery.result import AsyncResult
from core.infrastructure.adapters.input.celery_worker.worker import app as celery_app

router = APIRouter()


@router.get("/status/{task_id}")
async def get_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {"task_id": task_id, "status": result.status, "result": result.result if result.ready() else None}
