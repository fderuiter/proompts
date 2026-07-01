import os
import hashlib
import re
from pathlib import Path
from typing import List, Union, Dict, Any, Optional

from promptops.utils import load_yaml

class AssetRegistry:
    def __init__(self, base_dir: Optional[Union[str, Path]] = None):
        from promptops.utils import ROOT
        self.base_dir = Path(base_dir) if base_dir else ROOT

    def discover_assets(self) -> List[Dict[str, Any]]:
        assets = []
        for root, dirs, files in os.walk(self.base_dir):
            # Exclude hidden directories and special dirs if needed
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__']]
            for file in files:
                if file.startswith('.'):
                    continue
                file_path = Path(root) / file
                
                is_prompt = file.endswith('.prompt.md') or file.endswith('.prompt.yml') or file.endswith('.prompt.yaml')
                is_workflow = file.endswith('.workflow.yaml') or file.endswith('.workflow.yml')
                
                if not (is_prompt or is_workflow):
                    continue

                content = load_yaml(str(file_path))
                if not content:
                    continue
                
                # Derive title
                title = content.get('name')
                if not title:
                    # fallback to filename
                    stem = file_path.name
                    for ext in ['.prompt.md', '.prompt.yml', '.prompt.yaml', '.workflow.yaml', '.workflow.yml']:
                        if stem.endswith(ext):
                            stem = stem[:-len(ext)]
                            break
                    title = stem.replace('_', ' ').title()
                    content['name'] = title
                
                # Assign type
                if is_prompt:
                    content['type'] = 'prompt'
                else:
                    content['type'] = 'workflow'
                
                # Generate ID
                content['id'] = self.generate_id(content['name'])
                content['file_path'] = str(file_path)
                
                # Derive Category
                content['category'] = self.derive_category(content, file_path)

                assets.append(content)
                
        return assets

    def get_parsed_assets(self) -> List[Any]:
        from promptops.validation import PromptSchema, WorkflowSchema
        assets = []
        for data in self.discover_assets():
            asset_type = data.get('type')
            if asset_type == 'prompt':
                assets.append(PromptSchema(**data))
            elif asset_type == 'workflow':
                assets.append(WorkflowSchema(**data))
        return assets

    @staticmethod
    def generate_id(name: str) -> str:
        """Sanitize name and generate consistent ID."""
        sanitized = re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower())
        sanitized = re.sub(r'_+', '_', sanitized).strip('_')
        hash_suffix = hashlib.md5(name.encode()).hexdigest()[:6]
        return f"{sanitized}_{hash_suffix}"

    @staticmethod
    def derive_category(asset_data: Dict[str, Any], file_path: Optional[Path] = None) -> str:
        """Derive consistent category from metadata."""
        metadata = asset_data.get('metadata', {})
        
        # Tags for prompts
        from promptops.tags import extract_tags
        tags = extract_tags(asset_data)
        for tag in tags:
            if tag.lower().startswith('domain:'):
                val = tag.split(':', 1)[1].strip()
                if val:
                    return val.split('/', 1)[0].strip().title()

        if metadata and 'domain' in metadata:
            return metadata['domain'].split('/', 1)[0].strip().title()
        
        if metadata and 'topic' in metadata:
            return metadata['topic'].split('/', 1)[0].strip().title()
            
        if file_path:
            try:
                current = file_path
                while current.parent != current:
                    if current.parent.name in ['prompts', 'workflows']:
                        rel = file_path.relative_to(current.parent)
                        if len(rel.parts) > 1:
                            return rel.parts[0].replace('_', ' ').title()
                        break
                    current = current.parent
            except Exception:
                pass
                
        return 'Uncategorized'
