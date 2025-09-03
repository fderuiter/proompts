# 11. Security Hardening

**Objective:**
Reduce common security risks by implementing several layers of defense, including a strict CORS policy, rate limiting, standard authentication, and security headers.

**Context:**
- **Primary Security Middleware File:** `{{SRC_DIR}}/app/core/middleware.py`
- **Authentication Logic:** `{{SRC_DIR}}/app/core/auth.py`
- **Rate Limiting Library:** `{{slowapi|starlette-limiter}}`
- **Security Report:** `security.md`

**Agent Instructions:**
-   Apply the principle of "defense in depth."
-   Configuration for security policies (like CORS origins or rate limits) should be loaded from the central `settings` object, not hardcoded.
-   Document the security posture of the application.

**Tasks:**

1.  **Implement a Strict CORS Policy:**
    -   Add `CORSMiddleware` to your `main.py`.
    -   Configure it with a specific list of allowed origins, methods, and headers loaded from your `settings`.
    -   Avoid using wildcards (`"*"`) for origins in production.

2.  **Add Rate Limiting:**
    -   Install the chosen rate-limiting library (e.g., `slowapi`).
    -   Configure default rate limits (e.g., "100/minute") loaded from `settings`.
    -   Apply rate limiting to all endpoints, or to specific, sensitive ones as needed.
    -   Set up a `slowapi` limiter that uses a Redis backend for distributed rate limiting.

3.  **Implement or Strengthen Authentication:**
    -   If authentication is missing, implement a standard scheme like **OAuth2 with JWT Bearer tokens**.
    -   Create utility functions for creating and decoding JWTs.
    -   Create a `Depends` function that can be used in path operations to require authentication.
    -   If password-based login exists, ensure passwords are hashed with a strong algorithm like `bcrypt` or `argon2`.

4.  **Add Security Headers Middleware:**
    -   Create a simple custom middleware to add security-related HTTP headers to every response.
    -   Essential headers include:
        -   `X-Content-Type-Options: nosniff`
        -   `X-Frame-Options: DENY`
        -   `Strict-Transport-Security: max-age=31536000; includeSubDomains` (if served over HTTPS).
        -   `Content-Security-Policy: default-src 'self'` (or a more specific policy).

5.  **Create Security Report (`security.md`):**
    -   Create a new file, `security.md`.
    -   Document the security measures that have been implemented.
    -   Perform a brief self-audit against the OWASP Top 10 and list the status of each item. For example:
        -   **A01:2021 – Broken Access Control:** Addressed by [details of auth system].
        -   **A02:2021 – Cryptographic Failures:** Addressed by using HTTPS and hashing passwords.
        -   ...and so on.

**Deliverables:**
-   Git diff showing the addition of security middleware, authentication logic, and rate limiting.
-   The new `security.md` report.
-   Example `curl` commands demonstrating:
    -   A request being blocked by CORS.
    -   A request being blocked by the rate limiter (returning a 429 status).
    -   A request to a protected endpoint failing without a token and succeeding with one.
    -   Response headers including the new security headers.

**Acceptance Criteria:**
-   The security measures documented in `security.md` are verifiably implemented.
-   Tests for authentication, CORS, and rate limiting pass. For example, a test that makes too many requests should receive a `429 Too Many Requests` response.
-   The application remains fully functional for legitimate, authenticated users.
-   External security scanners (like a local `ZAP` scan) show an improved security posture.
