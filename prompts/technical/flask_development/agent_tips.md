# Agent Prompting Tips for Flask Development

When using the prompts in this directory to guide a coding agent, follow these best practices to ensure clear, actionable instructions.

-   **Be Specific About Locations**: Clearly state the full path to files and the names of functions or classes to be edited.
    -   *Good*: "Edit the `create_user` function in `/src/app/api/v1/blueprints/users.py`."
    -   *Bad*: "Edit the user creation code."

-   **Provide Concrete Examples**: For API changes or bug fixes, include `curl` examples of the request and the exact expected response body, especially for failing cases. This removes ambiguity.
    -   *Example*: "A `GET` request to `/api/v1/users/999` should return a 404 with the body `{\"error\": \"User not found\"}`."

-   **Require Schema and Doc Updates**: For any change to an API endpoint, explicitly require that the OpenAPI specification and any related schemas (e.g., Marshmallow, Pydantic) be updated accordingly. Ask the agent to provide a link to the updated documentation.

-   **Keep Scope Small and Focused**: Each prompt or request to the agent should be scoped to a single, logical unit of work, such as one blueprint, one service, or one bug fix. For larger features, ask the agent to first create a plan and then execute it one PR at a time.

-   **Specify Acceptance Commands**: Provide the exact commands the agent should run to verify its work. This creates a clear definition of done.
    -   *Examples*: `pytest -q`, `ruff --exit-zero`, `mypy --strict`, `flask --app app run`

-   **Provide Context for Tailoring**: If you want these prompts tailored for a specific repository, provide the following information:
    -   Repository URL
    -   Python, Flask, SQLAlchemy, and Postgres versions
    -   Package manager (`poetry`, `pip-tools`)
    -   CI provider (`github_actions`, `gitlab`)
    -   Deploy target (`fly.io`, `heroku`)
    -   Target test coverage percentage (`80%`)
