"""Runtime configuration for the LangGraph multi-agent service."""

# `Literal` constrains string values to known provider names.
# This helps prevent unsupported provider values from silently slipping through.
from typing import Literal

# `BaseSettings` reads values from environment variables into typed Python fields.
# This gives the runtime one central place to load configuration when the process starts.
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # `model_config` tells Pydantic how this settings class should load environment values.
    # We point it at `.env` so local runtime config can be loaded automatically later.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # `app_name` gives the service a readable identity in logs and responses.
    # This should match the environment template unless the deployer overrides it.
    app_name: str = "langgraph-multi-agents"

    # `app_env` describes which environment the process is running in.
    # Keeping it explicit helps future code branch safely for local vs production behavior.
    app_env: str = "development"

    # `app_host` is the network interface the API server will bind to at runtime.
    # We default to `0.0.0.0` so container-based local development works cleanly.
    app_host: str = "0.0.0.0"

    # `app_port` is the TCP port the API server will listen on.
    # The future FastAPI entrypoint will use this when starting Uvicorn.
    app_port: int = 8000

    # `log_level` controls how verbose runtime logging should be.
    # This stays as a string because logging libraries commonly accept string level names.
    log_level: str = "INFO"

    # `model_provider` selects which provider adapter the runtime should construct.
    # `Literal` keeps the accepted values intentionally narrow during phase 1.
    model_provider: Literal["ollama"] = "ollama"

    # `ollama_base_url` tells the provider layer where the external Ollama server runs.
    # This is a runtime integration detail, not a build-time dependency.
    ollama_base_url: str = "http://localhost:11434"

    # `ollama_chat_model` selects the default model name sent to Ollama.
    # This remains configurable because different local machines may have different models installed.
    ollama_chat_model: str = "llama3.1"

    # `graph_max_iterations` places a safety cap on supervisor loops.
    # This protects the early graph from getting stuck in accidental routing cycles.
    graph_max_iterations: int = 6

    # `enable_checkpointer` reserves an on/off switch for future graph persistence.
    # We default to `False` because the first runtime path should stay simple and easy to trace.
    enable_checkpointer: bool = False

    # `checkpointer_url` is optional because phase 1 does not require a persistence backend.
    # Later phases can validate and use this only when checkpointing is enabled.
    checkpointer_url: str | None = None


def get_settings() -> Settings:
    # This helper creates a fresh `Settings` object from the current environment.
    # Centralizing construction here gives the rest of the app one clear way to load config.
    return Settings()
