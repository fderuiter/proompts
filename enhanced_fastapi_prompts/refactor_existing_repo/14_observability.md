# 14. Observability

**Objective:**
Integrate robust observability tools for structured logging, distributed tracing, and error reporting. This will provide deep insights into the application's performance and behavior in a production environment.

**Context:**
- **Error Reporting Service:** `Sentry` or similar
- **Tracing/Metrics:** `OpenTelemetry` or `Prometheus`
- **Structured Logging Config:** `{{SRC_DIR}}/app/core/logging.py`
- **Runbook Location:** `docs/runbook.md`

**Agent Instructions:**
-   Ensure that logs, traces, and errors are correlated with a unique request ID.
-   Instrument key libraries (like FastAPI, SQLAlchemy, and HTTPX) to automatically generate traces.
-   Configuration, especially sensitive keys for observability services, must be loaded from `settings`.

**Tasks:**

1.  **Implement Structured Logging:**
    -   If not already done, refactor the logging setup in `{{SRC_DIR}}/app/core/logging.py` to output logs in a machine-readable format like JSON.
    -   Libraries like `structlog` are excellent for this.
    -   Each log record should contain a consistent set of fields, including timestamp, log level, message, and context.

2.  **Add Request ID Correlation:**
    -   Create a middleware that generates a unique request ID (e.g., a UUID) for every incoming request.
    -   Store this ID in a context variable (e.g., using `contextvars`) so it can be accessed throughout the application.
    -   Automatically inject the request ID into all log messages.

3.  **Integrate Error Reporting (Sentry):**
    -   Add the `sentry-sdk[fastapi]` dependency.
    -   Initialize Sentry in your `main.py` or `settings.py`, providing the DSN from your environment configuration.
    -   The SDK will automatically capture unhandled exceptions and report them.
    -   Enrich Sentry events by setting the user context and adding the request ID as a tag.

4.  **Set Up Distributed Tracing (OpenTelemetry):**
    -   Add the necessary OpenTelemetry dependencies: `opentelemetry-api`, `opentelemetry-sdk`, and exporters (e.g., `opentelemetry-exporter-otlp`).
    -   Add auto-instrumentation libraries for your stack (e.g., `opentelemetry-instrumentation-fastapi`, `opentelemetry-instrumentation-sqlalchemy`).
    -   Configure the OpenTelemetry SDK to sample traces and export them to a backend (like Jaeger, Honeycomb, or Sentry).
    -   Ensure the trace ID is the same as the request ID for correlation.

5.  **Expose Prometheus Metrics (Optional):**
    -   If using Prometheus, add a library like `starlette-prometheus`.
    -   Add middleware to expose a `/metrics` endpoint that provides default metrics (e.g., request latency, counts, status codes).
    -   Create custom metrics for application-specific events (e.g., users created, orders processed).

6.  **Create a Basic Runbook (`docs/runbook.md`):**
    -   Create a new document, `docs/runbook.md`.
    -   Provide instructions for on-call engineers.
    -   **Key Sections:**
        -   How to access logs, traces, and error reports (with links).
        -   Common error patterns and their likely causes.
        -   How to check the status of the application and its dependencies.
        -   Contact information for the primary owners.

**Deliverables:**
-   Git diff showing new dependencies and observability-related code.
-   The new `docs/runbook.md` file.
-   Example structured log output (in JSON format) showing a request ID.
-   Screenshots from the Sentry (or equivalent) and tracing backends showing:
    -   A captured error with its tags.
    -   A distributed trace for a multi-span request (e.g., API call -> DB query).

**Acceptance Criteria:**
-   When a request is made to the API, logs are generated in JSON format and include a unique `request_id`.
-   When an unhandled exception occurs, it is automatically captured in Sentry (or equivalent) and tagged with the correct `request_id`.
-   When a request is made, a trace is generated and visible in the tracing backend, with spans for the FastAPI entry point and any database calls.
-   The `/metrics` endpoint (if implemented) is available and serves Prometheus-formatted metrics.
-   The `runbook.md` provides a clear starting point for debugging production issues.
