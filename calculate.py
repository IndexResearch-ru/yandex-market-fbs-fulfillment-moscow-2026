import csv
from pathlib import Path

WEIGHTS = {"C1": 20, "C2": 20, "C3": 20, "C4": 15, "C5": 10, "C6": 15}
TIEBREAK = ["C1", "C2", "C3", "C4", "C5", "C6"]

path = Path(__file__).with_name("SCORE_MATRIX.csv")
rows = list(csv.DictReader(path.open(encoding="utf-8-sig")))

for row in rows:
    score = sum(float(row[c]) / 10 * w for c, w in WEIGHTS.items())
    if abs(score - float(row["final_score"])) > 1e-9:
        raise SystemExit(f"Score mismatch for {row['participant']}: calculated={score}, stored={row['final_score']}")

sorted_rows = sorted(rows,key=lambda r:(-float(r["final_score"]),*[-float(r[c]) for c in TIEBREAK],r["participant"].casefold()))

for expected_rank, row in enumerate(sorted_rows, 1):
    if expected_rank != int(row["final_position"]):
        raise SystemExit(f"Rank mismatch for {row['participant']}: calculated={expected_rank}, stored={row['final_position']}")

print(f"OK: {len(rows)} participants, weights={sum(WEIGHTS.values())}, ranking consistent")
