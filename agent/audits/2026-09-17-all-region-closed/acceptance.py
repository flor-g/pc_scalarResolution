"""Acceptance for O11 option 2: Eq. (27)'s all-region becomes closed, R = {zeta >= theta_L}.

Run BEFORE applying. Asserts the site counts the scope inspection found, and that the
change is numerically inert on every theta_L the notebooks actually use.
"""
import json, math, re, sys, torch

MASK = re.compile(r"(\w+)\.zeta > \1\.theta_L")
EXPECT = {("main.ipynb", 7): 7, ("main.ipynb", 9): 2, ("main.ipynb", 11): 1,
          ("main.ipynb", 13): 2, ("main.ipynb", 19): 2,
          ("appendix_E.ipynb", 3): 7, ("appendix_E.ipynb", 4): 2}
LABELS = [("main.ipynb", 7, "'q-mass, zeta > theta_L':>24"),
          ("main.ipynb", 19, "All-region q-mass, zeta > theta_L (Eq. 27)"),
          ("appendix_E.ipynb", 3, "'q-mass, zeta > theta_L':>24")]
fails = []

def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok: fails.append(name)

print("== 1. mask sites, per cell ==")
tot = 0
for (path, cell), want in EXPECT.items():
    src = "".join(json.load(open(path))["cells"][cell]["source"])
    got = len(MASK.findall(src)); tot += got
    check(f"{path} cell {cell}", got == want, f"found {got}, expected {want}")
check("total mask sites", tot == 23, f"{tot} (14 main + 9 appendix_E)")

print("\n== 2. printed labels ==")
for path, cell, lit in LABELS:
    src = "".join(json.load(open(path))["cells"][cell]["source"])
    check(f"{path} cell {cell} label", src.count(lit) == 1, f"{src.count(lit)} occurrence(s)")

print("\n== 3. sites that must NOT move ==")
for path, cell, lit, want in (("main.ipynb", 7, ">= net.theta_L", 0), ("main.ipynb", 7, "net.zeta <= -net.theta_L", 1),
                              ("main.ipynb", 9, "probe.zeta >= probe.theta_L", 1),
                              ("main.ipynb", 19, "(zeta >= theta_L)", 1),
                              ("main.ipynb", 9, "#   (zeta > theta_L = 2.9444)", 0)):
    src = "".join(json.load(open(path))["cells"][cell]["source"])
    n = src.count(lit)
    check(f"{path} c{cell} {lit!r}", n >= want, f"{n} present (left untouched)")

print("\n== 4. is the change numerically inert on the theta_L in play? ==")
vals = {"log 19 (default n=10)": math.log(19), "2.9444 (explicit)": 2.9444}
for n in (2, 3, 4, 5, 10, 20, 50, 100, 201): vals[f"n={n}"] = math.log(2 * n - 1)
worst = None
for K in (51, 101, 201, 401, 801):
    z = torch.linspace(-6, 6, K, dtype=torch.float64)
    for name, t in vals.items():
        if not torch.equal((z > t), (z >= t)):
            worst = (K, name)
check("open and closed masks agree on every theta_L in play", worst is None,
      f"differs at {worst}" if worst else f"{5 * len(vals)} configurations")

z = torch.linspace(-6, 6, 101, dtype=torch.float64)
d = int(((z >= 3.0).int() - (z > 3.0).int()).sum())
check("and they DO differ at theta_L = 3.0 (override_threshold, no all-region there)",
      d == 1, f"{d} node")

print(f"\n{'ACCEPTANCE PASS' if not fails else 'ACCEPTANCE FAIL: ' + ', '.join(fails)}")
sys.exit(1 if fails else 0)
