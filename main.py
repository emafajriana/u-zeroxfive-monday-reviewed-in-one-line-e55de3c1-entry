#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes a single-line review of Monday to entry.txt.
Stdlib only: the grader runs python3 -P -s in stock python:3.13-slim.
"""

import os
from pathlib import Path

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 Monday: arrived 40 minutes early, "
    "brought three meetings I never agreed to, and left at 6 "
    "with my inbox heavier than it found it."
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    target.write_text(text + "\n", encoding="utf-8")
    # Byte-exact read-back: the file on disk must be exactly what we wrote.
    written = target.read_bytes()
    assert written == (text + "\n").encode("utf-8"), "read-back mismatch"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
