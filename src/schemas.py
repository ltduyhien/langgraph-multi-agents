from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
                                                                                             
                                                                                       
    status: str = Field(..., description="Simple health indicator for the running service.")

                                                                         
                                                                  
    app_name: str = Field(..., description="Configured application name.")

                                                                                  
                                                                                
    environment: str = Field(..., description="Active runtime environment name.")

                                              
                                                                                   
    port: int = Field(..., description="Configured HTTP port for the service.")

class RunRequest(BaseModel):
                                                                                   
                                                                                        
    prompt: str = Field(..., min_length=1, description="Input text for the agent workflow.")

class RunResponse(BaseModel):
                                                                   
                                                                                                
    status: str = Field(..., description="High-level status of the graph run.")

                                                                            
                                                                                   
    output: str = Field(..., description="Final text output produced by the service.")
