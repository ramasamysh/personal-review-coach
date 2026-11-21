#!/usr/bin/env python3
"""Portable stdlib-only structure check; does not execute an LLM."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = [
    '.claude-plugin/plugin.json', 'README.md', 'CHANGELOG.md',
    'skills/annual-review/SKILL.md',
    'skills/annual-review/references/evidence-ledger.md',
    'skills/annual-review/references/compare-years.md',
    'skills/annual-review/references/goal-history.md',
    'skills/annual-review/references/storage-and-state.md',
    'skills/annual-review/templates/evidence.md',
    'skills/annual-review/templates/goal-history.md',
    'skills/annual-review/templates/comparison.md',
    'skills/quarterly-check-in/SKILL.md',
    'skills/quarterly-check-in/references/quarterly-protocol.md',
    'skills/quarterly-check-in/templates/quarterly-check-in.md',
]
errors = []
for rel in EXPECTED:
    if not (ROOT / rel).is_file():
        errors.append('Missing file: ' + rel)

if not errors:
    manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
    if manifest.get('name') != 'personal-review-coach' or manifest.get('version') != '0.3.0':
        errors.append('Unexpected manifest name/version')

    for skill in sorted((ROOT / 'skills').glob('*/SKILL.md')):
        data = skill.read_text()
        if not data.startswith('---\n') or len(data.split('---', 2)) < 3:
            errors.append(f'{skill}: missing YAML frontmatter')
        for field in ('name:', 'description:'):
            if field not in data.split('---', 2)[1]:
                errors.append(f'{skill}: frontmatter missing {field}')
        if '$ARGUMENTS' in data or '${CLAUDE_SKILL_DIR}' in data:
            # The core skill can mention these explicitly as forbidden examples.
            if 'Do not rely on' not in data:
                errors.append(f'{skill}: platform-specific token detected')

    # Verify literal relative link paths only; ignore external URLs and placeholders.
    for path in (ROOT / 'skills').rglob('*.md'):
        data = path.read_text()
        for dest in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', data):
            if re.match(r'^(https?://|mailto:|#)', dest):
                continue
            target = (path.parent / dest).resolve()
            if not target.exists() or not target.is_relative_to(ROOT):
                errors.append(f'{path.relative_to(ROOT)} broken/escaped link: {dest}')

    annual = (ROOT / 'skills/annual-review/SKILL.md').read_text()
    quarterly = (ROOT / 'skills/quarterly-check-in/SKILL.md').read_text()
    for phrase in ('compare OLDER_YEAR NEWER_YEAR', 'history PLANNING_YEAR', 'evidence YEAR'):
        if phrase not in annual:
            errors.append('Missing annual action ' + phrase)
    for phrase in ('explicit approval', 'check-in', 'goal-history.md'):
        if phrase not in quarterly:
            errors.append('Quarterly requirement not found: ' + phrase)

if errors:
    print('FAIL:', *errors, sep='\n- ')
    sys.exit(1)
print('PASS: required paths, manifest, skill frontmatter, links, and action references')
