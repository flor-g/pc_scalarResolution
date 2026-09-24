"""Probe: Part D's evaluations with Lambda = 512 for every prior (scratch, no project edits).

Code cell 1 and Code Cell 2's definitions are exec'd verbatim from main.ipynb; Code Cell 2's
RUN block is not. theta_u* is re-learned per configuration (decision D2) by respawn.
Closed form throughout (Eqs. 15-16); a Lambda = 8 pass reproduces the stored Part D table first.
"""
import math, sys, nbformat, torch

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(nb.cells[5].source, ns)
src = nb.cells[7].source
exec(src[: src.index("evaluation_network = LexicalPredictiveCodingNetwork()")], ns)
g = type("NS", (), ns)

UTT = ns["UTTERANCES"]


def row_for(net, name, prior, lam):
    probe = net.respawn(base_prior=prior, lexical_strength=lam)
    up = (probe.zeta > probe.theta_L).to(probe.dtype)
    mass = lambda q: float((probe.weights * q * up).sum())
    out = {"theta": probe.theta_u, "prior_upper": mass(torch.exp(probe.base_log_prior)), "u": {}}
    for y in UTT:
        phi_S, phi_u = probe.closed_form_fixed_point(y)
        lit = probe.literal_fixed_point(y)
        tmp = probe.closed_form_fixed_point(y, theta_u=0.0)[0]
        exc = ns["exclusion_indicator"](y, probe.zeta, probe.theta_L, sharpness=probe.exclusion_sharpness)
        q = probe.read_out(phi_S)
        out["u"][y] = {
            "full": mass(q), "lit": mass(probe.read_out(lit)), "temp": mass(probe.read_out(tmp)),
            "leak": float((probe.weights * q * exc).sum()),
            "Es": float((probe.weights * q * ns["logistic"](probe.zeta)).sum()),
            "peak": int(torch.argmax(phi_S)), "phi_u": [float(v) for v in phi_u],
        }
    s = out["u"]["some"]
    s["shift"] = s["full"] - s["lit"]
    for y in UTT:
        out["u"][y]["shift"] = out["u"][y]["full"] - out["u"][y]["lit"]
    k0 = int(torch.argmax(probe.base_log_prior))
    ks = s["peak"]
    sz = lambda k: float(ns["logistic"](probe.zeta[k]))
    out["delta"] = {
        "ell0_s": sz(k0), "some_s": sz(ks),
        "a": ks < k0, "b": float(probe.zeta[ks]) < probe.theta_L,
        "ell0_inside": float(probe.zeta[k0]) >= probe.theta_L,
    }
    out["rate"] = probe.stiffest_state_rate(probe.theta_u)
    thr = ns["criterion_threshold"](probe)
    out["thr"] = thr
    out["arrival"] = ns["updates_to_criterion"](probe) if thr is not None else None
    out["probe"] = probe
    return out


def report(lam_of, title):
    net = g.LexicalPredictiveCodingNetwork()
    priors = ns["part_d_priors"]()
    rows = {}
    for name, spec in priors.items():
        prior = spec[0] if isinstance(spec, tuple) else spec
        rows[name] = row_for(net, name, prior, lam_of(name))
    print(title)
    print(f"  {'prior':<13}{'Lambda':>7}{'theta_u*':>12}{'P0(all)':>9}"
          f"{'shift no':>10}{'some':>9}{'all':>9}{'max leak':>10}{'P(all|some)':>13}{'1st':>5}{'2nd':>5}")
    for name, r in rows.items():
        u = r["u"]; s = u["some"]
        leak = max(u[y]["leak"] for y in UTT)
        print(f"  {name:<13}{lam_of(name):>7.0f}{r['theta']:>12.4f}{r['prior_upper']:>9.4f}"
              f"{u['no']['shift']:>+10.4f}{s['shift']:>+9.4f}{u['all']['shift']:>+9.4f}{leak:>10.1e}"
              f"{s['full']:>13.4f}{('met' if s['shift'] < 0 else '-'):>5}{('met' if s['full'] < .5 else '-'):>5}")
    print()
    print(f"  {'prior':<13}{'E[s] no':>9}{'some':>8}{'all':>8}   {'q_lit some':>10}{'tempered':>10}"
          f"{'tempering':>11}{'utility':>9}   {'P(all|all) lit':>15}{'full':>8}")
    for name, r in rows.items():
        u = r["u"]; s = u["some"]
        print(f"  {name:<13}{u['no']['Es']:>9.3f}{s['Es']:>8.3f}{u['all']['Es']:>8.3f}   {s['lit']:>10.4f}"
              f"{s['temp']:>10.4f}{s['temp'] - s['lit']:>+11.4f}{s['shift'] - (s['temp'] - s['lit']):>+9.4f}"
              f"   {u['all']['lit']:>15.4f}{u['all']['full']:>8.4f}")
    print()
    print(f"  {'prior':<13}{'lambda_max(H)*':>15}{'theta_crit':>12}{'lambda(crit)':>14}{'updates':>9}{'holds to *':>12}"
          f"   delta: {'ell_0 peak s':>12}{'some peak s':>12}{'(a)':>5}{'(b)':>5}")
    for name, r in rows.items():
        t, a, d = r["thr"], r["arrival"], r["delta"]
        tc = (f"{t['theta_u']:>12.3f}{t['rate']:>14.1f}{(a['updates'] if a else '>60'):>9}{str(t['holds_to_star']):>12}"
              if t else f"{'no conjunction at theta_u*':>47}")
        print(f"  {name:<13}{r['rate']:>15.2e}{tc}   {'':7}{d['ell0_s']:>12.4f}{d['some_s']:>12.4f}"
              f"{('met' if d['a'] else '-'):>5}{('met' if d['b'] else '-'):>5}")
    print()
    return rows


base = report(lambda n: 512.0 if n == "delta (all)" else 8.0,
              "REPRODUCTION: Part D as stored (Lambda = 8, delta row 512)")
new = report(lambda n: 512.0, "PROBE: Lambda = 512 for every prior")

# phi_u* per utterance at Lambda = 512, and the mechanism's c_y projections
print("  phi_u* (tilt, width) at Lambda = 512, and c_y = B^T W (ell_0 - phi_L)")
for name, r in new.items():
    p = r["probe"]
    c = {y: p.project(p.base_log_prior - p.lexical_field(y)) for y in UTT}
    print(f"  {name:<13}" + "  ".join(f"{y}: phi_u [{v['phi_u'][0]:+.3f},{v['phi_u'][1]:+.3f}] c [{float(c[y][0]):+.1f},{float(c[y][1]):+.1f}]"
                                     for y, v in r["u"].items()))
