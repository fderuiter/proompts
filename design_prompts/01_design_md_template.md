---
id: design-md-template
title: Design.md Template
category: design_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [documentation, design]
---

# Design.md Template

Title: Document Software Design Decisions

Role: Documentation Architect

Task:
- Provide a structure for a project design.md file.
- Explain the purpose of each section.
- Summarise formatting tips and triggers for updates.

Context:
"""
A `design.md` records why and how something is built. Teams read it to understand the problem, review it to approve the approach and revisit it later for rationale.

| Section | Purpose | Typical Contents |
| --- | --- | --- |
| **1 · Title & Metadata** | Identify the doc quickly. | Feature name, authors, doc status |
| **2 · Context / Problem Statement** | Explain why change is needed. | Pain points, metrics, related issues |
| **3 · Goals (✓)** | Spell out what “done” means. | Success criteria, must-have use cases |
| **4 · Non-Goals (✗)** | Prevent scope creep. | Items explicitly out of scope |
| **5 · High-Level Solution Overview** | Give the elevator pitch. | One-paragraph summary, component diagram |
| **6 · Detailed Design / Architecture** | Show how it works. | Diagrams, API contracts, data model |
| **7 · Dependencies & Integration Points** | Reveal knock-on effects. | External services, migration plan |
| **8 · Security, Privacy, Performance & Reliability** | Cover cross-cutting concerns. | Threat model, SLO targets, capacity planning |
| **9 · Trade-offs & Alternatives Considered** | Document decision-making. | Options matrix, reason for final choice |
| **10 · Risks & Mitigations** | Surface what might go wrong. | Technical unknowns, rollback strategy |
| **11 · Testing & Validation Plan** | Prove it works. | Test strategy, benchmarks, acceptance criteria |
| **12 · Rollout Plan** | Explain how users get the feature. | Phased release, monitoring hooks |
| **13 · Future Work** | Keep the backlog clear. | Nice-to-haves, deferred features |
| **14 · Appendix / References** | Avoid clutter. | Glossary, links to prior designs |

Formatting tips: keep paragraphs short, use tables and diagrams, and add a "Last Updated" badge. Create or update `design.md` for new features, major refactors or significant post-launch changes.
"""

Constraints:
- Use consistent heading levels so the GitHub TOC works.
- Encourage bullet lists and Mermaid diagrams when useful.

Output Format: markdown
--------------------------------------------------
