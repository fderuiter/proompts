# 9. Background Tasks and Queues

**Objective:**
Integrate a robust background task queue to handle long-running or asynchronous jobs reliably. This involves setting up a task broker, defining a worker, and providing a clear pattern for enqueuing and processing tasks.

**Context:**
- **Chosen Task Queue:** `{{Celery|Arq|Dramatiq|RQ}}`
- **Chosen Broker:** `{{Redis|RabbitMQ}}`
- **Task Definitions Location:** `{{SRC_DIR}}/app/tasks/`
- **Worker Configuration:** `{{SRC_DIR}}/app/worker.py`

**Agent Instructions:**
-   Ensure the chosen task queue is well-integrated with the FastAPI application.
-   Implement best practices for task design, including idempotency, retries, and dead-letter queues.
-   The setup should be containerized for local development and production parity.

**Tasks:**

1.  **Install Dependencies:**
    -   Add the chosen task queue library (e.g., `celery`, `arq`) to the project's dependencies.
    -   Add the broker client library (e.g., `redis`, `pika`).

2.  **Configure the Task Queue:**
    -   Create a configuration file or use the central `settings` object to configure the broker URL, task serialization, and other parameters.
    -   In `{{SRC_DIR}}/app/worker.py`, create and configure the instance of your task queue (e.g., `Celery(..., broker=settings.BROKER_URL)`).

3.  **Create an Example Task:**
    -   In `{{SRC_DIR}}/app/tasks/example.py`, define a simple example task, such as one that logs a message or sends an email.
    -   The task should demonstrate best practices:
        -   **Naming:** Use a consistent naming convention (e.g., `app.tasks.send_email`).
        -   **Retries:** Configure an automatic retry policy with exponential backoff for transient errors.
        -   **Error Handling:** Include `try...except` blocks for graceful failure.

4.  **Integrate with the API:**
    -   In an API endpoint, show how to enqueue the task.
    -   Example: `send_email_task.delay(user_id=123)` or `await redis.enqueue_job('send_email', user_id=123)`.
    -   The endpoint should return an immediate `202 Accepted` response to the client, not wait for the task to complete.

5.  **Set Up Health Checks and Metrics:**
    -   Create a mechanism to check the health of the worker and the broker. This could be a separate health check endpoint or a CLI command.
    -   (Optional) Configure the worker to expose basic metrics, such as the number of tasks processed, failed, and in the queue.

6.  **Containerize the Worker:**
    -   Add a new service to the `docker-compose.yml` file for the worker.
    -   This service should use the same application image as the API but run a different command (e.g., `celery -A app.worker worker -l info`).
    -   Ensure the worker container can connect to the broker (Redis/RabbitMQ) container.

**Deliverables:**
-   Git diff showing new dependencies and code for the worker, tasks, and API integration.
-   The new `{{SRC_DIR}}/app/worker.py` and `{{SRC_DIR}}/app/tasks/example.py` files.
-   An updated `docker-compose.yml` with the new worker service.
-   A `README.md` section explaining how to run the worker and enqueue tasks.

**Acceptance Criteria:**
-   `docker-compose up` successfully starts the API, database, broker, and the new worker service.
-   Calling the relevant API endpoint successfully enqueues the background task.
-   The worker's logs show that it picked up and executed the task successfully.
-   If the task is designed to fail, it retries according to its policy and eventually lands in a dead-letter queue (if configured).
-   The system remains stable and functional under a simple load test.
