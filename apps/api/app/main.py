from fastapi import FastAPI

from app.core.config import get_settings
from app.core.logging import configure_logging

configure_logging()

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.get("/")
async def root():
    return {
        "message": "Welcome to ShopFlow"
    }