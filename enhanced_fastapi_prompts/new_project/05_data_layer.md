# 5. Data Layer with Migrations

**Objective:**
Implement a fully asynchronous data access layer using SQLAlchemy 2.x, with a repeatable and reliable database migration process managed by Alembic.

**Context:**
- **SQLAlchemy Version:** `2.x`
- **Database Driver:** `asyncpg` (for PostgreSQL)
- **Session Management:** `src/app/db/session.py`
- **Models:** `src/app/db/models.py`
- **Repositories:** `src/app/repositories/`
- **Migrations:** `/alembic`

**Agent Instructions:**
-   All database code must be asynchronous, using `async/await` syntax.
-   Abstract database queries into repository classes to decouple business logic from data access logic.
-   Establish a clean, scripted process for database migrations.

**Tasks:**

1.  **Install Dependencies:**
    -   Add `sqlalchemy[asyncio]` (ensure it's v2.x).
    -   Add `alembic`.
    -   Add the async database driver, `asyncpg`.

2.  **Configure Async SQLAlchemy:**
    -   In `src/app/db/session.py`, create the async engine and session factory, configured from the main `settings` object.
        ```python
        from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
        from sqlalchemy.orm import sessionmaker

        engine = create_async_engine(settings.DATABASE_URL, echo=True) # echo for dev
        AsyncSessionFactory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        ```
    -   Create a `get_db_session` dependency injector that yields an `AsyncSession`.

3.  **Define Base Models:**
    -   In `src/app/db/models.py`, define a declarative base class (`Base = declarative_base()`).
    -   Create an example `User` model that inherits from `Base`, including fields for `id`, `email`, `hashed_password`, and `role`. Use SQLAlchemy 2.0 `Mapped` and `mapped_column` syntax.

4.  **Set Up Alembic:**
    -   In the project root, run `alembic init alembic`.
    -   Configure `alembic.ini` with the `sqlalchemy.url` from your `settings`.
    -   In `alembic/env.py`:
        -   Import your `Base` from `src/app/db/models.py` and set `target_metadata = Base.metadata`.
        -   Configure it to work with an async driver.

5.  **Create Initial Migration:**
    -   Run `alembic revision --autogenerate -m "Create initial user table"` to create the first migration script.
    -   Inspect the generated script to ensure it's correct.
    -   Run `alembic upgrade head` to apply the migration to your local database.

6.  **Implement Repository and Unit of Work Patterns:**
    -   Create a `BaseRepository` class in `src/app/repositories/base.py`.
    -   Create a `UserRepository` in `src/app/repositories/user.py` that inherits from it.
    -   Implement `async` methods for CRUD operations (e.g., `async def create_user(...)`, `async def get_user_by_email(...)`). All methods should accept an `AsyncSession` as an argument.
    -   The service layer will be responsible for the "Unit of Work": creating the session, passing it to repositories, and committing or rolling back.

**Deliverables:**
-   Git diff showing new dependencies and data layer files.
-   The `/alembic` directory and `alembic.ini` configuration.
-   The first migration file in `/alembic/versions/`.
-   The `User` model, `UserRepository`, and `get_db_session` dependency.
-   A script or `Makefile` target (e.g., `make db-migrate`) to run `alembic upgrade head`.

**Acceptance Criteria:**
-   The `make db-migrate` command (or equivalent) successfully applies the initial migration to an empty database.
-   `alembic downgrade base` and `alembic upgrade head` can be run back-to-back without errors.
-   Unit/integration tests for the `UserRepository` pass. These tests should:
    -   Use a separate, clean test database.
    -   Create a user and verify it exists in the database.
    -   Fetch a user by email and verify the data is correct.
-   The application correctly connects to the database on startup.
