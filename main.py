"""Roast the Smart Fridge: One Line, Best Laugh Wins — entry program.

Writes one original roast of a smart home gadget (a single line of at
most 160 characters) to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "My video doorbell knows every courier by name, yet still files "
    "my mum as 'unknown visitor, possibly hostile'."
)


def main() -> None:
    line = ENTRY.strip()
    if not line or len(line) > 159 or "\n" in line or "\r" in line:
        raise ValueError("entry must be one non-empty line of at most 160 characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
