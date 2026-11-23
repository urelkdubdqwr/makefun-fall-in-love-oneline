"""Writes the one-line make.fun entry to entry.txt in the output directory."""

import os
import sys

ENTRY = (
    "The vending machine outside the hospital still owes my dead mother fifty cents, "
    "and I feed it quarters every visit so it stays in her debt, the last place that "
    "still expects her.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        sys.exit(f"main.py: cannot create output directory {out_dir!r}: {exc}")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
