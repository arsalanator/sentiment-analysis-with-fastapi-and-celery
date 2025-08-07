from fastapi import APIRouter, UploadFile, File
from starlette.responses import JSONResponse
import shutil
import os
from core.infrastructure.adapters.input.celery_worker.worker import process_csv

router = APIRouter()


@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    task = process_csv.delay(path)
    return JSONResponse(content={"task_id": task.id})
