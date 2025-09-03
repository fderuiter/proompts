# 12. Day-One Observability

**Objective:**
Integrate foundational observability tools for structured logging, error reporting, and distributed tracing from the beginning, ensuring the application is "production-ready" from an operational standpoint.

**Context:**
- **Error Reporting:** `Sentry`
- **Tracing & Metrics:** `OpenTelemetry`
- **Logging Config:** `src/app/core/logging.py`
- **Observability Wiring:** `src/app/main.py`

**Agent Instructions:**
-   Instrument the application to provide correlated logs, traces, and errors out of the box.
-   Use a request ID as the glue that ties all observability signals for a single transaction together.
-   All external service configurations (like Sentry DSN) must be loaded from the central `settings` object.

**Tasks:**

1.  **Set Up Structured Logging:**
    -   Add `structlog` as a dependency.
    -   In `src/app/core/logging.py`, configure `structlog` to output JSON-formatted logs.
    -   Include a standard set of processors to add context like timestamp, log level, and logger name.

2.  **Implement Request ID Middleware:**
    -   In `src/app/main.py`, add a middleware that:
        1.  Generates a unique request ID for each incoming request.
        2.  Adds the request ID to a `contextvars` variable.
        3.  Binds the request ID to `structlog`'s context.
        4.  Adds the request ID to the response headers (e.g., `X-Request-ID`).

3.  **Integrate Sentry for Error Reporting:**
    -   Add `sentry-sdk[fastapi]` as a dependency.
    -   In `src/app/main.py`, initialize the Sentry SDK, loading the DSN from `settings`.
    -   Enable the performance monitoring and traces sampler to integrate Sentry with tracing.
    -   The SDK will automatically capture unhandled exceptions.

4.  **Integrate OpenTelemetry for Tracing:**
    -   Add OpenTelemetry dependencies: `opentelemetry-sdk`, `opentelemetry-exporter-otlp`, and auto-instrumentation packages (`opentelemetry-instrumentation-fastapi`, `opentelemetry-instrumentation-sqlalchemy`, `opentelemetry-instrumentation-httpx`).
    -   Create a configuration function that sets up the OTEL SDK, a trace processor, and an exporter.
    -   Use the Sentry OTEL exporter to send traces to Sentry, or configure a standard OTLP exporter for another backend like Jaeger or Honeycomb.
    -   Run the application via `opentelemetry-instrument` to apply the auto-instrumentation.

5.  **Expose Prometheus Metrics:**
    -   Add `starlette-prometheus` as a dependency.
    -   In `src/app/main.py`, add the middleware to expose a `/metrics` endpoint. This provides basic request latency and count metrics by default.

**Deliverables:**
-   Git diff showing new dependencies and observability code.
-   Example JSON log output that includes a `request_id`.
-   A `curl` command showing the `X-Request-ID` in the response headers.
-   A screenshot from Sentry showing a captured error, tagged with the corresponding request ID.
-   A screenshot from the tracing backend (Sentry, Jaeger, etc.) showing a trace for a request that includes spans for the API and a database call.

**Acceptance Criteria:**
-   All logs are output in JSON format and contain a `request_id`.
-   Unhandled exceptions are automatically captured in Sentry.
-   Traces are generated for requests and are visible in the configured backend.
-   Logs, traces, and errors for a single request are correlated by the same ID.
-   The `/metrics` endpoint is available and serves metrics in Prometheus format.
-   The application functions correctly with all observability tools enabled.
