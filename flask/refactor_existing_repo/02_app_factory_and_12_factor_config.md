# 2. Application Factory and 12-Factor Configuration

**Goal:** Refactor the Flask application to use the application factory pattern and manage configuration via environment variables, adhering to 12-factor app principles.

**Context:**
*   This task assumes the application currently uses a globally instantiated Flask app object.
*   The goal is to improve the application's structure, making it more testable, maintainable, and configurable.

**Tasks:**

1.  **Implement the Application Factory:**
    *   Create a `create_app` function in a new file, e.g., `/src/app/__init__.py`.
    *   The `create_app` function should accept a settings object or a path to a configuration file as an argument.
    *   Move the Flask app instantiation (`app = Flask(__name__)`) inside this function.
    *   Relocate extension initializations (e.g., `db.init_app(app)`, `ma.init_app(app)`) inside the factory function.
    *   Register all blueprints within the factory function.
    *   Register any custom CLI commands inside the factory function.
    *   Return the `app` instance from the factory function.

2.  **Adopt Environment-Driven Configuration:**
    *   Introduce a library like `pydantic-settings` or `python-dotenv` to manage configuration.
    *   Create a settings class or object that loads configuration from environment variables.
    *   Define separate configuration classes for different environments (e.g., `LocalConfig`, `TestingConfig`, `ProductionConfig`). These should inherit from a common `BaseConfig`.
    *   Ensure sensitive information like `SECRET_KEY`, database URIs, and API keys are loaded from the environment.
    *   Update the application entry point (e.g., `wsgi.py`, `manage.py`) to call `create_app` with the appropriate configuration.

3.  **Provide Configuration Examples:**
    *   Create a `.env.example` file in the root of the repository.
    *   This file should list all required environment variables with placeholder or default values.
    *   Add comments to explain each variable.
    *   Ensure the actual `.env` file is added to `.gitignore`.

**Deliverables:**
*   A diff of the changes, showing the new application factory, the updated configuration management, and the new `.env.example` file.
*   A brief markdown document (`docs/configuration.md`) explaining how to configure the application for different environments using environment variables.

**Acceptance Criteria:**
*   The application must successfully boot and run in all supported environments (local, testing, production) using only environment variables for configuration.
*   All existing tests must pass after the refactoring.
*   The `create_app` function should be the single entry point for creating an application instance.
*   No hardcoded secrets or environment-specific values should remain in the codebase.

**Agent Tips:**
*   Start by creating the `create_app` function and moving the app instantiation.
*   Incrementally move extensions and blueprint registrations into the factory.
*   When updating the configuration, ensure you have a complete list of all required variables.
*   Update the test suite to use the application factory for creating test app instances. This is a critical step for ensuring test isolation.
