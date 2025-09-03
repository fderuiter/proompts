# 12. Docker & Local Developer Experience (DX)

**Objective:**
Create a seamless and reproducible local development environment using Docker and `docker-compose`. The goal is to allow any developer to get the full application stack running with a single command.

**Context:**
- **Dockerfile Path:** `/Dockerfile`
- **Docker Compose File:** `/docker-compose.yml`
- **Helper Script:** `/Makefile` or `/scripts/run.sh`

**Agent Instructions:**
-   Optimize the `Dockerfile` for smaller image size and faster builds by using multi-stage builds and efficient layer caching.
-   The `docker-compose.yml` should define the entire stack: API, database, cache, and message broker.
-   A `Makefile` is recommended to provide simple, memorable commands for common developer tasks.

**Tasks:**

1.  **Optimize the `Dockerfile`:**
    -   **Multi-Stage Build:** Use a `builder` stage to install dependencies and build any assets, then copy only the necessary artifacts into a slim final `python:3.X-slim` image. This dramatically reduces image size.
    -   **Layer Caching:** Structure `COPY` and `RUN` commands to take advantage of Docker's layer caching. Copy dependency files (`pyproject.toml`, `poetry.lock`) and install them *before* copying the application source code.
    -   **Non-Root User:** Create and run the application as a non-root user for improved security.
    -   **`.dockerignore`:** Create a comprehensive `.dockerignore` file to exclude unnecessary files and directories (`.git`, `.vscode`, `__pycache__`, etc.) from the build context.

2.  **Enhance `docker-compose.yml`:**
    -   Define services for all components:
        -   `api`: The FastAPI application.
        -   `db`: PostgreSQL (or other database), with a volume for data persistence.
        -   `cache`: Redis for caching.
        -   `broker`: Redis or RabbitMQ for background tasks.
    -   Use `.env` file substitution for environment variables to keep secrets out of the compose file.
    -   Configure `healthcheck`s for services like `db` and `cache`.
    -   Set up a shared network for easy service-to-service communication.
    -   Use volumes to mount the local source code into the `api` container for live reloading during development.

3.  **Create a `Makefile` for DX:**
    -   Create a `Makefile` in the project root.
    -   Add targets for common operations:
        -   `setup`: To build Docker images and perform initial setup.
        -   `up`: To start the full stack with `docker-compose up -d`.
        -   `down`: To stop the stack.
        -   `test`: To run the test suite inside the `api` container.
        -   `lint`: To run linters inside the `api` container.
        -   `typecheck`: To run `mypy` inside the `api` container.
        -   `logs`: To tail the logs from all services.
        -   `shell`: To open a shell inside the `api` container for debugging.

**Deliverables:**
-   An optimized, multi-stage `Dockerfile`.
-   A comprehensive `.dockerignore` file.
-   A `docker-compose.yml` file defining the complete application stack.
-   A `Makefile` with common development commands.
-   An updated `README.md` explaining how to use the `Makefile` to get started.

**Acceptance Criteria:**
-   A new developer can clone the repository and run `make up` to start the entire application stack without any manual setup.
-   The `api` service live-reloads when a local source file is changed.
-   `make test`, `make lint`, and `make typecheck` all execute correctly within the Docker environment.
-   The final `api` Docker image is reasonably small (e.g., < 500MB).
-   The application runs as a non-root user inside the container.
