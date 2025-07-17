# L5 README Generator

---
---
Below is a reusable **"prompt-for-the-prompt"** you can give to an AI agent (e.g. ChatGPT) so it can inspect an entire codebase and draft a high-quality `README.md` that covers everything a new developer typically needs.

---

```text
📝 **TASK OVERVIEW**

You are an expert technical writer and senior software engineer.  
Your task is to explore the entire repository you are given (all folders, files, and docs) and then generate a polished `README.md` in Markdown.  
Write in clear, concise English, suitable for engineers who have never seen this code before.

---

🔍 **WHAT TO EXTRACT & INCLUDE**

1. **Project title & one-sentence elevator pitch**  
1. **High-level purpose / problem solved** (why the project exists, who it serves)  
1. **Key features / capabilities** (bullet list)  
1. **Tech stack summary**  
   - Primary languages, frameworks, notable libraries  
   - Runtime / version requirements (e.g., Node v20, Python 3.12)  
1. **Architecture & folder structure**  
   - One-paragraph overview plus a tree diagram of top-level dirs and their purpose  
1. **Setup / installation**  
   - Prerequisites (SDKs, package managers, services)  
   - Step-by-step install & first-run commands  
   - How to configure environment variables or secrets (list each variable you find)  
1. **Running & developing**  
   - Common dev scripts/CLI commands (`npm run dev`, `poetry run`, `docker compose up`, etc.)  
   - Hot-reload / live-reload instructions if applicable  
1. **Testing**  
   - How to execute unit/integration tests  
   - Linting, formatting, or static-analysis commands  
1. **Deployment / production usage**  
   - CI/CD pipeline summary (mention GitHub Actions, Docker images, infrastructure as code files)  
   - Environment-specific settings or build flags  
1. **API / CLI usage examples** (curl commands, code snippets, or sample responses)  
1. **Troubleshooting & FAQ** (pull common pitfalls from code comments or issue templates)  
1. **Contribution guidelines** (reference `CONTRIBUTING.md` if present; otherwise draft a basic flow)  
1. **License & citation** (detect license file and include SPDX identifier)  
1. **Acknowledgements / credits** (third-party assets, inspirations)  
1. **Badges** (coverage, build status, Docker pulls, etc.—auto-generate markdown using shields.io)

---

📐 **STYLE & FORMAT RULES**

- Use level-1 `#` for the title, then level-2 `##` for main sections.  
- Prefer lists and tables over dense paragraphs when appropriate.  
- For code snippets, detect predominant language and apply fenced-code blocks with syntax highlighting.  
- Inline small diagrams or ASCII trees; link to larger architecture diagrams if they exist.  
- Add `<!-- TODO -->` comments where human owners must fill in details you cannot infer.  
- Ensure the README renders cleanly on GitHub / GitLab (wrap lines ≤ 100 chars, no proprietary markdown).

---

⚙️ **HOW TO WORK**

1. Enumerate all files; pay special attention to:
   - Dependency manifests (`package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, etc.)
   - Configuration (`.env*`, `config/*.yml`), Dockerfiles, and CI workflows.
2. Parse these artifacts to extract package names, version constraints, and commands.
3. Aggregate findings into the sections above.
4. Output ONLY the completed `README.md`—no extra commentary—between triple back-ticks.

```

---

## How to use this prompt

1. **Give the agent access** to the repository (zip upload, Git URL with `--depth 1`, or an internal file-system mount).
1. Paste the full prompt above as the agent’s instruction.
1. Review the generated `README.md`, adjust any TODOs, and commit it.

Feel free to tweak section headings or priorities to match your team’s conventions.
