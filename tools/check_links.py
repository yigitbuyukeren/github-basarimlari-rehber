#!/usr/bin/env python3
"""Rehberdeki yerel Markdown bağlantılarının hedeflerini denetle."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)")


def main():
    missing = []
    files = sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").glob("*.md"))
    for file in files:
        fenced = False
        for number, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith(("```", "~~~")):
                fenced = not fenced
                continue
            if fenced:
                continue
            for match in LINK.finditer(line):
                target = urlsplit(match.group(1).strip("<>"))
                if target.scheme or target.netloc or not target.path:
                    continue
                path = unquote(target.path)
                if not (file.parent / path).exists():
                    missing.append(f"{file.relative_to(ROOT)}:{number}: {path}")
    if missing:
        print("\n".join(missing))
        return 1
    print(f"{len(files)} Markdown dosyasındaki yerel bağlantılar doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
