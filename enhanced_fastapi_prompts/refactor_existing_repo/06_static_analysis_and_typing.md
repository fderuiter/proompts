# 6. Static Analysis & Typing

**Objective:**
Integrate a suite of static analysis tools to automatically enforce code quality, style, and type safety. This will serve as a quality gate, improving code consistency and reducing bugs.

**Context:**
- **Configuration File:** `pyproject.toml`
- **CI/Local Hook Tool:** `.pre-commit-config.yaml`

**Agent Instructions:**
-   Configure all tools in `pyproject.toml` to have a single source of truth for configuration.
-   Set up `pre-commit` to run these checks automatically before each commit, providing fast feedback to developers.
-   Aim for strict but pragmatic configurations that the team can adhere to.

**Tasks:**

1.  **Install Tooling:**
    -   Add `ruff`, `black`, `mypy`, and `bandit` to the development dependencies.
    -   Also add `pre-commit` for local git hooks.

2.  **Configure `ruff`:**
    -   In `pyproject.toml`, add a `[tool.ruff]` section.
    -   Set the `line-length` to a reasonable value (e.g., 88, to match `black`).
    -   Enable a comprehensive set of rules. A good starting point is `select = ["E", "F", "W", "I", "N", "UP", "B", "A", "C4", "T20", "PYI"]`.
    -   Configure the integrated `isort` tool within `ruff` via `[tool.ruff.lint.isort]`.

3.  **Configure `black`:**
    -   In `pyproject.toml`, add a `[tool.black]` section.
    -   Set the `line-length` to match `ruff`.

4.  **Configure `mypy` for Strict Typing:**
    -   In `pyproject.toml`, add a `[tool.mypy]` section.
    -   Start with a basic setup and incrementally increase strictness.
        -   `warn_return_any = true`
        -   `warn_unused_configs = true`
    -   For a stricter setup, add:
        -   `disallow_untyped_defs = true`
        -   `disallow_any_unimported = true`
        -   `no_implicit_optional = true`
    -   Enable plugins for SQLAlchemy and Pydantic to improve their type inference:
        -   `plugins = ["sqlalchemy.ext.mypy.plugin", "pydantic.mypy"]`

5.  **Configure `bandit` for Security Scanning:**
    -   In `pyproject.toml`, add a `[tool.bandit]` section.
    -   Define test paths to exclude (e.g., `skips = ["B101"]`).
    -   Specify the target directory: `targets = ["src"]`.

6.  **Set Up `pre-commit` Hooks:**
    -   Create a `.pre-commit-config.yaml` file in the root directory.
    -   Add hooks for `ruff`, `black`, `mypy`, and `bandit`.
    -   Use the official hooks where possible (e.g., `repo: https://github.com/psf/black`).
    -   Run `pre-commit install` to activate the hooks.

**Deliverables:**
-   An updated `pyproject.toml` containing configurations for `ruff`, `black`, `mypy`, and `bandit`.
-   A new `.pre-commit-config.yaml` file.
-   Git diffs showing code changes made after running the formatters (`ruff --fix`, `black`).

**Acceptance Criteria:**
-   `pre-commit run --all-files` passes without errors.
-   `mypy .` runs and reports no type errors.
-   The CI pipeline is updated to run these checks, and it passes.
-   The `README.md` or `CONTRIBUTING.md` is updated to instruct developers to install and use the pre-commit hooks.
