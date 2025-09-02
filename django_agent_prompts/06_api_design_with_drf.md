# Agent Prompt: Design a Versioned, Documented API with DRF

## 1. Objective

To implement a new, versioned, and well-documented REST API using Django Rest Framework (DRF), following best practices for structure, serialization, and schema generation.

## 2. User-Provided Parameters

-   **API Version:** `{{version}}` (e.g., `v1`)
-   **Authentication Scheme:** `{{JWT | Session | Token}}`
-   **API Root Path:** `/api/{{version}}/`

## 3. Agent Execution Plan

### Phase 1: Installation and Core Setup

1.  **Install Dependencies:**
    -   Add `djangorestframework` and `drf-spectacular` to the project's dependencies.

2.  **Configure Django Settings:**
    -   Add `rest_framework` and `drf_spectacular` to `INSTALLED_APPS`.
    -   Set up the default DRF configuration in `settings/base.py`.
        ```python
        REST_FRAMEWORK = {
            "DEFAULT_AUTHENTICATION_CLASSES": [
                # Configure based on {{Authentication Scheme}}
                "rest_framework.authentication.SessionAuthentication",
            ],
            "DEFAULT_PERMISSION_CLASSES": [
                "rest_framework.permissions.IsAuthenticated",
            ],
            "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
            "PAGE_SIZE": 25,
            "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
            "DEFAULT_THROTTLE_CLASSES": [
                "rest_framework.throttling.AnonRateThrottle",
                "rest_framework.throttling.UserRateThrottle",
            ],
            "DEFAULT_THROTTLE_RATES": {
                "anon": "100/hour",
                "user": "1000/hour",
            },
        }
        ```
    -   Configure the chosen authentication backend (e.g., `djangorestframework-simplejwt`).

### Phase 2: API Structure and Versioning

1.  **Create API App Structure:**
    -   Ensure an `api` app exists (`apps/api`).
    -   Create a versioned directory within the API app: `apps/api/{{version}}/`.
    -   Create `apps/api/{{version}}/urls.py`.

2.  **Set up URL Routing:**
    -   In the project's root `urls.py` (e.g., `config/urls.py`), include the API URLs under the versioned path.
        ```python
        # config/urls.py
        urlpatterns = [
            # ... other urls
            path("api/{{version}}/", include("apps.api.{{version}}.urls")),
        ]
        ```
    -   In `apps/api/{{version}}/urls.py`, set up a `DefaultRouter`.
        ```python
        # apps/api/v1/urls.py
        from rest_framework.routers import DefaultRouter
        from .views import UserViewSet

        router = DefaultRouter()
        router.register(r"users", UserViewSet, basename="user")

        urlpatterns = router.urls
        ```

### Phase 3: Implement Endpoints

1.  **Create Serializers:**
    -   For each model to be exposed, create a serializer in `apps/app_name/serializers.py`.
    -   Use `ModelSerializer` for efficiency.
    -   Be explicit with `fields` or `exclude` to avoid accidentally exposing sensitive data.
    -   Use `read_only_fields` for fields that should not be user-editable (e.g., `created_at`).

2.  **Create ViewSets:**
    -   In `apps/api/{{version}}/views.py`, create ViewSets for your resources.
    -   Use `ReadOnlyModelViewSet` for read-only endpoints and `ModelViewSet` for full CRUD.
    -   Define `queryset`, `serializer_class`, `permission_classes`, and `throttling_classes` on the ViewSet.
    -   Keep business logic out of views. Views should delegate to services.

3.  **Define Permissions:**
    -   Create custom permission classes in `apps/api/permissions.py` if needed (e.g., `IsOwnerOrReadOnly`).
    -   Apply the most restrictive permissions by default and open them up on a per-endpoint basis using the `@action` decorator if necessary.

### Phase 4: Documentation and Schema

1.  **Configure `drf-spectacular`:**
    -   Add the schema and UI endpoints to the root `urls.py`.
        ```python
        # config/urls.py
        from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

        urlpatterns += [
            path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
            path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
            path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
        ]
        ```
    -   Add metadata to `settings/base.py`:
        ```python
        SPECTACULAR_SETTINGS = {
            "TITLE": "{{Project Name}} API",
            "DESCRIPTION": "API for {{Project Name}}",
            "VERSION": "{{version}}",
            "SERVE_INCLUDE_SCHEMA": False,
        }
        ```

2.  **Annotate Views for Better Docs:**
    -   Use docstrings on ViewSet classes and methods to provide descriptions.
    -   Use `@extend_schema` decorators to add more detail, such as response codes, examples, and custom parameter descriptions.

3.  **Standardize Error Format:**
    -   Ensure that DRF's default exception handler is used, which provides a consistent `{ "detail": "..." }` or `{ "field_name": ["error message"] }` format for errors. If customization is needed, create a custom exception handler.

## 4. Final Verification Criteria

1.  **Schema Validation:**
    -   Start the development server.
    -   Access the schema URL (`/api/schema/`).
    -   Copy the generated OpenAPI JSON.
    -   Paste the JSON into an online OpenAPI validator (like Swagger Editor) and ensure it validates without errors.

2.  **API UI:**
    -   Access the Swagger UI (`/api/schema/swagger-ui/`) and Redoc (`/api/schema/redoc/`) pages.
    -   Verify that the endpoints are displayed correctly with their descriptions, parameters, and expected responses.

3.  **Endpoint Functionality:**
    -   Write contract tests for critical endpoints.
    -   These tests should:
        -   Verify the endpoint requires the correct authentication (`401 Unauthorized` for anonymous users).
        -   Verify the correct permissions are enforced (`403 Forbidden`).
        -   Verify a successful request (`200 OK`, `201 Created`) returns the expected data structure (can be checked with `pytest-snapshot`).
        -   Verify pagination headers or envelope are present on list endpoints.

4.  **Code Review:**
    -   Check that ViewSets are lean and do not contain business logic.
    -   Check that serializers explicitly define fields to be exposed.
