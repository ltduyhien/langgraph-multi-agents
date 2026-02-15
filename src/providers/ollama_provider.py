from langchain_ollama import ChatOllama
from src.config import Settings
from src.providers.base import ChatModelProvider, ProviderFactory


class OllamaChatModelProvider(ChatModelProvider):
    def __init__(self, client: ChatOllama) -> None:
        self._client = client

    def generate(self, prompt: str) -> str:
        response = self._client.invoke(prompt)
        return str(response.content)


class OllamaProviderFactory(ProviderFactory):
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def create_chat_model_provider(self) -> ChatModelProvider:
        client = ChatOllama(
            model=self._settings.ollama_chat_model,
            base_url=self._settings.ollama_base_url,
        )
        return OllamaChatModelProvider(client=client)
