"""O13, follow-up: is the image-type effect about Lambda at all, or about whether the utility
level engages? Compares the three beliefs per (class, image type) at the model's own cut.

    .venv/bin/python audits/2026-09-22-o13-options/o13_levels.py

Class (e) until a cell prints it (C6). Evidence for the user's decision, not a change.
"""
import csv, math, torch, nbformat
exec(open("audits/2026-09-22-o13-options/o13_options.py").read().split('print("=" * 104)')[0])

LEVELS = ("q_lit", "tempered", "model")


def predict3(cls, cells, lam, level):
    net = base.respawn(base_prior=elicited(cells), lexical_strength=lam)
    chi = chi_of(cls, THETA_L)
    phi_L = lam * chi
    if level == "q_lit":
        return masses(net, net.base_log_prior - phi_L), float("nan")
    th = 0.0 if level == "tempered" else maximizer(net, [phi_L, lam * (1.0 - chi)])
    return masses(net, fixed_point(net, phi_L, th)), th


def cell_scores(cls, img, lam):
    keys = [k for k in KEYS[cls] if k[2] == img]
    out = {}
    for lev in LEVELS:
        p, o, thetas, meanpos = [], [], [], 0.0
        for k in keys:
            it = items[k]
            pr, th = predict3(cls, it["prior"], lam, lev)
            if th == th:
                thetas.append(th)
            meanpos += sum((i + 1) * x for i, x in enumerate(pr)) / len(keys)
            for i in range(5):
                if it["obs"][i]:
                    p.append(pr[i]); o.append(it["data"][i])
        out[lev] = (r2(p, o), meanpos, (sum(thetas) / len(thetas)) if thetas else float("nan"))
    dm = sum(sum((i + 1) * x for i, x in enumerate(items[k]["data"])) for k in keys) / len(keys)
    return out, dm, len(keys)


print("=" * 104)
print("5.  THE THREE BELIEFS PER (CLASS, IMAGE TYPE), at Lambda = 48 (the best shared value).")
print("    q_lit is the literal listener ell_0 - phi_L; 'tempered' is theta_u = 0, a control;")
print("    'model' is theta_u*. R^2 is within that cell only, so compare DOWN a column, not across.")
print("=" * 104)
print(f"    {'class':<14}{'image':<10}{'n':>4}"
      + "".join(f"{l + ' R2':>13}" for l in LEVELS)
      + f"{'data mean':>11}" + "".join(f"{l + ' mean':>14}" for l in LEVELS) + f"{'mean theta_u*':>15}")
for cls in CLASSES:
    for img in ("shape", "artifact"):
        sc, dm, n = cell_scores(cls, img, 48.0)
        print(f"    {cls:<14}{img:<10}{n:>4}"
              + "".join(f"{sc[l][0]:>13.3f}" for l in LEVELS)
              + f"{dm:>11.2f}" + "".join(f"{sc[l][1]:>14.2f}" for l in LEVELS)
              + f"{sc['model'][2]:>15.1f}")

print()
print("=" * 104)
print("6.  WHICH BELIEF EACH CONDITION'S DATA SIT NEAREST, in mean scale position.")
print("=" * 104)
for cls in CLASSES:
    for img in ("shape", "artifact"):
        sc, dm, n = cell_scores(cls, img, 48.0)
        gaps = {l: abs(dm - sc[l][1]) for l in LEVELS}
        near = min(gaps, key=gaps.get)
        print(f"    {cls:<14}{img:<10} data {dm:.2f} | "
              + ", ".join(f"{l} {sc[l][1]:.2f} (off by {gaps[l]:+.2f})" for l in LEVELS)
              + f"  ->  nearest: {near.upper()}")

print()
print("=" * 104)
print("7.  DOES A PER-IMAGE-TYPE Lambda REACH WHAT THE LEVELS REACH? Best Lambda per cell, with")
print("    the best R^2 any of the three beliefs reaches in that cell at ANY Lambda on the ladder.")
print("=" * 104)
LAM = (2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 256, 512, 2048)
print(f"    {'class':<14}{'image':<10}{'best model':>22}{'best q_lit':>22}")
for cls in CLASSES:
    for img in ("shape", "artifact"):
        row = {}
        for lev in ("model", "q_lit"):
            vals = {}
            for lam in LAM:
                sc, dm, n = cell_scores(cls, img, float(lam))
                vals[lam] = sc[lev][0]
            bl = max(vals, key=vals.get)
            row[lev] = (vals[bl], bl)
        print(f"    {cls:<14}{img:<10}"
              + "".join(f"{f'{row[l][0]:.3f} at Lambda {row[l][1]:g}':>22}" for l in ("model", "q_lit")))
