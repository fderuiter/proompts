# 14. Observability

**Goal:** Instrument the application to provide tracing, structured logging, and basic metrics, enabling better monitoring and debugging in production.

**Context:**
*   This task is for applications that have poor visibility into their runtime behavior, making it difficult to diagnose issues.
*   Observability is often described as having three pillars: logs, metrics, and traces.

**Tasks:**

1.  **Implement Distributed Tracing:**
    *   Integrate an Application Performance Monitoring (APM) tool like `Sentry` or an OpenTelemetry (`OTEL`) SDK.
    *   Configure the tool to automatically instrument incoming requests, database queries, and other common operations.
    *   This will allow you to trace the lifecycle of a request as it moves through your application and even across different services.

2.  **Set Up Structured Logging:**
    *   Replace standard `print()` statements and basic logging with a structured logging library like `structlog`.
    *   Configure the logger to output logs in a machine-readable format, such as JSON.
    *   Include a request ID and other contextual information (e.g., user ID, endpoint) in every log message. This allows you to easily correlate all the log entries for a single request.

3.  **Expose Basic Prometheus Metrics:**
    *   Add a library like `prometheus-flask-exporter` to the application.
    *   Expose a `/metrics` endpoint that provides basic metrics in the Prometheus format, such as:
        *   Request latency (as a histogram).
        *   Request counts by endpoint, method, and status code.
        *   Information about the Python runtime.

**Deliverables:**
*   A diff showing the new observability-related dependencies and their configuration.
*   Example log output in the new structured JSON format.
*   A screenshot or link to the APM tool showing a trace for a request.

**Acceptance Criteria:**
*   The application automatically sends traces and error reports to the configured APM backend (e.g., Sentry).
*   Logs are written to standard output in a structured JSON format.
*   A request to the `/metrics` endpoint returns a valid Prometheus metrics payload.
*   Traces and logs are correlated with a unique request ID.

**Agent Tips:**
*   When setting up tracing, make sure the APM agent is initialized as early as possible in the application's startup process.
*   Structured logging is most powerful when you adopt it consistently. Avoid mixing structured and unstructured logs.
*   The request ID should be generated at the edge of your system (e.g., by your load balancer or in a middleware) and then passed through to all downstream services and log messages.
*   Don't log sensitive information like passwords, API keys, or personally identifiable information (PII). Use a filter to scrub this data from your logs.
