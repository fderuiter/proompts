# 12. Observability

**Goal:** Instrument the application for observability from day one, providing visibility into traces, metrics, and errors.

**Context:**
*   Setting up observability early means you'll have the tools to understand and debug your application's behavior as soon as it's deployed.
*   This involves integrating tools for the three pillars of observability: logs, metrics, and traces.

**Tasks:**

1.  **Set Up Error Tracking and Tracing:**
    *   Choose and integrate an Application Performance Monitoring (APM) tool. `Sentry` is a great choice for Flask, as is the `OpenTelemetry` SDK.
    *   Add the chosen library to the dependencies.
    *   Initialize the SDK in the application factory (`create_app`). The DSN or API key should be loaded from the environment.
    *   This will provide automatic error reporting and distributed tracing for web requests, database queries, and other instrumented libraries.

2.  **Implement Structured Logging:**
    *   Add `structlog` to the dependencies.
    *   In `src/app/core/logging.py`, configure `structlog` to output JSON-formatted logs in production and colorized, human-readable logs in development.
    *   Create a middleware that injects the current request ID (from the request context) into the `structlog` context. This will ensure all log messages produced during a request are tagged with that request's ID.

3.  **Expose Prometheus Metrics:**
    *   Add `prometheus-flask-exporter` to the dependencies.
    *   Initialize the extension in the application factory.
    *   This will automatically expose a `/metrics` endpoint with default metrics for request latency, counts, and other useful information.

**Deliverables:**
*   The integrated observability libraries (`Sentry` or `OTEL`, `structlog`, `prometheus-flask-exporter`).
*   The structured logging configuration.
*   The `/metrics` endpoint.
*   An updated `README.md` with a brief explanation of the observability setup.

**Acceptance Criteria:**
*   Errors that occur in the application are automatically captured and visible in the Sentry (or other APM) dashboard.
*   Traces for web requests are visible in the APM dashboard.
*   Logs are output in a structured JSON format when the app is run in a production environment.
*   All log messages for a given request are tagged with the same `request_id`.
*   The `/metrics` endpoint is available and returns a valid Prometheus-formatted response.

**Agent Tips:**
*   Initialize your APM SDK as early as possible in your application's startup (`create_app`) to ensure it can capture as much as possible.
*   `structlog` is very powerful. You can add processors to its pipeline to automatically add information to your logs, such as the current timestamp, log level, and logger name.
*   When a user reports a bug, the first thing you should ask for is the `request_id` from the error message. This ID will allow you to instantly find all the logs and the full trace for that specific request, making debugging much easier.
*   Don't log sensitive data! Use `structlog` processors or logging filters to scrub things like passwords, API keys, and PII from your logs before they are written.
