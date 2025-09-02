# Agent Prompt: Harden Django Settings and Secret Management

## 1. Objective

To refactor the Django settings into a 12-factor compliant configuration, separating configuration from code, eliminating secrets from the repository, and applying production security best practices.

## 2. User-Provided Parameters

-   **Settings Management Tool:** `{{django-environ | pydantic-settings}}`
-   **Path to Settings:** `{{path/to/settings.py}}` (or directory)

## 3. Agent Execution Plan

### Phase 1: Split Settings and Introduce Environment-Based Config

1.  **Analyze Existing Settings:**
    -   Read the current settings file(s) to identify hardcoded secrets, environment-specific configurations (like `DEBUG = True`), and database credentials.

2.  **Create Directory Structure:**
    -   If a single `settings.py` exists, create a `config/settings/` directory.
    -   Move the existing `settings.py` to `config/settings/base.py`.
    -   Create `dev.py`, `test.py`, and `prod.py` alongside `base.py`.

3.  **Install and Configure Settings Tool:**
    -   Add `{{Settings Management Tool}}` to the project's dependencies.
    -   In `config/settings/base.py`, instantiate the settings tool. For `django-environ`:
        ```python
        import environ
        env = environ.Env(
            # set casting, default value
            DEBUG=(bool, False)
        )
        # Assuming a .env file at the project root
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
        ```

### Phase 2: Externalize Secrets and Configuration

1.  **Refactor `base.py`:**
    -   Go through `base.py` and replace every hardcoded secret or configuration value with a call to the settings tool.
    -   **SECRET_KEY:** `SECRET_KEY = env("SECRET_KEY")`
    -   **DATABASE_URL:** `DATABASES = {"default": env.db("DATABASE_URL")}`
    -   **REDIS_URL:** `CACHES = {"default": env.cache("REDIS_URL")}`
    -   **ALLOWED_HOSTS:** `ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])`

2.  **Configure Environment-Specific Settings:**
    -   In `dev.py`:
        ```python
        from .base import *
        DEBUG = env.bool("DEBUG", default=True)
        # Add other dev-specific settings like django-debug-toolbar
        ```
    -   In `prod.py`:
        ```python
        from .base import *
        DEBUG = env.bool("DEBUG", default=False)
        # Production-only settings go here
        ```
    -   In `test.py`:
        ```python
        from .base import *
        # Test-specific settings, e.g., in-memory database or password hashers
        PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
        ```

3.  **Update `manage.py` and `wsgi.py`/`asgi.py`:**
    -   Change the `DJANGO_SETTINGS_MODULE` environment variable to point to the appropriate settings file. A common practice is to default to `dev` and require `prod` to be set explicitly.
        ```python
        # In manage.py
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
        ```

### Phase 3: Apply Security Hardening

1.  **Configure Production Security Flags (in `prod.py`):**
    -   `ALLOWED_HOSTS`: Must be populated via environment variable.
    -   `CSRF_TRUSTED_ORIGINS`: Must be populated via environment variable (e.g., `https://*.yourdomain.com`).
    -   `SECURE_HSTS_SECONDS`: `env.int("SECURE_HSTS_SECONDS", default=31536000)`
    -   `SECURE_HSTS_INCLUDE_SUBDOMAINS`: `True`
    -   `SECURE_HSTS_PRELOAD`: `True`
    -   `SECURE_SSL_REDIRECT`: `env.bool("SECURE_SSL_REDIRECT", default=True)`
    -   `SESSION_COOKIE_SECURE`: `env.bool("SESSION_COOKIE_SECURE", default=True)`
    -   `CSRF_COOKIE_SECURE`: `env.bool("CSRF_COOKIE_SECURE", default=True)`
    -   `SECURE_BROWSER_XSS_FILTER`: `True`
    -   `X_FRAME_OPTIONS`: `"DENY"`

2.  **Configure Production Logging:**
    -   In `prod.py`, override the `LOGGING` configuration to use `logging.handlers.JSONHandler` (or `structlog`) to output structured JSON to `stdout`.
    -   Ensure `DEBUG` is `False` in `prod.py`.

### Phase 4: Documentation

1.  **Create `.env.example`:**
    -   Create a file named `.env.example` in the project root.
    -   List *all* required environment variables.
    -   Use comments to explain what each variable is for.
    -   **CRITICAL:** Use placeholder values, NOT real secrets (e.g., `SECRET_KEY=change_me_in_production`).

2.  **Add to `.gitignore`:**
    -   Ensure `.env` and any other local environment files are listed in `.gitignore`.

## 4. Final Verification Criteria

1.  **No Secrets in Code:**
    -   Run a `grep` or search command for default Django `SECRET_KEY` values, `"localhost"`, or common password patterns within the settings directory. None should be found, except in comments or default values for the `env()` function.

2.  **Environment Files:**
    -   Verify that `.env.example` exists and is populated.
    -   Verify that `.gitignore` contains an entry for `.env`.

3.  **Django Production Check:**
    -   Execute the command: `python manage.py check --settings=config.settings.prod --deploy`
    -   The command must complete without any errors or warnings. It is acceptable for it to fail if environment variables (like `SECRET_KEY` or `ALLOWED_HOSTS`) are not set, as this proves they are being correctly loaded from the environment. The agent should run it with dummy env vars to ensure it *can* pass.
    `ALLOWED_HOSTS="localhost" SECRET_KEY="dummy" python manage.py check --settings=config.settings.prod --deploy`
