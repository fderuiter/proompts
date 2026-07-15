import os
import re
import yaml
import sys
from pathlib import Path

from promptops.engine import simulate_prompt_execution, run_workflow
from promptops.utils import ROOT

def main():
    docs_dir = ROOT / "docs"
    md_files = list(docs_dir.rglob("*.md"))
    
    yaml_pattern = re.compile(r'```yaml\n(.*?)\n```', re.DOTALL)
    
    has_errors = False
    
    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8')
        snippets = yaml_pattern.findall(content)
        
        for idx, snippet in enumerate(snippets):
            try:
                parsed = yaml.safe_load(snippet)
                if not isinstance(parsed, dict):
                    continue
                
                name = parsed.get("name", "Unknown")
                
                if "steps" in parsed:
                    test_data = parsed.get("testData", [])
                    tmp_file = md_file.parent / f"tmp_snippet_{idx}.workflow.yaml"
                    tmp_file.write_text(snippet, encoding='utf-8')
                    
                    try:
                        inputs = {}
                        if test_data:
                            test_case = test_data[0]
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
                    finally:
                        tmp_file.unlink()
                        
                elif "messages" in parsed:
                    if "testData" in parsed and len(parsed["testData"]) > 0:
                        test_case = parsed["testData"][0]
                        inputs = test_case.get("inputs", test_case.get("vars", {}))
                        if not inputs and "input" in test_case:
                            inputs = {"input": test_case["input"]} if isinstance(test_case["input"], str) else test_case["input"]
                        if not inputs:
                            inputs = {k: v for k, v in test_case.items() if k not in ["expected", "mock_evaluator_results"]}
                                
                        simulate_prompt_execution(parsed, inputs, strict_mode=True)
            except Exception as e:
                print(f"❌ Error in snippet {idx} of {md_file.relative_to(ROOT)} ({name}): {e}")
                has_errors = True

    if has_errors:
        sys.exit(1)
    else:
        print("✅ All docs snippets passed simulation.")

if __name__ == "__main__":
    main()
