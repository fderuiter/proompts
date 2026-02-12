
#!/usr/bin/env python3
"""
Script to fix variable descriptions in prompt YAML files.
It replaces stub descriptions (e.g., descriptions that are just `{{variable_name}}`)
with human-readable descriptions derived from the variable name.
"""

import os
import re
import sys

def fix_prompts(directory):
    files_modified = 0
    files_checked = 0

    # Regex to find variable name definition: - name: variable_name
    # Captures indentation, "- name: ", quote (optional), variable name, closing quote (optional)
    name_pattern = re.compile(r"^(\s*-\s*name:\s*)(['\"]?)([^'\"]+)\2\s*$")

    # Regex to find start of a list item: - ...
    list_item_pattern = re.compile(r"^\s*-\s+.*")

    # Regex to find description stub: description: ...{{...}}...
    # Must be indented. Capture the prefix (indentation + "description: ") and the value
    desc_stub_pattern = re.compile(r"^(\s+description:\s*)(.*\{\{.*\}\}.*)$")

    # Regex for root keys (start of line, no indent)
    root_key_pattern = re.compile(r"^[a-zA-Z0-9_]+:")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml'):
                filepath = os.path.join(root, file)
                files_checked += 1

                try:
                    with open(filepath, 'r') as f:
                        lines = f.readlines()

                    new_lines = []
                    current_variable_name = None
                    file_modified = False

                    for line in lines:
                        # Check for root key -> reset context
                        if root_key_pattern.match(line):
                            current_variable_name = None
                            new_lines.append(line)
                            continue

                        # Check for name definition
                        name_match = name_pattern.match(line)
                        if name_match:
                            current_variable_name = name_match.group(3) # Group 3 is the name
                            new_lines.append(line)
                            continue

                        # Check for any new list item (to reset context if name not found)
                        if list_item_pattern.match(line):
                            # If we are here, it's a list item but NOT a name definition (checked above)
                            current_variable_name = None
                            new_lines.append(line)
                            continue

                        # Check for description stub
                        desc_match = desc_stub_pattern.match(line)
                        if desc_match and current_variable_name:
                            prefix = desc_match.group(1) # e.g. "  description: "

                            # Generate human readable description from current_variable_name
                            # Strip quotes if present in name (though regex should handle outer quotes)
                            clean_name = current_variable_name.strip()

                            human_name = clean_name.replace('_', ' ').replace('-', ' ').replace('/', ' ').strip()
                            if human_name:
                                # Start with uppercase
                                human_name = human_name[0].upper() + human_name[1:]

                            # Construct new line
                            new_desc_text = f"The {human_name}"
                            new_line = f"{prefix}{new_desc_text}\n"

                            # Log change
                            print(f"File: {filepath}")
                            print(f"  Var: {current_variable_name}")
                            print(f"  Old: {line.strip()}")
                            print(f"  New: {new_line.strip()}")

                            new_lines.append(new_line)
                            file_modified = True
                        else:
                            new_lines.append(line)

                    if file_modified:
                        with open(filepath, 'w') as f:
                            f.writelines(new_lines)
                        files_modified += 1
                        print(f"Modified: {filepath}")

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

    print(f"Checked {files_checked} files.")
    print(f"Modified {files_modified} files.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "prompts"

    print(f"Scanning directory: {directory}")
    fix_prompts(directory)
