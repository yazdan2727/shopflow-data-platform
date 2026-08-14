from fastapi import FastAPI

from app.core.config import get_settings
from app.core.logging import configure_logging
from app.core.middleware import RequestMiddleware
from app.users.router import router as user_router
from app.auth.router import router as auth_router
from app.products.router import router as product_router

configure_logging()

settings = get_settings()


def create_app() -> FastAPI:

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
    )

    app.add_middleware(RequestMiddleware)

    app.include_router(user_router)
    app.include_router(auth_router)
    app.include_router(product_router)

    @app.get("/")
    async def root():
        return {
            "message": "Welcome to ShopFlow API"
        }

    @app.get("/health")
    async def health():
        return {
            "status": "healthy"
        }

    @app.get("/ready")
    async def ready():
        return {
            "status": "ready"
        }

    return app


app = create_app()
app.add_middleware(RequestMiddleware)