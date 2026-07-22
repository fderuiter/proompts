import os
import sys
from pathlib import Path

from promptops.engine import simulate_prompt_execution, run_workflow
from promptops.utils import ROOT, iter_markdown_files, load_yaml
from promptops.validation import analyze_workflow_dependencies

class CodeBlock:
    def __init__(self, lang, code):
        self.lang = lang
        self.code = code

def parse_markdown_ast(text):
    lines = text.split('\n')
    ast_nodes = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        
        if stripped.lower().startswith("```"):
            lang_part = stripped[3:].strip()
            lang = lang_part.split()[0].lower() if lang_part else ""
            i += 1
            code_lines = []
            while i < len(lines):
                end_line = lines[i].lstrip()
                if end_line.startswith("```"):
                    break
                code_lines.append(lines[i])
                i += 1
            ast_nodes.append(CodeBlock(lang, "\n".join(code_lines)))
        i += 1
    return ast_nodes

def main():
    docs_dir = ROOT / "docs"
    md_files = [f for f in iter_markdown_files(docs_dir) if "skills" not in f.parts]
    
    has_errors = False
    
    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8')
        ast_nodes = parse_markdown_ast(content)
        snippets = [node.code for node in ast_nodes if node.lang == 'yaml']
        
        for idx, snippet in enumerate(snippets):
            try:
                tmp_file = md_file.parent / f"tmp_snippet_{idx}.yaml"
                tmp_file.write_text(snippet, encoding='utf-8')
                
                try:
                    parsed = load_yaml(tmp_file)
                    if not isinstance(parsed, dict):
                        print(f"❌ Error in snippet {idx} of {md_file.relative_to(ROOT)}: Snippet must be a dictionary.")
                        has_errors = True
                        continue
                    
                    name = parsed.get("name", "Unknown")
                    
                    if "steps" in parsed:
                        test_data = parsed.get("testData", [])
                        if not test_data:
                            print(f"❌ Error in snippet {idx} of {md_file.relative_to(ROOT)} ({name}): Empty test data.")
                            has_errors = True
                            continue

                        try:
                            issues = analyze_workflow_dependencies(str(tmp_file), parsed, str(ROOT))
                            if issues:
                                if name == "Loop Prevention Demo" and any("Cyclic dependency" in issue for issue in issues):
                                    print(f"✅ Snippet '{name}' correctly triggered static cycle detection.")
                                    continue
                                print(f"❌ Error in snippet {idx} of {md_file.relative_to(ROOT)} ({name}): Static analysis issues:")
                                for issue in issues:
                                    print(f"  - {issue}")
                                has_errors = True
                                continue

                            for test_case in test_data:
                                inputs = test_case.get("inputs", test_case.get("vars", {}))
                                if not inputs and "input" in test_case:
                                    inputs = {"input": test_case["input"]} if isinstance(test_case["input"], str) else test_case["input"]
                                if not inputs:
                                    inputs = {k: v for k, v in test_case.items() if k not in ["expected", "mock_evaluator_results"]}
                                
                                try:
                                    run_workflow(str(tmp_file), inputs, verbose=False, strict_mode=True)
                                except Exception as loop_e:
                                    if "Loop Limit Exceeded" in str(loop_e) and name == "Loop Prevention Demo":
                                        print(f"✅ Snippet '{name}' correctly triggered Loop Limit Exceeded.")
                                    else:
                                        raise loop_e
                        except Exception as e:
                            print(f"❌ Error running workflow snippet {idx} of {md_file.relative_to(ROOT)} ({name}): {e}")
                            has_errors = True
                            
                    elif "messages" in parsed:
                        test_data = parsed.get("testData", [])
                        if not test_data:
                            print(f"❌ Error in snippet {idx} of {md_file.relative_to(ROOT)} ({name}): Empty test data.")
                            has_errors = True
                            continue

                        for test_case in test_data:
                            inputs = test_case.get("inputs", test_case.get("vars", {}))
                            if not inputs and "input" in test_case:
                                inputs = {"input": test_case["input"]} if isinstance(test_case["input"], str) else test_case["input"]
                            if not inputs:
                                inputs = {k: v for k, v in test_case.items() if k not in ["expected", "mock_evaluator_results"]}
                                    
                            simulate_prompt_execution(parsed, inputs, strict_mode=True)
                finally:
                    tmp_file.unlink()
            except Exception as e:
                print(f"❌ Error in snippet {idx} of {md_file.relative_to(ROOT)} ({name if 'name' in locals() else 'Unknown'}): {e}")
                has_errors = True

    if has_errors:
        sys.exit(1)
    else:
        print("✅ All docs snippets passed simulation.")

if __name__ == "__main__":
    main()
