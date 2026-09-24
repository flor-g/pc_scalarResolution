"""The four criteria as the grid gets COARSER than K = 101, against fine-grid references.
Odd K only (even K ties the central nodes of a symmetric prior). For each K: the plane's four
criteria and two conjunctions cell by cell against K = 801 and K = 401 (the fine grids' own
disagreement is the floor), Part D's nine rows' 36 statuses against K = 801, the number of nodes
inside the cell of "all" (zeta >= theta_L), and P(all) and the peak for the delta-like row.
Run from the repository root."""
import json, torch
nb = json.load(open("main.ipynb")); exec("".join(nb["cells"][5]["source"]))
net = LexicalPredictiveCodingNetwork()
KEYS = ("qs", "qp", "qb", "ms", "mp", "mb")
def verdicts(p):
    upper = (p.zeta >= p.theta_L).to(p.dtype)
    mass = lambda f: float((p.weights * p.read_out(f) * upper).sum())
    lit = mass(p.literal_fixed_point("some")); phi = p.closed_form_fixed_point("some")[0]
    q = mass(phi); node = int(torch.argmax(phi)); pn = int(torch.argmax(p.base_log_prior))
    qs = q - lit < 0 and abs(q - lit) >= 1e-12; qp = q < 0.5
    ms = node < pn; mp = float(p.zeta[node]) < p.theta_L
    return dict(qs=qs, qp=qp, qb=qs and qp, ms=ms, mp=mp, mb=ms and mp, P=q,
                peak=float(torch.sigmoid(p.zeta[node])))
alphas = [2.0 ** k for k in range(11)]; lambdas = [2.0 ** k for k in range(1, 12)]
rows = [(pr, l) for pr in BASE_WORLD_PRIORS.values() for l in (8.0, 512.0)]
rows.append((beta_world_prior(64.0, 1.0), 512.0))
def plane(K):
    return {(a, l): verdicts(net.respawn(num_nodes=K, base_prior=beta_world_prior(a, 1.0), lexical_strength=l))
            for a in alphas for l in lambdas}
def partd(K):
    return [verdicts(net.respawn(num_nodes=K, base_prior=pr, lexical_strength=l)) for pr, l in rows]
ref801, ref401 = plane(801), plane(401)
d801 = partd(801)
agree = lambda A, B, k: sum(A[c][k] == B[c][k] for c in A)
print("floor: K=401 against K=801, cells agreeing of 121:",
      {k: agree(ref401, ref801, k) for k in KEYS})
print()
print(f"{'K':>5}{'h':>7}{'in cell':>8}{'q both':>7}{'mode both':>10}  agree with K=801 (qs qp qb | ms mp mb)"
      f"{'':>4}PartD /36   delta-like P(all), peak   {'error':>6}")
for K in (101, 81, 61, 51, 41, 31, 25, 21, 17, 15, 13, 11, 9, 7, 5):
    try:
        g = plane(K); d = partd(K)
    except Exception as exc:
        print(f"{K:>5}  failed: {type(exc).__name__}: {str(exc)[:80]}"); continue
    probe = net.respawn(num_nodes=K)
    h = float(probe.zeta[1] - probe.zeta[0]); inside = int((probe.zeta >= probe.theta_L).sum())
    a = [agree(g, ref801, k) for k in KEYS]
    pd = sum(d[i][k] == d801[i][k] for i in range(len(rows)) for k in ("qs", "qp", "ms", "mp"))
    print(f"{K:>5}{h:>7.3f}{inside:>8}{sum(v['qb'] for v in g.values()):>7}{sum(v['mb'] for v in g.values()):>10}  "
          f"{a[0]:>4}{a[1]:>4}{a[2]:>4} |{a[3]:>4}{a[4]:>4}{a[5]:>4}{'':>12}{pd:>4}      "
          f"{d[-1]['P']:.4f}, {d[-1]['peak']:.4f}   {d[-1]['P'] - d801[-1]['P']:+.4f}")
