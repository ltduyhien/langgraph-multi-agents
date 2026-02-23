from fastapi.testclient import TestClient

                                                                                           
                                                        
from src.app import app

def test_health_endpoint_returns_expected_shape() -> None:
                                                                                   
                                                                                  
    with TestClient(app) as client:
                                                                                                       
        response = client.get("/health")

                                                                          
                                                                                               
    assert response.status_code == 200

                                                                                    
                                                                                                      
    assert response.json() == {
        "status": "ok",
        "app_name": "langgraph-multi-agents",
        "environment": "development",
        "port": 8000,
    }
