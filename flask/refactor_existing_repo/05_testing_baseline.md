# 5. Testing Baseline

**Goal:** Establish a fast, reliable, and comprehensive testing baseline for the application.

**Context:**
*   This task is for projects with low test coverage, no clear testing strategy, or a slow and unreliable test suite.
*   The target coverage and runtime are specified by `{{TARGET}}%` and `{{SECS}}s`.

**Tasks:**

1.  **Introduce Standard Testing Tools:**
    *   Add `pytest`, `pytest-cov`, `pytest-mock`, and `pytest-flask` to the development dependencies.
    *   Configure `pytest` via a `pytest.ini` or `pyproject.toml` file. Set up basic options like `testpaths` and `addopts`.
    *   Set up `pytest-cov` to generate coverage reports in HTML and XML formats. Configure it to fail if coverage drops below a certain threshold.

2.  **Implement Test Data Generation:**
    *   Introduce `factory_boy` and `Faker` for generating realistic test data.
    *   Create factories for your SQLAlchemy models. This will make it much easier to create test data in a consistent and readable way.

3.  **Seed the Test Suite:**
    *   Write a baseline set of tests to cover critical application functionality:
        *   **Health Check:** A simple test to ensure the `/health` or `/` endpoint returns a 200 OK.
        *   **Configuration:** Tests to ensure the app loads the correct configuration for different environments (e.g., `TestingConfig`).
        *   **Error Handlers:** Tests to verify that your custom error handlers for 404, 500, etc., are working correctly.
        *   **CRUD Operations:** At least one test for a simple CRUD lifecycle of a core model (Create, Read, Update, Delete).
        *   **Authentication:** Tests for successful login, failed login, and accessing a protected endpoint with and without authentication.

4.  **Optimize Test Performance:**
    *   Configure `pytest-xdist` to run tests in parallel, which can significantly reduce the total runtime.
    *   Identify and refactor any slow tests. Use markers (`@pytest.mark.slow`) to separate slow integration tests from fast unit tests.

**Deliverables:**
*   A diff showing the new testing dependencies and the new test files.
*   The `pytest` configuration in `pytest.ini` or `pyproject.toml`.
*   A coverage report in HTML format, showing the test coverage for the new tests.
*   Updated CI configuration to run the test suite and upload the coverage report.

**Acceptance Criteria:**
*   The test suite runs to completion without errors.
*   Test coverage is greater than or equal to `{{TARGET}}%`.
*   The total runtime of the test suite is less than or equal to `{{SECS}}` seconds.
*   The tests are reliable and produce consistent results.

**Agent Tips:**
*   When writing tests, use fixtures for setting up and tearing down resources like the app context and database sessions.
*   Use the `client` fixture provided by `pytest-flask` to make requests to your application.
*   Your tests should be independent of each other. Each test should run in a clean environment.
*   Use mocking (`pytest-mock`) to isolate your tests from external services like databases or APIs. This is especially important for unit tests.
*   For example, a curl for a health check test would be: `curl -X GET http://127.0.0.1:5000/health`. The agent should write a test that does the equivalent using the flask test client.
