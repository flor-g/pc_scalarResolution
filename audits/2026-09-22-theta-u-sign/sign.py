"""The theta_u* sign flip in Appendix F's conditions: is it a mechanism, and whose?

    .venv/bin/python audits/2026-09-22-theta-u-sign/sign.py

Class (e) until a cell prints it (C6). Evidence, not a change.
"""
import csv, math, torch, nbformat
exec(open("audits/2026-09-22-o13-options/o13_options.py").read().split('print("=" * 104)')[0])

B, Wt = base.basis, base.weights
mu = base.mu_u
G = B.T @ (Wt[:, None] * B)


def net_for(cells, lam):
    return base.respawn(base_prior=elicited(cells), lexical_strength=lam)


def couplings(net, cls, lam):
    chi = chi_of(cls, THETA_L)
    return [net.project(net.base_log_prior - lam * chi),
            net.project(net.base_log_prior - lam * (1.0 - chi))]


def limit_field(net, cls, lam):
    """Eq. (24): phi_S* -> (1/2)(I + B B^T W)(ell_0 - phi_L) as |theta_u| -> inf, from EITHER sign."""
    f = net.base_log_prior - lam * chi_of(cls, THETA_L)
    return 0.5 * (f + torch.mv(B, net.project(f)))


print("=" * 100)
print("1.  WHY THE SIGN IS NOT A PROPERTY OF THE ENTRY.  The ensemble is {chi, ker chi} and")
print("    chi + ker chi = 1 exactly, so sum_y phi_L,y = Lambda * 1 and")
print("        sum_y c_y = B^T W (2 ell_0 - Lambda * 1) = 2 B^T W ell_0,")
print("    because B^T W 1 = 0 (the basis is orthogonal to the constant). Eq. (B2) gives theta_u*")
print("    the sign of <mu_u, sum c>, so THAT SIGN IS FIXED BY THE PRIOR ALONE -- independent of")
print("    Lambda and of which entry was uttered.")
print("=" * 100)
print(f"    B^T W 1 = {[round(float(x), 12) for x in base.project(torch.ones_like(zeta))]}")
worst_id, worst_lam = 0.0, 0.0
for cls in CLASSES:
    for lam in (2.0, 8.0, 48.0, 512.0):
        for k in list(KEYS[cls])[:6]:
            net = net_for(items[k]["prior"], lam)
            got = torch.stack(couplings(net, cls, lam)).sum(dim=0)
            want = 2.0 * net.project(net.base_log_prior)
            worst_id = max(worst_id, float((got - want).abs().max()))
print(f"    max |sum_y c_y  -  2 B^T W ell_0| over 4 Lambda x 2 classes x 6 items: {worst_id:.2e}")

print()
print("=" * 100)
print("2.  THE SIGN PER CONDITION, and whether it moves with Lambda. <mu_u, sum c> = 2<mu_u, B^T W ell_0>.")
print("=" * 100)
print(f"    {'class':<14}{'image':<10}{'n':>4}{'mean <mu,sum c>':>18}{'items < 0':>11}"
      + "".join(f"{'sgn @ L=' + str(l):>12}" for l in (2, 48, 512)))
cond = {}
for cls in CLASSES:
    for img in ("shape", "artifact"):
        keys = [k for k in KEYS[cls] if k[2] == img]
        vals, signs = [], {l: set() for l in (2, 48, 512)}
        for k in keys:
            net = net_for(items[k]["prior"], 48.0)
            a = float(net.dot(mu, torch.stack(couplings(net, cls, 48.0)).sum(dim=0)))
            vals.append(a)
            for l in (2, 48, 512):
                n2 = net_for(items[k]["prior"], float(l))
                signs[l].add(1 if maximizer(n2, [float(l) * chi_of(cls, THETA_L),
                                                 float(l) * (1 - chi_of(cls, THETA_L))]) > 0 else -1)
        cond[(cls, img)] = vals
        print(f"    {cls:<14}{img:<10}{len(keys):>4}{sum(vals)/len(vals):>18.4f}"
              + f"{sum(1 for v in vals if v < 0):>11}"
              + "".join(f"{('+' if signs[l]=={1} else '-' if signs[l]=={-1} else 'mixed'):>12}"
                        for l in (2, 48, 512)))

print()
print("=" * 100)
print("3.  BUT DOES THE SIGN REACH THE BELIEF?  Eq. (24)'s limit is the SAME from both signs, and")
print("    the gap falls as 1/|theta_u|. If the model already sits at that limit, the sign is a")
print("    red herring and the difference between conditions is in ell_0 - phi_L, not in theta_u.")
print("=" * 100)
print(f"    {'class':<14}{'image':<10}{'mean |theta_u*|':>17}{'max |model - Eq24|':>21}"
      f"{'model R2':>11}{'Eq24 R2':>10}{'q_lit R2':>10}")
for cls in CLASSES:
    for img in ("shape", "artifact"):
        keys = [k for k in KEYS[cls] if k[2] == img]
        gap, mags = 0.0, []
        pm, pl, pq, obs = [], [], [], []
        for k in keys:
            it = items[k]
            net = net_for(it["prior"], 48.0)
            th = maximizer(net, [48.0 * chi_of(cls, THETA_L), 48.0 * (1 - chi_of(cls, THETA_L))])
            mags.append(abs(th))
            m = fixed_point(net, 48.0 * chi_of(cls, THETA_L), th)
            L = limit_field(net, cls, 48.0)
            gap = max(gap, float((m - L).abs().max()))
            mp, lp = masses(net, m), masses(net, L)
            qp = masses(net, net.base_log_prior - 48.0 * chi_of(cls, THETA_L))
            for i in range(5):
                if it["obs"][i]:
                    pm.append(mp[i]); pl.append(lp[i]); pq.append(qp[i]); obs.append(it["data"][i])
        print(f"    {cls:<14}{img:<10}{sum(mags)/len(mags):>17.1f}{gap:>21.2e}"
              f"{r2(pm, obs):>11.3f}{r2(pl, obs):>10.3f}{r2(pq, obs):>10.3f}")

print()
print("=" * 100)
print("4.  WHAT THE LIMIT ACTUALLY DOES.  Eq. (24) doubles the span(B) component of ell_0 - phi_L")
print("    and halves nothing else. Mean scale position of the field's read-out at each stage.")
print("=" * 100)
print(f"    {'class':<14}{'image':<10}{'prior':>8}{'q_lit':>8}{'Eq24':>8}{'model':>8}{'data':>8}"
      f"{'  q_lit->Eq24':>14}{'  Eq24 vs data':>15}")
for cls in CLASSES:
    for img in ("shape", "artifact"):
        keys = [k for k in KEYS[cls] if k[2] == img]
        acc = {x: 0.0 for x in ("prior", "q_lit", "eq24", "model", "data")}
        for k in keys:
            it = items[k]
            net = net_for(it["prior"], 48.0)
            th = maximizer(net, [48.0 * chi_of(cls, THETA_L), 48.0 * (1 - chi_of(cls, THETA_L))])
            mp = lambda v: sum((i + 1) * x for i, x in enumerate(v)) / len(keys)
            acc["prior"] += mp(it["prior"]); acc["data"] += mp(it["data"])
            acc["q_lit"] += mp(masses(net, net.base_log_prior - 48.0 * chi_of(cls, THETA_L)))
            acc["eq24"] += mp(masses(net, limit_field(net, cls, 48.0)))
            acc["model"] += mp(masses(net, fixed_point(net, 48.0 * chi_of(cls, THETA_L), th)))
        print(f"    {cls:<14}{img:<10}{acc['prior']:>8.2f}{acc['q_lit']:>8.2f}{acc['eq24']:>8.2f}"
              f"{acc['model']:>8.2f}{acc['data']:>8.2f}"
              f"{acc['eq24'] - acc['q_lit']:>+14.2f}{acc['eq24'] - acc['data']:>+15.2f}")

print()
print("=" * 100)
print("5.  THE MEAN theta_u* WAS A MEANINGLESS STATISTIC.  Sign varies ITEM BY ITEM, and near the")
print("    degenerate ray |theta_u*| blows up, so one item can dominate an average of a quantity")
print("    whose sign is not constant. Median and sign counts instead, at Lambda = 48.")
print("=" * 100)
print(f"    {'class':<14}{'image':<10}{'neg':>5}{'pos':>5}{'mean theta_u*':>15}{'median':>12}"
      f"{'min <mu,sum c>':>16}{'max |theta_u*|':>15}")
for cls in CLASSES:
    for img in ("shape", "artifact"):
        keys = [k for k in KEYS[cls] if k[2] == img]
        ths, aa = [], []
        for k in keys:
            net = net_for(items[k]["prior"], 48.0)
            a = float(net.dot(mu, torch.stack(couplings(net, cls, 48.0)).sum(dim=0)))
            aa.append(a)
            ths.append(maximizer(net, [48.0 * chi_of(cls, THETA_L),
                                       48.0 * (1 - chi_of(cls, THETA_L))]))
        srt = sorted(ths)
        med = srt[len(srt) // 2] if len(srt) % 2 else (srt[len(srt)//2 - 1] + srt[len(srt)//2]) / 2
        print(f"    {cls:<14}{img:<10}{sum(1 for t in ths if t < 0):>5}"
              f"{sum(1 for t in ths if t > 0):>5}{sum(ths)/len(ths):>15.1f}{med:>12.1f}"
              f"{min(abs(a) for a in aa):>16.4f}{max(abs(t) for t in ths):>15.1f}")

print()
print("=" * 100)
print("6.  THE MECHANISM THAT DOES REACH THE BELIEF.  Eq. (24) doubles the span(B) component, which")
print("    displaces the read-out UP the scale by a near-constant amount. The data are displaced by")
print("    very different amounts. Displacement from q_lit, in mean scale position.")
print("=" * 100)
print(f"    {'class':<14}{'image':<10}{'model - q_lit':>16}{'data - q_lit':>15}{'overshoot':>12}")
for cls in CLASSES:
    for img in ("shape", "artifact"):
        keys = [k for k in KEYS[cls] if k[2] == img]
        q = d = m = 0.0
        for k in keys:
            it = items[k]
            net = net_for(it["prior"], 48.0)
            th = maximizer(net, [48.0 * chi_of(cls, THETA_L), 48.0 * (1 - chi_of(cls, THETA_L))])
            mp = lambda v: sum((i + 1) * x for i, x in enumerate(v)) / len(keys)
            q += mp(masses(net, net.base_log_prior - 48.0 * chi_of(cls, THETA_L)))
            d += mp(it["data"])
            m += mp(masses(net, fixed_point(net, 48.0 * chi_of(cls, THETA_L), th)))
        print(f"    {cls:<14}{img:<10}{m - q:>+16.2f}{d - q:>+15.2f}{m - d:>+12.2f}")
