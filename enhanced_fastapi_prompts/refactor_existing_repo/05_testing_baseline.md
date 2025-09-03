# 5. Testing Baseline

**Objective:**
Establish a fast, reliable, and asynchronous testing suite. This involves setting up modern testing tools, creating reusable fixtures for core components like the application and database, and seeding the test suite with foundational tests.

**Context:**
- **Test Directory:** `/tests`
- **Target Test Coverage:** `{{TARGET_COVERAGE}}%` (e.g., 80%)
- **Target Max Test Runtime:** `{{MAX_RUNTIME_SECS}}s` (e.g., 30s)

**Agent Instructions:**
-   Focus on creating a testing harness that is easy for developers to use and extend.
-   Tests should be able to run in isolation and not depend on external services.
-   Use asynchronous test patterns to correctly test FastAPI's async capabilities.

**Tasks:**

1.  **Install Core Testing Dependencies:**
    -   Add the following packages to your development/testing dependencies:
        -   `pytest`: The test runner.
        -   `pytest-asyncio`: For running async test functions.
        -   `httpx`: A modern, async-capable HTTP client for testing API endpoints.
        -   `asgi-lifespan`: To manage FastAPI's startup and shutdown events during tests.
        -   `pytest-cov`: For measuring test coverage.
        -   `factory_boy` and `faker`: For generating test data.

2.  **Configure `pytest`:**
    -   Create a `pytest.ini` or add a `[tool.pytest.ini_options]` section to `pyproject.toml`.
    -   Configure `asyncio_mode = "auto"`.
    -   Define test paths, markers, and other options as needed.

3.  **Create Core Fixtures (`/tests/conftest.py`):**
    -   **App Fixture:** A fixture that creates an instance of the FastAPI application for testing.
    -   **Async Test Client Fixture:** A fixture that yields an `httpx.AsyncClient` configured to talk to the test app. This will be the primary tool for API tests.
    -   **Database Fixture:** A fixture that sets up a clean, isolated test database for each test function or session. It should create the schema and optionally seed data. For async tests, this must use an `AsyncSession`.
    -   **Event Loop Fixture:** `pytest-asyncio` provides this, but ensure it's configured correctly if needed.

4.  **Seed with Foundational Tests:**
    -   **Health Check Test:** A simple test to hit a `/health` or similar endpoint and assert a `200 OK` response.
    -   **OpenAPI Schema Test:** A test that fetches `/openapi.json` and asserts it's valid JSON and contains expected paths.
    -   **Error Handler Test:** A test that intentionally triggers a standard error (e.g., `404 Not Found`) and asserts that your custom error envelope is returned correctly.
    -   **Basic CRUD Test:** For a representative resource, write a test that covers Create, Read, Update, and Delete operations, asserting both the API responses and the database state changes.

5.  **Configure Test Coverage:**
    -   Configure `pytest-cov` (usually in `pyproject.toml` or `.coveragerc`) to measure coverage of your application source directory (e.g., `/src/app`).
    -   Exclude non-relevant files like `__init__.py`, `main.py`, or configuration files.

**Deliverables:**
-   Git diff showing the new testing dependencies.
-   The `/tests` directory populated with a `conftest.py` and initial test files.
-   A coverage report summary from the terminal.
-   The configuration file for pytest and coverage (`pytest.ini`, `pyproject.toml`, or `.coveragerc`).

**Acceptance Criteria:**
-   `pytest` runs successfully from the command line.
-   The initial set of tests for health checks, OpenAPI, error handling, and CRUD all pass.
-   A coverage report is generated, and the coverage meets or exceeds `{{TARGET_COVERAGE}}%`.
-   The total test suite runtime is less than or equal to `{{MAX_RUNTIME_SECS}}s`.
