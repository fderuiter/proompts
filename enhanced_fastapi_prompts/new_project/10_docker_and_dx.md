# 10. One-Command Developer Experience with Docker

**Objective:**
Create a complete, containerized local development environment managed by `docker-compose` and a `Makefile`, allowing any developer to set up and run the entire application stack with a single command.

**Context:**
- **Dockerfile Path:** `/Dockerfile`
- **Docker Compose File:** `/docker-compose.yml`
- **Helper Script:** `/Makefile`

**Agent Instructions:**
-   The `Dockerfile` must be optimized for build speed and small image size using multi-stage builds.
-   The `docker-compose.yml` should define the full stack, including the API, database, cache, and any other services.
-   The `Makefile` should provide simple, memorable commands for all common development tasks.

**Tasks:**

1.  **Create a Multi-Stage `Dockerfile`:**
    -   Define a `builder` stage that uses a full Python image to install dependencies via `poetry` or `pip`.
    -   Define a final, slim stage (`python:3.X-slim`) that copies the installed virtual environment and the application source code from the `builder` stage.
    -   Create a non-root user and group to run the application securely.
    -   The default command (`CMD`) should run the application via `uvicorn` with live reloading enabled.

2.  **Create a Comprehensive `.dockerignore`:**
    -   Exclude files that shouldn't be in the build context, such as `.git`, `.venv`, `__pycache__`, `.pytest_cache`, `*.pyc`, and environment files like `.env`.

3.  **Build the `docker-compose.yml`:**
    -   Create services for:
        -   `api`: Builds from the `Dockerfile`. Mounts the local `src` directory into the container for live reloading. Reads environment variables from an `.env` file.
        -   `db`: Uses the official `postgres:15` image. Sets up a volume for data persistence.
        -   `cache`: Uses the official `redis:7` image.
        -   `broker`: Uses `redis:7` or `rabbitmq:3` if needed for background tasks.
        -   (Optional) `mailhog`: A mail-catching server for testing email sending.
    -   Define a shared network for all services.
    -   Use `healthcheck`s to ensure services like `db` are ready before the `api` starts.

4.  **Create a `Makefile` for Simplicity:**
    -   Create a `Makefile` in the root of the project.
    -   Implement the following essential targets:
        -   `setup`: Builds the docker images.
        -   `up`: Runs `docker-compose up -d`.
        -   `down`: Runs `docker-compose down --remove-orphans`.
        -   `logs`: Runs `docker-compose logs -f api`.
        -   `test`: Executes `pytest` inside the `api` container.
        -   `lint`: Executes `ruff` and `black` inside the `api` container.
        -   `fmt`: Runs formatters (`ruff --fix`, `black`) inside the container.
        -   `typecheck`: Executes `mypy` inside the `api` container.
        -   `shell`: Opens a bash shell inside the `api` container.

5.  **Update Documentation:**
    -   In the `README.md`, update the "Quickstart" section to be:
        1.  `git clone ...`
        2.  `cp .env.example .env`
        3.  `make up`
    -   Add a section explaining the available `make` commands.

**Deliverables:**
-   A multi-stage `Dockerfile`.
-   A `.dockerignore` file.
-   A `docker-compose.yml` defining the full stack.
-   A `Makefile` with targets for all common dev tasks.
-   An updated `README.md` with the new, simplified setup instructions.

**Acceptance Criteria:**
-   From a fresh clone, a developer can run `make up` and have the entire stack running locally.
-   Changes made to the local source code are immediately reflected in the running `api` container (live reload).
-   `make test`, `make lint`, `make fmt`, and `make typecheck` all execute correctly within the isolated Docker environment.
-   `make shell` successfully opens an interactive shell in the `api` container.
-   The final production-ready Docker image is optimized and does not contain unnecessary build-time dependencies.
