import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2025-07-18"
AUTHOR = "fderuiter"

# Map headings to standardized versions
HEADING_MAP = {
    'goal': 'Purpose',
    'objective': 'Purpose',
    'context / background': 'Context',
    'context': 'Context',
    'background': 'Context',
    'instructions': 'Instructions',
    'additional notes': 'Additional Notes',
    'example usage': 'Example Usage',
    'references': 'References',
}

for d in sorted([p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith('c')]):
    for path in sorted(d.glob('*.md')):
        if path.name.lower() == 'overview.md':
            continue
        text = path.read_text(encoding='utf-8')
        lines = text.splitlines()
        if lines and lines[0].strip() == '---':
            # strip existing front matter
            end = 1
            while end < len(lines) and lines[end].strip() != '---':
                end += 1
            lines = lines[end+1:]
        # remove leading comments
        while lines and lines[0].strip().startswith('<!--'):
            # keep comment after
            lines.pop(0)
        # extract title
        title = None
        body_lines = []
        for line in lines:
            if title is None and line.startswith('#'):
                title = line.lstrip('#').strip()
                continue
            body_lines.append(line)
        if title is None:
            title = path.stem.replace('_', ' ').title()
            body_lines = lines
        # categorize lines by headings
        sections = {}
        current = 'Instructions'
        sections[current] = []
        for line in body_lines:
            m = re.match(r'^##+\s*(.+)', line)
            if m:
                heading = m.group(1).strip().lower()
                heading = HEADING_MAP.get(heading, heading.title())
                current = heading
                sections.setdefault(current, [])
            else:
                sections[current].append(line)
        # ensure all required sections exist
        for h in ['Purpose', 'Context', 'Instructions', 'Inputs', 'Output Format', 'Additional Notes']:
            sections.setdefault(h, [])
        # trim leading/trailing blank lines in each section
        for key, lines_list in sections.items():
            while lines_list and not lines_list[0].strip():
                lines_list.pop(0)
            while lines_list and not lines_list[-1].strip():
                lines_list.pop()
        # try to derive Purpose from first line of Instructions if empty
        if not sections['Purpose'] and sections['Instructions']:
            first_line = ''
            idx = 0
            for i, line in enumerate(sections['Instructions']):
                stripped = line.strip().strip('*').strip('"')
                if stripped:
                    first_line = stripped
                    idx = i
                    break
            if first_line:
                sections['Purpose'] = [first_line]
                sections['Instructions'] = sections['Instructions'][idx+1:]
        # build markdown
        id_ = path.stem.replace('_', '-').lower()
        front_matter = [
            '---',
            f'id: {id_}',
            f'title: {title}',
            f'category: {d.name}',
            f'author: {AUTHOR}',
            f'created: {TODAY}',
            f'last_modified: {TODAY}',
            'tested_model: gpt-4',
            'temperature: 0.2',
            'tags: []',
            '---',
            '',
            f'# {title}',
            ''
        ]
        content_lines = []
        order = ['Purpose', 'Context', 'Instructions', 'Inputs', 'Output Format', 'Additional Notes', 'Example Usage', 'References']
        for h in order:
            if h in sections:
                content_lines.append(f'## {h}')
                if sections[h] and sections[h][0].strip():
                    content_lines.append('')
                content_lines.extend(sections[h])
                content_lines.append('')
        new_text = '\n'.join(front_matter + content_lines).rstrip() + '\n'
        path.write_text(new_text, encoding='utf-8')
        print('Standardized', path)
