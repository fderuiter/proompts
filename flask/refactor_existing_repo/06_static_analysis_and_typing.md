# 6. Static Analysis and Typing

**Goal:** Integrate static analysis tools into the development workflow to enforce code quality, consistency, and correctness.

**Context:**
*   This task is for projects that lack automated checks for code style, common errors, and type safety.
*   The goal is to catch issues early, before they are merged into the main branch.

**Tasks:**

1.  **Set Up `ruff` and `black`:**
    *   Add `ruff` and `black` to the development dependencies.
    *   Configure `ruff` in `pyproject.toml` to handle linting, import sorting (as a replacement for `isort`), and code formatting. Select a comprehensive set of rules (e.g., `E`, `F`, `W`, `I`, `B`).
    *   Configure `black` for consistent code formatting.
    *   Ensure that the configurations for `ruff`'s formatter and `black` do not conflict. It is recommended to use one or the other for formatting.

2.  **Integrate `mypy` for Type Checking:**
    *   Add `mypy` to the development dependencies.
    *   Create a `mypy.ini` file or configure `mypy` in `pyproject.toml`.
    *   Enable strict mode (`strict = true`) for the main application source directory (e.g., `/src`).
    *   For external libraries that do not have type hints, you may need to add stubs (`*.pyi` files) or install type stubs from `typeshed` (e.g., `pip install types-requests`).
    *   Gradually add type hints to the existing codebase, starting with function signatures.

3.  **Add `bandit` for Security Analysis:**
    *   Add `bandit` to the development dependencies.
    *   Run `bandit` on the codebase to identify common security issues.
    *   Review the findings and either fix the issues or mark them as false positives using comments (`# nosec`).

4.  **Automate with `pre-commit`:**
    *   Set up `pre-commit` to run `ruff`, `black`, `mypy`, and `bandit` automatically before each commit.
    *   This ensures that all code committed to the repository meets the defined quality standards.

**Deliverables:**
*   A diff showing the new development dependencies and the configuration files for `ruff`, `black`, `mypy`, and `pre-commit`.
*   Updated CI configuration to run all static analysis checks on every pull request.
*   A codebase that has been formatted and linted according to the new rules.

**Acceptance Criteria:**
*   `ruff`, `black`, `mypy`, and `bandit` all run without reporting any errors on the entire codebase.
*   The `pre-commit` hooks are installed and working correctly.
*   The CI pipeline includes a "quality" or "linting" job that runs these checks, and this job must pass for a PR to be merged.

**Agent Tips:**
*   When introducing `mypy` to a large, untyped codebase, it can be overwhelming. Start by enabling it for a single module and gradually expand.
*   You can use tools like `monkeytype` to automatically generate type hints for your code based on runtime information.
*   Don't be afraid to use `typing.Any` as a temporary measure while you are adding types. You can come back and refine the types later.
*   The command to run these checks should be clear, e.g., `pytest -q`, `ruff --exit-zero`, `mypy --strict`. You should ensure these commands pass.
