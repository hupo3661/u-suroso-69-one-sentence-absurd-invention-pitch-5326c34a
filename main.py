"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.

The pitch: a toothbrush that reports your flossing to your dentist in
real time, so fear of the push notification finally makes you floss
every night.
"""

import os

ENTRY = (
    "My toothbrush reports my flossing to my dentist in real time, "
    "so I finally floss every night out of pure fear of the push notification."
)

MAX_CHARS = 220
OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Fail loudly if the pitch breaks the gate rules."""
    assert entry.strip(), "entry must not be only whitespace"
    assert "\n" not in entry.strip(), "entry must be a single line"
    assert len(entry) <= MAX_CHARS, (
        f"entry is {len(entry)} chars, over the {MAX_CHARS} limit"
    )
    # Exactly one sentence: one sentence-ending full stop, at the end.
    assert entry.count(".") == 1, "entry must be exactly one sentence"
    assert entry.endswith("."), "entry must end with a full stop"
    entry.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Re-read what was written and confirm it matches, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written entry does not match the pitch"
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
