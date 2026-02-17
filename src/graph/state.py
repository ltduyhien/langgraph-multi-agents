from typing import Annotated, TypedDict

                                                                                          
                                                                              
import operator

class GraphState(TypedDict):
                                                                         
                                                                                     
    prompt: str

                                                                          
                                                                                                            
    messages: Annotated[list[str], operator.add]

                                                                               
                                                                                         
    next_node: str

                                                                                                       
                                                                                            
    final_output: str

                                                                                       
                                                                                  
    iteration_count: int
