# Agent Prompt: Create a Containerized Development Environment

## 1. Objective

To create a consistent, isolated, and easy-to-use local development environment using Docker and Docker Compose, which can be started with a single command.

## 2. User-Provided Parameters

-   **Services Required:** `{{web, db, redis, worker, beat}}` (Comma-separated list)
-   **Database Image:** `{{postgres:15}}`
-   **Redis Image:** `{{redis:7-alpine}}`

## 3. Agent Execution Plan

### Phase 1: Dockerfile

1.  **Create a `Dockerfile`:**
    -   Create a file named `Dockerfile` in the repository root.
    -   Implement a multi-stage build to keep the final image slim and secure.

2.  **Define a `builder` Stage:**
    -   Start from a full Python image (e.g., `python:3.11`).
    -   Set `WORKDIR /app`.
    -   Install build-time system dependencies (e.g., `build-essential`, `libpq-dev`).
    -   Create a Python virtual environment (e.g., `python -m venv /opt/venv`).
    -   Copy `requirements.txt` or `pyproject.toml`/`poetry.lock`.
    -   Install Python dependencies into the virtual environment.

3.  **Define the Final Stage:**
    -   Start from a slim Python image (e.g., `python:3.11-slim`).
    -   Set `WORKDIR /app`.
    -   Install only required runtime system dependencies (e.g., `libpq5`).
    -   Copy the virtual environment from the `builder` stage (`COPY --from=builder /opt/venv /opt/venv`).
    -   Set the `PATH` to include the venv (`ENV PATH="/opt/venv/bin:$PATH"`).
    -   Copy the application source code (`COPY src/ .`).
    -   Create a non-root user and switch to it (`USER django-user`).
    -   Expose the application port (e.g., `EXPOSE 8000`).
    -   Set the default `CMD` to run the development server.

### Phase 2: Docker Compose

1.  **Create `docker-compose.yml`:**
    -   Create a file named `docker-compose.yml` in the root.
    -   Define the version (e.g., `version: '3.8'`).

2.  **Define the `web` Service:**
    -   `build: .` (or specify context and Dockerfile).
    -   `command: python manage.py runserver 0.0.0.0:8000`
    -   `volumes: ./src:/app` (Mount source code for live reloading).
    -   `ports: "8000:8000"`
    -   `env_file: .env`
    -   `depends_on`: List other services like `db` and `redis`.

3.  **Define the `db` Service (if required):**
    -   `image: {{Database Image}}`
    -   `volumes: postgres_data:/var/lib/postgresql/data` (Use a named volume for persistence).
    -   `environment`: Set `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` from `.env` variables.
    -   `ports: "5432:5432"` (Optional, for local debugging).

4.  **Define `redis`, `worker`, `beat` Services (if required):**
    -   **redis:** `image: {{Redis Image}}`, use a named volume for data.
    -   **worker:** `build: .`, `command: celery -A config.celery worker -l info`, `volumes: ./src:/app`, `env_file: .env`, `depends_on: [redis]`.
    -   **beat:** `build: .`, `command: celery -A config.celery beat -l info`, `volumes: ./src:/app`, `env_file: .env`, `depends_on: [redis]`.

5.  **Define Top-Level Named Volumes:**
    -   At the bottom of the file, declare the named volumes used by the services.
        ```yaml
        volumes:
          postgres_data:
          redis_data:
        ```

### Phase 3: Supporting Files

1.  **Create `.dockerignore`:**
    -   Create a `.dockerignore` file to prevent copying unnecessary files into the build context.
    -   Include `.git`, `__pycache__`, `.venv`, `*.pyc`, `.env`, etc. This speeds up the build and improves security.

2.  **Create `.env.example`:**
    -   Create or update `.env.example` with all variables needed by `docker-compose.yml` and the application, including database credentials.

3.  **Create `Makefile` Targets:**
    -   Add commands to the `Makefile` for managing the Docker Compose environment.
        ```makefile
        up:
		docker-compose up -d --build

        down:
		docker-compose down

        logs:
		docker-compose logs -f

        shell:
		docker-compose exec web bash

        migrate:
		docker-compose exec web python manage.py migrate

        makemigrations:
		docker-compose exec web python manage.py makemigrations
        ```

## 4. Final Verification Criteria

1.  **Environment Starts Successfully:**
    -   Run `cp .env.example .env` to set up the environment.
    -   Run `make up` (or `docker-compose up -d --build`).
    -   All containers must start without exiting or reporting errors. Check with `docker-compose ps`.

2.  **Web Service is Healthy:**
    -   Access the application's health check endpoint (e.g., `http://localhost:8000/health`).
    -   It must return a `200 OK` status.

3.  **Makefile Targets Function Correctly:**
    -   Run `make logs`. It should show the logs from all running services.
    -   Run `make shell`. It should open a bash shell inside the `web` container.
    -   Run `make migrate`. It should execute Django migrations successfully.
    -   Run `make down`. It should stop and remove all related containers.

4.  **Data Persistence:**
    -   Run `make up`. Create some data in the application (e.g., a new user).
    -   Run `make down` and then `make up` again.
    -   Verify that the data created in the first step still exists. This confirms the named volumes are working correctly.
