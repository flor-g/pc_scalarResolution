import json, time, torch
nb = json.load(open("main.ipynb")); exec("".join(nb["cells"][5]["source"]))
net = LexicalPredictiveCodingNetwork()
def verdicts(p):
    upper = (p.zeta >= p.theta_L).to(p.dtype)
    mass = lambda f: float((p.weights * p.read_out(f) * upper).sum())
    lit = mass(p.literal_fixed_point("some")); phi = p.closed_form_fixed_point("some")[0]
    q = mass(phi); node = int(torch.argmax(phi)); pn = int(torch.argmax(p.base_log_prior))
    return (q - lit < 0 and abs(q - lit) >= 1e-12, q < 0.5, node < pn, float(p.zeta[node]) < p.theta_L,
            q, float(torch.sigmoid(p.zeta[node])), p.theta_u)
rows = [(f"{n} L={l:g}", pr, l) for n, pr in BASE_WORLD_PRIORS.items() for l in (8.0, 512.0)]
rows.append(("delta-like L=512", beta_world_prior(64.0, 1.0), 512.0))
say = lambda b: "Y" if b else "."
for K in (101, 201, 401, 801, 1601):
    t0 = time.time()
    line = []
    for name, pr, l in rows:
        v = verdicts(net.respawn(num_nodes=K, base_prior=pr, lexical_strength=l))
        line.append(f"{name}: {''.join(say(x) for x in v[:4])} P(all)={v[4]:.4f} peak={v[5]:.4f}")
    plane = [0, 0, 0, 0, 0, 0]
    if K <= 801:
        for a in [2.0 ** k for k in range(11)]:
            for l in [2.0 ** k for k in range(1, 12)]:
                v = verdicts(net.respawn(num_nodes=K, base_prior=beta_world_prior(a, 1.0), lexical_strength=l))
                plane[0] += v[0]; plane[1] += v[1]; plane[2] += v[0] and v[1]
                plane[3] += v[2]; plane[4] += v[3]; plane[5] += v[2] and v[3]
    print(f"K={K}  plane q shift/position/both {plane[0]}/{plane[1]}/{plane[2]}  mode shift/position/both {plane[3]}/{plane[4]}/{plane[5]}  ({time.time()-t0:.0f}s)")
    for x in line: print("   ", x)
