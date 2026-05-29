#!/usr/bin/env python3
import sys
from promptops.validation import validate_prompts

def main():
    try:
        validate_prompts("/app", strict=True)
        print("All prompts validated successfully.")
        return 0
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
