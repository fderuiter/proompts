# 12. Docker and Local Developer Experience (DX)

**Goal:** Create a containerized local development environment that is consistent, easy to set up, and closely mirrors the production environment.

**Context:**
*   This task is for projects that have a complex setup process, rely on globally installed dependencies, or lack a consistent development environment.
*   The aim is to achieve "dev-prod parity" as much as possible.

**Tasks:**

1.  **Create a Multi-Stage Dockerfile:**
    *   Write a `Dockerfile` for the Flask application.
    *   Use a multi-stage build. The first stage should be a `builder` stage that installs dependencies. The final stage should copy the application code and dependencies from the builder, resulting in a smaller, cleaner production image.
    *   Run the application as a non-root user for improved security.
    *   Create a comprehensive `.dockerignore` file to prevent unnecessary files (like `.git`, `.pytest_cache`, `__pycache__`) from being copied into the image.

2.  **Orchestrate Services with Docker Compose:**
    *   Create a `docker-compose.yml` file to define and link all the services needed for local development.
    *   This should include:
        *   `web`: The Flask application itself.
        *   `db`: The PostgreSQL or MySQL database.
        *   `cache`: A Redis instance for caching.
        *   `broker`: A Redis or RabbitMQ instance for background jobs.
        *   (Optional) `mailhog`: A fake SMTP server for testing email sending.
    *   Mount the application source code as a volume in the `web` service to enable hot-reloading on code changes.

3.  **Simplify Common Tasks with a Makefile:**
    *   Create a `Makefile` with simple, memorable commands for common development tasks. This serves as a "single entry point" for developers.
    *   Include targets like:
        *   `setup`: To build the Docker images and perform any initial setup.
        *   `up`: To start all services using `docker-compose up`.
        *   `down`: To stop all services.
        *   `test`: To run the test suite inside the container.
        *   `lint`: To run linters inside the container.
        *   `typecheck`: To run `mypy` inside the container.
        *   `fmt`: To format the code.
        *   `shell`: To open a shell inside the `web` container for debugging.

**Deliverables:**
*   A `Dockerfile` for the Flask application.
*   A `.dockerignore` file.
*   A `docker-compose.yml` file for the local development environment.
*   A `Makefile` with a set of common development commands.

**Acceptance Criteria:**
*   A new developer can clone the repository and get the full development stack running with a single command (`make up` or `make setup && make up`).
*   The application runs correctly inside the Docker container.
*   Tests, linting, and other checks can be run via `make` commands.
*   Code changes made on the host machine are immediately reflected in the running container.

**Agent Tips:**
*   When writing the `Dockerfile`, be mindful of layer caching. Order your commands from least frequently changing to most frequently changing (e.g., install dependencies before copying your application code).
*   Use environment variables in your `docker-compose.yml` to make it configurable. You can use a `.env` file to set default values.
*   Make sure your database data is persisted in a Docker volume, so you don't lose your data every time you restart the `db` container.
*   The `Makefile` should be self-documenting. Add comments or a `help` target that explains what each command does.
