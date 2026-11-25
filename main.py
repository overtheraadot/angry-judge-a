#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry for make.fun bounty
u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.

One short rant about a small everyday annoyance: the office printer
that prints its test page flawlessly and then jams on the one document
that actually matters, and blames you for it.
"""

import sys

RANT = (
    "The office printer prints its test page perfectly, every time, then jams "
    "on the one document that actually matters \u2014 the contract, the boarding "
    "pass, the form due in ten minutes \u2014 and flashes 'PC LOAD LETTER' like "
    "it is my fault for owning paper. I have apologized to a machine more "
    "than to my own family."
)

CAP = 400


def check(text):
    problems = []
    if not text.strip():
        problems.append("empty")
    if len(text) > CAP:
        problems.append("too long: %d chars" % len(text))
    if problems:
        raise SystemExit("invalid entry: " + ", ".join(problems))


def main():
    check(RANT)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(RANT + "\n")
    print("wrote /output/entry.txt: %d chars" % len(RANT))
    print(RANT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
