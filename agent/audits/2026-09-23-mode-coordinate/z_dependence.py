"""Point 1 of Q5: the s-read baselines sit on the grid's edge node, so they move with the
half-width Z; the zeta-read ones do not. Also: where the s-density of each base prior peaks
analytically. Run from the repository root."""
import json, torch
nb = json.load(open("main.ipynb")); exec("".join(nb["cells"][5]["source"]))
rows = {"gaussian": gaussian_world_prior(0.0, 1.0), "flat": uniform_world_prior(),
        "Beta(1,3)": beta_world_prior(1.0, 3.0), "Beta(3,1)": beta_world_prior(3.0, 1.0),
        "Beta(64,1)": beta_world_prior(64.0, 1.0)}
for Z in (6.0, 8.0):
    net = LexicalPredictiveCodingNetwork(grid_half_width=Z)
    print(f"Z = {Z}: grid edge nodes s = {float(torch.sigmoid(net.zeta[0])):.5f}, {float(torch.sigmoid(net.zeta[-1])):.5f}")
    for name, prior in rows.items():
        m = net.respawn(base_prior=prior, **({"lexical_strength": 512.0} if name == "Beta(64,1)" else {}))
        s = torch.sigmoid(m.zeta); jac = -torch.log(s * (1 - s))
        phiS, _ = m.closed_form_fixed_point("some")
        f = lambda v: float(s[int(torch.argmax(v))])
        print(f"   {name:10s} base mode: zeta-read {f(m.base_log_prior):.5f}  s-read {f(m.base_log_prior + jac):.5f}"
              f"  | model mode under 'some': zeta-read {f(phiS):.5f}  s-read {f(phiS + jac):.5f}")
