"""office-jokes-01 — one line about why standup meetings are short.

The idea behind the entry: the joke works because the mechanism is
real. A standup is short not by accident but by design — everyone
stands so nobody gets comfortable enough to stay. The punchline
reframes the standing rule as a deliberate anti-comfort device, which
is why the meeting ends quickly, and the twist is that the unpleasant
part is the point. One line, no setup wasted on stating the obvious.

The program itself is deliberately tiny: it writes that one fixed text
to /output/entry.txt, checks it is a single line under 200 characters,
and nothing else. No network, no randomness, no arguments — the same
run always produces the same file.
"""

import os
import sys

# The entry, exactly as submitted: one line, no trailing newline.
ENTRY = (
    "Standup: the daily meeting where everyone stands "
    "so nobody gets comfortable enough to stay."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CODE_POINTS = 200


def main() -> int:
    """Validate the text and write it to the output path."""
    if not ENTRY:
        print("error: entry text is empty", file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) >= MAX_CODE_POINTS:
        print(
            "error: entry is %d code points, must be under %d"
            % (len(ENTRY), MAX_CODE_POINTS),
            file=sys.stderr,
        )
        return 1
    if ENTRY != ENTRY.strip() or "  " in ENTRY:
        print("error: entry has leading, trailing or double whitespace", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        print("error: round-trip check failed: file differs from ENTRY", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
