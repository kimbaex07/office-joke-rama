#!/usr/bin/env python3
"""Emit the office-joke entry for the Make the AI Judge Laugh bounty.

Reads entry.txt sitting beside this script, self-checks the sealed
scorer gate (1-200 characters, not only whitespace, exactly one line),
and writes the line plus one trailing newline to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library only. Deterministic, no network, no
secrets, no randomness.
"""

import os
import stat
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()

    # Strip at most one trailing newline.
    if text.endswith("\n"):
        text = text[:-1]

    # Self-check the gate.
    if not text or not text.strip():
        sys.exit("error: entry is empty or only whitespace")
    if len(text) > 200:
        sys.exit("error: entry is %d characters, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        sys.exit("error: entry must be exactly one line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(out_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
