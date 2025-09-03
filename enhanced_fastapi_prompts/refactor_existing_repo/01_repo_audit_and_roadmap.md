# 1. Repository Audit and Refactoring Roadmap

**Objective:**
Conduct a comprehensive audit of the FastAPI repository located at `{{REPO_URL_OR_PATH}}` and produce a detailed, phased refactoring plan. The initial audit should not introduce any behavioral changes to the application.

**Context:**
- **Repository URL/Path:** `{{REPO_URL_OR_PATH}}`
- **Branch:** `{{BRANCH}}`
- **Key Technology Versions:**
  - Python: `{{PYTHON_VERSION}}`
  - FastAPI: `{{FASTAPI_VERSION}}`
  - Pydantic: `{{PYDANTIC_VERSION}}`

**Agent Instructions:**
- Begin by exploring the repository.
- Your primary tools for this phase will be `ls`, `read_file`, and `grep` to explore the codebase.
- You are not to modify any code in this step. Your role is to analyze and report.
- The final deliverables should be well-structured markdown files.

**Tasks:**

1.  **Initial Codebase Scan:**
    -   Use `ls -R` to map the complete directory and file structure.
    -   Identify and read key configuration files (e.g., `pyproject.toml`, `setup.cfg`, `requirements.txt`, `Pipfile`, `.env*`).
    -   Identify and read CI/CD configuration files (e.g., `.github/workflows/*.yml`, `.gitlab-ci.yml`).
    -   Identify and read Docker-related files (e.g., `Dockerfile`, `docker-compose.yml`).
    -   Identify the testing setup (e.g., `tests/` directory, `pytest.ini`, `tox.ini`).

2.  **Create Audit Report (`audit.md`):**
    -   Based on the scan, create a document named `audit.md`.
    -   Structure the audit into the following sections:
        -   **Project Structure & Boundaries:** Analyze the layout. Is it modular? Are there clear boundaries between components (e.g., API, services, repositories)?
        -   **Configuration Management:** How are settings handled? Are they environment-aware? Are secrets managed securely?
        -   **Dependency Management:** What tool is used (`pip`, `poetry`, `pip-tools`)? Are dependencies pinned? Is there a process for auditing dependencies for vulnerabilities?
        -   **Testing Strategy:** What is the test coverage? Are there unit, integration, and end-to-end tests? How are they run?
        -   **Code Quality & Static Analysis:** Are linters (`ruff`, `black`), type checkers (`mypy`), and formatters used? Are they enforced?
        -   **Security:** Are there apparent security vulnerabilities (e.g., hardcoded secrets, missing auth, insecure CORS)?
        -   **Operations & Deployment:** How is the application containerized and deployed? Is the local development experience smooth?
        -   **Observability:** Is there evidence of structured logging, metrics, or tracing?

3.  **Develop Refactoring Plan (`refactor_plan.md`):**
    -   Create a document named `refactor_plan.md`.
    -   Translate the issues identified in `audit.md` into a series of distinct, sequential refactoring phases.
    -   For each phase, define:
        -   **Goal:** A clear objective for the phase (e.g., "Implement 12-Factor Config").
        -   **Tasks:** A high-level list of actions required.
        -   **Estimated Effort:** A rough estimate (e.g., Small, Medium, Large).
        -   **Potential Risk:** What could go wrong during this phase?
        -   **Verification:** How will success be measured?

4.  **Propose Pull Request Strategy (`pr_plan.md`):**
    -   Create a document named `pr_plan.md`.
    -   Outline a series of pull requests that correspond to the phases in the refactoring plan.
    -   For each proposed PR, provide a title and a brief description of its scope. This helps in breaking down the work into manageable chunks.

**Deliverables:**
- `audit.md`: A detailed report on the current state of the repository.
- `refactor_plan.md`: A strategic plan for refactoring the repository in phases.
- `pr_plan.md`: A list of proposed Pull Requests to execute the refactoring plan.

**Acceptance Criteria:**
- All three markdown files (`audit.md`, `refactor_plan.md`, `pr_plan.md`) are created in the root of the project.
- The agent has made no modifications to the application's source code.
- The existing CI pipeline (if any) remains green, confirming no functional changes were introduced.
