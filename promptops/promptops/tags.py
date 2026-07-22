"""Module docstring."""
from typing import Dict, Any, List

TAG_ALIASES = {
    "bioskills": "skill",
    "skills": "skill"
}

def normalize_tag(tag: str) -> str:
    """Normalize a tag by lowercasing, stripping whitespace, and resolving aliases."""
    normalized = tag.lower().strip()
    return TAG_ALIASES.get(normalized, normalized)

def extract_tags(content: Dict[str, Any]) -> List[str]:
    """Extract tags from a parsed YAML/JSON dict, merging legacy and metadata tags."""
    if not content or not isinstance(content, dict):
        return []

    tags_set = set()

    # Legacy tags
    legacy_tags = content.get("tags")
    if isinstance(legacy_tags, list):
        for t in legacy_tags:
            if isinstance(t, str):
                tags_set.add(normalize_tag(t))

    # Metadata tags
    metadata = content.get("metadata")
    if isinstance(metadata, dict):
        meta_tags = metadata.get("tags")
        if isinstance(meta_tags, list):
            for t in meta_tags:
                if isinstance(t, str):
                    tags_set.add(normalize_tag(t))

        domain = metadata.get("domain")
        if isinstance(domain, str) and domain.strip():
            tags_set.add(normalize_tag(f"domain:{domain}"))

        topic = metadata.get("topic")
        if isinstance(topic, str) and topic.strip():
            tags_set.add(normalize_tag(f"topic:{topic}"))

    # Return valid tags, omitting empty ones
    return sorted(list(t for t in tags_set if t))

def extract_tags_from_text(raw_text: str) -> List[str]:
    """Fallback extraction of tags from raw text if parsing fails. 
    It will look for aliases as well."""
    if not raw_text:
        return []
    
    tags_set = set()
    raw_lower = raw_text.lower()
    
    # We can check for known tags and aliases in the raw text
    for alias, canonical in TAG_ALIASES.items():
        if alias in raw_lower:
            tags_set.add(canonical)
    
    # Also check for "skill" itself
    if "skill" in raw_lower:
        tags_set.add("skill")
        
    # We could do a regex to extract tags if they are structured like `tags: [...]` but 
    # for now we're mostly concerned with detecting `skill` and its variants for fallback.
    return sorted(list(tags_set))
