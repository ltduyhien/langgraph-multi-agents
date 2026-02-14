"""Ollama-backed provider implementations."""

# `ChatOllama` is the LangChain integration that sends chat requests to an Ollama server.
# We use it inside our provider adapter so the rest of the app does not depend on Ollama directly.
from langchain_ollama import ChatOllama

# `Settings` provides the runtime configuration values this provider needs, such as the base URL and model name.
# `ProviderFactory` and `ChatModelProvider` are the contracts that keep the graph layer provider-agnostic.
from src.config import Settings
from src.providers.base import ChatModelProvider, ProviderFactory


class OllamaChatModelProvider(ChatModelProvider):
    # This concrete provider wraps a LangChain `ChatOllama` client.
    # Its purpose is to translate our simple `generate` contract into an Ollama-backed model invocation.

    def __init__(self, client: ChatOllama) -> None:
        # `client` is the configured LangChain model instance that knows how to call the Ollama HTTP server.
        # Injecting it here makes the class easier to test and keeps construction separate from usage.
        self._client = client

    def generate(self, prompt: str) -> str:
        # `invoke` sends the prompt to the model and returns a LangChain message-like result object.
        # For phase 1 we normalize that response down to plain text so the rest of the runtime stays simple.
        response = self._client.invoke(prompt)

        # `content` may be a string or a richer structure depending on the integration.
        # Casting to `str` gives the early prototype a predictable plain-text output contract.
        return str(response.content)


class OllamaProviderFactory(ProviderFactory):
    # This factory builds Ollama-backed provider instances from runtime settings.
    # The application will use the factory so provider creation stays centralized and replaceable.

    def __init__(self, settings: Settings) -> None:
        # `settings` supplies the model name and base URL that the external Ollama server expects.
        # Reading them here keeps provider wiring aligned with the central config loader.
        self._settings = settings

    def create_chat_model_provider(self) -> ChatModelProvider:
        # `ChatOllama` is configured at runtime from our settings object.
        # This is where our application-specific config meets the external Ollama integration.
        client = ChatOllama(
            model=self._settings.ollama_chat_model,
            base_url=self._settings.ollama_base_url,
        )

        # Returning the provider behind the abstract contract keeps the rest of the app decoupled from Ollama.
        return OllamaChatModelProvider(client=client)
