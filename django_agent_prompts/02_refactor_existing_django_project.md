# Agent Prompt: Refactor an Existing Django Repository for Scalability

## 1. Objective

To systematically refactor an existing Django repository to improve its structure, maintainability, testability, and overall scalability. The goal is to evolve the codebase towards a modern, modular architecture without disrupting functionality.

## 2. User-Provided Parameters

-   **Repository Path:** `{{repo_url_or_path}}` (Local path where the agent can access the code)
-   **Target Test Coverage:** `{{target_coverage}}` (e.g., 85%)

## 3. Agent Execution Plan

*Agent Note: This process should be executed in small, verifiable steps. Ideally, each phase should result in a distinct, reviewable set of changes.*

### Phase 1: Audit and Planning

1.  **Initial Codebase Audit:**
    -   Scan the entire directory structure. Identify the current layout (e.g., monolithic, apps-based).
    -   Analyze `settings.py`: Is it monolithic? How are secrets handled?
    -   Analyze `requirements.txt` / `pyproject.toml`: Are dependencies pinned? Are there outdated or conflicting packages? Run `python -m pip check`.
    -   Analyze `urls.py`: Is it a single large file or distributed?
    -   Analyze tests: What framework is used? What is the current test coverage? (`pytest --cov` or `coverage run`).
    -   Identify "god" models, fat views, and large utility modules.

2.  **Produce Audit Report:**
    -   Create a short markdown report (`REFACTOR_AUDIT.md`) summarizing the findings.
    -   List key risks (e.g., lack of tests, tightly coupled modules, poor secret management).
    -   Propose a high-level refactoring strategy based on the findings.
    -   **Request user approval before proceeding with changes.**

### Phase 2: Foundational Improvements (Tooling & Structure)

1.  **Introduce Modern Tooling (if absent):**
    -   Add and configure `pyproject.toml` for `black`, `isort`, `ruff`, and `mypy`.
    -   Set up `pre-commit` and install hooks. Apply formatting to the entire codebase in a single, isolated commit.
    -   Add `pytest`, `pytest-django`, and `pytest-cov`. Configure `pytest.ini`.

2.  **Split Settings:**
    -   Refactor the monolithic `settings.py` into `config/settings/{base,dev,test,prod}.py`.
    -   Introduce `django-environ` or `pydantic-settings` to load settings from environment variables.
    -   Replace all hardcoded secrets and configurations with `env("...")` calls.
    -   Create `.env.example`.

3.  **Restructure Project Layout:**
    -   Create an `apps/` directory if one doesn't exist.
    -   Move existing Django apps into the `apps/` directory.
    -   Adjust `sys.path` or `PYTHONPATH` and fix all resulting import errors.
    -   Split a large, central `urls.py` into per-app `urls.py` files, included from a root `config/urls.py`.

### Phase 3: Code Architecture Refactoring

1.  **Introduce Service and Repository Layers:**
    -   Identify business logic currently residing in views or models.
    -   Create `services.py` or `services/` directories within domain-specific apps.
    -   Move complex business logic into service functions/classes. Views should now call services.
    -   Identify direct database access (`.objects.filter(...)`) in views or services.
    -   Create `repositories.py` to encapsulate queryset logic. Services should call repositories, not `models.objects` directly. This centralizes data access patterns.

2.  **Decouple Serializers (for DRF):**
    -   Ensure serializers are used for data validation and representation only.
    -   Move any business logic out of `validate()` or `save()` methods and into services.

3.  **Refactor Utility Code:**
    -   Audit `utils.py` or `helpers.py` files.
    -   Group functions by domain and move them into the relevant app.
    -   Delete unused utility functions.

4.  **Introduce Type Hints:**
    -   Start with service layer and repository function signatures.
    -   Configure `mypy.ini` or `pyproject.toml` with per-module `mypy` settings to allow for gradual rollout (e.g., disable `disallow_untyped_defs` globally but enable it for new/refactored modules).

### Phase 4: CI, Containerization, and Documentation

1.  **Add/Improve CI Pipeline:**
    -   Create a `.github/workflows/ci.yml` file.
    -   Add jobs for linting, type-checking (`mypy`), and running tests with coverage checks.
    -   Fail the build if coverage drops or falls below the `{{target_coverage}}` threshold.

2.  **Add/Improve Dev Environment:**
    -   If not present, create a `Dockerfile` and `docker-compose.yml` for a consistent, one-command local setup.

3.  **Document the New Architecture:**
    -   Create an `ARCHITECTURE.md` file.
    -   Include "before" and "after" diagrams or descriptions of the project structure.
    -   Document the new layers (views, services, repositories) and their responsibilities.

4.  **Create Migration Plan:**
    -   For a live system, document any necessary data migrations or deployment steps that require zero-downtime considerations.

## 4. Final Verification Criteria

1.  **Tests and Coverage:**
    -   All existing and new tests must pass.
    -   Execute `make test` (or equivalent) and verify code coverage is `≥{{target_coverage}}%`.

2.  **Code Health:**
    -   The codebase must be free of linting errors (`ruff check --fix .`).
    -   `mypy .` should pass on all type-checked modules.
    -   Run `python -m pip check` to ensure no broken dependencies.

3.  **Circular Imports:**
    -   The project must start without any circular import errors. A simple check is to run the dev server (`manage.py runserver`) and `manage.py shell`.

4.  **Performance:**
    -   (Optional, if measurable) The application startup time should not have regressed by more than 10%.

5.  **Deliverables Check:**
    -   Confirm that `REFACTOR_AUDIT.md` and `ARCHITECTURE.md` have been created and populated.
    -   Confirm that CI and Docker files exist and are correctly configured.
