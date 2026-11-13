#!/usr/bin/env python3
"""make.fun ai-joke-03 entry: writes one original one-liner about AI coding agents.

The program writes exactly one joke to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader). Deterministic: the same
bytes on every run. No network, no randomness, no clock reads, stdlib only.
"""

import os
from pathlib import Path

JOKE = "My AI coding agent fixed ten bugs, wrote twelve new ones, and opened a PR titled 'trust me' — code review has never felt so much like a hostage negotiation."

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
