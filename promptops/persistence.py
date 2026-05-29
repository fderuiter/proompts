import os
import tempfile
import json
from pathlib import Path
from contextlib import contextmanager
from typing import Dict, Any, Union, Iterator

from filelock import FileLock
from ruamel.yaml import YAML


@contextmanager
def update_yaml(file_path: Union[str, Path]) -> Iterator[Dict[str, Any]]:
    """
    A context manager that yields the parsed YAML/JSON object from a file.
    When the context manager exits without exceptions, the modified object 
    is atomically written back to the file, preserving comments and formatting.
    
    File-level locking is enforced to prevent concurrent write issues.
    """
    file_path = Path(file_path)
    lock_path = file_path.with_suffix(file_path.suffix + ".lock")
    
    # We use filelock to ensure safe concurrent operations
    with FileLock(str(lock_path), timeout=60):
        is_json = file_path.name.endswith(".json")
        content = ""
        
        if file_path.exists():
            content = file_path.read_text(encoding="utf-8")
        else:
            content = "{}" if is_json else ""
        
        if is_json:
            data = json.loads(content) if content.strip() else {}
        else:
            yaml = YAML()
            yaml.preserve_quotes = True
            yaml.indent(mapping=2, sequence=4, offset=2)
            yaml.width = 120
            # Ruamel.yaml preserves document separators if explicitly told to based on input
            has_explicit_start = content.startswith("---")
            yaml.explicit_start = has_explicit_start
            
            data = yaml.load(content)
            if data is None:
                data = {}

        # Yield the parsed data to be mutated
        yield data

        # Write to temporary file for atomic replace
        fd, temp_path_str = tempfile.mkstemp(dir=file_path.parent, prefix=file_path.name + ".tmp.")
        temp_path = Path(temp_path_str)
        try:
            with os.fdopen(fd, 'w', encoding='utf-8') as f:
                if is_json:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    f.write("\n")
                else:
                    yaml.dump(data, f)
            
            # Atomic rename (os.replace works on both Windows and Linux)
            os.replace(temp_path, file_path)
        except Exception:
            if temp_path.exists():
                temp_path.unlink()
            raise
