from src.config import Settings
from src.graph.state import GraphState

def supervisor_node(state: GraphState, settings: Settings) -> dict[str, object]:
                                                                                        
                                                                                    
    next_iteration_count = state["iteration_count"] + 1

                                                                                               
                                                                                                
    if state["final_output"]:
        return {
            "iteration_count": next_iteration_count,
            "next_node": "END",
        }

                                                                                            
                                                                                           
    if next_iteration_count >= settings.graph_max_iterations:
        return {
            "iteration_count": next_iteration_count,
            "messages": [
                "Supervisor stopped the run because the graph reached the maximum iteration limit."
            ],
            "final_output": "The graph stopped before producing a final answer.",
            "next_node": "END",
        }

                                                                                        
                                                                                                  
    return {
        "iteration_count": next_iteration_count,
        "messages": ["Supervisor routed the request to the specialist node."],
        "next_node": "specialist",
    }
