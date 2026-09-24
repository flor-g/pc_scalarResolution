"""Does a read-out that assumes a unimodal posterior and compares only neighbours reproduce the
mode criteria? Under "some", for each configuration: (1) the number of strict local maxima of
phi_S* and of ell_0; (2) the mode position criterion from the unit that exceeds both neighbours,
against the argmax; (3) the mode shift criterion from the sign of ell_0's slope at that unit
(k* < k0 iff ell_0 rises from k* to k*+1, when ell_0 has one local maximum), against the argmax.
Configurations: Part D's priors at Lambda 8 and 512 plus the delta-like row, over Z in {6, 8},
K in {101, 201}, n in {2, 4, 10, 20}; and the 121-cell plane at the defaults. Run from the root."""
import json, itertools, torch
nb = json.load(open("main.ipynb")); exec("".join(nb["cells"][5]["source"]))

def local_maxima(v):
    v = v.tolist(); n = len(v)
    return [k for k in range(n) if (k == 0 or v[k] > v[k-1]) and (k == n-1 or v[k] > v[k+1])]

def check(model):
    phiS, _ = model.closed_form_fixed_point("some")
    ell0 = model.base_log_prior
    lm, lm0 = local_maxima(phiS), local_maxima(ell0)
    kstar, k0 = int(torch.argmax(phiS)), int(torch.argmax(ell0))
    shift_argmax, pos_argmax = kstar < k0, float(model.zeta[kstar]) < model.theta_L
    if len(lm) != 1:
        return len(lm), len(lm0), None, None
    k = lm[0]
    pos_local = float(model.zeta[k]) < model.theta_L
    shift_local = k + 1 < len(ell0) and float(ell0[k + 1]) > float(ell0[k])
    return len(lm), len(lm0), pos_local == pos_argmax, shift_local == shift_argmax

priors = dict(BASE_WORLD_PRIORS)
rows = [(n, p, l) for n, p in priors.items() for l in (8.0, 512.0)]
rows.append(("delta-like", beta_world_prior(64.0, 1.0), 512.0))
total = unimodal = unimodal0 = agree_pos = agree_shift = 0
for (Z, K, n) in itertools.product((6.0, 8.0), (101, 201), (2, 4, 10, 20)):
    base = LexicalPredictiveCodingNetwork(grid_half_width=Z, num_nodes=K, num_atoms=n)
    for name, p, l in rows:
        c, c0, ap, ash = check(base.respawn(base_prior=p, lexical_strength=l))
        total += 1; unimodal += c == 1; unimodal0 += c0 == 1
        agree_pos += bool(ap); agree_shift += bool(ash)
        if c != 1 or c0 != 1 or not ap or not ash:
            print(f"  exception: Z={Z} K={K} n={n} {name} L={l:.0f}: maxima phi_S* {c}, ell_0 {c0}, "
                  f"position agrees {ap}, shift agrees {ash}")
print(f"Part D rows over Z x K x n: {total} configurations; phi_S* unimodal in {unimodal}, "
      f"ell_0 unimodal in {unimodal0}; local rule agrees with argmax: position {agree_pos}, shift {agree_shift}")

net = LexicalPredictiveCodingNetwork()
total = unimodal = unimodal0 = agree_pos = agree_shift = 0
for a in [2.0 ** k for k in range(11)]:
    for l in [2.0 ** k for k in range(1, 12)]:
        c, c0, ap, ash = check(net.respawn(base_prior=beta_world_prior(a, 1.0), lexical_strength=l))
        total += 1; unimodal += c == 1; unimodal0 += c0 == 1
        agree_pos += bool(ap); agree_shift += bool(ash)
print(f"plane: {total} cells; phi_S* unimodal in {unimodal}, ell_0 unimodal in {unimodal0}; "
      f"local rule agrees with argmax: position {agree_pos}, shift {agree_shift}")
