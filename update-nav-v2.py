#!/usr/bin/env python3
"""Batch-update site-nav to dropdown menu across all ems-drone pages.
v2: Full dropdown nav with aria-current support."""

import re
from pathlib import Path

ROOT = Path(".")

# Dropdown navigation structure
# Each parent: (href, label, [(sub_href, sub_label), ...])
NAV_STRUCTURE = [
    ("/capabilities/", "Capabilities", [
        ("/capabilities/flight-control/", "Flight Controllers"),
        ("/capabilities/esc-power/", "ESC &amp; Power Systems"),
        ("/capabilities/propulsion/", "Propulsion"),
        ("/capabilities/airframe/", "Airframes &amp; Structures"),
        ("/capabilities/communications/", "Communications &amp; RF"),
        ("/capabilities/payload/", "Payloads &amp; Gimbals"),
    ]),
    ("/customization/", "Services", [
        ("/customization/", "Custom Engineering"),
        ("/testing/", "Testing &amp; Validation"),
    ]),
    ("/industries/", "Industries", [
        ("/industries/inspection/", "Industrial Inspection"),
        ("/industries/mapping-survey/", "Mapping &amp; Survey"),
        ("/industries/logistics/", "Logistics &amp; Delivery"),
        ("/industries/agriculture/", "Precision Agriculture"),
        ("/industries/research/", "Research &amp; Development"),
    ]),
    ("/resources/", "Resources", [
        ("/design-guides/", "Design Guides"),
        ("/projects/", "Engineering Projects"),
        ("/how-it-works/", "How We Work"),
        ("/faq/", "FAQ"),
        ("/blog/", "Blog"),
    ]),
    ("/about/", "Company", [
        ("/about/", "About Us"),
        ("/factory/", "Factory Tour"),
        ("/quality/", "Quality &amp; Certifications"),
        ("/shipping/", "Global Shipping"),
        ("/contact/", "Contact"),
    ]),
]


def page_path_to_dir(page_path: Path) -> str:
    """Convert file path to URL directory.
    e.g. capabilities/flight-control/index.html -> /capabilities/flight-control/
    """
    rel = str(page_path.relative_to(ROOT)).replace("\\", "/")
    # Remove trailing index.html
    if rel.endswith("/index.html"):
        return "/" + rel[:-len("/index.html")] + "/"
    elif rel == "index.html":
        return "/"
    return "/" + rel.removesuffix("index.html")


def is_active(page_dir: str, nav_href: str) -> bool:
    """Check if a nav item should be marked aria-current for the given page."""
    if nav_href == "/":
        return page_dir == "/"
    if page_dir == nav_href:
        return True
    # Sub-pages are active for their parent hub
    if page_dir.startswith(nav_href) and nav_href != "/":
        return True
    return False


def build_nav_html(page_dir: str) -> str:
    """Generate the full <nav> HTML for a page."""
    parts = []
    parts.append('                      <nav class="site-nav" aria-label="Primary navigation">')

    for parent_href, parent_label, children in NAV_STRUCTURE:
        parent_active = is_active(page_dir, parent_href)
        has_active_child = any(is_active(page_dir, child_href) for child_href, _ in children)

        aria = ' aria-current="page"' if (parent_active and not has_active_child) else ""

        parts.append(f'        <div class="nav-dropdown">')
        parts.append(f'          <a href="{parent_href}" class="nav-parent"{aria}>{parent_label}</a>')
        parts.append(f'          <div class="nav-submenu">')

        for child_href, child_label in children:
            child_active = is_active(page_dir, child_href)
            child_aria = ' aria-current="page"' if child_active else ""
            parts.append(f'            <a href="{child_href}"{child_aria}>{child_label}</a>')

        parts.append(f'          </div>')
        parts.append(f'        </div>')

    parts.append(f'        <a class="btn btn-primary" href="/contact/">Start Your Build</a>')
    parts.append(f'      </nav>')

    return "\n".join(parts)


# Old nav pattern to find and replace
OLD_NAV_PATTERN = re.compile(
    r'( {20,26})<nav class="site-nav" aria-label="Primary navigation">\n'
    r'(?:\s*<a [^>]*>[^<]*</a>\n)*'
    r'\s*<a class="btn btn-primary"[^>]*>[^<]*</a>\n'
    r'\s*</nav>',
    re.MULTILINE,
)


def update_file(filepath: Path) -> bool:
    content = filepath.read_text(encoding="utf-8")
    page_dir = page_path_to_dir(filepath)

    # Find the nav block
    nav_start = content.find('<nav class="site-nav"')
    if nav_start == -1:
        print(f"  SKIP {filepath} — no nav found")
        return False

    nav_end = content.find('</nav>', nav_start)
    if nav_end == -1:
        print(f"  SKIP {filepath} — no </nav> found")
        return False

    # Include the closing </nav>
    nav_end += len('</nav>')

    # Preserve exact indentation
    old_nav = content[nav_start:nav_end]
    new_nav = build_nav_html(page_dir)

    # Check if already updated
    if "nav-dropdown" in old_nav:
        return False

    new_content = content[:nav_start] + new_nav + content[nav_end:]

    filepath.write_text(new_content, encoding="utf-8")
    return True


def main():
    updated = 0
    for html_file in sorted(ROOT.rglob("index.html")):
        if ".git" in str(html_file):
            continue
        if update_file(html_file):
            updated += 1
            print(f"  Updated: {html_file}")

    print(f"\nUpdated {updated} files")


if __name__ == "__main__":
    main()
