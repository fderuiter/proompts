# 3. Modularization and Boundaries

**Goal:** Restructure the application into cohesive, loosely-coupled modules with well-defined boundaries to improve maintainability and scalability.

**Context:**
*   This task is for applications that have grown organically and now suffer from circular dependencies, mixed concerns, and a lack of clear structure.
*   The proposed structure follows a standard service-repository pattern, which is common in modern web applications.

**Proposed Layout:**

```
/src/app/
├── api/
│   └── v1/
│       └── blueprints/
│           ├── __init__.py
│           └── users.py         # Example blueprint for a resource
├── services/
│   ├── __init__.py
│   └── user_service.py    # Business logic for users
├── repositories/
│   ├── __init__.py
│   └── user_repository.py # Data access logic for users
├── schemas/
│   ├── __init__.py
│   └── user_schema.py     # Marshmallow/Pydantic schemas for users
├── db/
│   ├── models.py          # SQLAlchemy models
│   └── session.py         # DB session management
└── libs/
    └── *.py               # Shared, independent libraries
```

**Tasks:**

1.  **Restructure into Blueprints:**
    *   Move all route definitions from a monolithic `routes.py` or `app.py` into separate blueprint files.
    *   Group related endpoints into the same blueprint (e.g., all user-related endpoints in `users.py`).
    *   Organize blueprints under a versioned API folder (e.g., `/api/v1/blueprints/`).

2.  **Implement Service/Repository Pattern:**
    *   **Services (`/src/app/services/`):**
        *   Create service classes or modules that encapsulate the business logic of the application.
        *   Services should orchestrate calls to repositories and other services. They should not directly interact with the database or the HTTP request/response cycle.
    *   **Repositories (`/src/app/repositories/`):**
        *   Create repository classes or modules responsible for all data access logic.
        *   They should abstract away the database, providing a clean API for querying and modifying data (e.g., `get_user_by_id`, `create_user`).

3.  **Enforce Import Boundaries:**
    *   Use a tool like `import-linter` or Ruff's import rules (`lint.allowed-imports`) to enforce architectural boundaries.
    *   Define rules to prevent:
        *   Blueprints from importing directly from repositories (they should go through services).
        *   Repositories from importing from services or blueprints.
        *   Business logic (services, repositories) from importing from presentation layers (blueprints).
    *   Add a script to your `Makefile` or `pyproject.toml` to run the import linter.

**Deliverables:**
*   A diff of the changes, showing the new directory structure and the refactored code.
*   The configuration file for the import linter (`.importlinter` or `pyproject.toml`).
*   A brief document explaining the new architecture and the rationale behind it.

**Acceptance Criteria:**
*   The application is restructured according to the proposed layout.
*   The import linter or Ruff rules pass with zero forbidden import violations.
*   All existing application functionality remains intact, and all tests pass.
*   The separation of concerns is clear: blueprints for API, services for business logic, repositories for data access.

**Agent Tips:**
*   Start by refactoring one resource at a time. For example, focus on "users" first.
*   Create the necessary service and repository for the resource, then move the routes to the new blueprint.
*   After refactoring, write the import linting rules. This will help you catch any mistakes you made.
*   Be prepared to update tests to reflect the new structure. You may need to mock services instead of database models.
