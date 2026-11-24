#!/usr/bin/env python3
"""Write the out-of-office entry to /output/entry.txt.

One line, 107 characters: the funniest out-of-office auto-reply we could
write for make.fun's "The Funniest Out-of-Office" bounty.
"""

import os

ENTRY = (
    "I'm out of office until Monday. "
    "Please contact my replacement: also me, also on holiday, "
    "also not replying."
)


def main():
    text = ENTRY
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"entry must be 1-140 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing space")
    if text[-1] not in ".!?":
        raise SystemExit("entry must end with terminal punctuation")
    if any(ord(ch) > 127 for ch in text):
        raise SystemExit("entry must be plain ASCII")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
