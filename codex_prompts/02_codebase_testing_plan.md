# codebase-testing-plan.prompt.md

<!-- Comprehensive “Testing Strategy & Roadmap” prompt -->

## Goal

Generate a detailed analysis of an existing codebase **and** produce a step-by-step plan to introduce or improve automated testing, aligned with project priorities, team skills, and CI/CD constraints.

## Context / Background

- **Codebase**  
   - Language(s) & framework(s) in use (e.g., TypeScript + React, Python +Django, Go micro-services).  
   - Current repository structure and build tooling (monorepo? workspaces? Make? Nx?).

- **Project Constraints**  
   - Release cadence, regulatory requirements, non-functional requirements (performance, security, accessibility).  
   - Team size, testing experience, and CI infrastructure.

- **Existing Quality Signals**  
   - Any legacy test suites, lint rules, static analysis, code coverage reports, incident post-mortems, or flaky-test dashboards.

- **Desired Outcomes**  
   - Faster releases? Higher reliability? Migration safety net? Explicitly list primary drivers.

> **Attach or link** the repository root (or a representative subset) so Copilot Chat can inspect folder and file patterns.

## Instructions

- **Inventory & Baseline**  
   - Parse the repository to map modules, layers, and key entry points.  
   - Identify existing tests (unit, integration, e2e) and current coverage %.  
   - Surface “hot spots” (high churn × low tests) and critical paths (auth, payments).

- **Risk-Based Prioritization**  
   - Classify components by business risk and complexity.  
   - Propose a “test pyramid” tailored to the stack (unit › service › contract › UI › e2e).  
   - Highlight quick wins (pure functions), high-risk areas (concurrency, security), and refactors needed for testability.

- **Framework & Tooling Selection**  
   - Recommend test runner(s), assertion libs, mocking/stubbing frameworks, fixture generators, and coverage tools per language.  
   - Define naming conventions, file locations (`__tests__`, `.spec.ts`, etc.), and CI commands.

- **Road-Mapped Milestones**  
   - **Phase 0 – Foundation**: Linting, formatter, pre-commit hooks, basic unit test skeleton.  
   - **Phase 1 – Critical Units & Services**: Cover top-priority modules to 70 %+.  
   - **Phase 2 – Integration & Contract Tests**: Add service-to-service/DB tests, schema contracts, test containers.  
   - **Phase 3 – End-to-End & Non-Functional**: UI flows with Playwright/Cypress, performance benchmarks, security scans.  
   - **Phase 4 – Continuous Improvement**: Add mutation testing, flaky-test detection, nightly stress suites.

- **CI/CD Integration**  
   - Insert steps in existing pipeline (GitHub Actions, GitLab CI, Jenkins) for test execution, coverage gating, and artifact upload.  
   - Fail thresholds on coverage drops; notify via chat ops.

- **Metrics & Reporting**  
   - Adopt KPIs: coverage %, mean time to detection, test flake rate, deployment rollback count.  
   - Automate dashboards (e.g., SonarQube, Codecov) and publish daily summaries.

- **Governance & Best Practices**  
   - Define code-review checklist items related to tests.  
   - Introduce testing “contracts” for new modules (TDD/ATDD optional).  
   - Schedule recurring audit of flaky tests and dependency updates.

- **Knowledge-Sharing**  
   - Draft internal wiki pages, lunch-and-learns, and pairing mentorship sessions to upskill the team.  
   - Provide a contribution guide with sample test patterns and anti-patterns.

- **Edge Cases & Future Enhancements**  
   - Chaos engineering for resilience.  
   - Cross-browser/device matrix expansion.  
   - Progressive adoption of property-based and mutation testing.

## Additional Notes

- If no repository is attached, ask the user to provide a zip or Git URL.  
- For polyglot repos, outline strategy per language, noting shared tooling (e.g., Docker, Make).  
- Respect any regulatory or PII constraints when suggesting test data.  
- Encourage a “thin slice” vertical approach for early wins rather than blanket coverage targets.

## Example Usage

1. **Attach Context** → select the root of the service folder and `ci.yml`.  
1. **Send prompt**:  
   > “Here is the current codebase (Node.js + Express). We deploy weekly and have zero automated tests. We care most about preventing regressions in our billing logic.”  
1. Copilot Chat responds with the full analysis and phased testing roadmap.
