# 8. Data Layer & Migrations

**Objective:**
Establish a modern, asynchronous, and reliable data layer using SQLAlchemy 2.x and Alembic for database migrations. This involves setting up an async database engine, implementing the repository pattern for clean data access, and ensuring a repeatable migration process.

**Context:**
- **Database Dialect:** `postgresql+asyncpg` (or other async dialect)
- **SQLAlchemy Version:** `2.x`
- **DB Session File:** `{{SRC_DIR}}/app/db/session.py`
- **Models File:** `{{SRC_DIR}}/app/db/models.py`
- **Alembic Directory:** `/alembic`

**Agent Instructions:**
-   Ensure all database interactions are non-blocking by using `asyncio` with SQLAlchemy's async features.
-   The repository pattern should be used to abstract database logic from the service layer.
-   Alembic migrations should be the *only* way schema changes are applied.

**Tasks:**

1.  **Upgrade Dependencies:**
    -   Ensure `sqlalchemy` is version 2.0 or higher.
    -   Add `alembic` for migrations.
    -   Add an async database driver, e.g., `asyncpg` for PostgreSQL.

2.  **Configure Async SQLAlchemy Engine:**
    -   In `{{SRC_DIR}}/app/db/session.py`, create the async engine:
        ```python
        from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
        from sqlalchemy.orm import sessionmaker

        engine = create_async_engine(settings.DATABASE_URL)
        AsyncSessionFactory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        ```
    -   Create a dependency-injection-friendly function to get a database session:
        ```python
        async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
            async with AsyncSessionFactory() as session:
                yield session
        ```

3.  **Refactor Models and Repositories:**
    -   Ensure SQLAlchemy models in `{{SRC_DIR}}/app/db/models.py` are compatible with the latest SQLAlchemy version (e.g., using type-annotated mappings).
    -   Refactor all data access logic (CRUD operations) into repository classes (`{{SRC_DIR}}/app/repositories/`).
    -   Each method in a repository must be `async` and use `await` for database calls (e.g., `await session.execute(...)`, `await session.commit()`).
    -   Repositories should be initialized with an `AsyncSession`.

4.  **Set Up Alembic for Migrations:**
    -   Run `alembic init alembic` to create the migration environment.
    -   In `alembic/env.py`, configure it for async usage and point it to your SQLAlchemy models' `Base.metadata`.
    -   In `alembic.ini`, set the `sqlalchemy.url` to your database connection string.
    -   Generate an initial migration if the database already has a schema: `alembic revision --autogenerate -m "Initial schema"` followed by `alembic stamp head`.
    -   Establish and document a clear naming convention for migration files.

5.  **Implement Transaction Management:**
    -   The service layer should control the unit of work. A service method should receive a session, call one or more repository methods, and then commit or rollback the session.
    -   Consider creating a decorator or context manager for handling transactions to reduce boilerplate.

**Deliverables:**
-   Git diff showing updated dependencies and code changes in the `db` and `repositories` modules.
-   The complete `/alembic` directory and `alembic.ini` file.
-   The first migration file in `/alembic/versions/`.
-   Example of a refactored `async` repository method.

**Acceptance Criteria:**
-   `alembic upgrade head` and `alembic downgrade -1` commands execute successfully without errors.
-   All existing tests that interact with the database are updated to use the new `async` session and repository patterns, and they all pass.
-   A new, simple CRUD test for an async endpoint passes, confirming the end-to-end async data layer is working.
-   The application runs without any synchronous IO warnings from asyncio.
