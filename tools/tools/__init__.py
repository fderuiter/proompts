import re

def optimize_prompt(text: str) -> str:
    """
    Simulates the Prompt Optimizer locally without network calls.
    Returns an optimized version of the input text.
    """
    if not text:
        return text
    # A simple mock optimization logic: capitalize the first letter, strip extra whitespace, etc.
    optimized = text.strip()
    return f"{optimized}\n\n# Note: Optimized for clarity and instruction following."

def sanitize_prompt(text: str) -> str:
    """
    Simulates the Prompt Sanitiser locally without network calls.
    Removes sensitive placeholders and formatting issues.
    """
    if not text:
        return text
    # Sanitize URLs
    text = re.sub(r'https?://[^\s]+', '[REDACTED_URL]', text)
    # Sanitize typical secrets or API keys patterns
    text = re.sub(r'(?i)(api[_-]?key)\s*[:=]\s*[A-Za-z0-9_-]+', r'\1=[REDACTED_SECRET]', text)
    text = re.sub(r'(?i)(password)\s*[:=]\s*[A-Za-z0-9_-]+', r'\1=[REDACTED_SECRET]', text)
    # Sanitize markdown source citations e.g., [1]
    text = re.sub(r'\[\d+\]', '', text)
    return text.strip()
