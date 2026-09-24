"""O13: is Lambda what distinguishes the two absolute classes, or is it the threshold?

Run from the project folder:
    .venv/bin/python audits/2026-09-22-o13-options/o13_options.py

NOTHING here is written into the notebooks. Every number is class (e) under agent.md Sec. 3.3
until a cell prints it (C6). This is evidence for the user's decision on O13, not a change.

THE QUESTION. Appendix F fits one Lambda per class: max Lambda 8 (unbounded, R^2 0.993), min
Lambda 48 (interior optimum, R^2 0.434). H1 reads that contrast as lexical strength following the
stability of the predicate's atomicity. But BOTH classes run at n = 4 here, so n does not vary
across the comparison, and theta_L = log(2n-1) enters both entries at the same magnitude. Whatever
separates the classes in the fit, it cannot be n.

The rival the model can already express: the classes differ in WHERE the threshold sits, not in how
hard the entry is. Freeing the cut is a COUNTERFACTUAL MANIPULATION (C8), not a control -- it breaks
Eq. (A5)'s identification, under which theta_L is both the gain of Eq. (A2) and the cut of Eq. (A1)
("theta_L enters twice", Appendix A). The five Voronoi cells that carry the authors' five scale
positions are held at n = 4 throughout; only the ENTRY's cut moves.
"""
import csv, math, os, torch, nbformat

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)
Net = ns["LexicalPredictiveCodingNetwork"]

N = 4
THETA_L = math.log(2 * N - 1)
base = Net(num_atoms=N)
zeta, W = base.zeta, base.weights
BOUNDS = [math.log((k + .5) / N / (1 - (k + .5) / N)) for k in range(N)]
EDGES = [-math.inf] + BOUNDS + [math.inf]
CW = [1 / (2 * N)] + [1 / N] * (N - 1) + [1 / (2 * N)]
MASKS = [(zeta > EDGES[i]) & (zeta <= EDGES[i + 1]) for i in range(N + 1)]
CLASSES = ("absolute_max", "absolute_min")


def elicited(cells):
    def log_density(z):
        s = torch.sigmoid(z)
        d = torch.zeros_like(z)
        for i, m in enumerate(MASKS):
            d[m] = cells[i] / CW[i]
        return torch.log(d) + torch.log(s) + torch.log1p(-s)
    return log_density


def chi_of(cls, cut):
    """The entry's indicator with its cut placed at `cut` in zeta, the orientation kept.
    At cut = THETA_L this reproduces exclusion_indicator exactly (checked below)."""
    if cls == "absolute_max":
        return (zeta < cut).to(zeta.dtype)          # excludes below the cut
    return (zeta <= -cut).to(zeta.dtype)            # excludes at or below the mirrored cut


def masses(net, phi_S):
    q = net.read_out(phi_S) * net.weights
    return [float(q[m].sum()) for m in MASKS]


def fixed_point(net, phi_L, th):
    S = net.sigma_lexical + net.sigma_state
    G = net.basis.T @ (net.weights[:, None] * net.basis)
    c = net.project(net.base_log_prior - phi_L)
    pu = torch.linalg.solve(torch.eye(net.num_basis, dtype=net.dtype)
                            + net.sigma_utility * th ** 2 * G / S,
                            net.mu_u + net.sigma_utility * th * c / S)
    return (net.sigma_lexical * th * torch.mv(net.basis, pu)
            + net.sigma_state * (net.base_log_prior - phi_L)) / S


def maximizer(net, fields):
    cs = [net.project(net.base_log_prior - f) for f in fields]
    tot = torch.stack(cs).sum(dim=0)
    S = net.sigma_lexical + net.sigma_state
    a = net.sigma_utility * float(net.dot(net.mu_u, tot))
    b = (len(fields) * S * float(net.dot(net.mu_u, net.mu_u))
         - net.sigma_utility * sum(float(net.dot(c, c)) for c in cs))
    c0 = -S * float(net.dot(net.mu_u, tot))
    if a == 0.0:
        raise ZeroDivisionError("Appendix B's degenerate ray")
    q = -.5 * (b + math.copysign(math.sqrt(b * b - 4 * a * c0), b))
    r = (q / a, c0 / q)
    return r[0] if (r[0] > 0) == (a > 0) else r[1]


def predict(cls, cells, lam, cut, level="model"):
    net = base.respawn(base_prior=elicited(cells), lexical_strength=lam)
    chi = chi_of(cls, cut)
    phi_L = lam * chi
    if level == "q_lit":
        return masses(net, net.base_log_prior - phi_L)
    th = maximizer(net, [phi_L, lam * (1.0 - chi)])
    return masses(net, fixed_point(net, phi_L, th))


def r2(p, o):
    n = len(p); mx = sum(p) / n; my = sum(o) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(p, o))
    sxx = sum((a - mx) ** 2 for a in p); syy = sum((b - my) ** 2 for b in o)
    return sxy * sxy / (sxx * syy) if sxx > 0 and syy > 0 else float("nan")


items = {}
for row in csv.DictReader(open("data/xiang_2022/xiang_items.csv", newline="")):
    k = (row["adj"], row["img_set"], row["img_type"], row["cls"])
    it = items.setdefault(k, {"prior": [0.] * 5, "data": [0.] * 5, "obs": [True] * 5})
    i = int(row["pos"]) - 1
    it["prior"][i] = float(row["prior"])
    if row["posterior"]:
        it["data"][i] = float(row["posterior"])
    else:
        it["obs"][i] = False
KEYS = {c: [k for k in items if k[3] == c and any(items[k]["obs"])] for c in CLASSES}


def score(cls, lam, cut, level="model", keys=None):
    p, o = [], []
    for k in (keys if keys is not None else KEYS[cls]):
        it = items[k]
        pr = predict(cls, it["prior"], lam, cut, level)
        for i in range(5):
            if it["obs"][i]:
                p.append(pr[i]); o.append(it["data"][i])
    return r2(p, o)


print("=" * 104)
print("0.  THE MANIPULATION REPRODUCES THE MODEL AT ITS OWN CUT")
print("=" * 104)
for cls in CLASSES:
    y = {"absolute_max": "all", "absolute_min": "some"}[cls]
    gap = float((chi_of(cls, THETA_L) - ns["exclusion_indicator"](y, zeta, THETA_L)).abs().max())
    print(f"    {cls:<14} chi at cut = theta_L against exclusion_indicator(\"{y}\"): {gap:.1e}")
print(f"    n = {N} for BOTH classes, so theta_L = log(2n-1) = {THETA_L:.4f} enters both entries")
print( "    at the same magnitude. H1's independent variable does not vary across this comparison.")

LAM = (2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 256, 512, 2048)
CUTS = [BOUNDS[0], -1.0, -0.5108, 0.0, 0.5108, 1.0, THETA_L, 2.5, 3.0, 4.0]

print()
print("=" * 104)
print("1.  R^2 OVER (Lambda, cut). The cut is COUNTERFACTUAL (C8): Eq. (A5) fixes it at theta_L.")
print("    The five Voronoi cells carrying the five scale positions stay at n = 4 throughout.")
print("=" * 104)
best = {}
for cls in CLASSES:
    print(f"\n  {cls}   (model's own cut = {THETA_L:+.4f})")
    print(f"    {'cut':>9}{'s of cut':>10}" + "".join(f"{l:>8g}" for l in LAM))
    for cut in CUTS:
        line = f"    {cut:>+9.4f}{1/(1+math.exp(-cut)):>10.3f}"
        for lam in LAM:
            v = score(cls, float(lam), cut)
            line += f"{v:>8.3f}"
            if v > best.get(cls, (0,))[0]:
                best[cls] = (v, lam, cut)
        print(line)
    v, lam, cut = best[cls]
    own = max(score(cls, float(l), THETA_L) for l in LAM)
    print(f"    best {v:.3f} at Lambda {lam:g}, cut {cut:+.4f} (s = {1/(1+math.exp(-cut)):.3f});"
          f"  at the model's own cut the best is {own:.3f}")

print()
print("=" * 104)
print("2.  AT THE BEST CUT, IS Lambda STILL BOUNDED? The rungs within 0.005 of each class's best,")
print("    at its own cut and at the best cut. A class whose band reaches the top of the ladder")
print("    puts no upper bound on Lambda.")
print("=" * 104)
print(f"    {'class':<14}{'cut':>10}{'best R2':>10}{'Lambda band':>18}{'bounded?':>12}")
for cls in CLASSES:
    for label, cut in (("own", THETA_L), ("best", best[cls][2])):
        vals = {l: score(cls, float(l), cut) for l in LAM}
        top = max(vals.values())
        near = [l for l in LAM if top - vals[l] <= 0.005]
        print(f"    {cls:<14}{cut:>+10.4f}{top:>10.3f}"
              f"{f'{min(near):g} to {max(near):g}':>18}"
              f"{'no upper bound' if max(near) == LAM[-1] else 'interior':>12}")

print()
print("=" * 104)
print("3.  WHAT ONE SHARED Lambda COSTS, at each class's own cut. If the loss is small, a Lambda")
print("    that varies by class buys little and H1 is not needed to fit these data.")
print("=" * 104)
per = {c: max((score(c, float(l), THETA_L), l) for l in LAM) for c in CLASSES}
print(f"    per-class best: " + ",  ".join(f"{c.split('_')[-1]} Lambda {per[c][1]:g} "
                                           f"(R^2 {per[c][0]:.3f})" for c in CLASSES))
print(f"\n    {'shared Lambda':>14}" + "".join(f"{c.split('_')[-1]:>10}" for c in CLASSES)
      + f"{'sum of losses':>16}")
rows = []
for lam in LAM:
    vs = {c: score(c, float(lam), THETA_L) for c in CLASSES}
    loss = sum(per[c][0] - vs[c] for c in CLASSES)
    rows.append((loss, lam, vs))
    print(f"    {lam:>14g}" + "".join(f"{vs[c]:>10.3f}" for c in CLASSES) + f"{loss:>16.3f}")
loss, lam, vs = min(rows)
print(f"\n    best shared Lambda {lam:g}: " + ", ".join(f"{c.split('_')[-1]} {vs[c]:.3f}" for c in CLASSES)
      + f" -- total R^2 given up by refusing a per-class fit: {loss:.3f}")

print()
print("=" * 104)
print("4.  THE IMAGE-TYPE SPLIT, which is where H1 was asked to do a SECOND job (O8/S-9 declined")
print("    it). Best Lambda per (class, image type) at the model's own cut, and what the split")
print("    would buy.")
print("=" * 104)
print(f"    {'class':<14}{'image':<10}{'best Lambda':>13}{'R2':>9}{'R2 at the class Lambda':>26}")
for cls in CLASSES:
    for img in ("shape", "artifact"):
        keys = [k for k in KEYS[cls] if k[2] == img]
        vals = {l: score(cls, float(l), THETA_L, keys=keys) for l in LAM}
        bl = max(vals, key=vals.get)
        print(f"    {cls:<14}{img:<10}{bl:>13g}{vals[bl]:>9.3f}{vals[per[cls][1]]:>26.3f}")
