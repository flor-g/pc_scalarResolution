"""Audit 2026-09-21: can the realizable maximizer be defined by a TOLERANCE on Eq. (20)'s
flow, and does that break any standing prediction?

The user's proposal (2026-09-21): halting is achieved by tolerance. The fast loop already
halts that way (`infer`'s derivative_tolerance, decision I3, 1e-9). The slow flow of
Eq. (20) does not: main.ipynb obtains theta_u* in closed form (Eq. B2), and every
"realizable" theta_u it reports is located either by bisecting fractions of theta_u* or by
stopping the flow on Part C's criterion, an evaluator's statistic computed outside the
network. A tolerance rule would be self-contained: stop when the update |d theta_u| falls
below tol.

METHOD. Eq. (20)'s update is theta += (tau_state / tau_theta) * g(theta), with g the
gradient at the equilibrated fast subsystem, which Code Cell 2 computes as
`theta_u_gradient_at_equilibrium`. That function re-solves Eqs. (15)-(16) per call, which
is too slow for a flow of 10^5 updates over 121 cells, so the same quantity is rebuilt here
from the configuration's fixed pieces (c_y, G, mu_u, sigma_u, S) and checked against it:
by Eq. (17) the per-utterance gradient is <phi_u, (phi_u - mu_u)> / (sigma_u * theta), and
phi_u(theta) solves (I + sigma_u theta^2 G / S) phi_u = mu_u + sigma_u theta c_y / S.

Nothing here is written into the notebooks. Every number is class (e) under agent.md
Sec. 3.3 until a cell prints it (C6).

Run from the project folder:
    .venv/bin/python audits/2026-09-21-tolerance-halting/tolerance_halting.py
"""
import numpy as np
import nbformat
import torch

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)          # code cell 1
Net = ns["LexicalPredictiveCodingNetwork"]
beta_world_prior = ns["beta_world_prior"]
UTTERANCES = ns["UTTERANCES"]

# Code Cell 2's DEFINITIONS only: keep module-level definitions, imports and constants,
# and drop the bare calls that would re-run its report (and redraw its figures).
import ast

def definitions_only(source, name):
    """Definitions, imports and constant assignments; every call at module level is
    dropped, whether it stands alone or is assigned, so no report is re-run here."""
    tree = ast.parse(source)
    kept = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
                             ast.Import, ast.ImportFrom)):
            kept.append(node)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)) and not isinstance(
            getattr(node, "value", None), ast.Call
        ):
            kept.append(node)
    tree.body = kept
    exec(compile(tree, name, "exec"), ns)


definitions_only(nb.cells[7].source, "code_cell_2_defs")
criterion_for_some = ns["criterion_for_some"]
gradient_at = ns["theta_u_gradient_at_equilibrium"]
part_d_priors = ns["part_d_priors"]

TAU_STATE, TAU_THETA = 1.00, 20.0
STEP = TAU_STATE / TAU_THETA
TOLERANCES = (1e-9, 1e-6, 1e-4, 1e-2, 1e-1, 1.0)
CAP = 2_000_000


def pieces(net):
    """The configuration's theta-independent pieces, as numpy."""
    B = net.basis.numpy().astype(float)
    W = net.weights.numpy().astype(float)
    G = B.T @ (W[:, None] * B)
    mu = net.mu_u.numpy().astype(float)
    S = float(net.sigma_lexical + net.sigma_state)
    c = {y: B.T @ (W * (net.base_log_prior - net.lexical_field(y)).numpy().astype(float))
         for y in UTTERANCES}
    return G, mu, S, float(net.sigma_utility), c


def gradient(theta, G, mu, S, sigma_u, c):
    """Eq. (20)'s gradient at the fast fixed point, averaged over the inventory."""
    if theta == 0.0:
        # the limit: phi_u = mu, and <phi_u, BtW r_S> = <mu, c_y> / S
        return float(np.mean([mu @ c[y] for y in UTTERANCES]) / S)
    total = 0.0
    A = np.eye(len(mu)) + (sigma_u * theta * theta / S) * G
    for y in UTTERANCES:
        phi_u = np.linalg.solve(A, mu + (sigma_u * theta / S) * c[y])
        total += phi_u @ (phi_u - mu) / (sigma_u * theta)
    return total / len(UTTERANCES)


def flow_halts(net, tolerances=TOLERANCES, cap=CAP):
    """First update whose |delta theta| falls below each tolerance, iterating Eq. (20)."""
    G, mu, S, sigma_u, c = pieces(net)
    remaining = sorted(tolerances, reverse=True)
    out, theta = {}, float(net.theta_u_initial)
    for update in range(1, cap + 1):
        delta = STEP * gradient(theta, G, mu, S, sigma_u, c)
        theta += delta
        while remaining and abs(delta) < remaining[0]:
            out[remaining.pop(0)] = (update, theta)
        if not remaining:
            break
    for tol in remaining:
        out[tol] = (None, theta)
    return out


def verdict(net, theta):
    row = criterion_for_some(net, theta)
    return row["shift"], row["upper"], row["both"], float(net.stiffest_state_rate(theta))


def block(title):
    print("\n" + title)
    print("-" * len(title))


print("TOLERANCE AS THE HALTING MECHANISM OF Eq. (20) -- audit, 2026-09-21")

# ---------------------------------------------------------------- 0. self-checks
block("(0) SELF-CHECKS")
net = Net()
G, mu, S, sigma_u, c = pieces(net)
for theta in (0.0, 1.0, -5.0, 12.5):
    mine, theirs = gradient(theta, G, mu, S, sigma_u, c), gradient_at(net, theta)
    print(f"    gradient at theta_u = {theta:>6.1f}: rebuilt {mine:+.8f}   "
          f"Code Cell 2 {theirs:+.8f}   difference {abs(mine - theirs):.1e}")

for theta in (0.0, None):                      # None: the network's own theta_u, = theta_u*
    integrated = 0.0
    for utterance in UTTERANCES:
        result = net.infer(utterance, theta_u=theta, record_history=False)
        integrated += float(net.theta_u_gradient(result))
    integrated /= len(UTTERANCES)
    where = "theta_u = 0" if theta == 0.0 else f"theta_u* = {net.theta_u:.4f}"
    print(f"    INTEGRATED rather than closed form, at {where}: {integrated:+.8f}"
          + ("   (zero at the maximizer, by Eq. B2)" if theta is None else ""))

for name, alpha, lam, expect in (("flat", 1.0, 512.0, 7.816128),
                                 ("skewed high", 3.0, 512.0, 7.992595),
                                 ("delta (all)", 64.0, 512.0, 13.374852)):
    probe = net.respawn(base_prior=beta_world_prior(alpha, 1.0), lexical_strength=lam)
    p = pieces(probe)
    one = float(probe.theta_u_initial) + STEP * gradient(float(probe.theta_u_initial), *p)
    print(f"    one update, Beta({alpha:.0f},1) at Lambda = {lam:.0f}: theta_u -> {one:.6f}"
          f"   (Code Cell 2b prints {expect})")

# ---------------------------------------------------- 1. Part D's rows, both Lambdas
for lam, rows in ((8.0, part_d_priors()),
                  (512.0, {**part_d_priors(), "delta (all)": beta_world_prior(64.0, 1.0)})):
    block(f"(1) HALTING BY TOLERANCE, PART D'S ROWS AT LAMBDA = {lam:.0f}")
    print("    theta_u* is the asymptote of this same flow. 4*lambda_max(H) is the separation")
    print("    commitment 7 demands at that theta_u (Eq. 28); it is the cost that grows.")
    for name, specification in rows.items():
        prior, overrides = (specification if isinstance(specification, tuple)
                            else (specification, {}))
        probe = net.respawn(base_prior=prior, lexical_strength=lam, **overrides)
        star = probe.learned_theta_u()
        s_shift, s_upper, s_both, s_lam = verdict(probe, star)
        print(f"\n      {name:<12} theta_u* = {star:>10.2f}   shift {s_shift:+.4f}  "
              f"upper {s_upper:.4f}  both {str(s_both):<5}  4*lambda = {4 * s_lam:.2e}")
        halts = flow_halts(probe)
        print(f"      {'tolerance':>10}  {'updates':>10}  {'theta_halt':>11}  {'/theta*':>8}"
              f"  {'shift':>9}  {'upper':>7}  {'both':>6}  {'4*lambda':>9}")
        for tol in TOLERANCES:
            updates, theta = halts[tol]
            shift, upper, both, lam_h = verdict(probe, theta)
            u = "> cap" if updates is None else f"{updates:d}"
            print(f"      {tol:>10.0e}  {u:>10}  {theta:>11.4f}  {theta / star:>8.4f}"
                  f"  {shift:>+9.4f}  {upper:>7.4f}  {str(both):>6}  {4 * lam_h:>9.2e}")

# ------------------------------------------------------------------- 2. the plane
block("(2) THE PLANE: BOTH q CRITERIA AT THE HALTED theta_u, AGAINST theta_u*")
alphas = [2.0 ** k for k in range(0, 11)]
lambdas = [2.0 ** k for k in range(1, 12)]
counts = {tol: 0 for tol in TOLERANCES}
reached = {tol: 0 for tol in TOLERANCES}
star_count, agree = 0, {tol: 0 for tol in TOLERANCES}
for alpha in alphas:
    for lam in lambdas:
        probe = net.respawn(base_prior=beta_world_prior(alpha, 1.0), lexical_strength=lam)
        star = probe.learned_theta_u()
        star_both = criterion_for_some(probe, star)["both"]
        star_count += bool(star_both)
        halts = flow_halts(probe, cap=200_000)
        for tol in TOLERANCES:
            updates, theta = halts[tol]
            reached[tol] += updates is not None
            both = criterion_for_some(probe, theta)["both"]
            counts[tol] += bool(both)
            agree[tol] += bool(both) == bool(star_both)
print(f"    at each cell's own theta_u*: both criteria in {star_count} of 121 cells")
for tol in TOLERANCES:
    print(f"    tolerance {tol:>8.0e}: both in {counts[tol]:>3} of 121"
          f"   agreeing with theta_u* in {agree[tol]:>3} of 121"
          f"   (tolerance reached within 200,000 updates in {reached[tol]:>3})")

# ------------------------------------------- 3. the fast loop's own tolerance (I3)
block("(3) THE FAST LOOP'S TOLERANCE: DOES A COARSER ONE MOVE THE VERDICT?")
print("    default network (Gaussian prior, Lambda = 8), at theta_u = 1 (a control) and at")
print("    the theta_u one update of Eq. (20) reaches from 0.")
one_update = float(net.theta_u_initial) + STEP * gradient(float(net.theta_u_initial), G, mu, S, sigma_u, c)
for theta in (1.0, one_update):
    print(f"\n      theta_u = {theta:.4f}")
    exact_phi, _ = net.closed_form_fixed_point("some", theta_u=theta)
    for tol in (1e-9, 1e-6, 1e-4, 1e-3, 1e-2):
        result = net.infer("some", theta_u=theta, record_history=False,
                           derivative_tolerance=tol)
        gap = float((result["phi_S"] - exact_phi).abs().max())
        row = criterion_for_some(net, theta, belief=net.read_out(result["phi_S"]))
        print(f"      tol {tol:>7.0e}: steps {result['steps']:>7d}  "
              f"max|phi_S - phi_S*| {gap:.2e}  shift {row['shift']:+.4f}  "
              f"upper {row['upper']:.4f}  both {row['both']}")

print("\nDONE")
