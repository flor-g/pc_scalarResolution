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

> (2026-09-14, on T3) I think T3 should be at appendix C; if you need me to be more specific than
> that, explain what the print will include in more detail and I will tell you where it goes.

> (2026-09-14, on the three sub-choices offered) 1. (b) as you recommended. 2. all three blocks 3.
> lambda at 8 only for Block 1's rows.

> (2026-09-14, on the §8 draft, the §9 sentence and the counterfactual label) 1. prose approved. 2.
> approved 3. confirmed;  When you finished this up, proceed to T2.

> (2026-09-15, on T7's three questions) 1 and 3 are confirmed. Can you tell me more about 2?

> (2026-09-15, on the classing of the two single-part fields) these are essentially algebraic
> manipulations, as opposed to model manipulations that currently occupies the name of control. I
> think both are control by nature, but for the sake of not confusing the reader maybe lets call it
> counterfactual manipulations?

T3's placement, as offered and chosen: a new Appendix C §8, the present §8 renumbered §9 (anchor
`appc-8` becomes `appc-9`, ToC row regenerated); Code Cell C prints Block 1 (Part D's four priors at
Λ = 8: tilt and width coefficients, modes and all-region masses of the tempered control, the control
plus each part alone and the model, slopes at the control's mode), Block 2 (the 121-cell plane: sign
counts, mode up/down/unmoved and which part alone moves it, mass counts, where the control's mode
sits, and the table of cells where the q shift criterion is met and the mode shift criterion is not)
and Block 3 (the Eq. (24) halving: exact form, distance from c/2, signs, the limit field's mode and
criteria, the ten cells furthest from the halving, Part D's four rows). The coefficients are at each
configuration's own Λ and θ_u\*, not per unit Λ, and the new section says so.

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

## 2. Tasks, in order

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
- [x] **T2 (2026-09-14). Code Cell 4: the mode criteria recorded and summarized on the plane.** Closed:
  `lambda_alpha_sweep` stores, under *some* per cell, the mode nodes of φ_S\*, ℓ₀ and ℓ₀ − φ_L, the modes
  of φ_S\* and ℓ₀ in s, whether φ_S\*'s mode is outside the cell of *all*, and the smallest top-2 gap of
  the three fields. `plane_summary` adds `mode_shift`, `mode_position`, `mode_both` and `floors` (all six
  criteria) to its returned summary, and prints one block after the existing lines: the counts under
  both read-outs, unmoved modes and the ℓ₀ / ℓ₀ − φ_L comparison, the smallest gap, agreement for the
  shift criteria, the position criteria and the conjunctions, the 35 cells where a q criterion and its
  mode counterpart disagree (θ\*, P(all|some), shift, tempering, utility, both modes, the four yes/no),
  and the floors by α under both read-outs (the V), with * where a criterion also holds below its floor
  (none do). C7 names throughout. Acceptance (`audits/2026-09-14-mode-plane/test_t2.py`, before
  execution): existing lines unchanged; counts 67/59/13 against 74/59/33, unmoved 4, differing modes 0,
  gap 5.60e−05, agreement 53/21/14/33, 59/0/0/62, 13/20/0/88, all 35 rows and the V table equal to
  `output.txt`: PASS. Executed: main 0 errors, 8 figures, 14/14, 251 s; the only output change is Code
  Cell 4's 62 added lines, equal to the test; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS (203
  and 234 identical), 703 s. Code Cell 4 is not mirrored in appendix_E. The unmoved-mode count is
  printed as a node comparison (a shift of 0 steps). Commit 5ee04a6. Originally:
- **T2. Code Cell 4: record and summarize the delta criteria on the plane.**
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
- [x] **T3 (2026-09-14). Code Cell C, `utility_split_report`: the tilt/width split printed in Appendix
  C (user: new §8, Blocks 1-3, Block 1 at Λ = 8 only; §0).** Closed for the code: one function and one
  call appended to Code Cell C, called with `part_d_priors()` and Code Cell 4's `sweep_grids` α and Λ
  lists, so the plane is Code Cell 4's. Prints Blocks 1-3 as recorded in §0, under C7 names; the two
  single-part fields are labelled as counterfactual, not network states (agent, pending user
  confirmation: a construction of the report, not a control of the model). Acceptance
  (`audits/2026-09-14-utility-split/acceptance.py`, run before insertion): every number of
  `mode_mechanism_output.txt` and `halving_check_output.txt` for Part D's four diffuse rows, every plane
  count, the 21-cell and ten-cell tables: PASS. Executed: main 0 errors, 8 figures, 14/14, 266 s; the
  only output change is Code Cell C's 91 added lines, equal to the pre-insertion test; appendix_E 0
  errors, 5 figures, E2 18/18, E3 PASS (203 and 234 lines identical), 673 s. Code Cell C is not mirrored
  in appendix_E, so T4 does not apply. The §8 prose (and §9 renumbering, ToC, anchor) is drafted in §5
  for review. Commit 27a4122. Originally:
- **T3. The tilt/width decomposition (R15). Placement is the user's call.**
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
- [x] **T6 (2026-09-15). Notebook prose, approved by the user and applied.** Closed: the six edits of
  §6 (E1–E6) into Text cells 4, 4b and 6, commit af971c4. E1 Part C, the pairs do not always agree
  (121 position, 35 shift); E2 Part D, the two criteria as unnumbered displays on $k^\ast$ and $k_0$,
  the grid-steps column and the 0.12 spacing, and the Λ = 8 result (3, 6, 3, 5 steps; met under none
  and all four); E3 the R15 correction, made explicit at the user's instruction (which shift, which
  movement); E4 Text cell 4b, the eight rows and the steps at Λ = 512, with the flat row as plane cell
  (1, 512); E5 Text cell 6, the plane under the delta read-out and the V under both read-outs; E6 (the
  user, 2026-09-15) the word "delta" is the delta distribution, in the read-out's name and in the
  delta-like prior, and is unrelated to $\Delta_y$. Applied by `audits/2026-09-14-mode-plane/apply_t6.py`.
  Checks: every number in the new prose is printed by Code Cell 2, 2b, 4 or C; 74 anchors, 73 ToC
  links, none unresolved; no new "condition" or "verdict"; markdown spacing kept. Markdown only, so
  the notebooks were not re-executed. Originally:
- **T6. Notebook prose. Wording needs the user's review before it lands.**
  - Text cell 4 Part D's reading guide defines (a) and (b) as reported statistics, class (b) of
    agent.md §3.3, as unnumbered displays so Eqs. (1)–(41) do not shift (agent.md §2 item 5). It
    also announces the new lines.
  - Text cell 6, *Where both of Part C's conditions hold*: the delta criteria's counts, and the V
    under both read-outs, reported as a result (R14).
  - Text cell 4 Part C: one sentence that the conditions have a delta counterpart (B8) and that the
    two do not coincide.
  - Every quoted number is checked against the executed output.
- [x] **T7 (2026-09-15). Records, approved by the user and applied; commit 5acb6b5.** §7 holds the
  six changes: `decisions.md` B8's dated finding, the new C8 (control names a manipulation of the
  model; an algebraic one is a counterfactual manipulation), I12 (the argmax tie rule, confirmed by
  the user), E14 (the classing of everything T1–T3 added); `thesis_outline/revisions.md` §8's three
  rows, its dated note, and the two stale "not printed by any cell" lines; `agent.md` §3.3's class (c)
  row, which cited decision E4 where the entry is B4, now also carrying C8's distinction; and C8's
  naming in Code Cell C's comment and printed legend and in Appendix C §8. Verified: main 0 errors, 8
  figures, 14/14, the only output change being Code Cell C's legend; Code Cells 2 and 2b unchanged, so
  appendix_E was not re-executed. Still stale, left for the user: `revisions.md` line 816 says R15's
  investigation "is an open task in `procedure_records/delta_criteria_printing.md`", which T3 closed.
  Originally:
- **T7. Records.**
  - `decisions.md`: B8's implementational reason; an E-register entry for each new printed
    quantity; an I-entry for the mode tie rule if T1 makes one.
  - `thesis_outline/revisions.md` §8: point the numbers of Q2 and Q6 at their cells.
- [x] **T8 (2026-09-15). Commit** (agent.md §4.3), with the hash on each closed task: T1 2718404,
  T2 5ee04a6, T3 27a4122 with its prose 5a7bc8e, T6 af971c4, T7 5acb6b5, plus the record commits
  9937734, 92cf465, 4cb1d1a and 28c838a. Nothing is pushed; the user asks for pushes.
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
- `main.ipynb` Appendix C: the new §8 (draft below, for the user's review; not in the notebook), the
  present §8 renumbered §9 with its first sentence re-scoped, the ToC row, the anchor.

## 5. Appendix C §8 (T3's prose): approved by the user 2026-09-14 and applied

Applied by `audits/2026-09-14-utility-split/apply_prose.py`: §8 inserted as drafted, the old §8 now
§9 (`appc-9`), its first sentence as approved, the ToC row added (74 anchors, 73 links, none
unresolved). One change beyond the approved wording, for grammar: the next sentence's "It does not
address" became "They do not address", since its subject is now "Sections 1–7".

Every number is printed by Code Cell C's `utility_split_report` (test output
`audits/2026-09-14-utility-split/test_output.txt`, equal to the executed output if the run verifies).

> ### 8. Which part of the utility field moves the mode
>
> By Eq. (23) the field the utility level adds under *some*, $\varphi_S^\ast-\varphi_S^\ast(\theta_u{=}0)$,
> lies in $\operatorname{span}B$, so at $m=2$ it is $k_1b_1+k_2b_2$: a tilt part on the odd column and
> a width part on the even column, in §5's vocabulary. Unlike the projections of §§1–7, $k_1$ and
> $k_2$ are not per unit $\Lambda$: each is taken at its configuration's own $\Lambda$ and
> $\theta_u^\ast$, and $\theta_u^\ast$ moves with $\Lambda$. Code Cell C adds each part alone to the
> tempered control ($\theta_u=0$, field $\tfrac12(\ell_0-\varphi_L)$, whose mode node is that of
> $\ell_0$ in every configuration below) and reads off the mode and the all-region $q$-mass of
> Eq. (27). Those two fields are constructed for the comparison; the network does not settle on
> either.
>
> **Part D's priors at $\Lambda=8$.** The width coefficient is negative under all four priors, and
> the tilt coefficient is positive under three and $-1.50$ under $\mathrm{Beta}(1,3)$. Width alone
> lowers the all-region mass under all four, from $0.2356$ to $0.0230$ under $\mathrm{Beta}(3,1)$.
> Under the Gaussian and flat priors the tempered control's mode sits at $s=0.5000$, where the width
> part's slope is $0$: width alone leaves the mode there, tilt alone moves it up $6$ and $17$ grid
> steps, and the model moves it up $3$ and $6$. Under $\mathrm{Beta}(3,1)$ tilt alone moves the mode up
> $41$ steps and width alone down $4$, and the model moves it up $5$. Under $\mathrm{Beta}(1,3)$ the
> directions are exchanged, tilt alone down $3$ and width alone up $4$, and the model moves it up $3$.
>
> **The plane.** Over the $121$ cells of Code Cell 4, the tilt coefficient is positive and the width
> coefficient negative in every cell. The model's mode moves up in $50$ cells, down in $67$, and not
> at all in $4$. In every up cell tilt alone moves it up and width alone does not; in every down cell
> width alone moves it down and tilt alone does not. In all $117$ cells where the mode moves, the
> direction is the sign of the two parts' summed slope at the tempered control's mode, which is the
> first-order displacement of a smooth peak: adding $g$ to a field with a peak of curvature
> $f''<0$ moves the peak by about $g'/(-f'')$. The up cells are those whose tempered mode sits at
> $s\le0.9405$, the down cells those at $s\ge0.9405$. Width alone lowers the all-region mass in all
> $121$ cells and tilt alone in none. Code Cell C tabulates the $21$ cells where the $q$ shift
> criterion is met and the mode shift criterion is not.
>
> **Where the signs come from.** At $\sigma=1$ and $B^{\mathsf T}WB=I$, Eqs. (15)–(16) give
> $k=\tfrac{\theta_u}{2}\big(\mu_u+\tfrac{\theta_u}{2}c\big)\big/\big(1+\tfrac{\theta_u^2}{2}\big)$
> with $c=B^{\mathsf T}W(\ell_0-\varphi_L)$, so $k\to c/2$ as $\lvert\theta_u\rvert$ grows, which is
> Eq. (24). The fitted $k$ matches that form to $1.2\times10^{-15}$. The relative distance from $c/2$
> has median $8.6\times10^{-7}$ in the tilt column and $4.8\times10^{-6}$ in the width column, both
> columns are within $10^{-3}$ of it in $111$ cells, and the largest distance is $17\%$, in the tilt
> column at $(\alpha,\Lambda)=(1,2)$, where $\theta_u^\ast=-6.51$. $k$ and $c$ agree in sign in both
> columns in all $121$ cells. The limit field of Eq. (24) has the model's mode node, and gives the
> same reading on each of the four criteria, in all $121$ cells and under Part D's four priors. The
> signs of the tilt and width parts are therefore the signs of the literal field's own projection.
>
> Modes here are grid nodes, and the direction argument is first order, checked only by its sign.

Present §8's first sentence, to become §9's: "Everything above concerns separation and spanning." →
"Sections 1–7 concern separation and spanning."

## 6. T6 prose: approved by the user 2026-09-15 and applied (af971c4)

Written 2026-09-15 against the executed outputs of 5ee04a6. Every number is printed by Code Cell 2's
or 2b's criteria block, Code Cell 4's new block, or Code Cell C. What the C7 pass (98c2df8) already
covers is kept; the edits below fill what T6 asks for. No heading is added, so the ToC does not change.

**E1. Text cell 4, Part C, "The criteria" paragraph: one clause (T6 item 3).** The sentence ending
"with a mode shift and a mode position criterion of its own." becomes:

> …with a mode shift and a mode position criterion of its own. The two pairs are not assumed to
> agree, and they do not always: over the plane of Text cell 6 the two position criteria agree in all
> $121$ cells and the two shift criteria disagree in $35$.

**E2. Text cell 4, Part D, "The delta read-out's two criteria": definitions as unnumbered displays,
the new columns, and the Λ = 8 result (T6 item 1).** The paragraph becomes:

> **The delta read-out's two criteria.** Under *some*, Code Cell 2 also prints two criteria on the
> peak of $\varphi_S^\ast$, which it calls the mode. Writing $k^\ast$ for the grid node where
> $\varphi_S^\ast$ is largest and $k_0$ for the node where $\ell_0$ is, the **mode shift criterion**
> is
>
> $$k^\ast<k_0,$$
>
> met when the mode lies below the $\ell_0$ peak on the scale, and the **mode position criterion** is
>
> $$\zeta_{k^\ast}<\theta_L,$$
>
> met when the mode lies outside the cell of *all*. Both are statistics of the delta read-out, as the
> q criteria are of $q$, and neither is a model quantity. Being comparisons of grid nodes, they resolve
> a movement of the mode to one node; a tie would go to the first node, and the cell prints the gap
> between the two largest values of $\varphi_S^\ast$, which is never zero in these rows. The cell
> prints the mode shift in $s$ and in grid steps, $k^\ast-k_0$. The grid is uniform in $\zeta$ while
> $s$ compresses toward the ends of the scale, so the steps, multiplied by the grid spacing of
> $0.12$, give the shift in $\zeta$. The mode criteria are the counterparts on the delta read-out of
> the q shift and q position criteria and are not assumed to agree with them, so the cell prints the
> four side by side, with how often each pair agrees. As with the q criteria, this notebook takes no
> position on how they should be interpreted. At $\Lambda=8$ the mode lies $3$, $6$, $3$ and $5$
> grid steps above the $\ell_0$ peak under the Gaussian, flat, $\mathrm{Beta}(1,3)$ and
> $\mathrm{Beta}(3,1)$ priors, so the mode shift criterion is met under none and the mode position
> criterion under all four, and each agrees with its q counterpart in all four rows.

**E3. Text cell 4, Part D, the spike paragraph: a correction (R15).** The sentence "The movement of
the mode up the scale between the two is what the positive $\Delta_{\textit{some}}$ records." no
longer holds: by the paragraph above it, the positive shift is tempering, and halving a field does not
move its maximum. Proposed replacement:

> The movement of the mode up the scale between $q_{\mathrm{lit}}$ and the full network is the
> utility level's, since the $\theta_u$ control, $\tfrac12(\ell_0-\varphi_L)$, keeps its maximum where
> $q_{\mathrm{lit}}$ has it; Appendix C §8 splits the utility field into the part that moves the mode
> and the part that lowers the all-region mass. What $\Delta_{\textit{some}}$ records is not that
> movement: the shift under these two priors, $+0.0295$ and $+0.0421$, is all-region mass that the
> tempering adds to $q_{\mathrm{lit}}$ and that the utility level then fails to take away, as the
> paragraph above reports.

**E6. The word "delta" (user, 2026-09-15).** Two sites, so that the name is read as the distribution
and not as a difference. In Text cell 4 Part D, after "one row for each prior and utterance at that
prior's $\theta_u^\ast$.":

> The name is the delta *distribution* of Text cell 3 §4 item 5, the point mass at
> $(\varphi_S^\ast,\varphi_u^\ast)$, and the same word in the *delta-like* prior names a
> $\mathrm{Beta}(\alpha,1)$ approaching a point mass at $s=1$. Neither use carries any relation to
> $\Delta_y$, the shift of Eq. (37).

and in Part C, at the first occurrence of "delta-like", which precedes Part D:

> …and the delta-like prior concentrated on the all-region, a $\mathrm{Beta}(64,1)$ approaching a
> point mass at $s=1$, which needs that $\Lambda$…

**E4. Text cell 4b, after "We note the difference and reserve our position on it." (T6 item 1, for
Code Cell 2b).** Inserted before "Under *no* and *all*…", which then opens a new paragraph:

> Over the eight rows Code Cell 2b prints, the five at $\theta_u^\ast$ and the three realizable, the
> mode position criterion is met in all eight and the mode shift criterion in two, the delta-like
> prior's; the mode and q shift criteria agree in four of the eight. In grid steps the mode lies $19$,
> $20$, $27$ and $11$ nodes above the $\ell_0$ peak under the four diffuse priors and $11$ below it
> under the delta-like prior. The flat row is the plane's cell $(1,512)$, one of the $21$ cells
> Appendix C §8 tabulates where the q shift criterion is met and the mode shift criterion is not.

**E5. Text cell 6, section *Where both of Part C's q criteria hold*: two paragraphs after "What the
conjunction costs" (T6 item 2, R14).**

> **The same plane under the delta read-out.** Code Cell 4 also reads the mode shift and mode
> position criteria of Text cell 4 Part D off every cell. The mode position criterion holds in the
> same $59$ cells as the q position criterion. The mode shift criterion holds in $67$ cells against
> the q shift criterion's $74$, and the two disagree in $35$: the q shift criterion alone is met in
> $21$, all at $\alpha\le16$, and the mode shift criterion alone in $14$, which are ten cells of the
> saturated $\alpha=1024$ row and $(32,16)$, $(64,2)$, $(64,4)$ and $(64,8)$. Both mode criteria hold
> together in $13$ cells, every one of them inside the band of $33$, so the two conjunctions part in
> $20$ cells, all of them met under q alone.
>
> Under the delta read-out the band keeps its right arm and loses its left. The mode position
> criterion's floor is the q position criterion's at every $\alpha$. The mode shift criterion is never
> met at $\alpha\le8$; from $\alpha=16$ its floor is $256$, then $16$ at $\alpha=32$, then $2$ from
> $\alpha=64$ on. The floor of both mode criteria is therefore absent at $\alpha\le8$ and reads $256$,
> $256$, $512$ and $1024$ at $\alpha=16$, $32$, $64$ and $128$, against the q conjunction's $64$,
> $256$, $512$ and $1024$. The right arm, set by the position criteria, is shared from $\alpha=32$;
> the left arm, where the q shift criterion's floor falls as the prior sharpens, exists only under q.
> Appendix C §8 measures what the mode does there. Every cell where the mode moves up has the
> tempered control's mode at $s\le0.9405$, and every cell where it moves down has it at
> $s\ge0.9405$; at $\alpha=1$, $2$, $4$ and $8$ the $\ell_0$ peak, which is the tempered control's
> mode, sits at $s=0.5000$, $0.6726$, $0.8085$ and $0.8849$.

Choices put to the user, all approved 2026-09-15:
- E3 corrects an interpretive sentence (agent.md §5.4); its replacement follows R15.
- E2 writes the mode as the node $k^\ast$, following $k$ as the node index of Eqs. (25)–(27).
  Appendix C §8 writes $k_1,k_2$ for the utility coefficients, in a separate cell.
- E5 gives the V as a result and stops at the measurement: the two paragraphs do not say which
  criterion reads which part of the field.

## 7. T7 records: approved by the user 2026-09-15 and applied

Six changes, in `decisions.md`, `thesis_outline/revisions.md`, `agent.md` and the notebook. Under
agent.md §3.1 a settled decision is never edited, so B8 takes a dated finding rather than a rewrite.

**A. `decisions.md` B8, appended under *Findings added later*.**

> - **2026-09-15. The criteria are printed, and so is the mechanism under them.**
>   - T1 (2718404): Code Cells 2 and 2b, mirrored in E2 and E2b, print per row the modes of ℓ₀,
>     ℓ₀ − φ_L and φ_S\* in s, the mode shift in s and in grid steps, the two mode criteria beside the
>     two q criteria, the gap between the two largest nodes, and the counts and pairwise agreement.
>     At Λ = 8 the pairs agree in 4 of 4 rows; at Λ = 512 the shift criteria agree in 4 of 8 and the
>     position criteria in 8 of 8.
>   - T2 (5ee04a6): Code Cell 4 prints the same criteria over the 121 cells: 67, 59 and 13 against
>     q's 74, 59 and 33, the 35 cells where a shift criterion and its counterpart disagree, the four
>     unmoved modes, the 5.6e-5 smallest gap, and the floors under both read-outs.
>   - T3 (27a4122, prose 5a7bc8e): Code Cell C prints the tilt/width split, the plane counts and
>     Eq. (24)'s halving, reported in the new Appendix C §8.
>   - T6 (af971c4): Text cell 4 Parts C and D, Text cell 4b and Text cell 6 carry the criteria in
>     prose, under C7's names and B10's stance.
>   - Every number in this entry's *Evidence* and in the F4/F5 findings above is therefore printed
>     by a cell, and the numbers Q2 and Q6 of `thesis_outline/revisions.md` quote are sourced (C6).

**B. `decisions.md` E register, new entry E14.**

> **E14. The quantities T1–T3 added (2026-09-15).** Classed by the agent; the counterfactual label
> was confirmed by the user 2026-09-14.
> - Code Cells 2 and 2b (and E2, E2b): the modes in s, the mode shift in s and in grid steps
>   $k^\ast-k_0$, the two mode criteria and their conjunction, the top-2 gap, and the counts and
>   agreement: class (b), statistics of the delta read-out (B7, B8), defined in Text cell 4 Part D
>   since T6.
> - The grid spacing printed in that block's legend: class (d), read from the grid of I6 rather than
>   stored as a constant.
> - Code Cell 4, `lambda_alpha_sweep`: per cell under *some*, the mode nodes of φ_S\*, ℓ₀ and
>   ℓ₀ − φ_L, the modes of φ_S\* and ℓ₀ in s, whether φ_S\*'s mode lies outside the cell of *all*, and
>   the smallest top-2 gap of the three fields: class (b). `plane_summary`'s counts, agreement, the
>   35-cell table and the six floors: class (b). Signs are read with I5's zero band.
> - Code Cell C, `utility_split_report` (Appendix C §8): the tilt and width coefficients of the
>   utility field, the span-B residual, the two slopes at the tempered control's mode, the modes and
>   all-region masses of the four fields, the plane counts, the distances from c/2, the Gram and
>   exact-form errors, and the limit field's mode and criteria: class (b), statistics of Eqs. (15),
>   (16), (23) and (24) defined in Appendix C §8.
> - The two single-part fields, the tempered control plus tilt alone and plus width alone:
>   **counterfactual manipulations** (C8), controls in nature but not manipulations of the model,
>   since no setting of θ_u, Λ or μ_u produces either. Their printed numbers are class (b). B4's list
>   of retained fixed-θ_u controls (`theta_u_learned_reach.md` §5.C) is unaffected, since neither
>   field is an evaluation the model is run in. The printed block and Appendix C §8 name them so.
> - Appendix C §1 writes every projection per unit Λ; §8's coefficients are the exception, each at
>   its configuration's own Λ and θ_u\*, and §8 says so.
> - Code Cell 2b's own quantities stay under E12, and E13's masses are unchanged.

**B2. `decisions.md` C section, new entry C8 (the user, 2026-09-15).**

> ### C8. "Control" names a manipulation of the model; an algebraic one is a counterfactual manipulation
> - Status: Settled
> - Decided by: user (2026-09-15)
> - Decision: both kinds are controls in nature. The notebooks keep **control** for a manipulation of
>   the model, a configuration the network is actually run in with a parameter held off its learned
>   value: Part C's θ_u control, Text cell 5's θ_u = 1 tables, the μ_u settings, the m = 1 basis. A
>   quantity built by algebra on settled fields, which no setting of the model produces, is a
>   **counterfactual manipulation**: Appendix C §8's two single-part fields, the tempered control plus
>   the tilt part alone and plus the width part alone.
> - Theoretical reason: none. The distinction is for the reader (the user: "for the sake of not
>   confusing the reader").
> - Implementational reason: agent.md §3.3 keeps q_lit, the tempered control and the model apart, and
>   B4 lists the retained fixed-θ_u controls in `theta_u_learned_reach.md` §5.C. A field that is the
>   tempered control plus part of the utility field would take a third name confusable with the
>   second, and would enter that list without matching any run.
> - Bogacz status: naming convention; no operation.
> - Depends on it: Appendix C §8's prose, Code Cell C's printed block, E14's classing.
> - Evidence: no setting of θ_u, Λ, μ_u or B makes the network settle on either field; each is
>   φ_S\*(θ_u = 0) plus one column's share of Eq. (23)'s utility field.

**C. `decisions.md` I register, new entry I12.**

> ### I12. The mode is the first node of an argmax, and the gap is printed
> - Status: Settled
> - Decided by: agent, pending user confirmation (2026-09-15)
> - Decision: the mode of a field is `torch.argmax`, which takes the **first** node when two nodes
>   tie. Every block that reports a mode also prints the gap between the two largest values of
>   φ_S\*, so a tie would print as 0. Observed smallest: 3.4e-3 over Part D's rows at Λ = 8,
>   7.8e-3 over Code Cell 2b's rows, 5.6e-5 over the plane.
> - Theoretical reason: none. B7 defines the mode as the largest node and is silent on ties.
> - Implementational reason: a tie has to resolve somehow, and B8's mode shift criterion is a strict
>   node comparison, so which way it resolves would decide the criterion in a tie. Printing the gap
>   makes the rule's reach visible instead of assumed.
> - Bogacz status: statistic of the delta read-out (his Eq. 34); no counterpart in the tutorial.
> - Depends on it: B8's two criteria; Code Cells 2, 2b, 4 and C.
> - Evidence: the gaps printed in those cells; `audits/2026-09-13-delta-criteria/output.txt`.

**D. `thesis_outline/revisions.md`.** Three rows in §8, and two stale lines corrected. The R14 and
R15 rows are the user's and are not edited; the note goes in §8.

> | Q2's Part D and Λ = 512 rows: the modes, the mode shift in s and in grid steps, the two mode
> criteria | `main.ipynb` Code Cells 2 and 2b, the mode criteria block |
> | Q2's plane counts (67, 59, 13 against 74, 59, 33), the 35 disagreeing cells, the four unmoved
> modes, the 5.6e-5 gap, and the V under both read-outs | Code Cell 4, `plane_summary` |
> | Q6's tilt/width split, the 50 and 67 up/down counts, Eq. (24)'s halving and the limit field |
> Code Cell C, `utility_split_report`; Appendix C §8 |
>
> (2026-09-15: R14's and R15's code tasks, T1–T3 and T6 of
> `procedure_records/delta_criteria_printing.md`, are closed; T7 and T8 remain.)

- Q2, under *The audit*: "**Nothing in this subsection is printed by a notebook cell yet** (see
  "Printing" below)." becomes "**2026-09-15: every number in this subsection is printed**, by Code
  Cells 2, 2b and 4."
- Q6, at *Preliminary result*: "(record F4; `audits/…/mode_mechanism_output.txt`; not printed by any
  cell)" becomes "(record F4; printed by Code Cell C and reported in Appendix C §8 since 2026-09-15)".

**E. `agent.md` §3.3, the class (c) row (the user, 2026-09-15: "fix the error in agent.md").** The row
cited "decision E4" for the rule that a control states its justification in the prose; the entry
about controls is **B4** (E4 in `decisions.md` is the elicited-prior finding, and Code Cell E4 in
`appendix_E.ipynb` is a third thing with that label). The row now cites B4, says a control is a
configuration the network is actually run in, and adds C8's distinction: a quantity built by algebra
on settled fields is a counterfactual manipulation, not a control.

**F. The naming applied with C8 (the user, 2026-09-15).** Code Cell C's comment and printed legend and
Appendix C §8's sentence now say *counterfactual manipulation* and reserve *control* for a
configuration the model is run in. Code Cell C's printed legend grows by one line, so main was
re-executed; `appendix_E.ipynb` was not, since E3 reads main's Code Cell 2 and 2b outputs and Code
Cell C is not mirrored there.

Confirmed by the user 2026-09-15: I12; the Q2 and Q6 corrections made in place; C8's naming, so
E14 classes the two single-part fields as counterfactual manipulations rather than as controls; and
the `agent.md` fix. Nothing in T7 is left open.
