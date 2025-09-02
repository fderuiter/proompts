# Agent Prompt: Improve Performance and Implement Caching

## 1. Objective

To improve the performance and scalability of a Django application by auditing database queries for N+1 problems, adding database indexes, and implementing a multi-level caching strategy with Redis.

## 2. User-Provided Parameters

-   **Target P99 Latency:** `{{ms}}` (e.g., `200ms`) under a specified dev load.
-   **Cache Type:** `{{Redis | Memcached}}` (This guide assumes Redis)

## 3. Agent Execution Plan

### Phase 1: Database Optimization

1.  **Install Query Inspection Tools:**
    -   Add `django-debug-toolbar` to the development dependencies.
    -   Configure it in `settings/dev.py` and add its URLs to the root `urls.py`.

2.  **Audit for N+1 Query Problems:**
    -   Run the application locally and navigate through the main API endpoints and user-facing pages.
    -   Use the Django Debug Toolbar's "DB Queries" panel to identify endpoints that generate a large number of duplicate queries.
    -   For each identified N+1 problem, apply `select_related` (for foreign keys) or `prefetch_related` (for many-to-many or reverse relationships) to the queryset in the relevant view or repository.

3.  **Review Heavy Queries:**
    -   Identify any queries that are particularly slow (high duration in Debug Toolbar).
    -   Use `queryset.explain(analyze=True)` in the `manage.py shell` to get the database's query plan for these slow queries.
        ```python
        # In shell
        from apps.some_app.models import MyModel
        print(MyModel.objects.filter(...).explain(analyze=True))
        ```
    -   Document the output of the `EXPLAIN ANALYZE` for before/after comparison.

4.  **Add Database Indexes:**
    -   Based on the `EXPLAIN ANALYZE` output, identify missing indexes on frequently filtered or joined fields.
    -   Create a new migration using `python manage.py makemigrations --empty yourapp`.
    -   In the migration file, add a `migrations.AddIndex` operation.
        ```python
        # In the new migration file
        from django.db import migrations, models

        class Migration(migrations.Migration):
            dependencies = [...]
            operations = [
                migrations.AddIndex(
                    model_name="mymodel",
                    name="my_model_field_idx",
                    fields=["my_field"],
                ),
            ]
        ```
    -   Run the migration locally (`manage.py migrate`).

### Phase 2: Caching Implementation

1.  **Configure Redis Cache Backend:**
    -   Install `django-redis`.
    -   In `settings/base.py`, configure the `CACHES` setting.
        ```python
        CACHES = {
            "default": {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": env("REDIS_URL"),
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                }
            }
        }
        ```

2.  **Implement Per-View Caching:**
    -   For simple, read-only views or API endpoints that return the same data for all users, apply the `@cache_page` decorator.
    -   Add `django.middleware.cache.UpdateCacheMiddleware` and `django.middleware.cache.FetchFromCacheMiddleware` to your `MIDDLEWARE` settings.
        ```python
        # In a views.py
        from django.views.decorators.cache import cache_page

        @cache_page(60 * 15) # Cache for 15 minutes
        def my_view(request):
            ...
        ```

3.  **Implement Low-Level Cache API:**
    -   For more granular control, use the low-level cache API to store the results of expensive computations or complex database queries.
    -   Wrap the logic in a function that attempts to fetch from the cache first, and if not found, performs the operation and stores the result in the cache.
        ```python
        from django.core.cache import cache

        def get_complex_data(user_id):
            cache_key = f"complex_data_{user_id}"
            result = cache.get(cache_key)
            if result is None:
                # Expensive operation here
                result = ...
                cache.set(cache_key, result, timeout=3600) # Cache for 1 hour
            return result
        ```

### Phase 3: Asynchronous Operations

1.  **Identify Async-Friendly Spots:**
    -   Review views that perform multiple independent, I/O-bound operations (e.g., calling external APIs, multiple non-dependent database queries).
    -   These are good candidates for `async` views.

2.  **Convert to Async Views (where beneficial):**
    -   Convert the view from `def` to `async def`.
    -   Use `asyncio.gather` to run I/O-bound operations concurrently.
    -   Ensure all database access uses Django's async-safe ORM methods (e.g., `await Model.objects.aget(...)`).
        ```python
        import asyncio

        async def my_async_view(request):
            task1 = fetch_external_api_data()
            task2 = Model.objects.acount()
            results = await asyncio.gather(task1, task2)
            # ... process results
            return JsonResponse(...)
        ```

## 4. Final Verification Criteria

1.  **N+1 Problem Resolution:**
    -   Re-visit the pages/endpoints identified in the audit phase.
    -   Using the Django Debug Toolbar, confirm that the number of database queries has been significantly reduced to a constant number, not one that grows with the number of objects.

2.  **Index Application:**
    -   Run `EXPLAIN ANALYZE` on the previously slow queries.
    -   Verify that the new query plan shows the use of the newly created index (e.g., "Index Scan").

3.  **Cache Hits:**
    -   For cached views, verify the `X-Cache` headers or use the Debug Toolbar's "Cache" panel to confirm that subsequent requests are served from the cache.
    -   For low-level caching, add logging or use the `redis-cli MONITOR` command to observe `GET` and `SET` operations on the cache keys.

4.  **Latency Target:**
    -   (If a load testing tool is available) Run a simple load test against the development server.
    -   Measure the P99 latency for key endpoints and verify it is at or below the `{{ms}}` target.
    -   Alternatively, manually time responses for key endpoints before and after changes to demonstrate improvement.
