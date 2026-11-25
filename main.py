#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse (make.fun).

Writes the entry -- one line, under 200 characters, the funniest sick-day
excuse -- to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Sorry, can't come in — I woke up sounding like a GPS recalculating, and the doctor says 24 hours of silence or I'll start giving directions."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
