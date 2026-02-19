from src.graph.state import GraphState
from src.providers.base import ChatModelProvider

def specialist_node(state: GraphState, provider: ChatModelProvider) -> dict[str, object]:
                                                                                              
                                                                                                                
    generated_output = provider.generate(state["prompt"])

                                                                                                   
                                                                                                        
    return {
        "messages": ["Specialist generated a final response."],
        "final_output": generated_output,
        "next_node": "END",
    }
