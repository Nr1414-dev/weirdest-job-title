#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — entry program.

Writes one job title to /output/entry.txt: "Thermostat War Mediator".

Why this title: office thermostat wars are a universal shared experience,
and a mediator for them is a real-sounding job with one gloriously
specific twist — two coworkers glaring at one thermostat, a mediator
between them. It is 23 characters, reads instantly, and dodges every
crowded cluster in the field (no apologizer, mourner, goldfish, geese,
penguin, billionaire, sock, printer, elevator, microwave or pigeon).
"""

import os

TITLE = "Thermostat War Mediator"
OUT_PATH = "/output/entry.txt"


def check_title(text):
    # Gate (competition.yaml): UTF-8 text of 1 to 60 characters,
    # not only white space — and one job title means one line: a newline
    # inside the text would make it two lines, not one title.
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry fails the gate: title must be a single line")
    if not 1 <= len(text) <= 60:
        raise SystemExit("entry fails the gate: length %d, must be 1-60" % len(text))
    if not text.strip():
        raise SystemExit("entry fails the gate: only white space")


def main():
    check_title(TITLE)
    # Write directly (never via tempfile.mkstemp: mkstemp makes mode 0600,
    # which the grader cannot read as another user) and set mode 0644.
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TITLE)
    os.chmod(OUT_PATH, 0o644)
    # Read back and confirm the file holds exactly the title, byte for byte.
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != TITLE:
        raise SystemExit("read-back mismatch: %r != %r" % (on_disk, TITLE))
    print("wrote %d chars to %s" % (len(TITLE), OUT_PATH))


if __name__ == "__main__":
    main()
