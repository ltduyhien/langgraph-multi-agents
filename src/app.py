from fastapi import FastAPI
from src.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str | int]:
    return {
        "status": "ok",
        "app_name": settings.app_name,
        "environment": settings.app_env,
        "port": settings.app_port,
    }
