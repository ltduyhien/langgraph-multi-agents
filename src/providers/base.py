from abc import ABC, abstractmethod


class ChatModelProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class ProviderFactory(ABC):
    @abstractmethod
    def create_chat_model_provider(self) -> ChatModelProvider:
        raise NotImplementedError
