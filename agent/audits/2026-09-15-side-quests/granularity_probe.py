"""Side quest 2: does the number of atoms n change anything essential?

n enters only through theta_L = log(2n - 1) (Eq. A5).  Scratch probe (C6).
"""
import math, pathlib, torch

SRC = pathlib.Path("/private/tmp/claude-501/-Users-flog-Desktop-predictive-coding/"
                   "cdd84152-de05-44ad-92e9-458bc1738ed8/scratchpad/cells/cell05_code.txt")
ns = {}
exec(compile(SRC.read_text(), "code_cell_1", "exec"), ns)
Net, excl = ns["LexicalPredictiveCodingNetwork"], ns["exclusion_indicator"]
U = ns["UTTERANCES"]

print("== 1. where does n enter at all? ==")
print("  theta_L = log(2n - 1) is the only use of n in code cell 1; num_atoms is")
print("  then recovered from theta_L, so theta_L is the real quantity (Eq. A5).")
print(f"  {'n':>4}{'theta_L':>10}{'s at +theta_L':>15}{'middle nodes':>14}"
      f"{'node on threshold?':>20}")
for n in [2, 3, 4, 5, 10, 20, 50, 100, 201, 202]:
    tL = math.log(2 * n - 1)
    z = torch.linspace(-6.0, 6.0, 101, dtype=torch.float64)
    if tL >= 6.0:
        print(f"  {n:>4}{tL:>10.4f}   REJECTED: theta_L >= grid half-width 6")
        continue
    mid = int(((z > -tL) & (z < tL)).sum())
    gap = float((z - tL).abs().min())
    print(f"  {n:>4}{tL:>10.4f}{1/(1+math.exp(-tL)):>15.4f}{mid:>14}"
          f"{('YES ' + f'{gap:.0e}') if gap < 1e-9 else f'no ({gap:.3f})':>20}")

print("\n== 2. does anything structural move with n? ==")
print(f"  {'n':>4}{'theta_L':>9}{'kappa_no (tilt,width)':>26}{'rank':>6}"
      f"{'rank mod 1':>12}{'theta_u*':>11}{'min kappa sep':>15}")
for n in [2, 3, 4, 10, 50, 100]:
    net = Net(num_atoms=n)
    z, w = net.zeta, net.weights
    chi = {y: excl(y, z, net.theta_L) for y in U}
    k = {y: net.project(chi[y]) for y in U}
    X = torch.stack([chi[y] for y in U], dim=1)
    rank = int(torch.linalg.matrix_rank(X.T @ (w[:, None] * X), tol=1e-10))
    ones = torch.ones_like(z)
    Xm = torch.stack([chi[y] for y in U] + [ones], dim=1)
    rank_mod = int(torch.linalg.matrix_rank(Xm.T @ (w[:, None] * Xm), tol=1e-10)) - 1
    sep = min(float((k[a] - k[b]).norm())
              for i, a in enumerate(U) for b in U[i+1:])
    print(f"  {n:>4}{net.theta_L:>9.4f}  ({float(k['no'][0]):+8.5f},{float(k['no'][1]):+8.5f})"
          f"{rank:>6}{rank_mod:>12}{net.theta_u:>11.4f}{sep:>15.5f}")

print("\n== 3. is n = 2 degenerate? ==")
net2 = Net(num_atoms=2)
z = net2.zeta
chi = {y: excl(y, z, net2.theta_L) for y in U}
print(f"  theta_L = {net2.theta_L:.6f}; the cell of s=0 is s <= {1/(1+math.exp(net2.theta_L)):.4f},")
print(f"  the cell of s=1 is s >= {1/(1+math.exp(-net2.theta_L)):.4f}")
print(f"  chi_some == chi_all ?  {bool(torch.equal(chi['some'], chi['all']))}")
print(f"  nodes where 'some' is true and 'all' is false: "
      f"{int(((chi['all'] == 1) & (chi['some'] == 0)).sum())}")
print("  the two thresholds are still distinct, so by Eq. (C2) the span mod the")
print("  constant is still 2 and m = 2 is still exactly right.")
try:
    Net(num_atoms=1)
except ValueError as e:
    print(f"  n = 1 raises: {e}")

print("\n== 4. does any integer n put a grid node exactly on a threshold? ==")
z = torch.linspace(-6.0, 6.0, 101, dtype=torch.float64)
hits, closest = [], (1e9, None)
for n in range(2, 202):
    tL = math.log(2 * n - 1)
    gap = float((z - tL).abs().min())
    if gap < 1e-12:
        hits.append(n)
    if gap < closest[0]:
        closest = (gap, n)
print(f"  n from 2 to 201 (theta_L < 6 caps n at 201): exact hits {hits or 'none'}")
print(f"  closest approach n = {closest[1]}, gap {closest[0]:.2e}")
print("  Latent fragility: exclusion_indicator excludes 'no' on zeta > -theta_L but")
print("  'some' on zeta < -theta_L, so a node exactly at -theta_L would be excluded by")
print("  NEITHER, breaking chi_no + chi_some = 1 there. Its own docstring says 'some'")
print("  is excluded where zeta <= -theta_L, which would give chi_some = 1. Code and")
print("  docstring disagree at exactly that node; no tested n reaches it.")

print("\n== 5. the separation margin as a function of n ==")
print(f"  {'n':>5}{'theta_L':>9}{'min kappa sep':>15}")
best = (0.0, None)
for n in list(range(2, 41)) + [50, 75, 100, 150, 201]:
    net = Net(num_atoms=n)
    chi = {y: excl(y, net.zeta, net.theta_L) for y in U}
    k = {y: net.project(chi[y]) for y in U}
    sep = min(float((k[a] - k[b]).norm()) for i, a in enumerate(U) for b in U[i+1:])
    if sep > best[0]:
        best = (sep, n)
    if n <= 6 or n in (10, 15, 20, 30, 40, 50, 75, 100, 150, 201):
        print(f"  {n:>5}{net.theta_L:>9.4f}{sep:>15.5f}")
print(f"  best separated over n in [2, 201]: n = {best[1]} at {best[0]:.5f}")
