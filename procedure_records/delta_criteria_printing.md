# Printing the delta read-out's criteria, and why its mode moves

Working record, on the pattern of `theta_u_learned_reach.md`. **Status 2026-09-13: every task is
OPEN.** Nothing in the notebooks has been changed. The findings below come from the audit scripts in
`audits/2026-09-13-delta-criteria/`, and under C6 no prose may quote them until a cell prints them.

## 0. Instructions (the user's, verbatim, 2026-09-13)

> The cost sense retain the "realizability" name as is; no change needed. Now let's work on Q2.
> Here are my thoughts:
>
> 1. the delta read-out still comes with two criteria: a. whether mode(phi_s*) - mode(ell_0) is
> negative; this is shift_some. b. whether mode(phi_s*) falls outside the cell of [[all]]. Just be
> careful that even though these two criteria are meant to mirror the two criteria as already
> defined, their satisfaction may not be equivalent.
> 2. The V-shape is instereting and it definitely needs to be discussed,
> 3. I am not sure what you mean with the unstated premise and what level is it a motivation of.

> good. Your solution to Q2 is approved. No evidence for a missing level needs to be derived from
> V. Create open tasks for code cell edits. Regarding Q6, I agree with your suggestion; nevertheless,
> we might want to poke why a similar phenomenon also emerged for delta-readout.

> (2026-09-14) your decisions are confirmed. Just remember that we do not take a position that both
> conditions need to be met to count as scalar strengthening. We are just reporting them so that the
> reader can make their own judgment. (Any positions we take would be left to the paper, not the
> notebook. ) Execute next step.

Under B10 every line these tasks print reports a condition or criterion as a measurement ("holds",
"does not hold"), never as a verdict on strengthening.

## 1. Decisions this rests on

- `decisions.md` **B8** (user): the delta read-out's criteria, under *some*: (a) mode(φ_S\*) −
  mode(ℓ₀) < 0; (b) mode(φ_S\*) outside the cell of *all*. Not assumed equivalent to B2.
- `decisions.md` **B7** (the delta read-out table), **A16** (the delta is the construction's
  posterior), **C6** (every quoted number printed by a cell), **I5** (1e-12 zero band).
- `thesis_outline/revisions.md` **R14** (the V is reported under both read-outs in §4.5; no evidence
  for a missing level is derived from it) and **R15** (the Cremers parallel stays with q; why the
  delta read-out shows a similar movement is to be investigated).

## 2. Tasks, in order (all open)

Record format when closing: `[x] Tn (date): what changed; acceptance result; commit`.

- [x] **T0 (2026-09-14). Checkpoint.** HEAD 7854b8f, clean tree. T1 prints in Code Cell 2, and so in
  Code Cell 2b, which calls the same function (S-5 of `evaluation_partD_atStrongLambda.md`).
- [x] **T1 (2026-09-14). Code Cell 2, `delta_readout_report`: print the mode shift and mode position
  criteria (C7 names; (a) and (b) below).** Closed: one block at the end of `delta_readout_report`, so
  it prints in Code Cell 2 (Part D's four rows at Λ = 8) and Code Cell 2b (five rows at θ_u\* and three
  realizable rows at Λ = 512). Per row: modes of ℓ₀, ℓ₀ − φ_L and φ_S\* in s, the signed mode shift, the
  mode shift / mode position criteria and both, the q shift / q position criteria and both, the gap
  between the two largest nodes; then counts and pairwise agreement. Wording under B10/C7. Modes are
  printed in s only, not also in ζ (agent, pending user confirmation).
  **Superseded 2026-09-14 by the user:** "Print the mode shift in grid steps alongside s, then add a
  concise guide in code comment or text explaining to the reader that they can recover zeta by
  multiplying by 0.12." Added: a `steps` column (k − k0, signed) beside the shift in s; a printed
  legend line giving the grid spacing, read from the grid, and saying that steps times the spacing is
  the shift in ζ; a two-line code comment on why (s compresses toward the ends of the scale).
  Hand check before execution, from the printed s values: +3 for the Gaussian at Λ = 8, −11 for the
  delta-like row.
  Executed 2026-09-14: the column reads +3, +6, +3, +5 at Λ = 8 and +19, +20, +27, +11, −11 at Λ = 512
  (realizable rows equal their θ_u\* rows), matching the hand check; printed spacing 0.12. Only the legend,
  the column and E3's line counts changed. main 0 errors, 8 figures, 14/14, 249 s; appendix_E 0 errors,
  5 figures, E2 18/18, E3 PASS (203 and 234 lines identical).
  Acceptance: Λ = 8 rows equal `output.txt` §PART D ROWS in every mode and yes/no; the delta-like row
  equals it too; the Λ = 512 rows equal `evaluation_partD_atStrongLambda.md` F7. Smallest top-2 gap
  3.4e−3 (no ties). Code Cell 2 at Λ = 8: the pairs agree in 4 of 4 rows. Code Cell 2b at Λ = 512: mode
  and q shift criteria agree in 4 of 8 rows (flat and Beta(3,1), each at θ_u\* and realizable, have
  the q shift criterion met and the mode shift criterion not), position criteria in 8 of 8.
  Every previously printed line unchanged apart from the C7 renames. Originally:
  - For each Part D row under *some*, at θ_u\* and at the realizable θ_u row B7 already prints,
    print:
    - mode(ℓ₀), mode(ℓ₀ − φ_L) and mode(φ_S\*), in ζ and in s;
    - the signed mode shift, and whether (a) is met;
    - whether the mode is outside the cell, i.e. whether (b) is met;
    - both criteria together;
    - q's two conditions beside them, so the rows can be compared.
  - The mode is the grid node where the field is largest, as B7 defines it. Say that ties are
    resolved to the first index, and print the smallest gap between the two largest nodes.
  - Acceptance: the values equal `audits/2026-09-13-delta-criteria/output.txt` §PART D ROWS, and every
    line the cell printed before is unchanged.
- [ ] **T2. Code Cell 4: record and summarize the delta criteria on the plane.**
  - `lambda_alpha_sweep` stores mode(φ_S\*), mode(ℓ₀) and mode(ℓ₀ − φ_L) under *some* per cell.
  - `plane_summary` prints, for the delta read-out:
    - the counts for (a), (b) and both;
    - the agreement of (a) with q's first condition, of (b) with the second, and of the two
      conjunctions;
    - the cells where the read-outs disagree, with θ\*, q_H, shift, tempering, utility and the two
      modes;
    - the floors for (a), (b) and both;
    - **the V table under both read-outs**;
    - the unmoved-mode count, and whether mode(ℓ₀) and mode(ℓ₀ − φ_L) ever differ.
  - Acceptance: equal to `output.txt` §PLANE, §AGREEMENT, §CELLS WHERE THE READ-OUTS DISAGREE and §FLOORS
    AND THE V; the existing lines unchanged.
- [ ] **T3. The tilt/width decomposition (R15). Placement is the user's call.**
  - The preliminary result, F4 below, comes from `mode_mechanism.py`. Decide whether it is printed,
    and where:
    - (i) Code Cell 2, for Part D's rows;
    - (ii) Code Cell 4's summary, for the plane counts;
    - (iii) both;
    - (iv) not printed, if the paper does not quote it.
  - [x] Prerequisite (2026-09-13): the Eq. (24) halving is checked across the plane and on Part D's
    rows (F5, `halving_check.py`). The placement decision above is still open.
  - Acceptance: equal to `mode_mechanism_output.txt` for whatever is printed.
- [x] **T4 (2026-09-14). Mirror into Appendix E** — closed for T1: the block patched into E2 with the
  same replacement; no new printing call, so E3's replay list is unchanged. Originally:
  - Lift T1's changes and any T3 addition to Code Cell 2 verbatim into E2.
  - If a new printing call is added, add it to E3's replay list, with what it needs passed in.
  - Keep the `# === Code Cell 2` prefix.
- [x] **T5 (2026-09-14). Execute main, then appendix_E** — closed for T1: `RUNNER OK main.ipynb: error
  outputs 0, figures 8, runtime 248 s`, 14/14; `RUNNER OK appendix_E.ipynb: error outputs 0, figures 5,
  runtime 706 s`, E2 18/18, E3 PASS (202 and 233 lines identical), E4 unchanged. Output diffs against
  7854b8f: the T1 block inserted, and the C7 renames. Record: `audits/2026-09-14-no-position/`. T2, T3
  and T6 remain open. Originally:
  - Baseline: main 0 errors, 6 figures, 14/14; appendix_E 0 errors, 3 figures, E2 18/18, E3 PASS.
  - Diff the stored outputs against the T0 hash: only insertions, plus `cost:` lines.
- [ ] **T6. Notebook prose. Wording needs the user's review before it lands.**
  - Text cell 4 Part D's reading guide defines (a) and (b) as reported statistics, class (b) of
    agent.md §3.3, as unnumbered displays so Eqs. (1)–(41) do not shift (agent.md §2 item 5). It
    also announces the new lines.
  - Text cell 6, *Where both of Part C's conditions hold*: the delta criteria's counts, and the V
    under both read-outs, reported as a result (R14).
  - Text cell 4 Part C: one sentence that the conditions have a delta counterpart (B8) and that the
    two do not coincide.
  - Every quoted number is checked against the executed output.
- [ ] **T7. Records.**
  - `decisions.md`: B8's implementational reason; an E-register entry for each new printed
    quantity; an I-entry for the mode tie rule if T1 makes one.
  - `thesis_outline/revisions.md` §8: point the numbers of Q2 and Q6 at their cells.
- [ ] **T8. Commit** (agent.md §4.3), with the hash recorded on each closed task.
- **Order (2026-09-14, user, S-5 of `evaluation_partD_atStrongLambda.md`):** these tasks follow
  that change. T1 then prints the criteria in Code Cell 2 (Part D's four priors at Λ = 8) and in
  Code Cell 2b (all five at Λ = 512), where the delta-like row now lives; T1's acceptance against
  `output.txt` §PART D ROWS splits accordingly, and T4 mirrors into E2 and E2b.

## 3. Findings

- **F1 (2026-09-13, `output.txt`). The second conditions coincide; the first do not.**
  - On Part D's five rows, B8 and B2 agree row by row.
  - On the 121 plane cells:
    - q's second condition and (b) hold in the same 59 cells;
    - q's first condition holds in 74 cells and (a) in 67, disagreeing in 35;
    - the conjunctions hold in 33 and 13 cells, with every delta conjunction a q conjunction.
- **F2 (same). The V's left arm exists only under q.**
  - Least Λ for both:
    - under q: 512, 256, 128, 64, 64, 256, 512, 1024 at α = 1 … 128;
    - under the delta: none at α ≤ 8, then 256, 256, 512, 1024.
  - The right arm is shared, at Λ = 8α for α = 32–128.
- **F3 (same). Grid facts.**
  - mode(ℓ₀) = mode(ℓ₀ − φ_L) in every cell under *some*.
  - In 4 cells the mode does not move at all.
  - The smallest gap between the two largest nodes is 5.6e-5, so there are no ties.
- **F4 (2026-09-13, `mode_mechanism_output.txt`, preliminary). Why the mode moves up under the delta
  read-out.**
  - **The split.** The utility field φ_S\* − φ_S\*(θ_u = 0) lies in span B to 1.7e-12 (Eq. 23). It
    is split into B's odd (tilt) and even (width) columns.
  - **Signs.** On all 121 plane cells the tilt coefficient is positive and the width coefficient
    negative. On Part D the same holds, except that Beta(1,3)'s tilt is negative. Width is negative
    in all 126 configurations.
  - **Mass.** The width part alone lowers the all-region q-mass in all 121 cells; the tilt part alone
    never does.
  - **Mode.**
    - Where the model's mode moves up (50 cells), the tilt part alone moves it up and the width part
      alone never does.
    - Where it moves down (67 cells), the width part alone moves it down and the tilt part alone
      never does.
    - The sign of the two parts' combined slope at the literal mode predicts the direction in all
      117 cells where the mode moves. That is the first-order argument: at a smooth peak of the
      tempered field, adding g moves the peak by about g′/curvature.
    - The mode moves up where the literal mode sits at s ≤ 0.9405, and down where it sits at
      s ≥ 0.9405.
  - **Reading.**
    - A negative width coefficient concentrates the belief toward the centre of the scale. That
      lowers both tails, the all-region among them, and pulls the peak inward. The pull is zero at
      the centre, where the even column is flat, and grows toward the ends.
    - The tilt slides the peak in its own direction.
    - Near the centre the tilt wins and the peak moves up; near the upper end the width wins and the
      peak moves down.
    - q's first condition reads the tail, which the width governs. Criterion (a) reads the peak,
      which the tilt governs near the centre.
  - **Where the signs come from.** By Eq. (24), at large |θ_u| the utility field is half the literal
    field's span-B component, so the model doubles that component.
    - Under the delta-like prior the coefficients are exactly half of Part C's c_some:
      +480.83 = 961.66/2, and −264.89 ≈ −529.77/2.
    - So the tilt carries the skew of the literal field, the prior and the entry together. Even the
      symmetric Gaussian gets a positive tilt, because *some* excludes the bottom of the scale.
    - The width is negative because every log-density tested falls off toward both ends.
  - **Part D's four diffuse rows.**
    - Gaussian and flat: the literal mode is at the centre, where the width has no pull (slope 0),
      so the tilt alone moves the peak up.
    - Beta(3,1): the tilt's push (slope +0.881) outweighs the width's inward pull (−0.453).
    - Beta(1,3): the tilt pushes down (−0.125), but the mode sits below the centre, where the
      width's inward pull is upward (+0.454) and wins.
  - **What it says about the V.**
    - For α ≤ 8 the literal mode sits at s ≤ 0.885, inside the tilt-dominated range, so no Λ moves
      the mode down and (a) never holds.
    - From α = 32 the literal mode sits at s ≥ 0.970, where the width dominates.
    - α = 16 is at the crossover (0.9405).
  - **What it says about Q6.** The delta read-out's upward movement and q's positive shift share a
    direction and not a source. q's positive shift is the tempering, which a mode cannot see. The
    delta's movement is the tilt, plus the width's inward pull below the centre.
  - **Caveats.**
    - Modes are grid nodes.
    - The direction argument is first order.
    - The Eq. (24) halving was checked exactly only on the delta-like row. **Discharged by F5.**
    - No cell prints any of it.

- **F5 (2026-09-13, `halving_check_output.txt`). Eq. (24)'s halving holds across the plane, and the
  limit field carries F4's reading in every configuration tested.**
  - **Exact form.** At σ = 1 with BᵀWB = I (checked to 2.2e-16), Eqs. (15)–(16) give the utility
    coefficients as k = (θ/2)(μ_u + (θ/2)c)/(1 + θ²/2), with c = BᵀW(ℓ₀ − φ_L). The fitted coefficients
    match that to 1.2e-15. So k − c/2 = ((θ/2)μ_u − c/2)/(1 + θ²/2), which vanishes as |θ_u\*| grows.
  - **Distance from c/2, relative.**
    - Plane: the median is 8.6e-7 for the tilt and 4.8e-6 for the width. Both columns are within
      1e-3 in 111 cells, within 1e-2 in 119, and within 1e-1 in 120.
    - The worst cell is (α, Λ) = (1, 2), at θ\* = −6.51, the smallest |θ\*| on the plane: its tilt is
      17% below half (+0.94 against +1.14). The next is (1, 4), at θ\* = −16.39, with 3.4%.
    - Part D: Gaussian tilt 1.0e-2, Beta(1,3) tilt 3.8e-2, everything else ≤ 3e-3. The delta-like
      row is at 4.7e-7 and 3.7e-6.
  - **Signs.** sign(k) = sign(c) in both columns in all 121 cells and all five Part D rows. c is
    (+, −) in every plane cell; on Part D, Beta(1,3)'s c tilt is negative (−2.88). Part C's c_some
    under the delta-like prior is reproduced: +961.66, −529.77.
  - **The limit field.** ½(ℓ₀ − φ_L) + B c/2 has the model's mode node in all 121 cells.
    Criteria (a) and (b) and q's two conditions read the same off it as off the model, in all 121
    cells and in Part D's five rows. The q-masses differ slightly (flat 0.0798 against 0.0799;
    Beta(3,1) 0.1775 against 0.1788) without changing a verdict.
  - **Consequence.** F4's reading holds already at the smallest |θ_u\*| on the plane. In every
    configuration tested, the verdicts of both read-outs are those of the model doubling the literal
    field's own tilt and width. F4's caveat on the halving is discharged. Its other two caveats, grid
    modes and the first-order argument, stand.

## 4. Prose sites (after T1–T5)

- `thesis_outline/revisions.md`: §4.5 (the V under both read-outs); item 1 and §4.4 (the Cremers
  parallel, with F4's two sources, if the paper keeps the explanation).
- `main.ipynb`: as in T6.
