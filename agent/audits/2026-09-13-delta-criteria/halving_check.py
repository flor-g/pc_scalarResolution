"""Audit 2026-09-13 (procedure_records/delta_criteria_printing.md T3 prerequisite): does Eq. (24)'s
halving hold across the plane, and does the limit field carry F4's reading cell by cell?

Run from the project folder:  .venv/bin/python audits/2026-09-13-delta-criteria/halving_check.py

Under "some", each configuration at its own theta_u*:
  c  = B^T W (ell_0 - phi_L), the literal field's projection (Appendix B's c_y)
  k  = the utility field's coefficients in B, fitted from phi_S* - phi_S*(0)  (= (theta_u/2) phi_u*, Eq. 23)
  At sigma = 1 and B^T W B = I, Eqs. (15)-(16) give exactly
      k = (theta/2) (mu_u + (theta/2) c) / (1 + theta^2/2),   so   k - c/2 = ((theta/2) mu_u - c/2) / (1 + theta^2/2),
  and Eq. (24) is the limit k -> c/2. The limit field is L = (ell_0 - phi_L)/2 + B c/2.
Checked: the size of k - c/2 against c/2 per column; sign(k) = sign(c); whether L has the model's mode
node; whether criteria (a), (b) and q's two conditions read the same off L as off the model.
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
ODD, EVEN = None, None
for j in range(net.basis.shape[1]):
    col = net.basis[:, j]
    if float((col + col.flip(0)).abs().max()) < 1e-9:
        ODD = j
    elif float((col - col.flip(0)).abs().max()) < 1e-9:
        EVEN = j
assert ODD is not None and EVEN is not None


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def analyse(probe):
    assert probe.sigma_lexical == probe.sigma_state == probe.sigma_utility == 1.0
    B, w, theta = probe.basis, probe.weights, float(probe.theta_u)
    gram = B.T @ (w[:, None] * B)
    literal = probe.literal_fixed_point("some")                 # ell_0 - phi_L
    c = B.T @ (w * literal)
    phi_S, phi_u = probe.closed_form_fixed_point("some")
    tempered = probe.closed_form_fixed_point("some", theta_u=0.0)[0]
    k = torch.linalg.solve(gram, B.T @ (w * (phi_S - tempered)))
    k_formula = (theta / 2) * (probe.mu_u + (theta / 2) * c) / (1 + theta ** 2 / 2)
    limit = tempered + B @ (c / 2)
    upper = (probe.zeta > probe.theta_L).to(probe.dtype)

    def mass(field):
        return float((w * probe.read_out(field) * upper).sum())

    k_model, k_limit, k_0 = int(torch.argmax(phi_S)), int(torch.argmax(limit)), int(torch.argmax(probe.base_log_prior))
    theta_L = float(probe.theta_L)
    m_lit, m_model, m_limit = mass(literal), mass(phi_S), mass(limit)
    verdicts = lambda node, m: (
        node < k_0,                          # (a)
        float(probe.zeta[node]) < theta_L,   # (b)
        (m - m_lit) < -BAND,                 # q first
        m < 0.5,                             # q second
    )
    rel = [abs(float(k[j] - c[j] / 2)) / abs(float(c[j] / 2)) for j in (ODD, EVEN)]
    return {
        "theta": theta, "c": (float(c[ODD]), float(c[EVEN])), "k": (float(k[ODD]), float(k[EVEN])),
        "rel_tilt": rel[0], "rel_width": rel[1],
        "gram_err": float((gram - torch.eye(gram.shape[0], dtype=gram.dtype)).abs().max()),
        "formula_err": float((k - k_formula).abs().max()),
        "sign_ok": all((float(k[j]) > 0) == (float(c[j]) > 0) for j in (ODD, EVEN)),
        "node_same": k_model == k_limit, "node_gap": abs(k_model - k_limit),
        "s_model": sigmoid(float(probe.zeta[k_model])), "s_limit": sigmoid(float(probe.zeta[k_limit])),
        "v_model": verdicts(k_model, m_model), "v_limit": verdicts(k_limit, m_limit),
        "m_model": m_model, "m_limit": m_limit,
    }


print("PART D ROWS, under \"some\"")
print(f"  {'prior':<12}{'theta_u*':>11}{'c tilt':>10}{'c width':>10}{'k tilt':>10}{'k width':>10}"
      f"{'rel t':>9}{'rel w':>9}{'mode':>8}{'mode L':>8}{'mass':>8}{'mass L':>8}  verdicts a,b,q1,q2 same")
for name, spec in ns["part_d_priors"]().items():
    prior, overrides = spec if isinstance(spec, tuple) else (spec, {})
    r = analyse(net.respawn(base_prior=prior, **overrides))
    print(f"  {name:<12}{r['theta']:>11.2f}{r['c'][0]:>+10.2f}{r['c'][1]:>+10.2f}{r['k'][0]:>+10.2f}{r['k'][1]:>+10.2f}"
          f"{r['rel_tilt']:>9.1e}{r['rel_width']:>9.1e}{r['s_model']:>8.4f}{r['s_limit']:>8.4f}"
          f"{r['m_model']:>8.4f}{r['m_limit']:>8.4f}  {r['v_model'] == r['v_limit']}")

rows = []
for alpha in [2.0 ** i for i in range(11)]:
    prior = beta_world_prior(alpha, 1.0)
    for strength in [2.0 ** i for i in range(1, 12)]:
        r = analyse(net.respawn(base_prior=prior, lexical_strength=strength))
        r["alpha"], r["Lambda"] = alpha, strength
        rows.append(r)

n = len(rows)
print()
print(f"PLANE, {n} cells, under \"some\"")
print(f"  B^T W B = I to {max(r['gram_err'] for r in rows):.1e}; fitted k against the exact formula to "
      f"{max(r['formula_err'] / max(1.0, max(abs(x) for x in r['k'])) for r in rows):.1e} (relative)")
print(f"  |k - c/2| / |c/2|: tilt max {max(r['rel_tilt'] for r in rows):.2e}, "
      f"width max {max(r['rel_width'] for r in rows):.2e}; "
      f"median tilt {sorted(r['rel_tilt'] for r in rows)[n // 2]:.2e}, width {sorted(r['rel_width'] for r in rows)[n // 2]:.2e}")
for bound in (1e-1, 1e-2, 1e-3):
    print(f"    cells with both columns within {bound:g} of c/2: "
          f"{sum(1 for r in rows if r['rel_tilt'] < bound and r['rel_width'] < bound)}")
print(f"  sign(k) = sign(c) in both columns: {sum(1 for r in rows if r['sign_ok'])} of {n}")
print("  sign of c (tilt, width): "
      + ", ".join(f"({a},{b}) {sum(1 for r in rows if (r['c'][0] > 0) == (a == '+') and (r['c'][1] > 0) == (b == '+'))}"
                  for a in "+-" for b in "+-"))
print(f"  mode node of the limit field = the model's: {sum(1 for r in rows if r['node_same'])} of {n}; "
      f"largest node gap {max(r['node_gap'] for r in rows)}")
for idx, label in enumerate(("(a)", "(b)", "q first", "q second")):
    print(f"  verdict {label:<9} the same off the limit field as off the model: "
          f"{sum(1 for r in rows if r['v_model'][idx] == r['v_limit'][idx])} of {n}")
print(f"  all four verdicts the same: {sum(1 for r in rows if r['v_model'] == r['v_limit'])} of {n}")
print()
print("  the ten cells furthest from the halving (largest of the two relative gaps):")
print(f"    {'alpha':>6}{'Lambda':>7}{'theta_u*':>11}{'c tilt':>10}{'c width':>10}{'k tilt':>10}{'k width':>10}"
      f"{'rel t':>9}{'rel w':>9}{'mode':>8}{'mode L':>8}  same verdicts")
for r in sorted(rows, key=lambda r: -max(r["rel_tilt"], r["rel_width"]))[:10]:
    print(f"    {r['alpha']:>6.0f}{r['Lambda']:>7.0f}{r['theta']:>11.2f}{r['c'][0]:>+10.2f}{r['c'][1]:>+10.2f}"
          f"{r['k'][0]:>+10.2f}{r['k'][1]:>+10.2f}{r['rel_tilt']:>9.1e}{r['rel_width']:>9.1e}"
          f"{r['s_model']:>8.4f}{r['s_limit']:>8.4f}  {r['v_model'] == r['v_limit']}")
disagree = [r for r in rows if r["v_model"] != r["v_limit"] or not r["node_same"]]
if disagree:
    print("  cells where the limit field's mode node or a verdict differs from the model's:")
    for r in disagree:
        print(f"    ({r['alpha']:.0f}, {r['Lambda']:.0f}) theta_u* {r['theta']:.2f}: mode {r['s_model']:.4f} vs {r['s_limit']:.4f}; "
              f"verdicts model {r['v_model']} limit {r['v_limit']}")
