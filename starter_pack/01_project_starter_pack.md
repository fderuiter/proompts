# Project Starter Pack Prompts

Below are ready-to-copy prompts—one per document in the starter pack.
Each prompt tells an AI assistant (or any author) exactly what to deliver, what sections to include, and the desired length or format. Feel free to tweak wording or depth, but this will get you 90 % of the way there.

---

## 1. Project Charter / Vision Statement

Prompt:

> Draft a 1–2-page Project Charter for **“{Project Name}.”**
> Include these sections, each with concise bullets:
>
> - Purpose & Vision (why we’re doing this)
> - Business Goals & Success Metrics (SMART)
> - High-Level Scope (in / out)
> - Key Deliverables & Milestones
> - Assumptions & Constraints
> - Named Stakeholders & Sponsors
> - Budget / Resource Snapshot
>    Tone: executive-friendly, factual, no jargon.

---

## 2. Stakeholder & RACI List

Prompt:

> Create a one-page Stakeholder Register for **“{Project Name}.”**
> Provide a table with columns: Role, Name, Responsibility, RACI letter (R, A, C, I), Communication Channel.
> Follow with one paragraph on escalation paths.

---

## 3. Functional Specification / User-Story Backlog

Prompt:

> Write a lightweight Functional Specification for **“{Feature Area}.”**
> • Begin with a brief context summary.
> • Then list user stories in “As a … I want … so that …” format, each with Acceptance Criteria in Gherkin style.
> • End with open questions & dependencies.
> Aim for ≤5 pages.*

---

## 4. Non-Functional Requirements (NFR) Sheet

Prompt:

> Produce an NFR checklist for **“{Project Name}.”**
> Categories: Performance, Scalability, Availability, Security, Compliance, Accessibility, Observability, Internationalization.
> For each, give measurable targets (e.g., “p95 latency < 200 ms”). Present in a two-column table.*

---

## 5. High-Level Architecture Diagram & ADRs

Prompt:

> Write an Architecture Decision Record (ADR) titled **“Choose System Architecture for {Project Name}.”**
> Use the MADR 2.0 template.
> After the ADR text, list components and interfaces in PlantUML syntax so the diagram can be rendered. Keep narrative ≤2 pages.*

---

## 6. Data Model / ER Diagram

Prompt:

> Generate an Entity-Relationship description for **“{Domain}.”**
> Provide:
> • Overview paragraph
> • Table per entity: attributes, PK, FK, constraints
> • At the end, give a concise PlantUML ER diagram block.*

---

## 7. API Contract & Versioning Policy

Prompt:

> Create an OpenAPI 3.1 YAML spec stub for **“{Service}.”**
> Include one sample endpoint per CRUD verb, standard error schema, and a section explaining semantic versioning rules and deprecation policy.*

---

## 8. Roadmap / Milestone Plan

Prompt:

> Produce a quarterly roadmap for **{Next 12 Months}** showing Epics, Start/End dates, and owners. Deliver as a Markdown table plus a brief narrative explaining sequencing logic.*

---

## 9. Risk Register & Mitigation Plan

Prompt:

> Draft a Risk Register: table with Risk#, Description, Impact (1-5), Probability (1-5), Exposure (= I×P), Mitigation, Owner. Add a heat-map summary (textual: High / Medium / Low).*

---

## 10. Test Strategy & Definition of Done

Prompt:

> Write a 2-page Test Strategy for **“{Project Name}.”**
> Cover: Test Pyramid targets, tooling, coverage thresholds, non-functional tests, and the precise “Definition of Done” checklist.*

---

## 11. Coding Standards & Style Guide

Prompt:

> Produce a language-specific Style Guide for **{Language/Framework}.**
> Include: formatting (link to linter config), naming conventions, error handling rules, comment standards, and example code blocks. Output as Markdown.*

---

## 12. CI/CD Pipeline Blueprint

Prompt:

> Describe the CI/CD pipeline for **“{Project Name}.”**
> Sections: Trigger flow, Build steps, Test stages, Security scans, Artifact storage, Deployment strategy, Rollback hooks. Include a Mermaid flowchart snippet.*

---

## 13. Deployment & Rollback Runbook

Prompt:

> Create an operations runbook titled **“Deploying & Rolling Back {Project Name}.”**
> • Preconditions checklist
> • Step-by-step commands
> • Verification script
> • Rollback procedure
> • Contact matrix for on-call escalation.*

---

## 14. Repository README & Quick-Start Guide

Prompt:

> Write a repo README for **“{Project Name}.”**
> Must have: Project blurb, Badges placeholder, Prerequisites, 3-step local setup, Common npm or make commands, How to run tests, Contribution quick-links, License line.*

---

## 15. Branching / Version-Control Strategy

Prompt:

> Document the Git strategy (e.g., Trunk-Based) for **“{Project Name}.”**
> Include: branch types, naming, PR rules, release tags, hotfix flow diagram, and expected commit message format (Conventional Commits).*

---

## 16. Contribution Guidelines & Code-Review Checklist

Prompt:

> Create CONTRIBUTING.md content.
> Parts: How to file issues, Branch naming, PR template text, Code-Review checklist (10 yes/no items), and community conduct link.*

---

## 17. Communication & Meeting Cadence Plan

Prompt:

> Outline the team’s collaboration plan.
> Provide a table: Ceremony, Frequency, Duration, Participants, Tools (e.g., Slack, Zoom). End with norms for asynchronous updates.*

---

## 18. License & Third-Party Software Inventory

Prompt:

> Generate a Third-Party Inventory template.
> Columns: Package, Version, License, Usage, Notes.
> Prepend one paragraph explaining compliance obligations and link to SPDX identifiers.*

---

## 19. Security & Privacy Threat Model

Prompt:

> Author a STRIDE-based threat model for **“{Project Name}.”**
> Steps: System overview, Data-flow diagram description, Threat enumeration table (STRIDE columns), Mitigation actions, Residual risk rating.*

Copy, paste, and run any prompt when you’re ready to spin up that document—no blank-page anxiety required!
