import os
from pathlib import Path
import yaml

PROMPTS_DIR = Path("prompts").resolve()

def process_directory(directory):
    # Collect all prompts in this exact directory (not recursive)
    prompts = list(directory.glob("*.prompt.yaml")) + list(directory.glob("*.prompt.yml"))
    if not prompts:
        return
    
    # Find the most common modelParameters
    param_counts = {}
    param_repr_to_dict = {}
    
    for p in prompts:
        with open(p, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            
        params = data.get("modelParameters")
        if params is not None and isinstance(params, dict):
            # Normalize to compare
            repr_str = str(sorted(params.items()))
            param_counts[repr_str] = param_counts.get(repr_str, 0) + 1
            param_repr_to_dict[repr_str] = params
            
    if not param_counts:
        return
        
    # Find the one that appears most often (and at least > 1 to be worth a default?)
    # Actually, even if it's 1, if it's the only one, maybe? Let's just find the max.
    best_repr = max(param_counts, key=param_counts.get)
    best_params = param_repr_to_dict[best_repr]
    
    # Only create defaults if it saves lines? 
    # Yes, if param_counts[best_repr] > 1, or if we just want to centralize.
    # Let's write it to defaults.yaml
    defaults_file = directory / "defaults.yaml"
    existing_defaults = {}
    if defaults_file.exists():
        with open(defaults_file, "r", encoding="utf-8") as f:
            existing_defaults = yaml.safe_load(f) or {}
            
    # We will merge into defaults file or create it
    if "modelParameters" not in existing_defaults:
        existing_defaults["modelParameters"] = best_params
        
    # Wait, the inheritance says prompts adopt "model parameters defined in their containing directory".
    # In utils.py I implemented deep_merge.
    # What does the defaults.yaml look like? Should it be `modelParameters: { ... }` or just the parameters themselves?
    # "A prompt file with no modelParameters section successfully loads defaults from its parent directory"
    # This implies the defaults.yaml provides `modelParameters` key. So `{"modelParameters": {...}}`.
    
    with open(defaults_file, "w", encoding="utf-8") as f:
        yaml.dump(existing_defaults, f, default_flow_style=False, sort_keys=False)
        
    # Now remove from prompts that match exactly
    best_params_cmp = existing_defaults.get("modelParameters", {})
    
    for p in prompts:
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
            data = yaml.safe_load(content) or {}
            
        params = data.get("modelParameters")
        if params == best_params_cmp:
            # We can remove modelParameters
            # Let's remove it using regex to preserve comments, or yaml dumper.
            # PyYAML removes comments. Let's try to remove it as a block.
            del data["modelParameters"]
            with open(p, "w", encoding="utf-8") as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False)

for root, dirs, files in os.walk(PROMPTS_DIR):
    process_directory(Path(root))

print("Migration completed.")
