"""Audit 2026-09-13, preliminary (revisions.md Q6/R15): why the mode of phi_S* moves up the scale.

Run from the project folder:  .venv/bin/python audits/2026-09-13-delta-criteria/mode_mechanism.py

By Eq. (23), phi_S*(theta_u) - phi_S*(0) = (theta_u/2) B phi_u*, so the utility level's field u lies in
span(B), and the tempered field phi_S*(0) has the literal listener's mode. Split u into B's odd (tilt)
and even (width) columns, add each alone to the tempered field, and ask which one moves the mode and
which one moves the all-region q-mass. Under "some", each configuration at its own theta_u*.
A first-order check: at a smooth peak zeta_0 of the tempered field f, adding g moves the mode by about
g'(zeta_0) / (-f''(zeta_0)), so the sign of the shift is the sign of the added field's slope there.
Nothing here is written back into the notebooks.
"""
import ast
import math

import nbformat
import torch

BAND = 1e-12

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)
for node in ast.parse(nb.cells[7].source).body:
    wanted = isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)) or (
        isinstance(node, ast.Assign)
        and all(isinstance(t, ast.Name) and t.id.isupper() for t in node.targets)
    )
    if wanted:
        try:
            exec(compile(ast.Module([node], []), "code_cell_2", "exec"), ns)
        except Exception as exc:
            print("skipped from Code Cell 2:", ast.unparse(node)[:60], type(exc).__name__, exc)

net = ns["LexicalPredictiveCodingNetwork"]()
beta_world_prior = ns["beta_world_prior"]

zeta = net.zeta
assert torch.allclose(zeta, -zeta.flip(0)), "grid is not symmetric; parity test invalid"
parity = []
for j in range(net.basis.shape[1]):
    column = net.basis[:, j]
    if float((column + column.flip(0)).abs().max()) < 1e-9:
        parity.append("odd")
    elif float((column - column.flip(0)).abs().max()) < 1e-9:
        parity.append("even")
    else:
        parity.append("mixed")
print("columns of B:", parity)
ODD, EVEN = parity.index("odd"), parity.index("even")


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def analyse(probe):
    phi_S, phi_u = probe.closed_form_fixed_point("some")
    tempered = probe.closed_form_fixed_point("some", theta_u=0.0)[0]
    literal = probe.literal_fixed_point("some")
    u = phi_S - tempered
    B, w = probe.basis, probe.weights
    gram = B.T @ (w[:, None] * B)
    c = torch.linalg.solve(gram, B.T @ (w * u))
    tilt, width = B[:, ODD] * c[ODD], B[:, EVEN] * c[EVEN]
    upper = (probe.zeta > probe.theta_L).to(probe.dtype)

    def mass(field):
        return float((w * probe.read_out(field) * upper).sum())

    def mode_s(field):
        return sigmoid(float(probe.zeta[int(torch.argmax(field))]))

    k0 = int(torch.argmax(tempered))
    k0 = min(max(k0, 1), len(zeta) - 2)
    dz = float(zeta[k0 + 1] - zeta[k0 - 1])
    slope = lambda g: float(g[k0 + 1] - g[k0 - 1]) / dz
    return {
        "theta": float(probe.theta_u), "c_tilt": float(c[ODD]), "c_width": float(c[EVEN]),
        "residual": float((u - B @ c).abs().max()),
        "s_temp": mode_s(tempered), "s_tilt": mode_s(tempered + tilt),
        "s_width": mode_s(tempered + width), "s_full": mode_s(phi_S),
        "m_lit": mass(literal), "m_temp": mass(tempered), "m_tilt": mass(tempered + tilt),
        "m_width": mass(tempered + width), "m_full": mass(phi_S),
        "slope_tilt": slope(tilt), "slope_width": slope(width), "k_full": int(torch.argmax(phi_S)),
        "k_temp": int(torch.argmax(tempered)),
    }


def sign(x, band=0.0):
    return "+" if x > band else "-" if x < -band else "0"


print()
print("PART D ROWS (under \"some\"): mode in s, and all-region q-mass, for the tempered field alone,")
print("with the tilt part added, with the width part added, and with both (the model)")
print(f"  {'prior':<12}{'c_tilt':>9}{'c_width':>9} | {'mode tmp':>8}{'+tilt':>7}{'+width':>7}{'full':>7} |"
      f" {'mass tmp':>8}{'+tilt':>8}{'+width':>8}{'full':>8} | slope t/w at mode")
for name, spec in ns["part_d_priors"]().items():
    prior, overrides = spec if isinstance(spec, tuple) else (spec, {})
    r = analyse(net.respawn(base_prior=prior, **overrides))
    print(f"  {name:<12}{r['c_tilt']:>+9.2f}{r['c_width']:>+9.2f} | {r['s_temp']:>8.4f}{r['s_tilt']:>7.4f}"
          f"{r['s_width']:>7.4f}{r['s_full']:>7.4f} | {r['m_temp']:>8.4f}{r['m_tilt']:>8.4f}{r['m_width']:>8.4f}"
          f"{r['m_full']:>8.4f} | {r['slope_tilt']:+.3g} / {r['slope_width']:+.3g}   (span-B residual {r['residual']:.1e})")

alphas = [2.0 ** k for k in range(11)]
lambdas = [2.0 ** k for k in range(1, 12)]
rows = []
for alpha in alphas:
    prior = beta_world_prior(alpha, 1.0)
    for strength in lambdas:
        r = analyse(net.respawn(base_prior=prior, lexical_strength=strength))
        r["alpha"], r["Lambda"] = alpha, strength
        r["q1"] = (r["m_full"] - r["m_lit"]) < -BAND
        r["da"] = r["k_full"] < r["k_temp"]
        rows.append(r)

print()
print(f"PLANE, {len(rows)} cells, under \"some\"")
print(f"  largest span-B residual of the utility field: {max(r['residual'] for r in rows):.1e}")
print("  sign of the coefficients (tilt, width): "
      + ", ".join(f"({a},{b}) {sum(1 for r in rows if sign(r['c_tilt'])==a and sign(r['c_width'])==b)}"
                  for a in "+-" for b in "+-"))
up = [r for r in rows if r["k_full"] > r["k_temp"]]
down = [r for r in rows if r["k_full"] < r["k_temp"]]
still = [r for r in rows if r["k_full"] == r["k_temp"]]
print(f"  mode of the model against the tempered (= literal) mode: up {len(up)}, down {len(down)}, unmoved {len(still)}")
for label, group in (("up", up), ("down", down)):
    if not group:
        continue
    t_same = sum(1 for r in group if sign(r["s_tilt"] - r["s_temp"], 1e-12) == ("+" if label == "up" else "-"))
    w_same = sum(1 for r in group if sign(r["s_width"] - r["s_temp"], 1e-12) == ("+" if label == "up" else "-"))
    first = sum(1 for r in group if sign(r["slope_tilt"] + r["slope_width"]) == ("+" if label == "up" else "-"))
    print(f"    {label}: tilt alone moves it the same way in {t_same}, width alone in {w_same}; "
          f"first-order slope sign agrees in {first} of {len(group)}")
lower_t = sum(1 for r in rows if r["m_tilt"] < r["m_temp"] - BAND)
lower_w = sum(1 for r in rows if r["m_width"] < r["m_temp"] - BAND)
print(f"  all-region q-mass below the tempered field's: tilt alone in {lower_t}, width alone in {lower_w}, "
      f"model in {sum(1 for r in rows if r['m_full'] < r['m_temp'] - BAND)}")
split = [r for r in rows if r["q1"] and not r["da"]]
print(f"  the {len(split)} cells where q's first condition holds and criterion (a) does not:")
print(f"    {'alpha':>6}{'Lambda':>7}{'c_tilt':>9}{'c_width':>9}{'mode tmp':>9}{'+tilt':>7}{'+width':>7}{'full':>7}"
      f"{'mass tmp':>9}{'+tilt':>8}{'+width':>8}{'full':>8}")
for r in split:
    print(f"    {r['alpha']:>6.0f}{r['Lambda']:>7.0f}{r['c_tilt']:>+9.2f}{r['c_width']:>+9.2f}{r['s_temp']:>9.4f}"
          f"{r['s_tilt']:>7.4f}{r['s_width']:>7.4f}{r['s_full']:>7.4f}{r['m_temp']:>9.4f}{r['m_tilt']:>8.4f}"
          f"{r['m_width']:>8.4f}{r['m_full']:>8.4f}")
print("  down cells, where the literal mode sits (s):",
      sorted({round(r["s_temp"], 4) for r in down}))
print("  up cells, where the literal mode sits (s):",
      sorted({round(r["s_temp"], 4) for r in up}))
