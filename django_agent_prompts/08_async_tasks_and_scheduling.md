# Agent Prompt: Implement Async Tasks and Scheduling with Celery

## 1. Objective

To set up a robust background task processing system using Celery and a message broker (Redis or RabbitMQ), including task scheduling, idempotency, retries, and structured logging.

## 2. User-Provided Parameters

-   **Message Broker:** `{{Redis | RabbitMQ}}`
-   **Broker URL Environment Variable:** `{{BROKER_URL}}` (e.g., `CELERY_BROKER_URL`)

## 3. Agent Execution Plan

### Phase 1: Celery Setup and Configuration

1.  **Install Dependencies:**
    -   Add `celery` and `redis` (if using Redis) to the project's dependencies.

2.  **Create Celery Instance:**
    -   In the main project configuration directory (e.g., `config/`), create a new file named `celery.py`.
        ```python
        # In config/celery.py
        import os
        from celery import Celery

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
        app = Celery("{{project_name}}")
        app.config_from_object("django.conf:settings", namespace="CELERY")
        app.autodiscover_tasks()
        ```

3.  **Hook Celery into the Django App:**
    -   In `config/__init__.py`, import the celery app to ensure it loads when Django starts.
        ```python
        # In config/__init__.py
        from .celery import app as celery_app

        __all__ = ("celery_app",)
        ```

4.  **Configure Celery in Django Settings:**
    -   In `settings/base.py`, add the Celery configuration.
        ```python
        # CELERY SETTINGS
        CELERY_BROKER_URL = env("{{BROKER_URL}}")
        CELERY_RESULT_BACKEND = env("{{BROKER_URL}}") # Or a different backend
        CELERY_ACCEPT_CONTENT = ["json"]
        CELERY_TASK_SERIALIZER = "json"
        CELERY_RESULT_SERIALIZER = "json"
        CELERY_TIMEZONE = "UTC"
        CELERY_TASK_TRACK_STARTED = True
        ```

### Phase 2: Task Creation and Best Practices

1.  **Create a Sample Task:**
    -   In a relevant app (e.g., `apps/users`), create a `tasks.py` file. Celery's `autodiscover_tasks` will find it.
    -   Define a simple task.
        ```python
        # In apps/users/tasks.py
        from celery import shared_task
        import logging

        logger = logging.getLogger(__name__)

        @shared_task
        def add(x, y):
            logger.info(f"Adding {x} + {y}")
            return x + y
        ```

2.  **Implement an Idempotent Task:**
    -   Create a task that is safe to retry. Use database transactions or check for existing state to prevent duplicate side effects.
        ```python
        @shared_task(bind=True, max_retries=3, default_retry_delay=60)
        def process_payment(self, payment_id):
            try:
                payment = Payment.objects.get(id=payment_id)
                if payment.status == 'PROCESSED':
                    logger.warning(f"Payment {payment_id} already processed.")
                    return
                # ... processing logic ...
                payment.status = 'PROCESSED'
                payment.save()
            except Payment.DoesNotExist:
                logger.error(f"Payment {payment_id} not found.")
            except Exception as exc:
                # Retry on transient errors
                raise self.retry(exc=exc)
        ```

3.  **Set up a Dead-Letter Queue Strategy:**
    -   Configure Celery to route failed tasks (after all retries) to a specific queue for manual inspection. This requires broker-level configuration (e.g., queue arguments in `task_routes`).

### Phase 3: Scheduling Periodic Tasks (Celery Beat)

1.  **Configure Celery Beat Schedule:**
    -   In `settings/base.py`, define a schedule.
        ```python
        from celery.schedules import crontab

        CELERY_BEAT_SCHEDULE = {
            "cleanup-every-midnight": {
                "task": "apps.common.tasks.perform_cleanup",
                "schedule": crontab(minute=0, hour=0), # Runs every midnight
            },
        }
        ```
    -   Create the corresponding task (`perform_cleanup`) in `apps/common/tasks.py`.

### Phase 4: Containerization and Logging

1.  **Update `docker-compose.yml`:**
    -   Add services for a `worker` and a `beat` process.
    -   Both services should use the same application image as the `web` service.
    -   The `command` for each service should be different:
        -   `worker`: `celery -A config.celery worker -l info`
        -   `beat`: `celery -A config.celery beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler` (if using db scheduler) or just `celery -A config.celery beat -l info`

2.  **Implement Structured Logging:**
    -   Ensure your `LOGGING` configuration in Django settings applies to the `celery` logger.
    -   In production, use a `JSONFormatter` so that logs from workers and beat are structured and easily searchable.
    -   Celery tasks should use Python's standard `logging` module.

## 4. Final Verification Criteria

1.  **Task Execution:**
    -   Start the application stack (`docker-compose up`).
    -   Open a shell into the `web` container (`docker-compose exec web bash`).
    -   Open a Django shell (`python manage.py shell`).
    -   Import a task and execute it with `.delay()`:
        ```python
        from apps.users.tasks import add
        result = add.delay(5, 10)
        ```
    -   Check the logs of the `worker` container (`docker-compose logs worker`). Verify that the "Adding 5 + 10" log message appears.
    -   Check the result: `result.ready()` should eventually be `True`, and `result.get()` should be `15`.

2.  **Periodic Task Scheduling:**
    -   Check the logs of the `beat` container (`docker-compose logs beat`). Verify that it starts without errors and identifies the scheduled tasks.
    -   To test a periodic task without waiting, temporarily change its schedule to run every minute (`crontab(minute='*')`), restart the services, and watch the worker logs to see it being executed.

3.  **Graceful Shutdown:**
    -   Run `docker-compose stop`.
    -   Observe the logs. The worker should show a `worker: warm shutdown` message, indicating it's finishing its current tasks before exiting.

4.  **Retry Mechanism:**
    -   Create a test that calls a retry-able task that is designed to fail once.
    -   Verify from the worker logs that the task is retried after the specified delay.
