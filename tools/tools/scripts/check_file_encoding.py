import ast
import os
import sys

def check_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    
    try:
        tree = ast.parse(source, filename=filepath)
    except SyntaxError as e:
        return [(-1, f'SYNTAX_ERROR: {e}')]

    errors = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                func_name = node.func.attr
            else:
                continue

            if func_name in ("open", "read_text", "write_text"):
                # Check for binary mode in open()
                is_binary = False
                if func_name == "open":
                    if isinstance(node.func, ast.Name):
                        if len(node.args) >= 2:
                            mode_arg = node.args[1]
                            if isinstance(mode_arg, ast.Constant) and isinstance(mode_arg.value, str):
                                if 'b' in mode_arg.value:
                                    is_binary = True
                    elif isinstance(node.func, ast.Attribute):
                        for arg in node.args[:2]:
                            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                                if 'b' in arg.value and all(c in 'rwax+btU' for c in arg.value):
                                    is_binary = True
                    
                    # Check keyword arg for mode
                    for kw in node.keywords:
                        if kw.arg == "mode":
                            if isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
                                if 'b' in kw.value.value:
                                    is_binary = True

                if is_binary:
                    continue
                
                # Check for encoding keyword
                has_encoding = False
                for kw in node.keywords:
                    if kw.arg == "encoding":
                        has_encoding = True
                        break
                        
                if not has_encoding:
                    errors.append((node.lineno, func_name))
                    
    return errors

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    ignore_dirs = {".venv", "venv", ".git", "__pycache__", ".tox", ".pytest_cache", "build", "dist"}
    
    all_errors = {}
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                errors = check_file(filepath)
                if errors:
                    all_errors[filepath] = errors
                    
    if all_errors:
        print("ERROR: Found file opening calls without explicit encoding parameter:")
        for filepath, errors in all_errors.items():
            rel_path = os.path.relpath(filepath, root_dir)
            for lineno, func_name in errors:
                print(f"  {rel_path}:{lineno} - {func_name}()")
        print("\nAll text file operations must explicitly specify encoding (e.g., encoding='utf-8').")
        sys.exit(1)
    else:
        print("All file encoding checks passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
