from collections.abc import Callable

                                                                                          
                                                                                             
from langgraph.graph import END, START, StateGraph

                                                                
                                                                                                
                                                                       
                                                                              
from src.config import Settings
from src.graph.nodes.specialist import specialist_node
from src.graph.nodes.supervisor import supervisor_node
from src.graph.state import GraphState
from src.providers.base import ChatModelProvider

def route_from_supervisor(state: GraphState) -> str:
                                                                                           
                                                                                             
    return state["next_node"]

def build_graph(
    settings: Settings,
    provider: ChatModelProvider,
) -> Callable[[GraphState], GraphState]:
                                                                          
                                                                                                      
    builder = StateGraph(GraphState)

                                                                             
                                                                                                         
    def supervisor_wrapper(state: GraphState) -> dict[str, object]:
        return supervisor_node(state=state, settings=settings)

                                                                                      
                                                                                            
    def specialist_wrapper(state: GraphState) -> dict[str, object]:
        return specialist_node(state=state, provider=provider)

                                                              
                                                                                             
    builder.add_node("supervisor", supervisor_wrapper)
    builder.add_node("specialist", specialist_wrapper)

                                                     
                                                                                        
    builder.add_edge(START, "supervisor")

                                                                                            
                                                                           
    builder.add_conditional_edges(
        "supervisor",
        route_from_supervisor,
        {
            "specialist": "specialist",
            "END": END,
        },
    )

                                                                   
                                                                                                                    
    builder.add_edge("specialist", "supervisor")

                                                                            
                                                                                               
    return builder.compile()
