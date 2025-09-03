# 4. Dependency Hygiene

**Goal:** Achieve clean, reproducible, and secure dependency management for the project.

**Context:**
*   This task addresses issues with `requirements.txt` files that are often unpinned, lack a hash, or mix production and development dependencies.
*   The choice of tool is between `poetry` and `pip-tools`. The agent should use the one specified in `{{poetry|pip-tools}}`.

**Tasks:**

1.  **Switch to a Modern Dependency Management Tool:**
    *   **If `poetry`:**
        *   Initialize a `pyproject.toml` file using `poetry init`.
        *   Add all production dependencies to the `[tool.poetry.dependencies]` section.
        *   Add all development and testing dependencies to the `[tool.poetry.group.dev.dependencies]` section.
        *   Run `poetry lock` to generate a `poetry.lock` file.
    *   **If `pip-tools`:**
        *   Create `requirements/main.in` for production dependencies and `requirements/dev.in` for development/testing dependencies. `dev.in` should include `-r main.in`.
        *   Use `pip-compile` to generate `requirements/main.txt` and `requirements/dev.txt` lock files with hashes (`--generate-hashes`).

2.  **Pin Dependencies:**
    *   Ensure all direct and transitive dependencies are pinned to specific versions in the generated lock file (`poetry.lock` or `*.txt`).
    *   This is crucial for ensuring reproducible builds.

3.  **Group Dependencies:**
    *   Separate production dependencies from development, testing, and linting dependencies.
    *   This allows for smaller production artifacts and faster CI builds.

4.  **Security and Maintenance:**
    *   Integrate a dependency vulnerability scanner like `safety` or `pip-audit` into the CI pipeline.
    *   Run a tool like `pipdeptree` or `poetry show --tree` to identify and remove any unused dependencies.

**Deliverables:**
*   A diff showing the removal of the old dependency files (e.g., `requirements.txt`) and the introduction of the new ones (`pyproject.toml`, `poetry.lock`, or `requirements/*.in`, `requirements/*.txt`).
*   Updated CI configuration to use the new dependency management tool for installation and to run the vulnerability scanner.
*   A section in the `README.md` or `CONTRIBUTING.md` explaining how to install dependencies for development.

**Acceptance Criteria:**
*   A fresh clone of the repository can install all necessary dependencies using a single command (e.g., `poetry install` or `pip install -r requirements/dev.txt`).
*   The application boots and all tests pass with the newly resolved dependencies.
*   The CI pipeline successfully installs dependencies and runs the security audit without errors.
*   The lock file is committed to the repository.

**Agent Tips:**
*   Before you start, make a backup of the existing `requirements.txt` file.
*   Use `pip freeze` to get a list of the currently installed packages and their versions. This can be a starting point for your `pyproject.toml` or `.in` files.
*   Be careful to distinguish between production and development dependencies. `pytest`, `black`, `ruff`, etc., are almost always development dependencies.
*   After switching, you might find some dependency conflicts. You will need to resolve these by adjusting the version constraints in your `pyproject.toml` or `.in` files.
