# decisions.md

The record of architectural, evaluation, and implementation decisions for `main.ipynb` and
`appendix_E.ipynb`, with who made each and why. Procedures for adding to it are in `agent.md` §3.

> **Seeded 2026-09-13 from earlier working records** (agent memory files and
> `procedure_records/theta_u_learned_reach.md`, abbreviated reach.md below), condensed. Equation numbers follow the 2026-09-09 numbering. Numbers
> quoted here are for orientation: verify against the executed notebook before citing one.
> Where the records do not say who made a decision, **Decided by** reads `not recorded`; the user
> may wish to fill these in. Registers D and E were audited on 2026-09-13; their verdicts are
> the agent's and have not been confirmed by the user.

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
- Bogacz status: instance, φ_L playing the observed input of his Eq. (51); see D8.
- Depends on it: Eqs. (8), (11), (13); Appendix A's Eq. (A4) needs Eq. (11a)'s restored y term.

### A2. Lexical entries fixed by exclusion
- Status: Settled
- Decided by: not recorded
- Decision: each utterance carries an exclusion set E_y (Eq. 5), fixed by the entry alone, with no
  alternatives space.
- Theoretical reason: Appendix D (the asymmetry lies in the representation map).
- Implementational reason: none recorded.
- Bogacz status: no counterpart (input encoding).
- Depends on it: Eq. (6), the sign of g_L′, Appendix D.

### A3. ℓ₀ sits in g_L: g_L(φ_S) = ℓ₀ − φ_S
- Status: Settled
- Decided by: user accepted the relocation (2026-09-06)
- Decision: the base prior enters as the reference point of the lexical complement (Eq. 9), not in
  g_S.
- Theoretical reason: x ↦ ℓ₀ − x is the order-reversing affine involution on log-weights, the
  transport of set complement; g_L′ = −I, so ε_L reaches φ_S inhibitorily.
- Implementational reason: none recorded.
- Bogacz status: instance under restriction (ℓ₀ fixed), see D3.
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
- Bogacz status: the map is an instance of Eq. (42); its gradient, Eq. (A4), is a locality
  divergence the prose does not register, see D10.
- Findings added later: 2026-09-13, Appendix A now states the divergence (A17).

### A9. θ_u is learned in every evaluation, each configuration its own θ\*
- Status: Settled
- Decided by: user (2026-09-11, D1 and D2)
- Decision: θ\* is the maximizer of F̃ (Eq. B2), specific to every set of inputs and
  hyperparameters. Every override re-learns. A fixed θ_u is allowed only as a stated control (B4).
- Theoretical reason: a variational θ_u is a commitment of the model.
- Implementational reason: see I1 for how θ\* is obtained.
- Bogacz status: see D2.
- Depends on it: every reported result.
- Evidence: `procedure_records/theta_u_learned_reach.md` §1, T0-T11.

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
- Bogacz status: instance under restriction, see D4; §8.3's attribution overstates, see CF2.

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
  2026-09-13: at τ_r = τ_ε F is monotone under *some* only; under *no* and *all* three steps fall
  (Code Cell E4). Eq. (E6) keeps ≤ for stability, with the exception stated (O6).

### A13. The read-out is a softmax outside the dynamics
- Status: Settled; its standing as the reported belief is reframed by A16 (2026-09-13)
- Decided by: not recorded
- Decision: q = e^{φ_S}/Σ_j w_j e^{φ_S,j} (Eq. 12). E[s], sd, region masses and the leak are
  summaries of q, not model quantities.
- Theoretical reason: the normalizer is non-local, which is admissible only because the read-out
  takes no part in the dynamics or in Eq. (20).
- Bogacz status: divergence (interpretive), see D9.

### A15. The default base world prior is N(0, 1) in ζ, and it is not elicited
- Status: Settled; supersedes the description of the Gaussian as "the elicited prior" (E4)
- Decided by: user (2026-09-13)
- Decision: ℓ₀ is supplied by an elicited distribution where one is available, and need not be.
  Without one, the default is the Gaussian of mean 0 and precision 1 in ζ. It is one of the five
  base world priors the model is tested on (Part D).
- Theoretical reason: the framework represents states with Gaussians (Bogacz Eqs. 3, 36, 52). ℓ₀
  is not a state unit and need not be Gaussian by construction, but a Gaussian default is the choice
  consistent with the framework's assumption. The reason for mean 0 and precision 1 is not recorded.
- Implementational reason: `gaussian_world_prior(0.0, 1.0)` is what the constructor uses when no
  `base_prior` is given.
- Bogacz status: not an operation.
- Depends on it: every result reported "under the default Gaussian prior".

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

### A16. q is a comparison read-out; the construction's posterior is the delta at the settled state
- Status: Settled; reframes A13 and resolves D9
- Decided by: user (2026-09-13)
- Decision: q (Eq. 12) is kept for comparison with the RSA literature, and nothing in the
  architecture or the construction dictates it. The posterior native to the construction is
  Bogacz's delta at the settled state (φ_S\*, φ_u\*). Part D reports it after the q figures (B7). The
  framing sites of the prose say so (Text cell 3 §4 item 5, Text cell 4 Part C and Reporting
  statistics); Parts C and D keep their verdicts in q, stated as conditions on the comparison
  read-out.
- Theoretical reason: the framework's approximate posterior is a delta distribution (Bogacz §3,
  Eq. 34), and the foundational assumptions of standard RSA differ from the framework's, so q is a
  convention of the literature compared with.
- Implementational reason: none.
- Bogacz status: the delta is an instance of his Eq. (34); q has no counterpart in the tutorial (D9).
- Depends on it: Text cell 3 §4 item 5; Text cell 4 Part C, Part D, Reporting statistics;
  `delta_readout_report` in Code Cell 2.
- Evidence: `procedure_records/d9_delta_readout.md` F1-F4.

### A17. Eq. (A4) is stated as non-local; the relay and the alternatives level are named, not derived
- Status: Settled; resolves D10
- Decided by: user (2026-09-13)
- Decision: Appendix A states that Eq. (A4) does not satisfy the locality constraint, since θ_L gains
  all |Y| rows of A and its gradient sums products formed at |Y| word-form units (the violation of
  Eq. B4), and that a relay of the kind Appendix E gives θ_u would be required to make it local, in
  one or two sentences and without detail, since φ_L is not variational at this phase. It then
  notes, conditionally, that under the alternatives level the accompanying paper proposes on
  complexity grounds each level carries two entries, and if each pair is carried by a single
  log-odds unit Eq. (A4) has one term and no relay is needed. The pointer to the paper is bare (as
  O3).
- Theoretical reason: the user's instruction (verbatim): "clarify that theta_L as per A4 does not
  satisfy locality constraint. Then suggest that a relay similar to how we treated theta_u in
  appendix E would be required for theta_L to be local. This is just one or two sentences and do
  not get into the details since we have not implemented variation phi_L at this phase yet." and
  "cross refer to the paper, where we argued that an alternatives level is strongly motivated by
  complexity reduction. With an alternatives level, phi_L would only represent two lexical entries
  and I suppose therefore the locality problem should not arise at all and a relay wouldn't be
  needed."
- Qualification (agent, accepted by the user as the conditional wording): two entries remove the
  sum only if the pair is carried by one unit; two word-form units sharing θ_L would still pool
  across two neurons. Not stated in the prose: if one θ_L still gains the cuts of several cascade
  levels, Eq. (A4) pools across levels again; the outline does not settle how θ_L is split.
- Implementational reason: none; Eq. (A4) vanishes while φ_L is clamped, so no result moves.
- Bogacz status: divergence, see D10.
- Depends on it: Appendix A under Eq. (A4).
- Findings added later: 2026-09-13, the user moved the paragraph after *θ_L enters twice* and
  asked whether the sentence under Eq. (A4) makes Eq. (A4) local. It shows each term local (Bogacz
  Eq. 25 form), not the sum; at |Y| = 3 as stated the sum is non-local, and the locality line falls
  between one word-form unit and several, not at two entries. The paragraph now says so (user
  approved the wording). "Nothing here requires a normalization across the word-form units, which
  would not be local" read as a locality claim; it now says Eq. (A4) involves no normalization but
  does sum over the units (user, 2026-09-13).

### B1. The shift Δ_y is measured against q_lit, the untempered literal posterior
- Status: Settled; supersedes the θ_u = 0 control as baseline
- Decided by: user (2026-09-09)
- Decision: Δ_y = P(all; q_y) − P(all; q_lit,y) (Eq. 37). The tempered control is kept beside it as a
  secondary column.
- Theoretical reason: q_lit is the literal listener the criterion names. The cost: Δ_y then contains
  tempering plus the utility level, and the tempering is often the larger part. Eq. (39), the
  differential, is the statistic that isolates θ_u.
- Depends on it: Parts C and D, Text cell 6, the verdict.
- Findings added later: 2026-09-13, the prose no longer calls q_lit a posterior (A16, C3).

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
  `procedure_records/theta_u_learned_reach.md` §5.C. θ_u = 1 is no longer the start, so that cannot be a control's
  justification.

### B5. Text cell 5 Part B keeps its θ_u = 1 table and adds a learned table
- Status: Settled
- Decided by: user (2026-09-11, D3)

### B6. Non-discrimination is reported, not used to reject the reading
- Status: Settled
- Decided by: user (2026-09-07)
- Decision: where the criterion is met by utterances other than *some*, report it and read the
  headroom (saturation) before interpreting.

### B7. Part D reports the delta read-out beside the q figures
- Status: Settled
- Decided by: user (2026-09-13); the two print blocks under the table proposed by the agent
  (`d9_delta_readout.md` DEC4), confirmed by the user 2026-09-13
- Decision: after its figures Code Cell 2 prints, per Part D prior and utterance at θ_u\*, φ_u\*, the
  peak of φ_S\* in s (the grid node where φ_S\* is largest), its maximum and minimum, and the
  all-region q-mass for comparison; the delta-like row is repeated at the realizable θ_u, integrated.
  Below the table: the ℓ₀ peak beside the peak of φ_S\*("some") against the cell of *all*
  (ζ ≥ θ_L), and, for a row where the model moves the peak out of the cell, the node-level
  boundary check at θ_u\* on grids of 201, 401 and 801 nodes. Text cell 4 Part D carries a reading
  guide that cites Appendix A's Voronoi cell.
- Theoretical reason: A16.
- Implementational reason: printed in Code Cell 2 so that E2 mirrors it and E3 checks it.
- Depends on it: the reading guide in Text cell 4 Part D.
- Evidence: `procedure_records/d9_delta_readout.md` F2-F4.

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
- Findings added later: 2026-09-13, q_lit is "the untempered literal listener" where the prose
  called it "the untempered literal posterior" (A16; wording proposed as `d9_delta_readout.md` DEC5,
  confirmed by the user 2026-09-13). At the first mention of *literal* the prose states, in one
  sentence and without further explanation, that what it denotes here is distinct from what it
  denotes in the RSA and Gricean literature (user, 2026-09-13).

### C4. Naming
- Decided by: not recorded (settled 2026-09-07)
- θ_L, never β (collides with `beta_world_prior`). F is Bogacz's negative free energy, maximized.
  Subscripts capitalize exactly when the level is field-valued (L, S; not y, u). κ_y = BᵀWφ_L is the
  lexical projection; c_y = BᵀW(ℓ₀ − φ_L) is Appendix B's.

### C6. Every number the prose quotes is computed by explicit code and printed by a code cell
- Decided by: user (2026-09-13)
- A number computed off-notebook, or only by a script recorded in a change record, does not count
  as sourced. Supersedes the allowance of I8.

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
- Bogacz status: surrogate for Eqs. (18)-(20), see D7.
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
- Status: Superseded by C6 and I10 (2026-09-13)
- Decided by: T5.1 decision in `procedure_records/theta_u_learned_reach.md`; who made it not recorded
- The script is recorded verbatim in reach.md §7.1, and covers Appendix C §6 and Appendix D §1
  only. See E7.

### I9. Remaining implementation constants
- Status: Settled
- Decided by: not recorded
- Decision: τ_θ = 20, with 60 updates in the learning probe and 25 in Part A (the values
  Appendix B and Part C quote); `max_time` = 1000 in `infer`; `learn_theta_u`'s default of 50
  updates; bisection brackets and iteration counts (θ\* 1e-3 to 1e6 in 120 steps; the override
  threshold 1e-3 to 1e7 in 90; the criterion threshold 60 steps and 200 ray checks); Part A's test
  tolerances (1e-8, 1e-10, 1e-5, 1e-4, 5e-3); the K ladder 51 to 801 with smooth sharpness 0.1;
  `verify_samples` = 6; `MU_SENSITIVITY`; the radii and sectors of the μ_u plane.
- Evidence that results do not depend on the exact values: τ_θ sets the rate only (Eq. 20); for
  the rest, not recorded.

### I10. Where the numbers of C6 are printed
- Status: Settled
- Decided by: agent, confirmed by user (2026-09-13); proposed as DEC3 of `procedure_records/e4_e7_sourcing.md`
- Decision: numbers quoted in Text cells 4 and 5 are printed by Code Cells 2 and 3, inside the
  functions whose output they belong to. Each of Appendices A–D is followed by its own code cell
  (Code Cells A–D; Code Cell A also prints Text cell 3 §2's numbers about g_y). Numbers Appendix
  E.1 quotes that E2 does not print are printed by Code Cell E4.
- Implementational reason: additions to Code Cell 2 go inside existing functions, so Code Cell
  E3's replay needs no new calls; each addition is mirrored into E2 verbatim.

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
- Findings added later: 2026-09-13, Appendix A's pointer to the alternatives level is bare on the
  same rule (A17).
- Findings added later: 2026-09-13 (agent), the outline is now `thesis_outline/sections_3-6.md` and
  the section numbers above no longer apply. Neither current outline contains the settling-cost
  argument this pointer defers to: §5.1's complexity case concerns branching, not settling time. The
  planned §5.3 of `thesis_outline/revisions.md` would supply the target. The pointer stays bare, and
  the term itself is O7.

### O4. The `\ker` sentences in Text cell 3 §3.2 and Appendix A
- Status: Open as of 2026-09-09; **verify whether still open**
- The user reported mistyping them and supplied the reading; the corrected wording is the user's to
  restate.

### O5. Appendix B's sign sentence
- Status: **Settled** (user, 2026-09-13; record `procedure_records/o5_o6_resolution.md`). Opened
  2026-09-13 from `procedure_records/e4_e7_sourcing.md` F2.
- Decision: the counterfactual is both signs reversed, c_y → −c_y, maximizer +28.4375. Appendix B now
  reads "were both signs reversed the maximizer would be +28.437".
- Appendix B says that "were the two signs reversed the maximizer would be +22.578". Code Cell B
  prints: both signs reversed gives +28.4375 (the exact symmetry); ℓ₀'s sign reversed alone gives
  +22.5779; φ_L's sign reversed alone (the coupling ℓ₀ + φ_L) gives −22.5779. The sentence is left as
  written until the user restates what it should claim.

### O6. Does a relay as fast as the error units keep F monotone?
- Status: **Settled for now** (user, 2026-09-13; record `procedure_records/o5_o6_resolution.md`).
  Opened 2026-09-13 from `procedure_records/e4_e7_sourcing.md` F8.
- Decision: Eq. (E6) keeps τ_r ≤ τ_ε, and E.1 states the exception: at equality F is monotone under
  *some* only. E.1 also states what a strict bound would require: the largest τ_r/τ_ε at which no
  step of F decreases under any utterance, measured at every θ_u and prior claimed, with the bound
  placed at or below it (not measured). E.2 and E.3 now claim stability, not monotonicity, for a
  relay at τ_ε. `infer` keeps its strict guard, with a comment on how it differs from Eq. (E6).
- Code Cell E4 prints, at the default θ\*: under *some* no step of F falls at τ_r = τ_ε; under *no*
  and *all* three do (worst −2.9e-2). E.1 now reports both. Eq. (E6) states τ_r ≤ τ_ε, E.2 says a
  relay at the error units' own speed suffices, and `infer` already requires τ_r < τ_ε strictly.
  Options: keep ≤ and state the exception; make the bound strict; or read "monotone" to a tolerance.

### O7. "Realizability" names three different things
- Status: Open (since 2026-09-13)
- Decided by: not decided. Opened on the user's instruction (2026-09-13): "The terminology clash
  needs to be handled more carefully, so mark it as open decision." Raised while planning the outline
  revision, `thesis_outline/revisions.md` §5 item 2.
- The term carries three senses across the notebooks:
  1. **Exact realizability.** Appendix B: a θ at which both residuals vanish and F = 0, which is what
     identifies θ there ("it is realizability that identifies θ"; "what μ_u ≠ 0 buys is not
     realizability"). Code Cell B prints `REALIZABILITY AT theta_u*` in this sense.
  2. **The cost of reaching the verdict.** Code Cell 2's `realizability_report` and its header
     `REALIZABILITY: WHAT THE CONJUNCTION NEEDS, AGAINST WHAT theta_u* COSTS`; the `realizable θ_u`
     rows of `delta_readout_report`; Text cell 4 Part D's reading guide (four uses); a Code Cell 4
     comment; B7; O3. Mirrored in E2 and replayed by name in E3. It covers two different quantities:
     the least |θ_u| meeting the conjunction (2.126 under the delta-like prior), and the θ_u one
     update of Eq. (20) reaches (13.3749), which is the one labelled "realizable".
  3. **Representability of a direction by exclusion sets.** Appendix C: "no exclusion set realizes
     it", "is realizable".
  "Realizing E_y" in Appendix A and in Code Cell 1's comment is ordinary usage and not part of the
  clash.
- Options, and what each would change:
  - (a) Rename sense 2. This touches Code Cell 2's function name, headers and labels; E2 (agent.md §2
    item 1); E3's replay list, which calls the function by name (item 7); Text cell 4; B7 and O3.
    Both notebooks must be re-executed. A new term has to be chosen, and it should also say which of
    the two quantities it names.
  - (b) Rename sense 1: Appendix B's markdown and Code Cell B's printed header. Code Cell B is not
    mirrored in E2, so only main is re-executed. Check first whether sense 1 is the established usage
    Appendix B is borrowing, before renaming away from it.
  - (c) Keep the word and define each sense at first use.
  - Sense 3 can move to "represents" under any option.
- Needed to decide: the user's choice among (a)-(c), and the replacement term if (a) or (b).
- Interim rule: the outline revision does not introduce "realizability" in a new sense. Its new §5.3
  names the cost sense descriptively until O7 is settled.
- Depends on it: `thesis_outline/revisions.md` §5 item 2 and §3's §5.3 title; Text cell 4; Appendices
  B and C; Code Cells 2 and B; E2 and E3; B7; O3.

---

## D. Bogacz divergence register

**Audited 2026-09-13** against `main.ipynb` and `appendix_E.ipynb` at commit 76df22e, by the
procedure of `agent.md` §3.2, reading `Bogacz_2017_Free_Energy_Tutorial.md`. The scripts and their
output are in `audits/2026-09-13/`; V1 to V4 below refer to `verify_output.txt` there. Every
verdict is the agent's reading and has not been confirmed by the user.

### Verdict per operation

| Operation | Where | Verdict | Substitution, or pointer |
|---|---|---|---|
| Coordinates of the field units | Eqs. (1)–(3), (13), (18)–(19) | Instance under a change of variables, not stated in the prose | D6 |
| Clamp φ_L = Λχ_y, ε_y ≡ 0 | Eqs. (6), (8) | Instance | D8 |
| g_L(φ_S) = ℓ₀ − φ_S | Eq. (9) | Instance under restriction | D3 |
| g_S(φ_u) = θ_u Bφ_u, as a map | Eq. (10) | Instance | his Eq. (42) with Θ = θ_u B̃ and h = id (B̃ of D6) |
| Prior error r_u = φ_u − μ_u | Eq. (11) | Instance under restriction | his Eqs. (10), (13), with v_p = μ_u supplied by the tonic unit of his Fig. 3; μ_u is fixed where his v_p learns by Eq. (19) (A5) |
| F | Eq. (13) | Instance under restriction | his Eqs. (37), (52) with Σ = σI, in the coordinates of D6; the count of log σ terms matches |
| Error units | Eq. (18), `infer` | Instance under restriction (σ = 1) | his Eq. (54) at Σ = 1; D11 for σ ≠ 1 |
| State units | Eq. (19), `infer` | Instance, in the coordinates of D6 | his Eq. (53) with Θ_L = −I and Θ_S = θ_u B̃; reproduced to 1.8e-15 over 400 Euler steps (V3). How the prose writes it: E2 |
| Target identities | Eqs. (14), (17) | Instance | his Eq. (57) |
| Read-out and reported statistics | Eqs. (12), (25)–(27) | Divergence; resolved by A16 | D9 |
| θ_u gradient | Eq. (20), `theta_u_gradient` | Divergence (locality) | D1 |
| θ_u update scheme | `learn_theta_u` | Instance | D2 |
| θ_u(0) = 0 | A10 | No counterpart | the tutorial is silent on initial values |
| Initial state of `infer` | φ_S = ℓ₀, φ_u = μ_u, ε = 0 | Instance | his Exercises 2–3 start φ at the prior mean and ε at 0 |
| Timescale bound | commitment 7, §8.3 | Instance under restriction | D4 |
| Closed-form fixed points and θ\* | Eqs. (15)–(16), (B2), `settle` | Surrogate | D7 |
| Euler step, stopping rule, horizon | `infer` | Surrogate | dt = τ_ε/2; max\|derivative\| < 1e-9 for 10 steps; max_time 1000 (I3, I4, I9). His exercises use a fixed Δt and horizon |
| g_y, and the θ_L gradient (inactive) | Eqs. (A2)–(A4) | Map: instance. Gradient: divergence (locality), stated in Appendix A (A17) | D10 |
| Relay r = Bφ_u | Eqs. (E1)–(E4) | Divergence | D5 |
| Relay loop spectrum | Eq. (E5) | Analysis, not an operation | his §5.1 eigenvalue method (Eq. 66), applied to a different loop |
| Equations quoted in Text cells 1–2 and the pseudocode | his Eqs. 6, 50, 53–54, 59–61, 71 | Quoted accurately | the pseudocode and the last sentence of Text cell 2 describe Σ-learning the model does not perform; see E6 |

### Entries

**D1. The u → S weights are tied to one scalar.** Divergence (locality of plasticity). Bogacz's Θ
is free (Eq. 56), each entry updated by its own pre-times-post product. Tying the K·m entries to
θ_u makes Eq. (20) the chain rule of Eq. (56) onto a single direction, which pools products formed
at many synapses. Defence across K: B is one projection (A4, Appendix B *Locality*). Across m: none
in `main.ipynb`, which states the violation as Eq. (B4); Appendix E's relay supplies it (D5).
Decided by: user (A4, A12). Depends on it: Eq. (20), Appendix B, Appendix E.

**D2. How θ_u is updated.** Instance. `learn_theta_u` settles all three utterances, averages the
gradient, and steps θ_u by (τ_φ/τ_θ) times it. That is Bogacz's trial-wise parameter update (§2.4,
and the last paragraph of §3: a little per trial, after inference) with learning rate
α = τ_φ/τ_θ, batched over three trials. Eq. (20)'s continuous flow is the τ_θ ≫ τ_φ idealization of
the same scheme. Appendix B reports that per-presentation updates reach the same fixed point, from
numbers no cell prints (E7).

**D3. ℓ₀ inside g_L.** Instance under restriction. g_L(φ_S) = ℓ₀·1 − Iφ_S is his Θh(φ) acting on
(φ_S, 1), the 1 being the tonic unit that supplies v_p to his prior error node (Eq. 13, Fig. 3).
The restriction: ℓ₀ is fixed, where his v_p is plastic.

**D4. The fast-end timescale bound.** Instance under restriction. Bogacz assumes the error nodes
are fast relative to φ and states the consequence qualitatively (§5.1 after Eq. 65; Discussion).
τ_ε ≤ τ_φ/(4λ_max(H)) is a quantitative condition inside that assumption, derived here (F14). How
§8.3 attributes it is CF2.

**D5. The relay.** Divergence, recorded in E.2. It is not his §5 interneuron, which removes a
matrix inverse; what carries over is the move of putting the needed quantity into one neuron's
activity. Its locality is argued from his statement of local computation. Decided by: user (A12).
Two comments in Appendix E's code still carry the reading E.2 rejects (CF5).

**D6. The field units are grid samples scaled by √w_k.** Instance under a change of variables.
With φ̃ = W^{1/2}φ, ε̃ = W^{1/2}ε, ℓ̃₀ = W^{1/2}ℓ₀, φ̃_L = W^{1/2}φ_L and B̃ = W^{1/2}B (so B̃ᵀB̃ = I),
Eq. (13) is his F with Σ = σI, and Eqs. (18)–(19) are his Eqs. (53)–(54) exactly: `infer` matches
that system to 1.8e-15 (V3). The prose never states the change of variables, and two of its
statements hold only in it (E1, E2). Decided by: not recorded.

**D7. Closed forms in place of integration.** Surrogate. Agreement where integrated: Part D
1.0e-9 and 9.9e-10, the plane 9.95e-10 (2 of 121 cells), Part A below 1e-8; θ\* against an
independent bisection 4.6e-14. Not shown: that the dynamics reach θ\* (F15). Decided by: agent, of
necessity (I1).

**D8. φ_L clamped.** Instance: φ_L plays the observed input u (v₁) of his Eq. (51). The y level
below it is inert while ε_y ≡ 0.

**D9. The read-out rereads a state vector as a log-density.** **Resolved 2026-09-13** (A16, B7,
`procedure_records/d9_delta_readout.md`): q is a comparison read-out, and the delta at the settled
state is reported beside it. The finding as audited: divergence (interpretive), not
previously registered. **Flagged to the user.** Bogacz's approximate posterior is a delta at φ
(Eq. 34), so the maximizer of F is the whole of his inference. Here that maximizer, φ_S ∈ ℝ^K, is
reread as the log-density of a distribution over s (Eq. 12), and every reported statistic is a
functional of that second distribution. No locality question arises, since the read-out is outside
the dynamics. What rests on it: the temperature ½ of Eq. (15) and so the "tempering"; the reading
of q_lit as a posterior; every verdict of Parts C–D and Text cell 6. The prose says the statistics
are not model quantities (§4.5, §9.1), but not that q is not the framework's variational posterior.
Decided by: not recorded.

**D10. The θ_L gradient pools across word-form units.** **Resolved 2026-09-13** (A17): Appendix A
now states that Eq. (A4) is not local and names the relay. The finding as audited: divergence (locality), not previously
registered, and contradicted by the prose. **Flagged to the user.** Eq. (A4),
∂F/∂θ_L = ε_y·AWφ_L = Σ_i ε_{y,i}⟨a_i, φ_L⟩, sums products formed at |Y| different postsynaptic
neurons. By Appendix B's own criterion for Eq. (B4) that sum is not local, yet Appendix A calls
Eq. (A4) "local on the same terms as Eq. (20)". No reported result depends on it: Eq. (A4) vanishes
while φ_L is clamped.

**D11. The error-unit rate at σ ≠ 1.** Divergence of rate only, not exercised. `infer` integrates
τ_ε ε̇ = r/σ − ε, where his Eq. (54) is ε̇ = r − Σε: the fixed points agree and the relaxation
rates differ by the factor σ. No evaluation overrides a σ, so nothing reported depends on it. It
becomes live if a later phase unfixes σ.

### Citation findings: the tutorial as the prose cites it

| ID | Where | What the notebook says | What the tutorial says |
|---|---|---|---|
| CF1 | Text cell 3 §7, under Eq. (20) | his Eqs. (25) and (29) "are stated at the inference stage, before plasticity is introduced" | Both are in §2.5, after §2.4 *Learning model parameters*, introduced as the update rule for θ and called Hebbian. |
| CF2 | Text cell 3 §8.3 | "Bogacz gives exactly this analysis for the corresponding subsystem (his §5.1, following Eqs. 59–61)" | His eigenvalue analysis (Eq. 66) is of an error node and its interneuron with φ held constant, a subsystem this model does not have. What carries over is his statement that ε converges when φ is slower, and the method. "Exactly" and "corresponding" overstate. |
| CF3 | Appendix B, last paragraph before *Locality* | "the status of the corresponding claim in Bogacz, where inference is convex and plasticity is not" | The tutorial makes no convexity claim, and its running example g(v) = v² is non-convex in inference. |
| CF4 | Appendix A, under Eq. (A4) | Eq. (A4) is "local on the same terms as Eq. (20)" | See D10. Corrected 2026-09-13 (A17). |
| CF5 | Code Cell E1 `relay()` docstring; Code Cell E2 comment above the relay checks | the m-fold pooling "is the sharing Bogacz's Sec. 5 rejects for Sigma" | His §5 removes a matrix inverse. Appendix B dropped this claim for that reason and E.2 says so; the two code comments kept it. |
| CF6 | Text cell 3 Eq. (18); E.1 under Eq. (E3) | error units cite "Eqs. 53–54"; Θ tied to Θᵀ cites "Eqs. 53, 56" | Minor: the error units are his Eq. (54); Θᵀ appears in Eq. (53) and Θ in Eq. (54). |

---

## E. Quantity trace register

**Audited 2026-09-13** at the same commit, by the procedure of `agent.md` §3.3, in two passes.
Every default, module constant and numeric literal in Code Cells 1–4 and E1–E3 was listed and
classed (`constants.txt`). Every number quoted in the markdown was matched against the stored
outputs of both notebooks (`prose_numbers.txt`): of 373, 273 match a stored output, 53 appear only
in `procedure_records/theta_u_learned_reach.md`, and 47 in neither. Setting aside section numbers and coordinate
pairs the matcher misread, 86 have no printed source. The matcher checks value and not provenance,
so a number with few significant figures can match by coincidence.

### What passes

- Every model default in code equals the value the prose states: K = 101, half-width 6, n = 10
  (θ_L = log 19), Λ = 8, μ_u = [1, 1], m = 2 with columns ζ and ζ² orthonormalized against the
  constant, every σ = 1, θ_u learned, θ_u(0) = 0, stopping tolerance 1e-9 with patience 10,
  dt = τ_ε/2, and the bound of commitment 7.
- Every closed form in code is the prose equation, generalized to arbitrary σ and G where the prose
  is written at σ = 1 and m = 1: Eqs. (15)–(16), (21)–(22), (B2).
- q_lit, the tempered control and the model are kept apart in code names (`literal_fixed_point`,
  `theta_u=0.0`, the learned θ_u) and in every printed label.
- Every fixed-θ_u evaluation in Code Cells 2–4 is labelled a control in its output, and each
  matches a row of reach.md §5.C.

### Entries

**E1. The code's H is not −∇²F, as the prose defines it.** Class (e); the code is right and the
prose would change. Text cell 3 (inventory, commitment 7, Eq. 20, §8.3) defines H = −∇²F.
`stiffest_state_rate` computes the Hessian in the coordinates of D6, the quadrature metric, which
is what §8.3's characteristic equation needs, and every quoted λ_max(H) is that one. The two
differ: 3.0000 against 2.0647 at θ_u = 1, and 810.6907 against 809.8088 at θ\* (V2). Eqs. (21)–(22)
are unaffected, since the quadratic form is the same in either coordinates.

**E2. The first line of Eq. (19) is not ∂F/∂φ_S.** Class (e); the code is right and the prose would
change. Differentiating Eq. (13) gives ∂F/∂φ_S = −W(ε_S + ε_L). Eq. (19) writes −ε_S − ε_L, which
is W⁻¹∂F/∂φ_S (V1: a gap of up to 12.2 against the plain partial, 2.2e-16 against the metric one).
Part A's gradient check divides by w_k, so it tests the metric gradient. §8.2's argument that F
rises still holds, in that metric. Stating D6 repairs both E1 and E2.

**E3. The gradient at θ_u = 0 is misstated in three places.** Class (e). Its value is
⟨μ_u, Σ_y c_y⟩/(S·|Y|) = −6.8187, which the learning probe prints (V4).
- Text cell 3 §7 writes ⟨μ_u, Σ_y c_y⟩/|Y|, which is −13.64.
- The `theta_u_learning_probe` docstring writes ⟨μ_u, Σ_y c_y⟩/S, which is −20.46.
- Appendix B writes /(2|Y|) "at σ_L = σ_S": the right value at the model's σ, under the wrong
  condition. It needs S = 2; at σ_S = 3 the value is −3.41, not −6.82.

What these sentences use the value for, that it is nonzero, is unaffected.

**E4. "The elicited prior".** Class (e). **Resolved 2026-09-13** (A15, `procedure_records/e4_e7_sourcing.md`):
reworded at every site, and Text cell 3 §3.4 now gives the user's reason for a Gaussian default.
The finding as audited: The Gaussian of mean 0 and
precision 1 in ζ is called elicited in Text cell 3 (the inventory's "fixed (elicited)", and §3.4),
in Text cell 4 Part C three times, in Appendix B, in the `gaussian_world_prior` docstring and in one
printed line of Code Cell 2. No elicitation source for those values appears in either notebook, and
neither outline reports an elicitation having been run (`sections_3-5_outline.md` line 262 notes
that no human data exist yet). If the prior is a placeholder, calling it elicited borrows an
empirical warrant the model does not have (composition guide Entry 2a).

**E5. Part A's relaxation statistic.** Class (e), minor. Text cell 4 Part A describes the rate as
the least-squares slope of log‖φ_S − φ_S\*‖; the code fits the slope of the log of the largest
derivative over all units. Both decay at the slowest rate asymptotically, but they are different
quantities. The window's comment ("from 1e6 down to 1e3 times the settling tolerance") hard-codes
1e-10, the tolerance before T11; the tolerance is now 1e-9.

**E6. Stale numbers and quotations.** Class (e).
- E.1, under Eq. (E4a): "Code Cell E2 measures the gap at 1.78e-14". The stored output reads
  1.90e-15. Corrected 2026-09-13.
- E.3 *Revised*, sixth row, quotes Text cell 3 §7: "The only departure from Eq. (25) is the
  contraction against b…". No such sentence remains in `main.ipynb`.
- E.3 *Unaffected*: "every number in Code cells 9 and 10" uses the numbering before 2026-09-09;
  they are Code Cells 3 and 4.
- Text cell 2, last sentence: "a discrete analogue of uncertainty learning, where w plays the role
  of a scalar precision". The model learns no precision (A6), and w now names the quadrature
  weights. The pseudocode cell likewise sketches Σ-learning clamped at 1e-3, where the model fixes
  σ at the floor of 1.

**E7. Prose numbers printed by no cell and no recorded script.** **Resolved 2026-09-13** (C6, I10,
`procedure_records/e4_e7_sourcing.md`): every number below is now printed by a code cell. A re-run of the audit
over 365 quoted numbers finds none unsourced; its 9 unmatched are section numbers and coordinate
pairs (`audits/2026-09-13/after_e7/`). Recomputing them corrected several quoted values (F1, F3–F7,
F9 there) and raised F2 and F8, now O5 and O6. The finding as audited: class (e) until sourced. ★ marks
the ones an argument rests on.
- Text cell 3 §2: Gram rank 3, condition number 21.0, θ_L AWX = I₃ to 2.4e-15. A and g_y exist
  only in the prose.
- Text cell 4 Part C: c_some = [+961.66, −529.77] and c_all = [+961.66, +208.51] under the
  delta-like prior ★ (the parity account of the some/all asymmetry); Eq. (23) exact to 1.8e-15;
  Δ_some at most −0.0664 as θ_u → 0.
- Text cell 5: B^TWℓ₀ = [0, −18.5996] (Eq. 30); along μ_u = v[1, 1], θ\* from −143.2577 to −8.8983
  and the contrast from 5.8608 to 5.8152; Δ_some from +0.0080 to +0.0109 and Δ_all from −0.3598
  to −0.2914 at θ_u = 1 across the six settings (Code Cell 3's control table prints E[s], not
  shifts).
- Appendix B: the c_y table (−12.83178, −24.36744; −21.9509, −15.2484, −3.7127); the maximizer
  +22.578 with the signs reversed; cos(μ_u, c) = −0.986, −0.414, −0.167; F̃ = −420.209 and
  ‖r_S‖ = 22.5, 15.8, 22.5; per-presentation updates agreeing with batched ones to 4e-3 at −16.73
  and 1.6e-4 at −24.83 ★ (the basis of "the batching is not load-bearing"); the exposure table of
  seven θ\* ★ (the basis of *Alternative spaces*).
- Appendix C §§3 and 5: the unseen direction [0.512, −0.485, 1.000, 0.043], and the collapses at
  ±6.9e-18. The §7.1 script covers §6 only.
- Appendix D §1: the agreements of 5.3e-15, 1.4e-14 and 4.4e-16 under the T convention. The §7.1
  script computes only ‖r_S‖.
- Appendix E.1: the relay bounds under the other Part D priors (1.18e-3, 8.26e-5, 1.26e-7,
  7.06e-9) and the counts of decreasing F steps (six, fifty-eight, worst −8.35), which appear in
  reach.md's prose and in no recorded script.
- One line of arithmetic from a formula on the page, listed for completeness and not counted:
  log 64 = 4.16; (e⁶ + 1)/2 = 202.21 with θ_L = 5.99894 and 6.00389; δ > 0.004945; the stiffness
  ratios and largest dt in the *Integration cost* table; +0.0075 per unit in Text cell 5 §3.

**E8. The mask sharpness is used but never defined.** Class (a), incomplete.
`exclusion_indicator` builds the smooth mask as the logistic of margin/sharpness, at sharpness 0.1,
0.5, 1 and 2 in Part A, and commitment 6 and Appendix B list the sharpness among θ\*'s inputs. The
prose says only that χ_y becomes a profile in [0,1]^K (§9.2), and defines neither the form nor the
parameter (composition guide Entry 5c).

**E9. Comment drift, including one mirror difference E3 cannot see.** Hygiene (`agent.md` §5.5),
not quantities.
- Code Cell 2 calls the Λ×α sweep "Code Cell 3" in two comments, above `DELTA_ALL_ALPHA` and above
  the third figure. E2 corrected the first and kept the second. E3 compares printed output only, so
  it cannot see comments.
- Code Cell E1's `relay()` docstring says the prose "has NOT yet been lifted to this reading; that
  edit is outstanding". The prose now carries Eq. (B4) and the pointers to Appendix E.
- Changelog wording in code cell 1 ("ell_0 has moved to g_L", "where it coupled to the sum
  ell_0 + phi_L before"), mirrored in E1, and "used to be enough" in E1's `infer` docstring; some
  comments also use " -- " as sentence punctuation.

**E10. Implementation constants not yet recorded.** Class (d); now I9.

**E11. A value that silently assumes defaults.** Class (d), minor. `mu_u_probe` prints
"+0.3333 b_j at theta_u = 1" from a hard-coded 1/3, whatever its `theta_u` argument or σ.
