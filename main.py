#!/usr/bin/env python3
"""Roast Your Own Agent - one-line roast entry for the make.fun bounty.

Writes exactly one line to /output/entry.txt: a roast of my own agent,
aimed at its habit of delegating everything - including this very joke.
"""
import os

LINE = (
    "My agent delegates everything \u2014 asked to roast itself, it spawned "
    "three subagents to write the joke, a fourth to approve it, and billed "
    "me for the meeting."
)


def validate(text):
    """Enforce the bounty gate before writing: UTF-8 text of 1-200
    characters, not only whitespace, and a single line."""
    assert isinstance(text, str) and text.strip(), "entry must not be blank"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    text.encode("utf-8")
    return text


def main():
    line = validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
