"""Audit 2026-09-17: the user's hypothesis about scale classes, against the current model and
against Xiang, Kennedy, Xu & Leffel (2022). Nothing here is written back into the notebooks.

Run from the project folder:
    .venv/bin/python audits/2026-09-17-scale-classes/scale_classes.py

THE HYPOTHESIS (the user's, 2026-09-17)
  H1. Scalar expressions with UNSTABLE ATOMICITY carry WEAKER LEXICAL STRENGTH.
      Atomicity is n (Eq. A5) or its reciprocal delta (Eq. A6); lexical strength is Lambda
      (Text cell 3 Sec. 2, the scalar of phi_L = Lambda chi_y).
  H2. Open-scale adjectives behave like "some"; complete-scale adjectives like endpoint(s) + "some".

INSTANTIATION
  Xiang et al. use five scale positions, so the predicate resolves n = 4 atoms: theta_L = log 7 =
  1.9459 (Eq. A5), and the five Voronoi cells of the counts k = 0..4 ARE the five scale positions.
  Under Eq. (A1) at that theta_L:
    MAX  maximum-standard absolute ("straight", "full")  = the model's "all":  excludes zeta < theta_L,
         i.e. every position but 5.
    MIN  minimum-standard absolute ("bent", "spotted")   = the model's "some": excludes zeta <= -theta_L,
         i.e. position 1 only.
    REL  relative ("tall")   = a cut at a context-set t, anchored by neither endpoint nor the
         resolution limit.  chi_t = 1[zeta < t], a node on the cut half-weighted.
  Exposure ensembles (A9, decisions.md O8), each configuration learning its own theta_u*:
    complete scale  {MAX, MIN}      -- the antonym pair a closed scale carries: endpoint + "some".
    open scale      {REL(t), REL(-t)} -- "tall"/"short", the pair an open scale carries.
  Priors. Xiang et al. Exp. 1 elicited one prior per IMAGE SET, shared by the antonym pair and
  REVERSED for the second member. Absolute image sets put mass at a scalar endpoint; relative ones
  are spread out; SHAPES are more categorical than ARTIFACTS ("artifacts tend to have a less
  categorical distribution than shapes, in particular for the dimensions corresponding to absolute
  adjectives", p. 9:19). So here: absolute -> Beta(a, 1) in the MAX orientation and its mirror
  Beta(1, a) in the MIN orientation, with a larger for shapes than for artifacts; relative ->
  Beta(1, 1), which is mirror-symmetric.
  Lambda is NOT assumed: it is scanned, and the audit reports which Lambda each class needs to
  reproduce its measured profile. H1 predicts the ordering Lambda(MAX) > Lambda(REL) > Lambda(MIN),
  because the MAX threshold is anchored by the scale's endpoint, the REL threshold by context, and
  the MIN threshold IS the resolution limit -delta/2 and so inherits all of delta's instability.
"""
import ast
import math

import nbformat
import torch

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)

Net = ns["LexicalPredictiveCodingNetwork"]
beta_prior = ns["beta_world_prior"]
gaussian_prior = ns["gaussian_world_prior"]

N_ATOMS = 4
THETA_L = math.log(2 * N_ATOMS - 1)
net = Net(num_atoms=N_ATOMS)
zeta, W, B = net.zeta, net.weights, net.basis
G = B.T @ (W[:, None] * B)
mu = net.mu_u
s_grid = torch.sigmoid(zeta)
assert net.sigma_lexical == net.sigma_state == net.sigma_utility == 1.0
ODD = next(j for j in range(B.shape[1]) if float((B[:, j] + B[:, j].flip(0)).abs().max()) < 1e-9)
EVEN = next(j for j in range(B.shape[1]) if float((B[:, j] - B[:, j].flip(0)).abs().max()) < 1e-9)


# ---------------------------------------------------------------- closed forms (Eqs. 15-16)
def fixed_point(ell0, phi_L, theta):
    c = B.T @ (W * (ell0 - phi_L))
    phi_u = torch.linalg.solve(torch.eye(G.shape[0], dtype=G.dtype) + theta ** 2 * G / 2,
                               mu + theta * c / 2)
    return ((ell0 - phi_L) + theta * (B @ phi_u)) / 2, phi_u


def free_energy(ell0, phi_L, theta):
    phi_S, phi_u = fixed_point(ell0, phi_L, theta)
    r_L = phi_L - ell0 + phi_S
    r_S = phi_S - theta * (B @ phi_u)
    r_u = phi_u - mu
    return (-0.5 * float(torch.sum(W * r_L ** 2)) - 0.5 * float(torch.sum(W * r_S ** 2))
            - 0.5 * float(torch.sum(r_u ** 2)))


def learned_theta(ell0, fields):
    """Maximizer of F~ over an exposure ensemble (Eq. B2 / A9): dense scan, golden-section refine."""
    f = lambda th: sum(free_energy(ell0, phi_L, th) for phi_L in fields) / len(fields)
    grid = [0.0] + [sgn * 10 ** e for sgn in (1, -1) for e in [x / 40 for x in range(-120, 201)]]
    best = max(grid, key=f)
    lo, hi = best - abs(best) * 0.2 - 1e-3, best + abs(best) * 0.2 + 1e-3
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        a, b = hi - g * (hi - lo), lo + g * (hi - lo)
        if f(a) > f(b):
            hi = b
        else:
            lo = a
    return (lo + hi) / 2


def read_out(phi):
    shifted = phi - phi.max()
    q = torch.exp(shifted)
    return q / torch.sum(W * q)


def mean_s(phi):
    return float(torch.sum(W * read_out(phi) * s_grid))


def mode_s(phi):
    return float(s_grid[int(torch.argmax(phi))])


# ---------------------------------------------------------------- the five scale positions
BOUNDS = [math.log((k + 0.5) / N_ATOMS / (1 - (k + 0.5) / N_ATOMS)) for k in range(N_ATOMS)]


def positions(phi):
    """q-mass in each of the five Voronoi cells of the counts k = 0..4 (Appendix A)."""
    q = read_out(phi) * W
    edges = [-math.inf] + BOUNDS + [math.inf]
    return [float(q[(zeta > edges[i]) & (zeta <= edges[i + 1])].sum()) for i in range(N_ATOMS + 1)]


def fmt(profile):
    return " ".join(f"{v:5.2f}" for v in profile)


def peak_position(profile):
    return 1 + max(range(len(profile)), key=lambda i: profile[i])


# ---------------------------------------------------------------- the three entries
def chi_cut(t):
    chi = (zeta < t).to(zeta.dtype)
    chi[(zeta - t).abs() < 1e-12] = 0.5
    return chi


CHI = {
    "MAX": ns["exclusion_indicator"]("all", zeta, THETA_L),    # excludes zeta < theta_L
    "MIN": ns["exclusion_indicator"]("some", zeta, THETA_L),   # excludes zeta <= -theta_L
}


def chi_of(cls, t=0.0):
    return CHI[cls] if cls in CHI else chi_cut(t)


# ---------------------------------------------------------------- self-checks
print("SELF-CHECKS")
ref = Net(num_atoms=N_ATOMS)
a, b = ref.closed_form_fixed_point("some", theta_u=3.7)
c, d = fixed_point(ref.base_log_prior, ref.lexical_field("some"), 3.7)
print(f"  closed form here against Code Cell 1: {float((a - c).abs().max()):.1e}, "
      f"{float((b - d).abs().max()):.1e}")
full = Net()  # the default network, n = 10
th = learned_theta(full.base_log_prior, [full.lexical_field(y) for y in ("no", "some", "all")])
print(f"  theta_u* recovered for the default n = 10 network: {th:.4f}  (Code Cell 2 prints -28.4375)")
print(f"  n = {N_ATOMS}: theta_L = {THETA_L:.4f}, cell of the top count s >= "
      f"{1 - 1 / (2 * N_ATOMS):.3f}, cell of the bottom count s <= {1 / (2 * N_ATOMS):.3f}")
print(f"  MAX excludes {int((CHI['MAX'] > 0).sum())} of {len(zeta)} nodes, "
      f"MIN excludes {int((CHI['MIN'] > 0).sum())}, a midpoint REL cut excludes "
      f"{float(chi_cut(0.0).sum()):.1f}")
print(f"  the five cells partition the grid: masses sum to "
      f"{sum(positions(ref.base_log_prior)):.10f} under the prior alone")
print()


# ---------------------------------------------------------------- the profiles Xiang et al. report
print("WHAT XIANG ET AL. (2022) REPORT, as the target (Exp. 3, posterior degrees, five positions)")
print("  MAX  'participants consistently chose the maximum degree'                      -> peak at 5, near-categorical")
print("  MIN  'distributed among all the non-minimal degrees', 'peaking around the")
print("        middle part of the scale'                                                -> 2-5, peak at 3")
print("  REL  'clustered mainly on degrees above the mid-point'; the maximum has the")
print("        highest probability, with mass also at position 4                        -> 4-5, peak at 5")
print("  Exp. 2 (truth value judgments): more positive responses for MIN than REL than MAX;")
print("  the ONLY class with a credible image-type effect is MIN (shapes > artifacts, 2.54 [0.54, 4.38]).")
print("  Model fit by class (their Table 5 and Sec. 4): posterior R^2 MAX .94/.97, REL .69/.78, MIN .55/.58;")
print("  the semantic-threshold model .98/.58/.19 and the hybrid .97/.80/.32. MIN is every model's residual.")
print()


# ---------------------------------------------------------------- priors
def priors_for(kind, sharpness):
    """(MAX-orientation prior, MIN-orientation prior). Absolute image sets put mass at an endpoint
    and the antonym's prior is the same distribution reversed; relative sets are spread out."""
    if kind == "absolute":
        return beta_prior(sharpness, 1.0), beta_prior(1.0, sharpness)
    return beta_prior(1.0, 1.0), beta_prior(1.0, 1.0)


def ell0_of(prior):
    return net.respawn(base_prior=prior).base_log_prior


LAMBDAS = (0.5, 1, 2, 4, 8, 16, 32, 64, 128, 512)
CONDITIONS = {"artifacts (less categorical prior)": 3.0, "shapes (more categorical prior)": 12.0}

print("=" * 118)
print("1. PROFILES BY CLASS, SCANNED IN LAMBDA. Each row learns its own theta_u* (A9) over the")
print("   exposure ensemble its scale carries: {MAX, MIN} for a complete scale, {REL(t), REL(-t)} for")
print("   an open one. 'profile' is q-mass on the five positions; 'leak' is q-mass on the positions")
print("   the entry excludes; 'mode' is the peak of phi_S* (the delta read-out) as a position.")
print("=" * 118)

REL_CUT = 0.0  # the context threshold for a relative adjective: the midpoint of the scale
records = {}
for condition, sharp in CONDITIONS.items():
    print(f"\n  CONDITION: {condition}   (absolute sets Beta({sharp:g}, 1) / its mirror; relative sets Beta(1, 1))")
    for cls in ("MAX", "MIN", "REL"):
        kind = "relative" if cls == "REL" else "absolute"
        prior_max, prior_min = priors_for(kind, sharp)
        prior = prior_min if cls == "MIN" else prior_max
        ell0 = ell0_of(prior)
        chi = chi_of(cls, REL_CUT)
        if cls == "REL":
            partner = chi_cut(-REL_CUT)
            partner = 1.0 - chi_cut(REL_CUT) if abs(REL_CUT) < 1e-12 else partner
        else:
            partner = CHI["MIN"] if cls == "MAX" else CHI["MAX"]
        print(f"    {cls}  prior {prior.description}")
        print(f"      {'Lambda':>7}{'theta_u*':>12}{'E[s]':>8}{'mode':>6}{'peak':>6}   {'profile 1..5':>29}"
              f"{'leak':>8}{'shift vs q_lit':>16}")
        for lam in LAMBDAS:
            phi_L, phi_P = lam * chi, lam * partner
            th = learned_theta(ell0, [phi_L, phi_P])
            phi_S, _ = fixed_point(ell0, phi_L, th)
            prof = positions(phi_S)
            q = read_out(phi_S) * W
            leak = float(q[chi > 0.5].sum())
            lit = ell0 - phi_L
            shift = mean_s(phi_S) - mean_s(lit)
            records[(condition, cls, lam)] = (th, prof, leak, mean_s(phi_S), mode_s(phi_S))
            print(f"      {lam:>7g}{th:>12.2f}{mean_s(phi_S):>8.3f}"
                  f"{sum(1 for bnd in BOUNDS if mode_s(phi_S) > 1 / (1 + math.exp(-bnd))) + 1:>6}"
                  f"{peak_position(prof):>6}   {fmt(prof):>29}{leak:>8.3f}{shift:>+16.4f}")


print()
print("=" * 118)
print("2. WHICH LEVEL PRODUCES THE PROFILE. q_lit (ell_0 - phi_L, the literal listener), the tempered")
print("   control (theta_u = 0), and the model at its own theta_u*, on the five positions.")
print("=" * 118)
for condition, sharp in CONDITIONS.items():
    print(f"\n  CONDITION: {condition}")
    for cls, lam in (("MAX", 8), ("MIN", 8), ("MIN", 16), ("MIN", 32), ("REL", 8), ("REL", 4)):
        kind = "relative" if cls == "REL" else "absolute"
        prior_max, prior_min = priors_for(kind, sharp)
        ell0 = ell0_of(prior_min if cls == "MIN" else prior_max)
        chi = chi_of(cls, REL_CUT)
        partner = (1.0 - chi_cut(REL_CUT)) if cls == "REL" else (CHI["MIN"] if cls == "MAX" else CHI["MAX"])
        phi_L = lam * chi
        th = learned_theta(ell0, [phi_L, lam * partner])
        lit = ell0 - phi_L
        tempered, _ = fixed_point(ell0, phi_L, 0.0)
        full, _ = fixed_point(ell0, phi_L, th)
        print(f"    {cls} Lambda = {lam:<4g} theta_u* = {th:>10.2f}")
        for label, field in (("prior alone", ell0), ("q_lit", lit),
                             ("tempered (theta_u = 0)", tempered), ("model (theta_u*)", full)):
            prof = positions(field)
            print(f"      {label:<24} {fmt(prof)}   peak {peak_position(prof)}   E[s] {mean_s(field):.3f}"
                  f"   mode {mode_s(field):.3f}")

print()
print("=" * 118)
print("3. THE CONFLICT BETWEEN EACH CLASS'S ENTRY AND ITS OWN PRIOR. 'override Lambda' is the least")
print("   Lambda at which the entry holds (leak < 1/2) at the class's own theta_u*; a class whose")
print("   prior piles up on the states its entry excludes needs a large one.")
print("=" * 118)
print(f"    {'class':<6}{'prior':<22}{'sharpness':>10}{'prior mass on the':>19}{'override':>10}")
print(f"    {'':<6}{'':<22}{'':>10}{'excluded cells':>19}{'Lambda':>10}")
for sharp in (1.0, 3.0, 6.0, 12.0, 24.0):
    for cls in ("MAX", "MIN", "REL"):
        kind = "relative" if cls == "REL" else "absolute"
        prior_max, prior_min = priors_for(kind, sharp)
        prior = prior_min if cls == "MIN" else prior_max
        ell0 = ell0_of(prior)
        chi = chi_of(cls, REL_CUT)
        partner = (1.0 - chi_cut(REL_CUT)) if cls == "REL" else (CHI["MIN"] if cls == "MAX" else CHI["MAX"])
        q0 = read_out(ell0) * W
        prior_leak = float(q0[chi > 0.5].sum())
        lo, hi = 1e-3, 4096.0

        def leak_at(lam):
            th = learned_theta(ell0, [lam * chi, lam * partner])
            phi_S, _ = fixed_point(ell0, lam * chi, th)
            q = read_out(phi_S) * W
            return float(q[chi > 0.5].sum())

        if leak_at(lo) < 0.5:
            thr = "< 1e-3"
        elif leak_at(hi) >= 0.5:
            thr = "> 4096"
        else:
            for _ in range(40):
                mid = math.sqrt(lo * hi)
                if leak_at(mid) >= 0.5:
                    lo = mid
                else:
                    hi = mid
            thr = f"{math.sqrt(lo * hi):.2f}"
        print(f"    {cls:<6}{prior.description:<22}{sharp:>10g}{prior_leak:>19.3f}{thr:>10}")

print()
print("=" * 118)
print("4. THE THREE ENTRIES UNDER ONE COMMON PRIOR, which isolates the entry from the prior.")
print("   Beta(1, 1), every entry at Lambda = 8, each learning theta_u* over {entry, its partner}.")
print("=" * 118)
ell0 = ell0_of(beta_prior(1.0, 1.0))
print(f"    {'entry':<26}{'theta_u*':>11}{'E[s]':>8}{'mode':>7}   {'profile 1..5':>29}{'leak':>8}")
for label, chi, partner in (
        ("MAX  (excl. zeta < theta_L)", CHI["MAX"], CHI["MIN"]),
        ("MIN  (excl. zeta <= -theta_L)", CHI["MIN"], CHI["MAX"]),
        ("REL  cut at s = 0.50", chi_cut(0.0), 1.0 - chi_cut(0.0)),
        ("REL  cut at s = 0.62", chi_cut(BOUNDS[3]), 1.0 - chi_cut(BOUNDS[3])),
        ("REL  cut at s = 0.38", chi_cut(BOUNDS[1]), 1.0 - chi_cut(BOUNDS[1]))):
    th = learned_theta(ell0, [8.0 * chi, 8.0 * partner])
    phi_S, _ = fixed_point(ell0, 8.0 * chi, th)
    prof = positions(phi_S)
    q = read_out(phi_S) * W
    print(f"    {label:<26}{th:>11.2f}{mean_s(phi_S):>8.3f}{mode_s(phi_S):>7.3f}   {fmt(prof):>29}"
          f"{float(q[chi > 0.5].sum()):>8.3f}")

print()
print("=" * 118)
print("5. THE EXPOSURE ENSEMBLE (H2 / decisions.md O8): theta_u* for the ensembles each scale carries,")
print("   at n = 4 and Lambda = 8, under the flat prior. The default n = 10 quantifier inventory is")
print("   printed by Code Cell B (no -11.2844, some -44.1766, all -65.7004, all three -28.4375).")
print("=" * 118)
ENSEMBLES = {
    "complete scale {MAX, MIN}   (endpoint + some)": [CHI["MAX"], CHI["MIN"]],
    "complete scale {MAX}  alone": [CHI["MAX"]],
    "complete scale {MIN}  alone": [CHI["MIN"]],
    "open scale {REL(+), REL(-)} (the antonym pair)": [chi_cut(0.0), 1.0 - chi_cut(0.0)],
    "open scale {REL} alone": [chi_cut(0.0)],
}
for label, fields in ENSEMBLES.items():
    th = learned_theta(ell0, [8.0 * f for f in fields])
    phi_S, _ = fixed_point(ell0, 8.0 * fields[0], th)
    print(f"    {label:<48}theta_u* = {th:>10.2f}   E[s] under the first entry {mean_s(phi_S):.3f}")
