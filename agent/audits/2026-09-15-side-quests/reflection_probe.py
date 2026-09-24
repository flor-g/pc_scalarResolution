"""Side quest 1: is the O corner {1} as representational as {0}?

Tests whether the architecture is equivariant under the reflection zeta -> -zeta,
and whether the mirrored inventory {no, not all, all} is the reflection image of
{no, some, all}.  Scratch probe: no number here is in the notebook (C6).
"""
import math, pathlib, torch

SRC = pathlib.Path("/private/tmp/claude-501/-Users-flog-Desktop-predictive-coding/"
                   "cdd84152-de05-44ad-92e9-458bc1738ed8/scratchpad/cells/cell05_code.txt")
ns = {}
exec(compile(SRC.read_text(), "code_cell_1", "exec"), ns)
Net = ns["LexicalPredictiveCodingNetwork"]
excl = ns["exclusion_indicator"]

net = Net()                      # defaults: n = 10, Lambda = 8, N(0,1), mu_u = 1, m = 2
z, w, L, tL = net.zeta, net.weights, net.lexical_strength, net.theta_L
S = net.sigma_lexical + net.sigma_state
refl = lambda f: torch.flip(f, [0])          # zeta -> -zeta on a grid symmetric about 0
mx = lambda t: float(t.abs().max())

print(f"n = {net.num_atoms:.0f}, theta_L = {tL:.6f}, Lambda = {L}, mu_u = {net.mu_u.tolist()}")

print("\n== 1. is the substrate reflection-symmetric? ==")
print(f"  |zeta + refl(zeta)|      {mx(z + refl(z)):.2e}")
print(f"  |w - refl(w)|            {mx(w - refl(w)):.2e}")
print(f"  |ell_0 - refl(ell_0)|    {mx(net.base_log_prior - refl(net.base_log_prior)):.2e}")
node_gap = min(abs(float(zz) - tL) for zz in z)
print(f"  nearest grid node to +theta_L is {node_gap:.4f} away (0 would make the")
print(f"    strict/non-strict boundary in exclusion_indicator visible)")

print("\n== 2. basis parity ==")
b1, b2 = net.basis[:, 0], net.basis[:, 1]
print(f"  |refl(b1) + b1|  {mx(refl(b1) + b1):.2e}   (b1 odd: tilt)")
print(f"  |refl(b2) - b2|  {mx(refl(b2) - b2):.2e}   (b2 even: width)")
print(f"  <b1, ell_0> = {float(net.inner(b1, net.base_log_prior)):+.3e}  "
      f"(0 because b1 is odd and ell_0 even)")
print(f"  <b2, ell_0> = {float(net.inner(b2, net.base_log_prior)):+.6f}")

print("\n== 3. the four indicators, and the reflection that pairs them ==")
chi = {y: excl(y, z, tL) for y in ns["UTTERANCES"]}
chi["not all"] = (z >= tL).to(z.dtype)
print(f"  |refl(chi_no)   - chi_all|      {mx(refl(chi['no']) - chi['all']):.2e}")
print(f"  |refl(chi_some) - chi_not all|  {mx(refl(chi['some']) - chi['not all']):.2e}")
print("  kappa per unit Lambda (tilt, width):")
for y in ["no", "some", "all", "not all"]:
    k = net.project(chi[y])
    print(f"    {y:9s} ({float(k[0]):+.5f}, {float(k[1]):+.5f})")

# --- inventory-level machinery, written out so a custom inventory can be run ---
def coup(chis):
    return [net.project(net.base_log_prior - L * c) for c in chis]

def theta_star(chis):
    cs = coup(chis)
    tot = torch.stack(cs).sum(dim=0)
    a = net.sigma_utility * float(net.dot(net.mu_u, tot))
    if a == 0.0:
        raise ValueError("<mu_u, sum c> = 0")
    b = (len(chis) * S * float(net.dot(net.mu_u, net.mu_u))
         - net.sigma_utility * sum(float(net.dot(c, c)) for c in cs))
    c0 = -S * a / net.sigma_utility
    r = math.sqrt(b * b - 4.0 * a * c0)
    q = -0.5 * (b + math.copysign(r, b))
    roots = (q / a, c0 / q)
    return roots[0] if (roots[0] > 0) == (a > 0) else roots[1]

def fixed_point(chi_y, theta):
    c = net.project(net.base_log_prior - L * chi_y)
    M = torch.eye(net.num_basis, dtype=net.dtype) + net.sigma_utility * theta**2 / S
    phi_u = torch.linalg.solve(M, net.mu_u + net.sigma_utility * theta * c / S)
    phi_S = (net.sigma_lexical * theta * torch.mv(net.basis, phi_u)
             + net.sigma_state * (net.base_log_prior - L * chi_y)) / S
    return phi_S, phi_u

A = ["no", "some", "all"]          # the inventory the notebook runs
M = ["no", "not all", "all"]       # the mirrored inventory
# reflection pairs them as no <-> all, some <-> not all
PAIR = {"no": "all", "some": "not all", "all": "no", "not all": "some"}

print("\n== 4. sum_y c_y, and the sign that sets theta_u* ==")
for name, inv in (("{no, some, all}", A), ("{no, not all, all}", M)):
    tot = torch.stack(coup([chi[y] for y in inv])).sum(dim=0)
    a = float(net.dot(net.mu_u, tot))
    print(f"  {name:20s} sum c = ({float(tot[0]):+9.4f}, {float(tot[1]):+9.4f})   "
          f"<mu_u, sum c> = {a:+9.4f}   theta_u* = {theta_star([chi[y] for y in inv]):+9.4f}")

print("\n== 5. is the mirrored inventory the reflection image? ==")
for mu_label, mu in (("mu_u = (1, 1), as stipulated (A5)", torch.tensor([1.0, 1.0], dtype=net.dtype)),
                     ("mu_u = (-1, 1), the reflected mu_u", torch.tensor([-1.0, 1.0], dtype=net.dtype))):
    net.mu_u = mu
    tA, tM = theta_star([chi[y] for y in A]), theta_star([chi[y] for y in M])
    print(f"\n  {mu_label}")
    print(f"    theta_u*  {tA:+.5f} on {{no, some, all}}   {tM:+.5f} on {{no, not all, all}}")
    worst = 0.0
    for y in A:
        pA, _ = fixed_point(chi[y], tA)
        pM, _ = fixed_point(chi[PAIR[y]], tM)
        d = mx(refl(pA) - pM)
        worst = max(worst, d)
        print(f"    |refl(phi_S*({y})) - phi_S*({PAIR[y]}))|  {d:.3e}")
    print(f"    worst {worst:.3e}  ->  {'EXACT MIRROR' if worst < 1e-12 else 'NOT a mirror'}")
