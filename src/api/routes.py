from fastapi import APIRouter

                                                                          
                                                                      
from src.schemas import HealthResponse, RunRequest, RunResponse

                                                         
                                                                            
router = APIRouter()

@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
                                                                               
                                                                                                       
    return HealthResponse(
        status="ok",
        app_name="langgraph-multi-agents",
        environment="development",
        port=8000,
    )

@router.post("/runs", response_model=RunResponse)
def run_graph(request: RunRequest) -> RunResponse:
                                                                       
                                                                                                                                 
    return RunResponse(
        status="pending",
        output=f"Graph execution is not wired yet. Received prompt: {request.prompt}",
    )
