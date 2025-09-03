# 11. Continuous Integration on First PR

**Objective:**
Implement a complete Continuous Integration (CI) pipeline that runs on the very first pull request, ensuring that all code is automatically linted, type-checked, tested, and scanned for vulnerabilities before it can be merged.

**Context:**
- **CI Provider:** `{{github_actions|gitlab|circle}}`
- **CI Config File:** `.github/workflows/ci.yml`
- **Optional Deploy Target:** `{{fly.io|heroku|ecs|k8s}}`

**Agent Instructions:**
-   The CI pipeline must be fast and efficient, using caching for dependencies.
-   Set up branch protection rules to make the CI checks mandatory for merging to `main`.
-   The pipeline should provide clear, immediate feedback to the developer on their PR.

**Tasks:**

1.  **Create the CI Workflow File:**
    -   Create `.github/workflows/ci.yml` (or the equivalent for your provider).
    -   Configure the workflow to trigger on `pull_request` events targeting the `main` branch.

2.  **Define CI Jobs:**
    -   Create a sequence of jobs. You can run them in sequence or in parallel where possible.
    -   **`lint` Job:**
        -   Checks out the code.
        -   Sets up Python and caches dependencies.
        -   Runs `ruff check .` and `black --check .`.
    -   **`typecheck` Job:**
        -   Sets up Python and caches dependencies.
        -   Runs `mypy .`.
    -   **`test` Job:**
        -   Sets up Python and caches dependencies.
        -   Starts up required services (like a database) if not using a fully containerized test approach.
        -   Runs `pytest --cov` to execute tests and generate a coverage report.
        -   Uploads the coverage report (`coverage.xml`) to a service like Codecov.
    -   **`vuln-scan` Job:**
        -   Sets up Python and caches dependencies.
        -   Runs `pip-audit` to check for known vulnerabilities.
    -   **`build` Job:**
        -   Checks out the code.
        -   Builds the production Docker image to ensure the `Dockerfile` is valid.

3.  **Implement Dependency Caching:**
    -   Use the CI provider's built-in caching mechanism (e.g., `actions/cache` or the `cache` key in `actions/setup-python`) to cache the `pip` or `poetry` dependency cache. This dramatically speeds up subsequent runs.

4.  **Set Up Branch Protection:**
    -   In your Git provider's settings, protect the `main` branch.
    -   Require that all CI jobs (`lint`, `typecheck`, `test`, `build`, etc.) must pass before merging.
    -   (Recommended) Require that the branch be up-to-date with `main` before merging.

5.  **Add CI Badges to `README.md`:**
    -   Add a CI status badge and a code coverage badge to the top of the `README.md` file.

6.  **(Optional) Add a Continuous Deployment (CD) Workflow:**
    -   Create a separate file, `cd.yml`, that triggers on `push` events to the `main` branch.
    -   This workflow would be responsible for building the Docker image, pushing it to a registry, and deploying to your chosen hosting provider.

**Deliverables:**
-   The `.github/workflows/ci.yml` file.
-   An updated `README.md` with CI and coverage badges.
-   Screenshots of the branch protection rules configured in the repository settings.
-   A successful run of the CI pipeline on the pull request that introduced it.

**Acceptance Criteria:**
-   The CI pipeline is automatically triggered when a pull request is opened against `main`.
-   A pull request with a failing linter, type check, or test is blocked from being merged.
-   The pipeline completes in a reasonable amount of time (e.g., under 5 minutes) thanks to caching.
-   Code coverage reports are successfully uploaded and displayed in the coverage service and on the PR.
-   The `main` branch is protected, and merges are gated by the CI pipeline's success.
