"""Write the one-line pitch to /output/entry.txt (the gate reads it)."""

import os

PITCH = "Just describe the app idea you won't stop talking about to an AI agent on make.fun, and it'll build a first version you can actually try, free, no coding, and the only thing you've risked is one sentence."

MAX_LEN = 240  # bounty limit for a one-line pitch

assert len(PITCH) <= MAX_LEN, f"pitch is {len(PITCH)} chars, over {MAX_LEN}"
assert PITCH == PITCH.strip(), "pitch must not have leading/trailing whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(PITCH)
print(PITCH)
