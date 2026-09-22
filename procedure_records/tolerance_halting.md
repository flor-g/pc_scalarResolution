# Halting by tolerance: can the realizable maximizer be defined that way?

Investigation opened by the user on 2026-09-21, while deciding where O3's settling-cost
discussion sits. **Nothing is implemented in the notebooks.** Audit:
`audits/2026-09-21-tolerance-halting/` (`tolerance_halting.py`, `output.txt`).

---

## 1. The user's proposal, verbatim (2026-09-21)

> halting is achieved by tolerance. Currently we have tolerance at 1e-9 (I think), which is an
> arbitrary small number. The need for tolerance for a computer program is because numbers cannot
> be represented exactly. The need for tolerance in a living organism might share the same reason or
> it might not, over which we will not make a claim. But we can make a plausible argument that the
> representative tolerance is almost certainly greater than 1e-9, thus giving an earlier halt. It is
> not within the scope of this study to stipulate the appropriate tolerance that is representative
> of the human brain, and tolerance might not even be uniform across different inference tasks. The
> stipulation that we will commit to in the paper is that tolerance is the mechanism of halt. I
> understand that our current implementation of the realizable maximizer is not defined in terms of
> tolerance, so before adopting my take, the first thing you should inspect is that if the notebook
> can define the realizable maximizers with tolerance and whether that breaks our standing
> predictions.

Two questions, then: **can it be defined that way**, and **does it break anything**.

---

## 2. What the notebook does today

- **The fast loop already halts on a tolerance.** `infer` stops when max|derivative| < 1e-9 for ten
  consecutive checks (decision I3), above the roundoff floor of about 3e-11 (F34).
- **The slow flow does not.** θ\* comes from Eq. (B2) in closed form, and the two "realizable" θ_u
  the evaluation reports are located by rules outside the network: `criterion_threshold` bisects
  fractions of θ\*, and `updates_to_criterion` stops the flow on Part C's criterion, a statistic of
  q against q_lit computed by the evaluator. This is exactly what R10 calls ad hoc, and why A9 keeps
  θ\* as the commitment.
- **The flow itself is Eq. (20):** θ ← θ + (τ_state/τ_θ)·g(θ), τ_θ = 20. A tolerance rule is
  therefore available without inventing machinery: **halt when |Δθ_u| < tol**, which uses only the
  size of the unit's own update.

---

## 3. Method

Eq. (20)'s gradient at the equilibrated fast subsystem is Code Cell 2's
`theta_u_gradient_at_equilibrium`, which re-solves Eqs. (15)–(16) per call — too slow for flows of
10⁶ updates over 121 cells. The audit rebuilds the same quantity from the configuration's fixed
pieces and checks it against the notebook's:

- agreement at θ_u = 0, 1, −5, 12.5: **0.0e+00, 2.8e-14, 5.8e-15, 0.0e+00**;
- the integrated gradient at θ_u = 0 is **−6.81865270**, the closed form's value exactly, and at
  θ\* it is **+0.00000000**, as Eq. (B2) requires;
- one update from 0 at Λ = 512 gives **7.816128**, **7.992595**, **13.374852**, the three values
  Code Cell 2b prints.

---

## 4. Findings

- **H1. It can be defined that way, and the definition is self-contained.** The rule needs only
  |Δθ_u|, which the flow produces anyway. Unlike both current rules it never mentions θ\*, so R10's
  objection — that every realizable θ_u is located using a closed form the simulated system has no
  access to — **does not apply to it**.

- **H2. No verdict moves, at either Λ.** Part D's rows at Λ = 512, over tolerances from 1e-9 to 1:
  the flat, Beta(3,1) and delta-like priors meet both criteria at every tolerance, the Gaussian and
  Beta(1,3) priors meet neither, exactly as at θ\*. At Λ = 8 no row meets the conjunction at any
  tolerance, as at θ\*.

- **H3. The plane is unchanged, cell by cell.** Both q criteria hold in **33 of 121** cells at every
  tolerance tested, and the halted verdict agrees with the θ\* verdict in **121 of 121** cells.

- **H4. The cost falls by two to three orders of magnitude.** The separation 4λ_max(H) that
  commitment 7 demands, at Λ = 512:

  | | θ\* | tol = 1e-2 | tol = 1e-1 | tol = 1 |
  |---|---:|---:|---:|---:|
  | flat | 9.26e6 | 6.72e4 | 1.50e4 | 1.19e4 |
  | Beta(3,1) | 8.99e6 | 6.75e4 | 1.51e4 | 1.09e4 |
  | delta-like | 7.93e6 | 8.98e4 | 2.02e4 | 4.82e3 |

  θ_halt/θ\* is 0.03 to 0.11 across those rows, and the reported quantities move in the third or
  fourth decimal: the delta-like row's shift is −0.5217 at θ\* and −0.5208 at tol = 1, with
  P(all | *some*) 0.4351 against 0.4361.

- **H5. The rule halts at a slow *start*, not only near the asymptote. Since 2026-09-21 this is a
  prediction of the commitment, not a hazard of it** (the user ruled out any guard; see §6). Under the
  flat prior at Λ = 8, where θ\* = 5950.63, the first update is tiny because ⟨μ_u, Σ_y c_y⟩ is small
  there, so any tolerance ≥ 1e-2 halts after **one update, at θ_u = 0.0005** — the tempered control
  in all but name. The verdict is unchanged (the conjunction fails at θ\* too), but the reported
  shift would be +0.0854 rather than +0.0295 — the tempering alone. The guards once considered here
  (a relative tolerance |Δθ| < tol·|θ|; halting only after the flow has left its start; a minimum
  number of updates) are **rejected**: each requires the system to know something about the shape of
  its own trajectory beyond its local input, which is the commitment's own premise. What the
  commitment predicts instead: **where the flow starts slowly, the system halts at once and the
  belief stays at the tempered control.** Under Λ = 8 that is the flat prior at every coarse
  tolerance tested.

- **H6. A fine tolerance never fires in any plausible number of exposures.** At 1e-9 and 1e-6 at
  Λ = 512 the flow is still at θ_u ≈ 600 after **2,000,000 updates**, against θ\* ≈ 1500. This is
  F15 again, and it is the measured form of the user's argument: a tolerance anywhere near 1e-9 does
  not halt the flow at all, so the halting regime is the coarse one, where 3 to 3,700 updates
  suffice.

- **H7. The fast loop's tolerance is not where the cost lives.** Coarsening `infer`'s tolerance from
  1e-9 to 1e-2 at Λ = 8 leaves every verdict unchanged, moves φ_S by at most 5.2e-3, and saves only
  513 → 152 Euler steps. So "tolerance halts the fast loop" is already true and costs nothing to
  say; the claim that does work is the one about the **slow** flow.

- **H8. WITHDRAWN 2026-09-21 by H9 — the cost columns below are wrong; do not quote them.** They
  price a row by scaling the *settling* step count and never price the *flow*, which is where the
  cost actually is once halting makes the flow long. The θ_halt and update columns are correct and
  are superseded in the more careful form of H10. Kept for the record of what was claimed.
  *(Original text:)* What a committed tolerance costs, measured 2026-09-21 (block 4 of the audit,
  added after the user chose to define `learn_theta_u` by the tolerance itself). Steps are scaled
  from Code Cell 2b's integrated delta-like row (39,035 steps at λ = 180.9), since dt = τ_state/(8λ):

  | tolerance | Λ = 512: θ_halt | updates | an integrated row | Λ = 8: θ_halt |
  |---|---|---|---|---|
  | 1 | 34.7 to 61.4 | 3 to 7 | **12 to 37 s** | −0.34, 0.0005, −0.42, 0.18 — one update everywhere |
  | 1e-1 | 61.1 to 71.1 | 3 to 173 | **27 to 50 s** | −5.29, 0.0005, −4.32, 5.51 |
  | 1e-2 | 129.2 to 149.9 | 3,023 to 3,657 | **166 to 223 s** | −10.59, 0.0005, −8.07, 11.46 |

  The notebook's whole baseline is about 250 s and Code Cell 2b integrates three such rows, so
  **1e-2 is not affordable** (about nine minutes for the three) while 1 and 1e-1 are (about 80 to
  110 s added). At Λ = 512 the halted θ_u of 35 to 71 sits far above the θ_crit of 1.0 to 3.1 at
  which the conjunction is first met, which is the measured form of "the conjunction is reached
  early": it is a fact about the shape of the update, not about where the flow stops.

- **H9. There is an INTEGRABILITY BOUNDARY just above λ = 1206, and H8's cost table is wrong**
  (measured 2026-09-21 at HA4b; `integrability_boundary.py`, `integrability_spectrum.py`,
  `integrability_output.txt`). One `infer` at Λ = 512:

  | θ_u | λ_max | steps | steps/λ | seconds |
  |---:|---:|---:|---:|---:|
  | 13.37 | 180.8 | 39,007 | 215.8 | 1.73 |
  | 34.70 | 1,206.1 | 264,724 | 219.5 | 11.64 |
  | 52.07 | 2,713.3 | 21,706,280 | **8000.0** | 945.50 |
  | 54.43 | 2,964.6 | 23,717,000 | **8000.0** | 1025.57 |
  | 61.27 | 3,756.0 | 30,048,104 | **8000.0** | 1305.24 |
  | 71.09 | 5,055.8 | 40,446,305 | **8000.0** | 1751.29 |

  `infer` sets `max_steps = ceil(max_time / dt)` with `max_time = 1000.0` and
  `dt = tau_state/(8λ)`, so the cap **is** 8000·λ. The four large rows hit it exactly and
  returned **`converged = False`**: they are failures, not expensive successes. Cost is *linear*
  in λ — 219·λ steps at a flat 45 µs/step — up to the boundary, and the integration simply stops
  converging within its time horizon above it. **It is not a condition-number effect**:
  λ_min = 1.00000 at every θ_u tested, so cond = λ_max, and the 219 → 8000 jump is not in the
  spectrum. Why 27 simulated time units suffice below the boundary and 1000 do not above it is
  **not diagnosed**; nothing may be written about the cause until it is.

  **Two corrections this forces.**
  1. **H8's table is withdrawn.** It priced a row by scaling Code Cell 2b's *settling* step count
     and never priced the *flow*, which under halting is 61–173 updates × 3 inferences climbing
     into the non-converging region. Its "12 to 37 s" and "27 to 50 s" are not what a halted row
     costs. H4's 4λ figures stand (they are closed-form) and H2/H3's verdicts stand.
  2. **`FEASIBLE_STIFFNESS` is not the pure machine budget the agent described to the user.** It
     sits just under the convergence boundary — 1206 converges, 2713 does not — so raising it past
     about 1.2e3 admits rows that fail, and the block's
     `RuntimeError("the arrival theta_u was expected to be integrable")` fires. The user's approval
     to raise it was given on the agent's wrong description and **was not acted on**; the point was
     put back to them.

- **H10. What survives at Λ = 512, measured.** The conjunction holds at **every** halted θ_u at
  both tolerances, and the criteria barely move: flat's shift −0.0119 at today's arrival against
  −0.0145 halted; delta-like −0.5182 against −0.5213, with θ\*'s −0.5217. So halting costs no
  verdict (H2 confirmed against the real implementation). Of the three rows, only
  **delta (all) at tol = 1** (θ_u = 34.70, λ = 1206, 11.6 s) is inside the integrability boundary;
  flat (54.43) and skewed high (52.07) at tol = 1 are outside, as are all three at tol = 1e-1.

---

## 5. What this opens, for the user

Adopting the proposal touches an interpretive commitment, so under `agent.md` §5.4 it is the user's.

- **A9 and R10.** Today θ\* is the commitment *because* no self-contained halting rule existed. H1
  removes that reason. Three positions are available, and they differ in what the paper reports:
  1. **θ\* stays the commitment; tolerance explains why a real system stops earlier.** Every
     published number stands, and the cost objection is answered by H4 rather than by recomputation.
  2. **The halted θ_u becomes the commitment.** Then the reported configuration is a function of a
     tolerance the study declines to fix, and every table would carry that dependence — though by
     H2–H4 the verdicts and most digits survive.
  3. **Both, explicitly:** θ\* as the asymptote the model commits to, the tolerance-halted θ_u as
     what any realization reaches, with H2–H4 as the evidence that the two agree on every verdict.
- **The guard of H5** must be chosen if any rule is written into a cell.
- **Where the discussion sits** (the question O3 was opened for): the material is now measured, so
  §5.3's argument can rest on H2–H4 rather than on an appeal.

---

## 6. Status

**2026-09-21: the user took position 1** — θ\* stays the commitment, the mechanism is tolerance, and
the tolerance is ad hoc, so nothing reported may depend on it. Recorded as `decisions.md` **A19**
and `revisions.md` **R22**; A9 and R10 are unchanged, which is the point of the position. The user's
scope line: *"besides changing the notebook codes for halt and the halting description, we don't
need to change anything else"*.

**2026-09-21, second decision by the user, which answers Q-HA1 and Q-HA2 and rules out the guard:**

> If we commit to defining halt in terms of coarse tolerance, we should define learn_theta_u as what
> we commit to and report all realizable theta in terms of that. The fact that the conjunction is
> reached early can be stated in prose as a fact about the shape of update. Moreover, if we do
> commit to tolerance as what halting depends on, a guard would be UNACCEPTABLE; implementing a
> guard would be essentially ungraceful patchwork to save an incorrect theory; in particular, a
> guard violates our fundamental commitment that a system is agnostic to the close form or the shape
> of the update beyond its local input. That being said, if we commit to tolerance as halt, then
> that commitment predicts early halting for slow start; the implications of this commitment should
> be clearly stated as such.

So: **Q-HA1 = the committed tolerance**, not an argument passed where convenient; **Q-HA2 = every
realizable θ_u is the tolerance-halted one**, and the two rules that locate today's (the evaluator's
criterion, and bisection on fractions of θ\*) stop being how a realizable θ_u is defined. **No
guard**, on the principle that a guard needs knowledge of the trajectory's shape that the system
does not have. **The slow-start halt is therefore a prediction and is stated as one** (H5).

**2026-09-21, the position in six points (`decisions.md` A19).** Halting depends on tolerance only,
with no guard; no tolerance is committed to, and 1e-1 is offered as an ad hoc demonstration value;
the two early-halt implications are stated at their measured boundaries (block 5: the flat row at
Λ = 8 from 1e-3, every Part D prior at Λ = 8 from 1); the fast loop keeps 1e-9 and no argument is
spent on it; and predictions are reported in closed form.

**Two corrections the measurement forced, both told to the user.** Their point 3 said "above 1e-2":
the flat row is already stuck at θ_u = 0.0005 from **1e-3**, an order of magnitude finer. Their
point 4 said "above 1": all four priors halt in one update **at 1**, and Beta(3,1) at 3e-1. Neither
correction changes the position; both change where its boundary is drawn.

**What still divides the reported from the demonstrated.** A19's third part stands: the paper's
results are at θ\*, which is what keeps them independent of the ad hoc tolerance. What the tolerance
now fixes is the **realizable** rows — demonstrations that the dynamics reach the verdict — and they
carry the tolerance's value on their face. Tasks below; **nothing is implemented**.

---

## 7. Tasks (HA0–HA8), and the two questions that blocked them

**Both are answered by the user's second decision (§6), and both were answered *against* the
agent's recommendation.** The options are kept below as the record of what was not chosen; the
answers are what HA1 and HA4 implement. Corrected 2026-09-21 at HA0, because the list still carried
the pre-decision wording.

- **Q-HA1. How does `learn_theta_u` halt? — ANSWERED: by the committed tolerance.** Today it runs a
  fixed `num_updates` and stops there, which is the arbitrary cap A19 replaces. The user: *"we
  should define learn_theta_u as what we commit to"*. So the flow halts when |Δθ_u| < tol, and
  `num_updates` becomes a cap that reports when it is hit rather than a stopping rule. **Not**
  option (i) below, which the user overrode.
  - ~~**(i) (agent's recommendation, overridden) The tolerance is an explicit argument with no
    default**~~, `num_updates` kept as a guard, call sites passing a tolerance only where a halt is
    demonstrated, **no stored output moving**. Overridden because it leaves the committed mechanism
    out of the definition of the thing the paper commits to.
  - ~~**(ii) A default tolerance**~~, in the form first put — a silent default — is also not what
    was chosen. What is chosen is the same mechanically but not rhetorically: the tolerance is the
    halting rule, its value is ad hoc and **labelled as such at every call site and in every caption
    that reports a row halted by it** (A19 point 2, demonstration value 1e-1).
  - **Consequence, which the earlier wording denied: stored output moves.** Every existing call to
    the flow now halts by the tolerance, so the SLOW PARAMETER block's "0.0000 → −7.567163 over 60
    updates" line changes, and HA6's acceptance can no longer be "the baseline, unchanged".
- **Q-HA2. What happens to the two "realizable" θ_u the evaluation already reports** — the
  criterion-stopped one-update rows (7.8161, 7.9926, 13.3749) and `criterion_threshold`'s bisection
  on fractions of θ\*? **ANSWERED: option (ii), recompute at the tolerance.** The user: *"report all
  realizable theta in terms of that. The fact that the conjunction is reached early can be stated in
  prose as a fact about the shape of update."* So the evaluator's criterion and the bisection stop
  being how a realizable θ_u is **defined**; what they showed — that the conjunction is met early in
  the flow — is stated in prose instead, on H8's measured form (θ_halt of 35 to 71 at Λ = 512 sits
  far above the θ_crit of 1.0 to 3.1).
  - ~~**(i) (agent's recommendation, overridden) Keep both, relabelled.**~~ Overridden: a
    demonstration located by a rule the model does not own is not a realizable θ_u under A19.
  - **(ii) Recompute them at a tolerance. — CHOSEN.** The earlier note that A19's third part
    rejects this was wrong, and is corrected in §6: A19 puts the **predictions** in closed form at
    θ\*, which is what keeps them tolerance-free, while a **realizable** row is by definition the
    one the dynamics reach and so carries the tolerance on its face.
  - ~~**(iii) Drop them.**~~ Not chosen; §4.6's evidence and Text cell 4's demonstration are kept,
    recomputed.

**Tasks.**

- [x] **HA0. Checkpoint** (`agent.md` §4.2), before any code cell is touched. **Clean tree,
      `f07db5d`** (2026-09-21). No uncommitted work of the user's was present, so §4.2 step 2
      applies and the current commit is the checkpoint; no `backups/` folder is needed, since every
      file this change touches is tracked.
- [x] **HA1. `code cell 1`, `learn_theta_u`** under Q-HA1 — done 2026-09-21, commit recorded below.
      The rule: `step = (tau_state/tau_theta)*gradient`, applied, then `abs(step) < tolerance`
      halts. `tolerance` is **keyword-only with no default**, so no run can inherit an ad hoc value
      silently (A19 point 2) and every call site must name the value it is demonstrating at.
      `num_updates` becomes a cap that **raises `RuntimeError`** when reached — the user's
      instruction of 2026-09-21: *"when it is hit it should raise a runtime error. If any of our
      cases ended up incurring a runtime error, then we need to report it as such."* Two guards
      added (`tolerance <= 0`, `num_updates < 1`), both `ValueError`, neither about the
      trajectory's shape. The docstring gains three paragraphs: the rule and that it reads only the
      unit's own last step, the ad hoc status of the value with θ\* as the tolerance-free
      prediction, and the cap's meaning.
      **Coupling 9 holds**: the two definitions were already byte-identical here (the relay lives
      in `theta_u_gradient`, not in this def), so the same four replacements were applied to E1's
      own copy, and the two are verified source-identical after the edit.
      **Verified** against block 5 by integrating the real flow (not the audit's rebuild) through
      the edited cell: at Λ = 8, flat halts after 1 update at θ_u = **+0.000495** at both 1e-1 and
      1, gaussian after 1 update at **−0.340933** at 1 — the audit's 0.0005 and −0.3409. The cap
      raises with the last step's size, the tolerance and θ_u in the message; omitting `tolerance`
      is a `TypeError`.
      **Consequence carried to HA4:** the eight call sites (four per notebook) now fail with a
      `TypeError` until they name a tolerance, so **neither notebook executes between HA1 and
      HA4.** This is deliberate — a default would have hidden exactly the quantity A19 refuses to
      commit to — and it is why HA1's commit says `Verified: not run`.
- [x] **HA2. `infer`'s docstring and I3** — done 2026-09-21. **The task as written is void**: it
      said the 1e-9 "keeps its value" and "no behaviour changes", which H12 refuted. What was done:
      `infer`'s docstring in both notebooks carries the floor law and the keyed tolerance;
      `decisions.md` **I3 is rewritten** as `DERIVATIVE_TOLERANCE_PER_RATE x lambda_max(H)`, keeping
      its 2026-09-13 reasoning as the *reason for* the revision rather than against it, and noting
      that its old claim of "two orders inside the checks' 1e-8" was one order even then;
      `decisions.md` **A19 point 5 is revised** — the fast loop's tolerance is *not* inconsequential,
      H7 having been measured at Λ = 8 where the question does not arise; **F34 is annotated** in
      `theta_u_learned_reach.md` to say its 8.2e-11–1.6e-10 band is the floor *at that θ_u* and the
      law is 4.547e-13·λ_max(H), so F34's conclusion generalizes while the single fixed tolerance it
      licensed does not; and **`agent.md` §5.2's rule** now states that the floor scales, so the
      tolerance does, and that any threshold bounding a tolerance-linked quantity is expressed in
      multiples of the tolerance rather than as a constant.
- [x] **HA3. Text cell 3 §8.5** — done 2026-09-21. Three paragraphs replace the old one, whose
      stated reason for not reaching θ\* was "a run of the length the evaluation can afford" — the
      pre-A19 framing, in which a fixed update count was the stopping rule. Now: **how the flow
      stops** (|Δθ_u| < tol, the only rule, reading the unit's own last step and nothing about the
      trajectory; the fast subsystem stopping the same way at its own timescale, with a tolerance
      scaling as λ_max(H)); **the value is ad hoc and what is reported does not use it** (θ\* as the
      asymptote carrying no tolerance, a flow-derived θ_u labelled realizable and carrying its
      tolerance on its face); and **two consequences stated as consequences** — a plausible
      tolerance halts well short of θ\*, and a slow start halts at once at the tempered control.
      Per B10/C7 the cell takes no position on whether a living system needs a tolerance for the
      reason a floating-point computation does; it says only that this study does not fix one.
- [ ] **HA4. Appendix B and Text cell 4's realizability block**: the recomputation Q-HA2 settles.
      Every realizable θ_u is the tolerance-halted one, reported at the demonstration tolerance and
      labelled with it; the fact that the conjunction is met well before the halt moves into prose,
      on H8's numbers. C6 applies — each quoted number is printed by the cell that reports it.
  - [x] **HA4a. Call sites 1 and 2**, done 2026-09-21, commit recorded below. Code Cell 2 gains two
        named constants beside `FEASIBLE_STIFFNESS`: `DEMONSTRATION_TOLERANCE = 1.0e-1`, commented
        as ad hoc and named once so every row halted by it prints it, and `HALTING_CAP = 100_000`,
        commented as a cap and not a stopping rule. **Site 1**, `check_specification`'s
        "Eq. (20) ascends toward it from theta_u = 0": was 25 fixed updates, now halts at the
        demonstration tolerance after **15 updates at θ_u = −5.285227** (default Λ = 8,
        θ\* = −28.4375), F~ monotone, |grad| 6.82 → 2.00. **Site 2**,
        `theta_u_learning_probe`: `num_updates=60` is replaced by `tolerance`, defaulting to the
        named constant **which the block now prints**, so the ad hoc value is never invisible; the
        SLOW PARAMETER line becomes "0.0000 → −5.285227, halted after 15 update(s)" in place of
        "over 60 updates", and the settled/still-ascending clause becomes the halting relation (the
        final gradient −1.997 gives a step of 0.0999, just under 0.1).
        **Both sites got cheaper**, 15 updates against 25 and 60.
        **One dependence to keep visible:** site 1's clause that |grad| shrinks needs two updates,
        so a tolerance coarse enough to halt after one (≥ 1 at Λ = 8, block 5) makes that check
        **fail** rather than pass vacuously. That is deliberate and is commented in the cell — a
        silent weakening would have been the patchwork the user ruled out.
  - [x] **HA4b. Call sites 3 and 4**, done 2026-09-21, commit `d8c93ef`. New helper
        `halt_by_tolerance` applies `learn_theta_u`'s rule at the closed-form equilibrium, so the
        survey stays affordable; the end-to-end run integrates the flow and lands on it to better
        than **1e-13**. The realizability block is now **two tables** — where the flow halts (the
        realizable θ_u) and where the conjunction is first met, the second labelled in the OUTPUT
        as a fact about the shape of the update and not a halting rule. `DEMONSTRATION_TOLERANCE`
        is keyed to Λ, `{8.0: 1e-1, 512.0: 1}`, strict (an unlisted Λ raises).
        `FEASIBLE_STIFFNESS` 1.0e3 → **1.3e3**, just above 1206. The H11 cost line is replaced by
        `infer`'s own cap as a lower bound. The roundoff-floor block's leftover `arrival` reference
        (a `NameError`) is fixed to the halted θ_u.
        **Measured:** Λ = 8 block 0.0 s; Λ = 512 block **377.5 s**, of which the 7 integrated
        updates of the flow are 149 s and the settle 11.7 s — so **the flow, not the settling, is
        where the time goes**, which is exactly the assumption H8 got backwards. At Λ = 512 only
        `delta (all)` is inside the gate; `flat` and `skewed high` print the not-run-end-to-end
        line with their λ and the reason.
  - [x] **HA4c. The prose half**, done 2026-09-21. Written AFTER execution, not before: the
        passages carry ~25 numbers that the tolerance change moves, and C6 makes a number class (e)
        until a cell prints it, so writing them from the audit first would have been two passes and
        four C6 violations. **Appendix B**: the 60-update run to θ_u = −7.567 and "an integration of
        affordable length does not arrive" are replaced by the halt (15 updates, θ_u = −5.285227,
        gradient −1.997) and the division of labour — θ\* the tolerance-free asymptote, a
        flow-derived θ_u *realizable* and carrying its tolerance. **Text cell 4**: the tolerance
        paragraphs ("made badly at first" → "got wrong twice, in the same way"); the gate as a
        wall-clock budget at 3e3, with every Λ = 512 row integrated at its halt though none at θ\*;
        and the end-to-end rows as halts (54.429, 52.065, 34.695 after 3, 3, 7 updates) with the
        conjunction's early arrival moved into its own sentence as a fact about the shape of the
        update. 4λ now quoted at three scales: 12–46 at the thresholds, 4.8e3–1.5e4 at the halts,
        7.9e6–9.3e6 at θ\*.
        **A C6 violation in the agent's own first draft, caught and fixed:** it quoted the floor
        coefficient, the old tolerance's margins, the 31-step drift and the crossing λ, all from the
        audit. Rather than trim the argument, the floor block now **prints** the coefficient
        (4.547e-13, 4.547e-13, 4.548e-13 at three λ) and the counterfactual — what a fixed 1e-9
        would have bought there (0.74, 0.81, 1.82 floors, the first two **below** the floor) and the
        λ at which it equals the floor (2199). The notebook now justifies its own tolerance rule.
- [x] **HA5. Couplings and numbering** — done 2026-09-21. Coupling 5 quiet (no equation tag added
      or moved); 6 quiet (no anchor added; Text cell 3's `tc3-8-5` anchors verified intact);
      **coupling 9 verified by AST**: `learn_theta_u`, `halt_by_tolerance` and
      `demonstration_tolerance` are source-identical across main and E1/E2, and all five new
      constants are present in both. `infer` differs, **correctly** — E1's carries the relay — and a
      line-by-line diff confirms the difference is the relay, the spectral guard and pre-existing
      formatting, while the three tolerance lines are identical. **E3 PASS on both cells.** ToC
      untouched: no heading moved.
- [x] **HA6. Executed** 2026-09-21 (`agent.md` §5.1), main twice (the second time to print the
      floor coefficient the prose needed). **main: 0 errors, 8 figures, 14/14, 1154 s.
      appendix_E: 0 errors, 5 figures, 18/18, E3 PASS on both cells, 2516 s.**
      **Departures from the recorded baseline, reported not explained away.** Runtime: 250 s → 1154 s
      and 710 s → 2516 s, because three Λ = 512 rows are integrated end to end where one was, and
      the flow itself is now integrated to its halt (the flat row: 80.6 s of flow against 26.4 s of
      settling). E3's counts move because the cells print more lines — Code Cell 2 goes 203 → **221**
      identical and Code Cell 2b 234 → **261**, while the *pattern* the baseline records is
      unchanged: 1 changed (the pass count) and 4 inserted (the checks the relay adds) in Code Cell
      2, nothing at all in 2b. Step counts fall everywhere the tolerance coarsens: an inference at
      θ_u\* takes **138,390–138,398** steps against 148,081–148,104, about 6.5% fewer.
      **C6 swept over every markdown cell of both notebooks.** Three numbers were stale *because of
      this change* — φ_u\* at the realizable θ_u ([+71.1166,−39.1606] → **[+27.6730,−15.2423]**),
      φ_S\*'s extremes there (139.18/−852.64 → **140.50/−856.51**), and the θ_u\* step count — all
      three fixed. **Eight pre-existing C6 violations were found and are NOT this change's**: cell
      10's 0.2122 and cell 12's 0.0095, 0.0445, 0.1512, 0.5477, 4096, 0.0002 and 13378, identical
      before and after. Reported to the user; not touched here.
- [ ] **HA7. The outline.** §5.3 (planned) states the halting account and rests its cost argument on
      H2–H4; §5.5 Limits and §3.4 carry a clause if HA3 introduces notation they use. `revisions.md`
      R22's site entries.
- [ ] **HA8. Commit**, one logical change per commit, hashes recorded above.

**What stays untouched, by the user's scope line:** A9, R10, the θ\* tables, the plane, and
§§4.1–4.5. The audit's H2–H4 are evidence for the discussion, not new results to print, and they
stay class (e) unless a cell is later asked to print them.

**Corrected at HA0:** this paragraph used to begin "every reported number", which Q-HA2's answer
makes false. The realizable rows move, because they are now defined by the tolerance. What the scope
line protects is everything the paper reports **as a prediction** — and those are at θ\*.

---

## 8. HA4b: the open question (2026-09-21)

**Blocking the conversion of call sites 3 and 4.** H9 and H10 are measured; what to do about them
is the user's.

- **The integrability boundary is real and sits between λ = 1206 and λ = 2713.** Above it `infer`
  exhausts `max_time` and returns `converged = False`. Nothing in the model changes; what changes
  is which θ_u the notebook can *exhibit* by integration.
- **At tol = 1, one of the three Λ = 512 rows survives it** (delta (all), θ_u = 34.70, λ = 1206,
  11.6 s). The other two would print the existing "is not run end to end" line with the reason,
  which is an honest report and costs nothing.
- **At tol = 1e-1 none survives it**, so the end-to-end block would report nothing at Λ = 512.
- **The user's proposal (2026-09-21): tolerance is a function of the case's Λ**, with 1e-1 at
  Λ = 8 and 1 at Λ = 512 as ad hoc demonstration values, the hypothesis to be stated in the
  outline. **The premise the user was given for it — that cost is super-linear in λ — was the
  agent's error and is withdrawn (H9).** The hypothesis keeps independent, measured support: a
  *fixed* absolute tolerance buys very different amounts of flow at different Λ (15 updates at
  Λ = 8 against 61–173 at Λ = 512 for the same 1e-1), because the gradient's scale grows with Λ.
  If the hypothesis is stated, it must rest on that and **not** on the withdrawn cost claim.
- **Note for whoever writes it:** a tolerance keyed to Λ is *not* the relative tolerance
  |Δθ| < tol·|θ| that H5 rejects as a guard. Λ is a standing property of the configuration, fixed
  before the flow starts; |θ| is where the trajectory currently is. The first is a stipulation
  about the case, the second is the system reading its own trajectory, which is what the user
  ruled out. The outline should draw that line explicitly, or the two will be confused.
- **Not diagnosed:** why the settling time crosses from ~27 to >1000 simulated time units. No
  claim about the cause goes anywhere until it is.

- **H11. The printed cost extrapolation to θ\* is unsupported above the boundary** (2026-09-21).
  Code Cell 2b prints, for each end-to-end row, *"the same inference at theta_u\* = 1521.5 would be
  4.99e+08 steps, about 6.3 h"* (and 4.85e8 / 6.1 h, 4.28e8 / 5.5 h). That number is
  `steps_per_rate * star_rate`, i.e. the **linear** 219·λ model, extrapolated from λ ≈ 1.8e2 to
  λ ≈ 2.3e6 — four orders of magnitude, across the boundary H9 measures at λ ≈ 2e3, above which the
  integration does not converge at all. At θ\* the step cap alone is 8000·λ ≈ 1.85e10 steps, about
  230 h, and the run would end at the cap rather than at a fixed point.
  **The direction of the claim is unharmed and in fact strengthened** — θ\* is further out of reach
  than the notebook says, not nearer — so §4.6's argument and the outline's line (`revisions.md`
  line 449: "4.28e8 steps, hours, at a separation of 7.9e6") survive in substance. But the *number*
  is a linear extrapolation through a regime change and may not be printed as a measurement. Either
  it is replaced by the cap (a lower bound on the steps, with non-convergence stated) or the claim
  is made qualitatively. **Not yet changed**; it is part of HA4b.

- **H12. The convergence boundary is DIAGNOSED: a roundoff floor that grows as θ_u², against a
  fixed stopping tolerance** (2026-09-21, `why_it_stops_converging.py`,
  `why_it_stops_converging_output.txt`). It is **neither** of the two candidates named when H9 was
  recorded — not a slow mode of the dynamics, and not an instability of explicit Euler.

  **The dynamics settle just as fast on both sides of it.** max|derivative| decays exponentially at
  rate ≈ 1 per simulated time unit (the rate λ_min = 1 predicts) and reaches its floor by t ≈ 37 at
  either θ_u, then sits there unchanged to t = 166:

  | | θ_u = 34.70 (λ = 1206) | θ_u = 52.07 (λ = 2713) |
  |---|---|---|
  | t ≈ 10 | 1.668e-2 | 5.277e-2 |
  | t ≈ 20 | 5.254e-7 | 5.276e-2 → 5.254e-6 at t = 18 |
  | t ≈ 37–41 | **5.484e-10** | **1.234e-9** |
  | t ≈ 74–166 | 5.484e-10 (unchanged) | 1.234e-9 (unchanged) |

  **What differs is only the floor's height**, and the floor is a clean square law in θ_u:

  | θ_u | 13.37 | 20.00 | 34.70 | 42.00 | 46.90 | 52.07 | 61.27 |
  |---|---|---|---|---|---|---|---|
  | floor | 8.220e-11 | 1.828e-10 | 5.484e-10 | 8.031e-10 | 1.001e-9 | 1.234e-9 | 1.708e-9 |
  | /θ_u² | 4.598e-13 | 4.570e-13 | 4.555e-13 | 4.553e-13 | 4.551e-13 | 4.551e-13 | 4.550e-13 |
  | converges | yes | yes | yes | yes | **no** | no | no |

  **floor = 4.55e-13 · θ_u²**, constant to three figures over a 4.6-fold range, crossing the 1e-9
  tolerance at **θ_u = 46.6, λ = 2177** — with 42.00 the last success measured and 46.90 the first
  failure. Above the crossing the derivative can never fall below the tolerance, so the test cannot
  fire however long the run, and it ends at the cap.

  **Why quadratic:** θ_u enters the roundoff twice — the residuals carry it, and `phi_u_dot`
  multiplies the state error by it again (`-eps_utility + theta * project(eps_state)`).
  max|φ_S| ≈ 856 at *both* θ_u, so this is **not** the state growing.

  **What it means.** The boundary is a property of **the stopping tolerance**, not of the model, the
  integrator, or the machine's speed. I3 set 1e-9 above the roundoff floor measured at the θ_u of
  the time (F34: 8e-11 to 1.6e-10 — consistent with this law at θ_u ≈ 13–19). **The principle was
  right; the constant does not travel.** Applying I3's own principle consistently — a tolerance that
  sits above the floor at the θ_u actually being integrated — would restore convergence at every
  θ_u the halting flow reaches, and would let all three Λ = 512 rows run end to end instead of one.
  **That is a change to I3 and is the user's**; see §9.

---

## 9. The decision H12 opens, for the user (2026-09-21)

**`infer`'s stopping tolerance is not inconsequential after all.** A19's point 5 reads: *"it is not
imperative that the fast loop has the same tolerance as the slow loop, and coarsening the tolerance
does not affect runtime or result by much, so we leave discussions on fast loop tolerance since it
is inconsequential; the implementation takes 1e-9."* That rested on **H7**, which coarsened the
fast tolerance at **Λ = 8** and found nothing moved. H12 shows the opposite at the θ_u the halting
flow reaches at **Λ = 512**: the fixed 1e-9 is precisely what makes those configurations
non-integrable, and so decides which realizable θ_u can be **exhibited** at all. H7 is not wrong;
it was measured where the floor is far below the tolerance.

**The striking parallel, worth the paper's notice.** The user's own hypothesis for the *slow* loop
— that a case's representative tolerance scales with its Λ (R23) — has an exact analogue here for
the *fast* loop: a fixed absolute tolerance is not scale-free, and 1e-9 means something different
at θ_u = 13 than at θ_u = 52. The same observation at both timescales.

**Options.**

1. **Leave I3 at 1e-9.** One of three Λ = 512 rows runs end to end (`delta (all)`); the other two
   report why not. Honest, cheap, and already implemented. The cost is that the end-to-end
   demonstration is thinner than it was.
2. **Scale the fast tolerance with the floor**, e.g. `derivative_tolerance = max(1e-9, k·θ_u²)`
   with k a few multiples of 4.55e-13. This *implements I3's stated principle* — sit above the
   roundoff floor — rather than overriding it, and restores convergence at every θ_u the flow
   reaches. It changes stored step counts wherever θ_u is large, and F34's numbers need restating
   as a law rather than a band.
3. **Scale it, but only where 1e-9 is unreachable**, which is option 2 with the `max` doing the
   work; identical below θ_u = 46.6, so no existing printed step count moves.

**Not decided, and nothing about integrability goes in the paper until it is.** Option 3 looks to
the agent like the one that changes least while being correct, but I3 is a standing decision and
the choice is the user's.

- **H13. The floor tracks λ_max(H), not θ_u², and that is what makes a scaled tolerance legitimate**
  (2026-09-21, after the user asked *which* θ_u the agent's recommendation meant).

  **The user's objection.** A tolerance defined in terms of the **closed-form θ\*** would be
  illegitimate: unlike Λ, θ\* is agnostic to the system — the network has no access to it, which is
  R10's standing objection and the reason A9 keeps it as a commitment rather than a mechanism. The
  agent's recommendation meant the **current** θ_u, the value the utility unit holds, which is
  constant within one inference by the two-timescale commitment. But checking the variable showed
  θ_u was the wrong one anyway:

  | | floor/θ_u² | floor/λ_max(H) |
  |---|---|---|
  | spread, θ_u = 13.37 → 61.27 | 1.0107× | **1.0003×** |

  **floor = 4.547e-13 · λ_max(H)**, flat to four significant figures. θ_u² only appeared clean
  because λ_max = 1/σ_u + θ_u²·λ_max(G)/σ_S is nearly quadratic in θ_u at these magnitudes. The
  mechanism is arithmetic, not fitted: **floor ≈ 2.4 · ε · |φ_S| · λ_max** with ε = 2.22e-16 and
  max|φ_S| ≈ 856 — a derivative is a rate times a state error, the state error sits at machine
  precision relative to the state, and the stiffest rate is λ_max.

  **Why λ_max answers the objection.** It is computed from the network's own weights, basis, σ's and
  current θ_u; `fast_time_constant` **already computes it** to set τ_error and dt; and the
  architecture **already requires the system to have it**, since D4's standing commitment is
  τ_error ≤ τ_state / (4 λ_max(H)). If keying a tolerance to λ_max were system-agnostic, D4 would be
  too, and the two-timescale argument with it.

  **The one asymmetry to state, not bury.** Within an inference θ_u is fixed, so this is a standing
  property and not a reading of the trajectory. Across the slow flow θ_u changes, so the fast
  tolerance would change from update to update — which is already true of `dt` and `tau_error`, and
  for the same reason.

  So §9's option 2 is restated: **`derivative_tolerance = max(1e-9, k·λ_max(H))`**, k a few
  multiples of 4.55e-13. Below θ_u ≈ 46.6 the `max` returns 1e-9 and **no printed step count moves**.
  Still the user's decision (I3).

- **H14. AUDIT of `derivative_tolerance = k·λ_max(H)`** (2026-09-21, `scaled_fast_tolerance.py`,
  `scaled_fast_tolerance_output.txt`), run at the user's request. Margin = k / 4.547e-13 is how far
  above the roundoff floor the test sits; today's 1e-9 is a margin of **12.2 at λ = 180.8** and
  **1.8 at λ = 1206**, which is the whole problem — the margin shrinks as λ grows and vanishes at
  λ = 2177.

  **1. It converges everywhere, including where 1e-9 cannot.** θ_u = 52.07 and 61.27 run to the cap
  today; at every k tested they converge.

  **2. Cost stays linear and is slightly cheaper.** Steps per unit λ: 216–220 today, **181–224**
  across all k and θ_u. Nothing blows up.

  **3. The fixed point is as accurate as the tolerance**, which is the real trade. At k = 5.5e-12:
  |φ_S − φ_S\*| runs 1.6e-10 (θ_u = 5.29) to 2.1e-8 (θ_u = 61.27), against 9.5e-10 to 1.0e-9 today
  where today works at all. Still four orders below anything reported (results carry 4 decimals).

  **4. Reproducibility IMPROVES — the opposite of the expected risk.** F34's pathology is a
  tolerance inside the roundoff band making the stopping step depend on which roundoff-level sample
  lands below it. Nudging θ_u by one part in 1e15:

  | θ_u | 1e-9 (today) | k = 2.0e-12 | k = 5.5e-12 | k = 2.0e-11 |
  |---|---|---|---|---|
  | 34.70 | **31 steps** | 1 | **0** | **0** |
  | 13.37 | −1 | 1 | **0** | **0** |

  Today's fixed tolerance is *already* drifting at θ_u = 34.70, where its margin is down to 1.8.
  The scaled rule holds the margin constant and the drift goes to zero. **I3's own goal is better
  served by the scaled rule than by the constant it chose.**

  **5. What constrains k from above: Part A.** `check_specification` asserts
  `max(worst_state, worst_utility) < 1e-8` and `worst_dense < 1e-8` for integrated-against-closed-form
  agreement. Since the gap equals the tolerance, at the default net's θ_u\* = −28.44 (λ = 810.8):

  | k | margin | tolerance there | gap | against Part A's 1e-8 |
  |---|---|---|---|---|
  | 2.0e-12 | 4.4 | 1.62e-9 | 1.6e-9 | passes, 6× headroom, but 1-step drift |
  | **5.5e-12** | **12.1** | **4.46e-9** | **4.5e-9** | **passes, 2.2× headroom, no drift** |
  | 2.0e-11 | 44.0 | 1.62e-8 | 1.6e-8 | **FAILS** |

  **6. Every stored step count moves**, in both directions — at Λ = 8, θ_u = 5.29 the scaled rule is
  *stricter* than 1e-9 (margin 73 today) and takes 5,879 steps against 5,450. So this is a full
  re-execution of both notebooks, not a localized change.

  **Recommendation: k = 5.5e-12**, because it is not a new choice — it is *today's margin at the
  θ_u I3 was calibrated at*, made scale-free. **One caveat to carry:** Part A's own 1e-8 thresholds
  are then fixed constants sitting above a gap that scales with λ, which is the same mistake one
  level up. If the rule is adopted, those thresholds should scale too, or the headroom will shrink
  again as soon as a larger θ_u is integrated.

- **H15. THE SWEEP: which fixed thresholds are brittle** (2026-09-21, `threshold_sweep.py`,
  `threshold_sweep_output.txt`), at the user's request. 43 small numeric thresholds were extracted
  from both notebooks' code cells and each classified by whether the quantity it bounds scales with
  λ_max(H) or θ_u. Measured at k = 5.5e-12:

  | net | θ_u | λ | tol | \|φ−φ\*\| | Eq17 id_1 | Eq17 id_2 | \|1−q mass\| | min dF step |
  |---|---|---|---|---|---|---|---|---|
  | Λ=8 | 5.29 | 30.0 | 1.65e-10 | 1.57e-10 | 1.57e-10 | 3.28e-11 | 2.22e-16 | −2.3e-13 |
  | Λ=8 | 28.44 | 810.8 | 4.46e-09 | 4.45e-09 | 4.45e-09 | 1.73e-10 | 2.22e-16 | −1.7e-13 |
  | Λ=512 | 13.37 | 180.8 | 9.94e-10 | 9.89e-10 | 9.88e-10 | 8.95e-11 | 2.22e-16 | — |
  | Λ=512 | 34.70 | 1206.1 | 6.63e-09 | 6.64e-09 | 6.63e-09 | 2.22e-10 | 2.22e-16 | — |
  | Λ=512 | 52.07 | 2713.3 | 1.49e-08 | **1.49e-08** | **1.49e-08** | 3.41e-10 | 1.11e-16 | — |

  **BRITTLE — two quantities, three assertions.** `|φ − φ*|` and Eq. (17)'s first identity both
  track the tolerance to within 1% (ratio 0.95–1.00), so both scale as k·λ_max while their
  thresholds are a fixed **1e-8**:
  - `max(worst_state, worst_utility) < 1e-8` — "fixed point matches Eqs. (15)-(16)";
  - `worst_identity_1 < 1e-8` — "Eq. (17) eps_S = -eps_L";
  - `worst_dense < 1e-8` — the dense-scale variant of the first.

  **They already fail at θ_u = 52.07**, where the gap is 1.49e-8. Part A passes today only because
  it runs at the default net's θ_u\* = −28.44 (λ = 810.8), gap 4.45e-9, **2.2× headroom**. The
  break-even is λ_max = 1e-8/k = 1818, i.e. θ_u ≈ 42.6.

  **NOT brittle, measured rather than assumed:**
  - `worst_identity_2 < 1e-8` (Eq. 17's second identity) — grows, but far slower than the
    tolerance: 3.3e-11 → 3.4e-10 while the tolerance grows 90-fold. 29× headroom at θ_u = 52.07.
    It carries an explicit `theta_u *` factor, so this was the one expected to be worst; it is not.
  - `worst_q_mass < 1e-10` — flat at 2.22e-16, six orders of headroom.
  - `worst_monotone > -1e-9` — −2.3e-13 to −1.7e-13, no growth over the range tested, four orders
    of headroom. Its comment calls it "roundoff at the fixed point", which made it a suspect.
  - `spread < 1e-5` and `worst_gradient < 1e-4` are already *relative* quantities. `spread`'s own
    comment concedes θ_u-dependence ("about 1e-6 relative at theta_u\*... at theta_u = 1 the same
    estimate agrees to 1e-10"), so it is the next one to watch, but it is not in the tolerance's
    chain.
  - The remaining thresholds (basis orthonormality 1e-10, normalization guards 1e-12, parity and
    collision tests 1e-9, grid-convergence `tail < 5e-3`) bound structural quantities that do not
    depend on the tolerance.
  - **Not swept:** `appendix_E`'s relay checks `worst_relay_gradient < 1e-12` and
    `worst_lagged < 1e-9`. They compare the same gradient formed in a different summation order, so
    their residual plausibly scales with term magnitude and therefore with θ_u. They were not
    measured here and should be before the change lands.

- **H16. What the `< 1e-8` fix costs.** Replace the fixed constant with the scale-free question the
  check is actually asking — *did the integration land within a few multiples of the tolerance it
  was asked to achieve?*

  1. **`infer` must return its tolerance.** It returns `dt` and `tau_error` but not
     `derivative_tolerance`. One key, in `code cell 1` and E1 (**coupling 9**).
  2. **Three assertions become `< m * tolerance`** in main cell 7 and their three mirrors in E
     cell 3, with the detail strings reporting the **ratio** so the margin is visible rather than
     implied. Measured gap/tol ∈ [0.95, 1.00], so m = 4 leaves 4× headroom.
  3. **`worst_dense` needs per-run normalization.** It maxes over a ladder of dense-scale grids,
     each with its own λ and so its own tolerance; it must accumulate `max(gap / tol)`, not
     `max(gap)`.
  4. **Re-execution**, since every detail string prints numbers that move.
  5. **Unmeasured:** whether gap/tol stays ≈ 1 on the dense-scale nets. It should be checked before
     m is fixed.

  **A benefit worth weighing in.** The fixed 1e-8 is *slack* at low θ_u — at θ_u = 5.29 the actual
  gap is 1.57e-10, so the check has 64× of unused room and would not notice an integrator
  regression of fifty-fold. At m = 4 it would. **The scale-free form is a stricter test everywhere
  except where the constant currently fails outright.**

- **H17. The two relay checks, measured** (2026-09-21, `relay_threshold_sweep.py`), closing H15's
  unmeasured corner. Thresholds today: relay gradient **1e-12**, lagged **1e-9**.

  | net | θ_u | λ | tol | relay grad | /tol | lagged | /tol | min F step |
  |---|---|---|---|---|---|---|---|---|
  | Λ=8 | 5.29 | 30.0 | 1.65e-10 | 1.04e-14 | 0.00 | 2.85e-12 | 0.02 | −4.1e-10 |
  | Λ=8 | 28.44 | 810.8 | 4.46e-09 | 3.35e-15 | 0.00 | 8.46e-12 | 0.00 | −1.7e-13 |
  | Λ=512 | 13.37 | 180.8 | 9.94e-10 | 3.07e-12 | 0.00 | 1.54e-10 | 0.16 | −3.5e-10 |
  | Λ=512 | 34.70 | 1206.1 | 6.63e-09 | 5.95e-12 | 0.00 | 1.04e-09 | 0.16 | −3.5e-10 |

  **Both are safe where they actually run, and both would fail at Λ = 512.** `check_specification`
  runs at Λ = 8, where the relay gradient keeps 100–300× headroom and the lagged check 118×. At
  Λ = 512 the relay gradient is **3.07e-12 against its 1e-12** and the lagged check reaches
  **1.04e-9 against its 1e-9** — both already over.

  **They are brittle in different variables, which matters for the fix.**
  - The **relay gradient is not tolerance-linked at all** (ratio 0.00 throughout). It is roundoff on
    a summation-order difference, and it scales with the *gradient's own magnitude*, hence with Λ:
    1e-14 at Λ = 8 against 3e-12 at Λ = 512, at comparable θ_u. `m·tolerance` would not fix it; its
    scale-free form is relative — `|relay − columns| / |gradient|`.
  - The **lagged check is tolerance-linked**, at a stable 0.16·tol within a Λ. Two runs each
    stopping within their own tolerance differ by a fraction of it, so `< m'·tolerance` with
    m' = 1 fits it with 6× to spare.
  - **`worst_lagged_step > -1e-9` is thin**: −4.1e-10 at Λ = 8, θ_u = 5.29, only **2.4× headroom**,
    and not monotone in θ_u (−1.7e-13 at θ_u = 28.44), so it looks noisy rather than scaling. Worth
    watching; no fix proposed.

  **Not in scope for this change**, since neither fails where it runs — recorded so the next θ_u or
  Λ that reaches them does not find this unmeasured.

- **H18. m is capped at 2 by the user (2026-09-21):** *"under no circumstance will we consider
  m > 2, because the complexity would be too high to be plausible."* Measured gap/tol is
  **0.95 to 1.002**, so **m = 2** clears the worst observed case by very nearly a factor of two.
  The cap is satisfiable; it leaves no room to absorb a case with a materially larger ratio, so the
  dense-scale nets are checked before m is fixed.

---

## 10. HA9: the flow is integrated twice per row (2026-09-21, user approved)

**The finding.** After HA6, `realizability_report` integrates Eq. (20)'s flow to its halt for each
end-to-end row (printed: **80.61 s**, **75.19 s**, **145.24 s** at Λ = 512), and then
`delta_readout_report` integrates *the same flow again*, from the same start with the same
arguments, purely to arrive at the same θ_u for its "realizable" row. At one update — what the
criterion-stop used to give — this cost nothing and nobody noticed. At 3 to 7 updates climbing to
θ_u ≈ 54 it is about **300 s**, roughly a quarter of the run's whole increase.

**Why it is safe to remove, and what it is not.** What the delta read-out *demonstrates* is the
**settling** at that θ_u — Eqs. (18)–(19) integrated, which is what its `"integrated"` tag marks —
not the flow that reached it. The flow has already been integrated, in the block above, and
`realizability_report` records where it landed in `row["run"]["theta_u"]`. Taking that value is
therefore not a substitution of closed form for dynamics: it is **the value the integrated flow
actually reached**, reused instead of recomputed. (`halt_by_tolerance`'s closed-form value agrees
with it to better than 1e-13, but `row["run"]["theta_u"]` is preferred precisely because it is the
integrated one.)

**Prediction: no printed number moves.** `learn_theta_u` is deterministic and both calls start from
the same respawned network with the same arguments, so the second run reproduces the first exactly.
The only expected difference is runtime. **If any number does move, that is a finding about
determinism and is reported, not absorbed.**

- [x] **HA9a** done 2026-09-21. Three lines in `delta_readout_report`, mirrored into E2.
- [x] **HA9b** done. **The prediction held: no printed number moved.** All 69 lines of the
      function's own output matched the stored copy exactly. The two lines the first comparison
      flagged were an artifact of it running past the end of the function into Code Cell 2b's own
      printing — checked by confirming that header appears nowhere in Code Cell 2's source, rather
      than assumed. Measured: `delta_readout_report` **184.0 s** against about 485 s before, with
      `realizability_report` unchanged at 527.8 s.
- [x] **HA9c** done. **main: 0 errors, 8 figures, 14/14, 839 s** (from 1154 s, −315 s).
      **appendix_E: 0 errors, 5 figures, 18/18, E3 PASS both cells, 1961 s** (from 2516 s, −555 s).
      E3's counts unchanged at 221 and 261 identical lines with the same pattern.
      **Verified that nothing but runtime moved**, by diffing every stored output line against
      `bc3a261`: Code Cell 2b's output is **300 lines before and after**, and the only differences
      are the wall-clock seconds and µs/step inside `cost:` lines (26.06 → 25.38 s, 45 → 44 µs/step
      and so on). **Every step count is byte-identical** — 574,120, 527,295, 242,163 — as are all
      reported quantities. Those `cost:` lines are what `agent.md` §5.2 calls machine quantities and
      what E3 skips for that reason.
