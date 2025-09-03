# 9. Background Jobs

**Goal:** Implement a reliable system for running background jobs using Celery, with a specified message broker.

**Context:**
*   This task is for applications that need to perform long-running tasks (e.g., sending emails, processing images, calling third-party APIs) without blocking the main request-response cycle.
*   The chosen message broker is `{{redis|rabbitmq}}`.

**Tasks:**

1.  **Integrate Celery:**
    *   Add `Celery` and the appropriate broker client library (`redis` or `pika`) to the dependencies.
    *   Create a Celery application instance and configure it to connect to the message broker. The broker URL should be loaded from the environment.
    *   Integrate Celery with the Flask application so that tasks can access the application context (e.g., database connections, configuration).

2.  **Define and Implement Tasks:**
    *   Create a `tasks.py` file to define your Celery tasks.
    *   Implement at least one example background task (e.g., a task that sends a welcome email).
    *   Ensure tasks have descriptive names for easier monitoring.

3.  **Implement Robust Task Policies:**
    *   **Retry Policies:** Configure automatic retries for tasks that might fail due to transient issues (e.g., network errors). Use exponential backoff for retries.
    *   **Dead Letter Queue (DLQ):** Set up a DLQ to capture tasks that have failed permanently after all retries. This prevents losing important jobs.
    *   **Task Timeouts:** Set sensible timeouts for tasks to prevent them from running indefinitely.

4.  **Set Up Scheduled Tasks (Celery Beat):**
    *   If the application requires scheduled tasks (e.g., nightly cleanup jobs), configure `Celery Beat`.
    *   Define the schedule for the tasks in the Celery configuration.

5.  **Health Checks and Metrics:**
    *   Create a health check endpoint or a CLI command to check the status of the message broker and the Celery workers.
    *   Expose basic metrics, such as the number of tasks in the queue, the number of successful tasks, and the number of failed tasks.

**Deliverables:**
*   A diff showing the new Celery dependency and the related configuration and task files.
*   An updated `docker-compose.yml` that includes services for the Celery worker, Celery Beat (if applicable), and the message broker (`Redis` or `RabbitMQ`).
*   Documentation on how to run and monitor the background jobs.

**Acceptance Criteria:**
*   A background job can be successfully triggered from a Flask endpoint.
*   The job executes asynchronously in a separate Celery worker process.
*   A failing task is automatically retried according to its policy.
*   The full background job system (web app, worker, broker) can be started with a single command (e.g., `docker-compose up`).
*   The retry behavior can be observed in the logs.

**Agent Tips:**
*   When integrating Celery with Flask, you'll need a small factory function to create the Celery instance, similar to the application factory pattern.
*   Make your tasks idempotent if possible. This means that running the same task multiple times with the same arguments will have the same effect as running it once. This is important for safely retrying tasks.
*   Use a structured logging format for your Celery workers to make it easier to trace the execution of a task.
*   Remember that Celery workers run in separate processes and do not share memory with your Flask application. Any data needed by the task must be passed as arguments.
