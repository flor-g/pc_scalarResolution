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

- [ ] **T0. Checkpoint** (agent.md §4.2). Record the HEAD hash.
- [ ] **T1. Code Cell 2, `delta_readout_report`: print criteria (a) and (b).**
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
  - Before any of these, check the Eq. (24) halving across the plane, not only on the delta-like row
    (F4 caveat).
  - Acceptance: equal to `mode_mechanism_output.txt` for whatever is printed.
- [ ] **T4. Mirror into Appendix E** (agent.md §2).
  - Lift T1's changes and any T3 addition to Code Cell 2 verbatim into E2.
  - If a new printing call is added, add it to E3's replay list, with what it needs passed in.
  - Keep the `# === Code Cell 2` prefix.
- [ ] **T5. Execute main, then appendix_E** (agent.md §5.1).
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
    - The Eq. (24) halving is checked exactly only on the delta-like row.
    - No cell prints any of it.

## 4. Prose sites (after T1–T5)

- `thesis_outline/revisions.md`: §4.5 (the V under both read-outs); item 1 and §4.4 (the Cremers
  parallel, with F4's two sources, if the paper keeps the explanation).
- `main.ipynb`: as in T6.
