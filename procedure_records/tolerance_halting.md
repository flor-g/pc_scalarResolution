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

**What still divides the reported from the demonstrated.** A19's third part stands: the paper's
results are at θ\*, which is what keeps them independent of the ad hoc tolerance. What the tolerance
now fixes is the **realizable** rows — demonstrations that the dynamics reach the verdict — and they
carry the tolerance's value on their face. Tasks below; **nothing is implemented**.

---

## 7. Tasks (HA0–HA8), and the two questions that block them

**Blocking, because each decides whether stored output moves.**

- **Q-HA1. How does `learn_theta_u` halt?** Today it runs a fixed `num_updates` and stops there,
  which is the arbitrary cap A19 replaces.
  - **(i) (recommended) The tolerance is an explicit argument with no default**, and `num_updates`
    stays as a guard against a flow that never meets it. Call sites pass a tolerance only where a
    halt is being demonstrated; the cells that report θ\* do not call the flow at all. **No stored
    output moves**, and the code says what A19 says.
  - **(ii) A default tolerance.** Then every existing call halts by it, the SLOW PARAMETER block's
    "0.0000 → −7.567163 over 60 updates" line changes, and a default value is exactly the ad hoc
    quantity A19 says results must not depend on.
- **Q-HA2. What happens to the two "realizable" θ_u the evaluation already reports** — the
  criterion-stopped one-update rows (7.8161, 7.9926, 13.3749) and `criterion_threshold`'s bisection
  on fractions of θ\*?
  - **(i) (recommended) Keep both, relabelled.** They are demonstrations that the conjunction is
    reached early in the flow and integrable there, not predictions at a halted θ_u. Under A19 the
    prose says so, and says that neither stopping rule is the halting mechanism: one is the
    evaluator's criterion, the other needs θ\*. The halting account is about where
    the flow would stop, not about how these two rows were located.
  - **(ii) Recompute them at a tolerance.** Rejected by A19's third part: the rows would then depend
    on the ad hoc quantity.
  - **(iii) Drop them.** They are §4.6's evidence and Text cell 4's demonstration that the verdict
    does not wait for θ\*; dropping them would cost that.

**Tasks, once both are answered.**

- [ ] **HA0. Checkpoint** (`agent.md` §4.2), before any code cell is touched.
- [ ] **HA1. `code cell 1`, `learn_theta_u`** under Q-HA1: the halting rule, its docstring stating
      that the flow halts when its own update falls below the tolerance, and that the value is ad
      hoc (A19). **Coupling 9 fires** — E1 carries the same def with its relay argument, so the edit
      is applied to E1's own version, not lifted over it.
- [ ] **HA2. `infer`'s docstring and I3.** The 1e-9 is the same mechanism at the fast timescale, not
      a numerical detail; it stays above the roundoff floor (F34) and keeps its value. No behaviour
      changes.
- [ ] **HA3. Text cell 3 §7 or §8.5**, where Eq. (20) is introduced: one passage on halting by
      tolerance, θ\* as the asymptote the commitment names, and the ad hoc status of the value.
      Under B10/C7 the cell takes no position on what that means for the brain.
- [ ] **HA4. Appendix B and Text cell 4's realizability block**: the relabelling Q-HA2 settles.
- [ ] **HA5. Couplings and numbering.** 5 (no new tag unless HA3 adds one), 6, 9 (HA1), and E3's
      prefixes; the ToC only if a heading moves.
- [ ] **HA6. Execute** main then appendix_E (`agent.md` §5.1). Acceptance: the baseline, unchanged
      under Q-HA1(i) — main 0 errors, 8 figures, 14/14; appendix_E 0 errors, 5 figures, E2 18/18,
      E3 PASS — with any departure reported rather than explained away.
- [ ] **HA7. The outline.** §5.3 (planned) states the halting account and rests its cost argument on
      H2–H4; §5.5 Limits and §3.4 carry a clause if HA3 introduces notation they use. `revisions.md`
      R22's site entries.
- [ ] **HA8. Commit**, one logical change per commit, hashes recorded above.

**What stays untouched, by the user's scope line:** every reported number, A9, R10, the θ\* tables,
the plane, and §§4.1–4.5. The audit's H2–H4 are evidence for the discussion, not new results to
print, and they stay class (e) unless a cell is later asked to print them.
