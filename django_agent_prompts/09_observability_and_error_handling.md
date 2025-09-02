# Agent Prompt: Implement Observability and Error Handling

## 1. Objective

To integrate robust observability tools into a Django project for comprehensive error tracking, performance monitoring, structured logging, and application health checking.

## 2. User-Provided Parameters

-   **Error Tracking Service:** `{{Sentry | other}}`
-   **Sentry DSN Environment Variable:** `SENTRY_DSN`

## 3. Agent Execution Plan

### Phase 1: Structured Logging

1.  **Install Logging Library (if not standard `logging`):**
    -   Add `structlog` to dependencies (recommended for ease of use).

2.  **Configure `LOGGING` in `settings/prod.py`:**
    -   Set up a logging configuration that outputs structured JSON to `stdout`.
    -   Define formatters (e.g., `json_formatter` using `structlog.stdlib.JSONRenderer`), handlers (`console` that outputs to `sys.stdout`), and loggers.
    -   Ensure the root logger and the `django` logger are configured to use this handler.

3.  **Implement Request Correlation IDs:**
    -   Create a middleware that generates a unique ID (e.g., `request_id`) for each incoming request.
    -   Store this ID in a thread-local variable (or context var for async code).
    -   Configure the logger (e.g., via a `structlog` processor) to automatically include this `request_id` in every log message generated during that request's lifecycle.
        ```python
        # In a new middleware file
        import uuid
        from .logging_context import set_request_id

        class CorrelationIdMiddleware:
            def __init__(self, get_response):
                self.get_response = get_response

            def __call__(self, request):
                request_id = str(uuid.uuid4())
                set_request_id(request_id)
                response = self.get_response(request)
                response["X-Request-ID"] = request_id
                return response
        ```
    -   Add this middleware early in the `MIDDLEWARE` list.

### Phase 2: Error Tracking with Sentry

1.  **Install Sentry SDK:**
    -   Add `sentry-sdk[django]` to the project's dependencies.

2.  **Initialize Sentry:**
    -   In `settings/prod.py` (or `base.py` if DSN is guarded), initialize the Sentry SDK.
        ```python
        import sentry_sdk
        from sentry_sdk.integrations.django import DjangoIntegration
        from sentry_sdk.integrations.celery import CeleryIntegration
        from sentry_sdk.integrations.redis import RedisIntegration

        SENTRY_DSN = env("SENTRY_DSN", default=None)
        if SENTRY_DSN:
            sentry_sdk.init(
                dsn=SENTRY_DSN,
                integrations=[
                    DjangoIntegration(),
                    CeleryIntegration(),
                    RedisIntegration(),
                ],
                traces_sample_rate=0.2, # Sample 20% of transactions for performance
                send_default_pii=True, # Set to False if you don't want to send user IPs
            )
        ```

3.  **Create a Deliberate Error:**
    -   Create a temporary URL and view that raises an exception to test the Sentry integration.
        ```python
        # In a temporary urls.py
        path("sentry-debug/", lambda request: 1 / 0),
        ```

### Phase 3: Health and Liveness Endpoints

1.  **Create a `health` App:**
    -   If it doesn't exist, create an `apps/health` app.

2.  **Implement Health Check View:**
    -   Create a view in `apps/health/views.py`.
    -   **Liveness (`/api/v1/health/live/`):** A simple endpoint that returns `200 OK`. This tells an orchestrator (like Kubernetes) that the application process is running.
    -   **Readiness (`/api/v1/health/ready/`):** A more comprehensive check. This endpoint should:
        -   Attempt to connect to the database.
        -   Attempt to connect to the cache (Redis).
        -   Check any other critical downstream services.
        -   If all checks pass, return `200 OK`. If any fail, return `503 Service Unavailable`. This tells the orchestrator not to send traffic to this container.

3.  **Add URLs:**
    -   Add the `live` and `ready` endpoints to your API's URL configuration. Make these endpoints public (e.g., `permission_classes = [AllowAny]`).

### Phase 4: Basic Metrics

1.  **Add Metrics Middleware (if needed):**
    -   For a simple approach, create middleware that tracks basic request metrics.
    -   On request start, record `time.time()`.
    -   On response, calculate `latency = time.time() - start_time`.
    -   Log the latency, status code, and path.
        ```
        logger.info(
            "request_finished",
            extra={
                "path": request.path,
                "method": request.method,
                "status_code": response.status_code,
                "latency_ms": latency * 1000,
            }
        )
        ```
    -   *Note: For production systems, using a dedicated metrics library like `django-prometheus` is a better long-term solution.*

## 4. Final Verification Criteria

1.  **Structured Logs:**
    -   Start the application and make a request.
    -   Check the `stdout` of the `web` container.
    -   Verify that logs are formatted as single-line JSON objects.
    -   Verify that each log line from a single request shares the same `request_id`.
    -   Verify the `X-Request-ID` header is present in the HTTP response.

2.  **Sentry Error Capture:**
    -   Set a valid `SENTRY_DSN` in your environment.
    -   Access the debug URL that raises an exception (`/sentry-debug/`).
    -   Log in to the Sentry project dashboard.
    -   Verify that the `ZeroDivisionError` appears as a new issue.
    -   Check that the issue details include context like user information (if logged in), request headers, and tags.

3.  **Health Endpoints:**
    -   Access the liveness endpoint (`/api/v1/health/live/`). It must return a `200 OK`.
    -   Access the readiness endpoint (`/api/v1/health/ready/`). It must return `200 OK` if all services are connected.
    -   To test failure, stop the `db` container (`docker-compose stop db`) and access the readiness endpoint again. It must now return a `503 Service Unavailable`.

4.  **Metrics Logs:**
    -   Make several requests to different endpoints.
    -   Review the application logs. Verify that `request_finished` log messages are being generated with latency and status code information.
