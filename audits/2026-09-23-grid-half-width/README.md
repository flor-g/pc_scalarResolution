# The grid half-width, and what the verdicts actually depend on

Run 2026-09-23. `half_width.py` / `output.txt`. Raised by another agent's report that widening the
logit range from ±6 to ±8 "overturns the results". **The report is substantially right and its
framing is wrong**, and the difference matters for what to do about it.

Everything here is **class (e)**: no cell prints any of it, so none of it may be quoted in prose
(`agent.md` §3.3). The architecture is `exec`'d out of code cell 1 and Appendix F is re-run out of
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
nothing piles at the cut. **B is orthonormalized on the grid, so the settled field's own shape moves
with Z.** Fitting φ_S\* to a quadratic, its peak runs 1.70, 2.39, 2.78, 3.17, 3.61, 4.24 over
Z = 5, 6, 6.5, 7, 7.5, 8 and **crosses θ_L = 2.944 between Z = 6.5 and 7 — exactly where q_H passes
½**. Both q criteria and §3.6's mode criterion therefore fail together. §4.4 and §4.5 read an
**absolute position** on that field; Appendix F scores **R² over five-cell profiles across items**,
which reads **agreement of shape** and is invariant to it.

The clinching evidence is that **Appendix F runs at n = 4, so Z − θ_L = 4.05 — already inside the
region where the main evaluation's conjunction has collapsed to zero cells — and Appendix F is fine
there.** Same grid, same truncation, different statistic, opposite robustness.

## What this leaves

Not "the results are wrong". §4.4 and §4.5 carry an **unstated condition on Z − θ_L** that decision
**I6** was supposed to discharge and never did: I6 was an empty entry, with no decision text, no
reason and no evidence, while `agent.md` §3.3 makes the half-width a class (d) constant requiring
"evidence that the results it supports do not depend on its exact value".

§4.2 already carries half of the right guard — it says the verdicts are relative to *n* and that the
q shift criterion changes status somewhere on a sweep of n. Since θ_L = log(2n−1), that guard and
this finding are one fact seen from two ends, and §4.2 now states it as the width of the cell.
Reconsidering the criterion's *form* — an absolute mass threshold over a truncated cell is the
fragile object — is a B-series architectural question and is **not** taken here.
