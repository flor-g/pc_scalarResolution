"""Side quest 1: is the mirrored inventory {no, not all, all} the reflection image
of {no, some, all}?  Scratch probe, no number here is in the notebook (C6)."""
import math, pathlib, torch

SRC = pathlib.Path("/private/tmp/claude-501/-Users-flog-Desktop-predictive-coding/"
                   "cdd84152-de05-44ad-92e9-458bc1738ed8/scratchpad/cells/cell05_code.txt")
ns = {}
exec(compile(SRC.read_text(), "code_cell_1", "exec"), ns)
net = ns["LexicalPredictiveCodingNetwork"]()
excl = ns["exclusion_indicator"]
z, w, L, tL = net.zeta, net.weights, net.lexical_strength, net.theta_L
S, D = net.sigma_lexical + net.sigma_state, net.dtype
GRAM = net.basis.T @ (net.weights[:, None] * net.basis)
refl = lambda f: torch.flip(f, [0])
mx = lambda t: float(t.abs().max())

chi = {y: excl(y, z, tL) for y in ns["UTTERANCES"]}
chi["not all"] = (z >= tL).to(D)
A, M = ["no", "some", "all"], ["no", "not all", "all"]
PAIR = {"no": "all", "some": "not all", "all": "no"}
P = torch.tensor([-1.0, 1.0], dtype=D)                 # diag(-1,+1) on the (tilt, width) coords

def theta_star(inv, mu):
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

def fp(y, theta, mu):
    c = net.project(net.base_log_prior - L * chi[y])
    Mx = torch.eye(net.num_basis, dtype=D) + net.sigma_utility * theta**2 * GRAM / S
    phi_u = torch.linalg.solve(Mx, mu + net.sigma_utility * theta * c / S)
    phi_S = (net.sigma_lexical * theta * torch.mv(net.basis, phi_u)
             + net.sigma_state * (net.base_log_prior - L * chi[y])) / S
    return phi_S, phi_u

print("== 0. validate the helper against the notebook's own closed form ==")
worst = 0.0
for y in A:
    mine, _ = fp(y, net.theta_u, net.mu_u)
    theirs, _ = net.closed_form_fixed_point(y, theta_u=net.theta_u)
    worst = max(worst, mx(mine - theirs))
print(f"  worst |fp - closed_form_fixed_point| over the three utterances: {worst:.2e}")
assert worst < 1e-10, "helper does not reproduce the notebook's closed form"
print(f"  theta_u* reproduced: {theta_star(A, net.mu_u):+.6f} vs net {net.theta_u:+.6f}")

def q_of(p):
    e = torch.exp(p - p.max()); return e / torch.sum(w * e)
up, lo = (z > tL).to(D), (z <= -tL).to(D)            # all-region, no-region (Eq. 27)
mass = lambda q, r: float(torch.sum(w * q * r))
Es = lambda q: float(torch.sum(w * q * torch.sigmoid(z)))
q_lit = lambda y: q_of(net.base_log_prior - L * chi[y])

muA = torch.tensor([1.0, 1.0], dtype=D)
muM = P * muA

print("\n== A. the reflection applied to the model as a whole: (A, mu_u) vs (M, P mu_u) ==")
tA, tM = theta_star(A, muA), theta_star(M, muM)
print(f"  theta_u*  {tA:+.6f} on (A, mu_u)   {tM:+.6f} on (M, P mu_u)   diff {abs(tA-tM):.2e}")
worst = 0.0
for y in A:
    pA, uA = fp(y, tA, muA)
    pM, uM = fp(PAIR[y], tM, muM)
    dS, dU = mx(refl(pA) - pM), mx(P * uA - uM)
    worst = max(worst, dS, dU)
    print(f"  {y:5s} <-> {PAIR[y]:8s}  |refl(phi_S*)-phi_S*| {dS:.2e}   |P phi_u*-phi_u*| {dU:.2e}")
print(f"  worst {worst:.2e}  ->  {'EXACT MIRROR' if worst < 1e-10 else 'NOT a mirror'}")

print("\n== B. the mirrored inventory at the STIPULATED mu_u = (1,1) (A5) ==")
tMs = theta_star(M, muA)
print(f"  theta_u*  {tA:+.6f} on {{no, some, all}}   {tMs:+.6f} on {{no, not all, all}}")
print(f"  {'utterance':<11}{'E[s]':>9}{'P(all)':>9}{'P(no)':>9}{'P(all) lit':>12}{'P(no) lit':>11}")
for inv, th, tag in ((A, tA, ""), (M, tMs, "*")):
    for y in inv:
        q, ql = q_of(fp(y, th, muA)[0]), q_lit(y)
        print(f"  {y+tag:<11}{Es(q):>9.4f}{mass(q,up):>9.4f}{mass(q,lo):>9.4f}"
              f"{mass(ql,up):>12.4f}{mass(ql,lo):>11.4f}")
print("  (* = run in the mirrored inventory)")

print("\n== C. the scalar member's criterion, each inventory read on its own side ==")
for inv, th, y, reg, rn, tag in ((A, tA, "some", up, "all-region", "as printed"),
                                 (M, tMs, "not all", lo, "no-region", "mirrored"),
                                 (M, tM, "not all", lo, "no-region", "mirrored, at P mu_u")):
    q, ql = q_of(fp(y, th, muA if tag != "mirrored, at P mu_u" else muM)[0]), q_lit(y)
    sh, pos = mass(q, reg) - mass(ql, reg), mass(q, reg)
    print(f"  \"{y}\" vs {rn:<11} ({tag}): shift {sh:+.4f} -> "
          f"{'met' if sh < 0 else 'NOT met'}; position {pos:.4f} -> "
          f"{'met' if pos < 0.5 else 'NOT met'}")
