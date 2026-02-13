#!/usr/bin/env python3
import os
import yaml
import re
import shutil
import argparse
from collections import defaultdict

# Regex for finding prompt_file in workflow yaml (to preserve comments)
PROMPT_FILE_REGEX = re.compile(r'(prompt_file:\s*["\']?)([^"\']+)(["\']?)')

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def get_all_prompts(prompts_dir):
    all_prompts = set()
    for root, dirs, files in os.walk(prompts_dir):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                all_prompts.add(os.path.abspath(os.path.join(root, file)))
    return all_prompts

def get_workflow_definitions(workflows_dir):
    definitions = []
    
    for root, dirs, files in os.walk(workflows_dir):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                path = os.path.join(root, file)
                try:
                    data = load_yaml(path)
                    if not data or 'steps' not in data:
                        continue
                    
                    workflow_name = os.path.splitext(file)[0]
                    if workflow_name.endswith('.workflow'):
                        workflow_name = workflow_name.replace('.workflow', '')
                        
                    definitions.append({
                        'path': os.path.abspath(path),
                        'name': workflow_name,
                        'steps': data['steps']
                    })
                except Exception as e:
                    print(f"Error parsing workflow {path}: {e}")
                    
    return definitions

def plan_refactoring(prompts_root, workflows_root):
    # 1. Identify Workflow Prompts
    workflow_prompts = defaultdict(list) # path -> list of (workflow_path, step_index)
    definitions = get_workflow_definitions(workflows_root)
    
    schema_map = {} # workflow_path -> list of transformations (old_prompt_path, new_prompt_path)
    
    for wf in definitions:
        wf_path = wf['path']
        wf_name = wf['name']
        
        # Determine target folder for this workflow
        # Heuristic: Find common parent of prompts used in this workflow
        # If prompts are scattered, use the parent of the first prompt
        
        used_prompts = []
        for idx, step in enumerate(wf['steps']):
            if 'prompt_file' in step:
                p_path = os.path.abspath(os.path.join(os.getcwd(), step['prompt_file']))
                if os.path.exists(p_path):
                    used_prompts.append((idx, p_path))
                    workflow_prompts[p_path].append(wf_path)
        
        if not used_prompts:
            continue
            
        # Determine target directory
        # We want: prompts/CATEGORY/WORKFLOW_NAME_workflow/
        # Let's take the directory of the first prompt as the 'category' root
        first_prompt_dir = os.path.dirname(used_prompts[0][1])
        
        # Check if already in a workflow folder
        current_folder_name = os.path.basename(first_prompt_dir)
        if current_folder_name.endswith('_workflow'):
             target_dir = first_prompt_dir # Already correct?
        else:
             target_folder_name = f"{wf_name}_workflow" if not wf_name.endswith('_workflow') else wf_name
             target_dir = os.path.join(first_prompt_dir, target_folder_name)

        # Plan moves
        for step_idx, (original_idx, p_path) in enumerate(used_prompts):
            # New filename: 01_OldName.yaml (stripped of old number)
            old_filename = os.path.basename(p_path)
            # Strip existing numbers if any
            clean_name = re.sub(r'^\d+_', '', old_filename)
            new_filename = f"{step_idx + 1:02d}_{clean_name}"
            
            new_path = os.path.join(target_dir, new_filename)
            
            # Record transformation
            if p_path not in schema_map:
                 schema_map[p_path] = {'new_path': new_path, 'workflow': wf_path}
            else:
                 # Conflict! File used in multiple workflows?
                 if schema_map[p_path]['new_path'] != new_path:
                     print(f"WARNING: Prompt {p_path} used in multiple workflows with different targets. Skipping move.")
                     del schema_map[p_path] 
                     # Also remove from workflow_prompts so it doesn't get processed
                     
    # 2. Identify Meta Prompts
    meta_dir = os.path.join(prompts_root, 'meta')
    meta_moves = {}
    if os.path.exists(meta_dir):
        meta_target_dir = os.path.join(meta_dir, 'meta_prompt_chain')
        for file in os.listdir(meta_dir):
            if file.startswith('L') and file.endswith(('.yaml', '.yml')):
                # It's a meta prompt (L1_..., L2_...)
                # Check level
                match = re.match(r'L(\d+)_', file)
                if match:
                    level = int(match.group(1))
                    # Move to meta_prompt_chain/0{level}_L{level}_...
                    new_filename = f"{level:02d}_{file}"
                    old_path = os.path.join(meta_dir, file)
                    new_path = os.path.join(meta_target_dir, new_filename)
                    meta_moves[old_path] = new_path

    # 3. Identify Standalone Prompts
    standalone_moves = {}
    all_prompts = get_all_prompts(prompts_root)
    
    # helper to check if path is in schema_map or meta_moves
    moved_paths = set(schema_map.keys()) | set(meta_moves.keys())
    
    for p_path in all_prompts:
        if p_path in moved_paths:
            continue
            
        # Check if it has a number to strip
        filename = os.path.basename(p_path)
        if re.match(r'^\d+_', filename):
            # It's numbered but not in a workflow! Strip it.
            clean_name = re.sub(r'^\d+_', '', filename)
            new_path = os.path.join(os.path.dirname(p_path), clean_name)
            if new_path != p_path:
                standalone_moves[p_path] = new_path

    return schema_map, meta_moves, standalone_moves

def fix_references(prompts_root, workflows_root, dry_run=False):
    print("=== Fixing Workflow References ===")
    definitions = get_workflow_definitions(workflows_root)
    
    for wf in definitions:
        wf_path = wf['path']
        wf_name = wf['name']
        print(f"Checking {wf_name}...")
        
        updates = []
        
        # Calculate expected locations
        # We need to guess the target directory. 
        # Since files are already moved, we can't reliably "find" the common parent of old files.
        # But we can try to find where the files ARE now.
        
        # Strategy: Look at the OLD paths in the yaml.
        # Deduce where they SHOULD be.
        
        # Problem: We need the grouping to find the target folder IF the old paths are scattered.
        # But assuming the refactor logic from before:
        # Target dir was based on the first prompt's directory.
        
        with open(wf_path, 'r') as f:
            content = f.read()
            
        # We parse the file manually to find prompt_files because we want the raw string content
        # PROMPT_FILE_REGEX = re.compile(r'(prompt_file:\s*["\']?)([^"\']+)(["\']?)')
        matches = list(PROMPT_FILE_REGEX.finditer(content))
        
        # Groups: 1=prefix, 2=path, 3=suffix
        
        # We also need to process them in order to match the Step Index logic (01, 02...)
        # The YAML 'steps' list order usually matches the file order, but let's rely on the parsed 'steps' from definitions
        # which is safer.
        
        current_steps = wf['steps']
        
        # We unfortunately need to map the steps to the matches in the file.
        # The file content matches might be in order.
        
        # Let's iterate over the parsed steps, calculate the expected new path, and check if it exists.
        
        for idx, step in enumerate(current_steps):
            if 'prompt_file' not in step:
                continue
                
            old_rel_path = step['prompt_file']
            old_abs_path = os.path.abspath(old_rel_path)
            
            if os.path.exists(old_abs_path):
                continue # Path is valid, nothing to do
                
            # Path doesn't exist. Let's guess where it went.
            # Logic: prompts/CATEGORY/SUBDIR/07_name.yaml -> prompts/CATEGORY/SUBDIR/workflow_workflow/01_name.yaml
            
            # 1. Determine Category/Subdir
            # We can't know for sure where it WAS if we only have relative path like "prompts/clinical/protocol/..."
            # valid assumption: properties of the path string
            
            prompt_dir = os.path.dirname(old_rel_path) # e.g. prompts/clinical/protocol
            filename = os.path.basename(old_rel_path)   # e.g. 07_usdm_stage1.yaml
            
            # Workflow folder name logic
            target_folder_name = f"{wf_name}_workflow" if not wf_name.endswith('_workflow') else wf_name
            
            # Construct candidate new path
            # strip number
            clean_name = re.sub(r'^\d+_', '', filename)
            new_filename = f"{idx + 1:02d}_{clean_name}"
            
            # Candidate 1: Nested in workflow folder
            candidate_rel_path = os.path.join(prompt_dir, target_folder_name, new_filename)
            candidate_abs_path = os.path.abspath(candidate_rel_path)
            
            if os.path.exists(candidate_abs_path):
                # Found it!
                updates.append((old_rel_path, candidate_rel_path))
                continue
                
            # Candidate 2: Maybe it was already correctly numbered/named or logic was slightly different?
            # E.g. meta prompts moved to meta/meta_prompt_chain/
            if 'prompts/meta/' in old_rel_path:
                 # Check meta logic
                 # L1_... -> meta_prompt_chain/01_L1_...
                 # Extract level
                 mm = re.match(r'L(\d+)_', filename)
                 if mm:
                     level = int(mm.group(1))
                     meta_new_filename = f"{level:02d}_{filename}"
                     meta_rel_path = os.path.join('prompts/meta/meta_prompt_chain', meta_new_filename)
                     if os.path.exists(os.path.abspath(meta_rel_path)):
                         updates.append((old_rel_path, meta_rel_path))
                         continue

        if updates:
            print(f"Fixing {len(updates)} references in {wf_name}")
            if not dry_run:
                new_content = content
                for old_p, new_p in updates:
                    # We need to be careful replacing. The old_p string should be unique enough?
                    # or use the regex approach again but carefully.
                    
                    # Simple string replace might be dangerous if substrings overlap matches?
                    # using regex replace with strict matching on the specific value found
                    
                    # Pattern: prompt_file: ["']old_p["']
                    # We construct a specific regex for this replacement
                    escaped_old_p = re.escape(old_p)
                    pattern = re.compile(r'(prompt_file:\s*["\']?)' + escaped_old_p + r'(["\']?)')
                    new_content = pattern.sub(r'\1' + new_p + r'\2', new_content)
                
                with open(wf_path, 'w') as f:
                    f.write(new_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help="Print actions without executing")
    parser.add_argument('--fix-refs', action='store_true', help="Fix broken references only")
    args = parser.parse_args()
    
    prompts_root = os.path.abspath("prompts")
    workflows_root = os.path.abspath("workflows")
    
    if args.fix_refs:
        fix_references(prompts_root, workflows_root, dry_run=args.dry_run)
    else:
        schema_map, meta_moves, standalone_moves = plan_refactoring(prompts_root, workflows_root)
        if not schema_map and not meta_moves and not standalone_moves:
             print("No moves planned. Did you mean to run --fix-refs?")
        else:
             apply_changes(schema_map, meta_moves, standalone_moves, dry_run=args.dry_run)

