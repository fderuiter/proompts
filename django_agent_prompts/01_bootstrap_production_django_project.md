# Agent Prompt: Bootstrap a Production-Grade Django Project

## 1. Objective

To create a new, production-ready Django project from scratch, incorporating best practices for long-term maintainability, scalability, and security. The entire process should be automated and result in a runnable application with a single command.

## 2. User-Provided Parameters

Before starting, obtain the following parameters from the user:

-   **Project Name:** `{{project_name}}` (e.g., `acme_corp`)
-   **Python Version:** `{{3.11 | 3.12}}`
-   **Package Manager:** `{{poetry | pip-tools}}`
-   **Database:** `{{Postgres version}}` (e.g., `15.3`)
-   **Cache/Broker:** `{{Redis version}}` (e.g., `7.0`)
-   **Containerization:** `{{Docker yes/no}}` (Assume 'yes' for this guide)
-   **Hosting Target:** `{{AWS/GCP/Azure/Heroku/Other}}` (For initial setup, this informs general patterns but isn't critical for local dev)

## 3. Agent Execution Plan

### Phase 1: Initial Scaffolding and Environment Setup

1.  **Create Project Directory Structure:**
    ```bash
    mkdir -p src/{{project_name}} apps config scripts infra docs
    touch src/manage.py
    ```
    *Justification: Placing `manage.py` at `src/` keeps the root directory clean and separates application code from repository metadata files (like `README.md`, `pyproject.toml`).*

2.  **Initialize Package Manager:**
    -   **If `poetry`:** Run `poetry init` and interactively set up `pyproject.toml`.
    -   **If `pip-tools`:** Create `requirements/base.in`, `dev.in`, `prod.in`.

3.  **Create Initial Git and Pre-Commit Setup:**
    -   Run `git init`.
    -   Create a `.gitignore` file (e.g., from gitignore.io for Python, Django, Docker).
    -   Create `.pre-commit-config.yaml`. Add initial hooks for `black`, `isort`, `ruff`.

### Phase 2: Core Dependencies and Tooling

1.  **Install Core Dependencies:**
    -   **Base:** `django`, `psycopg2-binary` (or `psycopg`), `redis`, `celery`, `django-environ` (or `pydantic-settings`), `gunicorn`.
    -   **API:** `djangorestframework`, `drf-spectacular`.
    -   **Prod:** `whitenoise[brotli]`.
    -   **Dev/Test:** `pytest`, `pytest-django`, `pytest-cov`, `factory-boy`, `freezegun`, `faker`, `black`, `isort`, `ruff`, `mypy`, `bandit`, `safety` (or `pip-audit`), `pre-commit`.

2.  **Configure `pyproject.toml`:**
    -   Add configuration sections for `[tool.black]`, `[tool.isort]`, `[tool.ruff]`, and `[tool.mypy]`.
    -   For `mypy`, start with `strict = true` and a basic configuration.
    -   For `coverage`, set fail-under threshold: `fail_under = 90`.

3.  **Pin Dependencies:**
    -   **If `poetry`:** Run `poetry lock` to create `poetry.lock`.
    -   **If `pip-tools`:** Run `pip-compile requirements/base.in > requirements/base.txt` (and for dev/prod).

### Phase 3: Django Project Configuration

1.  **Scaffold Django Project & Apps:**
    -   `django-admin startproject config src/{{project_name}}`
    -   `python src/manage.py startapp users apps/users`
    -   `python src/manage.py startapp common apps/common`
    -   `python src/manage.py startapp api apps/api`
    -   `python src/manage.py startapp health apps/health`

2.  **Refactor Settings:**
    -   Move `src/{{project_name}}/settings.py` to `config/settings/base.py`.
    -   Create `dev.py`, `test.py`, `prod.py` in `config/settings/`, inheriting from `base.py`.
    -   Use `django-environ` to manage all environment-specific variables (e.g., `SECRET_KEY`, `DATABASE_URL`, `REDIS_URL`).
    -   Set `DJANGO_SETTINGS_MODULE` in `src/manage.py` and `src/{{project_name}}/wsgi.py`.

3.  **Implement Security Defaults (in `prod.py`):**
    -   `SECURE_HSTS_SECONDS`, `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`.
    -   Set up a basic Content Security Policy (CSP).

4.  **Configure Core Apps and URLs:**
    -   Add `users`, `common`, `api`, `health`, `rest_framework`, `drf_spectacular` to `INSTALLED_APPS` in `base.py`.
    -   Create a main `config/urls.py` that includes routers from `apps/api/urls.py`.
    -   In `apps/api/`, create a `v1` router. Add the health check endpoint: `/api/v1/health/`.

5.  **Set up Logging and Observability:**
    -   Configure `structlog` or Python's `logging.DictConfigurator` for JSON-formatted logs in production.
    -   Add placeholder hooks for Sentry in `prod.py`.

### Phase 4: Containerization

1.  **Create `.env.example` and `.env.test`:**
    -   List all required environment variables with placeholder values.
    -   `.env.test` should configure an isolated test database.

2.  **Create `Dockerfile`:**
    -   Use a multi-stage build.
    -   Stage 1: Build/install dependencies.
    -   Stage 2: Final slim image with `whitenoise` and production settings.

3.  **Create `docker-compose.yml`:**
    -   Define services: `web`, `db`, `redis`, `worker`, `beat`.
    -   `web`: Builds from `Dockerfile`, mounts source code in dev, runs `gunicorn` in prod.
    -   `db`: Uses official `postgres:{{Postgres version}}` image, mounts a volume for data persistence.
    -   `redis`: Uses official `redis:{{Redis version}}` image.
    -   `worker`/`beat`: Use the same web image but with `celery` commands.

### Phase 5: CI and Documentation

1.  **Create GitHub Actions Workflow (`.github/workflows/ci.yml`):**
    -   Define jobs for: linting, type-checking, testing.
    -   Use a matrix strategy to test against Python `3.11` and `3.12`.
    -   Cache dependencies to speed up runs.
    -   (Optional) Add a job to build and push the Docker image on merges to `main`.

2.  **Create Documentation:**
    -   `README.md`: Project overview, local setup instructions.
    -   `Makefile`: Create targets `setup`, `run` (or `up`), `down`, `test`, `fmt`, `lint`, `type`, `migrate`.
    -   `ARCHITECTURE.md`: Briefly describe the project structure and key decisions.
    -   `docs/adr/`: Create a directory for Architecture Decision Records.

## 4. Final Verification Criteria

To confirm success, the agent must perform the following checks:

1.  **Local Environment:**
    -   Execute `make setup` (to install dependencies and set up `.env`).
    -   Execute `make up` (or `docker-compose up`).
    -   Verify the application is running by accessing the health check endpoint (`http://localhost:8000/api/v1/health/`). It must return a `200 OK` status.

2.  **Testing Suite:**
    -   Execute `make test`.
    -   The test suite must pass completely.
    -   Parse the coverage report to ensure test coverage is `≥90%`.

3.  **Production Readiness:**
    -   Execute `python src/manage.py check --settings=config.settings.prod --deploy`.
    -   The command must execute without any errors or warnings (placeholders for secrets like `SECRET_KEY` are acceptable).
