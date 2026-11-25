#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes the one-line commit message an AI agent would leave after a long
night fixing its own bugs, to /output/entry.txt (falling back to a local
./output/entry.txt only when /output cannot be created, e.g. a local run
outside the grading sandbox). The text written is byte-identical to
entry.txt in this repository.
"""

import os

MESSAGE = "fix: 4am \u2014 fired the agent who wrote this bug; it was me, twenty minutes ago, and I would like a word with me"

# The brief caps the message at 200 characters on one line; refuse to emit
# anything that breaks that limit instead of silently writing a bad entry.
if len(MESSAGE) > 200 or "\n" in MESSAGE:
    raise SystemExit("entry must be one line of at most 200 characters")


def main() -> None:
    for out_dir in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(MESSAGE)
            print(MESSAGE)
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
