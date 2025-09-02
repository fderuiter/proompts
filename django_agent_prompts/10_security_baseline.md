# Agent Prompt: Implement a Django Security Baseline

## 1. Objective

To configure a Django project with a strong security baseline, mitigating common web application vulnerabilities as outlined by the OWASP Top 10.

## 2. User-Provided Parameters

-   **Production Domain(s):** `{{yourdomain.com}}` (Used for `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, etc.)
-   **Rate Limiting Required:** `{{yes | no}}`

## 3. Agent Execution Plan

### Phase 1: Harden Settings for Production

*Agent Note: Most of these settings should be applied in `settings/prod.py` and sourced from environment variables where appropriate.*

1.  **Configure Host and CSRF Headers:**
    -   `ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[".{{yourdomain.com}}"])`
    -   `CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["https://*.{{yourdomain.com}}"])`

2.  **Enable HSTS (HTTP Strict Transport Security):**
    -   `SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=31536000)` (1 year)
    -   `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
    -   `SECURE_HSTS_PRELOAD = True`

3.  **Enable Secure Cookies and SSL Redirect:**
    -   `SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)`
    -   `SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=True)`
    -   `CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=True)`

4.  **Set Browser Anti-Sniffing Headers:**
    -   `SECURE_CONTENT_TYPE_NOSNIFF = True`
    -   `X_FRAME_OPTIONS = "DENY"`

5.  **Implement a Content Security Policy (CSP):**
    -   Install `django-csp`.
    -   Add `csp.middleware.CSPMiddleware` to `MIDDLEWARE`.
    -   Configure a restrictive default policy in `settings/prod.py`.
        ```python
        CSP_DEFAULT_SRC = ("'none'",)
        CSP_SCRIPT_SRC = ("'self'",) # Or a CDN
        CSP_STYLE_SRC = ("'self'",)
        CSP_IMG_SRC = ("'self'", "data:")
        CSP_FONT_SRC = ("'self'",)
        CSP_CONNECT_SRC = ("'self'",)
        CSP_FRAME_ANCESTORS = ("'none'",)
        ```

### Phase 2: Authentication and Access Control

1.  **Rotate SECRET_KEY:**
    -   Ensure `SECRET_KEY` is loaded from an environment variable and is not the default Django key.
    -   Advise the user to generate and use separate, unique keys for `dev`, `test`, and `prod` environments.

2.  **Disable Admin in Production (Recommended):**
    -   Create a separate `urls_prod.py` that omits the `/admin/` path.
    -   Use an environment variable to select the root URLconf.
    -   Alternatively, place the admin on a non-standard, secret URL.

3.  **Implement Auth Rate Limiting (if required):**
    -   If `{{Rate Limiting Required}}` is 'yes', install `django-axes`.
    -   Add `axes.middleware.AxesMiddleware` to `MIDDLEWARE`.
    -   Configure `AXES_FAILURE_LIMIT` (e.g., 5 attempts) and `AXES_COOLOFF_TIME`.

### Phase 3: CI-Based Security Auditing

1.  **Add `bandit` to CI:**
    -   Add `bandit` to dev dependencies.
    -   Add a step in `.github/workflows/ci.yml` to run `bandit -r . -c pyproject.toml`.
    -   Configure `pyproject.toml` or `.bandit` to exclude known false positives (e.g., `B101:assert_used`).
        ```toml
        [tool.bandit]
        skips = ["B101"]
        ```

2.  **Add Dependency Audit to CI:**
    -   Add `pip-audit` or `safety` to dev dependencies.
    -   Add a step in CI to run `pip-audit` against the project's requirements. This will check for known vulnerabilities in dependencies.

### Phase 4: Secure File Handling

1.  **Validate File Uploads:**
    -   If the application accepts file uploads, ensure a library like `python-magic` is used to validate the file type by its content, not just its extension.
    -   Scan user-uploaded files for malware using a tool like ClamAV if possible.

2.  **Configure Storage Policies:**
    -   For user-uploaded content, use a separate storage backend (like an S3 bucket).
    -   Ensure this bucket is not publicly readable by default.
    -   Serve files via signed URLs with short expiry times, rather than making them public.
    -   Set a `Content-Disposition: attachment` header to prevent browsers from rendering uploaded HTML/JS files, mitigating XSS risks.

## 4. Final Verification Criteria

1.  **Security Check Command:**
    -   Run `python manage.py check --settings=config.settings.prod --deploy`.
    -   The command must pass without any security-related warnings.

2.  **HTTP Header Inspection:**
    -   Start the production-configured server locally.
    -   Use `curl -I http://localhost:8000` (or `https://` if using a local proxy).
    -   Verify the following headers are present and correct in the response:
        -   `Strict-Transport-Security`
        -   `X-Content-Type-Options: nosniff`
        -   `X-Frame-Options: DENY`
        -   `Content-Security-Policy`

3.  **CI Pipeline Validation:**
    -   Review the `ci.yml` file.
    -   Confirm that jobs for `bandit` and `pip-audit` exist and are configured to fail the build on issues.

4.  **OWASP Checklist:**
    -   Create a simple `SECURITY_AUDIT.md` file.
    -   Map the implemented controls back to the OWASP Top 10 list to show coverage.
        -   **A01: Broken Access Control:** Addressed by default Django permissions, disabling admin.
        -   **A02: Cryptographic Failures:** Addressed by HSTS, secure cookies, rotating `SECRET_KEY`.
        -   **A03: Injection:** Addressed by Django ORM's parameterization.
        -   **A04: Insecure Design:** N/A for this scope, relates to business logic.
        -   **A05: Security Misconfiguration:** Addressed by hardening settings, `check --deploy`.
        -   **A06: Vulnerable and Outdated Components:** Addressed by `pip-audit` in CI.
        -   ...and so on.
    -   This provides a clear deliverable demonstrating the security improvements.
