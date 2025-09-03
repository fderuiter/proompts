# 8. Caching and Performance

**Goal:** Integrate a caching layer and establish a performance baseline for the application from the start.

**Context:**
*   Proactively setting up caching and performance monitoring helps prevent issues as the application grows.
*   The caching backend will be Redis.

**Tasks:**

1.  **Integrate Flask-Caching:**
    *   Add `Flask-Caching` to the dependencies.
    *   Initialize the extension in the application factory (`create_app`).
    *   Configure it to use a Redis backend, with the URL loaded from the environment.
    *   Define a clear cache key prefixing strategy in the configuration to avoid key collisions.

2.  **Implement Example Caching:**
    *   Apply caching to a non-critical, read-only endpoint. The `/health` or `/__version__` endpoints are good candidates.
    *   Use the `@cache.cached(timeout=60)` decorator to demonstrate view caching.
    *   This serves as a working example for how to cache other parts of the application.

3.  **Set Up Query Profiling:**
    *   Add a middleware or use a Flask extension that logs database query counts and timings for each request, especially in the development environment.
    *   This provides immediate feedback on how many queries an endpoint is making, helping to spot N+1 issues early.

4.  **Enable Gzip and ETag Support:**
    *   Configure the WSGI server (`gunicorn`) or a reverse proxy to compress responses with `gzip`.
    *   Use a Flask extension or middleware to automatically add `ETag` headers to responses. This allows for conditional GET requests, saving bandwidth. `Flask-Caching` has some support for this.

**Deliverables:**
*   The `Flask-Caching` extension integrated and configured.
*   An example of a cached view.
*   A `performance.md` document that describes:
    *   The caching strategy.
    *   How to use the query profiler.
    *   The baseline latency and query count for the main endpoints.

**Acceptance Criteria:**
*   The caching backend is Redis, configured via environment variables.
*   The example cached endpoint demonstrates caching behavior (i.e., the second request is faster and doesn't hit the view function).
*   In the development environment, database query information is logged for each request.
*   ETag headers are present on responses.
*   The baseline performance is documented.

**Agent Tips:**
*   Be deliberate about what you cache. Caching can introduce complexity, especially around invalidation. Start with data that changes infrequently.
*   Make it easy to disable caching during local development or for specific requests. This can be done with a configuration flag or a request header.
*   An N+1 query is when your code executes one query to retrieve a list of items, and then N subsequent queries to retrieve related data for each item. These are major performance killers and should be fixed by "eager loading" the related data in the initial query (e.g., using SQLAlchemy's `joinedload` or `selectinload`).
*   The goal here is not to over-optimize, but to put the tools in place to monitor performance and make informed optimizations when needed.
