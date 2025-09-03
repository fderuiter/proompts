# Prompts for GitHub-Native Stacks

This collection of prompts is designed to guide an AI software engineering agent in setting up or refactoring projects to use a modern, "GitHub-native" stack.

The core philosophy is to use a consistent, best-practice toolchain that integrates deeply with GitHub's ecosystem.

## Core Tooling

The "Global GitHub Hygiene" prompt establishes a baseline that includes:

- **Package Management:** Poetry
- **CI/CD:** GitHub Actions
- **Containerization:** Docker with GHCR (GitHub Container Registry)
- **Code Quality:** Ruff, Black, Mypy, pre-commit
- **Testing:** Pytest
- **Security:** CodeQL, Dependabot
- **Release Management:** `release-please`
- **Documentation:** MkDocs with GitHub Pages

The framework-specific prompts (Django, FastAPI, Flask) build upon this foundation.

## CI/CD Example

A minimal, drop-in CI workflow file is available at `ci_example.yml`. The prompts may instruct the agent to use this as a starting point.

## Usage Note

If you want the agent to generate ready-to-commit files based on these prompts, provide a repository URL and specify the framework.
