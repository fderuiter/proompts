1. **Dependency Setup**
   - Run `pip install -r requirements.txt` to install Pydantic and other necessary dependencies.
2. **Create New Prompt YAML**
   - Write the highly robust, expert-level prompt `macos_esf_unified_logging_threat_hunter.prompt.yaml` in `prompts/technical/security/secops/`.
3. **Verify File Contents**
   - Read the newly created file using `read_file` to confirm exact contents were written correctly and formatted strictly as YAML.
4. **Validation and Docs Indexing**
   - Run `python3 tools/scripts/validate_prompt_schema.py --strict` to ensure the prompt schema is valid.
   - Run `python3 tools/scripts/update_docs_index.py` followed by `python3 tools/scripts/generate_docs.py` to update the documentation.
5. **Testing**
   - Run `python3 tools/scripts/test_all.py` to ensure all tests pass.
6. **Pre-Commit Checks**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
7. **Local Branch and Commit**
   - Create a local branch `macos-esf-threat-hunter` and commit the repository changes locally, since I am instructed not to use the submit tool.
8. **Final Output**
   - Use `message_user` with `continue_working: False` to output the raw YAML without markdown formatting, starting exactly with "---", fulfilling the strict output constraints.
