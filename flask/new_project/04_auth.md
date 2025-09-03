# 4. Auth

**Goal:** Implement standard, secure authentication from day one.

**Context:**
*   Authentication is a critical component of most web applications. It's important to get it right from the start.
*   The chosen authentication method is `{{session|JWT|OIDC}}`. This prompt should be tailored to the chosen method.

**Tasks:**

1.  **Choose and Implement Auth Method:**
    *   **If `session`:**
        *   Use `Flask-Login` for session management.
        *   Implement a `User` model that includes methods required by `Flask-Login` (e.g., `is_authenticated`, `get_id`).
        *   Create login and logout endpoints.
    *   **If `JWT` (JSON Web Tokens):**
        *   Use a library like `Flask-JWT-Extended`.
        *   Create endpoints to issue access and refresh tokens in exchange for credentials (e.g., `/api/v1/auth/token`).
        *   Implement a decorator or middleware to protect endpoints, requiring a valid JWT.
    *   **If `OIDC` (OpenID Connect):**
        *   Use a library like `authlib` to integrate with an OIDC provider (e.g., Auth0, Okta, Keycloak).
        *   Implement the OIDC login flow (redirect to provider, handle callback).
        *   Use the received ID token to identify the user.

2.  **Scaffold Roles and Permissions:**
    *   Add `roles` and `permissions` fields to the `User` model or as a separate model.
    *   Create a decorator (e.g., `@roles_required('admin')`) to protect endpoints based on user roles.
    *   This provides a basic foundation for authorization, even if the logic is simple at first.

3.  **Secure Admin Actions:**
    *   Identify any initial actions that should be restricted to administrators (e.g., creating other users, viewing all data).
    *   Apply the role-based protection to these endpoints.

4.  **Create User Model and Repository:**
    *   Implement a `User` model in `src/app/db/models.py`. It should include fields for email, a hashed password, and any other relevant information.
    *   **Crucially, never store passwords in plaintext.** Use a strong hashing algorithm like `bcrypt` or `argon2`.
    *   Create a `UserRepository` to handle creating and retrieving users.

**Deliverables:**
*   The chosen authentication library integrated into the application.
*   The `User` model with password hashing.
*   Endpoints for login/logout or token issuance.
*   A protected endpoint that can only be accessed by an authenticated user.
*   A protected endpoint that can only be accessed by an admin.
*   End-to-end tests for the authentication and authorization flows.

**Acceptance Criteria:**
*   Authentication and authorization end-to-end tests are green.
*   An unauthenticated user attempting to access a protected endpoint receives a `401 Unauthorized` error.
*   A non-admin user attempting to access an admin-only endpoint receives a `403 Forbidden` error.
*   Passwords are correctly hashed in the database.
*   The chosen auth flow (session, JWT, or OIDC) works correctly.

**Agent Tips:**
*   Security is paramount. Follow the best practices recommended by the authentication library you are using.
*   For JWTs, store them securely on the client-side (e.g., in an `HttpOnly` cookie for web clients).
*   Your e2e tests are critical here. They should simulate a full login flow and then attempt to access protected resources.
*   Start with a simple role system (e.g., `user` and `admin`). You can make it more complex later if needed.
*   Use a library to handle password hashing. Don't try to implement it yourself. `werkzeug.security` (which comes with Flask) has helpers for this, but a dedicated library like `bcrypt` is often recommended.
