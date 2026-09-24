# The grid half-width, and what the verdicts actually depend on

Run 2026-09-23. `half_width.py` / `output.txt`. Raised by another agent's report that widening the
logit range from ±6 to ±8 "overturns the results". **The report is substantially right and its
framing is wrong**, and the difference matters for what to do about it.

Everything here is **class (e)**: no cell prints any of it, so none of it may be quoted in prose
(`agent/agent.md` §3.3). The architecture is `exec`'d out of code cell 1 and Appendix F is re-run out of
Code Cell 23 verbatim, so this measures the notebook's own code at a half-width it never varies.
Node count is scaled with Z to hold the spacing at 0.12, which separates truncation from
resolution — the notebook's own refinement check varies nodes **at fixed half-width** and says so in
its own print label, so it cannot see this axis.

## The claim, restated correctly

It is not about 6 against 8. The controlling quantity is **Z − θ_L, the width of the *all*-cell
in log-odds**. θ_L = log(2n−1), so n moves one end of that cell and Z moves the other; the verdicts
track the width, and neither Z nor n predicts them alone. At Z = 8 the conjunction returns as soon
as the cell is narrowed again (n = 50, 74; and at Z = 10, 12 with n = 400, 3000).

Sweeping Z at n = 10, Λ = 512, flat prior, q_H runs **0.000, 0.036, 0.302, 0.669, 0.927, 0.999**
over Z = 5, 6, 6.5, 7, 7.5, 8 — a smooth sigmoid centred near Z ≈ 7, with **the published Z = 6 on
its lower shoulder**, about half a unit from the turn.

## It is not numerical, and here is the mechanism

- **q_H equals Eq. (24)'s limit to four decimals at every Z.** At Λ = 512 the model sits on its own
  amplification asymptote, so this is a property of ½(I + BBᵀW)(ℓ₀ − φ_L), not of the solver, the
  grid resolution, or θ_u\*'s magnitude.
- **The entry never leaks** (~1e-170 into the region *some* excludes), so no mask has failed.
- **q_lit is flat at ≈ 0.05 across every Z**, so the literal listener is untouched and the utility
  level alone carries this.
- The channel is that **B is ζ and ζ² orthonormalized under the quadrature inner product on
  [−Z, Z]**, so the basis is rebuilt by the grid and the tilt direction reaches further on a wider
  one. Eq. (24) then doubles the field's component in span B.

## What is affected, and what is not

**§4.5's plane collapses.** Both conditions together, of 121 cells: **68, 33, 5, 0, 0** at
Z = 5, 6, 6.5, 7, 8. Both floors move, not just the conjunction — the first condition runs
113 → 0 and the second 76 → 14, so §4.5's *opposing floors* story is itself Z-conditional.
**Z = 6 returns 33 of 121 with least Λ = 64 over α = 1 to 128, which is exactly what §4.5
reports**, so the sweep is computing the notebook's own quantity.

**Appendix F is robust in its claims and conditional in its numbers.** H1's content — the maximum
class unbounded in Λ (6 to the ladder's top), the minimum class with an interior optimum — holds at
Z = 5, 6, 7 and 8 alike, and that ordering is what §5.2 and §6 item 4 rest on. The maximum class's
R² is 0.993 at Λ = 8 at every Z, and the model's image-type difference moves only +0.03 → +0.04 and
−0.14 → −0.20. What moves is the **minimum class's bracket (64–96, 32–48, 24, 24) and its R²
(0.418, 0.434, 0.448, 0.455)**, and pooled R² (0.827 → 0.774). §5.2's "bracketed between 32 and 48"
is therefore a Z-conditional number; its H1 sentence is not.

## Why the two differ, which is the usable part

**The criterion's form decides its truncation sensitivity** — but the first reading of *why* was
wrong and is corrected here. It is **not** that a wider interval holds more mass: the settled field
stays normalizable (negative ζ² coefficient at every Z measured) and the top node's share is ~0, so
nothing piles at the cut. **B is orthonormalized on the grid, so φ_S\*'s own shape moves
with Z.** Fitting φ_S\* to a quadratic, its peak runs 1.70, 2.39, 2.78, 3.17, 3.61, 4.24 over
Z = 5, 6, 6.5, 7, 7.5, 8 and **crosses θ_L = 2.944 between Z = 6.5 and 7 — exactly where q_H passes
½**. That peak is the peak of φ_S\*, which Eq. (12) makes q's mode too, so neither read-out
escapes it. §4.4 and §4.5 read a mass above a fixed cut; Appendix F scores **R² over
five-cell profiles across items**, which reads **agreement of shape** and is invariant to it.

**The dependence sits below the criterion.** Eq. (24)'s limit is ½(I + P)f with **P = BBᵀW, the
W-orthogonal projection onto span{ζ, ζ²}**. P is basis-independent — rotating B by an arbitrary
orthogonal Q moves Pf by 2.3e-13 — and **P itself moves with Z**, because the projection is taken in
L²([−Z, Z]): projecting the same field, Pf at ζ = −3, −1, 0, 1, 3, 5 shifts by +53.5, −9.8, −20.5,
−17.8, +7.8 and **+80.8** between Z = 6 and Z = 8. What "the ζ and ζ² components of the field" means
is truncation-dependent, and the amplification doubles that component. **No reformulation of the
criterion removes this**; it changes only whether a statistic is sensitive to it. Removing it needs
the projection taken under a fixed reference measure rather than the quadrature one, which breaks
BᵀWB = I, assumed by Eq. (B2)'s closed form — the orthonormality that makes the closed forms exact
is what ties the utility basis to the truncation.

**Sufficient, not equivalent.** "peak < θ_L" is **Text cell 4's mode position criterion verbatim**,
ζ_{k\*} < θ_L, met when the mode lies outside the cell of *all* — so the half-width moves that
criterion's own left-hand side. Over 32 configurations (four priors × Λ ∈ {8, 512} × Z ∈ {5,6,7,8}),
it and the q conjunction agree in only **13**. A peak above θ_L always fails the
conjunction (6 of 6), but many rows with the peak below it fail anyway, through the first condition
q_H < q_lit — the more fragile of the two, collapsing 113 → 74 → 24 → 0 → 0 against the second's
76 → 59 → 48 → 25 → 14. **The conjunction is not "a claim about where the peak sits."** And the
difference is not marginal: by Z = 7 the shift criterion is met in **no cell of the plane** while
the position criterion still holds in 25, so **the position criterion is the more robust of the two
under the half-width**, not the less.

The clinching evidence is that **Appendix F runs at n = 4, so Z − θ_L = 4.05 — already inside the
region where the main evaluation's conjunction has collapsed to zero cells — and Appendix F is fine
there.** Same grid, same truncation, different statistic, opposite robustness.

## The 77 against 74, settled 2026-09-23 (block 8)

**The first version of this audit read the q shift criterion met in 77 cells at Z = 6 where Code
Cell 4 prints 74.** Everything else agreed exactly: 59, 33, 67, 13, 20. The cause is the rule, not
the grid. Code Cell 4 reads the shift's sign through **I5's zero band of 1e-12**, this audit's
`criterion()` read a bare `q - lit < 0`. The three cells are all α = 1024 with q = q_lit = 1.000000
and shifts of −1.1e−16, −6.7e−16 and −4.0e−13 — differences of equal numbers where the prior has
overridden the entry, which is exactly what I5's band exists to exclude. **None of the three meets
the q position criterion**, so the conjunction counted 33 under either rule and nothing this audit
argues from ever moved.

**The notebook is right, the audit was wrong, and the error was confined to one column.**
`criterion()` now applies the band, so every column here is the notebook's own quantity. Block 3's
first column changes from 113, 77, 25, 5, 0 to **113, 74, 24, 0, 0**. Block 7 is unchanged.

**Also fixed: the rotation was unseeded.** Block 6's `max |Pf - P'f|` came from an unseeded random
Q and moved between runs (2.3e-13, 3.4e-13, 1.7e-13 on three of them), which is the scale of the
result and not the result. It is seeded now, and two consecutive runs of the whole script are
byte-identical. E17 had quoted one of the unseeded digits, 3.4e-13; the seeded figure is 2.3e-13.

## §4.5's gap between the two read-outs

Block 7 sweeps the plane on both conjunctions. **Z = 6 returns 33 (q), 13 (delta), gap 20, delta a
strict subset**, and its least α at which the mode shift criterion is met anywhere is **16** — which
are §4.5's own figures and its "never met at α ≤ 8". Both are Z = 6 figures: the gap runs
**31, 20, 4, 0, 0** and the least α runs **8, 16, 32, 32, 128** over Z = 5, 6, 6.5, 7, 8.

**What survives is what §4.5 argues from.** The delta conjunction is a **strict subset** of the q
conjunction at every half-width, with **0 reversals in all 605 cells**, so the two read-outs part
only in q's favour, the left arm exists only under q, and R14's instruction to derive no evidence
for a missing level from the V is untouched. **Caution:** the gap reaching 0 at Z ≥ 7 means *both*
conjunctions are empty there, not that the read-outs have come to agree.

## What this leaves

Not "the results are wrong". §4.4 and §4.5 carry an **unstated condition on Z − θ_L** that decision
**I6** was supposed to discharge and never did: I6 was an empty entry, with no decision text, no
reason and no evidence, while `agent/agent.md` §3.3 makes the half-width a class (d) constant requiring
"evidence that the results it supports do not depend on its exact value".

§4.2 already carries half of the right guard — it says the verdicts are relative to *n* and that the
q shift criterion changes status somewhere on a sweep of n. Since θ_L = log(2n−1), that guard and
this finding are one fact seen from two ends, and §4.2 now states it as the width of the cell.
**Settled by the user, 2026-09-23.** The criterion's form does **not** change: the dependence sits
below it, in a projection taken under the grid's own measure, so reformulating relocates it rather
than removing it. And $Z$ needs **no** printed evidence — no cell sweeps the half-width, this audit
stays class (e), and §4.2's guard stays qualitative by decision rather than by default.
