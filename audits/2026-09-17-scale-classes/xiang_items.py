"""Audit 2026-09-17, part 2: the model run on Xiang, Kennedy, Xu & Leffel's (2022) own 96 items,
with their own elicited priors, and compared with their own posterior-degree data.
Nothing here is written back into the notebooks; every number is class (e) under agent.md Sec. 3.3
until a cell prints it (C6).

Run from the project folder:
    .venv/bin/python audits/2026-09-17-scale-classes/xiang_items.py

DATA. `xiang_items.csv` beside this script, derived from the authors' public OSF repository
(https://osf.io/nr6a4/, CC-BY): `Expt1.priors/expt1.priors.adjsplitted.byitem.csv` (the elicited
degree prior for each of the 96 items, in that adjective's own orientation), `Expt3.posterior_
degrees/adj.posterior.judgment.results.csv` and `Expt2.Truth_value_judgment/Expt2.adjTVJ.csv`
(averaged per item and scale position over participants, keyed by the authors' `scale_updated`),
and `Expt1.priors/adj_info.csv` for the class of each adjective. Zero prior cells are smoothed as
the authors smooth them (+1e-5, taken off the largest cell) and the five cells renormalized. Ten
item x position cells drew no Experiment 3 response and are read as 0.

THE MODEL ON THESE ITEMS. Five scale positions = the five Voronoi cells of a predicate resolving
n = 4 atoms (Eq. A5), theta_L = log 7. In each adjective's own orientation Eq. (A1) gives
    absolute_max  "straight", "full"    -> the model's "all":  excludes zeta < theta_L
    absolute_min  "bent", "striped"     -> the model's "some": excludes zeta <= -theta_L
    relative      "tall"                -> a cut at a context threshold t, scanned below
and the antonym the item pairs it with is, in that same orientation, the entry's complement. So the
exposure ensemble of A9 is {chi, 1 - chi} for every item, which is what fixes decisions.md O8 here.
The elicited five-cell prior is pushed onto the grid as a density in s that is constant on each
Voronoi cell, times the Jacobian s(1-s) of Eq. (1). Lambda is the only quantity scanned.

R^2 is the squared Pearson correlation over item x position rows, which is how the authors compute
theirs (`LG&QF.model.predictions.R`, lines 184-190): their Table 5 reports, for posterior degrees,
LG .78 overall (.94 max, .55 min, .69 rel) and QF .82 overall (.97 max, .58 min, .78 rel).
"""
import csv
import math
import os

import nbformat
import torch

HERE = os.path.dirname(os.path.abspath(__file__))
nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)
Net = ns["LexicalPredictiveCodingNetwork"]

N_ATOMS = 4
THETA_L = math.log(2 * N_ATOMS - 1)
net = Net(num_atoms=N_ATOMS)
zeta, W, B = net.zeta, net.weights, net.basis
G = B.T @ (W[:, None] * B)
mu = net.mu_u
s_grid = torch.sigmoid(zeta)
BOUNDS = [math.log((k + 0.5) / N_ATOMS / (1 - (k + 0.5) / N_ATOMS)) for k in range(N_ATOMS)]
EDGES = [-math.inf] + BOUNDS + [math.inf]
CELL_WIDTH = [1 / (2 * N_ATOMS)] + [1 / N_ATOMS] * (N_ATOMS - 1) + [1 / (2 * N_ATOMS)]
CHI_ALL = ns["exclusion_indicator"]("all", zeta, THETA_L)
CHI_SOME = ns["exclusion_indicator"]("some", zeta, THETA_L)


def fixed_point(ell0, phi_L, theta):
    c = B.T @ (W * (ell0 - phi_L))
    phi_u = torch.linalg.solve(torch.eye(G.shape[0], dtype=G.dtype) + theta ** 2 * G / 2,
                               mu + theta * c / 2)
    return ((ell0 - phi_L) + theta * (B @ phi_u)) / 2, phi_u


def free_energy(ell0, phi_L, theta):
    phi_S, phi_u = fixed_point(ell0, phi_L, theta)
    return (-0.5 * float(torch.sum(W * (phi_L - ell0 + phi_S) ** 2))
            - 0.5 * float(torch.sum(W * (phi_S - theta * (B @ phi_u)) ** 2))
            - 0.5 * float(torch.sum((phi_u - mu) ** 2)))


def learned_theta(ell0, fields):
    """theta_u* in closed form: the maximizing root of Eq. (B2), summed over the ensemble as in
    Eq. (B3) with G = I. This is Code Cell B's `stationary_maximizer`, lifted verbatim in form."""
    couplings = [B.T @ (W * (ell0 - phi_L)) for phi_L in fields]
    total_sigma = 2.0
    total = sum(couplings)
    a = float(torch.dot(mu, total))
    b = (len(couplings) * total_sigma * float(torch.dot(mu, mu))
         - sum(float(torch.dot(c, c)) for c in couplings))
    c0 = -total_sigma * a
    q = -0.5 * (b + math.copysign(math.sqrt(b * b - 4.0 * a * c0), b))
    roots = (q / a, c0 / q)
    return roots[0] if (roots[0] > 0) == (a > 0) else roots[1]


def scanned_theta(ell0, fields):
    """The same maximizer by a dense scan then golden-section refinement, as a check on the above."""
    f = lambda th: sum(free_energy(ell0, phi_L, th) for phi_L in fields) / len(fields)
    grid = [0.0] + [sgn * 10 ** e for sgn in (1, -1) for e in [x / 20 for x in range(-60, 101)]]
    best = max(grid, key=f)
    lo, hi = best - abs(best) * 0.3 - 1e-3, best + abs(best) * 0.3 + 1e-3
    g = (math.sqrt(5) - 1) / 2
    for _ in range(120):
        x, y = hi - g * (hi - lo), lo + g * (hi - lo)
        if f(x) > f(y):
            hi = y
        else:
            lo = x
    return (lo + hi) / 2


def read_out(phi):
    q = torch.exp(phi - phi.max())
    return q / torch.sum(W * q)


def positions(phi):
    q = read_out(phi) * W
    return [float(q[(zeta > EDGES[i]) & (zeta <= EDGES[i + 1])].sum()) for i in range(N_ATOMS + 1)]


def ell0_from_cells(p):
    """A five-cell probability vector as a log-density in zeta: constant in s on each Voronoi cell,
    times the Jacobian ds/dzeta = s(1-s) of Eq. (1)."""
    dens = torch.zeros_like(zeta)
    for i in range(N_ATOMS + 1):
        mask = (zeta > EDGES[i]) & (zeta <= EDGES[i + 1])
        dens[mask] = p[i] / CELL_WIDTH[i]
    return torch.log(dens) + torch.log(s_grid) + torch.log1p(-s_grid)


def chi_cut(t):
    chi = (zeta < t).to(zeta.dtype)
    chi[(zeta - t).abs() < 1e-12] = 0.5
    return chi


def pearson_r2(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    return (sxy * sxy) / (sxx * syy) if sxx > 0 and syy > 0 else float("nan")


# ---------------------------------------------------------------- the items
rows = list(csv.DictReader(open(os.path.join(HERE, "xiang_items.csv"), newline="")))
items = {}
for r in rows:
    key = (r["adj"], r["img_set"], r["img_type"], r["cls"])
    it = items.setdefault(key, {"prior": [0.0] * 5, "post": [0.0] * 5, "tvj": [0.0] * 5})
    i = int(r["pos"]) - 1
    it["prior"][i] = float(r["prior"])
    it["post"][i] = float(r["posterior"]) if r["posterior"] else 0.0
    it["tvj"][i] = float(r["tvj"]) if r["tvj"] else 0.0
print(f"items {len(items)}; by class "
      + ", ".join(f"{c} {sum(1 for k in items if k[3] == c)}"
                  for c in ("absolute_max", "absolute_min", "relative")))
print(f"n = {N_ATOMS}, theta_L = {THETA_L:.4f}; the five cells are s <= {1/(2*N_ATOMS):.3f}, "
      f"then three of width {1/N_ATOMS:.2f}, then s >= {1-1/(2*N_ATOMS):.3f}")
check = ell0_from_cells([0.2] * 5)
print(f"prior push-forward check: a uniform five-cell prior returns "
      f"{[round(v, 4) for v in positions(check)]}")
ref = Net(num_atoms=N_ATOMS)
gap = abs(learned_theta(ref.base_log_prior, [ref.lexical_field(y) for y in ("no", "some", "all")])
          - scanned_theta(ref.base_log_prior, [ref.lexical_field(y) for y in ("no", "some", "all")]))
full = Net()
print(f"closed-form theta_u* against the scan, n = {N_ATOMS} inventory: {gap:.1e}; "
      f"default n = 10 inventory: {learned_theta(full.base_log_prior, [full.lexical_field(y) for y in ('no', 'some', 'all')]):.4f} "
      f"(Code Cell 2 prints -28.4375)")
print()


def model_profile(cls, prior, lam, cut_t, level="model"):
    ell0 = ell0_from_cells(prior)
    if cls == "absolute_max":
        chi = CHI_ALL
    elif cls == "absolute_min":
        chi = CHI_SOME
    else:
        chi = chi_cut(cut_t)
    phi_L = lam * chi
    if level == "literal":
        return positions(ell0 - phi_L)
    if level == "tempered":
        return positions(fixed_point(ell0, phi_L, 0.0)[0])
    theta = learned_theta(ell0, [phi_L, lam * (1.0 - chi)])
    return positions(fixed_point(ell0, phi_L, theta)[0])


LAMBDAS = (0.25, 0.5, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 64, 128)
CUTS = {"between 2 and 3 (s = 0.375)": BOUNDS[1], "between 3 and 4 (s = 0.625)": BOUNDS[2],
        "between 4 and 5 (s = 0.875)": BOUNDS[3]}


def run(level, cut_t, lam_by_class):
    pred, obs, by_class = [], [], {}
    for (adj, iset, img, cls), it in items.items():
        p = model_profile(cls, it["prior"], lam_by_class[cls], cut_t, level)
        by_class.setdefault(cls, [[], []])
        by_class[cls][0].extend(p)
        by_class[cls][1].extend(it["post"])
        pred.extend(p)
        obs.extend(it["post"])
    return pred, obs, by_class


print("=" * 112)
print("6. THE MODEL AGAINST EXPERIMENT 3, ITEM BY ITEM. R^2 over the five positions of every item in")
print("   the class, at one Lambda for all classes; the relative cut is scanned separately below.")
print("   Their Table 5: LG .78 overall (.94 / .55 / .69), QF .82 overall (.97 / .58 / .78).")
print("=" * 112)
for cut_name, cut_t in CUTS.items():
    print(f"\n  relative cut {cut_name}")
    print(f"    {'Lambda':>7} | {'model: all':>10}{'max':>7}{'min':>7}{'rel':>7} | "
          f"{'q_lit: all':>11}{'max':>7}{'min':>7}{'rel':>7} | {'tempered: all':>14}")
    for lam in LAMBDAS:
        line = f"    {lam:>7g} |"
        for level in ("model", "literal", "tempered"):
            pred, obs, by_class = run(level, cut_t, {c: lam for c in
                                                     ("absolute_max", "absolute_min", "relative")})
            line += f" {pearson_r2(pred, obs):>10.3f}"
            if level != "tempered":
                for cls in ("absolute_max", "absolute_min", "relative"):
                    line += f"{pearson_r2(*by_class[cls]):>7.3f}"
            line += " |"
        print(line)


print()
print("=" * 112)
print("7. LAMBDA PER CLASS. The R^2 of a class depends only on that class's own Lambda, so each column")
print("   is its own scan. H1 predicts the ordering: the more of the threshold's location depends on")
print("   the unstable resolution delta, the weaker Lambda. max is anchored at the endpoint itself,")
print("   min at delta/2 above the other endpoint, rel at a context threshold with no atoms at all.")
print("=" * 112)
WIDE = (2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 256, 512, 2048)
for cut_name, cut_t in CUTS.items():
    print(f"\n  relative cut {cut_name}")
    print(f"    {'Lambda':>7}{'max':>9}{'min':>9}{'rel':>9}")
    best = {}
    for lam in WIDE:
        vals = {}
        for cls in ("absolute_max", "absolute_min", "relative"):
            pred, obs = [], []
            for (adj, iset, img, c), it in items.items():
                if c != cls:
                    continue
                pred.extend(model_profile(cls, it["prior"], lam, cut_t))
                obs.extend(it["post"])
            vals[cls] = pearson_r2(pred, obs)
            if vals[cls] > best.get(cls, (0, None))[0]:
                best[cls] = (vals[cls], lam)
        print(f"    {lam:>7g}" + "".join(f"{vals[c]:>9.3f}" for c in
                                         ("absolute_max", "absolute_min", "relative")))
    print("    best: " + ", ".join(f"{c.split('_')[-1]} Lambda {best[c][1]:g} (R^2 {best[c][0]:.3f})"
                                   for c in ("absolute_max", "absolute_min", "relative")))

print()
print("=" * 112)
print("8. CLASS PROFILES AT THE FITTED LAMBDA, against the data, split by image type.")
print("   Positions 1..5. 'data' is Experiment 3; 'model' is this model; 'q_lit' the literal listener.")
print("=" * 112)
FITTED = {"absolute_max": 8.0, "absolute_min": 32.0, "relative": 16.0}
CUT = BOUNDS[2]
print(f"   fitted Lambda: {FITTED}; relative cut between positions 3 and 4 (s = 0.625)")
for cls in ("absolute_max", "absolute_min", "relative"):
    for img in ("shape", "artifact"):
        keys = [k for k in items if k[3] == cls and k[2] == img]
        rowsum = {lvl: [0.0] * 5 for lvl in ("data", "prior", "q_lit", "model")}
        for k in keys:
            it = items[k]
            for i in range(5):
                rowsum["data"][i] += it["post"][i]
                rowsum["prior"][i] += it["prior"][i]
            for lvl, level in (("q_lit", "literal"), ("model", "model")):
                p = model_profile(cls, it["prior"], FITTED[cls], CUT, level)
                for i in range(5):
                    rowsum[lvl][i] += p[i]
        n = len(keys)
        print(f"\n   {cls:<13}{img:<10}({n} items)")
        for lvl in ("prior", "q_lit", "model", "data"):
            v = [x / n for x in rowsum[lvl]]
            print(f"     {lvl:<7}" + " ".join(f"{x:6.3f}" for x in v)
                  + f"   peak {1 + max(range(5), key=lambda i: v[i])}"
                  + f"   mean position {sum((i + 1) * x for i, x in enumerate(v)):.2f}")

print()
print("=" * 112)
print("9. THE IMAGE-TYPE EFFECT, class by class. Xiang et al. find a credible image-type effect for")
print("   the MINIMUM class only, in both experiments (Exp. 2: 2.54 [0.54, 4.38]; Exp. 3: 0.99")
print("   [0.45, 1.54] with a -1.08 [-1.56, -0.59] interaction with scale position), and none for")
print("   the maximum or relative classes. Here: the shape-minus-artifact difference in the mean")
print("   scale position, in the data and in the model.")
print("=" * 112)
print(f"   {'class':<14}{'data shape':>11}{'data artif':>11}{'data diff':>11}"
      f"{'model shape':>13}{'model artif':>13}{'model diff':>12}{'prior diff':>12}")
for cls in ("absolute_max", "absolute_min", "relative"):
    cells = {}
    for img in ("shape", "artifact"):
        keys = [k for k in items if k[3] == cls and k[2] == img]
        acc = {"data": 0.0, "model": 0.0, "prior": 0.0}
        for k in keys:
            it = items[k]
            acc["data"] += sum((i + 1) * x for i, x in enumerate(it["post"]))
            acc["prior"] += sum((i + 1) * x for i, x in enumerate(it["prior"]))
            p = model_profile(cls, it["prior"], FITTED[cls], CUT)
            acc["model"] += sum((i + 1) * x for i, x in enumerate(p))
        cells[img] = {k: v / len(keys) for k, v in acc.items()}
    print(f"   {cls:<14}{cells['shape']['data']:>11.2f}{cells['artifact']['data']:>11.2f}"
          f"{cells['shape']['data'] - cells['artifact']['data']:>+11.2f}"
          f"{cells['shape']['model']:>13.2f}{cells['artifact']['model']:>13.2f}"
          f"{cells['shape']['model'] - cells['artifact']['model']:>+12.2f}"
          f"{cells['shape']['prior'] - cells['artifact']['prior']:>+12.2f}")


print()
print("=" * 112)
print("10. THE MINIMUM CLASS, WHERE EVERY MODEL IN THEIR PAPER IS WEAKEST. Lambda against the two")
print("    image types separately, with the literal listener beside the model. The empirical means")
print("    are 3.29 (shape) and 4.42 (artifact), a difference of -1.13.")
print("=" * 112)
print(f"    {'Lambda':>7} | {'model shape':>12}{'model artif':>12}{'diff':>8}{'R2 shape':>10}{'R2 artif':>10}"
      f" | {'q_lit shape':>12}{'q_lit artif':>12}{'diff':>8}{'R2 shape':>10}{'R2 artif':>10}")
for lam in (0.5, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 64):
    line = f"    {lam:>7g} |"
    for level in ("model", "literal"):
        cells = {}
        for img in ("shape", "artifact"):
            keys = [k for k in items if k[3] == "absolute_min" and k[2] == img]
            pred, obs, mean = [], [], 0.0
            for k in keys:
                it = items[k]
                p = model_profile("absolute_min", it["prior"], lam, BOUNDS[2], level)
                pred.extend(p)
                obs.extend(it["post"])
                mean += sum((i + 1) * x for i, x in enumerate(p)) / len(keys)
            cells[img] = (mean, pearson_r2(pred, obs))
        line += (f"{cells['shape'][0]:>12.2f}{cells['artifact'][0]:>12.2f}"
                 f"{cells['shape'][0] - cells['artifact'][0]:>+8.2f}"
                 f"{cells['shape'][1]:>10.3f}{cells['artifact'][1]:>10.3f} |")
    print(line)

print()
print("=" * 112)
print("11. HOW MANY UTILITY DIRECTIONS (Appendix C). The same comparison at m = 2 (the model), and at")
print("    m = 3 and m = 4, which are MEASUREMENTS under the settled m = 2 and not a proposal.")
print("    Eq. (24)'s limit field is (1/2)(I + B B^T W)(ell_0 - phi_L): only the span(B) component of")
print("    the prior survives the utility level's amplification, so m bounds how much of a sharply")
print("    peaked prior can reach the settled belief.")
print("=" * 112)
B0, G0, mu0 = B, G, mu
print(f"    {'m':>3}{'max':>9}{'min':>9}{'rel':>9}{'overall':>10}   {'min: shape':>11}{'artif':>8}{'diff':>8}")
for m in (2, 3, 4):
    sub = Net(num_atoms=N_ATOMS, basis_degree=m)
    B, G = sub.basis, sub.basis.T @ (W[:, None] * sub.basis)
    mu = sub.mu_u
    globals()["B"], globals()["G"], globals()["mu"] = B, G, mu
    vals, allp, allo = {}, [], []
    for cls in ("absolute_max", "absolute_min", "relative"):
        pred, obs = [], []
        for (adj, iset, img, c), it in items.items():
            if c != cls:
                continue
            pred.extend(model_profile(cls, it["prior"], FITTED[cls], BOUNDS[2]))
            obs.extend(it["post"])
        vals[cls] = pearson_r2(pred, obs)
        allp.extend(pred)
        allo.extend(obs)
    means = {}
    for img in ("shape", "artifact"):
        keys = [k for k in items if k[3] == "absolute_min" and k[2] == img]
        means[img] = sum(sum((i + 1) * x for i, x in enumerate(
            model_profile("absolute_min", items[k]["prior"], FITTED["absolute_min"], BOUNDS[2])))
            for k in keys) / len(keys)
    print(f"    {m:>3}" + "".join(f"{vals[c]:>9.3f}" for c in
                                  ("absolute_max", "absolute_min", "relative"))
          + f"{pearson_r2(allp, allo):>10.3f}   {means['shape']:>11.2f}{means['artifact']:>8.2f}"
          f"{means['shape'] - means['artifact']:>+8.2f}")
print("    (data: -1.13)")
globals()["B"], globals()["G"], globals()["mu"] = B0, G0, mu0   # part 11 rebinds them; m = 2 again


print()
print("=" * 112)
print("12. THE INTERACTION sections_3-6.md §5.2 CLAIMS: is the difference BETWEEN classes larger in")
print("    one image condition? Mean scale position per class, and the largest gap between classes.")
print("    (The outline calls shapes the impoverished-prior condition. The authors report the")
print("    opposite about the priors themselves: 'artifacts tend to have a less categorical")
print("    distribution than shapes, in particular for the dimensions corresponding to absolute")
print("    adjectives', p. 9:19. The prior row below is their elicited prior.)")
print("=" * 112)
for source in ("prior", "data", "model"):
    print(f"    {source}")
    print(f"      {'':<10}{'max':>7}{'min':>7}{'rel':>7}{'max - min':>11}{'max - rel':>11}")
    for img in ("shape", "artifact"):
        means = {}
        for cls in ("absolute_max", "absolute_min", "relative"):
            keys = [k for k in items if k[3] == cls and k[2] == img]
            tot = 0.0
            for k in keys:
                it = items[k]
                v = (it["prior"] if source == "prior" else it["post"] if source == "data"
                     else model_profile(cls, it["prior"], FITTED[cls], BOUNDS[2]))
                tot += sum((i + 1) * x for i, x in enumerate(v))
            means[cls] = tot / len(keys)
        print(f"      {img:<10}{means['absolute_max']:>7.2f}{means['absolute_min']:>7.2f}"
              f"{means['relative']:>7.2f}"
              f"{means['absolute_max'] - means['absolute_min']:>11.2f}"
              f"{means['absolute_max'] - means['relative']:>11.2f}")


print()
print("=" * 112)
print("13. S-2: WHERE A RELATIVE ADJECTIVE'S CUT COULD COME FROM. Under S-1 only Lambda may be")
print("    fitted, so t has to be stipulated or derived. Four candidates, each with its own Lambda")
print("    scan over the relative class alone.")
print("=" * 112)


def prior_quantile_cut(p, level=0.5):
    """The node below which the elicited prior holds `level` of its mass, linear within a cell."""
    cum = 0.0
    for i in range(N_ATOMS + 1):
        if cum + p[i] >= level:
            frac = (level - cum) / p[i] if p[i] > 0 else 0.0
            lo = EDGES[i] if i > 0 else float(zeta[0])
            hi = EDGES[i + 1] if i < N_ATOMS else float(zeta[-1])
            return lo + frac * (hi - lo)
        cum += p[i]
    return float(zeta[-1])


def rel_profile(prior, lam, mode):
    if mode == "midpoint":
        t = 0.0
    elif mode == "prior median":
        t = prior_quantile_cut(prior, 0.5)
    elif mode == "prior upper quartile":
        t = prior_quantile_cut(prior, 0.75)
    else:
        t = mode
    return model_profile("relative", prior, lam, t)


REL = [k for k in items if k[3] == "relative"]
for label in ("midpoint", "prior median", "prior upper quartile",
              BOUNDS[1], BOUNDS[2], BOUNDS[3]):
    name = label if isinstance(label, str) else f"cell boundary s = {1 / (1 + math.exp(-label)):.3f}"
    best = (0.0, None)
    row = []
    for lam in (2, 4, 6, 8, 12, 16, 24, 32, 64, 128):
        pred, obs = [], []
        for k in REL:
            pred.extend(rel_profile(items[k]["prior"], lam, label))
            obs.extend(items[k]["post"])
        r2 = pearson_r2(pred, obs)
        row.append(r2)
        if r2 > best[0]:
            best = (r2, lam)
    print(f"    {name:<28}" + " ".join(f"{v:5.3f}" for v in row)
          + f"   best R^2 {best[0]:.3f} at Lambda {best[1]:g}")
print("    (Lambda = 2, 4, 6, 8, 12, 16, 24, 32, 64, 128 across the row)")

print()
print("=" * 112)
print("14. S-7: THE PARITY OF THE ENTRIES' LOADINGS, kappa = B^T W chi, at n = 4. The three classes")
print("    of H2, each with the complement its antonym supplies. A cut at the midpoint of the")
print("    log-odds scale has no even component at all, which is the parity result §5.2 now states.")
print("=" * 112)
print(f"    {'entry':<34}{'cut (s)':>9}{'tilt':>10}{'width':>10}{'|width/tilt|':>14}")
ENTRIES = [("MAX  = all,  excl. zeta < theta_L", CHI_ALL, 1 - 1 / (2 * N_ATOMS)),
           ("   its antonym, the O corner", 1.0 - CHI_ALL, 1 - 1 / (2 * N_ATOMS)),
           ("MIN  = some, excl. zeta <= -theta_L", CHI_SOME, 1 / (2 * N_ATOMS)),
           ("   its antonym, no", 1.0 - CHI_SOME, 1 / (2 * N_ATOMS)),
           ("REL  cut at the midpoint", chi_cut(0.0), 0.5),
           ("   its antonym", 1.0 - chi_cut(0.0), 0.5),
           ("REL  cut at s = 0.625", chi_cut(BOUNDS[2]), 0.625),
           ("REL  cut at s = 0.375", chi_cut(BOUNDS[1]), 0.375)]
ODD = next(j for j in range(B.shape[1]) if float((B[:, j] + B[:, j].flip(0)).abs().max()) < 1e-9)
EVEN = next(j for j in range(B.shape[1]) if float((B[:, j] - B[:, j].flip(0)).abs().max()) < 1e-9)
for label, chi, cut in ENTRIES:
    kappa = B.T @ (W * chi)
    tilt, width = float(kappa[ODD]), float(kappa[EVEN])
    ratio = "-" if abs(tilt) < 1e-12 else f"{abs(width / tilt):.3f}"
    print(f"    {label:<34}{cut:>9.3f}{tilt:>+10.5f}{width:>+10.5f}{ratio:>14}")
print("    (a node lying exactly on a cut is half-weighted, which is what returns the midpoint")
print("     cut's width to machine precision)")

print()
print("=" * 112)
print("15. S-2 and Appendix C §5: HOW MANY UTILITY DIRECTIONS EACH OF THESE INVENTORIES FORCES.")
print("    Appendix C §5 counts the span of the entries modulo the constant. A complementary pair")
print("    spans 1, whatever its cut, so none of H2's inventories forces m = 2; the model carries")
print("    m = 2 as a property of the architecture.")
print("=" * 112)
print(f"    {'inventory':<40}{'thresholds':>11}{'span mod 1':>12}{'kappa_1 + kappa_2':>19}")
for label, chi in (("complete scale, MAX and its antonym", CHI_ALL),
                   ("complete scale, MIN and its antonym", CHI_SOME),
                   ("open scale, REL(midpoint) and antonym", chi_cut(0.0)),
                   ("open scale, REL(s = 0.625) and antonym", chi_cut(BOUNDS[2]))):
    pair = torch.stack([chi, 1.0 - chi], dim=1)
    centred = pair - (W[:, None] * pair).sum(0) / W.sum()
    span = int(torch.linalg.matrix_rank(centred.T @ (W[:, None] * centred), rtol=1e-9))
    k1, k2 = B.T @ (W * chi), B.T @ (W * (1.0 - chi))
    print(f"    {label:<40}{1:>11}{span:>12}"
          f"{float((k1 + k2).abs().max()):>19.1e}")
print("    (the last column is |kappa(chi) + kappa(1 - chi)|: B is orthogonal to the constant, so")
print("     an antonym's loading is exactly the negative of the entry's, and the pair is a")
print("     reflection about the prior's own coupling rather than a collapse of the kind Eq. (C3)")
print("     reports for an odd m = 1 basis)")
