# 3. Modularization and Boundaries

**Objective:**
Refactor the project structure into a modular, layer-based architecture. This will improve separation of concerns, making the codebase easier to navigate, test, and maintain.

**Context:**
- **Application Source Directory:** `{{SRC_DIR}}` (e.g., `src/`, `app/`)
- **Proposed Structure:**
  ```
  {{SRC_DIR}}/app/
  ├── api/
  │   └── v1/
  │       └── routers/
  │           └── *.py         # API Endpoints/Routers
  ├── core/                  # Core services like config, logging
  ├── db/
  │   ├── models.py        # SQLAlchemy models
  │   └── session.py       # DB session management
  ├── repositories/
  │   └── *.py             # Data access layer
  ├── schemas/
  │   └── *.py             # Pydantic schemas (for API I/O)
  ├── services/
  │   └── *.py             # Business logic layer
  └── main.py                # FastAPI app instantiation
  ```

**Agent Instructions:**
- Carefully move existing code from its current location to the new structure.
- Update all import statements to reflect the new file locations.
- The goal is a structural refactor; avoid changing business logic.
- Use a tool like `importlinter` or `ruff`'s dependency rules (`TID`) to enforce boundaries.

**Tasks:**

1.  **Restructure Directories:**
    -   Create the new directory layout as specified in the `Context`.
    -   Move existing files into their new locations. For example:
        -   API endpoint definitions go into `{{SRC_DIR}}/app/api/v1/routers/`.
        -   Business logic goes into `{{SRC_DIR}}/app/services/`.
        -   Database interaction code (CRUD operations) goes into `{{SRC_DIR}}/app/repositories/`.
        -   Pydantic models for request/response go into `{{SRC_DIR}}/app/schemas/`.
        -   SQLAlchemy models go into `{{SRC_DIR}}/app/db/models.py`.

2.  **Update `main.py`:**
    -   Ensure `{{SRC_DIR}}/app/main.py` is clean. It should primarily be responsible for:
        -   Creating the `FastAPI` app instance.
        -   Including the API routers from the `api/v1/routers` directory.
        -   Configuring middleware and exception handlers.

3.  **Fix Imports:**
    -   Systematically go through all moved files and correct their import statements to point to the new locations. This is the most critical and error-prone step.

4.  **(Optional) Enforce Import Rules:**
    -   Add `importlinter` to dev dependencies or configure `ruff.lint.isort` with `known-local-folder` to help enforce boundaries.
    -   Alternatively, configure Ruff's explicit dependency rules. For example, `services` should not import from `api`.
    -   Create a configuration file (e.g., `.importlinter` or in `pyproject.toml`) that defines the allowed import contracts between layers.
        -   Example contract: `api` can import from `services`, `schemas`. `services` can import from `repositories`, `schemas`. `repositories` can import from `db`.

**Deliverables:**
-   Git diff showing the file moves and import fixes.
-   A tree view of the new project structure.
-   (Optional) The configuration file for the import linting tool (`.importlinter` or `pyproject.toml`).

**Acceptance Criteria:**
-   The application runs correctly with the new structure.
-   All existing tests pass without modification to the test logic itself (fixtures and imports may need updates).
-   (If implemented) The import linter (`importlinter` or `ruff`) passes, confirming that no forbidden cross-layer imports exist.
