"""Audit 2026-09-13: sections_3-6.md §5.2 (closed vs open scale, endpoint orientation) against the
current model. Nothing here is written back into the notebooks.

Run from the project folder:  .venv/bin/python audits/2026-09-13-scale-structure/scale_structure.py

A single-threshold predicate with its cut at proportion s_t excludes the states below the cut,
chi_t = 1[zeta < logit s_t] (the §5.2 convention; a node lying exactly on the cut gets weight 1/2),
phi_L = Lambda chi_t, Lambda = 8, mu_u = the network default, every sigma = 1.
Fixed points from Eqs. (15)-(16) in the general form of Code Cell 1's closed_form_fixed_point:
    c = B^T W (ell_0 - phi_L),   (I + theta^2 G / 2) phi_u = mu_u + theta c / 2,   phi_S = [(ell_0 - phi_L) + theta B phi_u] / 2
"Utility contribution to posterior degree" = E_q[s] at theta minus E_q[s] at theta = 0 (the tempered field).
Reported at theta_u = 1 (a control, to reproduce §5.2's numbers), at theta_u = -28.4375 (the default
prior's theta_u*, carried: F9/F23's mistake, tested only as a hypothesis for §5.2's "theta_u*" column),
at Eq. (24)'s limit |theta_u| -> inf (theta-free; record F5 shows it decides every verdict on the plane),
and at the theta_u* of two ILLUSTRATIVE exposure ensembles (no decision is implied by either).
"""
import ast
import math

import nbformat
import torch

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

Net = ns["LexicalPredictiveCodingNetwork"]
net = Net()
zeta, W, B = net.zeta, net.weights, net.basis
assert net.sigma_lexical == net.sigma_state == net.sigma_utility == 1.0
G = B.T @ (W[:, None] * B)
mu = net.mu_u
ODD = next(j for j in range(B.shape[1]) if float((B[:, j] + B[:, j].flip(0)).abs().max()) < 1e-9)
EVEN = next(j for j in range(B.shape[1]) if float((B[:, j] - B[:, j].flip(0)).abs().max()) < 1e-9)
s_grid = torch.sigmoid(zeta)
LAMBDA = float(net.lexical_strength)


def fixed_point(ell0, phi_L, theta):
    c = B.T @ (W * (ell0 - phi_L))
    phi_u = torch.linalg.solve(torch.eye(G.shape[0], dtype=G.dtype) + theta ** 2 * G / 2, mu + theta * c / 2)
    phi_S = ((ell0 - phi_L) + theta * (B @ phi_u)) / 2
    return phi_S, phi_u, c


def limit_field(ell0, phi_L):
    c = B.T @ (W * (ell0 - phi_L))
    return (ell0 - phi_L) / 2 + B @ torch.linalg.solve(G, c) / 2, c


# --- self-check against Code Cell 1 on the network's own entry
check = net.respawn()
phi_S_ref, phi_u_ref = check.closed_form_fixed_point("some", theta_u=3.7)
phi_S_me, phi_u_me, _ = fixed_point(check.base_log_prior, check.lexical_field("some"), 3.7)
print(f"closed form here against Code Cell 1 (\"some\", theta_u = 3.7): "
      f"{float((phi_S_ref - phi_S_me).abs().max()):.1e}, {float((phi_u_ref - phi_u_me).abs().max()):.1e}")


def read_out(phi):
    shifted = phi - phi.max()
    q = torch.exp(shifted)
    return q / torch.sum(W * q)


def mean_s(phi):
    return float(torch.sum(W * read_out(phi) * s_grid))


def mode_s(phi):
    return float(s_grid[int(torch.argmax(phi))])


def chi_cut(s_t):
    t = math.log(s_t / (1 - s_t))
    chi = (zeta < t).to(zeta.dtype)
    chi[(zeta - t).abs() < 1e-12] = 0.5
    return chi


def free_energy(ell0, phi_L, theta):
    phi_S, phi_u, _ = fixed_point(ell0, phi_L, theta)
    r_L = phi_L - ell0 + phi_S
    r_S = phi_S - theta * (B @ phi_u)
    r_u = phi_u - mu
    return -0.5 * float(torch.sum(W * r_L ** 2)) - 0.5 * float(torch.sum(W * r_S ** 2)) - 0.5 * float(torch.sum(r_u ** 2))


def learned_theta(ell0, fields):
    """Maximizer of F~ = mean over the ensemble, by a dense scan then golden-section refinement."""
    f = lambda th: sum(free_energy(ell0, phi_L, th) for phi_L in fields) / len(fields)
    grid = [0.0] + [sgn * 10 ** e for sgn in (1, -1) for e in [x / 40 for x in range(-120, 201)]]
    best = max(grid, key=f)
    lo, hi = best - abs(best) * 0.2 - 1e-3, best + abs(best) * 0.2 + 1e-3
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        a, b = hi - g * (hi - lo), lo + g * (hi - lo)
        if f(a) > f(b):
            hi = b
        else:
            lo = a
    th = (lo + hi) / 2
    asymptote = f(1e9)
    return th, f(th) - asymptote


# --- self-check: the ensemble scan recovers the default theta_u* = -28.4375
ens = [check.lexical_field(y) for y in ("no", "some", "all")]
th_default, margin = learned_theta(check.base_log_prior, ens)
print(f"theta_u* recovered for the default network by this scan: {th_default:.4f} (Code Cell 2 prints -28.4375), margin {margin:+.4f}")
print()

PRIORS = {
    "flat Beta(1,1)": ns["beta_world_prior"](1.0, 1.0),
    "Gaussian prec 1": ns["gaussian_world_prior"](0.0, 1.0),
    "Gaussian prec 2": ns["gaussian_world_prior"](0.0, 2.0),
    "Gaussian prec 4": ns["gaussian_world_prior"](0.0, 4.0),
}
CUTS = (0.50, 0.73, 0.95, 0.98, 0.99)

print("LOADINGS OF chi_t ON B (theta-free): width/tilt ratio (§5.2 quotes 0.219 at 0.73, 0.633 at 0.95, 1.07 at 0.99)")
for s_t in CUTS:
    kappa = B.T @ (W * chi_cut(s_t))
    print(f"  s_t = {s_t:.2f}: kappa tilt {float(kappa[ODD]):+.5f}, width {float(kappa[EVEN]):+.5f}, "
          f"|width/tilt| = {abs(float(kappa[EVEN]) / float(kappa[ODD])):.3f}")
print()

for prior_name, prior in PRIORS.items():
    ell0 = net.respawn(base_prior=prior).base_log_prior
    print(f"PRIOR {prior_name}   (utility contribution to E[s]; §5.2 quotes flat +0.034 at 0.50 -> +0.070 at 0.98,"
          " +0.047 -> +0.099 'at theta_u*'; Gaussian prec 2 -0.005 at 0.50, +0.020 at 0.98)")
    print(f"  {'s_t':>5} | {'c_prior t/w':>17} {'c_entry t/w':>17} | {'th=1':>8} {'th=-28.44':>9} {'limit':>8}"
          f" {'lim tilt':>8} {'lim width':>9} | {'mode lit':>8} {'mode th=1':>9} {'mode lim':>8} |"
          f" {'th* {t}':>9} {'contr':>7} {'th* {t,not t}':>13} {'contr':>7}")
    for s_t in CUTS:
        chi = chi_cut(s_t)
        phi_L = LAMBDA * chi
        tempered = (ell0 - phi_L) / 2
        c_prior = B.T @ (W * ell0)
        c_entry = -(B.T @ (W * phi_L))
        base = mean_s(tempered)
        contr = lambda th: mean_s(fixed_point(ell0, phi_L, th)[0]) - base
        lim, c = limit_field(ell0, phi_L)
        coeff = torch.linalg.solve(G, c) / 2
        lim_tilt = mean_s(tempered + B[:, ODD] * coeff[ODD]) - base
        lim_width = mean_s(tempered + B[:, EVEN] * coeff[EVEN]) - base
        th1, _ = learned_theta(ell0, [phi_L])
        th2, _ = learned_theta(ell0, [phi_L, LAMBDA * (1 - chi)])
        print(f"  {s_t:>5.2f} | {float(c_prior[ODD]):>+8.2f}/{float(c_prior[EVEN]):>+8.2f} "
              f"{float(c_entry[ODD]):>+8.2f}/{float(c_entry[EVEN]):>+8.2f} | {contr(1.0):>+8.4f} {contr(-28.4375):>+9.4f}"
              f" {mean_s(lim) - base:>+8.4f} {lim_tilt:>+8.4f} {lim_width:>+9.4f} | {mode_s(ell0 - phi_L):>8.4f}"
              f" {mode_s(fixed_point(ell0, phi_L, 1.0)[0]):>9.4f} {mode_s(lim):>8.4f} |"
              f" {th1:>9.2f} {contr(th1):>+7.4f} {th2:>13.2f} {contr(th2):>+7.4f}")
    print()

print("DENSE CUTS AT EQ. (24)'S LIMIT: utility contribution to E[s], its tilt and width parts, and the leak")
print("(leak = q-mass on the excluded states zeta < logit s_t; a leak near or above 1/2 means the prior")
print(" overrides the entry, so the entry is not what is being read)")
DENSE = (0.50, 0.55, 0.60, 0.65, 0.70, 0.73, 0.76, 0.80, 0.85, 0.90, 0.93, 0.95, 0.97, 0.98, 0.99)
for prior_name, prior in PRIORS.items():
    ell0 = net.respawn(base_prior=prior).base_log_prior
    print(f"  {prior_name}")
    print(f"    {'s_t':>5}{'contr':>9}{'tilt':>9}{'width':>9}{'leak lit':>10}{'leak temp':>10}{'leak lim':>10}{'mode lim':>9}")
    for s_t in DENSE:
        chi = chi_cut(s_t)
        phi_L = LAMBDA * chi
        tempered = (ell0 - phi_L) / 2
        lim, c = limit_field(ell0, phi_L)
        coeff = torch.linalg.solve(G, c) / 2
        base = mean_s(tempered)
        leak = lambda phi: float(torch.sum(W * read_out(phi) * chi))
        print(f"    {s_t:>5.2f}{mean_s(lim) - base:>+9.4f}{mean_s(tempered + B[:, ODD] * coeff[ODD]) - base:>+9.4f}"
              f"{mean_s(tempered + B[:, EVEN] * coeff[EVEN]) - base:>+9.4f}{leak(ell0 - phi_L):>10.4f}"
              f"{leak(tempered):>10.4f}{leak(lim):>10.4f}{mode_s(lim):>9.4f}")
    print()
