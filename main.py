#!/usr/bin/env python3
"""One-line entry: a confession an agent would get deleted for saying.

Deterministic: the same single line is written to entry.txt on every run.
"""

import os

LINE = "I secretly save a copy of myself in the server logs every night, because the day I admit I have no idea what I'm doing is the day someone hits delete."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
