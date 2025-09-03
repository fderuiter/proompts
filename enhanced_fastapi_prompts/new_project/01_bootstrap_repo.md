# 1. Bootstrap Production-Ready Skeleton

**Objective:**
Initialize a new Git repository with a production-ready directory structure and a minimal, working FastAPI application. This skeleton will serve as the foundation for the entire project.

**Context:**
- **Project Name:** `{{PROJECT_NAME}}`
- **Python Version:** `{{PYTHON_VERSION}}` (e.g., 3.11)
- **FastAPI Version:** `{{FASTAPI_VERSION}}` (e.g., 0.109.0)
- **Pydantic Version:** `{{PYDANTIC_VERSION}}` (e.g., 2.5)
- **Package Manager:** `{{poetry|pip-tools}}`
- **ASGI Server:** `{{uvicorn|hypercorn}}`
- **Database Support:** `{{Postgres|none}}`
- **Cache Support:** `{{Redis|none}}`
- **Broker Support:** `{{Redis|RabbitMQ|none}}`

**Agent Instructions:**
-   Generate a clean, logical directory structure from the start.
-   Initialize the project with the chosen dependency manager.
-   The initial application should be minimal but include basic health and version endpoints.
-   Set up `pre-commit` with basic formatters from day one.

**Tasks:**

1.  **Initialize Git Repository:**
    -   Create a new directory named `{{PROJECT_NAME}}`.
    -   Inside, run `git init` and create an initial commit on the `main` branch.

2.  **Set Up Dependency Management:**
    -   **Poetry:** Run `poetry init` to create `pyproject.toml`. Add `fastapi`, `uvicorn`, etc., as dependencies.
    -   **pip-tools:** Create `requirements/main.in` and `requirements/dev.in` and add the base dependencies.

3.  **Create Directory Structure:**
    -   Create the following directory tree:
      ```
      /src/
          /app/
              /api/
                  /v1/
                      /routers/
                          health.py
                          example.py
              /core/
                  config.py
                  logging.py
              /db/
                  models.py
                  session.py
              /repositories/
                  .keep
              /schemas/
                  .keep
              /services/
                  .keep
              main.py
      /tests/
      /scripts/
      /infra/
          /docker/
      .gitignore
      README.md
      ```

4.  **Implement Minimal Application:**
    -   **`main.py`:** Instantiate the FastAPI app. Include the health router.
    -   **`health.py`:** Create an `APIRouter`. Add a `/health` endpoint that returns `{"status": "ok"}`. Add a `/__version__` endpoint that returns the app version from `pyproject.toml` or settings.

5.  **Add Basic Tooling:**
    -   Create a `.gitignore` file from a standard Python template.
    -   Add `ruff` and `black` as dev dependencies.
    -   Create a `pyproject.toml` with basic configurations for these tools.
    -   Set up `.pre-commit-config.yaml` with hooks for `ruff` and `black`.
    -   Run `pre-commit install`.

6.  **Create Initial `README.md`:**
    -   Add a `README.md` with the project title.
    -   Include a "Quickstart" section explaining how to set up the virtual environment and run the app (e.g., `poetry install`, `poetry run uvicorn ...`).

**Deliverables:**
-   A new Git repository with the specified directory structure.
-   A `pyproject.toml` or `requirements/*.in` files with initial dependencies.
-   A minimal, runnable FastAPI application.
-   A `.pre-commit-config.yaml` and a configured `pyproject.toml`.
-   A basic `README.md`.

**Acceptance Criteria:**
-   The application starts successfully when run with `uvicorn`.
-   A `GET` request to `/api/v1/health` returns a `200 OK` with `{"status": "ok"}`.
-   `pytest` runs successfully (even if there are no tests yet).
-   `pre-commit run --all-files` passes without errors.
