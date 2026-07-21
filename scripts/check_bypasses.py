#!/usr/bin/env python3
import sys
import re

def main():
    files = sys.argv[1:]
    has_errors = False

    # Exempt promptops/utils.py which provides the shared core utilities
    exempt_files = ['promptops/promptops/utils.py']

    banned_patterns = [
        (r'\bos\.walk\s*\(', "os.walk"),
        (r'\byaml\.safe_load\s*\(', "yaml.safe_load"),
        (r'\byaml\.load\s*\(', "yaml.load"),
    ]

    for file_path in files:
        # Check if file is exempted
        if any(file_path.endswith(ef) for ef in exempt_files):
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception:
            continue

        for i, line in enumerate(lines):
            for pattern, name in banned_patterns:
                if re.search(pattern, line):
                    print(f"Error: {file_path}:{i+1} uses prohibited function '{name}'. "
                          "Please use unified workspace utilities (e.g. walk_workspace, load_yaml) instead.")
                    has_errors = True

    if has_errors:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
