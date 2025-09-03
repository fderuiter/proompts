# 13. CI/CD and Repository Hygiene

**Objective:**
Implement a fast, reliable Continuous Integration (CI) pipeline to automate quality checks. Improve repository hygiene by enforcing branch protection rules and clear ownership.

**Context:**
- **CI Provider:** `{{github_actions|gitlab|circle}}`
- **CI Configuration File:** `.github/workflows/ci.yml` (or equivalent)
- **Deployment Target:** `{{fly.io|heroku|ecs|k8s|none}}`

**Agent Instructions:**
-   The CI pipeline should be fast; use caching for dependencies wherever possible.
-   The pipeline should run a sequence of jobs that provide comprehensive feedback on every pull request.
-   Branch protection rules should be used to prevent merging code that fails quality checks.

**Tasks:**

1.  **Create the CI Pipeline:**
    -   Create the CI configuration file (e.g., `.github/workflows/ci.yml`).
    -   Define a sequence of jobs that run on every pull request:
        1.  **Lint:** Run `ruff` and `black`.
        2.  **Typecheck:** Run `mypy`.
        3.  **Test:** Run `pytest`, including coverage generation.
        4.  **Vuln Scan:** Run `pip-audit` to check for dependency vulnerabilities.
        5.  **Build:** Build the Docker image to ensure it builds correctly.

2.  **Optimize CI Performance:**
    -   **Cache Dependencies:** Configure the CI provider's caching mechanism to store and reuse the Python virtual environment (e.g., `actions/setup-python` with caching for `pip` or `poetry`).
    -   **Matrix Builds:** (Optional) If supporting multiple Python versions, use a matrix strategy to run the jobs across all supported versions.

3.  **Integrate Code Coverage:**
    -   In the `Test` job, after running `pytest --cov`, upload the coverage report to a service like `Codecov` or `Coveralls`.
    -   Add a badge for the coverage status to the `README.md`.

4.  **Configure Branch Protection (GitHub/GitLab):**
    -   In the repository settings, protect the `main` branch.
    -   Require that all CI jobs (lint, test, etc.) must pass before a pull request can be merged.
    -   Require that branches are up-to-date before merging.
    -   Require approvals from code owners (see next step).

5.  **Improve Repository Hygiene:**
    -   **`CODEOWNERS`:** Create a `CODEOWNERS` file (usually in the `.github/` directory) to define which teams or individuals own different parts of the codebase. This automates reviewer requests.
    -   **Badges:** Add badges to the `README.md` for the CI status, code coverage, and other relevant metrics.

6.  **(Optional) Set Up Continuous Deployment (CD):**
    -   Create a separate workflow that triggers on merges to the `main` branch.
    -   This workflow should be responsible for:
        1.  Building and tagging the production Docker image.
        2.  Pushing the image to a container registry (e.g., Docker Hub, ECR, GCR).
        3.  Deploying the new image to the specified target (`fly.io`, etc.).
        4.  Running database migrations as part of the deployment process.

**Deliverables:**
-   The CI pipeline configuration file (`.github/workflows/ci.yml`).
-   An updated `README.md` with CI status and coverage badges.
-   A new `CODEOWNERS` file.
-   (Optional) The CD pipeline configuration file.
-   A document or screenshot showing the branch protection rules.

**Acceptance Criteria:**
-   A new pull request automatically triggers the CI pipeline.
-   If any CI job (lint, test, etc.) fails, the pull request is blocked from merging.
-   Code coverage reports are successfully uploaded and visible.
-   The `CODEOWNERS` file correctly assigns reviewers to new pull requests.
-   (If CD is implemented) A merged pull request automatically triggers a successful deployment to the staging/production environment.
