#!/usr/bin/env python3
"""Mechanical checks for a skill folder. Usage: python validate_skill.py <folder>"""
import re, sys, pathlib

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
errors = []
skill = root / "SKILL.md"
if not skill.exists():
    sys.exit("FAIL: SKILL.md missing")
text = skill.read_text()
m = re.match(r"---\n(.*?)\n---\n", text, re.S)
if not m:
    errors.append("frontmatter missing")
else:
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name or name.group(1).strip() != root.name:
        errors.append(f"name must match folder '{root.name}'")
    if not desc or len(desc.group(1)) < 80:
        errors.append("description missing or too short")
if len(text.splitlines()) > 500:
    errors.append("SKILL.md exceeds 500 lines")
for md in root.rglob("*.md"):
    for ref in re.findall(r"`((?:\.\./)?(?:references|systems|portable|examples|evals|scripts)/[\w./-]+\.\w+)`", md.read_text()):
        cands = [root / ref, md.parent / ref, root / "references" / ref]
        if not any(c.resolve().exists() for c in cands):
            errors.append(f"{md.relative_to(root)}: missing path {ref}")
for f in root.rglob("*"):
    if f.is_file() and f.stat().st_size == 0:
        errors.append(f"empty file {f.relative_to(root)}")
for need in ["README.md", "LICENSE"]:
    if not (root / need).exists():
        errors.append(f"{need} missing")
print("FAIL" if errors else "PASS")
for e in errors:
    print(" -", e)
sys.exit(1 if errors else 0)
