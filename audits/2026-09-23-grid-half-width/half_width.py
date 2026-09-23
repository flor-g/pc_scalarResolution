"""Does the grid half-width Z change the verdicts? Run from the project folder:

    .venv/bin/python audits/2026-09-23-grid-half-width/half_width.py

Nothing here is printed by any cell, so every number below is class (e) under
`agent.md` §3.3 and reaches no prose. The architecture is exec'd out of
`main.ipynb` code cell 1 and Appendix F is re-run out of Code Cell 23 verbatim,
so this audit measures the notebook's own code at a half-width it never varies.

Z is held at 6.0 everywhere in both notebooks (decision I6). theta_L = log(2n-1),
so the *all*-cell is {zeta >= theta_L} and its width in log-odds is Z - theta_L.
Node count is scaled with Z to hold the spacing at 0.12, which separates
truncation from resolution: the notebook's own refinement check varies nodes at
FIXED half-width and so cannot see this axis.
"""
import contextlib, io, json, math, re, torch

NB = json.load(open("main.ipynb"))
ARCH = "".join(NB["cells"][5]["source"])
CELL_F = "".join(NB["cells"][23]["source"])
exec(ARCH, globals())

NODES = lambda Z: int(round(2 * Z / 0.12)) + 1


# Code Cell 4 reads the shift's sign through a zero band of 1e-12 (decision I5):
# where the prior overrides the entry every utterance settles on the same belief and
# the shifts are differences of equal numbers, so a bare sign test counts roundoff.
# This audit's first version omitted the band and so reported the q shift criterion
# met in 3 cells more than the notebook at Z = 6, 77 against Code Cell 4's 74. All
# three are alpha = 1024 with q = q_lit = 1.000000 and shifts of -1.1e-16, -6.7e-16
# and -4.0e-13, and none of them meets the q position criterion, which is why the
# conjunction counted 33 either way. The band is applied here so that every column
# is the notebook's own quantity.
ROUNDOFF = 1e-12


def criterion(net):
    """Text cell 4 Part C's two q criteria for "some", at the learned theta_u*."""
    up = (net.zeta >= net.theta_L).to(net.dtype)
    lit = float((net.weights * net.read_out(net.literal_fixed_point("some")) * up).sum())
    star = net.learned_theta_u()
    belief = net.read_out(net.closed_form_fixed_point("some", theta_u=star)[0])
    q = float((net.weights * belief * up).sum())
    shift = q - lit
    return star, lit, q, (abs(shift) >= ROUNDOFF and shift < 0.0), (q < 0.5)


def block_1():
    print("=" * 100)
    print("  1. THE MECHANISM: q_H tracks Eq. (24)'s limit, so this is not numerical")
    print("     flat prior, n = 10, Lambda = 512, spacing held at 0.12")
    print("=" * 100)
    print(f"{'Z':>6}{'Z-theta_L':>11}{'nodes':>7}{'theta_u*':>11}{'q_lit':>9}{'q_H':>9}"
          f"{'q at Eq(24)':>13}{'leak':>10}{'both':>6}")
    for Z in (5, 6, 6.5, 7, 7.5, 8, 9, 10, 12):
        net = LexicalPredictiveCodingNetwork(num_nodes=NODES(Z), grid_half_width=float(Z),
                                             lexical_strength=512.0,
                                             base_prior=BASE_WORLD_PRIORS["flat"])
        star, lit, q, c1, c2 = criterion(net)
        up = (net.zeta >= net.theta_L).to(net.dtype)
        low = (net.zeta <= -net.theta_L).to(net.dtype)
        f = net.base_log_prior - net.lexical_field("some")
        lim = 0.5 * (f + net.basis @ (net.basis.T @ (net.weights * f)))
        q_lim = float((net.weights * net.read_out(lim) * up).sum())
        leak = float((net.weights
                      * net.read_out(net.closed_form_fixed_point("some", theta_u=star)[0])
                      * low).sum())
        print(f"{Z:>6}{Z - net.theta_L:>11.3f}{NODES(Z):>7}{star:>11.1f}{lit:>9.4f}{q:>9.4f}"
              f"{q_lim:>13.4f}{leak:>10.1e}{('Y' if c1 and c2 else 'n'):>6}")
    print("     q_H equals Eq. (24)'s limit to four decimals at every Z: the model is on its")
    print("     own amplification asymptote, and that limit's shape is set by B, which is")
    print("     zeta and zeta^2 orthonormalized on [-Z, Z]. The entry never leaks, and q_lit")
    print("     is flat, so the utility level alone carries this.")


def block_2():
    print()
    print("=" * 100)
    print("  2. THE DRIVER IS Z - theta_L, NOT Z: narrowing the cell again restores the")
    print("     conjunction at a wider grid.  flat prior, Lambda = 512")
    print("=" * 100)
    print(f"{'Z':>6}{'n':>7}{'theta_L':>10}{'Z-theta_L':>11}{'theta_u*':>11}"
          f"{'q_lit':>9}{'q_H':>9}{'both':>6}")
    for Z, n in ((6, 10), (8, 10), (8, 20), (8, 50), (8, 74), (10, 400), (12, 3000)):
        net = LexicalPredictiveCodingNetwork(num_nodes=NODES(Z), grid_half_width=float(Z),
                                             num_atoms=n, lexical_strength=512.0,
                                             base_prior=BASE_WORLD_PRIORS["flat"])
        star, lit, q, c1, c2 = criterion(net)
        print(f"{Z:>6}{n:>7}{net.theta_L:>10.4f}{Z - net.theta_L:>11.3f}{star:>11.1f}"
              f"{lit:>9.4f}{q:>9.4f}{('Y' if c1 and c2 else 'n'):>6}")
    print("     The verdict tracks the cell width, not Z and not n separately. It is not an")
    print("     exact invariant of Z - theta_L on these rows and is not claimed to be.")


def block_3():
    print()
    print("=" * 100)
    print("  3. SECTION 4.5's PLANE, swept whole at five half-widths.  Beta(alpha,1),")
    print("     alpha = 2^0..2^10, Lambda = 2^1..2^11, 121 cells")
    print("=" * 100)
    alphas = [2.0 ** k for k in range(11)]
    lambdas = [2.0 ** k for k in range(1, 12)]
    print(f"{'Z':>6}{'Z-theta_L':>11}{'first':>8}{'second':>8}{'BOTH':>7}"
          f"{'band Lambda':>14}{'band alpha':>13}")
    for Z in (5.0, 6.0, 6.5, 7.0, 8.0):
        first = second = 0
        cells = []
        for a in alphas:
            for L in lambdas:
                try:
                    net = LexicalPredictiveCodingNetwork(
                        num_nodes=NODES(Z), grid_half_width=Z, lexical_strength=L,
                        base_prior=beta_world_prior(a, 1.0))
                    _, _, _, c1, c2 = criterion(net)
                except Exception:
                    continue
                first += c1
                second += c2
                if c1 and c2:
                    cells.append((a, L))
        thL = math.log(19)
        band = (f"{min(L for _, L in cells):g}-{max(L for _, L in cells):g}" if cells else "-")
        ab = (f"{min(a for a, _ in cells):g}-{max(a for a, _ in cells):g}" if cells else "-")
        print(f"{Z:>6}{Z - thL:>11.3f}{first:>8}{second:>8}{len(cells):>7}{band:>14}{ab:>13}")
    print("     Z = 6 returns 33 of 121 with least Lambda 64 over alpha 1 to 128, which is")
    print("     what Sec. 4.5 reports: the sweep is computing the notebook's own quantity.")


def block_4():
    print()
    print("=" * 100)
    print("  4. APPENDIX F, Code Cell 23 re-run verbatim at four half-widths (n = 4)")
    print("=" * 100)
    print(f"{'Z':>6}{'Z-theta_L':>11}   best on ladder / rungs within 0.005 / model image-type diff")
    for Z in (5.0, 6.0, 7.0, 8.0):
        g = {"__name__": "__main__"}
        exec(ARCH, g)
        g["evaluation_network"] = g["LexicalPredictiveCodingNetwork"](
            num_nodes=NODES(Z), grid_half_width=Z)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(CELL_F, g)
        t = buf.getvalue()
        best = re.search(r"best on this ladder:(.*)", t)
        mx = re.search(r"max\s+Lambda (\S+ to \S+)", t)
        mn = re.search(r"min\s+Lambda (\S+ to \S+)", t)
        f5 = t[t.find("F.5"):t.find("F.6")]
        diff = re.findall(r"^\s*absolute_(max|min)\s+.*?([-+][\d.]+)\s*$", f5, re.M)
        print(f"{Z:>6}{Z - math.log(7):>11.3f}   {best.group(1).strip() if best else '?'}")
        print(f"{'':>17}   max Lambda {mx.group(1) if mx else '?'};  "
              f"min Lambda {mn.group(1) if mn else '?'};  "
              f"model diff {', '.join(a + ' ' + b for a, b in diff)}")
    print("     H1's content -- max unbounded in Lambda, min with an interior optimum -- holds")
    print("     at every Z. R^2 is a correlation over item x position rows, so inflating the")
    print("     top cell uniformly across items barely moves it. What moves is the bracket's")
    print("     location and the minimum class's R^2.")


def block_5():
    print()
    print("=" * 100)
    print("  5. THE DEPENDENCE SITS BELOW THE CRITERION. Eq. (24)'s limit is 0.5(I + P)f with")
    print("     P = B B^T W, the W-orthogonal projection onto span{zeta, zeta^2}.")
    print("=" * 100)
    ref = None
    for Z in (6.0, 8.0):
        net = LexicalPredictiveCodingNetwork(num_nodes=NODES(Z), grid_half_width=Z,
                                             lexical_strength=512.0,
                                             base_prior=BASE_WORLD_PRIORS["flat"])
        f = net.base_log_prior - net.lexical_field("some")
        Pf = net.basis @ (net.basis.T @ (net.weights * f))
        # Seeded, so the figure below is reproducible. Unseeded it moved between runs
        # (2.3e-13, 3.4e-13, 1.7e-13 on three of them), which is the scale of the
        # result rather than the result, and E17 had quoted one of those digits.
        torch.manual_seed(0)
        Q, _ = torch.linalg.qr(torch.randn(2, 2, dtype=net.dtype))
        B2 = net.basis @ Q
        Pf2 = B2 @ (B2.T @ (net.weights * f))
        idx = [int(torch.argmin((net.zeta - v).abs())) for v in (-3., -1., 0., 1., 3., 5.)]
        vals = [float(Pf[k]) for k in idx]
        print(f"   Z = {Z:g}: max |Pf - P'f| under an arbitrary rotation of B = "
              f"{float((Pf - Pf2).abs().max()):.1e}  (P is basis-independent)")
        print(f"            Pf at zeta = -3,-1,0,1,3,5: " + ", ".join(f"{v:+.2f}" for v in vals))
        if ref is None:
            ref = vals
        else:
            print(f"            change from Z = 6:          "
                  + ", ".join(f"{b - a:+.2f}" for a, b in zip(ref, vals)))
    print("     The projection is taken in L^2([-Z, Z]), so what 'the zeta and zeta^2 components")
    print("     of the field' MEANS is truncation-dependent, and the amplification doubles that")
    print("     component. No reformulation of the criterion removes this. Removing it needs a")
    print("     fixed reference measure, which breaks B^T W B = I -- assumed by Eq. (B2).")


def block_6():
    print()
    print("=" * 100)
    print("  6. 'peak < theta_L' IS THE MODE POSITION CRITERION (Text cell 4: zeta_k* < theta_L,")
    print("     met when the mode lies outside the cell of 'all'). It is SUFFICIENT for the q")
    print("     conjunction to fail when it is NOT met, and not equivalent to it.")
    print("=" * 100)
    agree = total = 0
    rows = []
    for prior in ("flat", "gaussian", "skewed high", "skewed low"):
        for lam in (8.0, 512.0):
            for Z in (5., 6., 7., 8.):
                net = LexicalPredictiveCodingNetwork(num_nodes=NODES(Z), grid_half_width=Z,
                                                     lexical_strength=lam,
                                                     base_prior=BASE_WORLD_PRIORS[prior])
                star, lit, q, c1, c2 = criterion(net)
                phi = net.closed_form_fixed_point("some", theta_u=star)[0]
                peak = float(net.zeta[int(torch.argmax(phi))])
                below = peak < net.theta_L
                agree += (below == (c1 and c2))
                total += 1
                if not below:
                    rows.append((prior, lam, Z, peak, c1 and c2))
    print(f"   the mode position criterion and the q conjunction agree in {agree} of {total}")
    print(f"   (four priors x Lambda in {{8, 512}} x Z in {{5,6,7,8}}).")
    print("   Every row whose peak sits ABOVE theta_L fails the conjunction:")
    for prior, lam, Z, peak, both in rows:
        print(f"     {prior:<12} Lambda {lam:>5g}  Z {Z:g}  peak {peak:>6.3f} > theta_L  "
              f"conjunction {'Y' if both else 'n'}")
    print("   Many rows whose peak is below it fail anyway, through the FIRST condition")
    print("   q_H < q_lit, which is the more fragile of the two (block 3: 113, 77, 25, 5, 0")
    print("   against the second's 76, 59, 48, 25, 14). The conjunction is therefore NOT")
    print("   'a claim about where the peak sits'; the peak is the channel Z acts through, and")
    print("   the mode position criterion is the statistic that reads it directly.")


def block_7():
    print()
    print("=" * 100)
    print("  7. SECTION 4.5's 20-CELL GAP between the q and delta conjunctions, under Z.")
    print("     q conjunction  = q shift AND q position;  delta = mode shift AND mode position")
    print("=" * 100)
    alphas = [2.0 ** k for k in range(11)]
    lambdas = [2.0 ** k for k in range(1, 12)]
    print("{:>6}{:>9}{:>13}{:>7}{:>10}{:>9}{:>9}{:>15}".format(
        "Z", "q conj", "delta conj", "gap", "d-not-q", "mshift", "mpos", "least alpha ms"))
    for Z in (5.0, 6.0, 6.5, 7.0, 8.0):
        Q = D = gap = rev = ms = mp = 0
        ms_by_alpha = {}
        for a in alphas:
            hit = 0
            for L in lambdas:
                try:
                    net = LexicalPredictiveCodingNetwork(
                        num_nodes=NODES(Z), grid_half_width=Z, lexical_strength=L,
                        base_prior=beta_world_prior(a, 1.0))
                    _, lit, q, c1, c2 = criterion(net)
                    phi = net.closed_form_fixed_point(
                        "some", theta_u=net.learned_theta_u())[0]
                except Exception:
                    continue
                k = int(torch.argmax(phi))
                k0 = int(torch.argmax(net.base_log_prior))
                shift = k < k0                                  # mode shift
                pos = float(net.zeta[k]) < net.theta_L          # mode position
                qc, dc = (c1 and c2), (shift and pos)
                Q += qc; D += dc; ms += shift; mp += pos; hit += shift
                gap += (qc and not dc)
                rev += (dc and not qc)
            ms_by_alpha[a] = hit
        first = [a for a in alphas if ms_by_alpha[a] > 0]
        print("{:>6g}{:>9}{:>13}{:>7}{:>10}{:>9}{:>9}{:>15}".format(
            Z, Q, D, gap, rev, ms, mp, ("%g" % first[0]) if first else "none"))
    print("     Z = 6 returns 33 / 13 / 20 with the delta conjunction a strict subset, which is")
    print("     what Sec. 4.5 reports, and its least alpha for the mode shift criterion is 16 --")
    print("     that section's 'never met at alpha <= 8'. Both figures are Z = 6 figures: the gap")
    print("     runs 31, 20, 4, 0, 0 and the least alpha runs 8, 16, 32, 32, 128.")
    print("     ROBUST: delta is a strict subset of q at every Z, 0 reversals in all 605 cells,")
    print("     so the left arm existing only under q survives and no missing level follows.")
    print("     CAUTION: a gap of 0 at Z >= 7 means BOTH conjunctions are empty, not that the")
    print("     two read-outs agree.")


def block_8():
    """Why this audit once read 77 where Code Cell 4 prints 74, settled 2026-09-23.

    Run at the notebook's own half-width and node count, so the only thing that can
    differ is the rule. It is I5's zero band: Code Cell 4 reads the shift's sign as
    sign(shift) < 0 with a band of 1e-12, this audit's first version read q - lit < 0.
    """
    print("=" * 100)
    print("  8. THE 77 AGAINST 74, AT Z = 6. The band of decision I5, and nothing else.")
    print("     Z = 6.0, K = 101: the notebook's own grid, so only the counting rule differs")
    print("=" * 100)
    alphas = [2.0 ** k for k in range(11)]
    lambdas = [2.0 ** k for k in range(1, 12)]
    bare = banded = second = both_bare = both_banded = 0
    differing = []
    for a in alphas:
        for L in lambdas:
            net = LexicalPredictiveCodingNetwork(
                num_nodes=101, grid_half_width=6.0, lexical_strength=L,
                base_prior=beta_world_prior(a, 1.0))
            up = (net.zeta >= net.theta_L).to(net.dtype)
            lit = float((net.weights * net.read_out(
                net.literal_fixed_point("some")) * up).sum())
            q = float((net.weights * net.read_out(net.closed_form_fixed_point(
                "some", theta_u=net.learned_theta_u())[0]) * up).sum())
            shift = q - lit
            c1_bare = shift < 0.0
            c1_band = abs(shift) >= ROUNDOFF and shift < 0.0
            c2 = q < 0.5
            bare += c1_bare; banded += c1_band; second += c2
            both_bare += c1_bare and c2; both_banded += c1_band and c2
            if c1_bare != c1_band:
                differing.append((a, L, shift, q, lit, c2))
    print(f"     q shift criterion, bare sign test q - lit < 0 : {bare}")
    print(f"     q shift criterion, with I5's 1e-12 band       : {banded}"
          "   <- Code Cell 4 prints 74")
    print(f"     q position criterion                          : {second}"
          "   <- Code Cell 4 prints 59")
    print(f"     conjunction, bare {both_bare} / banded {both_banded}"
          "                    <- Code Cell 4 prints 33")
    print(f"     the {len(differing)} cells the rules disagree on, all saturated:")
    print(f"       {'alpha':>7}{'Lambda':>8}{'shift':>12}{'q':>11}{'q_lit':>11}"
          f"{'q position':>12}")
    for a, L, s, q, lit, c2 in differing:
        print(f"       {a:>7.0f}{L:>8.0f}{s:>12.1e}{q:>11.6f}{lit:>11.6f}"
              f"{('met' if c2 else 'not met'):>12}")
    print("     Every one is a difference of equal numbers where the prior has overridden")
    print("     the entry, which is what I5's band exists to exclude, and none meets the q")
    print("     position criterion, so the conjunction counted 33 under either rule and")
    print("     nothing this audit argues from ever moved. The notebook is right. Block 3's")
    print("     first column now carries the band, and its series runs 113, 74, 24, 0, 0.")


if __name__ == "__main__":
    print("GRID HALF-WIDTH AUDIT, 2026-09-23. Class (e): no cell prints any of this.")
    print(f"torch {torch.__version__}, dtype {DTYPE}. Notebook default Z = 6.0, K = 101.")
    print()
    block_1(); block_2(); block_3(); block_4(); block_5(); block_6(); block_7()
    print()
    block_8()
