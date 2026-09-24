"""Q5 follow-up: is the peak of phi_S* detectable by neighbour comparison alone? Counts the
strict local maxima of phi_S* (node larger than both neighbours; an edge node larger than its
one neighbour) for every utterance, over Part D's rows and the 121-cell plane. Run from the root."""
import json, torch
nb = json.load(open("main.ipynb")); exec("".join(nb["cells"][5]["source"]))
net = LexicalPredictiveCodingNetwork()
def local_maxima(v):
    v = v.tolist(); n = len(v)
    return [k for k in range(n) if (k == 0 or v[k] > v[k-1]) and (k == n-1 or v[k] > v[k+1])]
def report(label, model, show=True):
    out = {}
    for u in UTTERANCES:
        phiS, _ = model.closed_form_fixed_point(u)
        lm = local_maxima(phiS); g = int(torch.argmax(phiS))
        out[u] = (len(lm), g in lm, [round(float(torch.sigmoid(model.zeta[k])), 4) for k in lm])
    if show: print(f"{label:24s}", {u: out[u] for u in UTTERANCES})
    return out
cfg = [(n, p, 8.0) for n, p in BASE_WORLD_PRIORS.items()] + [(n, p, 512.0) for n, p in BASE_WORLD_PRIORS.items()]
cfg.append(("delta-like", beta_world_prior(64.0, 1.0), 512.0))
for n, p, l in cfg:
    report(f"{n} L={l:.0f}", net.respawn(base_prior=p, lexical_strength=l))
hist = {}
for a in [2.0 ** k for k in range(11)]:
    for l in [2.0 ** k for k in range(1, 12)]:
        out = report("", net.respawn(base_prior=beta_world_prior(a, 1.0), lexical_strength=l), show=False)
        for u, (c, _, _) in out.items(): hist[(u, c)] = hist.get((u, c), 0) + 1
print("plane, 121 cells: (utterance, number of local maxima) -> cells:", dict(sorted(hist.items())))
