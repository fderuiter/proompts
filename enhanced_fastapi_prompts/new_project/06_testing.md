# 6. Solid Testing Harness

**Objective:**
Establish a comprehensive and efficient asynchronous testing harness using `pytest`. This includes setting up core fixtures, defining test markers, and aiming for high test coverage from the start.

**Context:**
- **Test Runner:** `pytest`
- **Test Directory:** `/tests`
-   **Fixtures File:** `/tests/conftest.py`
- **Target Coverage:** `{{TARGET_COVERAGE}}%` (e.g., 85%)

**Agent Instructions:**
-   Tests must be fully isolated from each other and from external services.
-   Use `pytest` fixtures to create reusable setup and teardown logic for components like the database and API client.
-   Leverage `pytest-asyncio` to write clean, modern asynchronous tests.

**Tasks:**

1.  **Install Testing Dependencies:**
    -   Add the following to your dev dependencies:
        -   `pytest`
        -   `pytest-asyncio`
        -   `httpx` (for making async requests to the app)
        -   `asgi-lifespan` (to handle FastAPI startup/shutdown events in tests)
        -   `pytest-cov` (for coverage)
        -   `factory_boy` and `Faker` (for test data generation)

2.  **Configure `pytest`:**
    -   In `pyproject.toml` or `pytest.ini`, configure `pytest`:
        -   `asyncio_mode = "auto"`
        -   Define test path: `testpaths = ["tests"]`
        -   Define markers for organizing tests: `markers = ["slow", "integration", "e2e"]`

3.  **Create Core Fixtures in `conftest.py`:**
    -   **`event_loop`:** A session-scoped event loop fixture.
    -   **`db_session`:** An async fixture that:
        -   Connects to a separate test database.
        -   Creates all tables before tests run (`yield`ing a session).
        -   Drops all tables after tests are done.
        -   Uses transactions to isolate each test function.
    -   **`app`:** A fixture that creates an instance of the FastAPI application.
    -   **`async_client`:** A fixture that provides a ready-to-use `httpx.AsyncClient` for making requests to the test `app`.

4.  **Implement Test Data Factories:**
    -   Create a `/tests/factories.py` module.
    -   Use `factory_boy` to create factories for your database models (e.g., `UserFactory`).
    -   This allows you to easily generate valid, randomized test data (e.g., `user = UserFactory()`).

5.  **Write Initial Test Suites:**
    -   **/tests/api/:** Create end-to-end tests for your API endpoints.
        -   Use the `async_client` fixture.
        -   Test success cases, error cases (4xx), and authentication/authorization.
    -   **/tests/repositories/:** Create integration tests for your repository methods.
        -   Use the `db_session` and factory fixtures.
        -   Test that data is correctly written to and read from the test database.
    -   **/tests/services/:** Create unit tests for your service layer logic.
        -   Mock repository dependencies to test business logic in isolation.

6.  **Configure Coverage Measurement:**
    -   In `pyproject.toml` or `.coveragerc`, configure `pytest-cov` to:
        -   Measure coverage for your source directory (`src/app`).
        -   Generate an HTML report for inspection (`--cov-report=html`).
        -   Fail if coverage drops below the `{{TARGET_COVERAGE}}`.

**Deliverables:**
-   Git diff showing new testing dependencies.
-   The `/tests` directory populated with `conftest.py`, `factories.py`, and initial test suites.
-   Configuration for `pytest` and `pytest-cov` in `pyproject.toml`.
-   A `Makefile` target (`make test-cov`) to run tests with coverage reporting.
-   An HTML coverage report.

**Acceptance Criteria:**
-   `make test` runs all tests, and they all pass.
-   The test suite runs against an isolated test database, not the development database.
-   The generated coverage report shows that the coverage level is at or above `{{TARGET_COVERAGE}}%`.
-   Tests are organized using markers, and a subset of tests can be run (e.g., `pytest -m "not slow"`).
-   End-to-end API tests correctly use the `async_client` to test the running application.
