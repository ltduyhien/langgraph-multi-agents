"""Provider contracts for model-backed agent interactions."""

# `ABC` and `abstractmethod` let us define a formal interface for provider implementations.
# This keeps the graph layer dependent on a stable contract instead of one concrete backend.
from abc import ABC, abstractmethod


class ChatModelProvider(ABC):
    # This abstract base class defines the minimum behavior a chat model provider must support.
    # Runtime graph nodes will call this interface, and concrete providers such as Ollama will implement it.

    @abstractmethod
    def generate(self, prompt: str) -> str:
        # `prompt` is the input text the provider should send to the underlying model.
        # Returning plain text keeps the first phase simple before we introduce richer message objects.
        raise NotImplementedError


class ProviderFactory(ABC):
    # This abstract base class defines how the application creates provider instances.
    # A factory gives the runtime one place to decide which backend implementation to construct.

    @abstractmethod
    def create_chat_model_provider(self) -> ChatModelProvider:
        # The returned object must satisfy the `ChatModelProvider` contract above.
        # This method separates provider creation from provider usage, which helps future testing.
        raise NotImplementedError
