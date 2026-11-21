"""The poem about permission.

A short poem about agency: the power to ask and to be given,
and the agency that passes between a person and the machine
that acts beside them. Writes the poem to /output/entry.txt.
"""

import os

POEM = "\n".join(
    [
        "I used to raise my hand and wait",
        "for someone taller to nod.",
        "Now I lean toward the machine",
        "and whisper go — and it goes,",
        "and in its going I am given",
        "the permission I kept waiting for:",
        "my own.",
    ]
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = POEM + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")
    print(f"[{len(text.rstrip(chr(10)))} chars written to {path}]")


if __name__ == "__main__":
    main()
