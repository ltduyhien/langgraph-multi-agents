from fastapi import FastAPI
from src.api.routes import router
from src.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)
app.include_router(router)
