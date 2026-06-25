import os
import re

for root, dirs, files in os.walk('prompts'):
    for file in files:
        if file.endswith('.yaml') or file.endswith('.md'):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()

            if '{"error": "unsafe"}' in content:
                original_content = content
                
                # First, if it's a prompt file and the import is not present, add it
                if "{% import 'common/macros.j2' as macros %}" not in content:
                    content = "{% import 'common/macros.j2' as macros %}\n" + content
                
                # Replace regex versions first
                content = content.replace(r'\{"error": "unsafe"\}', '{{ macros.safety_refusal_regex() }}')
                
                # Replace normal versions
                content = content.replace('{"error": "unsafe"}', '{{ macros.safety_refusal() }}')
                
                if content != original_content:
                    with open(path, 'w') as f:
                        f.write(content)
                    print(f"Refactored {path}")
