# 5. Data Layer

**Goal:** Set up a robust data layer using SQLAlchemy for object-relational mapping (ORM) and Alembic for database migrations.

**Context:**
*   A solid data layer is fundamental to any database-driven application.
*   This task establishes the patterns for defining models, managing database sessions, and handling schema changes.

**Tasks:**

1.  **Integrate SQLAlchemy:**
    *   Add `SQLAlchemy` and the appropriate database driver (e.g., `psycopg2-binary` for PostgreSQL) to the dependencies.
    *   In `src/app/db/session.py`, create the SQLAlchemy `engine` and `sessionmaker`.
    *   The database connection URL should be loaded from the application's configuration.

2.  **Set Up Alembic for Migrations:**
    *   Initialize Alembic in the project (`alembic init migrations`).
    *   Configure `alembic.ini` and `migrations/env.py` to:
        *   Connect to the database using the URL from the application's config.
        *   Automatically detect model changes by pointing to the `db.models.Base`.
    *   Establish a clear naming convention for migration files (e.g., `YYYYMMDD_HHMM_description`).

3.  **Define Base Models and a First Model:**
    *   In `src/app/db/models.py`, create a declarative base (`Base = declarative_base()`). All models will inherit from this.
    *   Create the first model for your application (e.g., the `User` model from the auth task, or the `Item` model from the API task).

4.  **Create Initial Migration and Seed Script:**
    *   Generate the first Alembic migration script (`alembic revision --autogenerate -m "Create initial tables"`).
    *   Review the generated script to ensure it's correct.
    *   In `scripts/seed.py`, write a simple script that uses the SQLAlchemy models and session to populate the database with some initial data for development.

5.  **Implement Repository/Unit of Work Helpers:**
    *   In `src/app/repositories/`, create a base repository class with common CRUD methods (`create`, `get`, `update`, `delete`).
    *   Implement a "Unit of Work" (UoW) pattern to manage transaction boundaries. The UoW can be a context manager that provides a session and handles commit/rollback logic. This is often done in a base service or repository.

**Deliverables:**
*   SQLAlchemy and Alembic configuration.
*   The first database model(s).
*   The first Alembic migration file.
*   A seed script for initial data.
*   Base classes/helpers for the repository and Unit of Work patterns.

**Acceptance Criteria:**
*   The `alembic upgrade head` command successfully applies the initial migration to a fresh database.
*   The `alembic downgrade base` command successfully reverts the migration.
*   The seed script runs without errors and populates the database.
*   CRUD tests for the first model pass, demonstrating that the data layer is working correctly.

**Agent Tips:**
*   The `env.py` file in Alembic is tricky. You'll need to make sure its `target_metadata` is set to your model's `Base.metadata`.
*   Always manually review auto-generated migrations. Alembic is good, but it's not perfect and can sometimes miss things, especially with complex schema changes.
*   The Unit of Work pattern is powerful for ensuring data consistency. A typical usage in a service might look like:
    ```python
    def create_user(self, user_data):
        with self.uow as uow:
            user = self.user_repo.create(user_data, session=uow.session)
            uow.commit()
            return user
    ```
*   Use a tool like `docker-compose` to run your database in a container for local development. This ensures a clean and consistent database environment.
