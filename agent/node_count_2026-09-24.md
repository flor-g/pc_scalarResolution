# The node count K: printing what was found, and what it implies (opened 2026-09-24)

Working record under `agent/agent.md` §5.3. Fold into `agent/history.md` when it closes. IDs carry
the prefix **NK** so they do not collide with `thesis_outline/revisions.md`'s R and Q or with the
proof-scope record's PS.

## 1. The user's instructions

> Now can you check if we have every tried accuracies other than K = 10?

> I see. The trend towards finer K is worth reporting. However, I am more interested in the trend
> towards coarser K, since that informs us the minimum complexity required before things become
> unpredictive.

> No need. Print what we have found so far in an appropriate place the notebook. In the outline,
> discuss the implications and direction of future investigation regarding this issue. Now plan
> your tasks regarding this.

"No need" declines the aligned-grid audit (θ_L held on a Voronoi boundary at every K). It is
therefore **not** run here; it enters the outline as a direction of future investigation.

## 2. What is already established (evidence, not yet printed by a cell)

From `agent/audits/2026-09-24-node-count/` and decision I6's two 2026-09-24 findings:

- **Before this change, no cell re-evaluated the criteria at another K.** K was varied only for
  E[s] (Code Cell 2's specification check), for the delta-like row's boundary peak (Code Cell 2b),
  for the neighbour rule (Code Cell A, PS11), and jointly with Z in the half-width ladders.
- **The finer end.** Part D's nine rows keep all four statuses at K = 101 to 1601. The plane's q
  conjunction runs 33, 36, 36, 34 and the mode conjunction 13, 15, 15, 15 at K = 101, 201, 401,
  801. The subset relation holds at every K. Five boundary cells account for the movement.
- **The coarse end.** Agreement with K = 801 stays at the fine grids' own floor down to K = 81
  (spacing 0.15, 21 nodes in the cell of *all*). K = 61 is the first where a Part D status flips.
  Below that, results alternate with whether a node falls just inside the cell (ζ = 3.0 against
  θ_L = 2.944), under the hard and the smooth mask alike: the coarse end measures the
  discretization of cut-based statistics, not a representational minimum of the model.

## 3. Decisions this rests on, and the ones it needs

- **I10** (where C6's numbers are printed) and its 2026-09-23 precedent: each cell reports the
  dependence of **its own** statistic, and the four criteria and the plane at every Z went to Code
  Cell A. The K ladder is the same statistic along the third grid axis, so it goes to Code Cell A
  too, beside `half_width_report`. Code Cell A has no mirror, so E2, E2b and E3 are untouched.
  **Agent's placement, pending the user.**
- **B10 / C7.** The notebook states what the ladder shows and takes no position on it; the words
  "condition" and "verdict" are not used.
- **C6.** Every count the outline will quote must first be printed by the new block.
- **NK-D1, answered by the user 2026-09-24: no K end in §4.2's guard.**
  > No to the 4.2 guard. we don't know the lower bound of K yet, so we don't want to add that to the
  > guard as if we know it. What we need in the outline is a warning to the reader on a suspected
  > lower bound of K and pointer to the relevant section that discusses what we know about it.

  So the lower bound is **suspected, not established**, everywhere it is written, notebook
  included. The guard stays with n and Z. The outline carries a **warning** where the reader meets
  the grid (§4.3, which reports grid refinement) and a **pointer** to §5.5, which holds what is
  known. The headline counts get **no per-site K qualifier**; the finer-end movement of the plane
  counts (33 → 36, 13 → 15) is reported in §5.5 beside the coarse end. *Agent's reading of the
  ruling on that last point, named to the user.*

## 4. Tasks, in order

- [x] **NK0. Checkpoint.** `git status` clean at `5e755a1` (2026-09-24).
- [x] **NK1. Code: `node_count_report` in Code Cell A**, called after `peak_locality_report`.
  Prints, under *some*, each configuration at its own θ_u\* (A9):
  1. **The floor**: K = 401 against K = 801, cells agreeing per criterion, of 121.
  2. **The finer end**: Part D's nine rows × four criteria at K = 101, 201, 401, 801, 1601, with
     the delta-like row's P(all); the plane's six counts and the mode-not-q reversals at K = 101,
     201, 401, 801.
  3. **The coarse end**, odd K only (101, 81, 61, 51, 41, 31, 25, 21, 17, 15, 13, 11, 9, 7, 5):
     spacing, nodes in the cell of *all*, **the distance from θ_L to the first node inside the
     cell** (the column that makes the node-placement mechanism visible rather than asserted), the
     two conjunction counts, cell-by-cell agreement with K = 801 per criterion, Part D statuses
     agreeing of 36.
  4. **The smooth-mask control** of the coarse end (exclusion sharpness 0.1, the control Code
     Cell 2's Sec. 1 check already uses), agreement columns only, labelled as a control (B4, C8).
  Acceptance: the numbers reproduce `coarse_ladder_output.txt`, `coarse_ladder_smooth_output.txt`
  and `plane_flips_output.txt`; runtime of the block recorded under `cost:`-free text only if
  deterministic. **Done**: the prototype reproduces all four audit outputs digit for digit and runs
  in about a second. One column differs from the plan (finding NK-F2).
- [x] **NK2. Execute** main, then appendix_E (E3 reads main's Code Cells 2 and 2b; neither
  changes, so E3 must pass with its usual shape). Acceptance: 0 errors, 8 and 5 figures, 15/15,
  E3 PASS (223/1/4; 263); a full output diff against NK0 shows only Code Cell A changed.
- [x] **NK3. Appendix A prose**: a paragraph after the half-width ladder, "**A third axis: the
  node count**", stated and not interpreted — K is the grid parameter Text cell 3 §1 calls an
  accuracy parameter; the finer end moves the plane counts by a few boundary cells and leaves
  Part D unchanged; the coarse end tracks the fine grid to K = 81 and, below K = 61, alternates with
  the distance from θ_L to the first node inside the cell, under the smooth mask too. It says that
  this **suggests a lower bound on K without establishing one**, since placement and resolution are
  not separated; the cell prints it and the appendix draws nothing further from it.
- [x] **NK4. Text cell 3 §1**: qualify "K is an accuracy parameter: refining it converges" — the
  settled fields and E[s] converge, while a criterion's status, being a threshold on them, can
  change at a boundary cell with K; pointer to Appendix A. (Correction of an overstatement in the
  specification, not an interpretive change; flagged to the user with the diff.)
- [x] **NK5. Text cells 4 and 6**: where 33 and 13 are quoted (Text cell 4 near "across the 33
  cells of Text cell 6"; Text cell 6's "both q criteria hold together in 33", "over the 33 cells",
  "13 cells"), one clause each: the counts are at K = 101, and Appendix A prints them at other K.
  No number changes.
- [x] **NK6. Outline, the warning and what is known** (NK-D1 answered):
  - **§4.3, the warning.** After the grid-refinement sentence: refinement converges in the tail,
    but a **lower bound on K is suspected** — below about K = 61–81 at Z = 6 the criteria stop
    tracking the fine grid — and it is **not established**, because what the coarse ladder shows
    cannot yet be told apart from node placement against θ_L. One sentence and a pointer to §5.5.
    §4.2's guard is **not** touched.
  - **§5.5 Limits, what is known**, a bullet beside the truncation bullet: the fine end (Part D
    unchanged to K = 1601; the plane counts move by a few boundary cells, 33 → 34–36 and 13 → 15,
    subset relation intact at every K); the coarse end (tracks the fine grid to K = 81, the first
    Part D flip at K = 61, alternation with node placement below, the smooth mask no cure); and the
    reading the evidence allows — a suspected floor for the evaluation's cut-based statistics, not
    a measured minimum for the model. Every number from NK1's printed block.
- [x] **NK7. Outline, the direction of future investigation**, closing §5.5's bullet (or §5.6 if
  the user prefers it among the predictions):
  1. **Separate placement from resolution**: hold θ_L on a Voronoi boundary at every K (or integrate
     the cell with exact partial weights), so that what remains of the degradation is the field's
     own resolution — the audit the user declined now, named as the next step.
  2. **State the minimum in the model's units**: spacing against the width of the cell of *all*
     (Z − θ_L), and against the scale's granularity n, since n fixes θ_L; whether the minimum K
     tracks n is the question the aligned grid could answer.
  3. **Give A21's representational cost a number**: K is the number of situation units, so a
     representational minimum would say how many units the field-valued choice needs — the cost
     §3's opening names in words.
  4. **Replace cut-based statistics where a smooth one exists**, so that the reported quantities
     inherit the convergence the fields have.
- [x] **NK8. Word budget**: §4.3, §5.5 (and §5.6 if used) raised; §§4–5 and Total re-summed;
  headings in step with the table (`agent/agent.md` §5.3's bookkeeping rule).
- [x] **NK9. Records**: I6 findings marked printed (class (e) → sourced); I10 finding (placement);
  E-register **E19** classing the new quantities (reported statistics; the smooth mask a control);
  `thesis_outline/revisions.md` §15 as the outline-side view; this record's findings log.
- [x] **NK10. Close**: C6 sweep over both notebooks and the outline; dangling-reference check;
  commit per task under §4.3; fold this record into `agent/history.md` when the user confirms.

**Order and gates.** NK-D1 is answered, so nothing waits on the user except the start. Code
before prose (§5.3): NK3–NK7 are written against NK2's executed output, never against the audit's.

## 5. Findings log

- **NK-F1 (NK1): seven plane cells move at the finer end, not five.** The audit's
  `plane_flips.py` checked q shift, q position and the two conjunctions only; the printed list adds
  (α 16, Λ 32) in mode position and (α 32, Λ 8) in mode shift. §2 above and I6's first finding
  said five; the outline quotes seven.
- **NK-F2 (NK1): the column that sorts the coarse rungs is the lower edge, not the first node.**
  The plan asked for the distance from θ_L to the first node inside the cell. That column is
  +0.056 on K = 101, 81 and 61 as well, which track the fine grid, so it does not separate
  anything. Under the trapezoidal weights the first node inside carries the interval down to the
  midpoint with the node below; that midpoint minus θ_L does sort the rungs (negative: q
  conjunction 33, 32, 29, 24, 9, 0 as it grows; +0.056: 32 to 39). Both columns are printed, and
  I6's "node at ζ = 3.0" account is corrected in a new finding there.
- **NK-F3 (NK1): at a fixed lower-edge offset, agreement still falls with the spacing** (q shift
  116 of 121 at K = 51, 76 at K = 7, all at +0.056). So placement does not account for all of the
  coarse end, and the ladder already separates the two in part. It still does not establish a
  bound: the offset is held only at one value, never at zero.
- **NK-F4 (NK6): the outline's §4.3 and §5.5 were drafted while NK2 ran**, from the prototype's
  output, whose code is identical to the cell's; every number is checked against the executed
  cell before commit.
- **NK-F5 (NK2): acceptance met.** main 0 errors, 8 figures; appendix_E 0 errors, 5 figures; 15/15;
  E3 PASS (223 identical / 1 changed / 4 inserted; 263). Against NK0 only Code Cell A's output
  changed, apart from Code Cell 2b's and E2b's machine-timing `cost:` lines. main was run a second
  time after NK-F6's fix; the diff between the two runs is the header lines alone.
- **NK-F6: the block's header and Appendix A cited Eq. (2) for the trapezoidal weights.** Eq. (2) is
  the quadrature inner product, and Text cell 3 §1 says only "fixed positive quadrature weights";
  the trapezoidal rule lives in Code Cell 1's `build_grid`. Both now cite `build_grid`.
- **NK-F7 (C6 sweep): two derived numbers replaced by printed ones.** "Within four cells of the
  floor" became the printed ranges (119–121 at the floor, 117–120 at K = 81), and "three statuses
  change at K = 61" became "only 33 of 36 agree". Every numeral in Appendix A's new paragraph is
  found in Code Cell A's output.
- **NK-F8 (NK5): the K = 101 clause went to the first quote of each count per text cell**, three
  sites (Text cell 4's band of 33; Text cell 6's 33 and 13), not all six, so as not to repeat it.
  The agent's scoping, named to the user.
- **NK-F9 (§4.3): the warning was placed after the refinement/half-width pair, and E3's sentence
  before it**, so that "the companion to that one" keeps its antecedent and E3's "every one of these
  numbers" does not appear to cover Code Cell A, which E3 does not replay.
