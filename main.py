#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

The line is a genuine review: a specific plant's-eye grievance (a pot
with no drainage, yesterday's coffee for water, a sunless corner) and
the reason for the single star (the owner still claims the plant is
thriving). The joke's turn is the gap between what the owner says
("low maintenance", "thriving") and what the plant endures (drowning).
Under 280 characters, one line, no stock phrasing.
"""

import os

MAX_CHARS = 279  # gate: /output/entry.txt must be 1-279 UTF-8 characters

ENTRY = (
    "One star: he calls me 'low maintenance' while I drown in a pot with "
    "no drainage, watered with yesterday's coffee, in the one corner of "
    "the room the sun forgot \u2014 and he still tells guests I'm thriving."
)


def main() -> None:
    text = ENTRY.strip()
    if not text or "\n" in text or len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry fails the gate: one line, 1-{MAX_CHARS} chars "
            f"(got {len(text)})"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"chars: {len(text)}")


if __name__ == "__main__":
    main()
