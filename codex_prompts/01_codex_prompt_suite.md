# Codex-Flavoured Prompt Suite

Here’s a **Codex-flavoured edition** of the prompt suite — ready to paste straight into an OpenAI ChatGPT / Codex chat window.
All four files keep the standard “Goal → Context → Instructions → References → Additional Notes → Example Usage” layout, but:

* **Example Usage** now says “Paste this prompt into ChatGPT…” (no Copilot-specific steps).
* Each prompt reminds ChatGPT that it should answer by emitting **file contents and/or shell commands**, not by actually running anything.
* Environment-variable handling, sample code, and `.env` templates assume an **OpenAI API–based project** (the most common Codex scenario).

---

## 1. `project-init.codex.prompt.md`

```markdown
# Project Init & Skeleton (OpenAI Codex)

## Goal
Spin up a brand-new repository with a minimal but runnable skeleton, plus a one-command local dev experience.

## Context / Background
- Caller will supply:  
  1. **Language / framework** (e.g., TypeScript 5 + Next.js 14 or Python 3.12 + FastAPI).  
  2. **Package manager** (`npm`, `pnpm`, `poetry`, etc.).  
  3. **Licence** (MIT, Apache-2.0, proprietary).  
- The codebase will almost certainly talk to the **OpenAI API**. We therefore expect:  
  - a `.env.example` file with `OPENAI_API_KEY=`  
  - a helper module (`src/openaiClient.ts` or `openai_client.py`) that wraps `openai` calls.  
- Assume **GitHub** remote unless the caller overrides it.

## Instructions
1. **Ask the caller** for:
   - Project name & краткое описание  
   - Language / framework & version  
   - Package manager  
   - Monorepo? (yes/no)  
1. Generate:
   - Folder tree (`src/`, `tests/`, `configs/`, `scripts/`).  
   - A runnable “Hello, Codex 🚀” module under `src/` that makes a trivial `openai.ChatCompletion.create` call using the env var.  
   - `.env.example`, `README.md`, `.gitignore`, `CHANGELOG.md`, `CONTRIBUTING.md`.  
   - Task runner (`Makefile`, `npm scripts`, or `justfile`) with **setup / start / test / lint** targets.  
1. **Respond with**:
   - *Exact* shell commands to execute (e.g., `pnpm create next-app@latest …`).  
   - Full text of every generated file enclosed in triple back-ticks.  

## References
- [Org Directory Layout Guide](../docs/architecture/layout.md)

## Additional Notes
- If monorepo = yes, scaffold `packages/` with tooling placeholders.  
- All generated code should compile / run without extra tweaks.

## Example Usage
> Paste this prompt into ChatGPT, answer the four questions it asks, then copy the shell commands and file snippets into your editor/terminal.
```

---

## 2. `tooling-and-quality.codex.prompt.md`

```markdown
# Tooling, Linting & Quality Gates (OpenAI Codex)

## Goal
Add opinionated linters, formatters, type-checkers, commit hooks, and test frameworks so the repo “fails fast” on bad code.

## Context / Background
- A repository already exists (created via `project-init.codex.prompt.md`).  
- The primary language(s) were specified by the caller.  
- CI provider defaults to **GitHub Actions**.

## Instructions
1. Detect language(s) and apply tooling:
   - **JS/TS** → ESLint + Prettier, TypeScript strict, `husky` + `lint-staged`.  
   - **Python** → Ruff/Flake8, Black, Mypy, pre-commit.  
1. Add test framework:
   - **JS/TS** → Vitest (or Jest).  
   - **Python** → Pytest with coverage ≥ 80 %.  
1. Create / update config files (`.eslintrc`, `pyproject.toml`, etc.).  
1. Produce a **`quality.yml` GitHub Action**: install → lint → test → upload coverage.  
1. Reply with:
   - Any new or patched files (triple-back-tick blocks).  
   - A short “How to run locally” snippet (`pnpm test`, `pytest -q`, …).

## References
- [Quality Gates Standard](../docs/quality/gates.md)

## Additional Notes
- Merge, don’t clobber, any existing config.  
- Use the `.env.example` from step 1 to inject `OPENAI_API_KEY` in integration tests if needed.

## Example Usage
> Paste this prompt into ChatGPT from the root of your repo.  
> Tell ChatGPT the primary language if it can’t infer it (for polyglot repos).
```

---

## 3. `ci-cd.codex.prompt.md`

```markdown
# Continuous Integration & Delivery (OpenAI Codex)

## Goal
Generate GitHub Actions workflows that build, test, version, and deploy the app (often a containerised service that calls the OpenAI API).

## Context / Background
- Tooling & tests are in place.  
- Deployment targets could be Vercel, AWS ECS/Fargate, Fly.io, or plain Docker Compose on a VM.  
- Secrets will include `OPENAI_API_KEY`.

## Instructions
**Ask the caller**:
1. Environments (dev / staging / prod).  
1. Deployment platform and region.  
1. Secret-management preference (GitHub Encrypted Secrets, AWS Secrets Manager, Vault…).  
1. Versioning scheme (SemVer via `release-please`, CalVer, etc.).  

Then scaffold:
- `ci.yml` → lint + test + build.  
- `release.yml` → auto-tag & changelog.  
- `deploy-<env>.yml` files → fetch artifact, deploy, smoke-test endpoint that internally calls OpenAI with `echo` prompt “ping”.  
- Docs in `docs/deploy.md` describing how to add secrets.

Return all workflow YAML and any helper shell scripts as code blocks.

## References
- [CI/CD Best Practices](../docs/devops/ci-cd.md)

## Additional Notes
- Cache deps with `actions/cache@v4`.  
- Matrix test on multiple Node/Python versions if applicable.

## Example Usage
> Paste this prompt into ChatGPT after quality tooling is merged, answer the four questions, then commit the generated `.github/workflows/*`.
```

---

## 4. `docs-and-onboarding.codex.prompt.md`

```markdown
# Documentation & Developer Onboarding (OpenAI Codex)

## Goal
Create living docs that cut time-to-first-PR and capture architectural decisions.

## Context / Background
- Repo is runnable and deployable.  
- Org favours Markdown docs plus ADRs.

## Instructions
Generate / update:
1. **`README.md`**  
   - Quick Start (`pnpm i && pnpm dev` / `poetry run uvicorn main:app --reload`).  
   - Env-vars table (`OPENAI_API_KEY`, `OPENAI_ORG` …).  
   - Architecture diagram (ASCII or Mermaid link).  
   - Badges (build, test-coverage, licence).  
1. **`CONTRIBUTING.md`**  
   - Local setup, pre-commit, commit message style.  
1. `docs/` folder  
   - `architecture.md`, `troubleshooting.md`, `adr/0001-record-architecture-decisions.md`.  
1. `.vscode/extensions.json` suggesting “OpenAI Code-Completion”, Docker, and ESLint plugins.  

Output each file as a fenced code block.

## References
- [ADR Template](../docs/adr/template.md)

## Additional Notes
- If Codespaces or Dev Containers are desired, also scaffold `.devcontainer/`.

## Example Usage
> Paste this prompt into ChatGPT once CI/CD is in place, then review & commit the generated docs.
```

---

## Using the Suite

1. **Open a fresh ChatGPT/Codex chat tab.**
1. Run the four prompts **in order**, pasting each one verbatim and answering the questions it asks.
1. For every response, copy the file snippets / shell commands into your local workspace or PR.
1. Commit early & often; adjust anything that doesn’t match your team’s standards.

If you need an extra prompt (e.g., scaffolding Infrastructure-as-Code with Terraform or Pulumi), just let me know!
