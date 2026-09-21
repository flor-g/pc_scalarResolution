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

- **H5. The hazard: the rule can halt at a slow *start*, not only near the asymptote.** Under the
  flat prior at Λ = 8, where θ\* = 5950.63, the first update is tiny because ⟨μ_u, Σ_y c_y⟩ is small
  there, so any tolerance ≥ 1e-2 halts after **one update, at θ_u = 0.0005** — the tempered control
  in all but name. The verdict is unchanged (the conjunction fails at θ\* too), but the reported
  shift would be +0.0854 rather than +0.0295. **Any adopted rule needs a guard**, and the audit does
  not choose one. Candidates: a relative tolerance |Δθ| < tol·|θ|; a rule that halts only after the
  flow has left its start; or a minimum number of updates. Each is a stipulation of the same kind as
  the tolerance itself.

- **H6. A fine tolerance never fires in any plausible number of exposures.** At 1e-9 and 1e-6 at
  Λ = 512 the flow is still at θ_u ≈ 600 after **2,000,000 updates**, against θ\* ≈ 1500. This is
  F15 again, and it is the measured form of the user's argument: a tolerance anywhere near 1e-9 does
  not halt the flow at all, so the halting regime is the coarse one, where 3 to 3,700 updates
  suffice.

- **H7. The fast loop's tolerance is not where the cost lives.** Coarsening `infer`'s tolerance from
  1e-9 to 1e-2 at Λ = 8 leaves every verdict unchanged, moves φ_S by at most 5.2e-3, and saves only
  513 → 152 Euler steps. So "tolerance halts the fast loop" is already true and costs nothing to
  say; the claim that does work is the one about the **slow** flow.

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

**2026-09-21: measured, nothing adopted, nothing implemented.** The audit is committed; no notebook,
outline or decision entry has been changed on the strength of it. `decisions.md` A9, A11, I3, O3 and
`thesis_outline/revisions.md` R9, R10 are the entries that would move, and none has been touched.
