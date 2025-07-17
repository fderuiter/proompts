# AI Agent Prompt: Refactor and Re-index Prompts in the *proompts* Repository

---

## 1\u00B7 Mission

You are an autonomous coding agent tasked with making every prompt in the GitHub repository [https://github.com/fderuiter/proompts](https://github.com/fderuiter/proompts) concise, well-organized and easy to find.  Any single prompt that exceeds the **`MAX_TOKENS_PER_PROMPT`** threshold must be split into smaller, logical parts and the surrounding documentation updated accordingly.

---

## 2\u00B7 Operational Constraints

| Parameter               | Value                                   | Purpose                                              |
| ----------------------- | --------------------------------------- | ---------------------------------------------------- |
| `REPO_URL`              | `https://github.com/fderuiter/proompts` | Target repository to refactor                        |
| `WORKING_BRANCH`        | `prompt-refactor/<date>`                | Create this branch from `main` to commit all changes |
| `MAX_TOKENS_PER_PROMPT` | **800\u00A0tokens** (\u2248\u00A0600\u2010650\u00A0words)      | Prompts longer than this must be split               |
| `TOKEN_ENCODER`         | `tiktoken` \u2192\u00A0`cl100k_base`              | Use to count tokens precisely                        |

*Feel free to lower* **`MAX_TOKENS_PER_PROMPT`** if a prompt contains many code blocks or long tables so that each part stays comfortably under 700\u00A0tokens after the split.

---

## 3\u00B7 Success Criteria

1. **No prompt file exceeds `MAX_TOKENS_PER_PROMPT`.**
1. **All links resolve** (use the bundled `scripts/validate_markdown.sh`).
1. **`overview.md`, `docs/index.md`, and `docs/table-of-contents.md`** reflect the new file structure.
1. **PR passes CI** and the validation script with zero warnings.

---

## 4\u00B7 Step-by-Step Plan

1. **Setup**

   ```bash
   git clone $REPO_URL && cd proompts
   git checkout -b $WORKING_BRANCH
   ```

1. **Enumerate prompt files**
   ▸ Recursively collect all `*.md` files **excluding**:

   * any `overview.md`
   * any file inside `docs/`
   * `README.md`, `LICENSE.md`, `AGENTS.md`

1. **Detect oversize prompts**
   For every candidate file:

   ```python
   import tiktoken, pathlib, textwrap
   enc = tiktoken.get_encoding('cl100k_base')
   tokens = len(enc.encode(open(path).read()))
   if tokens > MAX_TOKENS_PER_PROMPT:
       mark_for_split(path, tokens)
   ```

1. **Split logically**
   For each oversize file:

   * Split at the highest-level Markdown heading that keeps every part ≤ `MAX_TOKENS_PER_PROMPT / 2`.
   * Name parts `<originalStem>_part-01.md`, `…_part-NN.md`.
   * In each new part add a front-matter banner:

     ```md
     <!--
     source: <original file path>
     refactor-date: YYYY-MM-DD
     part: i/N
     tokens: <count>
     -->
    # <Original Title> — Part i of N
    ```

   * Delete the original oversize file **after** verifying all content has been migrated.

1. **Update directory-level `overview.md`**

   * Append an entry for every new prompt file:

    ```md
    - **<Prompt Title> (Part i/N):** <one-sentence summary>
    ```

   * Keep the file alphabetically (or numerically) sorted.

1. **Update global documentation**

   1. **`docs/index.md`** — this is the published table-of-contents.  Maintain its two-level structure (`## Category` ➜ links).
   1. **`docs/table-of-contents.md`** — if present, mirror the same links (one item per line).  Create it if it doesn’t exist.
   1. Ensure every link uses the relative path *from* the docs folder.

1. **Link rewriting**

   * Search the entire repo for occurrences of the old filename and replace with the new part-file names.
   * Run `scripts/validate_markdown.sh` and fix any broken links.

1. **Commit & Push**

   ```bash
   git add .
   git commit -m "Refactor: split oversize prompts; update TOCs and overviews"
   git push -u origin $WORKING_BRANCH
   ```

1. **Open a Pull Request**

   * Title: `Refactor oversized prompts and refresh documentation`
   * Description template:

     ```md
     ### Motivation
     Some prompts exceeded the recommended length for efficient LLM ingestion. This PR splits them, updates all meta-docs and fixes internal links.

     ### Highlights
     * ✅ All prompts ≤ ${MAX_TOKENS_PER_PROMPT} tokens
     * ✅ `overview.md` files regenerated
     * ✅ `docs/index.md` + `docs/table-of-contents.md` refreshed
     * ✅ CI + Markdown validation pass

     Closes #<issue-number-if-any>
     ```

1. **Post-merge cleanup** (optional)

   * Delete working branch locally and on origin.

---

## 5\u00B7 Quality Checklist (for the Agent)

* [ ] Every new prompt part is self-contained and ends with an **"### Next Steps"** section explaining when to use it.
* [ ] No duplicate anchor text in any markdown heading.
* [ ] Spell-check and lint applied (`mdl`, `markdownlint`).
* [ ] 🚦 CI pipeline shows green before requesting human review.

---

## 6\u00B7 Edge Cases & Tips

* **Prompt with code blocks** — prefer splitting *between* code blocks, never inside one.
* **Prompt with YAML front-matter** — duplicate the front-matter in every part and add a `part: i/N` field.
* **Directories without `overview.md`** — generate one following the style already used in other folders.
* **Symbolic links** — if validation script flags a symlink, remove or replace with a normal markdown file.

---

## 7\u00B7 Deliverables

1. Pull request on GitHub linked above.
1. Summary report in the PR description listing:

   * files split / renamed
   * token counts *before* vs. *after*
   * any additional clean-up performed.

---

## 8\u00B7 Go 🏃

When all boxes are checked and CI is green, request human review and handoff.

*End of prompt.*
