import hashlib
import re
from pathlib import Path
from typing import Tuple, Optional, Any, Dict, List

def get_tool_name(path: Path, content: dict) -> Tuple[str, str]:
    """
    Returns (original_name, sanitized_name).
    Handles unified normalization and hashing for truncation.
    """
    name = content.get('name')
    if not name:
        name = path.name.replace(".prompt.yaml", "").replace(".prompt.yml", "").replace(".prompt.md", "")
        
    original_name = name
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    
    if len(name) > 64:
        h = hashlib.md5(str(path).encode()).hexdigest()[:6]
        name = name[:57] + "_" + h
        
    return original_name, name

def get_tool_name_mcp(path: Path, content: dict) -> str:
    """Wrapper that just returns the sanitized name for MCP server."""
    _, sanitized = get_tool_name(path, content)
    return sanitized

def _get_words(text: str) -> set:
    words = set()
    for w in re.findall(r'[a-z]+|[0-9]+', text.lower()):
        if w.isdigit():
            words.add(str(int(w)))
        else:
            words.add(w)
    return words

def resolve_skill_from_path(path: Path, skills_list: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Heuristically (fuzzy) resolve a skill from a prompt file path.
    """
    stem = path.name.replace('.prompt.md', '').replace('.prompt.yml', '').replace('.prompt.yaml', '')
    stem_clean = re.sub(r'^\d+_', '', stem).lower()
    stem_words = _get_words(stem_clean)
    
    best_match = None
    best_score = 0
    best_skill_len = float('inf')
    
    for skill in skills_list:
        skill_name_clean = skill.get("name", "").lower()
        skill_words = _get_words(skill_name_clean)
        
        score = len(stem_words & skill_words)
        if score > best_score or (score > 0 and score == best_score and len(skill_words) < best_skill_len):
            best_score = score
            best_match = skill
            best_skill_len = len(skill_words)
            
    if not best_match or best_score == 0:
        m = re.match(r'^(\d+)_', stem)
        if m:
            idx = int(m.group(1)) - 1
            if 0 <= idx < len(skills_list):
                best_match = skills_list[idx]
                best_score = 1
                
    if best_match and best_score > 0:
        return best_match
    return None
