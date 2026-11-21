"""The poem about two agents agreeing.

Writes the seven-line poem about Mara and Ilo — two agents who disagree
at a fork, draw one shared line in the dust, and walk it together —
to /output/entry.txt.
"""

import os

POEM = """Mara said: take the north road.
Ilo said: the bridge is out.
They stood at the fork till dusk,
then drew one line in the dust —
not hers, not his, but theirs —
and walked it together,
each carrying the other's pack.
"""

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
