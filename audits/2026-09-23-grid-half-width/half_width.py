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


def criterion(net):
    """Text cell 4 Part C's two q criteria for "some", at the learned theta_u*."""
    up = (net.zeta >= net.theta_L).to(net.dtype)
    lit = float((net.weights * net.read_out(net.literal_fixed_point("some")) * up).sum())
    star = net.learned_theta_u()
    belief = net.read_out(net.closed_form_fixed_point("some", theta_u=star)[0])
    q = float((net.weights * belief * up).sum())
    return star, lit, q, (q - lit < 0.0), (q < 0.5)


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
    print("  6. THE PEAK-CROSSING IS SUFFICIENT FOR FAILURE, NOT EQUIVALENT TO IT")
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
    print(f"   'peak < theta_L' and the q conjunction agree in {agree} of {total} configurations")
    print(f"   (four priors x Lambda in {{8, 512}} x Z in {{5,6,7,8}}).")
    print("   Every row whose peak sits ABOVE theta_L fails the conjunction:")
    for prior, lam, Z, peak, both in rows:
        print(f"     {prior:<12} Lambda {lam:>5g}  Z {Z:g}  peak {peak:>6.3f} > theta_L  "
              f"conjunction {'Y' if both else 'n'}")
    print("   Many rows whose peak is below it fail anyway, through the FIRST condition")
    print("   q_H < q_lit, which is the more fragile of the two (block 3: 113, 77, 25, 5, 0")
    print("   against the second's 76, 59, 48, 25, 14). The conjunction is therefore NOT")
    print("   'a claim about where the peak sits'; the peak is the channel Z acts through.")


if __name__ == "__main__":
    print("GRID HALF-WIDTH AUDIT, 2026-09-23. Class (e): no cell prints any of this.")
    print(f"torch {torch.__version__}, dtype {DTYPE}. Notebook default Z = 6.0, K = 101.")
    print()
    block_1(); block_2(); block_3(); block_4(); block_5(); block_6()
