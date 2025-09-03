# 2. Config/Settings

**Goal:** Implement a typed, environment-driven configuration system using Pydantic settings.

**Context:**
*   This task follows the 12-factor app methodology, which states that configuration should be strictly separated from code and loaded from the environment.
*   Using Pydantic provides runtime type checking and validation for your configuration, preventing common errors.

**Tasks:**

1.  **Set Up Pydantic Settings:**
    *   Add `pydantic-settings` to the project dependencies.
    *   In `src/app/core/config.py`, create a `Settings` class that inherits from `pydantic_settings.BaseSettings`.
    *   Define all configuration variables as attributes on this class with type hints (e.g., `SECRET_KEY: str`, `DATABASE_URL: PostgresDsn`).
    *   Use Pydantic's `Field` to provide default values or other metadata.

2.  **Support Multiple Environments:**
    *   Use a `APP_ENV` environment variable (`local`, `test`, `prod`) to determine which configuration to load.
    *   The `Settings` class can be designed to load from different `.env` files based on the value of `APP_ENV` (e.g., `.env.local`, `.env.prod`).
    *   Alternatively, create separate `LocalSettings`, `TestSettings`, and `ProdSettings` classes that inherit from a common `BaseSettings`.

3.  **Configure Logging:**
    *   In `src/app/core/logging.py`, create a function to configure the application's logging.
    *   The logging configuration should be driven by the settings object (e.g., log level, log format).
    *   For development (`local`), logs should be human-readable. For production (`prod`), they should be structured (JSON).

4.  **Create `.env.example`:**
    *   Create a `.env.example` file in the root directory.
    *   This file should list every environment variable the application needs to run.
    *   Provide sensible default values for local development.
    *   Add comments to explain what each variable is for.
    *   Ensure the actual `.env` files are in `.gitignore`.

**Deliverables:**
*   The `src/app/core/config.py` and `src/app/core/logging.py` files.
*   The `.env.example` file.
*   The application factory (`create_app`) updated to use the new settings object.

**Acceptance Criteria:**
*   The application correctly loads its configuration from environment variables.
*   The application can be started in all supported environments (`local`, `test`, `prod`) by setting the `APP_ENV` variable.
*   Attempting to start the application with a missing or invalid environment variable results in a clear validation error from Pydantic.
*   The logging format changes based on the environment.

**Agent Tips:**
*   Pydantic can automatically read variables from a `.env` file if `python-dotenv` is installed. This is great for local development.
*   Use Pydantic's special types like `PostgresDsn` or `RedisDsn` to get automatic validation for connection strings.
*   Make your settings object available throughout your application via Flask's `current_app.config`. You can load the Pydantic settings into the Flask config object.
*   Remember to prefix your environment variables (e.g., `MYAPP_SECRET_KEY`) to avoid conflicts with other applications running on the same system. You can configure this in Pydantic's `SettingsConfigDict`.
