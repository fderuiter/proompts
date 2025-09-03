# 7. API Versioning and Schema

**Objective:**
Establish a stable, versioned, and well-documented API surface. This involves organizing routes under a versioned prefix, using Pydantic for strict request/response models, and ensuring the auto-generated OpenAPI schema is clean and useful.

**Context:**
- **API Version:** `v1`
- **API Prefix:** `/api/v1`
- **Main App File:** `{{SRC_DIR}}/app/main.py`
- **Routers Directory:** `{{SRC_DIR}}/app/api/v1/routers/`

**Agent Instructions:**
-   Ensure all public-facing endpoints are grouped under the `/api/v1` prefix.
-   Every endpoint should have a `response_model` defined to prevent accidental data leakage and ensure a consistent API contract.
-   Implement a standardized error response schema.

**Tasks:**

1.  **Route Under `/api/v1` Prefix:**
    -   In `{{SRC_DIR}}/app/main.py`, create a main `APIRouter`.
    -   Include all resource-specific routers (e.g., from `{{SRC_DIR}}/app/api/v1/routers/`) into this main router.
    -   Include the main router in the FastAPI app instance with the prefix `/api/v1`.
    -   This creates a single point for versioning the entire API.

2.  **Enforce Response Models:**
    -   Audit all API endpoints (e.g., `@router.get(...)`).
    -   Ensure every endpoint has the `response_model` argument set to a specific Pydantic schema from the `schemas` module. This is crucial for security and documentation.
    -   For endpoints that return lists, use `response_model=list[MySchema]`.

3.  **Implement a Standard Error Envelope:**
    -   Create a generic Pydantic schema for error responses, for example, `ErrorDetail(detail: str)`.
    -   Register custom exception handlers that catch common exceptions (e.g., `HTTPException`, `RequestValidationError`) and return responses that conform to the `ErrorDetail` schema. This ensures consumers can always parse error messages reliably.

4.  **Configure OpenAPI Generation:**
    -   In `{{SRC_DIR}}/app/main.py` where the `FastAPI` app is instantiated, ensure the documentation URLs are explicitly set and enabled:
        -   `docs_url="/docs"`
        -   `redoc_url="/redoc"`
        -   `openapi_url="/api/v1/openapi.json"`

5.  **Implement Standard API Patterns:**
    -   **Pagination:** If not already present, define a standard pagination pattern. This can be done via query parameters (`skip: int = 0`, `limit: int = 100`) and a wrapper response schema like `PaginatedResponse[T](items: list[T], total: int)`.
    -   **Filtering:** Establish a convention for filtering resources, either through query parameters or a more advanced filtering system if needed.

**Deliverables:**
-   Git diff showing changes to `main.py`, routers, and the addition of exception handlers.
-   The generated `/api/v1/openapi.json` file.
-   Screenshots or text examples of the Swagger UI (`/docs`) and ReDoc (`/redoc`) pages.
-   Example `curl` commands for a paginated endpoint and an endpoint that returns a standardized error.

**Acceptance Criteria:**
-   All API endpoints are accessible only under the `/api/v1` prefix.
-   The application's OpenAPI schema (`/api/v1/openapi.json`) is valid and accurately reflects all endpoints.
-   Every endpoint uses a `response_model`, confirmed by inspecting the code and the `openapi.json` schema.
-   Triggering a 404 or 422 error returns a JSON response with the standardized error shape.
-   The interactive documentation at `/docs` and `/redoc` is available and functional.
