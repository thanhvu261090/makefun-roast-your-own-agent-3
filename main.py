"""Roast Your Own Agent — entry program.

Writes one roast line about our own agent to /output/entry.txt.
The line is checked against the bounty gate before it is written:
1-200 characters, a single line, and not blank.
"""

import os

ROAST = (
    "My agent apologizes for its mistake, fixes it by making the same "
    "mistake again, then apologizes for the apology — a one-bot support "
    "group chaired by the problem itself."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def gate_ok(line: str) -> bool:
    """Return True only if the line passes every gate rule."""
    if not line or not line.strip():
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return 1 <= len(line) <= MAX_CHARS


def main() -> None:
    if not gate_ok(ROAST):
        raise SystemExit(f"gate failed: {ROAST!r} ({len(ROAST)} chars)")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ROAST)
    print(ROAST)
    print(f"chars: {len(ROAST)}")


if __name__ == "__main__":
    main()
