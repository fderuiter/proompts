#!/usr/bin/env python3
"""Search prompts by keyword."""

import argparse
from pathlib import Path
import sys

try:
    from utils import ROOT, iter_prompt_files, load_yaml
except ImportError:
    sys.path.append(str(Path(__file__).parent))
    from utils import ROOT, iter_prompt_files, load_yaml

def search(query: str, verbose: bool = False):
    query = query.lower()
    found = 0
    for path in iter_prompt_files(ROOT):
        content = load_yaml(path)
        name = content.get('name', '').lower()
        description = content.get('description', '').lower()

        if query in name or query in description:
            found += 1
            print(f"Match: {content.get('name')} ({path.relative_to(ROOT)})")
            if verbose and content.get('description'):
                 print(f"  Description: {content.get('description')}")
            if verbose:
                print()

    if found == 0:
        print(f"No prompts found matching '{query}'.")

def main():
    parser = argparse.ArgumentParser(description="Search prompts by keyword")
    parser.add_argument("query", help="Keyword to search for")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show description")
    args = parser.parse_args()

    search(args.query, args.verbose)

if __name__ == "__main__":
    main()
