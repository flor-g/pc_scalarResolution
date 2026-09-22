# Side quests: the mirrored inventory, and the number of atoms

Working record for two questions the user raised on 2026-09-15, on the pattern of
`theta_u_learned_reach.md`. Both are exploratory: the user asked for a sense of the answer, not a
settled one, so nothing here has entered a notebook. **Every number below comes from a scratch
script and is class (e) under `agent.md` §3.3 until a cell prints it (C6).**

## 0. Instructions (the user's, verbatim, 2026-09-15)

> Now there are two side quests we want to ask:
>
> 1. we have that the O corner {1} is non-representational. Another question we want to follow: is
>    {1} as representational as {0}? That is, if we have an inventory of three {no, notall, all},
>    will it behave exactly like a mirrored version of the current {no, some, all}?
> 2. if our predicates have three atoms instead of ten, with corresponding K and theta_L, would some
>    essential results be different? What is there is exactly two atom, will the model become
>    degenerate?
>
> ---
>
> We don't necessarily have to answer these questions in full at the current phase since we have
> limited time, but we want to have a sense about what the answer might be. Record these two
> questions and let's start by looking at the first question.

## 1. Decisions these rest on

- **A2** entries fixed by exclusion; **A5** μ_u ≠ 0, implementation takes μ_u = 1 ∈ ℝ^m;
  **A7** m = 2; **A15** the default ℓ₀ is N(0, 1) in ζ; **I6** grid K = 101, half-width 6.
- **O1** (open since 2026-09-07) what fixes δ, and so θ_L. Side quest 2 bears on it directly: a
  dated finding is appended there.
- Appendix C §§3-5 (the count is thresholds, Eq. C2), §4 (the *not all* rectangle), §8 (Eq. 24's
  limit field).
- Appendix A Eq. (A1), the authority for how E_y maps to the grid.

## 2. Tasks

Record format: `[x] Tn (date): what changed; acceptance result; commit`.

- [x] T0 (2026-09-15): checkpoint 350e8e5. The tree carries one uncommitted line in `main.ipynb`
  cell 18 (Appendix C §4's O corner aside) which is **the user's, not folded in** (`agent.md` §4.2
  step 4).
- [x] T1 (2026-09-15): `audits/2026-09-15-side-quests/reflection_probe.py`. The substrate, basis
  parity and the four indicators under ζ → −ζ.
- [x] T2 (2026-09-15): `mirror_equivariance.py`. The equivariance test proper. Acceptance: the
  helper reproduces `closed_form_fixed_point` to 0.00e+00 and `learned_theta_u` to 6 decimals (F0).
- [x] T3 (2026-09-15): `mirror_under_priors.py`. The reflection carried onto ℓ₀.
- [x] T4 (2026-09-15): `granularity_probe.py`. θ_L, rank, θ_u\*, the threshold scan and the
  separation margin over n.
- [x] T5 (2026-09-15): `granularity_criteria.py`. The reported criteria as a function of n, using
  the notebook's own methods throughout.
- [x] T6 (2026-09-15): this record; `decisions.md` O9, O10, and a dated finding under O1.

Output of all five scripts: `audits/2026-09-15-side-quests/output.txt`.

## 3. Findings

- **F0 (a bug in the first pass, and what caught it).** The first `mirror_equivariance.py` wrote
  `torch.eye(m) + sigma_u * theta**2 / S`, which adds the scalar to *every* entry, where
  `closed_form_fixed_point` writes `torch.eye(m) + sigma_u * theta**2 * gram / S`. The off-diagonal
  entries do not commute with P below, so the mirror appeared broken by 3.7e+03 while θ_u\* matched
  to 4e-14. Fixed by carrying the Gram matrix, and a validation against
  `closed_form_fixed_point` (now 0.00e+00) was added so the same class of error cannot recur.
  Lesson for later probes: **validate any reimplementation against the cell it reimplements before
  reading anything off it.**

### Side quest 1

- **F1 (the architecture is exactly mirror-symmetric).** Write R for ζ → −ζ on the grid and
  P = diag(−1, +1) on the (tilt, width) coordinates. Then Rb₁ = −b₁ and Rb₂ = +b₂ (to 4e-17), so
  RB = BP, and since W is symmetric under R, BᵀWR = P BᵀW. The reflection pairs the inventories
  utterance by utterance, Rχ_no = χ_all and Rχ_some = χ_not all, **exactly** (0.00e+00). It follows
  that the model built on (inventory, ℓ₀, μ_u) and the model built on
  (mirrored inventory, Rℓ₀, Pμ_u) are reflections: same θ_u\*, and φ_S\* and φ_u\* related by R and
  P. Measured worst discrepancy **7.11e-15** under N(0,1), **7.11e-15** under Beta(3,1) ↔ Beta(1,3),
  **1.14e-13** under Beta(64,1) ↔ Beta(1,64).
- **F2 (so the answer to "is {1} as representational as {0}" is yes, exactly).** Nothing in the
  representation prefers {0}. Appendix C §4's rectangle is the finite statement of it; F1 is the
  statement for the whole model.
- **F3 (but the model is not mirror-symmetric, and μ_u is the only reason).** Of the ingredients,
  the grid, W, b₁, b₂ and the default ℓ₀ = N(0,1) are all R-invariant or of definite parity.
  **μ_u = 1 = (1, 1) is not**: Pμ_u = (−1, +1) ≠ μ_u. So running the mirrored inventory at the
  stipulated μ_u is *not* the mirror. θ_u\* is −28.4375 on {no, some, all} against −19.7219 on
  {no, not all, all}; under Beta(3,1) ↔ Beta(1,3) it **changes sign**, +55.0081 against −17.0332.
  A5 records μ_u = 1 as a stipulation with no target to be derived from, so this asymmetry is
  stipulated rather than motivated.
- **F4 (the fields barely notice, and Appendix C §8 says why).** At the stipulated μ_u the settled
  fields differ by only 4.98e-02 (Gaussian) and 5.67e-02 (Beta(3,1)), despite θ_u\* differing by
  8.7 and by a sign. Eq. (24)'s limit k → c/2 is independent of θ_u, sign included, and every
  configuration here is deep in that regime. So the mirror breaks in the **learned parameter**, and
  the settled field is nearly insensitive to the break.
- **F5 (the criteria read the same on each side).** Reading each inventory's scalar member against
  its own region — *some* against the all-region, *not all* against the no-region — gives shift
  +0.0008 against +0.0009 and position 0.0025 against 0.0025, so both give the same verdict on both
  q criteria. (The q shift criterion is not met under the default Gaussian; that is the prior, not
  the mirror, and matches what Part C already reports.)

### Side quest 2

- **F6 (n enters in exactly one place).** `theta_L = log(2 * num_atoms - 1)` is the only use of n in
  code cell 1, and `num_atoms` is then recovered *from* θ_L, so θ_L is the real quantity and n its
  denotation (Eq. A5). **K does not track n**: Text cell 3 §1 and I6 make K an accuracy parameter
  for the quadrature, not a state space, so "three atoms with corresponding K" overstates what has
  to move. θ_L < grid half-width caps n at 201.
- **F7 (nothing structural moves).** At n ∈ {2, 3, 4, 10, 50, 100} the three χ_y have rank 3 and
  rank 2 modulo the constant, so by Eq. (C2) there are still two thresholds and **m = 2 stays
  exactly right**. θ_u\* moves smoothly and keeps its sign: −32.5731 at n = 2 to −19.1884 at
  n = 100.
- **F7 qualified, 2026-09-22 (T14).** The smoothness clause is a property of **N(0,1)**, not of the
  model. Sweeping all four `BASE_WORLD_PRIORS`, θ_u\* under the **flat** prior at Λ = 8 runs
  −1082.011 at n = 2, +2510.809 at n = 3, +5950.626 at n = 10, −3322.896 at n = 11: it is not
  monotone and **not bounded**. Eq. (B2)'s two roots have the constant product −S/σ_u, so θ_u\*
  diverges exactly where ⟨μ_u, Σ_y c_y⟩ vanishes, and that coupling changes sign twice along the
  ladder. This is **Appendix B's degenerate ray, reached by varying n alone**, and
  `theta_u_stationary_points` guards only exact zero, so nothing flagged it. The rank and m = 2
  results of F7 are untouched. Code Cell A now prints the coupling beside θ_u\*.
- **F8 (n = 2 is not degenerate; n = 1 is).** At n = 2, θ_L = 1.0986, the cell of s = 0 is
  s ≤ 0.25 and the cell of s = 1 is s ≥ 0.75, χ_some ≠ χ_all, and 19 grid nodes lie strictly
  between the thresholds. The two thresholds stay distinct, so the span is unchanged. Degeneracy is
  at n = 1, where θ_L = 0 and the entries for *some* and *all* coincide; the constructor already
  rejects it.
- **F9 (but the reported criteria do move with n, and they cross).** This is the substantive answer
  to "would some essential results be different", and it is yes. For *some*:
  - under N(0,1), the **q shift** criterion is not met at n = 2…20 and **is met at n = 50**;
  - under Beta(3,1), the **q position** and **mode position** criteria are not met at n = 2, 3 and
    **are met at n ≥ 4**, and the **q shift** criterion is not met at n ≤ 10 and **met at n ≥ 20**.

  So n = 10 is not a neutral choice of units: it sits on one side of two crossings under a prior
  the notebook runs. This makes **O1 consequential** rather than cosmetic.
- **F9 extended and qualified, 2026-09-22 (T14, Code Cell A).** The sweep now covers all four
  `BASE_WORLD_PRIORS` at Λ = 8 **and** Λ = 512 — 80 rows — and every row prints all four criteria.
  F9's own readings all survive. Three things it did not say, and the prose must:
  1. **Magnitude.** F9 wrote "crosses at n = 50" under N(0,1) without the size of what crosses. The
     q shift there falls **+1.017e-01** at n = 2 → **+2.966e-06** at n = 20 → **−7.593e-07** at
     n = 50: the change of status is the **sign flip of a quantity decayed five orders of
     magnitude**, not a substantive change in what the model reports. Contrast *skewed high* at
     Λ = 512, where the same criterion changes status at **−9.546e-02**. These are not findings of
     equal weight and F9 presented them as one kind.
  2. **A ladder brackets, it does not locate.** "Crosses at n = 50" means *not met at 20, met at
     50*; the change lies somewhere in (20, 50]. No rung measures where it happens.
  3. **The crossings do move with Λ**, which §4 listed as unchecked. The q shift criterion changes
     at n = 50 under three priors at Λ = 8 and by n = 15 or n = 10 under all four at Λ = 512; the
     q position criterion, met at every rung under N(0,1) at Λ = 8, fails at n ≤ 5 at Λ = 512.
     **Granularity and lexical strength are not separable** in what the evaluation reports.

  Two further facts the wider sweep produced. The **mode shift** criterion is met in **one row of
  the eighty** (*skewed low*, Λ = 8, n = 201): the peak of φ_S\* otherwise sits above ℓ_0's peak
  whatever the q criteria say. And **q position and mode position agree in 79 of 80 rows**,
  disagreeing only at *flat*, Λ = 8, n = 2.
- **A measurement limit found at T14.** χ_y is a threshold on the grid, so two n whose
  θ_L = log(2n − 1) fall between the same two grid nodes give the **same network but for θ_L**:
  n = 12 and n = 13 return byte-identical rows. n is resolved only as finely as the grid resolves
  θ_L. No rung of the published ladder collides, so nothing printed is affected.
- **F10 (separation is best near n = 15).** The minimum κ separation over the three utterances rises
  from 0.70917 at n = 2 to a maximum **1.49027 at n = 15**, and falls to 0.05999 at n = 201. The
  implementation's n = 10 gives 1.44196, near the peak.
- **F11 (a latent divergence between code and Eq. (A1), noticed, not changed).** Eq. (A1) writes
  E_some ↦ {ζ ≤ −θ_L}, non-strict. `exclusion_indicator` computes `margin = -(zeta + theta_L)` and
  excludes where `margin > 0`, i.e. ζ < −θ_L, **strict**; its own docstring states the non-strict
  form, so the code disagrees with both the docstring and Eq. (A1). At a node lying exactly on
  −θ_L, χ_no and χ_some would both be 0 and χ_no + χ_some = 1 would fail there, which Appendix C §2
  and Eq. (C1) rely on. Prose defines and code implements (`agent.md` §3), so the code is the side
  that is wrong. **Left for the user** (§5.4): it is a code cell, and outside the scope of these two
  questions.
- **F11 corrected, 2026-09-16.** F11 as first written said the divergence was "invisible today: no
  integer n in [2, 201] puts a grid node on a threshold". **That was wrong**, and the error was in
  the scan, not the arithmetic: it swept only θ_L = log(2n − 1) for integer n and the K ladder, and
  never covered the *explicit* θ_L values the notebooks pass. Code Cell 4's
  `override_threshold(boundaries=(1.0, 2.0, 3.0))` puts **θ_L = 3.0 exactly on node 25** of the
  K = 101 grid. The divergence was therefore live in a table the notebook prints, and fixing it
  (decision I13) moved that row's θ_u\* from 14946.06 to 14937.23 and Text cell 6's quoted range
  from "13378 to 14946" to "13378 to 14937". Lesson, beside F0: **a static scan for literals is not
  a reachability test.** The authoritative check is a full printed-output diff of both notebooks
  before and after, which is exhaustive over everything they actually compute.

## 4. What is not answered

- Side quest 1 measured θ_u\*, φ_S\*, φ_u\* and the two q criteria. It has **not** run the mirrored
  inventory through Part D's four priors, the Λ×α plane, or the mode criteria, and has not asked
  what a principled μ_u for a mirrored scale would be.
- ~~Side quest 2 measured n at the default Λ = 8 under two priors. It has **not** swept n against
  Λ, nor checked whether the crossings of F9 move with Λ, nor looked at n's effect in Text cell 4b's
  Λ = 512 configuration.~~ **Closed 2026-09-22 by T14**: Code Cell A's `granularity_report` sweeps
  n against all four base priors at Λ = 8 and Λ = 512, printing all four criteria per row. The
  crossings **do** move with Λ (F9 extended, point 3).
- Side quest 1 still has no prose site, because it has not entered a notebook. **Side quest 2 now
  has one**: Appendix A's markdown cell reports it in the notebook, and §4.2 of
  `thesis_outline/sections_3-6.md` carries it in the paper with a clause in §5.2 (S-8, T15).
