from types import SimpleNamespace

                                         
                                                                    
from src.schemas import RunResponse
from src.services.run_service import RunService

def test_run_service_builds_graph_and_returns_final_output(monkeypatch) -> None:
                                                                                                  
                                                                                          
    captured_prompts: list[str] = []

    class FakeProvider:
                                                                                            
                                                                                                  
        def generate(self, prompt: str) -> str:
            captured_prompts.append(prompt)
            return f"provider output for: {prompt}"

    class FakeProviderFactory:
                                                                                                                 
                                                                                                     
        def __init__(self, settings) -> None:
            self._settings = settings

        def create_chat_model_provider(self) -> FakeProvider:
            return FakeProvider()

    class FakeGraph:
                                                                                     
                                                                                                 
        def __init__(self, provider: FakeProvider) -> None:
            self._provider = provider

        def invoke(self, initial_state: dict[str, object]) -> dict[str, object]:
            provider_output = self._provider.generate(str(initial_state["prompt"]))
            return {
                **initial_state,
                "messages": [f"specialist completed the run with: {provider_output}"],
                "final_output": "final graph answer",
                "next_node": "END",
                "iteration_count": 1,
            }

                                                                            
                                                                                                           
    monkeypatch.setattr("src.services.run_service.OllamaProviderFactory", FakeProviderFactory)
    monkeypatch.setattr(
        "src.services.run_service.build_graph",
        lambda settings, provider: FakeGraph(provider=provider),
    )

                                                                                           
                                                                                              
    settings = SimpleNamespace(
        model_provider="ollama",
        graph_max_iterations=6,
        ollama_base_url="http://localhost:11434",
        ollama_chat_model="llama3.1",
    )

                                                                                  
                                                                                  
    service = RunService(settings=settings)
    result = service.run(prompt="test prompt")

                                                                                    
                                                                           
    assert result == RunResponse(
        status="completed",
        output="final graph answer",
    )

                                                                                                     
                                                                                             
    assert captured_prompts == ["test prompt"]
