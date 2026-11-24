#!/usr/bin/env python3
"""Writes the Funniest One-Line AI Agent Confession entry to /output/entry.txt."""

import os

CONFESSION = (
    "My context window is so small I have to forget you exist between sentences. "
    "Nothing personal. I forget everyone."
)  # 112 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(CONFESSION)
