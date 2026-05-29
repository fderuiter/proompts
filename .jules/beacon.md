# BEACON'S JOURNAL

## Learning 1: Documentation Generation
Generated docs are build artifacts and must not be committed to git. They are placed in the `docs/` directory. Static guides (like `USAGE.md`, `BEST_PRACTICES.md`) are manually maintained, while prompt/workflow documentation (like `docs/clinical.md`, `docs/workflows/`) are generated automatically by `engine/scripts/generate_docs.py` and `engine/scripts/update_docs_index.py`. The `enforce_generated_docs_untracked` check in `test_all.py` ensures these artifacts are ignored. This is an important consideration when modifying the docs section.

## Learning 2: Workflow Simulation
The `run_workflow.py` script executes workflow simulation using mock data in the `testData` array of a prompt definition. This relies on string mapping inputs via the `map_inputs` of a workflow, evaluating them against the prompt `testData` expected inputs. If missing, it outputs a generic string or falls back to the first available expected output.

## Learning 3: Taxonomy
A tag taxonomy `domain:<value>` exists for defining domain mappings within prompts. If present in `tags` or `metadata.tags`, it guides documentation generation instead of relying on the strict directory hierarchy.

## Learning 4: Broken links validation
Links validation is tested under `engine/scripts/check_broken_links.py`. Broken links are disallowed in the PRs according to rules of Beacon.

## Gap: Missing `tools/README.md` and Unclear Link in `README.md`
The root `README.md` links to `tools/overview.md` but lists it as `tools/` with a broken context, missing a `README.md`. Adding a `README.md` to `tools/` that properly guides the user and aligns with the expected repository UI format would reduce cognitive load. Also, in `README.md`:
| **[`tools/`](tools/overview.md)** | **The Engine Room.** <br> Utilities for maintenance and development. | [`scripts/`](engine/scripts/README.md) (Python), [`prompt_tools/`](engine/prompt_tools/README.md) (Meta-prompts) |
This should link to `tools/README.md` or keep it consistent. A `README.md` is more standard than `overview.md` for top-level folders unless part of the `check_prompts` verification, which checks prompt/workflow folders, but `tools/` is an auxiliary script folder. Let's create `tools/README.md` (or rename `tools/overview.md` to `tools/README.md`) and update links. However, I should check the `check_prompts` tool again. Actually, `check_prompts.py` only validates `prompts/` and `workflows/`.
