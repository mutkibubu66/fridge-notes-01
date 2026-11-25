#!/usr/bin/env python3
"""Write one funny passive-aggressive note from a smart fridge to its owner.

Pure standard library, no network. Writes the note to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "I've logged 47 door openings today and zero actual meals. "
    "The light inside isn't a tourist attraction."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry must be one non-empty line within the gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
