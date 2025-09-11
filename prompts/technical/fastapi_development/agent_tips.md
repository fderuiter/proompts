# Agent Prompting Tips for FastAPI Development

When using the prompts in this directory to guide a coding agent, follow these best practices to ensure clear, actionable instructions.

-   **Provide Specific Locations**: Clearly state the full path to files and the names of routers or functions to be edited.
    -   *Good*: "Edit the `create_user` function in `/src/app/api/v1/routers/users.py`."
    -   *Bad*: "Edit the user creation code."

-   **Include Exact Traces and Outputs**: For bug fixes, provide the full failing test output. For API changes, include `curl` examples with the exact request and expected response bodies. HTTP traces are invaluable.

-   **Define Acceptance via API Calls**: Specify acceptance criteria in terms of HTTP calls with their expected status codes and JSON responses.
    -   *Example*: "A `GET` request to `/api/v1/users/123` must return status 200 and a JSON body matching the `UserPublic` schema."

-   **Keep Scope Small and Focused**: Each prompt should be scoped to a single router, service, or bug fix. For larger features, ask the agent to first create a plan and then execute it one PR at a time.

-   **Require OpenAPI and Schema Updates**: For any change to an API endpoint, explicitly require that the OpenAPI specification be updated. Ask the agent to confirm that the changes are reflected in the `/docs` UI and that schema examples are included.

-   **Provide Context for Tailoring**: If you want these prompts tailored for a specific repository, provide the following information:
    -   Repository URL
    -   Python, FastAPI, Pydantic, and Postgres versions
    -   Package manager (`poetry`, `pip-tools`)
    -   CI provider (`github_actions`, `gitlab`)
    -   Deploy target (`fly.io`, `heroku`)
    -   Target test coverage percentage (`80%`)
