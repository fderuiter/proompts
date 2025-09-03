# 13. CI/CD and Repo Hygiene

**Goal:** Implement a fast and reliable Continuous Integration (CI) pipeline and establish repository best practices to ensure code quality and guarded merges.

**Context:**
*   **CI Provider:** `{{github_actions|gitlab|circle}}`
*   **Deploy Target:** `{{fly.io|heroku|ecs|k8s|none}}`

**Tasks:**

1.  **Build an Efficient CI Pipeline:**
    *   Create a CI configuration file (e.g., `.github/workflows/ci.yml`).
    *   Define a sequence of jobs that run on every pull request:
        1.  **Lint:** Run `ruff`, `black`, etc.
        2.  **Typecheck:** Run `mypy`.
        3.  **Tests:** Run the `pytest` suite.
        4.  **Build:** Build the Docker image.
        5.  **Vulnerability Scan:** Run `safety` or `pip-audit` on dependencies, and a container scanner (like `trivy`) on the Docker image.
    *   Use caching for dependencies (e.g., `pip` or `poetry` cache) to speed up job execution.
    *   If applicable, use a matrix strategy to run tests against multiple Python versions.

2.  **Enforce Quality Gates:**
    *   Configure the CI provider to upload test coverage reports (e.g., to Codecov or Coveralls).
    *   Set up branch protection rules for the main branch (`main` or `master`).
    *   Require that all CI checks must pass before a pull request can be merged.
    *   Require that pull requests have at least one approval from a code owner.

3.  **Improve Repository Hygiene:**
    *   Create a `CODEOWNERS` file to define which teams or individuals are responsible for different parts of the codebase.
    *   Create a pull request template (`.github/PULL_REQUEST_TEMPLATE.md`) to guide contributors in providing good context for their changes.
    *   Enhance the `README.md` and `CONTRIBUTING.md` files to provide clear instructions for setup, testing, and contributing.

4.  **(Optional) Set Up Continuous Deployment (CD):**
    *   If a deploy target is specified, create a separate CD pipeline.
    *   This pipeline should be triggered only on merges to the main branch.
    *   It should build the production Docker image, push it to a registry (e.g., Docker Hub, ECR, GCR), and then deploy the new version to the specified target.

**Deliverables:**
*   The CI/CD configuration file(s).
*   The `CODEOWNERS` file and pull request template.
*   Updated documentation (`README.md`, `CONTRIBUTING.md`).
*   A document (`branch_protection.md`) that details the branch protection rules that have been configured.

**Acceptance Criteria:**
*   The CI pipeline runs successfully on a clean pull request.
*   A pull request cannot be merged if any of the required checks (linting, testing, etc.) fail.
*   Test coverage reports are successfully uploaded.
*   Branch protection rules are in place and documented.
*   (Optional) A merge to the main branch triggers a successful deployment.

**Agent Tips:**
*   Build your CI pipeline incrementally. Start with a single job (e.g., tests) and then add more jobs one by one.
*   Use secrets management provided by your CI platform to handle sensitive information like API keys or deploy tokens. Do not hardcode them in the CI configuration.
*   When setting up `CODEOWNERS`, be specific. You can assign ownership based on file paths or glob patterns.
*   A good pull request template often includes sections for "What does this PR do?", "How to test it", and a checklist of required items (e.g., "I have added tests", "I have updated the documentation").
