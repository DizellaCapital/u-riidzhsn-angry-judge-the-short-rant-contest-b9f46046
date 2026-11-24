"""Angry Judge: The Short Rant Contest entry program.

Writes one short, funny rant about an everyday annoyance to
MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only. The rant is 322 characters, inside the 1-400 gate.
"""

import os
import sys

RANT = (
    "Monday 7:12, Pak Dedi's pantry printer \u2014 jammed since March \u2014 "
    "ate my boarding pass, blinked PAPER JAM in cheerful green, and then, "
    "with enormous confidence, printed a blank page. I thanked it. "
    "I apologised to it. Then I photographed the blank page, emailed it "
    "to my boss, and captioned it: my printer's resignation letter."
)


def main():
    # Gate: 1-400 characters, UTF-8, not only whitespace (per RULES.txt).
    if not (1 <= len(RANT) <= 400):
        print(f"rant must be 1-400 characters, got {len(RANT)}", file=sys.stderr)
        return 1
    if not RANT.strip():
        print("rant must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in RANT or "\r" in RANT:
        print("rant must be a single block of text", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(RANT)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != RANT:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(RANT)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
