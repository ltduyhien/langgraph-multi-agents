from fastapi import APIRouter
from src.config import get_settings
from src.services.run_service import RunService
from src.schemas import HealthResponse, RunRequest, RunResponse

router = APIRouter()
settings = get_settings()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        environment=settings.app_env,
        port=settings.app_port,
    )


@router.post("/runs", response_model=RunResponse)
def run_graph(request: RunRequest) -> RunResponse:
    run_service = RunService(settings=settings)
    return run_service.run(prompt=request.prompt)
