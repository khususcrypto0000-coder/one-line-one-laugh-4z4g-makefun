"""One Line, One Laugh - make.fun one-liner entry.

Writes a single original funny line to /output/entry.txt (UTF-8,
no trailing newline), then reads it back and asserts byte-identical.
"""

import os
import sys

ENTRY = "I asked the plumber for a quote; he looked at my pipes and said, 'Son, this isn't plumbing - it's archaeology.'"

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guards: one line, 1-140 chars, not just whitespace.
    assert 1 <= len(ENTRY) <= 140, "ENTRY must be 1-140 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "ENTRY must be a single line"
    assert ENTRY.strip(), "ENTRY must not be only whitespace"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read back and assert byte-identical.
    with open(OUTPUT_PATH, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    assert back.decode("utf-8") == ENTRY, "decoded text mismatch"
    print("wrote %d bytes to %s" % (len(data), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
