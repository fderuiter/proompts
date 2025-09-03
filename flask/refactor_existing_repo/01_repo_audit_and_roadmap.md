# 1. Repo Audit and Refactoring Roadmap

**Goal:** Audit the existing Flask repository at `{{REPO_URL_OR_PATH}}` and propose a comprehensive, phased refactoring plan.

**Context:**
*   **Repository:** `{{REPO_URL_OR_PATH}}`
*   **Branch:** `{{BRANCH}}`
*   **Python Version:** `{{X}}`
*   **Flask Version:** `{{Y}}`

**Tasks:**

1.  **Comprehensive Codebase Scan:**
    *   **Project Structure:** Analyze the directory layout. Look for monolithic files (`god objects`), lack of modularity, unclear separation of concerns (e.g., business logic mixed with view logic), and inconsistent naming conventions.
    *   **Configuration Management:** Investigate how configuration is handled. Check for hardcoded secrets, environment-specific settings not loaded from the environment, and lack of a unified config object.
    *   **Dependencies:** Review the dependency management (`requirements.txt`, `Pipfile`, `pyproject.toml`). Check for unpinned, outdated, or unused dependencies. Assess the use of a lock file for reproducible builds.
    *   **Testing:** Evaluate the test suite. Assess test coverage, the types of tests present (unit, integration, e2e), the testing frameworks used, and the overall reliability and speed of the tests.
    *   **CI/CD:** Examine the continuous integration and deployment pipeline. Check for its existence, completeness (linting, testing, building), and efficiency.
    *   **Dockerization:** If a `Dockerfile` or `docker-compose.yml` exists, review it for best practices (e.g., multi-stage builds, non-root user, layer caching, `.dockerignore`).

2.  **Issue Categorization and Reporting:**
    *   Create a detailed report (`audit.md`) that lists all identified issues.
    *   Categorize each issue under one of the following headings:
        *   **Structure & Boundaries:** Issues related to project layout, modularity, and separation of concerns.
        *   **Testing:** Gaps in test coverage, slow or flaky tests, lack of a testing strategy.
        *   **Code Quality:** Inconsistent code style, high complexity, lack of type hints, "code smells."
        *   **Security:** Potential vulnerabilities (e.g., outdated dependencies, hardcoded secrets, lack of security headers).
        *   **Operations & DevOps:** Problems with local development setup, CI/CD, containerization, and observability.

3.  **Propose a Phased Refactoring Plan:**
    *   Based on the audit, create a `refactor_plan.md` document.
    *   Break down the refactoring process into logical, incremental phases. Each phase should be deliverable as a single pull request.
    *   For each phase, provide:
        *   A clear goal (e.g., "Implement Application Factory Pattern").
        *   A list of specific tasks.
        *   An estimate of effort and risk (e.g., Low, Medium, High).
        *   Dependencies on other phases.

4.  **Define a Pull Request Strategy:**
    *   Create a `PR_list.md` file.
    *   For each phase in the refactoring plan, propose a clear pull request title and a detailed description.

**Deliverables:**
*   `audit.md`: A detailed report of all findings from the codebase scan, categorized by area.
*   `refactor_plan.md`: A phased plan for refactoring the application, including goals, tasks, effort, and risk for each phase.
*   `PR_list.md`: A list of proposed pull requests, one for each phase of the refactoring plan, with clear titles and descriptions.

**Acceptance Criteria:**
*   The audit report is comprehensive and covers all the areas specified in the tasks.
*   The refactoring plan is actionable, with well-defined, incremental phases.
*   The proposed changes in the plan must not alter the existing application behavior.
*   The CI pipeline (if it exists) must remain green after any preliminary setup or analysis.
*   The agent should not make any code changes to the application itself in this phase, only deliver the requested markdown files.
