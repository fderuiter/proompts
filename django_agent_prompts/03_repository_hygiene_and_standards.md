# Agent Prompt: Implement Repository Hygiene and Standards

## 1. Objective

To establish and enforce a consistent set of standards and automation for a repository, improving contributor experience, code quality, and maintainability.

## 2. User-Provided Parameters

-   **Branching Strategy:** `{{trunk-based | gitflow}}`
-   **Automated Versioning Tool:** `{{semantic-release | bump2version}}`
-   **Automated Dependency Updates:** `{{Renovate | Dependabot}}`

## 3. Agent Execution Plan

### Phase 1: Contributor Guidelines and Templates

1.  **Create Code Ownership File:**
    -   Create a `.github/CODEOWNERS` file. Add initial entries, assigning ownership of critical paths (e.g., `config/`) to a default team or user.

2.  **Create Issue and PR Templates:**
    -   Create `.github/ISSUE_TEMPLATE/bug_report.md` and `.github/ISSUE_TEMPLATE/feature_request.md`.
    -   Create a `.github/pull_request_template.md` that includes a checklist for authors (e.g., "Tests added," "Docs updated," "CHANGELOG entry included").

3.  **Document Branching and Commit Strategy:**
    -   Create a `CONTRIBUTING.md` file.
    -   Document the chosen **Branching Strategy** (`{{trunk-based | gitflow}}`).
    -   Add a section on **Conventional Commits**, explaining the `fix:`, `feat:`, `chore:`, etc., prefixes. Provide examples.

### Phase 2: Automation and Enforcement

1.  **Configure Pre-Commit Hooks:**
    -   Create/update `.pre-commit-config.yaml`.
    -   Add the following essential hooks:
        -   `pre-commit-hooks`: `trailing-whitespace`, `end-of-file-fixer`, `check-yaml`, `check-added-large-files`
        -   `psf/black`
        -   `PyCQA/isort`
        -   `charliermarsh/ruff`
        -   `pre-commit/mirrors-mypy`

2.  **Create a `Makefile`:**
    -   Create a `Makefile` in the repository root.
    -   Add common developer commands:
        -   `setup`: Install dependencies.
        -   `run`: Start the development server.
        -   `test`: Run the test suite.
        -   `lint`: Run `ruff` and `black --check`.
        -   `type`: Run `mypy`.
        -   `fmt`: Apply `ruff --fix`, `black`, and `isort`.

3.  **Set up Automated Dependency Updates:**
    -   **If `Renovate`:** Add a `renovate.json` configuration file to the repository root.
    -   **If `Dependabot`:** Create a `.github/dependabot.yml` configuration file.
    -   Configure it to check for updates to `pyproject.toml` or `requirements.txt` on a weekly schedule.

4.  **Set up Automated Versioning:**
    -   **If `semantic-release`:** Add a `.releaserc.json` configuration and a GitHub Actions workflow to trigger on pushes to the main branch.
    -   **If `bump2version`:** Create a `.bumpversion.cfg` file. The CI should include a manual or automated step to call this.

### Phase 3: CI/CD Enforcement

1.  **Update CI Pipeline:**
    -   Modify `.github/workflows/ci.yml`.
    -   Ensure the CI pipeline runs the `lint`, `type`, and `test` jobs on every pull request.
    -   Configure the main branch's protection rules (via user instruction or API) to require these checks to pass before merging.

2.  **Add a `semantic-release` Job (if applicable):**
    -   Add a job to the CI pipeline that runs *only* on merges to the main branch.
    -   This job should execute `semantic-release`, which will automatically create a new version tag, generate release notes, and publish a GitHub Release.

## 4. Final Verification Criteria

1.  **File Existence:**
    -   Verify that the following files exist:
        -   `.github/CODEOWNERS`
        -   `.github/pull_request_template.md`
        -   `.github/ISSUE_TEMPLATE/bug_report.md`
        -   `.github/ISSUE_TEMPLATE/feature_request.md`
        -   `CONTRIBUTING.md`
        -   `.pre-commit-config.yaml`
        -   `Makefile`
        -   `renovate.json` or `.github/dependabot.yml`
        -   Configuration for `semantic-release` or `bump2version`.

2.  **CI Behavior:**
    -   (Conceptual) Confirm the CI configuration file (`.github/workflows/ci.yml`) contains jobs that block PR merges on linting, type, or test failures.
    -   (Conceptual) Confirm the CI has a job configured to handle automated versioning upon merging to the main branch.

3.  **Pre-commit Installation:**
    -   Run `pre-commit install` and `pre-commit run --all-files`. Verify that it completes successfully and that files are modified according to the rules.
