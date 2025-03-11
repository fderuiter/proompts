Here are the six core prompts structured into separate markdown documents, each with clear titles, content, and usage guidelines. 

---

## 📌 **Overview of Prompts and When to Use Them**

Below are distinct prompts categorized into five separate markdown documents designed to optimize your agentic coding workflow:

- **Prompt 1: Product Brief**  
  _Use at the very start of an application to define its high-level vision, features, and architecture._

- **Prompt 2: Project Brief (Epic)**  
  _Use at the beginning of every project (or major feature) to clarify goals, features, technical entities, and success metrics._

- **Prompt 3: Technical Implementation Plan**  
  _Use after completing the Project Brief to establish a clear, detailed, step-by-step technical execution plan._

- **Prompt 3: To-Do List Generation**  
  _Use after finalizing your technical plan, creating actionable tasks to guide coding sessions._

- **Prompt 4: Coding Session Guidelines**  
  _Use at the beginning of each coding task/session to instruct the AI clearly and maintain consistency._

- **Prompt 5: Project Review Guidelines**  
  _Use once the project or major feature development is complete to perform comprehensive quality checks and final validation._

---

# Prompt 1: Product Brief
**Filename:** `01_product_brief.md`

```markdown
# Product Brief

**Vision:**  
[Briefly describe the overall vision of the product.]

**Key Features and Roadmap:**  
- Feature 1 (Phase 1)  
- Feature 2 (Phase 2)  
- (Add more as needed…)

**Overall Architecture:**  
- Chosen architectural style (e.g., Domain-Driven Design, Event-driven, Vertical Slice, CRUD)  
- Brief description of key components and their interactions  

**Additional Context:**  
- Other relevant high-level details  
- Considerations, constraints, or risks  
- Stakeholder expectations or other non-technical considerations  

---

**When to use:**  
- Before starting a new application/project  
- When clarifying the vision and high-level scope for yourself or collaborators  

---

### Prompt 2: Project Brief (Epic)

```markdown
# Project Brief

## Project Description
- Briefly describe what this project or epic aims to accomplish.

## Key Features
- List and describe key features or milestones to be achieved.

## Technical Entities & Data Models
- Describe important data structures, entities, types, or objects relevant to this project.

## Business Rules & Logic
- Clearly outline any critical business rules or logic specific to this project.

## Success Metrics
- Define how the success of this project will be measured (performance, user engagement, etc.).

## Additional Implementation Details
- List any other technical details relevant to this project, constraints, or special considerations.
```

---

### Prompt 3: Technical Implementation Plan

```markdown
# Technical Implementation Plan

## Architecture Breakdown
- Clearly define modules, services, and architecture specifics.

## Libraries and Tools
- List exact libraries, frameworks, and technologies to use.

## Data Models & Specifications
- Detail all required data models, including fields, types, constraints, and relationships.

## Business Logic & Rules
- Define the logic clearly and comprehensively.

## Dependencies & Risk Analysis
- Identify potential dependencies, pitfalls, and solutions.

## Implementation Steps
- Clearly outline step-by-step how you’ll implement each feature, component, or service.

*Note: Iterate this plan at least 3-5 times to ensure robustness.*
```

---

### Prompt 4: Coding Session Guidelines

```markdown
# Development Guidelines

## Workflow (Per Task)
- **Write tests** first to cover the desired functionality clearly.
- **Implement code** to fulfill test cases.
- **Run tests** to confirm the implementation is correct:
  - Use `dotnet test` or specific test filters (`dotnet test --filter "TestName"`).
- Fix any errors that arise during testing immediately.

## Task Completion Checklist
After completing each task:
- [ ] Run tests (`dotnet test`) to confirm success.
- [ ] Update the to-do list with completed items marked clearly.
- [ ] Update `memory.md` with important project state changes or learnings.
- [ ] Note any lessons learned or insights in the development guidelines.
- [ ] End the chat session clearly after each completed task.

## Memory Maintenance
- Always refer to and update the `memory.md` file for context between sessions.
```

---

### Prompt 5: Project Review Guidelines

```markdown
# Project Review Guidelines

Before considering your work complete:

- [ ] **Run formatter:** Use `dotnet format` or equivalent tool.
- [ ] **Execute tests** with `dotnet test` and fix any failures.
- [ ] **Resolve warnings** identified by the compiler or static analysis tools.
- [ ] **Code review** by running `git diff --name-only main` and verifying all changes.
- [ ] Verify the **to-do list** ensuring all tasks are completed.
- [ ] Cross-reference the current state of the project with details in `memory.md`.
- [ ] Update development guidelines with insights from the completed project.
```

---

### Prompt 5: To-do List Generation

```markdown
# To-do List

- [ ] Task 1: Brief description of the task.
- [ ] Task 2: Another clear, actionable task.
- [ ] Task 3: Continue listing tasks derived from the technical plan.

## Completed Tasks
- [X] Previously completed task.

*Maintain clarity to support efficient AI task execution.*
```

---

### Prompt 6: Project Memory Management

```markdown
# Project Memory (`memory.md`)

## Current Project State
- Document current architectural decisions and justifications clearly.
- Capture critical notes or insights from past sessions.

## Contextual Notes
- Record important decisions or context needed for future reference.
- Include issues encountered and resolutions found.
- Do not mark task completions here; track them only in the to-do list.

*Regularly updated for persistent context management between sessions.*
```

---

### 🗒️ **When to Use Each Prompt:**

| Prompt                    | When to Use                                                              |
|---------------------------|--------------------------------------------------------------------------|
| **Product Brief**         | Once at the very beginning of the entire application.                    |
| **Project Brief (Epic)**  | Start of every significant feature or sub-project.                       |
| Technical Implementation Plan  | After defining the Project Brief; iterate until finalized.                |
| Coding Session Guidelines | At the start of every coding session/task.                               |
| Project Review Guidelines | After the project or feature completion for final validation and review. |
| To-Do List                | Updated continuously after technical implementation planning and each completed task. |
| Project Memory            | Continuously maintained after each session/task to preserve context.     |

──────────────────────────────

**Conclusion:**  
By using each prompt systematically and sequentially, you ensure a structured, repeatable, and highly effective AI-assisted workflow. This approach improves productivity, clarity, and the overall quality of AI-assisted software development tasks.