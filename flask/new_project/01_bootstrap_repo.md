# 1. Bootstrap Repo

**Goal:** Create a production-ready skeleton for a new Flask application with a logical structure and essential tooling.

**Inputs:**
*   `PROJECT_NAME`: `{{NAME}}`
*   `PYTHON_VERSION`: `{{X}}`
*   `FLASK_VERSION`: `{{Y}}`
*   `DB_TYPE`: `{{PostgresVer}}`
*   `PACKAGE_MANAGER`: `{{poetry|pip-tools}}`
*   `WSGI_SERVER`: `{{gunicorn}}`
*   `CACHE_BACKEND`: `{{redis|none}}`
*   `BROKER_BACKEND`: `{{redis|rabbitmq|none}}`

**Proposed Directory Tree:**

```
/{{NAME}}/
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── ci.yml
├── .vscode/
│   └── settings.json      # Recommended VSCode settings
├── infra/
│   └── docker/
│       ├── Dockerfile
│       └── docker-compose.yml
├── scripts/
│   └── seed.py            # Script for seeding initial data
├── src/
│   └── app/
│       ├── __init__.py      # App factory (create_app)
│       ├── api/
│       │   └── v1/
│       │       └── blueprints/
│       │           ├── __init__.py
│       │           ├── health.py    # Health check blueprint
│       │           └── example.py   # Example resource blueprint
│       ├── core/
│       │   ├── config.py
│       │   └── logging.py
│       ├── db/
│       │   ├── models.py
│       │   └── session.py
│       ├── schemas/
│       │   └── .keep
│       ├── services/
│       │   └── .keep
│       ├── repositories/
│       │   └── .keep
│       └── libs/
│           └── .keep
├── tests/
│   ├── __init__.py
│   └── test_health.py     # Test for the health check endpoint
├── .dockerignore
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── Makefile
├── pyproject.toml
└── README.md
```

**Tasks:**

1.  **Generate Project Structure:**
    *   Create the complete directory tree as specified above.
    *   Populate the `.keep` files in empty directories to ensure they are tracked by git.

2.  **Implement Basic Endpoints:**
    *   **Health Check:** Create a `/health` endpoint in `src/app/api/v1/blueprints/health.py`. It should return a 200 OK with the JSON body `{"status": "ok"}`.
    *   **Version:** Create a `/__version__` endpoint that returns the application version from the `pyproject.toml` file.

3.  **Set Up `pyproject.toml`:**
    *   Initialize the project using the specified package manager (`poetry` or `pip-tools` conventions).
    *   Add sections for `ruff`, `black`, `mypy`, `pytest`, `coverage`, and `bandit` with sensible default configurations.
    *   Define the project `name`, `version`, and `authors`.

4.  **Configure `pre-commit`:**
    *   Create a `.pre-commit-config.yaml` file.
    *   Add hooks for `ruff`, `black`, `mypy`, and other useful checks (e.g., `check-yaml`, `check-toml`).

**Deliverables:**
*   A new git repository containing the complete project skeleton as described.

**Acceptance Criteria:**
*   The project can be set up and all initial checks pass. This means:
    *   `make setup` (or equivalent) installs all dependencies.
    *   `make test` runs the initial test for the `/health` endpoint and passes.
    *   `make lint` and `make typecheck` run without errors.
    *   `pre-commit install` and `pre-commit run --all-files` complete successfully.
*   A GET request to the `/health` endpoint returns a 200 OK response with the correct JSON body.

**Agent Tips:**
*   This is a bootstrapping task. The focus is on creating a solid foundation. Don't add any complex business logic.
*   The `.keep` files are a convention to make sure empty directories are included in the initial commit.
*   The `pyproject.toml` is the heart of a modern Python project. Take time to set it up correctly.
*   The `Makefile` should provide a simple and consistent interface for all common development tasks.
