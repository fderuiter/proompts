# Enhanced FastAPI Prompts for Asynchronous Coding Agents

This folder contains a set of comprehensive, agent-focused prompts for bootstrapping a new FastAPI project or refactoring an existing one. These prompts are designed to be used by an asynchronous coding agent, providing clear, actionable instructions to ensure robust and complete implementation.

## How to Use

Each prompt is a self-contained markdown file representing a specific task or phase. To use a prompt:

1.  **Select a Prompt:** Choose the relevant prompt file from either the `new_project` or `refactor_existing_repo` directory.
2.  **Fill in Placeholders:** Review the `Context` section of the prompt and replace all `{{PLACEHOLDER}}` values with the specifics of your project.
3.  **Provide to Agent:** Give the entire content of the markdown file to your coding agent as the primary instruction set for the task.

The agent is expected to follow the tasks, produce the specified deliverables, and meet all acceptance criteria.

---

## Agent-Prompt Tips Specific to FastAPI

To ensure the best results when working with a coding agent on a FastAPI project, follow these guidelines:

*   **Be Specific with Locations:** Always provide exact file paths and function/router names.
    *   **Bad:** "Change the user creation logic."
    *   **Good:** "In the file `/src/app/api/v1/routers/users.py`, modify the `create_user` function."

*   **Provide Concrete Evidence:** Include failing test output, full stack traces, and exact HTTP requests/responses. Use `curl` examples with expected response bodies and status codes. This helps the agent understand the precise state and goal.
    *   **Example:** "The `POST /users` endpoint should return a `422 Unprocessable Entity` with the body `{"detail":[{"loc":["body","email"],"msg":"value is not a valid email address","type":"value_error.email"}]}` when the email is invalid."

*   **Define Clear Acceptance Criteria:** Specify acceptance tests in the form of HTTP calls, expected JSON payloads, and status codes. This creates a clear definition of "done."

*   **Scope Prompts Narrowly:** Limit each prompt to a single, cohesive unit of work, such as one API router, one service, or one specific refactoring task. For larger changes, ask the agent to first create a plan, then execute it in a separate pull request.

*   **Enforce Schema Updates:** When API endpoints are changed, explicitly require that the agent updates the OpenAPI schema (`openapi.json`). Request that they provide clear examples in the schema to document the changes for consumers.
