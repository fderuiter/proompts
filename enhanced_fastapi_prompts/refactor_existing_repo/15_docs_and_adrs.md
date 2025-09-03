# 15. Documentation & Architectural Decision Records (ADRs)

**Objective:**
Make the repository self-documenting and easy for new developers to onboard. This involves improving key documentation files and introducing a lightweight process for recording significant architectural decisions.

**Context:**
- **Key Documentation Files:** `README.md`, `CONTRIBUTING.md`
- **Template Files:** `.github/PULL_REQUEST_TEMPLATE.md`
- **ADR Directory:** `docs/adr/`

**Agent Instructions:**
-   The `README.md` should be the front door to the project, providing all essential information to get started.
-   ADRs should be simple, focused, and capture the "why" behind important technical choices.

**Tasks:**

1.  **Enhance the `README.md`:**
    -   Ensure the README includes:
        -   A clear, concise project description.
        -   Badges for CI status, code coverage, etc.
        -   **Prerequisites:** What tools need to be installed locally (e.g., Docker, `make`).
        -   **Quickstart:** A single set of commands to get the local development environment running (e.g., `git clone ...`, `cd ...`, `make up`).
        -   **Running Tests:** How to run the test suite (e.g., `make test`).
        -   A brief overview of the project architecture.

2.  **Create a `CONTRIBUTING.md`:**
    -   Create a `CONTRIBUTING.md` file.
    -   Explain the development workflow:
        -   How to create a branch.
        -   How to run linters and pre-commit hooks.
        -   The process for submitting a pull request.
        -   Code style guidelines (or link to them).

3.  **Create a Pull Request Template:**
    -   Create a `.github/PULL_REQUEST_TEMPLATE.md` file.
    -   The template should prompt the author to provide:
        -   A clear description of the change.
        -   A link to the relevant issue (if any).
        -   A checklist for self-review (e.g., "I have added tests," "I have updated documentation").
        -   Instructions for the reviewer on how to test the changes.

4.  **Introduce Architectural Decision Records (ADRs):**
    -   Create a directory `docs/adr/`.
    -   Create `0000-use-adr-process.md` to explain what ADRs are and how to use them.
    -   Create two example ADRs for decisions made during this refactoring process. Good candidates are:
        -   `0001-adopt-poetry-for-dependency-management.md`
        -   `0002-implement-repository-pattern-for-data-access.md`
    -   Each ADR should have a simple structure:
        -   **Title:** A short, descriptive title.
        -   **Status:** Proposed, Accepted, Deprecated.
        -   **Context:** What is the problem or decision to be made?
        -   **Decision:** What is the chosen solution?
        -   **Consequences:** What are the positive and negative results of this decision?

**Deliverables:**
-   An updated `README.md` file.
-   A new `CONTRIBUTING.md` file.
-   A new `.github/PULL_REQUEST_TEMPLATE.md` file.
-   The `docs/adr/` directory containing the template and at least two example ADRs.

**Acceptance Criteria:**
-   The `README.md` provides a clear, actionable quickstart guide.
-   A new developer, given only the URL to the repository, can successfully get the application running locally in under an hour by following the documentation.
-   When a new pull request is opened, the template is automatically populated in the description field.
-   The example ADRs clearly document the context, decision, and consequences of a past architectural choice.
