"""Which plane cells change status between K = 101 and finer grids, and whether the delta
conjunction stays a subset of the q conjunction. Run from the repository root."""
import json, torch
nb = json.load(open("main.ipynb")); exec("".join(nb["cells"][5]["source"]))
net = LexicalPredictiveCodingNetwork()
def verdicts(p):
    upper = (p.zeta >= p.theta_L).to(p.dtype)
    mass = lambda f: float((p.weights * p.read_out(f) * upper).sum())
    lit = mass(p.literal_fixed_point("some")); phi = p.closed_form_fixed_point("some")[0]
    q = mass(phi); node = int(torch.argmax(phi)); pn = int(torch.argmax(p.base_log_prior))
    qs = q - lit < 0 and abs(q - lit) >= 1e-12
    return dict(qb=qs and q < 0.5, mb=node < pn and float(p.zeta[node]) < p.theta_L,
                qs=qs, qp=q < 0.5, shift=q - lit, P=q)
alphas = [2.0 ** k for k in range(11)]; lambdas = [2.0 ** k for k in range(1, 12)]
grid = {}
for K in (101, 201, 401, 801):
    grid[K] = {(a, l): verdicts(net.respawn(num_nodes=K, base_prior=beta_world_prior(a, 1.0), lexical_strength=l))
               for a in alphas for l in lambdas}
    rev = sum(v["mb"] and not v["qb"] for v in grid[K].values())
    print(f"K={K}: q both {sum(v['qb'] for v in grid[K].values())}, mode both {sum(v['mb'] for v in grid[K].values())}, "
          f"mode-both-not-q-both {rev}")
for K in (201, 401, 801):
    for key in grid[101]:
        a, b = grid[101][key], grid[K][key]
        for f in ("qs", "qp", "qb", "mb"):
            if a[f] != b[f]:
                print(f"  K=101->{K} cell alpha={key[0]:g} Lambda={key[1]:g}: {f} {a[f]}->{b[f]}  "
                      f"shift {a['shift']:+.2e}->{b['shift']:+.2e}  P(all) {a['P']:.4f}->{b['P']:.4f}")
