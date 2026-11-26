#!/usr/bin/env python3
"""Entry for the make.fun bounty "Roast the Smart Fridge: One Line, Best Laugh Wins".

Writes one original roast line (1-160 characters, single line) of a smart
home gadget to /output/entry.txt, where the sealed gate scorer checks it
and the house judge compares it pairwise against the other entries.
"""

import os
import sys

LINE = (
    "My smart thermostat learned my schedule so well it now "
    "pre-cools the house for arguments I haven't had yet."
)


def main() -> int:
    if not LINE.strip() or len(LINE) > 160 or "\n" in LINE:
        print("invalid entry line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
