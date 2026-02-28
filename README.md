- `langgraph-multi-agents`

- Small FastAPI service that runs a LangGraph workflow behind an API.

- Runtime flow:
  - client calls `/runs`
  - `src/api/routes.py` validates the request
  - `src/services/run_service.py` creates the provider and graph
  - `src/graph/builder.py` runs the supervisor and specialist nodes
  - `src/providers/ollama_provider.py` calls Ollama
  - the graph returns the final response through the API

- Main runtime files:
  - `src/app.py`
  - `src/api/routes.py`
  - `src/services/run_service.py`
  - `src/config.py`
  - `src/graph/builder.py`
  - `src/graph/state.py`
  - `src/graph/nodes/supervisor.py`
  - `src/graph/nodes/specialist.py`
  - `src/providers/base.py`
  - `src/providers/ollama_provider.py`

- External dependency:
  - Ollama is a separate runtime service
  - this repo does not start Ollama for you
  - the app calls the Ollama server configured in `.env`

- Local setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
cp .env.example .env
```

- Prepare Ollama:

```bash
ollama pull llama3.1
```

- Run the API server:

```bash
.venv/bin/uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

- Run focused tests:

```bash
.venv/bin/python -m pytest tests/test_health.py tests/test_run_flow.py tests/test_run_service.py
```

- Manual checks:

```bash
curl http://127.0.0.1:8000/health
```

```bash
curl -X POST http://127.0.0.1:8000/runs \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Say hello from LangGraph"}'
```

- What verification proves:
  - app startup works
  - router wiring works
  - `/health` returns the expected shape
  - `/runs` delegates into `RunService`
  - `RunService` builds the graph and returns a typed result

- How to read failures:
  - if tests fail before the server runs, look at app wiring, route wiring, or service orchestration
  - if `/health` fails, look at startup or config loading
  - if `/health` works but `/runs` fails before generation, look at the route, service, or graph path
  - if `/runs` fails during generation, look at Ollama availability, model setup, or provider integration

- Current status:
  - app, route, service, provider, graph, and test layers are implemented
  - focused tests pass locally in `.venv`
  - `main` keeps the commented development version
  - `prod` keeps the synced stripped-comment version

- Likely next work:
  - provider and `/runs` error handling
  - Docker-based startup
  - more graph branches or more specialist nodes
