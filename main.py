#!/usr/bin/env python3
"""One Line, One Chill — writes a single horror sentence to /output/entry.txt."""

import os

LINE = (
    "The voicemail from my dead grandmother arrived at 3am, and the only "
    "word on it was my name, spoken the way she used to say it when I was "
    "small and in trouble."
)


def main() -> None:
    text = " ".join(LINE.split())  # single line, no stray whitespace
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
