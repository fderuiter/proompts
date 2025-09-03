# 9. Secure-by-Default Configuration

**Objective:**
Establish a secure-by-default posture for the application by implementing essential security controls like CORS, rate limiting, and security headers from the start.

**Context:**
- **Middleware Location:** `src/app/main.py`
- **Rate Limiting Library:** `slowapi`
- **Security Documentation:** `docs/deployment_checklist.md`

**Agent Instructions:**
-   Security configurations should be loaded from the central `settings` object, not hardcoded.
-   Implement sensible, strict defaults that can be relaxed if necessary, rather than starting with loose permissions.
-   Create a deployment checklist that includes security verification steps.

**Tasks:**

1.  **Implement Strict CORS Policy:**
    -   In `src/app/main.py`, add `CORSMiddleware`.
    -   In your `settings` model, define `CORS_ALLOWED_ORIGINS` as a `list[str]`.
    -   In `.env.example`, set this to an empty list or a placeholder like `http://localhost:3000` for a local frontend.
    -   Configure the middleware to use this setting. **Do not use `allow_origins=["*"]`**.

2.  **Scaffold Rate Limiting:**
    -   Add `slowapi` to the project dependencies.
    -   In `src/app/core/limiter.py`, create a `Limiter` instance that uses the `Request` object's scope to get the client's host.
    -   Configure the default limit (e.g., "100/minute") from the `settings` object.
    -   In `src/app/main.py`, add `slowapi`'s exception handler and apply the limiter to the application state.
    -   Apply the rate limit decorator to an example endpoint.

3.  **Add Security Headers Middleware:**
    -   Create a simple custom middleware in `src/app/main.py` or a dedicated middleware file.
    -   This middleware should add the following headers to every response:
        -   `X-Content-Type-Options: nosniff`
        -   `X-Frame-Options: DENY`
        -   `Content-Security-Policy: default-src 'self'` (a restrictive default)
    -   If the application will be served over HTTPS, also add:
        -   `Strict-Transport-Security: max-age=31536000; includeSubDomains`

4.  **Add Request ID Middleware:**
    -   Create a middleware that generates a unique ID (e.g., UUID) for each incoming request.
    -   Attach this ID to the `request.state` and as a response header (`X-Request-ID`). This is crucial for tracing and debugging.

5.  **Set Input Size Limits:**
    -   Research and document how to limit the maximum request body size, for example, by configuring the underlying ASGI server (`uvicorn`) or through a middleware, to prevent denial-of-service attacks.

6.  **Create Deployment Checklist:**
    -   Create a `docs/deployment_checklist.md` file.
    -   Add a section for "Security Verification":
        -   "Confirm `CORS_ALLOWED_ORIGINS` is set correctly for the production environment."
        -   "Verify that rate limits are appropriate for expected traffic."
        -   "Check that HSTS is enabled if using HTTPS."
        -   "Ensure `DEBUG` mode is disabled in production settings."

**Deliverables:**
-   Git diff showing the new `slowapi` dependency and middleware configurations in `main.py`.
-   The `docs/deployment_checklist.md` file.
-   Tests that verify the security features:
    -   A test showing a cross-origin request is blocked.
    -   A test showing a request is rejected with a `429` status after the limit is exceeded.
    -   A test that asserts the presence of security headers on a response.

**Acceptance Criteria:**
-   All security tests pass.
-   A `curl -v` request to an API endpoint shows the security headers in the response.
-   A cross-origin request from a browser (in a test environment) is blocked by CORS.
-   Making rapid requests to a rate-limited endpoint triggers a `429 Too Many Requests` error.
-   The deployment checklist provides clear, actionable steps for security verification.
