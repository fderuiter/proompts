# Enhanced Agent Prompts for Django Projects

This directory contains a collection of comprehensive, step-by-step prompts designed for use with an asynchronous coding agent. Each markdown file tackles a specific, high-level development task for a Django project, breaking it down into an actionable execution plan with clear verification criteria.

## Purpose

The goal of these prompts is to provide a robust, reusable, and standardized framework for common software engineering tasks. By using these templates, a coding agent can perform complex operations like bootstrapping a new production-grade application, refactoring legacy code, or implementing a security baseline with a high degree of precision and consistency.

## How to Use

1.  **Select a Prompt:** Choose the markdown file that matches your development goal (e.g., `01_bootstrap_production_django_project.md`).
2.  **Fill in Parameters:** Each prompt begins with a "User-Provided Parameters" section. Fill in the `{{...}}` placeholders with the specific details for your project.
3.  **Provide to Agent:** Paste the entire, filled-in content of the markdown file into your coding agent as the initial instruction.

The agent will use the "Agent Execution Plan" as its step-by-step guide and the "Final Verification Criteria" to confirm that the task was completed successfully.

## Prompt Library

| File | Title | Description |
| --- | --- | --- |
| `01_bootstrap_production_django_project.md` | Bootstrap Production-Grade Django Project | Creates a new, maintainable Django project from scratch. |
| `02_refactor_existing_django_project.md` | Refactor Existing Django Project | Systematically refactors a repo for modularity and scalability. |
| `03_repository_hygiene_and_standards.md` | Implement Repository Hygiene | Enforces uniform repo standards like pre-commit, CI, and templates. |
| `04_settings_and_secrets_hardening.md` | Harden Settings and Secrets | Implements 12-factor settings and secure secret management. |
| `05_testing_strategy_and_fixtures.md` | Implement a Modern Testing Strategy | Establishes a fast and reliable testing suite with pytest. |
| `06_api_design_with_drf.md` | Design a Versioned, Documented API | Implements a versioned, documented API with DRF and OpenAPI. |
| `07_performance_and_caching.md` | Improve Performance and Caching | Audits for N+1s and implements a Redis caching layer. |
| `08_async_tasks_and_scheduling.md` | Implement Async Tasks with Celery | Sets up a reliable background processing system with Celery. |
| `09_observability_and_error_handling.md` | Implement Observability | Integrates structured logging, error tracking (Sentry), and health checks. |
| `10_security_baseline.md` | Implement a Security Baseline | Configures Django to mitigate common OWASP Top 10 risks. |
| `11_containerized_dev_environment.md` | Create a Containerized Dev Environment | Creates a one-command local setup with Docker Compose. |
| `12_documentation_and_adrs.md` | Establish Project Documentation | Creates essential docs like README, ARCHITECTURE, and ADRs. |
