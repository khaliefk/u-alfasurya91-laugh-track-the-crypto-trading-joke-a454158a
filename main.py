#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single fresh one-line joke about crypto and trading life to
/output/entry.txt (102 characters, inside the 1-200 gate).
"""

import os

ENTRY = "I bought the dip at $60K. It dipped again, dug a basement, and now my portfolio pays rent underground."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry out of gate: {len(ENTRY)} chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
