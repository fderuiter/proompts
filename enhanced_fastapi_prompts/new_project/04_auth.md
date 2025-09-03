# 4. Authentication and Authorization

**Objective:**
Implement a standard, secure authentication and authorization system from day one. This will involve setting up an authentication scheme, creating password and token utilities, and providing a clear structure for role-based access control.

**Context:**
- **Authentication Scheme:** `{{JWT|OIDC}}` (This prompt will assume JWT)
- **Token URL:** `/api/v1/auth/token`
- **Auth Logic Location:** `src/app/core/auth.py`
- **Security Schemas:** `src/app/schemas/auth.py`
- **Password Hashing Library:** `passlib[bcrypt]`

**Agent Instructions:**
-   Implement OAuth2 with Password Flow for token generation, a common pattern for first-party clients.
-   Store only hashed passwords in the database. Never store plaintext passwords.
-   Create reusable dependencies (`Depends`) to protect endpoints and retrieve the current user.

**Tasks:**

1.  **Install Dependencies:**
    -   Add `passlib[bcrypt]` for password hashing.
    -   Add `python-jose[cryptography]` for creating and verifying JWTs.

2.  **Create Password Hashing Utilities:**
    -   In `src/app/core/auth.py`, create a `PasswordManager` class or functions:
        -   `hash_password(password: str) -> str`: Hashes a password using `bcrypt`.
        -   `verify_password(plain_password: str, hashed_password: str) -> bool`: Verifies a password against a hash.

3.  **Implement JWT Token Utilities:**
    -   In `src/app/core/auth.py`, create a `TokenManager` class or functions:
        -   `create_access_token(data: dict) -> str`: Creates a JWT with an expiration time.
        -   `decode_access_token(token: str) -> dict | None`: Decodes a token, handles expiration, and catches validation errors.
    -   Load the `SECRET_KEY` and token expiration settings from the main `settings` object.

4.  **Define Auth Schemas:**
    -   In `src/app/schemas/auth.py`, create Pydantic models for:
        -   `Token`: The response schema for the token endpoint (`access_token: str`, `token_type: str`).
        -   `TokenData`: The data encoded within the JWT (`username: str | None = None`).

5.  **Create Protected Endpoint Dependency:**
    -   In `src/app/core/auth.py`, define the OAuth2 scheme: `oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")`.
    -   Create a `get_current_user` dependency function that:
        -   Takes the token from the request via `oauth2_scheme`.
        -   Decodes the token using your utility.
        -   Retrieves the user from the database based on the token data.
        -   Raises a `401 Unauthorized` exception if the token is invalid or the user doesn't exist.

6.  **Build the Token Endpoint:**
    -   Create a new router at `src/app/api/v1/routers/auth.py`.
    -   Implement the `/token` endpoint using `OAuth2PasswordRequestForm`.
    -   The endpoint should:
        1.  Authenticate the user by comparing the provided password with the hashed password from the database.
        2.  If valid, create a new access token.
        3.  Return the token in the `Token` schema format.

7.  **Scaffold Role/Permission System:**
    -   In your user model, add a field for `role` (e.g., `role: str`, could be an enum `admin`, `user`).
    -   Create a dependency, e.g., `def require_admin(current_user: User = Depends(get_current_user)):`, that checks the user's role and raises a `403 Forbidden` if they don't have the required permissions.
    -   Apply this dependency to a secure example endpoint.

**Deliverables:**
-   Git diff showing new dependencies and the new auth-related files.
-   The `src/app/core/auth.py`, `src/app/schemas/auth.py`, and `src/app/api/v1/routers/auth.py` files.
-   An updated user model with a password hash field and role.
-   A suite of end-to-end tests for authentication and authorization.

**Acceptance Criteria:**
-   The end-to-end auth tests pass:
    -   A test successfully retrieves a token from the `/token` endpoint.
    -   A test shows a protected endpoint returns `401 Unauthorized` without a token.
    -   A test shows a protected endpoint returns `401 Unauthorized` with an invalid/expired token.
    -   A test shows a protected endpoint returns `200 OK` with a valid token.
    -   A test shows an admin-only endpoint returns `403 Forbidden` for a regular user.
    -   A test shows an admin-only endpoint returns `200 OK` for an admin user.
-   The database stores only hashed passwords, verified by inspecting the DB state during a test.
