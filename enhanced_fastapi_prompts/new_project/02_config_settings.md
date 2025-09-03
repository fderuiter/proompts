# 2. Typed, Environment-Driven Configuration

**Objective:**
Implement a robust, typed configuration system using Pydantic's `BaseSettings` that loads settings from environment variables, providing clear separation for different environments (local, testing, production).

**Context:**
- **Config File Path:** `src/app/core/config.py`
- **Pydantic Version:** `2.x`
- **Environments:** `local`, `testing`, `production`

**Agent Instructions:**
-   All configuration should be loaded into a single, immutable `settings` object.
-   No secrets or environment-specific values should be hardcoded.
-   Provide a clear, documented example file for developers to use as a template.

**Tasks:**

1.  **Add `pydantic-settings` Dependency:**
    -   Add `pydantic-settings` to the project's dependencies in `pyproject.toml` or `requirements/main.in`.

2.  **Create `Settings` Model in `config.py`:**
    -   In `src/app/core/config.py`, create a `Settings` class that inherits from `pydantic_settings.BaseSettings`.
    -   Define typed attributes for all configuration variables the app will need:
        -   `APP_NAME: str = "My FastAPI App"`
        -   `ENVIRONMENT: str = "local"`
        -   `LOG_LEVEL: str = "INFO"`
        -   `DATABASE_URL: str`
        -   `API_SECRET_KEY: str`
        -   `REDIS_URL: str | None = None`
    -   Use Pydantic's `model_config` to specify the source `.env` file:
        ```python
        from pydantic_settings import BaseSettings, SettingsConfigDict

        class Settings(BaseSettings):
            model_config = SettingsConfigDict(env_file=".env", extra="ignore")
            # ... fields ...
        ```
    -   Create a single, cached instance to be used throughout the app: `settings = Settings()`.

3.  **Implement Environment-Specific Logic:**
    -   Use the `ENVIRONMENT` setting to drive environment-specific behavior within the application. For example, `if settings.ENVIRONMENT == "production": ...`.
    -   The settings class can be designed to load different `.env` files based on the environment, but environment variables should always take precedence.

4.  **Create Logging Configuration:**
    -   In `src/app/core/logging.py`, create a function to configure the application's logging.
    -   This configuration should read its values (e.g., `LOG_LEVEL`) from the `settings` object.
    -   Call this configuration function once at application startup in `main.py`.

5.  **Create `.env.example`:**
    -   In the project root, create a `.env.example` file.
    -   List every environment variable required by the `Settings` model.
    -   Provide sensible, non-secret defaults for local development (e.g., `DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/appdb"`).
    -   For secrets, use placeholder values like `API_SECRET_KEY="your_secret_key_here"`.
    -   Add comments to explain the purpose of each variable.

6.  **Update `.gitignore`:**
    -   Add `.env` and `.env.*` to the `.gitignore` file to ensure no local environment files with secrets are ever committed.

**Deliverables:**
-   The `src/app/core/config.py` file containing the `Settings` model.
-   The `src/app/core/logging.py` file.
-   A `.env.example` file in the project root.
-   An updated `.gitignore`.
-   Git diff showing dependency updates and integration into `main.py`.

**Acceptance Criteria:**
-   The application starts correctly using configuration from a local `.env` file.
-   The application can be configured entirely via shell environment variables, which override any values in `.env` files.
-   Attempting to start the application without a required environment variable (like `DATABASE_URL`) raises a Pydantic validation error.
-   No secrets are present in any files checked into version control.
-   Logs are emitted at the level specified by the `LOG_LEVEL` setting.
