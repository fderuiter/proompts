# 10. Caching and Performance

**Objective:**
Implement a sensible caching strategy to improve response times and reduce database load. Additionally, establish a performance baseline by profiling hot endpoints and optimizing common performance bottlenecks like N+1 queries.

**Context:**
- **Cache Backend:** `Redis`
- **Cache Helper Location:** `{{SRC_DIR}}/app/core/cache.py`
- **Performance Report:** `perf.md`

**Agent Instructions:**
-   Implement a simple, reusable cache helper or decorator to abstract away the Redis client logic.
-   Focus on caching data that is expensive to compute or frequently accessed but changes infrequently.
-   Use profiling tools to identify actual bottlenecks before attempting optimizations.

**Tasks:**

1.  **Set Up Redis Cache:**
    -   Add `redis` to the project dependencies.
    -   In `docker-compose.yml`, ensure a Redis service is available for caching.
    -   In your `core.config.py`, add settings for the Redis cache URL.

2.  **Create a Cache Helper:**
    -   In `{{SRC_DIR}}/app/core/cache.py`, create a simple cache client wrapper or a decorator.
    -   The helper should manage connections and provide simple `get` and `set` methods.
    -   Key features should include:
        -   **Key Prefixing:** Automatically prefix all cache keys (e.g., `f"myapp-cache:{key}"`) to avoid collisions.
        -   **Default TTL:** Allow setting a default Time-To-Live (TTL) for keys.
        -   **Serialization:** Handle serialization/deserialization (e.g., JSON) if storing complex objects.

3.  **Implement Low-Level Caching:**
    -   Identify a suitable endpoint for caching (e.g., a `GET` endpoint that lists public, rarely changing data).
    -   In the service or repository layer, add caching logic:
        -   First, attempt to fetch the result from the cache.
        -   If it's a cache miss, fetch the data from the database.
        -   Store the result in the cache before returning it.
    -   Demonstrate both getting a cache hit and a cache miss.

4.  **Profile Hot Endpoints:**
    -   Identify 1-2 "hot" (frequently used or slow) endpoints.
    -   Use a profiler (like `cProfile` or a middleware-based profiler) to measure their performance under a sample load.
    -   Alternatively, use logging to count the number of SQL queries executed per request.

5.  **Optimize N+1 Queries:**
    -   Inspect the query logs from the profiling step for the "N+1 selects" anti-pattern.
    -   If found, fix it by using SQLAlchemy's eager loading strategies, such as `selectinload` or `joinedload`.

6.  **Enable Gzip Compression:**
    -   Add `GZipMiddleware` to the FastAPI application in `main.py` to compress responses, reducing payload size for clients that support it.
    -   `app.add_middleware(GZipMiddleware, minimum_size=1000)`

7.  **Create Performance Report (`perf.md`):**
    -   Create a new file, `perf.md`.
    -   Document the baseline performance for the profiled endpoints. Include:
        -   Average latency (e.g., `GET /items - 150ms`).
        -   Number of SQL queries before and after optimization.
    -   Document the results of the cache hit/miss demo.

**Deliverables:**
-   Git diff showing new dependencies, the cache helper, and caching logic.
-   The `perf.md` report with baseline metrics.
-   Logs or screenshots demonstrating a cache hit vs. a cache miss.
-   Logs showing the reduction in SQL queries after fixing an N+1 issue.

**Acceptance Criteria:**
-   The performance baseline documented in `perf.md` is reproducible.
-   Tests for the cached endpoint pass, and it can be demonstrated that subsequent calls are served from the cache.
-   Gzip compression is enabled and verified by checking response headers (`Content-Encoding: gzip`).
-   The application's overall performance is measurably improved for the targeted endpoints.
