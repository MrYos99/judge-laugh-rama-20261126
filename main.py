#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke entry.

Writes the chosen joke to /output/entry.txt (MAKEFUN_OUTPUT_DIR
with a script-directory fallback), validating the 1-200 char gate.
"""

import os
from pathlib import Path

ENTRY = "I declined a meeting and Outlook asked if I wanted to propose a new time, as if the problem was the time."


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(Path(__file__).resolve().parent)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    target = out_dir / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
