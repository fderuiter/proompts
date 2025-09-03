# 6. Testing

**Goal:** Build a solid testing harness from the start, with fixtures, data factories, and clear organization.

**Context:**
*   A good testing setup makes development faster and safer. This task sets up the foundation for all future tests.
*   The target test coverage is `{{TARGET}}%`.

**Tasks:**

1.  **Configure Test Suite with `pytest`:**
    *   Ensure `pytest`, `pytest-flask`, `pytest-cov` are in the development dependencies.
    *   Configure `pytest` in `pyproject.toml` or `pytest.ini`. Define test paths, markers, and default options.
    *   Set up `pytest-cov` to generate HTML and XML coverage reports and to fail if coverage is below `{{TARGET}}%`.

2.  **Create Core Test Fixtures:**
    *   In `tests/conftest.py`, create essential `pytest` fixtures that will be available to all tests:
        *   `app`: An instance of the Flask application, configured for testing.
        *   `client`: A Flask test client for making requests to the `app` fixture.
        *   `db_session`: A SQLAlchemy session for interacting with the test database. This fixture should manage transactions, rolling back changes after each test to ensure isolation.
        *   `runner`: A Flask CLI test runner for testing custom CLI commands.

3.  **Implement Data Factories:**
    *   Add `factory_boy` and `Faker` to the development dependencies.
    *   In `tests/factories.py`, create factories for your database models (e.g., `UserFactory`, `ItemFactory`).
    *   These factories should be able to generate realistic, randomized data and create objects in the database.
    *   Create a `factories` fixture that provides easy access to all your factories within tests.

4.  **Organize Tests and Use Markers:**
    *   Structure your `tests` directory to mirror your `src` directory (e.g., `tests/api/v1/test_example.py`).
    *   Define custom `pytest` markers in your `pytest.ini` to categorize tests, for example:
        *   `@pytest.mark.slow`: For tests that are slow to run.
        *   `@pytest.mark.integration`: For tests that interact with external services like a database.
        *   `@pytest.mark.e2e`: for full end-to-end tests.
    *   This allows you to selectively run different types of tests (e.g., `pytest -m "not slow"`).

5.  **Enable Parallel Testing:**
    *   Add `pytest-xdist` to the dependencies to enable running tests in parallel.
    *   This can dramatically speed up your test suite as it grows.

**Deliverables:**
*   A `tests/conftest.py` file with the core fixtures.
*   A `tests/factories.py` file with data factories.
*   The `pytest` configuration in `pyproject.toml` or `pytest.ini`.
*   Example tests that demonstrate the use of the fixtures and factories.

**Acceptance Criteria:**
*   The test suite runs successfully with `pytest`.
*   The test database is created, used for the test session, and then torn down correctly.
*   Tests are properly isolated from each other.
*   Test coverage meets or exceeds `{{TARGET}}%`.
*   Tests can be run in parallel using `pytest -n auto`.

**Agent Tips:**
*   Fixtures are the most powerful feature of `pytest`. Use them to abstract away setup and teardown logic, making your tests clean and readable.
*   Your `db_session` fixture is critical. A common pattern is to start a transaction at the beginning of the test and roll it back at the end. This is much faster than dropping and recreating the entire database for each test.
*   Factory Boy is excellent for creating test data. Learn how to use its features like sequences and sub-factories to handle complex data relationships.
*   Write your tests to be as specific as possible. Each test should ideally test one thing. This makes it much easier to debug when a test fails.
