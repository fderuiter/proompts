# 13. Docs and ADRs

**Goal:** Establish clear, comprehensive documentation from the start to create a self-explaining repository.

**Context:**
*   Good documentation is not a "nice-to-have"; it's a critical part of a healthy project. It lowers the barrier to entry for new contributors and preserves institutional knowledge.
*   This task focuses on creating the essential documentation files and establishing a process for recording architectural decisions.

**Tasks:**

1.  **Create Essential Documentation Files:**
    *   **`README.md`:** Create a high-quality `README`. It must include:
        *   A clear, one-sentence description of the project.
        *   CI and coverage badges.
        *   A "Quick Start" section with the exact commands needed to get the local development environment running (`make setup`, `make up`).
        *   An overview of the key `make` commands (`test`, `lint`, etc.).
        *   A brief summary of the project's architecture and tech stack.
    *   **`CONTRIBUTING.md`:** Create a file that explains how to contribute to the project. It should cover:
        *   The branching strategy (e.g., "create a feature branch from `main`").
        *   The pull request process.
        *   Coding style guidelines (e.g., "we use `black` and `ruff`").
    *   **`PULL_REQUEST_TEMPLATE.md`:** In `.github/`, create a template to guide contributors in creating well-formed pull requests. It should include sections for a description of the change, testing instructions, and a checklist.
    *   **`CODEOWNERS`:** In `.github/`, create a `CODEOWNERS` file to define default reviewers for different parts of the codebase.

2.  **Introduce Architecture Decision Records (ADRs):**
    *   Create a `docs/adr` directory.
    *   Add a template file, `000-template.md`, for new ADRs. This template should be simple, with sections for `Status`, `Context`, `Decision`, and `Consequences`.
    *   Write the first two ADRs for the project, documenting the initial key decisions:
        *   `001-use-flask-for-web-framework.md`
        *   `002-use-postgresql-for-database.md`

**Deliverables:**
*   A comprehensive `README.md`.
*   A `CONTRIBUTING.md` file.
*   A `.github/PULL_REQUEST_TEMPLATE.md` file.
*   A `.github/CODEOWNERS` file.
*   The `docs/adr` directory containing the template and the first two ADRs.

**Acceptance Criteria:**
*   A new developer can onboard to the project in under an hour, using only the documentation provided in the repository.
*   The `README.md` provides a clear and complete guide to setting up and running the project locally.
*   The ADRs clearly articulate the project's foundational architectural decisions.
*   The pull request template is automatically applied to new pull requests.

**Agent Tips:**
*   Write your documentation for a new team member who is intelligent but has zero context on this project. Avoid jargon where possible.
*   Keep documentation close to the code it describes. The best documentation is often in the form of well-written, self-explanatory code and tests.
*   ADRs should be lightweight and easy to write. Their goal is to quickly capture the "why" behind a decision, not to be a comprehensive design document.
*   Automate what you can. Use badges in the `README` that update automatically. Use templates to enforce consistency.
