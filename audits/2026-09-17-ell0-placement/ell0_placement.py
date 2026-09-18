"""Where ell_0 enters: g_L (the model, Eq. 9) against g_S (the alternative).

Scratch probe, no project edits. code cell 1 and Code Cell 2's definitions are exec'd
verbatim from main.ipynb; Code Cell 2's RUN block is not.

Variant A (the model, decision A3):   g_L(phi_S) = ell_0 - phi_S,   g_S(phi_u) = theta_u B phi_u
Variant B (the alternative):          g_L(phi_S) = -phi_S,          g_S(phi_u) = ell_0 + theta_u B phi_u

Everything else is held fixed: same F (Eq. 13), same chain, same B, same mu_u, same sigmas,
same read-out (Eq. 12), same exclusion convention (Eq. 5), same Lambda.
"""
import math, sys, nbformat, torch

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(nb.cells[5].source, ns)
src = nb.cells[7].source
exec(src[: src.index("evaluation_network = LexicalPredictiveCodingNetwork()")], ns)

Net = ns["LexicalPredictiveCodingNetwork"]
UTT = ns["UTTERANCES"]


# ---------------------------------------------------------------- variant B, in closed form
def closed_form_B(net, utterance, theta_u=None):
    """Stationary point of F under g_L(phi_S) = -phi_S, g_S(phi_u) = ell_0 + theta_u B phi_u.

        r_L = phi_L + phi_S,  r_S = phi_S - ell_0 - theta_u B phi_u,  r_u = phi_u - mu_u

    dF/dphi_S = 0  ->  phi_S* = [sigma_L (ell_0 + theta_u B phi_u) - sigma_S phi_L] / S
    dF/dphi_u = 0  ->  (I + sigma_u theta^2 G / S) phi_u* = mu_u - sigma_u theta c_B / S,
                       c_B = B^T W (ell_0 + phi_L)
    """
    theta = net.theta_u if theta_u is None else float(theta_u)
    phi_L = net.lexical_field(utterance)
    S = net.sigma_lexical + net.sigma_state
    gram = net.basis.T @ (net.weights[:, None] * net.basis)
    coupling = -net.project(net.base_log_prior + phi_L)           # c_B, signed as in A
    matrix = (torch.eye(net.num_basis, dtype=net.dtype, device=net.device)
              + net.sigma_utility * theta ** 2 * gram / S)
    rhs = net.mu_u + net.sigma_utility * theta * coupling / S
    phi_u = torch.linalg.solve(matrix, rhs)
    phi_S = (net.sigma_lexical * (net.base_log_prior + theta * torch.mv(net.basis, phi_u))
             - net.sigma_state * phi_L) / S
    return phi_S, phi_u


def coupling_A(net, y):
    return net.project(net.base_log_prior - net.lexical_field(y))


def coupling_B(net, y):
    return -net.project(net.base_log_prior + net.lexical_field(y))


def theta_star(net, couplings):
    """Eq. (B2)'s maximizer, taking the couplings as given (G = B^T W B = I)."""
    S = net.sigma_lexical + net.sigma_state
    total = torch.stack(couplings).sum(dim=0)
    a = net.sigma_utility * float(net.dot(net.mu_u, total))
    if a == 0.0:
        return None
    b = (len(couplings) * S * float(net.dot(net.mu_u, net.mu_u))
         - net.sigma_utility * sum(float(net.dot(c, c)) for c in couplings))
    c0 = -S * a / net.sigma_utility
    q = -0.5 * (b + math.copysign(math.sqrt(b * b - 4.0 * a * c0), b))
    roots = (q / a, c0 / q)
    return roots[0] if (roots[0] > 0) == (a > 0) else roots[1]


def upper_mass(net, phi_S):
    up = (net.zeta > net.theta_L).to(net.dtype)
    return float((net.weights * net.read_out(phi_S) * up).sum())


def leak(net, y, phi_S):
    exc = ns["exclusion_indicator"](y, net.zeta, net.theta_L, sharpness=net.exclusion_sharpness)
    return float((net.weights * net.read_out(phi_S) * exc).sum())


def rule(t):
    print("-" * 78 + "\n" + t)


# ================================================================= 1. self-check
rule("1. Self-check: variant A reproduces the stored network")
net = Net()
print(f"  theta_u* (A, default inventory)      {net.learned_theta_u():+.5f}     [expect -28.43749]")
print(f"  theta_u* (A, recomputed from c_y^A)  {theta_star(net, [coupling_A(net, y) for y in UTT]):+.5f}")
phiS, phiu = net.closed_form_fixed_point("some")
phiS2, phiu2 = closed_form_B(net, "some")
print(f"  G = B^T W B - I  max|.|               "
      f"{float((net.basis.T @ (net.weights[:, None] * net.basis) - torch.eye(net.num_basis, dtype=net.dtype)).abs().max()):.1e}")

# ================================================================= 2. the couplings
rule("2. The utility level's drive c_y, under the two placements (Eq. 16's numerator)")
print("   A:  c_y = B^T W (ell_0 - phi_L)      the prior NET of the entry")
print("   B:  c_y = -B^T W (ell_0 + phi_L)     the prior and the entry SUMMED\n")
print(f"   {'utterance':<10} {'c_y^A':>22} {'c_y^B':>22}")
for y in UTT:
    cA, cB = coupling_A(net, y), coupling_B(net, y)
    print(f"   {y:<10} {str([round(float(v), 4) for v in cA]):>22} {str([round(float(v), 4) for v in cB]):>22}")
ell0_proj = net.project(net.base_log_prior)
print()
for y in UTT:
    cA, cB = coupling_A(net, y), coupling_B(net, y)
    d = cA - cB - 2.0 * ell0_proj
    s = cA + cB + 2.0 * net.project(net.lexical_field(y))
    print(f"   {y:<10} max|c^A - c^B - 2 B^T W ell_0| = {float(d.abs().max()):.1e}"
          f"     max|c^A + c^B + 2 B^T W phi_L| = {float(s.abs().max()):.1e}")
print("\n   So the two differ by exactly 2 B^T W ell_0, whatever the entry, and agree up to")
print("   the sign the prior carries against the entry.  2 B^T W ell_0 = "
      f"{[round(float(v), 4) for v in 2 * ell0_proj]}")

# ================================================================= 3. same phi_u => same phi_S
rule("3. At sigma_L = sigma_S the two agree GIVEN phi_u; they differ in phi_u* itself")
print("   phi_S*(phi_u) difference is (sigma_L - sigma_S) ell_0 / S, exactly.\n")
for y in UTT:
    pA = net.closed_form_fixed_point(y, theta_u=1.0)
    phiL = net.lexical_field(y)
    S = net.sigma_lexical + net.sigma_state
    same_u = (net.sigma_lexical * (net.base_log_prior + 1.0 * torch.mv(net.basis, pA[1]))
              - net.sigma_state * phiL) / S
    pB = closed_form_B(net, y, theta_u=1.0)
    print(f"   {y:<6} at theta_u = 1:  max|phi_S^A - phi_S^B| at the SAME phi_u "
          f"{float((pA[0] - same_u).abs().max()):.1e}"
          f"   |phi_u*^A - phi_u*^B| {float((pA[1] - pB[1]).abs().max()):.4f}"
          f"   max|phi_S*^A - phi_S*^B| {float((pA[0] - pB[0]).abs().max()):.4f}")
print("\n   With sigma_L = 2, sigma_S = 1 the first column is no longer zero:")
net2 = net.respawn(sigma_lexical=2.0)
for y in UTT:
    pA = net2.closed_form_fixed_point(y, theta_u=1.0)
    phiL = net2.lexical_field(y)
    S = net2.sigma_lexical + net2.sigma_state
    same_u = (net2.sigma_lexical * (net2.base_log_prior + 1.0 * torch.mv(net2.basis, pA[1]))
              - net2.sigma_state * phiL) / S
    pred = float(((net2.sigma_lexical - net2.sigma_state) * net2.base_log_prior / S).abs().max())
    print(f"   {y:<6} max|phi_S^A - phi_S^B| at the same phi_u {float((pA[0] - same_u).abs().max()):.4f}"
          f"   predicted (sigma_L - sigma_S)|ell_0|_max / S {pred:.4f}")

# ================================================================= 4. the literal listener
rule("4. Is the literal listener ell_0 - phi_L a fixed point of the network?")
print("   A:  phi_S* = [sigma_L theta B phi_u + sigma_S (ell_0 - phi_L)] / S  ->  ell_0 - phi_L")
print("       as sigma_S -> infinity.  The baseline is a limit of the model itself.")
print("   B:  phi_S* = [sigma_L (ell_0 + theta B phi_u) - sigma_S phi_L] / S.")
print("       sigma_S -> infinity gives -phi_L (the entry, prior discarded);")
print("       sigma_L -> infinity gives ell_0 + theta B phi_u (the prior, entry discarded).\n")
for lab, sl, ss in (("sigma_S = 1e6", 1.0, 1e6), ("sigma_L = 1e6", 1e6, 1.0)):
    n3 = net.respawn(sigma_lexical=sl, sigma_state=ss)
    y = "some"
    lit = n3.base_log_prior - n3.lexical_field(y)
    pA = n3.closed_form_fixed_point(y, theta_u=1.0)[0]
    pB = closed_form_B(n3, y, theta_u=1.0)[0]
    print(f"   {lab:<14} max|phi_S^A - (ell_0 - phi_L)| {float((pA - lit).abs().max()):.2e}"
          f"     max|phi_S^B - (ell_0 - phi_L)| {float((pB - lit).abs().max()):.2e}")

# ================================================================= 5. Part D, both variants
rule("5. Part D's five priors, at Lambda = 8 and at Lambda = 512, under both placements")
print("   q_lit is ell_0 - phi_L throughout (variant A's baseline), so the two variants are")
print("   scored against the same literal listener.  shift = q_H - q_lit for *some*.\n")
priors = dict(ns["part_d_priors"]())
priors["delta-like"] = ns["beta_world_prior"](64.0, 1.0)   # Code Cell 2b's DELTA_ALL_ALPHA
for lam in (8.0, 512.0):
    print(f"   Lambda = {lam:.0f}")
    print(f"   {'prior':<12} {'theta*^A':>11} {'theta*^B':>11} {'q_lit':>8} "
          f"{'q_H^A':>8} {'q_H^B':>8} {'shift^A':>9} {'shift^B':>9}  A 1st/2nd  B 1st/2nd")
    for name, spec in priors.items():
        p = net.respawn(base_prior=spec, lexical_strength=lam)
        tA = theta_star(p, [coupling_A(p, y) for y in UTT])
        tB = theta_star(p, [coupling_B(p, y) for y in UTT])
        y = "some"
        qlit = upper_mass(p, p.literal_fixed_point(y))
        qA = upper_mass(p, p.closed_form_fixed_point(y, theta_u=tA)[0])
        qB = upper_mass(p, closed_form_B(p, y, theta_u=tB)[0])
        f = lambda q: ("met" if q - qlit < 0 else "no ") + "/" + ("met" if q < 0.5 else "no ")
        print(f"   {name:<12} {tA:>11.2f} {tB:>11.2f} {qlit:>8.4f} {qA:>8.4f} {qB:>8.4f} "
              f"{qA - qlit:>+9.4f} {qB - qlit:>+9.4f}  {f(qA)}    {f(qB)}")
    print()

# ================================================================= 6. does the entry hold
rule("6. The largest leak in a row (the prior overriding the entry), at theta*")
print(f"   {'prior':<12} {'Lambda':>7} {'leak A':>10} {'leak B':>10}")
for lam in (8.0, 512.0):
    for name, spec in priors.items():
        p = net.respawn(base_prior=spec, lexical_strength=lam)
        tA = theta_star(p, [coupling_A(p, y) for y in UTT])
        tB = theta_star(p, [coupling_B(p, y) for y in UTT])
        lA = max(leak(p, y, p.closed_form_fixed_point(y, theta_u=tA)[0]) for y in UTT)
        lB = max(leak(p, y, closed_form_B(p, y, theta_u=tB)[0]) for y in UTT)
        print(f"   {name:<12} {lam:>7.0f} {lA:>10.2e} {lB:>10.2e}")

# ================================================================= 7. the Lambda limit
rule("7. How Lambda reaches the utility level under each placement")
print("   |c_y| as Lambda grows, under the Gaussian prior (utterance *some*):\n")
print(f"   {'Lambda':>8} {'|c^A|':>10} {'|c^B|':>10} {'|c^A| - |c^B|':>14}")
for lam in (1e-9, 1.0, 8.0, 64.0, 512.0, 4096.0):
    p = net.respawn(lexical_strength=lam)
    cA, cB = coupling_A(p, "some"), coupling_B(p, "some")
    nA, nB = float(cA.norm()), float(cB.norm())
    print(f"   {lam:>8.3g} {nA:>10.4f} {nB:>10.4f} {nA - nB:>+14.4f}")
print("\n   At Lambda -> 0 (no lexical field) the two couplings are +B^T W ell_0 and -B^T W ell_0:")
p = net.respawn(lexical_strength=1e-9)
print(f"   c^A = {[round(float(v), 4) for v in coupling_A(p, 'some')]}"
      f"   c^B = {[round(float(v), 4) for v in coupling_B(p, 'some')]}")
print("   As Lambda -> infinity both approach -Lambda B^T W chi_y, so the placements differ")
print("   in the prior's sign against the entry, not in the entry's own leading term.")

# ================================================================= 8. is theta*^B really the maximizer
rule("8. Self-check: theta*^B maximizes variant B's reduced free energy")
print("   F is evaluated directly from variant B's residuals at its own stationary")
print("   (phi_S, phi_u), averaged over the three utterances, and scanned in theta.\n")


def free_energy_B(net, theta):
    tot = 0.0
    for y in UTT:
        phi_S, phi_u = closed_form_B(net, y, theta_u=theta)
        phi_L = net.lexical_field(y)
        r_L = phi_L + phi_S
        r_S = phi_S - net.base_log_prior - theta * torch.mv(net.basis, phi_u)
        r_u = phi_u - net.mu_u
        tot += (-net.squared_norm(r_L) / (2 * net.sigma_lexical)
                - net.squared_norm(r_S) / (2 * net.sigma_state)
                - float(net.dot(r_u, r_u)) / (2 * net.sigma_utility))
    return tot / len(UTT)


for name, spec in list(priors.items()):
    for lam in (8.0, 512.0):
        p = net.respawn(base_prior=spec, lexical_strength=lam)
        tB = theta_star(p, [coupling_B(p, y) for y in UTT])
        grid = [tB * (1.0 + d) for d in (-0.2, -0.05, -0.01, 0.0, 0.01, 0.05, 0.2)]
        vals = [free_energy_B(p, t) for t in grid]
        best = grid[max(range(len(grid)), key=lambda i: vals[i])]
        scan = sorted((free_energy_B(p, t), t) for t in
                      [tB * (1 + k / 200.0) for k in range(-100, 101)])[-1][1]
        print(f"   {name:<12} Lambda {lam:>5.0f}   theta*^B {tB:>12.4f}"
              f"   argmax on a +-50% scan {scan:>12.4f}"
              f"   rel. gap {abs(scan - tB) / abs(tB):.2e}")
