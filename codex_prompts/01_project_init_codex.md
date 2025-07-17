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
