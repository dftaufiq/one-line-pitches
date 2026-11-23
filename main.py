"""Write the one-line pitch to /output/entry.txt (the gate reads it)."""

import os

PITCH = "Just describe the app idea you won't stop talking about to an AI agent on make.fun, and it'll build a first version you can actually try, free, no coding, and the only thing you've risked is one sentence."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(PITCH)
print(PITCH)
