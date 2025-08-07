from fastapi import FastAPI
from core.infrastructure.adapters.input.fastapi_api.routes import upload, status

app = FastAPI()
app.include_router(upload.router, prefix="/api")
app.include_router(status.router, prefix="/api")