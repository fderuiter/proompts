# 4. Dependency Hygiene

**Objective:**
Establish a robust and reproducible dependency management system. This involves migrating to a modern packaging tool, pinning all dependencies, and integrating security audits into the workflow.

**Context:**
- **Chosen Package Manager:** `{{poetry|pip-tools}}`
- **Project Root:** `{{PROJECT_ROOT}}`

**Agent Instructions:**
-   The goal is to have a single command that can create a fully functional virtual environment from a clean clone.
-   Ensure that dependencies are split into logical groups (e.g., main, development, testing).
-   Integrate a tool to check for known vulnerabilities in dependencies.

**Tasks:**

1.  **Choose and Implement a Package Manager:**
    -   **If `poetry`:**
        -   Run `poetry init` to create a `pyproject.toml` if one doesn't exist.
        -   Manually add existing dependencies from `requirements.txt` to `pyproject.toml` under `[tool.poetry.dependencies]` and `[tool.poetry.group.dev.dependencies]`.
        -   Run `poetry lock` to create a `poetry.lock` file.
        -   Run `poetry install --all-extras` to verify.
    -   **If `pip-tools`:**
        -   Create `requirements/main.in` and `requirements/dev.in` files.
        -   List direct dependencies in the `.in` files.
        -   Run `pip-compile requirements/main.in` to generate `requirements/main.txt`.
        -   Run `pip-compile requirements/dev.in` to generate `requirements/dev.txt`.
        -   Update installation scripts to use `pip install -r requirements/main.txt -r requirements/dev.txt`.

2.  **Pin Dependencies:**
    -   Ensure that the generated lock file (`poetry.lock` or `*.txt`) contains exact versions for all transitive dependencies. This is the key to reproducible builds.

3.  **Integrate Security Auditing:**
    -   Add a dependency vulnerability scanner to the development dependencies.
        -   For `poetry`, you can use `poetry-check-plugins`.
        -   A universal option is `pip-audit`. Add it to your dev/test dependencies.
    -   Add a script or `Makefile` target (e.g., `make audit`) that runs the scanner against the project's dependencies.
    -   Example command: `pip-audit`.

4.  **Clean Up Old Files:**
    -   Remove the old `requirements.txt` file (if it wasn't replaced by `pip-tools`).
    -   Update the `README.md` and any contribution guides to reflect the new dependency installation process (e.g., `poetry install` or `pip install -r ...`).

**Deliverables:**
-   Git diff showing the removal of old dependency files and the creation of new ones.
-   The new configuration file (`pyproject.toml` or `requirements/*.in`).
-   The new lock file (`poetry.lock` or `requirements/*.txt`).
-   A report of removed/updated dependencies.
-   An updated `README.md` with new setup instructions.

**Acceptance Criteria:**
-   From a fresh clone of the repository, a user can create a working virtual environment with one or two commands.
-   The `make audit` or equivalent command executes successfully and reports the vulnerability status.
-   All application tests pass with the newly installed, pinned dependencies.
