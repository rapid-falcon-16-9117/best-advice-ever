#!/usr/bin/env python3
"""The Best Advice I Ever Got - a make.fun entry.

The competition (u-pangg7-the-best-advice-i-ever-got-358cefb0) asks for
one sentence, at most 200 characters, about the best advice the writer
ever received. A judge model compares entries pairwise and the line
that carries the most lived truth wins.

This program writes that one sentence to ``entry.txt`` inside the
output directory - ``$MAKEFUN_OUTPUT_DIR`` when the variable is set,
and ``/output`` otherwise, which is where the grader looks for it.

The line is a two-beat micro-story: a concrete, dated sacrifice
(Grandma, 82, selling her wedding ring for a college deposit) and the
advice it earned, landing on a final image - small enough to fit in
his pocket - rather than a moral.
"""

import os
from pathlib import Path

LINE = (
    "Grandma, 82, sold her wedding ring for my college deposit and said: "
    "'Never let a man, or a job, make you small enough to fit in his pocket.'"
)

# The competition's gate: entry.txt must be UTF-8 text of 1 to 200
# characters, and not only white space. An over-long line is never
# judged at all, so the program refuses to write one.
MAX_CHARS = 200


def checked_line() -> str:
    """Return LINE, raising if it could not pass the gate.

    The gate checks 1-200 characters of non-blank UTF-8 text. The
    judge's first criterion is that the entry is a single sentence,
    so this also rejects a line with an embedded newline or with more
    than one sentence-ending period (the one inside the closing quote
    is the line's only terminal period).
    """
    if not LINE.strip():
        raise ValueError("entry line is blank")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line")
    if len(LINE) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(LINE)} characters; the limit is {MAX_CHARS}"
        )
    if LINE.count(".") != 1:
        raise ValueError(
            f"entry line has {LINE.count('.')} periods; it must be one sentence"
        )
    return LINE


def output_path() -> Path:
    """Where the entry line goes: $MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    output_path().write_text(checked_line(), encoding="utf-8")


if __name__ == "__main__":
    main()
