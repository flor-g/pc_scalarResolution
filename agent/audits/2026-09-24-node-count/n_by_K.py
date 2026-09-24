"""Appendix A's n ladder at other node counts: are its statuses stable in K, and how many nodes
does the all-region hold at K = 101? Read-only; the evidence behind sections_3-6.md 5.5's "the
evaluations it reports do not need it" (the (K, Z) proposal). Run from the repository root."""
import json, math, torch
nb = json.load(open("main.ipynb")); exec("".join(nb["cells"][5]["source"]))
net = LexicalPredictiveCodingNetwork()
def v(p):
    up = (p.zeta >= p.theta_L).to(p.dtype); mass = lambda f: float((p.weights * p.read_out(f) * up).sum())
    lit = mass(p.literal_fixed_point("some")); phi = p.closed_form_fixed_point("some")[0]; q = mass(phi)
    node = int(torch.argmax(phi)); pn = int(torch.argmax(p.base_log_prior))
    return (q - lit < 0 and abs(q - lit) >= 1e-12, q < 0.5, node < pn, float(p.zeta[node]) < p.theta_L)
ladder = (2, 3, 4, 5, 10, 15, 20, 50, 100, 201)
cfg = [(l, pr) for l in (8.0, 512.0) for pr in BASE_WORLD_PRIORS.values()]
print("statuses (of 32 = 8 blocks x 4 criteria) agreeing with K = 801, per n;")
print("nodes in the all-region at K = 101, and the least odd K giving 21 of them at Z = 6")
print(f"{'n':>4}{'K=101':>7}{'K=201':>7}{'K=401':>7}{'in region':>11}{'K for 21':>10}")
for n in ladder:
    ref = [v(net.respawn(num_atoms=n, num_nodes=801, lexical_strength=l, base_prior=pr)) for l, pr in cfg]
    row = []
    for K in (101, 201, 401):
        got = [v(net.respawn(num_atoms=n, num_nodes=K, lexical_strength=l, base_prior=pr)) for l, pr in cfg]
        row.append(sum(a == b for g, r in zip(got, ref) for a, b in zip(g, r)))
    probe = net.respawn(num_atoms=n); inside = int((probe.zeta >= probe.theta_L).sum())
    th, K = math.log(2 * n - 1), 5
    while sum(-6 + 12 * k / (K - 1) >= th for k in range(K)) < 21: K += 2
    print(f"{n:>4}" + "".join(f"{x:>7}" for x in row) + f"{inside:>11}{K:>10}")
