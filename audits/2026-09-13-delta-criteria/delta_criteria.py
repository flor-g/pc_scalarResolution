"""Audit 2026-09-13: the delta read-out's two criteria against Part C's two q criteria.

Run from the project folder:  .venv/bin/python audits/2026-09-13-delta-criteria/delta_criteria.py

Criteria, all under "some", each configuration at its own learned theta_u*:
  q1  shift < 0            P(all-region; q_H) - P(all-region; q_lit)  (Eq. 37), 1e-12 zero band (I5)
  q2  q_H < 1/2            P(all-region; q_H)
  da  mode(phi_S*) - mode(ell_0) < 0     (user's definition; also reported against mode(ell_0 - phi_L))
  db  mode(phi_S*) outside the cell of "all", zeta < theta_L
The mode is the grid node where the field is largest (Code Cell 2's delta read-out).
Nothing here is written back into the notebooks.
"""
import ast
import math

import nbformat
import numpy as np
import torch

BAND = 1e-12

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)
# Code Cell 2: imports, definitions and upper-case constants only, so RUN does not execute.
for node in ast.parse(nb.cells[7].source).body:
    wanted = isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)) or (
        isinstance(node, ast.Assign)
        and all(isinstance(t, ast.Name) and t.id.isupper() for t in node.targets)
    )
    if wanted:
        try:
            exec(compile(ast.Module([node], []), "code_cell_2", "exec"), ns)
        except Exception as exc:  # reported, not hidden
            print("skipped from Code Cell 2:", ast.unparse(node)[:60], type(exc).__name__, exc)

net = ns["LexicalPredictiveCodingNetwork"]()
beta_world_prior = ns["beta_world_prior"]


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def mode(field):
    values = field.detach().double()
    order = torch.sort(values, descending=True).values
    return int(torch.argmax(values)), float(order[0] - order[1])


def record(probe):
    zeta, theta_L = probe.zeta, float(probe.theta_L)
    upper = (probe.zeta > probe.theta_L).to(probe.dtype)
    phi_S = probe.closed_form_fixed_point("some")[0]
    literal = probe.literal_fixed_point("some")
    tempered = probe.closed_form_fixed_point("some", theta_u=0.0)[0]

    def mass(field):
        return float((probe.weights * probe.read_out(field) * upper).sum())

    q_H, q_lit, q_tmp = mass(phi_S), mass(literal), mass(tempered)
    k_S, gap_S = mode(phi_S)
    k_0, gap_0 = mode(probe.base_log_prior)
    k_L, gap_L = mode(literal)
    z_S, z_0, z_L = float(zeta[k_S]), float(zeta[k_0]), float(zeta[k_L])
    shift = q_H - q_lit
    return {
        "theta": float(probe.theta_u), "q_H": q_H, "q_lit": q_lit, "shift": shift,
        "tempering": q_tmp - q_lit, "utility": q_H - q_tmp,
        "q1": shift < -BAND, "q2": q_H < 0.5,
        "s_S": sigmoid(z_S), "s_0": sigmoid(z_0), "s_L": sigmoid(z_L),
        "mode_shift": z_S - z_0, "mode_shift_lit": z_S - z_L,
        "da": z_S < z_0, "da_lit": z_S < z_L, "db": z_S < theta_L,
        "min_gap": min(gap_S, gap_0, gap_L), "k_S": k_S, "k_0": k_0, "k_L": k_L,
    }


def yn(flag):
    return "yes" if flag else "no"


# ---------------------------------------------------------------- Part D's five rows
print("PART D ROWS, under \"some\" (reproduces Code Cell 2 where it prints the same quantity)")
print(f"  {'prior':<12}{'theta_u*':>11}{'q_H':>8}{'shift':>9}{'q1':>4}{'q2':>4}"
      f"{'mode l0':>9}{'mode lit':>9}{'mode phi':>9}{'da':>4}{'db':>4}")
for name, spec in ns["part_d_priors"]().items():
    prior, overrides = spec if isinstance(spec, tuple) else (spec, {})
    r = record(net.respawn(base_prior=prior, **overrides))
    print(f"  {name:<12}{r['theta']:>11.4f}{r['q_H']:>8.4f}{r['shift']:>+9.4f}{yn(r['q1']):>4}{yn(r['q2']):>4}"
          f"{r['s_0']:>9.4f}{r['s_L']:>9.4f}{r['s_S']:>9.4f}{yn(r['da']):>4}{yn(r['db']):>4}")
print()

# ---------------------------------------------------------------- the plane
alphas = [2.0 ** k for k in range(11)]
lambdas = [2.0 ** k for k in range(1, 12)]
cells = {}
for alpha in alphas:
    prior = beta_world_prior(alpha, 1.0)
    for strength in lambdas:
        cells[(alpha, strength)] = record(net.respawn(base_prior=prior, lexical_strength=strength))

rows = list(cells.items())
count = lambda key: sum(1 for _, r in rows if r[key])
print(f"PLANE, {len(rows)} cells (alpha = 1..1024, Lambda = 2..2048), under \"some\"")
print(f"  q1 {count('q1')}, q2 {count('q2')}, both {sum(1 for _, r in rows if r['q1'] and r['q2'])}"
      "   (Code Cell 4 prints second condition 59, both 33)")
print(f"  da {count('da')}, db {count('db')}, both {sum(1 for _, r in rows if r['da'] and r['db'])}")
print(f"  da against mode(ell_0 - phi_L) instead of mode(ell_0): {count('da_lit')} "
      f"(modes of ell_0 and ell_0 - phi_L differ in {sum(1 for _, r in rows if r['k_0'] != r['k_L'])} cells)")
print(f"  mode of phi_S* unmoved from mode(ell_0) (shift exactly 0, so da not met): "
      f"{sum(1 for _, r in rows if r['k_S'] == r['k_0'])} cells")
print(f"  smallest gap between the largest and second-largest node over all modes: "
      f"{min(r['min_gap'] for _, r in rows):.2e}")
print()


def crosstab(a, b, label):
    tab = {(x, y): sum(1 for _, r in rows if r[a] == x and r[b] == y) for x in (True, False) for y in (True, False)}
    print(f"  {label}: both met {tab[(True, True)]}, only {a} {tab[(True, False)]}, "
          f"only {b} {tab[(False, True)]}, neither {tab[(False, False)]}")


print("AGREEMENT")
crosstab("q1", "da", "first conditions (q1 vs da)")
crosstab("q2", "db", "second conditions (q2 vs db)")
for _, r in rows:
    r["q_both"], r["d_both"] = r["q1"] and r["q2"], r["da"] and r["db"]
crosstab("q_both", "d_both", "conjunctions")
print()

print("CELLS WHERE THE READ-OUTS DISAGREE")
print(f"  {'alpha':>6}{'Lambda':>7}{'theta_u*':>12}{'q_H':>8}{'shift':>9}{'temper':>9}{'utility':>9}"
      f"{'mode l0':>9}{'mode phi':>9}  q1 da  q2 db")
for (alpha, strength), r in rows:
    if r["q1"] != r["da"] or r["q2"] != r["db"]:
        print(f"  {alpha:>6.0f}{strength:>7.0f}{r['theta']:>12.2f}{r['q_H']:>8.4f}{r['shift']:>+9.4f}"
              f"{r['tempering']:>+9.4f}{r['utility']:>+9.4f}{r['s_0']:>9.4f}{r['s_S']:>9.4f}"
              f"  {yn(r['q1']):>3}{yn(r['da']):>3} {yn(r['q2']):>3}{yn(r['db']):>3}")
print()

print("FLOORS AND THE V: least Lambda from which a condition holds at every larger Lambda on the grid")


def floor(alpha, key):
    held = [cells[(alpha, s)][key] for s in lambdas]
    for j in range(len(lambdas)):
        if all(held[j:]):
            return lambdas[j], all(held[j:]) and not any(held[:j])
    return None, not any(held)


print(f"  {'alpha':>6} | {'q1':>6}{'q2':>6}{'q both':>8} | {'da':>6}{'db':>6}{'d both':>8}   (* = not upward closed)")
for alpha in alphas:
    out = []
    for key in ("q1", "q2", "q_both", "da", "db", "d_both"):
        value, clean = floor(alpha, key)
        out.append(("-" if value is None else f"{value:.0f}") + ("" if clean else "*"))
    print(f"  {alpha:>6.0f} | {out[0]:>6}{out[1]:>6}{out[2]:>8} | {out[3]:>6}{out[4]:>6}{out[5]:>8}")
