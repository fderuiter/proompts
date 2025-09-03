# 10. Docker and Developer Experience (DX)

**Goal:** Provide a "one-command" local development setup using Docker, Docker Compose, and a Makefile.

**Context:**
*   A smooth and consistent development environment is crucial for developer productivity and happiness.
*   The goal is to allow a new developer to get the entire application stack running with a single command.

**Tasks:**

1.  **Write a Multi-Stage Dockerfile:**
    *   In `infra/docker/Dockerfile`, create a multi-stage `Dockerfile`.
    *   **Builder Stage:** Start from a full Python image, create a virtual environment, and install all dependencies (`main` and `dev`).
    *   **Final Stage:** Start from a slim Python image. Copy the virtual environment from the builder stage. Run the application as a non-root user.
    *   Create a comprehensive `.dockerignore` file to keep the build context clean and the final image small.

2.  **Orchestrate with Docker Compose:**
    *   In `infra/docker/docker-compose.yml`, define all the services required for local development:
        *   `web`: The Flask application, built from the `Dockerfile`.
        *   `db`: The PostgreSQL database, using an official image.
        *   `cache`: A Redis instance for caching.
        *   `broker`: A Redis or RabbitMQ instance for background jobs.
        *   (Optional) `mailhog`: A fake SMTP server for testing emails.
    *   Mount the `src` directory as a volume into the `web` container to enable hot-reloading.
    *   Use a `.env` file to manage configuration for Docker Compose (e.g., database passwords, exposed ports).

3.  **Create a `Makefile` for Common Tasks:**
    *   Create a `Makefile` in the root directory to act as a friendly command-line interface for the project.
    *   Implement the following targets:
        *   `setup`: Build the Docker images.
        *   `up`: Start all services with `docker-compose up -d`.
        *   `down`: Stop all services.
        *   `logs`: Tail the logs from all services.
        *   `test`: Execute the test suite inside the `web` container.
        *   `lint`: Run the linter inside the `web` container.
        *   `typecheck`: Run `mypy` inside the `web` container.
        *   `fmt`: Format the code using `black` and `ruff`.
        *   `shell`: Open an interactive shell (`/bin/bash`) inside the `web` container.
        *   `db-shell`: Connect to the database shell (`psql`).

**Deliverables:**
*   `infra/docker/Dockerfile`
*   `infra/docker/docker-compose.yml`
*   `.dockerignore`
*   `Makefile`
*   An updated `README.md` explaining how to use the `make` commands.

**Acceptance Criteria:**
*   After a fresh `git clone`, a new developer can run `make setup` and then `make up` to get the entire stack running.
*   Code changes made to the source code on the host machine are immediately reflected in the running `web` container.
*   All `make` commands (`test`, `lint`, `shell`, etc.) work correctly.
*   The setup is documented in the `README.md`.

**Agent Tips:**
*   Pay attention to the order of commands in your `Dockerfile` to optimize for layer caching. For example, copy the dependency files (`pyproject.toml`, `poetry.lock`) and install dependencies *before* you copy your application source code.
*   Use Docker volumes to persist database data between `docker-compose down` and `up`. Otherwise, your database will be wiped clean every time.
*   The `Makefile` should be self-documenting. A common pattern is to add a `help` target that prints out all the available commands and what they do.
*   Make sure the non-root user in your Docker container has the correct permissions to write to any necessary directories.
