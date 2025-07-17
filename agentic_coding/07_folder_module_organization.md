<!-- markdownlint-disable MD029 -->

# Folder & Module Organization

## Enhanced Initial Prompt

> "Given the attached Python codebase, analyze its package and module layout. Identify where feature- or domain-based grouping could improve clarity, point out violations of separation-of-concerns (e.g. separating `views/` vs. `services/` vs. `models/` vs. `utils/`), flag overly deep or circular package hierarchies, and then **produce a detailed, step-by-step refactoring plan** that includes:
>
> - **Pre-refactor checklist**:
>
>    - `pytest --maxfail=1 --disable-warnings -q`
>    - `coverage run -m pytest && coverage report`
>    - `flake8 .` / `pylint myproject/`
>    - Record failures and coverage %.
>
> - **File migration steps**:
>
>    - Use `git mv` for each package/module move.
>    - Update imports (relative vs. absolute) using `sed`, `isort`, or an IDE refactor tool.
>    - Amend paths in `setup.py` / `pyproject.toml` if needed.
>
> - **Post-refactor validation** (run after each logical group of moves):
>
>    - `pytest`
>    - `coverage run && coverage xml`
>    - `flake8` / `pylint`
>    - Smoke test a couple of CLI commands or demo scripts.
>
> - **Rollback guidance**: if any step fails, revert via `git reset --hard HEAD@{1}`, reopen the failing move, and iterate.
>    Provide the exact shell commands and suggest tooling (e.g. `import-linter`, `ruff`) so that each move is immediately followed by a validation step."

---

## Follow-up Prompt 1

> "Drill into your refactoring plan for three sample modules (e.g. `auth`, `orders`, `reports`):
>
> - Show the **before** and **after** directory trees (using `tree -L 2`).
> - List the exact `git mv` commands you’d run.
> - Provide the `sed` (or `rope`/IDE) patterns to rewrite imports (e.g. `from oldpkg.module import X` → `from newpkg.feature.module import X`).
> - Identify which pytest test files touch each module, and show how to update their imports.
> - Give the commands to run just those tests and verify they pass (`pytest tests/test_auth.py`)."

---

## Follow-up Prompt 2

> "Examine cross-module dependencies under the new layout:
>
> - Highlight any cyclic or horizontal imports you discovered (e.g. `models` importing `services` and vice versa).
> - For each cycle, suggest extracting a shared package (`myapp.core`) or defining clear boundaries (interfaces vs. implementations).
> - Show how to configure and run `import-linter` or `flake8-import-order` to enforce the new layering rules.
> - Provide the exact validation commands (e.g. `import-linter check`, `flake8 --select=I`) that confirm no broken or forbidden imports remain."

---

## Follow-up Prompt 3

> "Validate the scalability of your new structure by adding a stub for a future feature `recommendation_engine`:
>
> - Sketch where its package (`myapp/recommendation/`) and modules (`model.py`, `service.py`, `api.py`) would live.
> - Create minimal placeholder code (`class Recommender: pass`) and an empty `__init__.py`.
> - Write one smoke pytest (`tests/test_recommendation_smoke.py`) that imports `Recommender` and asserts no errors.
> - Run the **full** suite:
>
>    ```bash
>    pytest && coverage run -m pytest && flake8 && mypy myapp/
>    ```
>
> - Report that everything passes, and call out any “smells” (e.g. deep nesting, missing `__init__.py`, import ambiguities) that might still crop up as you add real code, with quick mitigation tips."
