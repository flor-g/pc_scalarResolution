"""Data-integrity check for `xiang_items.csv`. Reads nothing from the notebooks and runs no model.

    .venv/bin/python data/xiang_2022/check_data.py

It verifies the file's sha256 and shape, then reprints the six empirical class profiles that F1 of
`procedure_records/scale_classes_hypothesis.md` records. **This script is not a source for any
number the paper quotes** — under C6 that source is Code Cell F of `main.ipynb`. Its only job is to
tell you whether the file beside it is the file the README describes.
"""
import csv
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "xiang_items.csv")
SHA256 = "c23d930d48357455b797a953651459e97b4371ef53de00b745cafbeb792004a0"
CLASSES = ("absolute_max", "absolute_min", "relative")
EXPECTED_ITEMS = {("absolute_max", "shape"): 16, ("absolute_max", "artifact"): 16,
                  ("absolute_min", "shape"): 12, ("absolute_min", "artifact"): 12,
                  ("relative", "shape"): 20, ("relative", "artifact"): 20}

digest = hashlib.sha256(open(CSV, "rb").read()).hexdigest()
ok = digest == SHA256
print(f"sha256 {digest}")
print(f"  {'matches' if ok else 'DOES NOT MATCH'} the README")

rows = list(csv.DictReader(open(CSV, newline="")))
items = {}
for r in rows:
    it = items.setdefault((r["adj"], r["img_set"], r["img_type"], r["cls"]),
                          {"prior": [0.0] * 5, "post": [0.0] * 5, "tvj": [0.0] * 5})
    i = int(r["pos"]) - 1
    it["prior"][i] = float(r["prior"])
    it["post"][i] = float(r["posterior"]) if r["posterior"] else 0.0
    it["tvj"][i] = float(r["tvj"]) if r["tvj"] else 0.0

counts = {k: sum(1 for key in items if (key[3], key[2]) == k) for k in EXPECTED_ITEMS}
blank = sum(1 for r in rows if not r["posterior"])
print(f"{len(rows)} rows, {len(items)} items, {blank} absent Experiment 3 cells "
      f"(README says 480, 96, 10)")
print("  item counts " + ("match" if counts == EXPECTED_ITEMS else f"DIFFER: {counts}"))

worst = max(abs(sum(it["prior"]) - 1.0) for it in items.values())
print(f"  every item's prior sums to 1 within {worst:.1e}")

print()
print("The six empirical profiles (Experiment 3), against F1 of scale_classes_hypothesis.md:")
print(f"  {'class':<13}{'condition':<10}" + "".join(f"{i:>7}" for i in range(1, 6))
      + f"{'peak':>7}{'mean pos':>10}")
for cls in CLASSES:
    for img in ("shape", "artifact"):
        keys = [k for k in items if k[3] == cls and k[2] == img]
        v = [sum(items[k]["post"][i] for k in keys) / len(keys) for i in range(5)]
        print(f"  {cls:<13}{img:<10}" + "".join(f"{x:>7.3f}" for x in v)
              + f"{1 + max(range(5), key=lambda i: v[i]):>7}"
              + f"{sum((i + 1) * x for i, x in enumerate(v)):>10.2f}")

sys.exit(0 if ok and counts == EXPECTED_ITEMS and len(items) == 96 else 1)
