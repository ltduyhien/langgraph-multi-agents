from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "langgraph-multi-agents"

    app_env: str = "development"

    app_host: str = "0.0.0.0"

    app_port: int = 8000

    log_level: str = "INFO"

    model_provider: Literal["ollama"] = "ollama"

    ollama_base_url: str = "http://localhost:11434"

    ollama_chat_model: str = "llama3.1"

    graph_max_iterations: int = 6

    enable_checkpointer: bool = False

    checkpointer_url: str | None = None


def get_settings() -> Settings:
    return Settings()
