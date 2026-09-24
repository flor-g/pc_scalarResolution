"""Q5 of agent/review_2026-09-23_proof_scope.md: does the delta read-out's mode depend on
the coordinate it is read in? Under "some", each configuration's mode criteria are computed
twice: with the mode as the grid node where phi_S* is largest (the zeta mode, B7/B8), and as
the node where the same distribution's density over s is largest, phi_S* - log s(1-s).
Run from the repository root."""
import json, math, torch
nb = json.load(open("main.ipynb"))
exec("".join(nb["cells"][5]["source"]))

net = LexicalPredictiveCodingNetwork()

def criteria(model):
    s = torch.sigmoid(model.zeta)
    jac = -torch.log(s * (1 - s))
    phiS, _ = model.closed_form_fixed_point("some")
    ell0 = model.base_log_prior
    cell = float(torch.sigmoid(torch.tensor(model.theta_L)))   # all's cell: s >= cell
    out = {}
    for name, extra in (("zeta", 0.0), ("s", jac)):
        m = float(s[int(torch.argmax(phiS + extra))])
        m0 = float(s[int(torch.argmax(ell0 + extra))])
        out[name] = dict(mode=m, base=m0, shift=m - m0 < 0, position=m < cell)
    return out, cell

def row(label, model):
    c, cell = criteria(model)
    z, s = c["zeta"], c["s"]
    flag = "" if (z["shift"], z["position"]) == (s["shift"], s["position"]) else "   <-- differs"
    print(f"{label:28s} theta*={model.theta_u:10.3f} cell s>={cell:.4f} | "
          f"zeta: mode {z['mode']:.5f} base {z['base']:.5f} shift {z['shift']!s:5} pos {z['position']!s:5} | "
          f"s: mode {s['mode']:.5f} base {s['base']:.5f} shift {s['shift']!s:5} pos {s['position']!s:5}{flag}")
    return c

print("PART D, Lambda = 8 and Lambda = 512, under 'some'")
for lam in (8.0, 512.0):
    for name, prior in BASE_WORLD_PRIORS.items():
        row(f"{name} L={lam:.0f}", net.respawn(base_prior=prior, lexical_strength=lam))
row("delta-like Beta(64,1) L=512", net.respawn(base_prior=beta_world_prior(64.0, 1.0), lexical_strength=512.0))

print("\nPLANE, Beta(alpha,1) x Lambda, 121 cells, under 'some'")
alphas = [2.0 ** k for k in range(11)]; lambdas = [2.0 ** k for k in range(1, 12)]
counts = {k: 0 for k in ("shift_z", "shift_s", "pos_z", "pos_s", "both_z", "both_s",
                          "shift_diff", "pos_diff", "both_diff")}
diffs = []
for a in alphas:
    for l in lambdas:
        c, _ = criteria(net.respawn(base_prior=beta_world_prior(a, 1.0), lexical_strength=l))
        z, s = c["zeta"], c["s"]
        counts["shift_z"] += z["shift"]; counts["shift_s"] += s["shift"]
        counts["pos_z"] += z["position"]; counts["pos_s"] += s["position"]
        bz, bs = z["shift"] and z["position"], s["shift"] and s["position"]
        counts["both_z"] += bz; counts["both_s"] += bs
        counts["shift_diff"] += z["shift"] != s["shift"]
        counts["pos_diff"] += z["position"] != s["position"]
        counts["both_diff"] += bz != bs
        if z["position"] != s["position"] or bz != bs:
            diffs.append((a, l, z["mode"], s["mode"], z["position"], s["position"], bz, bs))
print(counts)
print("cells where the position or the conjunction differs (alpha, Lambda, zeta mode, s mode, pos z/s, both z/s):")
for d in diffs:
    print("  ", d)
