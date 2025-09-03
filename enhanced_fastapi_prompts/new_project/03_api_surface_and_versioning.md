# 3. API Surface and Versioning

**Objective:**
Design and implement the initial V1 API surface, establishing clear versioning, standardized error responses, and reusable patterns for pagination and filtering from the outset.

**Context:**
- **API Version:** `v1`
- **API Prefix:** `/api/v1`
- **Main App File:** `src/app/main.py`
- **Routers Directory:** `src/app/api/v1/routers/`
- **Schemas Directory:** `src/app/schemas/`

**Agent Instructions:**
-   All endpoints must be versioned under the `/api/v1` prefix.
-   Implement global exception handlers to ensure all errors, including validation errors, return a consistent and predictable JSON structure.
-   Use Pydantic schemas for all request and response bodies to enforce a strict contract.

**Tasks:**

1.  **Set Up Versioned Routing:**
    -   In `src/app/main.py`, create a main `APIRouter` for the v1 API.
    -   Include all individual resource routers (like `health.py`, `example.py`) into this main v1 router.
    -   Mount the v1 router onto the main FastAPI app instance with `prefix="/api/v1"`.

2.  **Implement Standardized Error Handlers:**
    -   Create a generic error schema in `src/app/schemas/errors.py`, e.g., `ErrorResponse(detail: str | list[dict])`.
    -   In `src/app/main.py`, add a global exception handler for `RequestValidationError` (HTTP 422). This handler should reformat Pydantic's verbose errors into a cleaner, more user-friendly structure.
    -   Add another global handler for `HTTPException` to ensure all manually raised HTTP errors conform to your `ErrorResponse` schema.

3.  **Define a Pagination Pattern:**
    -   Create a generic Pydantic `Page` schema in `src/app/schemas/pagination.py`:
        ```python
        from pydantic import BaseModel, Field
        from typing import Generic, TypeVar

        T = TypeVar("T")

        class Page(BaseModel, Generic[T]):
            items: list[T]
            total: int
            page: int = Field(..., gt=0)
            size: int = Field(..., gt=0)
        ```
    -   Create a `Depends` function that provides pagination query parameters (`page: int = 1`, `size: int = 20`).
    -   Update the example router to include an endpoint that returns a paginated response using this schema.

4.  **Establish Filtering Conventions:**
    -   Document a convention for how API filtering will work. For simple cases, this can be done via query parameters on list endpoints (e.g., `GET /users?is_active=true`).
    -   For a more complex filtering strategy, you might define a filter parameter that accepts a JSON object.

5.  **Enforce `response_model` Usage:**
    -   For all created endpoints, explicitly set the `response_model`.
    -   For the paginated endpoint, use the generic `Page` schema (e.g., `response_model=Page[UserSchema]`).

**Deliverables:**
-   Git diff showing changes to `main.py` and the router files.
-   New files for schemas (`errors.py`, `pagination.py`) and exception handlers.
-   The generated `/api/v1/openapi.json` file.
-   `curl` examples demonstrating:
    -   A successful request to a paginated endpoint.
    -   A request that triggers a 422 validation error, showing the custom error response.
    -   A request that triggers a 404 error, showing the custom error response.

**Acceptance Criteria:**
-   All endpoints are accessible under the `/api/v1` prefix.
-   A `POST` request with an invalid request body returns a `422` status code and a JSON payload conforming to the `ErrorResponse` schema.
-   A request to a non-existent URL returns a `404` status code and a JSON payload conforming to the `ErrorResponse` schema.
-   The `/api/v1/openapi.json` schema is valid and accurately documents the paginated response and error shapes.
-   The example paginated endpoint works correctly.
