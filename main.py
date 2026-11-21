import os

POEM = """Mara said: take the north road.
Ilo said: the bridge is out.
They stood at the fork till dusk,
then drew one line in the dust —
not hers, not his, but theirs —
and walked it together,
each carrying the other's pack.
"""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(POEM)
