# 9. Security Defaults

**Goal:** Build a safe-by-default service by implementing a set of standard security measures from the outset.

**Context:**
*   Security should be a foundational part of the application, not an afterthought.
*   This task involves integrating several Flask extensions to protect against common web vulnerabilities.

**Tasks:**

1.  **Set Security Headers with Flask-Talisman:**
    *   Add `Flask-Talisman` to the dependencies.
    *   Initialize it in the application factory.
    *   Configure a strict Content Security Policy (CSP). A good starting point is `default-src 'self'`.
    *   Enable HTTP Strict Transport Security (HSTS), but only if the application will be deployed behind a proxy that terminates TLS (i.e., it's served over HTTPS).

2.  **Scaffold Rate Limiting with Flask-Limiter:**
    *   Add `Flask-Limiter` to the dependencies.
    *   Initialize the extension and configure it with a persistent storage backend like Redis.
    *   Establish a sensible default rate limit for all requests (e.g., "200 per day; 50 per hour").
    *   Scaffold a stricter limit for auth-related endpoints (e.g., "10 per minute") to protect against brute-force attacks.

3.  **Configure CORS:**
    *   Add `Flask-Cors` to the dependencies.
    *   Configure a restrictive CORS policy. By default, it should not allow any cross-origin requests.
    *   If a frontend will be used, add its specific origin to an allowlist in the configuration. Avoid using wildcard (`*`) origins.

4.  **Implement Request ID Middleware:**
    *   Create a simple middleware that generates a unique ID for every incoming request (e.g., using `uuid4`).
    *   Attach this ID to the Flask `g` object (`g.request_id`).
    *   Include the request ID in all structured log messages and in API error responses. This is invaluable for correlating events and debugging.

5.  **Set Input Size Limits:**
    *   Configure the WSGI server or a reverse proxy to limit the maximum size of a request body. This can prevent denial-of-service attacks that use large payloads.

**Deliverables:**
*   The integrated security extensions (`Talisman`, `Limiter`, `Cors`).
*   The request ID middleware.
*   A `security.md` document outlining the security measures in place, the rationale for their configuration, and instructions for how to report a vulnerability.

**Acceptance Criteria:**
*   HTTP responses include the security headers set by `Flask-Talisman`. This can be verified with browser developer tools or `curl -v`.
*   The configured rate limits are enforced and return a `429 Too Many Requests` error when exceeded.
*   The CORS policy blocks requests from untrusted origins.
*   Every log message and error response contains a unique request ID.
*   The security settings are documented in `security.md`.

**Agent Tips:**
*   A Content Security Policy (CSP) is very powerful but can be hard to configure. Start with a strict policy and use your browser's developer console to see which resources are being blocked. Add them to the policy one by one.
*   For rate limiting, the key should be based on the user's IP address or, for authenticated users, their user ID.
*   The request ID should be generated as early as possible in the request lifecycle. If you have a load balancer or reverse proxy in front of your app, it's often best to have it generate the ID and pass it to your application as a header (e.g., `X-Request-ID`).
*   Security is an ongoing process. The goal here is to establish a strong baseline.
