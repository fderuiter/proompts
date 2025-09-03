# 3. API Surface and Versioning

**Goal:** Define and implement the initial v1 API surface with schema validation and automated documentation.

**Context:**
*   This task builds on the bootstrapped repository to create the first real API endpoints.
*   Using a framework like `Flask-Smorest` from the start ensures the API is well-documented and robust.

**Tasks:**

1.  **Integrate Flask-Smorest:**
    *   Add `flask-smorest` and `marshmallow` to the dependencies.
    *   Initialize the `Api` extension in the application factory (`create_app`).
    *   Configure the `Api` with a title, version, and OpenAPI version.

2.  **Create a Versioned Blueprint:**
    *   In `src/app/api/v1/`, create a main blueprint for the v1 API.
    *   All resource-specific blueprints (like the example blueprint) will be registered with this v1 blueprint. This keeps the API versioned under the `/api/v1` URL prefix.

3.  **Define Request/Response Schemas:**
    *   In `src/app/schemas/`, create `Marshmallow` schemas for the example resource.
    *   You should have at least:
        *   A schema for creating the resource (request).
        *   A schema for representing the resource (response).
        *   A schema for updating the resource (request).

4.  **Implement the Example Resource:**
    *   In `src/app/api/v1/blueprints/example.py`, create a `Blueprint` and define the CRUD endpoints for an example resource (e.g., "Item", "Product").
    *   Use `Flask-Smorest` decorators to:
        *   `@blp.arguments(RequestSchema)`: Validate incoming request data.
        *   `@blp.response(200, ResponseSchema)`: Marshall outgoing data and document the successful response.
        *   Document other possible responses (e.g., 404 Not Found, 422 Unprocessable Entity).

5.  **Standardize Error Responses:**
    *   Implement a global error handler that catches common exceptions (e.g., `werkzeug.exceptions.NotFound`, validation errors) and returns a standardized JSON error response.
    *   The error response should have a consistent structure, like `{"error": {"code": "NOT_FOUND", "message": "Resource not found."}}`.

6.  **Expose API Documentation:**
    *   Ensure the configuration exposes the OpenAPI spec (e.g., at `/api/spec.json`) and a documentation UI (e.g., Swagger UI at `/api/docs`).

**Deliverables:**
*   The example resource blueprint with full CRUD functionality.
*   The Marshmallow schemas for the example resource.
*   The global error handling logic.
*   A fully functional and documented v1 API.

**Acceptance Criteria:**
*   The API is accessible under the `/api/v1` prefix.
*   All CRUD operations on the example resource work as expected and are validated by the schemas.
*   Sending an invalid request results in a `422` error with a structured JSON body explaining the validation errors.
*   The API documentation is accessible at `/api/docs` and accurately reflects the functionality of the example resource.
*   Example clients generated from the OpenAPI spec can successfully interact with the API.

**Agent Tips:**
*   Think about the structure of your schemas carefully. You can use inheritance to reduce duplication (e.g., a `ItemUpdateSchema` can inherit from `ItemCreateSchema`).
*   Provide clear examples in your schema definitions. These examples will be shown in the API documentation and are very helpful for consumers of your API.
*   Use `curl` to manually test your endpoints as you build them. Include these `curl` commands and their expected outputs in your test plan.
*   The scope of this task should be limited to one example resource. The goal is to set the pattern for how all future resources will be built.
