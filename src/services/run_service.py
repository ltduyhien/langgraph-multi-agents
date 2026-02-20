from src.config import Settings
from src.graph.builder import build_graph
from src.graph.state import GraphState
from src.providers.ollama_provider import OllamaProviderFactory
from src.schemas import RunResponse

class RunService:
                                                                     
                                                                                               

    def __init__(self, settings: Settings) -> None:
                                                                                             
                                                                                           
        self._settings = settings

    def run(self, prompt: str) -> RunResponse:
                                                                                            
                                                                                                                 
        provider_factory = OllamaProviderFactory(settings=self._settings)
        provider = provider_factory.create_chat_model_provider()

                                                                      
                                                                                                           
        graph = build_graph(settings=self._settings, provider=provider)

                                                                                            
                                                                             
        initial_state: GraphState = {
            "prompt": prompt,
            "messages": [],
            "next_node": "supervisor",
            "final_output": "",
            "iteration_count": 0,
        }

                                                                                               
                                                                                                   
        final_state = graph.invoke(initial_state)

                                                                                                                 
                                                                                              
        return RunResponse(
            status="completed",
            output=final_state["final_output"],
        )
