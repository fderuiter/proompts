# Design.md Template and Guidelines

A `design.md` is your project’s “source of truth” for **why** and **how** something is being built. Teams read it to understand the problem, review it to approve the approach, and return to it months later to remember the rationale behind key choices.  A solid `design.md` usually follows this structure (adapt or reorder as your culture dictates):

<!-- markdownlint-disable MD033 -->
| Section                                              | Purpose                               | Typical Contents                                                                                                   |
| ---------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **1 · Title & Metadata**                             | Identify the doc at a glance.         | • Feature / component name; • Authors & reviewers; • Doc status (Draft → Review → Approved) |
| **2 · Context / Problem Statement**                  | Explain **why** we need anything new. | • Business/user pain points; • Data or metrics illustrating the gap; • Link to related issues, RFCs, PRDs |
| **3 · Goals (✓)**                                    | Spell out what “done” means.          | • Success criteria (functional and non-functional); • Must-have use-cases |
| **4 · Non-Goals (✗)**                                | Prevent scope creep.                  | • Explicitly list what will **not** be addressed |
| **5 · High-Level Solution Overview**                 | Give reviewers the “elevator pitch”.  | • One-paragraph summary; • Diagram of main components |
| **6 · Detailed Design / Architecture**               | Show **how** it works.                | • Component diagrams (C4, UML, sequence, data-flow, etc.); • API contracts / request-response examples; • Data model (schemas, migrations); • State machines or algorithms |
| **7 · Dependencies & Integration Points**            | Reveal knock-on effects.              | • External services, libraries, feature flags; • Migration or rollout plan |
| **8 · Security, Privacy, Performance & Reliability** | Cover cross-cutting concerns.         | • Threat model & mitigations; • P-level or SLO targets; • Load estimates, capacity planning |
| **9 · Trade-offs & Alternatives Considered**         | Document decision-making.             | • Options matrix (pros/cons); • Reasons final choice wins |
| **10 · Risks & Mitigations**                         | Surface what might go wrong.          | • Technical unknowns, operational risks; • Fallback or rollback strategy |
| **11 · Testing & Validation Plan**                   | Show how you’ll prove it works.       | • Unit / integration test strategy; • Performance benchmarks; • Acceptance criteria |
| **12 · Rollout Plan**                                | Describe how users get the feature.   | • Phased release, canary, or dark-launch steps; • Monitoring & observability hooks |
| **13 · Future Work**                                 | Keep the backlog clear.               | • Nice-to-haves; • Deferred features |
| **14 · Appendix / References**                       | Avoid cluttering the main flow.       | • Glossary; • Links to code spikes, prior designs, ADRs |

## Formatting Tips

* **Keep paragraphs short**; reviewers skim.
* Use **bullet lists, tables, and diagrams** generously.
* For diagrams, embed an image or use Mermaid code blocks (GitHub-compatible).
* Add a **“Last Updated”** badge so stale docs stand out.
* Adopt **consistent heading levels** (`##`, `###`) so the GitHub TOC sidebar is useful.

## When to create or update `design.md`

| Trigger                                 | Action                                                  |
| --------------------------------------- | ------------------------------------------------------- |
| New feature or major refactor           | Create a fresh doc and mark it *Draft*.                 |
| Significant design change after launch  | Append an “Alternatives” update or link an ADR section. |
| Minor tweaks (e.g., small API addition) | Inline edit and bump “Last Updated”.                    |

A clear, version-controlled `design.md` saves time during code review, eases onboarding, and becomes living documentation that evolves with your system.

<!-- markdownlint-enable MD033 -->
