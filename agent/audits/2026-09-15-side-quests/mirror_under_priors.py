"""Side quest 1, completed: the reflection acts on ell_0 too.

Beta(alpha, beta) in s reflects to Beta(beta, alpha), so the full equivariance
pairs (inventory, ell_0, mu_u) with (mirrored inventory, reflected ell_0, P mu_u).
The default N(0,1) in zeta is self-reflective, which is why mu_u is the only
thing that breaks the mirror there.  Scratch probe (C6).
"""
import math, pathlib, torch

SRC = pathlib.Path("/private/tmp/claude-501/-Users-flog-Desktop-predictive-coding/"
                   "cdd84152-de05-44ad-92e9-458bc1738ed8/scratchpad/cells/cell05_code.txt")
ns = {}
exec(compile(SRC.read_text(), "code_cell_1", "exec"), ns)
Net, excl = ns["LexicalPredictiveCodingNetwork"], ns["exclusion_indicator"]
beta, gauss = ns["beta_world_prior"], ns["gaussian_world_prior"]
refl = lambda f: torch.flip(f, [0])
mx = lambda t: float(t.abs().max())
PAIR = {"no": "all", "some": "not all", "all": "no"}
A, M = ["no", "some", "all"], ["no", "not all", "all"]

def chis(net):
    c = {y: excl(y, net.zeta, net.theta_L) for y in ns["UTTERANCES"]}
    c["not all"] = (net.zeta >= net.theta_L).to(net.dtype)
    return c

def theta_star(net, inv, mu, chi):
    L, S = net.lexical_strength, net.sigma_lexical + net.sigma_state
    cs = [net.project(net.base_log_prior - L * chi[y]) for y in inv]
    tot = torch.stack(cs).sum(dim=0)
    a = net.sigma_utility * float(net.dot(mu, tot))
    b = (len(inv) * S * float(net.dot(mu, mu))
         - net.sigma_utility * sum(float(net.dot(c, c)) for c in cs))
    c0 = -S * a / net.sigma_utility
    r = math.sqrt(b * b - 4.0 * a * c0)
    q = -0.5 * (b + math.copysign(r, b))
    roots = (q / a, c0 / q)
    return roots[0] if (roots[0] > 0) == (a > 0) else roots[1]

def fp(net, chi_y, theta, mu):
    L, S, D = net.lexical_strength, net.sigma_lexical + net.sigma_state, net.dtype
    G = net.basis.T @ (net.weights[:, None] * net.basis)
    c = net.project(net.base_log_prior - L * chi_y)
    Mx = torch.eye(net.num_basis, dtype=D) + net.sigma_utility * theta**2 * G / S
    phi_u = torch.linalg.solve(Mx, mu + net.sigma_utility * theta * c / S)
    return (net.sigma_lexical * theta * torch.mv(net.basis, phi_u)
            + net.sigma_state * (net.base_log_prior - L * chi_y)) / S

D = torch.float64
muA = torch.tensor([1.0, 1.0], dtype=D)
muM = torch.tensor([-1.0, 1.0], dtype=D)

print("== does the reflection carry the prior? ==")
for pa, pb in [(3.0, 1.0), (1.0, 3.0), (64.0, 1.0), (1.0, 1.0)]:
    nA, nM = Net(base_prior=beta(pa, pb)), Net(base_prior=beta(pb, pa))
    print(f"  Beta({pa:g},{pb:g}) -> Beta({pb:g},{pa:g}):  "
          f"|refl(ell_0^A) - ell_0^M| = {mx(refl(nA.base_log_prior) - nM.base_log_prior):.2e}")

print("\n== the mirror, prior reflected as well, at P mu_u ==")
for label, pA_, pM_ in [("Gaussian N(0,1) (self-reflective)", gauss(0.0, 1.0), gauss(0.0, 1.0)),
                        ("Beta(3,1) <-> Beta(1,3)", beta(3.0, 1.0), beta(1.0, 3.0)),
                        ("Beta(64,1) <-> Beta(1,64)", beta(64.0, 1.0), beta(1.0, 64.0))]:
    nA, nM = Net(base_prior=pA_), Net(base_prior=pM_)
    cA, cM = chis(nA), chis(nM)
    tA = theta_star(nA, A, muA, cA)
    tM = theta_star(nM, M, muM, cM)
    worst = max(mx(refl(fp(nA, cA[y], tA, muA)) - fp(nM, cM[PAIR[y]], tM, muM)) for y in A)
    print(f"  {label:34s} theta_u* {tA:+10.5f} / {tM:+10.5f}  "
          f"worst {worst:.2e}  {'EXACT' if worst < 1e-9 else 'BROKEN'}")

print("\n== the same, at the stipulated mu_u = (1,1) on both sides ==")
for label, pA_, pM_ in [("Gaussian N(0,1)", gauss(0.0, 1.0), gauss(0.0, 1.0)),
                        ("Beta(3,1) <-> Beta(1,3)", beta(3.0, 1.0), beta(1.0, 3.0))]:
    nA, nM = Net(base_prior=pA_), Net(base_prior=pM_)
    cA, cM = chis(nA), chis(nM)
    tA, tM = theta_star(nA, A, muA, cA), theta_star(nM, M, muA, cM)
    worst = max(mx(refl(fp(nA, cA[y], tA, muA)) - fp(nM, cM[PAIR[y]], tM, muA)) for y in A)
    print(f"  {label:34s} theta_u* {tA:+10.5f} / {tM:+10.5f}  "
          f"worst {worst:.2e}  {'EXACT' if worst < 1e-9 else 'BROKEN'}")
