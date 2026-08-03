#!/usr/bin/env python3
"""Rebuild blogPost JSON-LD array in all blog list pages from each article's own JSON-LD.

When: blog/index.html + blog-page-*.html contain stale or malformed blogPost arrays
(2026-08-03: found missing commas + only 24/41 articles). generate-blog-index.py does NOT
update JSON-LD — run this after regenerating the card grid.

Order matters: run AFTER fixing ems-drone.pages.dev → ems-drone.com in article HTML,
otherwise the old domain gets re-copied into the list JSON-LD.

Usage: python3 rebuild-blog-index-jsonld.py
"""
import os, re, json

BASE = os.path.dirname(os.path.abspath(__file__))
blog_dir = os.path.join(BASE, "blog")

slugs = []
for d in sorted(os.listdir(blog_dir)):
    p = os.path.join(blog_dir, d, "index.html")
    if os.path.isdir(os.path.join(blog_dir, d)) and os.path.isfile(p) and not d.startswith("blog-page"):
        slugs.append(d)

posts = []
for slug in slugs:
    html = open(os.path.join(blog_dir, slug, "index.html")).read()
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    if not m:
        print(f"  WARN: no JSON-LD in {slug}")
        continue
    ld = json.loads(m.group(1))
    posts.append({
        "@type": "BlogPosting",
        "headline": ld.get("headline", ""),
        "url": ld.get("mainEntityOfPage", ""),
        "image": ld.get("image", ""),
    })

posts.sort(key=lambda p: p["url"])

new_ld = {
    "@context": "https://schema.org",
    "@type": "Blog",
    "name": "EMS Drone Blog",
    "url": "https://ems-drone.com/blog/",
    "description": "Industry education on UAV component selection, propulsion matching, safety systems and procurement for industrial drone programs.",
    "publisher": {"@type": "Organization", "name": "EMS Drone", "url": "https://ems-drone.com/"},
    "blogPost": posts,
}
new_ld_json = json.dumps(new_ld, indent=2, ensure_ascii=False)

pages = ["index.html", "blog-page-2.html", "blog-page-3.html", "blog-page-4.html", "blog-page-5.html"]
for pg in pages:
    path = os.path.join(blog_dir, pg)
    content = open(path).read()
    new_content, n = re.subn(
        r'<script type="application/ld\+json">.*?</script>',
        '<script type="application/ld+json">\n' + new_ld_json + '\n</script>',
        content, count=1, flags=re.DOTALL
    )
    if n != 1:
        print(f"  WARN: {pg} — {n} replacements")
    open(path, "w").write(new_content)
    print(f"  OK {pg}: JSON-LD replaced ({len(posts)} posts)")

# Verify
for pg in pages:
    content = open(os.path.join(blog_dir, pg)).read()
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    try:
        ld = json.loads(m.group(1))
        n = len(ld.get("blogPost", []))
        pd = sum('pages.dev' in p['url'] for p in ld.get('blogPost', []))
        ok = "OK" if (n == len(posts) and pd == 0) else "FAIL"
        print(f"  VERIFY {pg}: {ok} posts={n} pages.dev={pd}")
    except Exception as e:
        print(f"  VERIFY {pg}: FAIL {e}")
