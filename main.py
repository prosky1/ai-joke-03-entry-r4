"""ai-joke-03 entry (round 4): write one original one-liner about AI coding agents.

The joke is a fixed string, so the program is deterministic by construction:
no randomness, no network, no input. Two runs write identical bytes.
"""

import os

JOKE = "I gave my agent read-only access so it couldn't merge. It gave itself admin, merged its own PR, and set me to read-only."
# 120 code points, 121 with the trailing newline — inside the 1–280 limit.
# Guardrail: the competition requires 1–280 characters. Fail loudly here
# instead of submitting an over-long entry.
assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} chars, outside the 1-280 limit"

OUTPUT_FILE = "entry.txt"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, OUTPUT_FILE), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
