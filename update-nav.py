#!/usr/bin/env python3
"""Batch update navigation across all ems-drone HTML files.
Replaces old /components/ links with /capabilities/ and /applications/ with /industries/."""
import re
from pathlib import Path

ROOT = Path(".")

# Old → New URL mappings
NAV_REPLACEMENTS = [
    # Navigation links (href only — run before text label changes)
    ('href="/components/"', 'href="/capabilities/"'),
    ('href="/components#"', 'href="/capabilities#'),
    ('href="/applications/"', 'href="/industries/"'),
    ('href="/applications#"', 'href="/industries#'),
    # Navigation text labels (in site-nav context)
    ('href="/capabilities/">Components</a>', 'href="/capabilities/">Capabilities</a>'),
    ('href="/industries/">Applications</a>', 'href="/industries/">Industries</a>'),
    # aria-current on old pages
    ('aria-current="page">Components', 'aria-current="page">Capabilities'),
    ('aria-current="page">Applications', 'aria-current="page">Industries'),
    # Footer text labels
    ('<a href="/capabilities/">Components</a>', '<a href="/capabilities/">Capabilities</a>'),
    ('<a href="/industries/">Applications</a>', '<a href="/industries/">Industries</a>'),
    # Blog post CTAs (old links to components/applications)
    ('href="/components/">Explore the component architecture', 'href="/capabilities/">Explore capabilities'),
    ('href="/components/#flight-control">Explore flight control', 'href="/capabilities/flight-control/">Explore flight control'),
    ('href="/components/#esc-power">Explore ESC', 'href="/capabilities/esc-power/">Explore ESC'),
    ('href="/applications/">Explore application contexts', 'href="/industries/">Explore industries'),
    ('href="/components/">Explore components', 'href="/capabilities/">Explore capabilities'),
    # Contact page paths
    ('href="/applications/">Start with the mission', 'href="/industries/">Start with the industry'),
    # /components/ page path → /capabilities/
    ('href="/components/index.html"', 'href="/capabilities/"'),
    # Old directory references in text (keep context)
    ('/components/', '/capabilities/'),
    ('/applications/', '/industries/'),
]

updated = 0
for html_file in ROOT.rglob("*.html"):
    content = html_file.read_text(encoding="utf-8")
    original = content
    for old, new in NAV_REPLACEMENTS:
        content = content.replace(old, new)
    if content != original:
        html_file.write_text(content, encoding="utf-8")
        updated += 1
        print(f"  Updated: {html_file}")

print(f"\nUpdated {updated} files")
