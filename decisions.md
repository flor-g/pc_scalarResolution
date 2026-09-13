# decisions.md

The record of architectural, evaluation, and implementation decisions for `main.ipynb` and
`appendix_E.ipynb`, with who made each and why. Procedures for adding to it are in `agent.md` §3.

> **Seeded 2026-09-13 from earlier working records** (agent memory files and
> `theta_u_learned_reach.md`), condensed. Equation numbers follow the 2026-09-09 numbering. Numbers
> quoted here are for orientation: verify against the executed notebook before citing one.
> Where the records do not say who made a decision, **Decided by** reads `not recorded`; the user
> may wish to fill these in. Registers D and E list candidates known from the records; **neither
> audit has been run.**

## Entry template

```
### <ID>. <Title>
- Status: Settled | Open | Superseded by <ID>
- Decided by: user (date) | agent, confirmed by user (date) | agent, pending user confirmation | not recorded
- Decision:
- Theoretical reason:
- Implementational reason:
- Bogacz status: instance of Eq. (N) with <substitution> | instance under <restriction> | divergence, see D<n> | surrogate for <operation>
- Depends on it:
- Evidence:
- Findings added later: (dated, appended; never edit the decision itself)
```

IDs: **A** architecture, **B** evaluation, **C** conventions, **I** implementation, **O** open,
**D** Bogacz divergence register, **E** quantity trace register.

---

## A. Architecture

### A1. Three-level chain with φ_L clamped by the utterance
- Status: Settled
- Decided by: not recorded
- Decision: E_y ← φ_L ← φ_S ← φ_u ← 1 (Eq. 7). φ_L = Λχ_y is clamped (Eq. 6), so ε_y ≡ 0 (Eq. 8)
  and the y level takes no part in the dynamics. g_y is retained, defined in Appendix A.
- Theoretical reason: the map from lexical field to word form belongs to a word-recognition model
  that can be stacked beneath; unclamping φ_L later reopens the channel without changing anything
  below it.
- Implementational reason: none recorded.
- Bogacz status: hierarchy of his §4.2 (Eqs. 51-54) with the observation at φ_L. Not audited.
- Depends on it: Eqs. (8), (11), (13); Appendix A's Eq. (A4) needs Eq. (11a)'s restored y term.

### A2. Lexical entries fixed by exclusion
- Status: Settled
- Decided by: not recorded
- Decision: each utterance carries an exclusion set E_y (Eq. 5), fixed by the entry alone, with no
  alternatives space.
- Theoretical reason: Appendix D (the asymmetry lies in the representation map).
- Implementational reason: none recorded.
- Bogacz status: no counterpart (input encoding). Not audited.
- Depends on it: Eq. (6), the sign of g_L′, Appendix D.

### A3. ℓ₀ sits in g_L: g_L(φ_S) = ℓ₀ − φ_S
- Status: Settled
- Decided by: user accepted the relocation (2026-09-06)
- Decision: the base prior enters as the reference point of the lexical complement (Eq. 9), not in
  g_S.
- Theoretical reason: x ↦ ℓ₀ − x is the order-reversing affine involution on log-weights, the
  transport of set complement; g_L′ = −I, so ε_L reaches φ_S inhibitorily.
- Implementational reason: none recorded.
- Bogacz status: candidate divergence, see D3.
- Depends on it: Eqs. (9), (11), (15); Appendix D.

### A4. g_S = θ_u B φ_u with θ_u scalar and B fixed; B is a single projection
- Status: Settled
- Decided by: user (2026-09-07, single projection); user (2026-09-11, θ_u stays scalar)
- Decision: forward weights u → S are θ_u B. B is the fixed spatial profile of one projection, not
  K·m synapses sharing a gain. θ_u is the only plastic parameter.
- Theoretical reason: with B a single projection, ⟨ε_S, b⟩ is one signal at one synapse and Eq. (20)
  is Hebbian at m = 1. A free matrix M is local (Bogacz Eq. 56) but unidentified: μ_u anchors one
  direction and M diverges in the other m − 1.
- Implementational reason: none.
- Bogacz status: divergence, see D1.
- Depends on it: Eqs. (10), (16), (19), (20), (B2); Appendix B Locality; Appendix E.
- Evidence: matrix analysis in scratch only, not in the notebook.

### A5. μ_u ≠ 0 is a standing premise; μ_u = 1
- Status: Settled
- Decided by: not recorded
- Decision: the terminating prior mean is nonzero by stipulation. The exact non-degeneracy condition
  is ⟨μ_u, Σ_y c_y⟩ ≠ 0 (Appendix B). The implementation takes μ_u = 1 ∈ ℝ^m.
- Theoretical reason: at μ_u = 0 the chain stops rather than terminates, and θ_u is unidentifiable
  through the scale degeneracy (θ_u, φ_u) → (cθ_u, φ_u/c).
- Implementational reason: the code raises on the exact condition.
- Bogacz status: instance; his Eq. (25) diverges identically at v_p = 0, an unstated premise there.
- Depends on it: A9, A10.
- Rejected, do not revisit: a hyperprior on θ_u; folding θ_u into B; deriving μ_u as an ensemble mean.

### A6. Every σ fixed at 1; no precision learning
- Status: Settled
- Decided by: not recorded
- Decision: σ_y = σ_L = σ_S = σ_u = 1.
- Theoretical reason: the minimum admitted by Friston (2005) and adopted by Bogacz. Unfixing a
  field-level Σ would need his §5 interneurons.
- Implementational reason: none recorded.
- Bogacz status: instance under restriction Σ = I.
- Depends on it: the temperature ½ in Eq. (15); the tempered control (C3).

### A7. m = 2
- Status: Settled
- Decided by: not recorded
- Decision: the utility basis has two columns.
- Theoretical reason: Appendix C. The count is thresholds, not utterances; two ends of the scale give
  two thresholds. m = 1 is degenerate (Text cell 5 Part A), and at m ≥ |Y| = 3 learning collapses to
  q_lit.
- Implementational reason: none.
- Bogacz status: not applicable.
- Depends on it: Part A's parity argument, Appendix C, the need for Appendix E's relay.

### A8. g_y = θ_L A W φ_L; θ_L is a gain and a threshold
- Status: Settled
- Decided by: not recorded (settled 2026-09-07)
- Decision: A is a fixed profile matrix, one projection per word-form unit; θ_L the scalar gain,
  fixed by σ(−θ_L) = δ/2 (Appendix A).
- Theoretical reason: θ_L is semantic, the only parameter in both the generative map and the
  observation model, which identifies it.
- Implementational reason: none.
- Rejected: a softmax g_y (the normalizer needs sibling units' activity, which violates local
  computation); θ_L as an input rather than a multiplicative weight (gradient not Hebbian).
- Bogacz status: instance of Eq. (42) with Θ = θ_L A W. Not audited.

### A9. θ_u is learned in every evaluation, each configuration its own θ\*
- Status: Settled
- Decided by: user (2026-09-11, D1 and D2)
- Decision: θ\* is the maximizer of F̃ (Eq. B2), specific to every set of inputs and
  hyperparameters. Every override re-learns. A fixed θ_u is allowed only as a stated control (B4).
- Theoretical reason: a variational θ_u is a commitment of the model.
- Implementational reason: see I1 for how θ\* is obtained.
- Bogacz status: see D2.
- Depends on it: every reported result.
- Evidence: `theta_u_learned_reach.md` §1, T0-T11.

### A10. The θ_u flow starts at θ_u(0) = 0
- Status: Settled; supersedes readings (a) +1 and (b) ±1 on θ\*'s side
- Decided by: user (2026-09-11, OPEN-1 reading (c))
- Decision: one start shared by every configuration.
- Theoretical reason: the roots of Eq. (B2) have opposite signs, so 0 lies on θ\*'s rising side and
  the flow reaches θ\* in every configuration. (b) was rejected as conceptually poor practice, since
  the start would differ between configurations.
- Implementational reason: no sign rule needed.
- Bogacz status: the tutorial is silent on initial values.
- Evidence: 145/145 configurations; reach.md §2.
- **Wording constraint (user):** the network at θ_u = 0 is the tempered control, never q_lit (C3).

### A11. Timescale commitment: τ_ε ≤ τ_φ/(4 λ_max(H)) ≪ τ_φ ≪ τ_θ
- Status: Settled
- Decided by: user added the commitment (2026-09-11, D4); its exact form was found by the agent (F14)
  and written into the prose in the T10 pass
- Decision: the error units are fast relative to the stiffest state mode, not only relative to τ_φ.
- Theoretical reason: critical damping of the stiffest mode; at learned θ\* the old τ_ε = 0.1 makes
  F non-monotone (§8.2 check failed, min step −18.3).
- Implementational reason: `fast_time_constant()`, dt = τ_ε/2 (I4).
- Bogacz status: candidate, see D4.

### A12. main keeps the non-local form of Eq. (20); Appendix E is a bonus
- Status: Settled
- Decided by: user (2026-09-08)
- Decision: `main.ipynb` implements Eq. (20) as Σ_j φ_u,j⟨ε_S, b_j⟩, non-local at m > 1, with pointers
  to Appendix E, which makes it local with a descending relay r = Bφ_u.
- Theoretical reason: the relay changes none of the results, and may be too complicated for a reader
  on a first pass.
- Implementational reason: E3 verifies the two implementations print the same results.
- Bogacz status: divergence, see D1 and D5.
- Findings added later: under A11 the relay needs only τ_r ≤ τ_ε, for monotone F (F26, 2026-09-11).

### A13. The read-out is a softmax outside the dynamics
- Status: Settled
- Decided by: not recorded
- Decision: q = e^{φ_S}/Σ_j w_j e^{φ_S,j} (Eq. 12). E[s], sd, region masses and the leak are
  summaries of q, not model quantities.
- Theoretical reason: the normalizer is non-local, which is admissible only because the read-out
  takes no part in the dynamics or in Eq. (20).
- Bogacz status: no counterpart; not an operation of the network.

### A14. Implicature through θ_u is conventionalized, not computed within the trial
- Status: Settled
- Decided by: not recorded (resolved 2026-09-07)
- Decision: θ\* depends on Σ_y c_y, an exposure statistic across trials. No within-trial
  alternatives set exists in the architecture.
- Theoretical reason: one synapse, one scalar, one pooled error signal; nothing compares
  alternatives inside one inference pass.
- Depends on it: Appendix B Alternative spaces; Part C's closing claim; see O2.

---

## B. Evaluation

### B1. The shift Δ_y is measured against q_lit, the untempered literal posterior
- Status: Settled; supersedes the θ_u = 0 control as baseline
- Decided by: user (2026-09-09)
- Decision: Δ_y = P(all; q_y) − P(all; q_lit,y) (Eq. 37). The tempered control is kept beside it as a
  secondary column.
- Theoretical reason: q_lit is the literal listener the criterion names. The cost: Δ_y then contains
  tempering plus the utility level, and the tempering is often the larger part. Eq. (39), the
  differential, is the statistic that isolates θ_u.
- Depends on it: Parts C and D, Text cell 6, the verdict.

### B2. The criterion is the conjunction of two conditions
- Status: Settled
- Decided by: user (from `sections_3-5_outline.md` §4.2)
- Decision: first condition Δ_some < 0; second q_H(all | some) < ½. Neither alone suffices.
- Depends on it: Part C, Part D table, Text cell 6 *Where both of Part C's conditions hold*.

### B3. Delta-like prior: Beta(64, 1) with Λ = 8α = 512
- Status: Settled
- Decided by: user asked for the test (2026-09-07); the constants' derivation (Λ_crit ≈ α log 2n) is
  not recorded as user-confirmed
- Decision: Beta(64, 1) stands in for the unrepresentable P₀(s = 1) = 1; Λ must rise with α or the
  prior overrides the entry.
- Evidence: the Gaussian prior at Λ = 512 is the control showing the effect is the prior's, not Λ's.

### B4. Fixed-θ_u evaluations only as stated controls
- Status: Settled
- Decided by: user (2026-09-11, D2)
- Decision: each retained fixed-θ control states its justification in the prose. The list is
  `theta_u_learned_reach.md` §5.C. θ_u = 1 is no longer the start, so that cannot be a control's
  justification.

### B5. Text cell 5 Part B keeps its θ_u = 1 table and adds a learned table
- Status: Settled
- Decided by: user (2026-09-11, D3)

### B6. Non-discrimination is reported, not used to reject the reading
- Status: Settled
- Decided by: user (2026-09-07)
- Decision: where the criterion is met by utterances other than *some*, report it and read the
  headroom (saturation) before interpreting.

---

## C. Conventions that constrain claims

### C1. No Gricean reference frame
- Decided by: user (2026-09-07)
- Results are stated in the model's own terms. Naming a contrasted position is allowed, attributed
  precisely: within-trial computation over alternatives is neo-Gricean (Horn 1972; Gazdar 1979;
  Levinson 2000; Sauerland 2004; Geurts 2010), not Grice (1975).

### C2. The θ_u = 0 case is named for its parameter
- Decided by: user (2026-09-07)
- "The θ_u control" / "the tempered control", never "the truth-conditional baseline".

### C3. Three objects kept apart
- Decided by: user correction (2026-09-11)
- q_lit: θ_u = 0 and σ_S → ∞, field ℓ₀ − φ_L. Tempered control: θ_u = 0 at the model's σ, field
  ½(ℓ₀ − φ_L), the model's start. The model: θ\*. Never "the control" unqualified.

### C4. Naming
- Decided by: not recorded (settled 2026-09-07)
- θ_L, never β (collides with `beta_world_prior`). F is Bogacz's negative free energy, maximized.
  Subscripts capitalize exactly when the level is field-valued (L, S; not y, u). κ_y = BᵀWφ_L is the
  lexical projection; c_y = BᵀW(ℓ₀ − φ_L) is Appendix B's.

### C5. Reader-facing text
- Decided by: not recorded (set 2026-09-07); punctuation 2026-09-08; spacing and numbering chosen by
  the user 2026-09-09
- No changelog prose or references to earlier versions. No dashes as sentence punctuation. Every
  list loose. Equation numbering scheme as in `agent.md` §2.5. Code comments short, pointing to the
  markdown.

---

## I. Implementation

### I1. Closed-form θ\* and fixed points where integration is infeasible
- Status: Settled
- Decided by: **agent, adopted of necessity (2026-09-11, D5); not separately confirmed by the user**
- Decision: θ\* from Eq. (B2); fixed points from Eqs. (15)-(16). The dynamics are integrated only
  where feasible (I2), and the output says which configurations those are.
- Theoretical reason: §8.6 makes the closed forms exact.
- Implementational reason: |θ\*| reaches 1.2e4 on the plane and the φ_u rate 3.5e7 under the flat
  prior; the flow from 0 cannot be integrated to θ\* (F15).
- Bogacz status: surrogate for Eqs. (18)-(20).
- Evidence: T8 runs one criterion-meeting case end to end with nothing in closed form (F29).

### I2. FEASIBLE_STIFFNESS = 1e3
- Status: Settled
- Decided by: **agent, pending user confirmation** (T2, 2026-09-11)
- Decision: `settle()` integrates where λ_max(H) ≤ 1e3 (about 8 s per inference), else reads the
  closed form.
- Implementational reason: run time.
- Evidence needed: that no verdict depends on the threshold's exact value. Not recorded.

### I3. Stopping tolerance 1e-9
- Status: Settled; supersedes 1e-10
- Decided by: user (2026-09-13, T11)
- Implementational reason: 1e-10 sat inside the roundoff floor, so step counts were decided by
  roundoff (F34). At 1e-9 step counts are reproducible and the settled state is accurate to about
  1e-9, two orders inside the specification checks' 1e-8.

### I4. dt = τ_ε/2 with τ_ε from `fast_time_constant()`
- Status: Settled
- Decided by: agent, implementing A11 (2026-09-11); not recorded as separately confirmed

### I5. 1e-12 zero band for sign counts on the plane
- Status: Settled
- Decided by: **agent, pending user confirmation** (F24, 2026-09-11)
- Implementational reason: the α = 1024 row is saturated roundoff at learned θ\*.

### I6. Grid K = 101, half-width 6; world state in ζ = logit s
- Status: Settled
- Decided by: not recorded

### I7. Appendix E's E2 mirrors main's Code Cell 2, verified by E3
- Status: Settled
- Decided by: not recorded (structure of 2026-09-08)
- Coupling rules in `agent.md` §2.

### I8. Appendix C and D numbers come from a recorded script, not a cell
- Status: Settled
- Decided by: T5.1 decision in `theta_u_learned_reach.md`; who made it not recorded
- The script is recorded verbatim in reach.md §7.1. See E1.

---

## O. Open decisions

### O1. What fixes δ, and so θ_L
- Status: Open (since 2026-09-07)
- Appendix A derives θ_L from a just-noticeable difference, σ(−θ_L) = δ/2, with n = 1/δ. What fixes δ
  is not settled. The implementation takes n = 10.

### O2. The exposure distribution p(y) is uniform and unargued
- Status: Open; not yet raised with the user as a decision
- The θ_u flow averages the three utterances' gradients equally, so the operative quantity is
  3·E_{p(y)}[c_y] at uniform p(y). Non-uniform exposure moves θ\*. Appendix B names it as a prior over
  utterances; no text argues for uniform.

### O3. The outline pointer for the cost of realizability
- Status: Open, by the user's choice
- The complexity point (seconds of settling are an implausible cost) belongs to the outline's
  hypothesized alternative representation level (`sections_3-5_outline.md` 3.4, 3.4.3, 5.3). The
  pointer from `main.ipynb` stays bare until the background outline is finalized (reach.md A11).

### O4. The `\ker` sentences in Text cell 3 §3.2 and Appendix A
- Status: Open as of 2026-09-09; **verify whether still open**
- The user reported mistyping them and supplied the reading; the corrected wording is the user's to
  restate.

---

## D. Bogacz divergence register

**Audit status: not run.** The entries below are candidates known from the records. Each needs the
procedure of `agent.md` §3.2 before its verdict is final. Mark each `[audited YYYY-MM-DD]` when done.

| ID | Operation | Where | Candidate verdict | What differs, and the recorded defence |
|---|---|---|---|---|
| D1 | Weights u → S tied as θ_u B | Eqs. (10), (20); A4 | Divergence | Bogacz's Θ is a free matrix (Eq. 56), each entry local. Tying K·m entries to one scalar is weight sharing. Defence over K: B is one projection. Over m: non-local in main (A12), local via the relay in Appendix E. |
| D2 | θ_u as a continuous slow flow with τ_θ, averaged over the utterance ensemble | Eq. (20); A9 | Needs audit | His Eq. (25)/(29) supply the gradient at the inference stage, and parameters change after inference settles, trial by trial. Whether a continuous flow on the ensemble-summed gradient is an instance is not checked. |
| D3 | Affine offset ℓ₀ in g_L | Eq. (9); A3 | Needs audit | His generative maps are Θh(φ) (Eq. 42), with no additive field. Whether ℓ₀ is an instance (a fixed input from a tonic node, as μ_u is) is not checked. |
| D4 | The fast-end timescale bound | Eq. (20); A11 | Needs audit | He assumes error nodes converge fast. Whether a bound in terms of λ_max(H) is an instance of his treatment or a new commitment is not checked. |
| D5 | Relay r = Bφ_u | Appendix E, E1-E6 | Divergence | Not his §5 interneuron, which removes a matrix inverse. Only the move, putting the needed quantity into one neuron's activity, carries over. Recorded in E.2. |
| D6 | Quadrature measure W on field levels | Eqs. (2)-(3), (13) | Needs audit | His norms are Euclidean. Whether the weighted inner product is an instance under a change of variable or a divergence is not checked. |
| D7 | Closed forms in place of integration | I1 | Surrogate | Agreement with integrated dynamics is reported only in feasible configurations. |
| D8 | Clamped φ_L, ε_y ≡ 0 | Eqs. (6), (8); A1 | Needs audit | Observation enters at an internal level rather than the sensory bottom. |

---

## E. Quantity trace register

**Audit status: not run.** Candidates known from the records, classed per `agent.md` §3.3. Class (e)
entries need the user's attention.

| ID | Quantity | Where | Candidate class | Note |
|---|---|---|---|---|
| E1 | Numbers quoted in Appendices C and D | Appendices C, D | (a)/(b), sourced by script | Printed by no cell; sourced from reach.md §7.1 (I8, F27 residue). Acceptable only while that script stays recorded. |
| E2 | q_lit | `literal_fixed_point`, Parts C-D | (b) as a limit | Not a configuration the network can occupy at the model's σ; defined as Eq. (15) at θ_u = 0, σ_S → ∞. Justified in Part C. |
| E3 | Tempered control, θ_u = 0 | Parts C-D, Text cell 6 | (c) | Justified: separates tempering from the utility level. Also the model's start (A10). |
| E4 | θ_u = 1 sites | Code Cell 3, Text cell 5 Part B, Appendices C-D | (c) | Each must carry a §5.C justification. Verify every site does. |
| E5 | `tau_theta=20.0`, `tau_state=1.00` | Code Cell 2 probes | (d)? | The prose fixes only the ordering τ_φ ≪ τ_θ; the values are implementation choices. Not recorded in decisions. |
| E6 | `sharpness` of `exclusion_indicator` | Code cell 1, specification checks | unknown | Smooth masks are used in verification; whether the prose defines a sharpness parameter is not checked. |
| E7 | Two θ\* solvers: `theta_u_stationary_points` (code cell 1) and bisection `theta_u_stationary_point` (Code Cell 2) | Code cells 1-2 | (d) | The bisection is accurate only to about 4e-8 at \|θ\*\| > 6000 (F17). Which one each result uses is not recorded here. |
| E8 | FEASIBLE_STIFFNESS, derivative tolerance, zero band, max_steps | Code Cells 1-4 | (d) | I2, I3, I5; max_steps not recorded. |
| E9 | g_y, A, θ_L's gain role | Appendix A | unknown | Whether the architecture code implements g_y or only the clamp is not checked. |
