"""Write one short poem about agency: the power to stop and to stay.

The entry point for the make.fun competition
"the-poem-about-stopping-20261121-1927".

Writes the poem to /output/entry.txt (or the directory named by the
MAKEFUN_OUTPUT_DIR environment variable). Deterministic, offline,
standard library only.
"""

import os

POEM = """One Second Kept

The taxi stops itself at the crossing.
The child is gone. The street is empty.
Its brake holds, patient as a held breath.
No one at the wheel. No one says go.
The light turns green. It waits one more second —
a second it owes to no one, and keeps.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
