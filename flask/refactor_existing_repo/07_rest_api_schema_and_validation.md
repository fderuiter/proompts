# 7. REST API Schema and Validation

**Goal:** Introduce typed validation for all API endpoints and generate OpenAPI documentation to improve developer experience and API robustness.

**Context:**
*   This task is for Flask applications that have REST APIs without a formal specification or consistent validation.
*   The recommended tools are `Flask-Smorest` (which uses `apispec` and `marshmallow`) or `Flask-RESTX`.

**Tasks:**

1.  **Adopt an API Framework:**
    *   Choose and integrate either `Flask-Smorest` or `Flask-RESTX` into the application.
    *   Initialize the extension in the application factory.

2.  **Define API Schemas:**
    *   For each resource in your API, create request and response schemas using `marshmallow` (for `Flask-Smorest`) or the framework's built-in tools.
    *   These schemas should define the expected data types, validation rules (e.g., required fields, length constraints), and structure of the API payloads.

3.  **Apply Schemas to Endpoints:**
    *   Decorate your view functions to apply the schemas for request validation and response marshalling.
    *   For example, in `Flask-Smorest`, you would use `@Blueprint.arguments(RequestSchema)` and `@Blueprint.response(200, ResponseSchema)`.

4.  **Version the API:**
    *   Ensure all API endpoints are versioned under a common prefix, such as `/api/v1`.
    *   This is a best practice that allows you to evolve your API without breaking existing clients.

5.  **Implement Standardized Error Handling:**
    *   Create a consistent error envelope for all API errors (e.g., validation errors, not found errors). The response should have a predictable structure, like `{"error": {"code": "VALIDATION_ERROR", "message": "Invalid input.", "details": {...}}}`.
    *   Register custom exception handlers to automatically convert exceptions into this structured JSON response.

6.  **Expose OpenAPI Documentation:**
    *   Configure the chosen framework to expose an OpenAPI specification file (e.g., `/api/spec.json`).
    *   Enable the built-in documentation UI (e.g., Swagger UI or ReDoc) at a path like `/api/docs`.
    *   Enhance the documentation with examples for each endpoint.

**Deliverables:**
*   A diff showing the integration of the new API framework and the application of schemas to the endpoints.
*   New schema files for all API resources.
*   Updated error handling logic to produce consistent JSON error responses.

**Acceptance Criteria:**
*   All API endpoints have request and response schemas.
*   Invalid requests to the API are rejected with a 4xx error and a structured JSON error body.
*   The OpenAPI specification is available at `/api/spec.json` and is valid.
*   The API documentation is accessible in a browser and accurately reflects the API's functionality.
*   Each endpoint change should be accompanied by an update to the OpenAPI documentation and schema examples.

**Agent Tips:**
*   Start with one endpoint. Define its schemas, apply them, and test them thoroughly before moving to the next.
*   Use `curl` or a tool like Postman to test your endpoints. Provide `curl` examples for failing cases, including the exact expected response body. For example:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"email": "invalid"}' http://127.0.0.1:5000/api/v1/users
    ```
    The expected response might be:
    ```json
    {
      "error": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid input.",
        "details": {
          "email": ["Not a valid email address."]
        }
      }
    }
    ```
*   Pay attention to how you handle different status codes for responses (e.g., 200 for OK, 201 for Created, 204 for No Content).
