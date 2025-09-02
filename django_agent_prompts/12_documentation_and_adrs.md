# Agent Prompt: Establish Project Documentation and ADRs

## 1. Objective

To create essential project documentation that enables new contributors to quickly get started and understand key architectural decisions, fostering long-term maintainability and knowledge sharing.

## 2. User-Provided Parameters

-   **Setup Time Goal (minutes):** `{{X}}` (e.g., `15`)

## 3. Agent Execution Plan

### Phase 1: Core Project Documentation

1.  **Create/Update `README.md`:**
    -   The README should be the front door to the project.
    -   Include:
        -   A brief project description.
        -   A list of prerequisites (e.g., `git`, `Docker`, `make`).
        -   A "Getting Started" section with a single command to run the project (e.g., `make setup && make up`).
        -   A table of useful `Makefile` commands (`test`, `lint`, `fmt`, etc.).
        -   A link to the more detailed `CONTRIBUTING.md`.

2.  **Create `CONTRIBUTING.md`:**
    -   This file should detail the process for contributing code.
    -   Include:
        -   The project's branching strategy (e.g., GitFlow, Trunk-Based).
        -   The Conventional Commits specification.
        -   Instructions on how to run linters and tests locally before pushing.
        -   The pull request process, including a link to the PR template.

3.  **Create `ARCHITECTURE.md`:**
    -   This document provides a high-level overview of the system's design.
    -   Include:
        -   A "Context" section describing the system's purpose.
        -   A "Guiding Principles" section (e.g., "Follow the 12-Factor App methodology," "Service-oriented architecture").
        -   A diagram or description of the main components (e.g., `web`, `worker`, `database`) and their interactions.
        -   A breakdown of the application's module boundaries (e.g., what `apps/users` is responsible for vs. `apps/products`).

### Phase 2: Architecture Decision Records (ADRs)

1.  **Create ADR Directory and Template:**
    -   Create a directory: `docs/adr/`.
    -   Inside it, create a template file named `0000-template.md`.
    -   The template should include the following sections:
        -   **Title:** A short, descriptive title.
        -   **Status:** Proposed, Accepted, Deprecated, Superseded.
        -   **Context:** What is the issue that needs to be decided?
        -   **Decision:** What is the change that we're proposing?
        -   **Consequences:** What becomes better or worse after this decision?

2.  **Create Initial ADRs for Key Decisions:**
    -   Based on the project setup, create the first few ADRs to document foundational choices. This serves as an example for future contributors.
    -   **Example ADRs:**
        -   `0001-use-poetry-for-dependency-management.md`
        -   `0002-adopt-service-repository-pattern.md`
        -   `0003-use-django-environ-for-settings-management.md`
        -   `0004-choose-celery-for-asynchronous-tasks.md`

### Phase 3: Onboarding and Changelog

1.  **Create an Onboarding Document:**
    -   Create `docs/onboarding.md`.
    -   This document is a step-by-step tutorial for a new contributor.
    -   Its goal is to get them from a fresh clone of the repository to a running application and passing test suite in under `{{X}}` minutes.
    -   It should be more detailed than the README's "Getting Started" section, explaining *what* is happening at each step.

2.  **Set up `CHANGELOG.md`:**
    -   Create a `CHANGELOG.md` file in the root directory.
    -   Structure it according to the "Keep a Changelog" format (https://keepachangelog.com/).
    -   Include sections for `[Unreleased]`, and then previous versions.
    -   Categorize changes under `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
    -   If using `semantic-release`, this file can be automatically updated. Instruct the user to add a placeholder.

## 4. Final Verification Criteria

1.  **File Existence:**
    -   Verify that all the specified documentation files have been created in their correct locations:
        -   `README.md`
        -   `CONTRIBUTING.md`
        -   `ARCHITECTURE.md`
        -   `CHANGELOG.md`
        -   `docs/onboarding.md`
        -   `docs/adr/0000-template.md`
        -   At least one example ADR file (e.g., `0001-...md`).

2.  **README Quality Check:**
    -   Read `README.md`. It must contain a clear, one-command instruction to start the project.
    -   It must link to other important documents.

3.  **Onboarding Path Simulation:**
    -   Mentally (or by executing the commands) follow the steps in `docs/onboarding.md`.
    -   The steps must be clear, correct, and logically lead to a running application.
    -   The estimated time to complete the steps should be reasonable for the `{{X}}` minute goal.

4.  **ADR Structure:**
    -   Check the content of the ADR template and the example ADRs. They must follow the specified "Title, Status, Context, Decision, Consequences" structure.
