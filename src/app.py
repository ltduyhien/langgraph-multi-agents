"""Application entrypoint for the LangGraph multi-agent service."""

# `FastAPI` is the web framework that will expose the runtime HTTP API.
# The server process will import the `app` object from this file when it starts.
from fastapi import FastAPI

# `get_settings` loads typed runtime configuration from environment variables.
# This lets the application entrypoint expose environment-aware metadata and behavior.
from src.config import get_settings

# `settings` is created once at import time so the application has a shared configuration object.
# This keeps the first version simple and gives later modules a clear startup pattern to follow.
settings = get_settings()

# `app` is the ASGI application object that Uvicorn will run at runtime.
# Its title and version appear in generated docs and help identify the service.
app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str | int]:
    # This lightweight endpoint confirms that the API process started successfully.
    # It is useful before graph routes exist because it verifies config loading and app boot.
    return {
        "status": "ok",
        "app_name": settings.app_name,
        "environment": settings.app_env,
        "port": settings.app_port,
    }
