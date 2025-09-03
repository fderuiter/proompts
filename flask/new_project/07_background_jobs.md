# 7. Background Jobs

**Goal:** Prepare the application for asynchronous workloads by setting up Celery and a message broker.

**Context:**
*   Even if there are no immediate needs for background jobs, setting up the infrastructure from the start makes it much easier to add them later.
*   The chosen message broker is `{{redis|rabbitmq}}`.

**Tasks:**

1.  **Integrate Celery:**
    *   Add `Celery` and the broker client (`redis` or `pika`) to the dependencies.
    *   In `src/app/core/celery.py`, create a Celery application instance.
    *   Write a helper function to integrate Celery with the Flask application context, so tasks can access things like the database session and configuration.

2.  **Create an Example Task:**
    *   In a new file, `src/app/tasks/example.py`, create a simple example task.
    *   For instance, a task that takes a string as an argument and logs it.
    *   This task will serve as a template and a way to verify the setup.

3.  **Configure Celery:**
    *   Configure the Celery instance with the broker URL, result backend, and other settings. These should be loaded from the application's main configuration object.
    *   Set default policies for tasks, such as automatic retries with exponential backoff and reasonable timeouts.

4.  **Create a Health Endpoint:**
    *   Create a new API endpoint, e.g., `/api/v1/health/jobs`, that can be used to check the health of the background job system.
    *   This endpoint could trigger a simple task and then poll for its result, confirming that the workers and broker are functioning correctly.

5.  **Update Docker Compose:**
    *   Add services for the Celery worker (`worker`) and the message broker (`broker`) to the `docker-compose.yml` file.
    *   If you need scheduled tasks, also add a service for `celery-beat`.

**Deliverables:**
*   The Celery integration code (`src/app/core/celery.py`).
*   The example task file (`src/app/tasks/example.py`).
*   The health check endpoint for the job system.
*   An updated `docker-compose.yml` with the new services.

**Acceptance Criteria:**
*   The full application stack, including the web server, Celery worker, and broker, starts successfully with `docker-compose up`.
*   The example task can be triggered (e.g., from the health check endpoint or a shell) and executes successfully in the worker.
*   The logs from the worker show the task being received and executed.
*   The job system health check endpoint returns a successful response.

**Agent Tips:**
*   The integration between Celery and Flask is a common pattern. You can find many examples online. The key is to ensure that tasks created by Celery have access to the Flask application context.
*   Make your tasks idempotent whenever possible. This means that running a task multiple times with the same arguments has the same effect as running it once, which is crucial for safe retries.
*   Use a unique name for each task. This makes them easier to identify in monitoring tools.
*   For the health check, be careful about how you check for the result. A simple "fire-and-forget" check might be sufficient to start, just to confirm the worker picks up the job.
