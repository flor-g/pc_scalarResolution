"""Acceptance for the complement fix to exclusion_indicator, before it is applied.

OLD = the function as the notebooks ship it. NEW = the proposed replacement.
"""
import math, pathlib, torch

SRC = pathlib.Path("/private/tmp/claude-501/-Users-flog-Desktop-predictive-coding/"
                   "cdd84152-de05-44ad-92e9-458bc1738ed8/scratchpad/cells/cell05_code.txt")
ns = {}
exec(compile(SRC.read_text(), "code_cell_1", "exec"), ns)
OLD, build, U = ns["exclusion_indicator"], ns["build_grid"], ns["UTTERANCES"]

def NEW(utterance, zeta, theta_L, sharpness=None):
    if utterance not in U:
        raise ValueError(f"utterance must be one of {U}")
    if theta_L <= 0:
        raise ValueError("theta_L must be positive")
    if sharpness is not None and sharpness <= 0:
        raise ValueError("sharpness must be positive when given")
    complement = utterance == "some"
    if utterance == "all":
        margin = theta_L - zeta
    else:                                    # "no", and "some" as its complement
        margin = zeta + theta_L
    if sharpness is None:
        chi = (margin > 0).to(zeta.dtype)
    else:
        chi = torch.sigmoid(margin / sharpness)
    return 1.0 - chi if complement else chi

K_LADDER, SHARP = (51, 101, 201, 401, 801), (0.1, 0.5, 1.0, 2.0)
fails = []

def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        fails.append(name)

print("== 1. step branch: identical to OLD on every shipped configuration ==")
worst_step, worst_sm = 0.0, 0.0
nochange = True
for K in K_LADDER:
    z, _ = build(num_nodes=K, half_width=6.0)
    for n in range(2, 202):
        t = math.log(2 * n - 1)
        for y in U:
            if not torch.equal(OLD(y, z, t), NEW(y, z, t)):
                nochange = False
check("step branch unchanged over K x n x utterance", nochange,
      f"({len(K_LADDER) * 200 * 3} comparisons)")

print("\n== 2. smooth branch: equal to OLD within the 1e-12 zero band (I5) ==")
for K in K_LADDER:
    z, _ = build(num_nodes=K, half_width=6.0)
    for n in range(2, 202):
        t = math.log(2 * n - 1)
        for y in U:
            for s in SHARP:
                worst_sm = max(worst_sm, float((OLD(y, z, t, s) - NEW(y, z, t, s)).abs().max()))
check("smooth branch within 1e-12", worst_sm < 1e-12, f"worst {worst_sm:.3e}")
check("smooth branch invisible at 4 printed decimals", worst_sm < 5e-5, f"worst {worst_sm:.3e}")

print("\n== 3. \"no\" and \"all\" are bit-identical (only \"some\" is redefined) ==")
same = all(torch.equal(OLD(y, *a), NEW(y, *a))
           for y in ("no", "all")
           for a in [(build(num_nodes=K, half_width=6.0)[0], math.log(2 * n - 1))
                     for K in K_LADDER for n in (2, 10, 69, 201)])
check("no/all unchanged in the step branch", same)

print("\n== 4. the boundary case the fix exists for ==")
z, _ = build(num_nodes=101, half_width=6.0)
t = 3.0                                       # node 25 sits exactly on -theta_L
j = int(torch.argmin((z + t).abs()))
check("OLD is wrong there (Eq. A1 wants chi_some = 1)", float(OLD("some", z, t)[j]) == 0.0,
      f"OLD chi_some[{j}] = {float(OLD('some', z, t)[j]):.1f}")
check("NEW matches Eq. (A1)", float(NEW("some", z, t)[j]) == 1.0,
      f"NEW chi_some[{j}] = {float(NEW('some', z, t)[j]):.1f}")
d_old = float((OLD("no", z, t) + OLD("some", z, t) - 1).abs().max())
d_new = float((NEW("no", z, t) + NEW("some", z, t) - 1).abs().max())
check("OLD breaks chi_no + chi_some = 1 there (this is the bug)", d_old == 1.0,
      f"max dev {d_old:.1e}")
check("NEW: chi_no + chi_some = 1 everywhere", d_new == 0.0, f"max dev {d_new:.1e}")

print("\n== 5. Eq. (C1): complementary pair projects antipodally ==")
net = ns["LexicalPredictiveCodingNetwork"](theta_L=3.0)
res = {}
for label, f in (("OLD", OLD), ("NEW", NEW)):
    res[label] = float((net.project(f("some", net.zeta, 3.0))
                        + net.project(f("no", net.zeta, 3.0))).abs().max())
check("OLD violates Eq. (C1) there (this is the bug)", res["OLD"] > 1e-3,
      f"residual {res['OLD']:.1e}")
check("NEW satisfies Eq. (C1)", res["NEW"] < 1e-15, f"residual {res['NEW']:.1e}")

print(f"\n{'ACCEPTANCE PASS' if not fails else 'ACCEPTANCE FAIL: ' + ', '.join(fails)}")
raise SystemExit(1 if fails else 0)
