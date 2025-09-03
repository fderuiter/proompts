# 8. DB Layer and Migrations

**Goal:** Establish a solid, modern, and maintainable persistence layer using SQLAlchemy and Alembic for database migrations.

**Context:**
*   This task is for projects that may be using an older version of SQLAlchemy, have no migration strategy, or have poorly managed database sessions.
*   The focus is on upgrading to SQLAlchemy 2.x patterns, which favor a more explicit, less "magical" API.

**Tasks:**

1.  **Upgrade to SQLAlchemy 2.x:**
    *   Update the `SQLAlchemy` dependency to the latest 2.x version.
    *   Refactor the codebase to use the new 2.0 style of querying (e.g., `select()` statements instead of `Query` objects).
    *   Ensure the database engine and session creation are compatible with the latest version.

2.  **Implement Robust Session Management:**
    *   Create helper functions or context managers for managing the lifecycle of a database session.
    *   A common pattern is to have a session that is created at the beginning of a request and closed (committed or rolled back) at the end. This can be managed with a custom middleware or a decorator.

3.  **Set Up Alembic for Migrations:**
    *   Initialize Alembic in the repository if it's not already present (`alembic init migrations`).
    *   Configure Alembic to connect to your database and to find your SQLAlchemy models.
    *   Establish a clear naming convention for migration files (e.g., `YYYYMMDD_HHMM_add_user_table.py`).
    *   Generate an initial migration that reflects the current state of the database schema.

4.  **Define Transaction Boundaries:**
    *   Refactor business logic (in services) to have clear transaction boundaries.
    *   Use a "Unit of Work" pattern, where all operations within a single business transaction are committed or rolled back together. This prevents leaving the database in an inconsistent state.

5.  **Create Repository Helpers:**
    *   If not already done in the modularization step, create repository classes that encapsulate common database operations.
    *   These helpers should abstract the details of SQLAlchemy, providing a simpler interface to the rest of the application (e.g., `user_repo.get(id)`, `user_repo.create(data)`).

**Deliverables:**
*   A diff showing the updated SQLAlchemy and Alembic dependencies and the refactored database-related code.
*   The Alembic migrations directory with the initial migration file.
*   Updated service layer code that demonstrates clear transaction management.

**Acceptance Criteria:**
*   Alembic migrations can be applied (`alembic upgrade head`) and reverted (`alembic downgrade base`) without errors.
*   All existing CRUD (Create, Read, Update, Delete) tests pass with the new database layer.
*   The application correctly manages database sessions and transactions, preventing leaks and ensuring data consistency.
*   The SQLAlchemy code follows modern 2.x best practices.

**Agent Tips:**
*   Upgrading SQLAlchemy can be a significant undertaking. Do it carefully and test thoroughly.
*   When setting up Alembic, make sure the `env.py` file is correctly configured to find your database models. This is a common point of failure.
*   The "Unit of Work" pattern can be implemented as a context manager that you can use in your service methods:
    ```python
    with unit_of_work() as uow:
        user = user_repo.get(user_id, uow.session)
        user.update(data)
        uow.commit()
    ```
*   Ensure your database connection string is loaded from the environment, not hardcoded.
