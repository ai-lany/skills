#!/usr/bin/env python3
"""Copy references/tokens.css into every example between the tokens:start/end markers.

Examples stay single-file (easy to paste into an artifact or a new project) while tokens.css
remains the single source of truth. Run after editing tokens.css:  python3 scripts/sync_tokens.py
"""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
tokens = (root / "references" / "tokens.css").read_text()
pattern = re.compile(r"(/\* tokens:start \*/\n).*?(/\* tokens:end \*/)", re.S)
for page in sorted((root / "examples").glob("*.html")):
    html = page.read_text()
    new, n = pattern.subn(lambda m: m.group(1) + tokens + m.group(2), html)
    if n:
        page.write_text(new)
        print(f"synced {page.relative_to(root)}")
