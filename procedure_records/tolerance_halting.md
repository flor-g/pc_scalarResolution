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

- **H8. What a committed tolerance costs, measured 2026-09-21** (block 4 of the audit, added after
  the user chose to define `learn_theta_u` by the tolerance itself). Steps are scaled from Code Cell
  2b's integrated delta-like row (39,035 steps at λ = 180.9), since dt = τ_state/(8λ):

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
- [ ] **HA2. `infer`'s docstring and I3.** The 1e-9 is the same mechanism at the fast timescale, not
      a numerical detail; it stays above the roundoff floor (F34) and keeps its value. No behaviour
      changes.
- [ ] **HA3. Text cell 3 §7 or §8.5**, where Eq. (20) is introduced: one passage on halting by
      tolerance, θ\* as the asymptote the commitment names, and the ad hoc status of the value.
      Under B10/C7 the cell takes no position on what that means for the brain.
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
  - [ ] **HA4b. Call sites 3 and 4**, the end-to-end rows and the delta read-out's realizable row.
        Blocked on a measurement and a question — see §8.
- [ ] **HA5. Couplings and numbering.** 5 (no new tag unless HA3 adds one), 6, 9 (HA1), and E3's
      prefixes; the ToC only if a heading moves.
- [ ] **HA6. Execute** main then appendix_E (`agent.md` §5.1). Acceptance: main 0 errors, 8 figures,
      14/14; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS. **Stored output moves here** (Q-HA1's
      consequence), so the acceptance is no longer "the baseline, unchanged": the expected departures
      are the realizable rows, the SLOW PARAMETER block's update line, and `cost:` lines. Any other
      departure — above all in the θ\* tables or the plane — is reported, not explained away.
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
