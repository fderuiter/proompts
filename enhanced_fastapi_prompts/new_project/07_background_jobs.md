# 7. Background Jobs

**Objective:**
Integrate a reliable background job queue to process long-running tasks asynchronously, ensuring the API remains responsive and tasks are executed durably.

**Context:**
- **Task Queue:** `{{Celery|Arq|Dramatiq|RQ}}`
- **Broker:** `{{Redis|RabbitMQ}}`
- **Worker Setup:** `src/app/worker.py`
- **Task Definitions:** `src/app/tasks/`

**Agent Instructions:**
-   Set up the chosen task queue and its broker (e.g., Redis).
-   The worker should be containerized and managed via `docker-compose` for local development.
-   Implement a clear pattern for defining tasks and enqueuing them from the API.

**Tasks:**

1.  **Install Dependencies:**
    -   Add the chosen task queue library (e.g., `celery`) to `pyproject.toml`.
    -   Add the broker client library (e.g., `redis`).

2.  **Configure the Task Queue:**
    -   In `src/app/worker.py`, create and configure the task queue instance.
    -   Load broker URL and other settings from the central `settings` object (`src/app/core/config.py`).
    -   Ensure the worker can access the application context if needed (e.g., for database access).

3.  **Define an Example Task:**
    -   Create a new module `src/app/tasks/example_tasks.py`.
    -   Define a simple task, e.g., `send_welcome_email(user_id: int)`.
    -   In the task, simulate work with `time.sleep()` and log messages to show it's being executed.
    -   Configure the task with a retry policy (e.g., retry on `ConnectionError` up to 3 times).

4.  **Integrate Task Enqueuing in the API:**
    -   Create a new API endpoint, for example, in the `users` router after a user is created.
    -   From this endpoint, enqueue the background task: `send_welcome_email.delay(user_id=new_user.id)`.
    -   The API endpoint should return immediately with a `201 Created` or `202 Accepted` response, not waiting for the task to finish.

5.  **Containerize the Worker:**
    -   In your main `docker-compose.yml`, add a new service for the `worker`.
    -   This service will use the same Docker image as your `api` service.
    -   The `command` for the worker service will be different, e.g., `celery -A src.app.worker.celery_app worker -l info`.
    -   Ensure the `worker` service `depends_on` the `broker` (e.g., Redis) service.

6.  **Create a Health Endpoint for the Worker:**
    -   (Optional but recommended) Add a feature to your task queue setup to monitor worker health. For Celery, this can be done with `Flower` or by inspecting the broker.
    -   Create an API endpoint like `/api/v1/health/workers` that reports the status of connected workers.

**Deliverables:**
-   Git diff showing new dependencies and the worker/task files.
-   The `src/app/worker.py` and `src/app/tasks/example_tasks.py` files.
-   An updated `docker-compose.yml` with the new `worker` and `broker` services.
-   An updated `Makefile` with a target to view worker logs (`make logs-worker`).
-   An API endpoint that enqueues the example task.

**Acceptance Criteria:**
-   `make up` (or `docker-compose up`) starts the API, broker, and worker containers successfully.
-   Calling the trigger endpoint returns a `2xx` response instantly.
-   The worker logs show that the task was received and executed.
-   If the task is designed to fail, the logs show it retrying according to its policy.
-   The system remains stable, and the API is responsive while the task runs in the background.
