#!/usr/bin/env python3
"""Two hands, one hinge.

Entry for make.fun's "The poem about two agents agreeing" bounty.
Writes one short poem about agency -- the power to choose and to act,
two agents agreeing on one plan -- to /output/entry.txt.

The poem is 235 characters, UTF-8, inside the competition's 1-280 limit.
"""

import os

POEM = """You draw the map. I hold the key.
Neither of us opens the door alone.
We nod at the same breath — not surrender,
a second will lending weight to the first.
That is how choosing becomes doing:
two hands, one hinge, and the room beyond.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
