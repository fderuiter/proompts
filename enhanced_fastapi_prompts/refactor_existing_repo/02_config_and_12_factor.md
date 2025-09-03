# 2. Centralized, 12-Factor Configuration

**Objective:**
Refactor the application's configuration to follow the 12-Factor App methodology. This involves creating a central, typed configuration object using Pydantic's `BaseSettings` and ensuring a strict separation of configuration from code.

**Context:**
- **Application Source Directory:** `{{SRC_DIR}}` (e.g., `src/`, `app/`)
- **Primary Config File Path:** `{{SRC_DIR}}/app/core/config.py`

**Agent Instructions:**
- Use Pydantic `BaseSettings` to load configuration from environment variables.
- Ensure no secrets (API keys, database passwords, etc.) are hardcoded or checked into version control.
- Create a clear, well-documented example environment file.

**Tasks:**

1.  **Install Pydantic-Settings:**
    -   Add `pydantic-settings` to the project's dependencies (`pyproject.toml` or `requirements.txt`).

2.  **Create/Update `config.py`:**
    -   Navigate to `{{SRC_DIR}}/app/core/`.
    -   Create or modify the `config.py` file.
    -   Define a `Settings` class that inherits from `pydantic_settings.BaseSettings`.
    -   Add typed fields for all required configuration variables (e.g., `DATABASE_URL: str`, `API_SECRET_KEY: str`, `ENVIRONMENT: str = "local"`).
    -   Use `model_config` to set `env_file = ".env"` and `extra = "ignore"`.

3.  **Integrate Settings into Application:**
    -   Create a singleton instance of the `Settings` class (e.g., `settings = Settings()`).
    -   Search the codebase for hardcoded configuration values and replace them with references to the `settings` object (e.g., `settings.DATABASE_URL`).

4.  **Implement Environment-Specific Settings:**
    -   Ensure the configuration logic can differentiate between environments (e.g., `local`, `testing`, `production`). This is often handled by an `ENVIRONMENT` variable read by the `Settings` class.

5.  **Standardize Logging Configuration:**
    -   If a logging configuration exists, refactor it to pull settings (like log level) from the new `settings` object.
    -   If no standardized logging exists, create a basic logging configuration in `{{SRC_DIR}}/app/core/logging.py` that uses the `settings`.

6.  **Create `.env.example`:**
    -   Create a `.env.example` file in the repository root.
    -   This file should list all required environment variables for the application to run.
    -   Use placeholder values for sensitive variables (e.g., `DATABASE_URL="postgresql+asyncpg://user:password@localhost/db"`). Do not include real secrets.
    -   Add comments to explain each variable.

7.  **Update `.gitignore`:**
    -   Ensure that `.env` and any environment-specific files (e.g., `.env.local`, `.env.prod`) are listed in the `.gitignore` file to prevent accidental commits of secrets.

**Deliverables:**
-   Git diff showing the changes to application code and dependency files.
-   The new or modified `{{SRC_DIR}}/app/core/config.py` file.
-   A new `.env.example` file in the project root.
-   An updated `.gitignore` file.

**Acceptance Criteria:**
-   The application successfully boots and runs when configured solely through environment variables (or a `.env` file).
-   Running `grep -ri "SECRET\|PASSWORD\|KEY" {{SRC_DIR}}` reveals no hardcoded secrets in the application source code (ignoring the example file and variable names themselves).
-   The `.env.example` file exists and is checked into version control, while `.env` is ignored.
-   All relevant tests pass after the refactor.
