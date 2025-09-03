# 11. Security Hardening

**Goal:** Reduce the application's exposure to common web security risks by implementing a set of standard security measures.

**Context:**
*   This task addresses common vulnerabilities and security misconfigurations in web applications.
*   The focus is on applying well-known security enhancements through dedicated Flask extensions.

**Tasks:**

1.  **Implement Security Headers with Flask-Talisman:**
    *   Add `Flask-Talisman` to the dependencies.
    *   Initialize the extension to set security-enhancing HTTP headers, including:
        *   `Content-Security-Policy` (CSP): Start with a restrictive policy and gradually open it up as needed.
        *   `Strict-Transport-Security` (HSTS): Ensure this is only enabled if the application is served over HTTPS.
        *   `X-Frame-Options`, `X-Content-Type-Options`, etc.

2.  **Add Rate Limiting with Flask-Limiter:**
    *   Add `Flask-Limiter` to the dependencies.
    *   Configure a default rate limit for all endpoints.
    *   Apply stricter rate limits to sensitive endpoints, such as login and password reset forms, to protect against brute-force attacks.

3.  **Configure CORS and CSRF:**
    *   **CORS (Cross-Origin Resource Sharing):** If your API is intended to be used by a frontend application on a different domain, use `Flask-Cors` to configure a restrictive CORS policy. Only allow origins that you trust.
    *   **CSRF (Cross-Site Request Forgery):** If your application uses session-based authentication (cookies), use `Flask-WTF` or a similar extension to add CSRF protection to all state-changing requests (POST, PUT, DELETE).

4.  **Secure Cookies and Sessions:**
    *   Ensure that session cookies are configured with the `HttpOnly`, `Secure`, and `SameSite=Lax` (or `Strict`) flags.
    *   Use a server-side session store (like Redis or a database) instead of client-side cookies if you need to store more than a small amount of data.

**Deliverables:**
*   A diff showing the new security-related dependencies and their configuration.
*   A `security.md` document that outlines the security measures that have been implemented and their status. It should also document any risks that have been consciously accepted.

**Acceptance Criteria:**
*   The application's HTTP responses include the security headers set by `Flask-Talisman`. This can be verified using browser developer tools or an online scanner.
*   The rate limits are enforced. A script or test should demonstrate that exceeding the limit results in a `429 Too Many Requests` error.
*   The CORS policy correctly blocks requests from untrusted origins.
*   CSRF protection is active on all relevant forms.

**Agent Tips:**
*   Implementing a Content Security Policy (CSP) can be tricky. Start with a very strict policy (e.g., `default-src 'self'`) and then use the browser's console to see what resources are being blocked. Gradually add sources to the policy until your application works correctly.
*   When configuring rate limiting, be sure to use a persistent storage backend like Redis, especially if you have multiple application instances.
*   Don't apply global rate limits that are too strict, as you might lock out legitimate users. Apply stricter limits only to specific, high-risk endpoints.
*   A good way to test your security headers is to use a website like `securityheaders.com`. You will need to expose your local instance to the internet using a tool like `ngrok` to do this.
