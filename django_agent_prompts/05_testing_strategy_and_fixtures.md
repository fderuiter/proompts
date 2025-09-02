# Agent Prompt: Implement a Modern Testing Strategy

## 1. Objective

To establish a fast, reliable, and maintainable testing strategy for a Django project using modern tools and patterns like `pytest`, `factory_boy`, and snapshot testing.

## 2. User-Provided Parameters

-   **Target Test Duration (minutes):** `{{X}}` (e.g., `2`)
-   **Target Coverage:** `{{target_coverage}}` (e.g., `90%`)

## 3. Agent Execution Plan

### Phase 1: Tooling Setup and Configuration

1.  **Install Testing Dependencies:**
    -   Ensure the following packages are in the dev/test dependency group:
        -   `pytest`
        -   `pytest-django`
        -   `pytest-cov` (for coverage)
        -   `factory_boy` (for fixtures)
        -   `freezegun` (for time-based tests)
        -   `faker` (for generating realistic fake data)
        -   `pytest-xdist` (for parallel testing)
        -   `pytest-snapshot` (for snapshot testing)

2.  **Configure `pytest.ini`:**
    -   Create or update the `pytest.ini` file in the project root.
    -   Set the `DJANGO_SETTINGS_MODULE`.
    -   Define custom markers for categorizing tests:
        ```ini
        [pytest]
        DJANGO_SETTINGS_MODULE = config.settings.test
        python_files = tests.py test_*.py *_tests.py

        markers =
            unit: marks tests as unit tests (fast, no external services).
            integration: marks tests as integration tests (may require db, cache).
            slow: marks tests as slow to run.
        ```
    -   Configure `pytest-cov` to generate reports and fail if coverage is below the target.
        ```ini
        [pytest]
        ...
        addopts = -ra -q --cov=apps/ --cov-report=term-missing --cov-fail-under={{target_coverage}}
        ```

### Phase 2: Fixture and Factory Implementation

1.  **Set up `factory_boy`:**
    -   For each core model (e.g., `User`, `Product`), create a corresponding factory in a `factories.py` file within the app.
        ```python
        # in apps/users/factories.py
        import factory
        from .models import User
        from faker import Faker

        fake = Faker()

        class UserFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = User

            email = factory.LazyAttribute(lambda _: fake.email())
            first_name = factory.LazyAttribute(lambda _: fake.first_name())
            # Add other fields...
        ```

2.  **Seed Faker for Deterministic Randomness:**
    -   In your top-level `conftest.py`, create a fixture that seeds the `Faker` instance. This makes "random" data predictable between test runs.
        ```python
        # in tests/conftest.py or root conftest.py
        import pytest
        from faker import Faker

        @pytest.fixture(scope='session', autouse=True)
        def faker_seed():
            return Faker.seed(0) # Seed with a constant
        ```

### Phase 3: Writing and Organizing Tests

1.  **Structure Test Files:**
    -   Organize tests by the module they are testing, e.g., `apps/users/tests/test_models.py`, `apps/users/tests/test_services.py`.

2.  **Implement Unit Tests:**
    -   Mark tests that do not require database or cache access with `@pytest.mark.unit`.
    -   These should test pure functions (e.g., in services or utils) and model methods in isolation.
    -   Use `mocker` (built into `pytest`) to patch out external dependencies.

3.  **Implement Integration Tests:**
    -   Mark tests that require the database or other services with `@pytest.mark.integration`.
    -   Use `UserFactory()` instead of manual object creation.
    -   Use `pytest-django`'s `db` and `django_db_setup` fixtures.
    -   Enable database reuse in `pytest.ini` to speed up subsequent runs:
        ```ini
        [pytest]
        ...
        addopts = ... --reuse-db
        ```

4.  **Implement Snapshot Tests for APIs:**
    -   For API endpoints (especially list/detail views), use `pytest-snapshot` to verify the structure of the JSON response. This makes it easy to detect unintended changes to the API contract.
        ```python
        # in apps/api/tests/test_endpoints.py
        def test_user_list_api(api_client, snapshot):
            # ... create users with factory ...
            response = api_client.get("/api/v1/users/")
            assert response.status_code == 200
            snapshot.assert_match(response.json())
        ```

5.  **Isolate Slow Tests:**
    -   Any test known to be particularly slow (e.g., complex data processing, PDF generation) should be marked with `@pytest.mark.slow`.
    -   Configure the CI to run slow tests less frequently, or to run them in a separate, non-blocking job.

## 4. Final Verification Criteria

1.  **Configuration Files:**
    -   Verify that `pytest.ini` exists and contains the required configurations (`DJANGO_SETTINGS_MODULE`, markers, `addopts` with coverage check).

2.  **Test Execution and Speed:**
    -   Run the full test suite with `pytest`.
    -   The run must complete successfully.
    -   Time the execution. It should complete in under `{{X}}` minutes.
    -   Run tests in parallel with `pytest -n auto`. Verify it completes successfully and is faster.

3.  **Coverage Report:**
    -   Check the output of the test run.
    -   Confirm that the final coverage percentage meets or exceeds the `{{target_coverage}}%` target.

4.  **Test Filtering:**
    -   Run `pytest -m "unit"` and verify that only unit tests are executed.
    -   Run `pytest -m "not slow"` and verify that slow tests are skipped.

5.  **Factory and Fixture Usage:**
    -   Review newly created tests to confirm they use `factory_boy` factories instead of `models.objects.create()`.
