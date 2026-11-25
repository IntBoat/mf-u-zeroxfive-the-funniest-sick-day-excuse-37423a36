#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "Sorry, I can't come in today — my smart fridge locked me out of the kitchen and is holding my lunch hostage until I update its firmware."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
