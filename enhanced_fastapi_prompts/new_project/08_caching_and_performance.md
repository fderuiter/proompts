# 8. Caching and Performance Baseline

**Objective:**
Integrate a Redis-based caching layer to improve application performance and establish a baseline for key performance metrics like latency and query counts.

**Context:**
- **Cache Backend:** `Redis`
- **Cache Helper:** `src/app/core/cache.py`
- **Performance Documentation:** `docs/performance.md`

**Agent Instructions:**
-   Implement a simple, reusable helper for interacting with the Redis cache.
-   Identify and optimize at least one potential N+1 query problem, even if it's in an example endpoint.
-   Enable Gzip compression at the middleware level to reduce response sizes.

**Tasks:**

1.  **Set Up Redis:**
    -   Add `redis` to the project dependencies.
    -   Add a `redis` service to the `docker-compose.yml` file, along with a volume for persistence.
    -   Add `REDIS_URL` to your `settings` model and `.env.example`.

2.  **Create a Cache Helper:**
    -   In `src/app/core/cache.py`, create a `CacheManager` class or functions that wrap the `redis-py` client.
    -   Features should include:
        -   Connection pooling.
        -   Automatic key prefixing to avoid collisions.
        -   Methods for `get`, `set`, and `delete`, with support for TTL.
        -   Handling of serialization/deserialization (e.g., to/from JSON).

3.  **Implement Caching on an Endpoint:**
    -   Choose an example `GET` endpoint.
    -   In the service layer for that endpoint, implement a cache-aside pattern:
        1.  Attempt to fetch the data from Redis first.
        2.  If it's a cache miss, fetch from the database.
        3.  Before returning the data, store it in Redis with a reasonable TTL.

4.  **Profile and Eliminate N+1 Queries:**
    -   Enable query logging in SQLAlchemy's async engine (`echo=True`) for development.
    -   Create an example endpoint that intentionally has an N+1 query problem (e.g., fetching a list of users and then their individual profiles in a loop).
    -   Write a test that asserts the number of queries is high.
    -   Fix the N+1 problem using SQLAlchemy's `selectinload` eager loading strategy.
    -   Update the test to assert that the number of queries is now low (e.g., 2).

5.  **Enable Gzip Compression:**
    -   In `src/app/main.py`, add FastAPI's `GZipMiddleware`.
    -   Set a `minimum_size` (e.g., 1000 bytes) to avoid gzipping very small responses.

6.  **Document Performance Baseline:**
    -   Create a `docs/performance.md` file.
    -   Document the latency of the cached endpoint, showing the difference between a cache hit and miss.
    -   Document the N+1 query optimization, showing the number of SQL queries before and after the fix.
    -   Note that Gzip is enabled.

**Deliverables:**
-   Git diff showing the new `redis` dependency and caching-related code.
-   The `src/app/core/cache.py` helper module.
-   An updated `docker-compose.yml` with a `redis` service.
-   A test case that proves the N+1 query optimization.
-   The `docs/performance.md` file.

**Acceptance Criteria:**
-   The application connects to Redis on startup.
-   Tests for the cached endpoint show that a cache hit is significantly faster than a miss and does not touch the database.
-   The test for the N+1 fix passes, verifying the reduction in database queries.
-   Responses from the API larger than 1000 bytes include the `Content-Encoding: gzip` header.
-   The performance metrics documented in `docs/performance.md` are accurate and reproducible.
