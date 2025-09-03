# 11. CI/CD

**Goal:** Implement a fast and effective Continuous Integration (CI) pipeline that runs on the very first pull request.

**Context:**
*   CI is a cornerstone of modern software development. Setting it up early establishes a culture of quality and automation.
*   **CI Provider:** This will be set up for GitHub Actions, but can be adapted for others.
*   **Deploy Target:** `{{fly.io|heroku|ecs|k8s|none}}`

**Tasks:**

1.  **Create the CI Workflow:**
    *   In `.github/workflows/ci.yml`, create a new GitHub Actions workflow.
    *   Trigger the workflow on `pull_request` events targeting the `main` branch.

2.  **Define CI Jobs:**
    *   Create a sequence of jobs to validate the code. These jobs can run in parallel where possible.
        1.  **Linting & Formatting:** A job that runs `ruff` and `black --check`.
        2.  **Type Checking:** A job that runs `mypy`.
        3.  **Testing:** A job that runs the `pytest` suite. This job will likely need to spin up service containers (like a database) to run integration tests.
        4.  **Building:** A job that builds the production Docker image.
        5.  **Security Scan:** A job that runs `safety` or `pip-audit` to check for vulnerable dependencies.

3.  **Optimize the Pipeline:**
    *   **Cache Dependencies:** Use `actions/cache` to cache the `pip` or `poetry` dependency cache between runs. This dramatically speeds up the "install dependencies" step.
    *   **Run Services:** For the `test` job, use the "services" feature of GitHub Actions to start a database container (e.g., `services: postgres: image: postgres:15`).

4.  **Enforce Quality Gates:**
    *   In the repository settings, configure branch protection for the `main` branch.
    *   Require all the jobs in the `ci.yml` workflow to pass before a pull request can be merged.
    *   (Optional) Configure coverage reporting using a tool like `codecov-action` to upload coverage reports.

5.  **(Optional) Create a Deployment Workflow:**
    *   If a deploy target is specified, create a separate `deploy.yml` workflow.
    *   Trigger this workflow on `push` events to the `main` branch (i.e., after a PR is merged).
    *   This workflow will build the Docker image, push it to a container registry (like Docker Hub or GitHub Container Registry), and then run the deploy command for the specified platform.

**Deliverables:**
*   The `.github/workflows/ci.yml` file.
*   (Optional) The `.github/workflows/deploy.yml` file.
*   Branch protection rules configured for the `main` branch.
*   Badges for the CI status and coverage in the `README.md`.

**Acceptance Criteria:**
*   The CI pipeline is triggered when a pull request is opened against `main`.
*   The pipeline runs all checks (lint, types, tests, build, scan) successfully.
*   A pull request cannot be merged if any CI check fails.
*   (Optional) A merge to `main` successfully triggers a deployment to the target environment.
*   The `README.md` file shows a "passing" badge for the CI pipeline.

**Agent Tips:**
*   Start with a simple CI file and build it up. Get one job working first (e.g., linting) before adding the others.
*   Use GitHub Actions secrets to store any sensitive information, like a `DOCKER_HUB_TOKEN` or `FLY_API_TOKEN`.
*   Look for pre-made actions on the GitHub Marketplace to simplify your workflows (e.g., `actions/setup-python`, `actions/checkout`).
*   Make sure your tests are configured to connect to the service container running in the CI environment. You'll need to pass the correct hostname and credentials as environment variables.
