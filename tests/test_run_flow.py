from fastapi.testclient import TestClient

                                                  
                                                                                            
from src.app import app

                                                                                                     
                                                                                
from src.schemas import RunResponse
from src.services.run_service import RunService

def test_run_endpoint_uses_service_result(monkeypatch) -> None:
                                                                              
                                                                                             
    def fake_run(self, prompt: str) -> RunResponse:
        return RunResponse(
            status="completed",
            output=f"stubbed result for: {prompt}",
        )

                                                                                                      
                                                                                                 
    monkeypatch.setattr(RunService, "run", fake_run)

                                                                      
                                                                               
    with TestClient(app) as client:
        response = client.post("/runs", json={"prompt": "hello graph"})

                                                                                        
                                                                                                 
    assert response.status_code == 200
    assert response.json() == {
        "status": "completed",
        "output": "stubbed result for: hello graph",
    }
