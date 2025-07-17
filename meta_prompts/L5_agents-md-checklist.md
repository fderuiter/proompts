# L5 AGENTS.md best-practice checklist and generation meta-prompt

## 1  Best-practice checklist for an **AGENTS.md** file

| Goal                               | Why it matters                                                                                                                                                     | Concrete tips                                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Clarify purpose**                | Codex (and similar agents) read AGENTS.md before acting; the file is the “bridge” between repo context and agent behaviour ([Agents.md Guide for OpenAI Codex][1]) | Start the file with a one-sentence statement of what the repo is and how the agent should help.               |
| **Place files hierarchically**     | Codex merges *\~/.codex/AGENTS.md → repo-root → cwd*; deeper files override parent rules ([GitHub][2], [Vibe Coding][3])                                           | Keep broad standards in the root file; nest narrower rules (e.g. `/tests/AGENTS.md`).                         |
=======
| **Place files hierarchically**     | Codex merges ~/.codex/AGENTS.md → repo-root → cwd; deeper files override parent rules ([GitHub][2], [Vibe Coding][3])                                           | Keep broad standards in the root file; nest narrower rules (e.g. `/tests/AGENTS.md`).                         |
| **Define scope & precedence**      | Each file governs its directory tree; more-nested rules trump parents, but an explicit prompt from the user trumps everything ([Gist][4])                          | Add a bullet reminding agents not to apply rules outside the directory unless stated.                         |
| **Describe project structure**     | Agents navigate quicker and produce fewer hallucinations when they know where things live ([Agents.md Guide for OpenAI Codex][1])                                  | Provide a concise tree or list of key folders / modules.                                                      |
| **Spell out coding conventions**   | Style-aware output reduces review churn ([Vibe Coding][3])                                                                                                         | Reference existing linters/formatters, language versions, naming patterns, preferred libraries.               |
| **Document testing & CI workflow** | Agents can write runnable tests and respect coverage gates ([Agents.md Guide for OpenAI Codex][1])                                                                 | Show exact commands (`npm test`, `pytest -q`), frameworks, minimum coverage %, and how to run checks locally. |
| **Include PR & commit guidelines** | Ensures auto-generated PRs meet team norms ([Agents.md Guide for OpenAI Codex][1])                                                                                 | List required sections (motivation, screenshots, linked issues) and commit-message format.                    |
| **Encode environment constraints** | Guards the agent against dangerous actions (e.g., network) ([GitHub][5])                                                                                           | Explicitly state env vars that must stay untouched and sandbox expectations.                                  |
| **Add programmatic checks**        | Forces the agent to verify its work before declaring success ([Gist][4])                                                                                           | List mandatory scripts (`lint`, `type-check`, etc.) the agent must run and pass.                              |
| **Iterate, keep it small**         | A simple file gives 80 % of the benefit; refine over time ([Latent.Space][6])                                                                                      | Start with structure + conventions, then expand when gaps appear.                                             |

---

## Ready-to-use **meta-prompt** for generating an AGENTS.md from any GitHub repo


```
# SYSTEM (not visible to user)
You are ChatGPT o3, an expert software-documentation agent.

# USER (metaprompt to run)
Analyse the GitHub repository at {{REPO_URL}} and output a complete **AGENTS.md** file that follows current best practices for ChatGPT Codex.

## Instructions
1. **Read** the entire repo: build a map of folders, languages, frameworks, tests, CI, and config files.
2. **Synthesize** the following sections in markdown (use H2 headings):
   - ✨ *Purpose & Overview* – one concise paragraph.
   - ✨ *Project Structure* – bullet list or tree of key directories/modules.
   - ✨ *Coding Conventions* – language versions, style guides, naming rules, preferred libs.
   - ✨ *Testing & Quality Gates* – commands, frameworks, coverage thresholds.
   - ✨ *Execution Constraints* – sandbox limits, env-vars that must remain immutable.
   - ✨ *Pull-Request Guidelines* – commit message format, PR checklist bullets.
   - ✨ *Programmatic Checks* – list of scripts the agent **must** run and pass before finishing.
3. **Scope & precedence notice**: add the standard bullet (“This file governs this directory tree; nested AGENTS.md override; direct system prompts override all.”).
4. **Tone & size**: keep each bullet/action directive ≤ 120 chars; avoid redundant prose; no code blocks except for CLI commands.
5. **Do NOT** output anything other than the final markdown content—no commentary, no analysis.

Return the markdown as the entire reply.
```

**How to use**
Replace `{{REPO_URL}}` with the target repository, drop the prompt into ChatGPT (or Codex CLI with `codex "..."`), and the agent will emit a ready-to-commit `AGENTS.md` that embodies the recommended structure above.

[1]: https://agentsmd.net/ "Agents.md Guide for OpenAI Codex - Enhance AI Coding"
[2]: https://github.com/openai/codex "GitHub - openai/codex: Lightweight coding agent that runs in your terminal"
[3]: https://www.vibecoding.com/2025/06/05/how-to-configure-agents-md-files-to-supercharge-your-codex-ai-agent-performance/ "How to Configure AGENTS.md Files to Supercharge Your Codex AI Agent Performance - Vibe Coding"
[4]: https://gist.github.com/dpaluy/cc42d59243b0999c1b3f9cf60dfd3be6 "AGENTS.md  SPEC for OpenAI Codex · GitHub"
[5]: https://raw.githubusercontent.com/openai/codex/main/AGENTS.md "raw.githubusercontent.com"
[6]: https://www.latent.space/p/codex "ChatGPT Codex: The Missing Manual - Latent.Space"
