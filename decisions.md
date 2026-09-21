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
- Decided by: user accepted the relocation (2026-09-06); reasons extended by the user (2026-09-17)
- Decision: the base prior enters as the reference point of the lexical complement (Eq. 9), not in
  g_S. **It is a choice, not a consequence**, and the paper states it as a commitment
  (`thesis_outline/revisions.md` R18).
- Theoretical reason: four, the first recorded in 2026-09-06 and the rest on 2026-09-17.
  1. x ↦ ℓ₀ − x is the order-reversing affine involution on log-weights, the transport of set
     complement; g_L′ = −I, so ε_L reaches φ_S inhibitorily. Its fixed point ℓ₀/2 is a field the
     model settles on (Appendix D §3).
  2. **The user (a).** Putting ℓ₀ at g_S is messy node-wise and the architecture is less clean. In
     exact form: under g_L the entry and the prior meet as one error unit's activity,
     ε_L = φ_L − ℓ₀ + φ_S; under g_S they never meet, and ℓ₀ − φ_L is no unit's activity.
  3. **The user (b).** It is intuitive to hypothesize that the world prior and lexical strength have
     counteractive dynamics. This has empirical content: the two placements are distinguishable as
     soon as σ_L ≠ σ_S, the φ_S difference at a shared φ_u being exactly (σ_L − σ_S)ℓ₀/S.
  4. **Agent, from the measurement below.** Under g_L the literal listener ℓ₀ − φ_L is a fixed point
     of the network (σ_S → ∞); under g_S it is reachable at no σ. Text cell 4 Part C's baseline, and
     the sentence that it is not an external construction built to be beaten, depend on this.
- Implementational reason: none.
- Bogacz status: instance under restriction (ℓ₀ fixed), see D3.
- Depends on it: Eqs. (9), (11), (15), and **Eq. (16)'s coupling c_y = BᵀW(ℓ₀ − φ_L)**, which is the
  one quantity the placement changes; Appendix D; **Text cell 4 Part C's baseline** (reason 4);
  **the Λ = 512 result** — at Λ = 8 the anti-exhaustive shift for *some* is two to three orders of
  magnitude larger under g_S, and at Λ = 512 the conjunction holds under 3 of 5 priors here against
  2 of 5 there.
- Evidence: **`main.ipynb` Code Cell D, *Sec. 5: where ell_0 enters*, which prints them** (task U3,
  2026-09-17, commit 23bdf23; P-1 settled by the user 2026-09-17), so they are no longer class (e)
  under §3.3. The audit behind them, `audits/2026-09-17-ell0-placement/` at commit b548e0a, is the
  derivation and is not what the prose cites.
- **Dated finding, 2026-09-17 (evidence only; A3 is confirmed, not reopened).** The alternative was
  measured rather than argued: `audits/2026-09-17-ell0-placement/` runs variant B (g_L = −φ_S,
  g_S = ℓ₀ + θ_u Bφ_u) against the model, everything else held.
  - The placement changes exactly one quantity, the utility level's drive: c_y = BᵀW(ℓ₀ − φ_L) here
    against −BᵀW(ℓ₀ + φ_L) there. The two differ by exactly 2BᵀWℓ₀ (max 2.8e-14 over the three
    entries) and sum to −2BᵀWφ_L (1.1e-14), so **the entry enters both the same way and the whole
    difference is the sign the prior carries against it**. At σ_L = σ_S the two give the same φ_S
    given φ_u (1.8e-15); φ_u\* differs by 12.3997 at θ_u = 1, and φ_S\* by 3.9996.
  - **Under g_L the literal listener is a fixed point of the network** (φ_S\* → ℓ₀ − φ_L as
    σ_S → ∞, 2.7e-5 at σ_S = 1e6); **under g_S it is reachable at no σ** (σ_S → ∞ gives −φ_L,
    σ_L → ∞ gives ℓ₀ + θ_u Bφ_u). This is a third theoretical reason, and Text cell 4's Part C
    baseline sentence depends on it.
  - The two are distinguishable as soon as σ_L ≠ σ_S: the φ_S difference at a shared φ_u is exactly
    (σ_L − σ_S)ℓ₀/S (6.3063 predicted, 6.3063 measured at σ_L = 2). So a later precision-bearing
    phase tests the placement.
  - The evaluation depends on it: at Λ = 8 the anti-exhaustive shift for *some* is two to three
    orders of magnitude larger under g_S (+0.3405 against +0.0004 on Beta(1,3)), and at Λ = 512 the
    conjunction holds under 3 of 5 priors here against 2 of 5 there.
  - The user (2026-09-17) gave reasons (a) and (b) and decided that the paper states the placement
    as a commitment (`revisions.md` **R18**). **P-7 settled by the user the same day: amend.** The
    reasons and the widened dependency list are folded into the fields above (task U2, closed
    2026-09-17); this finding is kept as the evidence behind them.
  - Variant B's fields are a **counterfactual manipulation (C8)**, not a control: no setting of the
    model produces them. Any cell that prints them must label them so.

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
- Findings added later: 2026-09-13 (agent). The outline revision (`thesis_outline/revisions.md`
  R9, item 2) argues that the slow flow of Eq. (20) never arrives at θ\* (F15) and that, without an
  alternatives level, a mechanism outside F̃ must halt it. A flow halted short of θ\* holds θ_u at
  the halting value, which is not the θ\* this entry defines as learned. Raised with the user as
  revisions.md Q5: either θ\* stays the commitment and halting is an implementation account of
  approximating it, or the halted value becomes the commitment, which would revise this entry. No
  change to the model.
- Findings added later: 2026-09-13, **Q5 settled by the user: θ\* stays the commitment; this entry
  is unchanged.** The user's reason, to be explained in the paper at an appropriate place
  (`thesis_outline/revisions.md` R10): the mathematical model predicts θ\* as the halting value, and
  the simulation exposes a cost problem. No self-contained halting mechanism for the simulation has
  been determined. Every "realizable" θ_u is defined ad hoc, given θ\* already known in closed form.
  A simulated system should be assumed agnostic to that closed-form value, so an ad hoc realizable
  θ_u cannot yet be adopted as the theoretical commitment. Checked against Code Cell 2 (agent):
  `criterion_threshold` bisects on fractions of θ\*, and `realizability_report` computes an arrival
  count only where the conjunction holds at θ\*. `updates_to_criterion` steps Eq. (20) without θ\*,
  but it stops on Part C's criterion, which is a statistic of the read-out q against q_lit outside
  the network, so that stopping rule is not one the simulated system has either.

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

### A19. Halting is by tolerance; the tolerance is ad hoc, and nothing reported depends on it
- Status: Settled
- Decided by: the **user** (2026-09-21), position 1 of the three the audit put to them.
- Decision, in three parts.
  1. **The mechanism is tolerance.** A flow halts when its own update falls below a tolerance. The
     fast loop already works this way (`infer`, I3); the slow flow of Eq. (20) is to be described,
     and coded, the same way: halt when |Δθ_u| < tol.
  2. **θ\* stays the commitment, unchanged** (A9, R10). This is the position the project already
     held; the audit supplies the mechanism that R10 said was missing, and does not move the
     commitment.
  3. **The tolerance itself is ad hoc, and no reported result may depend on it.** Why a computer
     program needs one is that numbers are not represented exactly; whether a living organism needs
     one for the same reason is **not a claim this study makes**. It is also not in scope to
     stipulate a tolerance representative of the brain, and a tolerance need not be uniform across
     inference tasks. What can be argued is that a representative tolerance is almost certainly
     **greater than 1e-9**, so a real system halts **earlier** than the flow's asymptote.
- **Evidence** (`procedure_records/tolerance_halting.md`, findings H1–H7; audit
  `audits/2026-09-21-tolerance-halting/`): the rule is self-contained, using only |Δθ_u| and never
  θ\*; at Λ = 512 every Part D verdict is unchanged for tolerances from 1e-9 to 1; the plane keeps
  33 of 121 and agrees with θ\* in 121 of 121 cells; and 4λ_max(H) falls from about 9e6 to about
  1e4. Two cautions: a coarse tolerance can halt at a slow **start** (H5), and a tolerance near 1e-9
  never fires in any plausible number of exposures (H6).
- **What follows for reporting.** Results stay at θ\*, which is what makes them independent of the
  ad hoc quantity. A tolerance-halted θ_u is not a reported configuration, and any row shown at one
  is labelled as a demonstration of the dynamics, not as a prediction.
- Bogacz status: none. Halting is a property of the flow's stopping rule, not of a message.
- Depends on it: A9 and R10 (the reason θ\* stays the commitment is now stated, not merely
  asserted); I3, whose 1e-9 becomes an instance of the mechanism rather than a numerical detail;
  O3's deferred settling-cost discussion; the planned §5.3.
- **The position in full, the user's six points (2026-09-21), with the measured form of each.**
  1. **Halting depends on tolerance and on nothing else.** No second stopping rule, and **no guard**:
     a guard would need knowledge of the trajectory's shape beyond the unit's local input, which the
     architecture denies it. (Where the flow halts is fixed jointly by the tolerance and by the flow
     the configuration produces; what the hypothesis says is that the **mechanism** is tolerance
     alone.)
  2. **No theoretical commitment to any tolerance.** Results are offered at **1e-1**, an ad hoc value
     for demonstration.
  3. **Early halt under the flat prior at Λ = 8** is an implication of a coarse tolerance. **Measured
     boundary: from 1e-3 upward**, where the row halts in one update at θ_u = 0.0005 and never
     leaves the tempered control; at 3e-4 it still reaches 26.89. (The user's "above 1e-2" is
     conservative by an order of magnitude; the effect begins at 1e-3.)
  4. **Early halt under every Part D prior at Λ = 8** is an implication of a coarser one. **Measured
     boundary: at 1 and above**, where all four halt in one update; Beta(3,1) already does at 3e-1.
     Halting in one update is not the same as never leaving the start: only the flat row does the
     latter.
  5. **The fast loop need not share the slow loop's tolerance.** Coarsening it changes no verdict and
     little runtime (H7), so it is inconsequential and no discussion is spent on it. **The
     implementation keeps 1e-9** (I3).
  6. **Because no value is committed to, the model's predictions are reported in closed form** unless
     otherwise specified. This is what keeps every reported result independent of the ad hoc
     quantity, and it is position 1 restated.
- Evidence for points 3 and 4: block 5 of `audits/2026-09-21-tolerance-halting/output.txt`.
- Tasks: `procedure_records/tolerance_halting.md` §7 (HA0–HA8). **Q-HA1 and Q-HA2 are answered:**
  `learn_theta_u` halts by the committed tolerance, every realizable θ_u is reported at it, and the
  two rules that locate today's realizable values stop defining one.

### A18. The inventory holds at least {χ_y, ker χ_y}; antonymy is not a model primitive
- Status: Settled
- Decided by: the **user** (2026-09-21), closing O8's ensemble half.
- Decision: the exposure ensemble of A9 contains, for any entry, **at least that entry and its
  kernel**: {χ, ker χ}, in Appendix D Eq. (D2)'s sense. **An antonym of x is never needed to define
  x.** A predicate heard with no antonym therefore raises no gap — the ensemble is architectural,
  not lexical.
- Theoretical reason, the user's, recorded as given:
  1. **Antonymy is a consequence, and closer to a coincidence, of learned scalar resolution.** Two
     words happen to share a scale and may then be called antonyms. Nothing in the architecture
     introduces the relation.
  2. **Antonymy is not invertible; the kernel is.** ant(ant(x)) need not be x, and Xiang et al.'s own
     materials show it (F20): *straight* is paired with *bent* and with *curved*, *short* with *long*
     and with *tall*. ker is an involution wherever it closes (Eq. D2), which is what makes it the
     architectural partner and antonymy a lexical accident.
  3. **The architectural partner exists where the lexical one does not.** ker E_all = {1}, the O
     corner of Appendix C §4, which English does not lexicalize (Horn's gap) and which Appendix D §2
     already records as the entry whose complement escapes the family.
- **What this phase may predict, and how far.** In this phase complement(x) may **coincide** with
  ant(x) — it does for Xiang et al.'s absolute pairs — and that coincidence is a prediction of the
  single θ, not a definition. It is stated as such, and not transported (the pattern of O9).
- **Phase note: the stipulation goes partly stale, in the direction of becoming a consequence.**
  Under the proposed architecture of §5.1, with **at most two entries per level**, the two entries
  of a level are strictly boolean complements by construction, so what this phase stipulates the
  next one derives. **This does not conflict with O14's asymmetry:** complementarity holds *within*
  a level, while O14's asymmetry is *across* levels — the 0 boundary fixed by θ_L and the 1 boundary
  by an alternatives level's θ_A. F18's broken parity is a fact about moving one boundary against
  the other, which is a relation between levels, not between the two entries of one.
- **What stays a stipulation here.** That the inventory contains the pair at all is this phase's
  stipulation, in O2's sense, and is labelled as one. This phase models no exposure statistics; it
  declines to derive the inventory and declines to invent frequencies for it (O2).
- Bogacz status: none; this is a statement about what the ensemble of A9 contains.
- Depends on it: A9's ensemble, hence every θ\*; O8; §5.2's ensemble sentence; Appendix D §2's
  kernel table, which is where the notation is defined; §5.1's cascade, already written as
  ⟨E_some, ker E_some⟩ and ⟨E_all, ker E_all⟩.
- Evidence: F20 and F1 in `procedure_records/scale_classes_hypothesis.md`; the ensemble probes of
  `audits/2026-09-13-scale-structure/` (|θ\*| 4.6 to 91 across candidate ensembles, verdicts
  unchanged in what was tested). Tasks: `procedure_records/exposure_stipulation.md` X6–X8.

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
- Status: Superseded in part by B10 (2026-09-14): the two conditions stand as defined; the notebooks take no position that their conjunction is what counts
- Decided by: user (from `sections_3-5_outline.md` §4.2)
- Decision: first condition Δ_some < 0; second q_H(all | some) < ½. Neither alone suffices.
- Depends on it: Part C, Part D table, Text cell 6 *Where both of Part C's conditions hold*.
- Findings added later: 2026-09-17 (agent), the region the second condition is stated over changed
  under **O11**: P(all-region) now takes the closed R = {ζ ≥ θ_L}. B2's own text is unaffected, since
  it states the condition as q_H(all | some) < ½ without naming the region's endpoint, and no printed
  number moved in either notebook.

### B3. Delta-like prior: Beta(64, 1) with Λ = 8α = 512
- Status: Settled
- Decided by: user asked for the test (2026-09-07); the constants' derivation (Λ_crit ≈ α log 2n) is
  not recorded as user-confirmed
- Decision: Beta(64, 1) stands in for the unrepresentable P₀(s = 1) = 1; Λ must rise with α or the
  prior overrides the entry.
- Evidence: the Gaussian prior at Λ = 512 is the control showing the effect is the prior's, not Λ's.
- Findings added later:
  - 2026-09-14 (`procedure_records/evaluation_partD_atStrongLambda.md` F1–F5). With Λ = 512 for all
    five priors, the conjunction holds under three (flat, Beta(3,1), delta-like); every leak falls
    below 1e−174, and the *no*/*all* shifts saturate to zero. The Gaussian control above still reads
    +0.0071, but raising Λ alone does bring two diffuse priors into the conjunction. By B9 the row
    and this derivation move to Code Cell 2b.

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

### B8. The delta read-out carries two criteria of its own
- Status: Settled as a definition. Where and how the paper uses them is open (`thesis_outline/revisions.md` Q2, Q6). Reported without position in the notebooks (B10).
- Decided by: user (2026-09-13)
- Decision: under *some*, (a) mode(φ_S\*) − mode(ℓ₀) < 0, the delta analogue of the shift; (b)
  mode(φ_S\*) outside the cell of *all*, ζ < θ_L (Appendix A). The mode is the grid node where the
  field is largest (B7). They mirror B2's two conditions and are **not assumed equivalent** to them
  (user: "their satisfaction may not be equivalent").
- Theoretical reason: A16. The delta is the construction's posterior, so the criterion needs a
  form stated on it.
- Implementational reason: none yet. No cell prints them (C6), so their numbers are class (e) for
  prose.
  **2026-09-14: now printed** by `delta_readout_report` (Code Cells 2 and 2b; T1 of
  `delta_criteria_printing.md`), under the C7 names mode shift criterion and mode position criterion,
  so their Part D and Text cell 4b numbers are sourced.
- Bogacz status: statistics of the delta read-out (his Eq. 34); the tutorial has no counterpart for
  the criteria.
- Depends on it: revisions.md Q2 (the V under both read-outs), Q6 (R7's supporting sentence).
- Evidence: `audits/2026-09-13-delta-criteria/output.txt`, which reproduces Code Cell 2's Part D rows
  and Code Cell 4's 59 and 33.
  - Part D: the delta criteria agree with B2 row by row.
  - Plane, 121 cells:
    - first conditions 74 (q) against 67 (delta), disagreeing in 35;
    - second conditions 59 and 59, coinciding in every cell;
    - both 33 against 13, every delta conjunction being a q conjunction.
  - mode(ℓ₀) = mode(ℓ₀ − φ_L) in every cell under *some*.
  - Four cells have an unmoved mode.
- Findings added later: 2026-09-13.
  - **The user approved revisions.md Q2 option (a) as R14.** §4.5 reports the V under both
    read-outs, and no evidence for a missing level is derived from it.
  - **The code edits that print these criteria are open tasks** T0–T8 in
    `procedure_records/delta_criteria_printing.md`.
  - **Preliminary, `audits/2026-09-13-delta-criteria/mode_mechanism_output.txt` (record F4).** The
    utility field splits into B's odd (tilt) and even (width) parts. The width is negative in every
    configuration tested and lowers all-region mass in all 121 plane cells. The tilt moves the mode
    up in every cell where it rises (50); the width moves it down in every cell where it falls (67).
    The crossover is a literal mode near s = 0.94. So criterion (a) reads the peak, which the tilt
    governs near the centre, and q's first condition reads the tail, which the width governs. That is
    why they part.
  - **Eq. (24)'s halving, checked across the plane (record F5,
    `audits/2026-09-13-delta-criteria/halving_check_output.txt`).**
    - The utility coefficients k equal (θ/2)(μ_u + (θ/2)c)/(1 + θ²/2) to 1.2e-15, and sit within 1e-3
      of c/2 in 111 of 121 cells. The worst is (1, 2) at θ\* = −6.51, 17% on the tilt.
    - k and c have the same signs in every configuration.
    - The limit field reproduces the model's mode node and all four verdicts ((a), (b), and both q
      conditions) in all 121 cells and Part D's five rows. F4's reading therefore holds cell by cell.
  - **2026-09-14, Λ = 512 for all five priors (`procedure_records/evaluation_partD_atStrongLambda.md`
    F7).** The delta criteria part from q's on two Part D rows for the first time: under the flat and
    Beta(3,1) priors the q conjunction holds and criterion (a) does not (peaks move up to s = 0.917).
  - **2026-09-15. The criteria are printed, and so is the mechanism under them.**
    - T1 (2718404): Code Cells 2 and 2b, mirrored in E2 and E2b, print per row the modes of ℓ₀,
      ℓ₀ − φ_L and φ_S\* in s, the mode shift in s and in grid steps, the two mode criteria beside the
      two q criteria, the gap between the two largest nodes, and the counts and pairwise agreement. At
      Λ = 8 the pairs agree in 4 of 4 rows; at Λ = 512 the shift criteria agree in 4 of 8 and the
      position criteria in 8 of 8.
    - T2 (5ee04a6): Code Cell 4 prints the same criteria over the 121 cells: 67, 59 and 13 against q's
      74, 59 and 33, the 35 cells where a shift criterion and its counterpart disagree, the four
      unmoved modes, the 5.6e-5 smallest gap, and the floors under both read-outs.
    - T3 (27a4122, prose 5a7bc8e): Code Cell C prints the tilt/width split, the plane counts and
      Eq. (24)'s halving, reported in the new Appendix C §8.
    - T6 (af971c4): Text cell 4 Parts C and D, Text cell 4b and Text cell 6 carry the criteria in
      prose, under C7's names and B10's stance.
    - Every number in this entry's *Evidence* and in the F4 and F5 findings above is therefore printed
      by a cell, and the numbers Q2 and Q6 of `thesis_outline/revisions.md` quote are sourced (C6).

### B10. The notebooks report the conditions and take no position on what counts as strengthening
- Status: Settled
- Decided by: user (2026-09-14)
- Decision: "we do not take a position that both conditions need to be met to count as scalar
  strengthening. We are just reporting them so that the reader can make their own judgment. (Any
  positions we take would be left to the paper, not the notebook.)" Part C's two conditions (B2) and
  the delta read-out's two criteria (B8) are reported, each and together, as measurements; no text or
  printed line in `main.ipynb` or `appendix_E.ipynb` says that meeting them, or failing them, is or is
  not scalar strengthening.
- Theoretical reason: the notebook is the measurement record; what counts as strengthening is argued
  in the paper.
- Implementational reason: none.
- Depends on it: Text cell 4 Part C (the criterion paragraph, "Neither is sufficient alone", every
  "verdict" and "criterion met"), Parts D and 4b, Text cell 6, Code Cells 2 and 2b's printed lines
  ("a scalar implicature for \"some\" requires a NEGATIVE shift", "the criterion is NOT met", "Part
  C's verdict"), Code Cell 4's summary; `procedure_records/delta_criteria_printing.md` T1 wording.
- Findings added later:
  - 2026-09-14: the existing prose and printed lines take the position in many places; listed for the
    user, not yet revised (agent.md §5.4).
  - 2026-09-14, the user refined B10: "criterion is kay. Calling it a criterion does not mean we
    commit to this criterion." Naming and wording in C7. Sites revised under
    `procedure_records/b10_no_position.md`.

### B9. Part D's companion at a strong Λ: every prior at Λ = 512, in a cell of its own
- Status: Settled (implementation in progress)
- Decided by: user (2026-09-14), approving S-1 to S-5 and S-7 of
  `procedure_records/evaluation_partD_atStrongLambda.md`
- Decision:
  - A new text cell and code cell ("Text cell 4b", "Code Cell 2b") follow Code Cell 2. They report
    Part D's evaluations with Λ = 512 (B3's Λ = 8α at α = 64) for all five priors and all three
    utterances, each at its own θ_u\* (A9).
  - Part D (Code Cell 2) keeps the four diffuse priors at Λ = 8. The delta-like row, and every block
    that is about it or triggered only by it, moves to Code Cell 2b: the constants and their
    derivation, the Gaussian-at-512 control, the headroom and mechanism blocks, the integrated run and
    the roundoff floor, the delta read-out's realizable rows and boundary check, and the delta-like
    figure (S-2).
  - Code Cell 2b adds two figures at Λ = 512: *no*/*some*/*all* under the Gaussian prior, and *some*
    under all five priors (S-7; reading recorded in the change record, agent, pending user
    confirmation).
  - The change precedes `delta_criteria_printing.md` T1, which then prints criteria (a) and (b) in
    both cells (S-5).
  - The argument of Parts C and D and Text cell 6 is rewritten after the code, against its outputs
    (S-6).
- Theoretical reason: the delta row alone carried Λ = 512, so Part D's table mixed two lexical
  strengths; and at Λ = 8 the diffuse priors override the entries for *no* and *all* (max leak up to
  0.91), so those columns partly measure the override that B3 says a probe must avoid.
- Implementational reason: panels and counts within one cell share one Λ.
- Bogacz status: no new operation; reported statistics of Eqs. (12), (15)–(16) as in B2 and B7.
- Depends on it: Text cell 4 Parts C and D, *Integration cost and conditioning*, Text cell 6, E.1's
  delta-like relay bound; B3, B7, B8, I10.
- Evidence: `audits/2026-09-14-strong-lambda/` (F1–F8 of the change record).
- Findings added later:
  - 2026-09-14, prose pass (change record §6). **Agent drafts, pending user confirmation:** Part C's
    first commitment restated as "strengthening is relative to the prior and to the strength of the
    entry together"; two new reserved positions (the leak of *all* under the Gaussian prior at Λ = 8;
    q's conjunction against the delta read-out's peak under flat and Beta(3,1)); Part C's closing
    claim re-scoped to three of five priors at Λ = 512. Nothing here changes a settled decision.
  - 2026-09-14: **all of the above confirmed by the user**, together with the change record's T1
    implementation choices and the S-7 reading. The user added B10.

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

### C7. The four criteria's names, the stance sentence, and two words not used
- Status: Settled
- Decided by: user (2026-09-14)
- Decision:
  - The first criterion (B2's first condition, B8's (a)) is **the shift criterion**; the second (B2's
    second, B8's (b)) is **the position criterion**. Where the read-out has to be named: **the q shift
    criterion** (Δ_some < 0), **the q position criterion** (q_H(all | some) < ½), **the mode shift
    criterion** (mode(φ_S\*) − mode(ℓ₀) < 0), **the mode position criterion** (mode(φ_S\*) outside the
    cell of *all*).
  - Calling them criteria does not commit the notebooks to them (B10).
  - The words "condition" and "verdict" are not used in the notebooks, for consistency of word choice.
  - Where the prose took a position ("we take …"), it reads, in the user's words: "the reader, in
    accordance with their own judgement, may take satisfaction of the disjunction, the conjunction,
    either one of the two alone, or even neither criteria as scalar strengthening. This notebook takes
    no position on how the criteria should be interpreted." (The instruction wrote "nether"; read as
    "neither".)
- Depends on it: every site of `procedure_records/b10_no_position.md` §2; printed lines of Code Cells
  2, 2b and 4 and of E2, E2b; decisions B2, B8 keep their historical wording.

### C8. "Control" names a manipulation of the model; an algebraic one is a counterfactual manipulation
- Status: Settled
- Decided by: user (2026-09-15)
- Decision: both kinds are controls in nature. The notebooks keep **control** for a manipulation of
  the model, a configuration the network is actually run in with a parameter held off its learned
  value: Part C's θ_u control, Text cell 5's θ_u = 1 tables, the μ_u settings, the m = 1 basis. A
  quantity built by algebra on settled fields, which no setting of the model produces, is a
  **counterfactual manipulation**: Appendix C §8's two single-part fields, the tempered control plus
  the tilt part alone and plus the width part alone.
- Theoretical reason: none. The distinction is for the reader (the user: "for the sake of not
  confusing the reader").
- Implementational reason: `agent.md` §3.3 keeps q_lit, the tempered control and the model apart, and
  B4 lists the retained fixed-θ_u controls in `procedure_records/theta_u_learned_reach.md` §5.C. A
  field that is the tempered control plus part of the utility field would take a third name
  confusable with the second, and would enter that list without matching any run.
- Bogacz status: naming convention; no operation.
- Depends on it: Appendix C §8's prose, Code Cell C's printed block, E14's classing.
- Evidence: no setting of θ_u, Λ, μ_u or B makes the network settle on either field; each is
  φ_S\*(θ_u = 0) plus one column's share of Eq. (23)'s utility field.

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
- Status: Settled; amended in part by I11 (2026-09-14)
- Decided by: agent, confirmed by user (2026-09-13); proposed as DEC3 of `procedure_records/e4_e7_sourcing.md`
- Decision: numbers quoted in Text cells 4 and 5 are printed by Code Cells 2 and 3, inside the
  functions whose output they belong to. Each of Appendices A–D is followed by its own code cell
  (Code Cells A–D; Code Cell A also prints Text cell 3 §2's numbers about g_y). Numbers Appendix
  E.1 quotes that E2 does not print are printed by Code Cell E4.
- Implementational reason: additions to Code Cell 2 go inside existing functions, so Code Cell
  E3's replay needs no new calls; each addition is mirrored into E2 verbatim.

### I11. Code Cell 2b, its mirror, and how E3 finds both
- Status: Settled
- Decided by: agent, confirmed by user (2026-09-14; S-3 and S-4 of
  `procedure_records/evaluation_partD_atStrongLambda.md`)
- Decision:
  - The cells B9 adds are named "Text cell 4b" and "Code Cell 2b" (anchors `tc4b`, `code2b`), so no
    later cell is renumbered. Numbers Text cell 4b quotes are printed by Code Cell 2b.
  - `appendix_E.ipynb` mirrors Code Cell 2b verbatim as Code Cell E2b. E3 replays both and diffs each
    against main's stored output: Code Cell 2 as before (four inserted checks, the pass count),
    Code Cell 2b with no difference allowed.
  - E3 matches its baselines by `# === Code Cell 2:` and `# === Code Cell 2b:`, since "Code Cell 2b"
    also begins with the old prefix `# === Code Cell 2`.
  - E4's relay bound takes the delta-like row explicitly, since Part D's rows no longer include it.
- Implementational reason: amends I10's "E3's replay needs no new calls". E3 keeps its coverage of
  every moved block, including the integrated run, where the relay's path differs.
- Depends on it: agent.md §1 (cell maps) and §2 (couplings 1, 2, 7).

### I12. The mode is the first node of an argmax, and the gap is printed
- Status: Settled
- Decided by: agent, confirmed by user (2026-09-15)
- Decision: the mode of a field is `torch.argmax`, which takes the **first** node when two nodes tie.
  Every block that reports a mode also prints the gap between the two largest values of φ_S\*, so a
  tie would print as 0. Observed smallest: 3.4e-3 over Part D's rows at Λ = 8, 7.8e-3 over Code Cell
  2b's rows, 5.6e-5 over the plane.
- Theoretical reason: none. B7 defines the mode as the largest node and is silent on ties.
- Implementational reason: a tie has to resolve somehow, and B8's mode shift criterion is a strict
  node comparison, so in a tie the tie-break would decide the criterion. Printing the gap makes the
  rule's reach visible instead of assumed.
- Bogacz status: statistic of the delta read-out (his Eq. 34); no counterpart in the tutorial.
- Depends on it: B8's two criteria; Code Cells 2, 2b, 4 and C.
- Evidence: the gaps printed in those cells; `audits/2026-09-13-delta-criteria/output.txt`.

### I13. χ_some is built as the complement of χ_no, not from a margin of its own
- Status: Settled
- Decided by: user (2026-09-16), after the agent reported the divergence
- Decision: `exclusion_indicator` gives *some* no margin of its own. E_some is the complement of E_no
  (Eq. 5), so χ_some = 1 − χ_no, in the step branch and the smooth branch alike. *no* and *all* keep
  their own margins and the shared strict test. Applied to `main.ipynb` code cell 1 and to
  `appendix_E.ipynb` Code Cell E1, which carries a verbatim copy.
- Theoretical reason: Eq. (A1) writes E_some ↦ {ζ ≤ −θ_L}, **non-strict**, because Appendix A's
  Voronoi reading puts the threshold at half a cell and gives the boundary to the endpoint's cell.
  The complement form realizes that exactly, and makes χ_no + χ_some = 1 hold at every node — the
  identity Appendix C §2 and Eq. (C1) rest on — by construction rather than by coincidence.
- Implementational reason: the previous form built *some* from the negated margin of *no* and applied
  the shared `margin > 0`, which yields the **strict** ζ < −θ_L. A single shared comparison cannot
  express Eq. (A1)'s mix of one closed and two open regions; taking the complement keeps one
  comparison and one smooth map while matching Eq. (A1). In the smooth branch the two forms differ
  only as 1 − σ(x) against σ(−x), worst 2.22e-16.
- Bogacz status: no counterpart (input encoding), as A2.
- Depends on it: Eq. (6) and χ_y everywhere; Eq. (C1) and Appendix C §§2, 4; Code Cell 4's override
  threshold table; Text cell 6's quoted θ_u\* range.
- Evidence: `audits/2026-09-16-exclusion-complement/`. Acceptance PASS: step branch identical over
  3000 shipped configurations, smooth branch within 2.22e-16, *no* and *all* bit-identical. At the
  one reachable coincidence χ_some goes 0 → 1, χ_no + χ_some = 1 becomes exact, and the Eq. (C1)
  residual falls from 3.0e-02 to 3.3e-16.
- Findings added later: 2026-09-16 (agent), **the change was not output-neutral, contrary to the
  agent's first report.** `override_threshold`'s `boundaries = (1.0, 2.0, 3.0)` puts θ_L = 3.0
  exactly on node 25 of the K = 101 grid, the only such coincidence anywhere in either notebook. The
  θ_u\* printed for that row moved 14946.06 → 14937.23, and Text cell 6's quoted range moved from
  "13378 to 14946" to "13378 to 14937". **The new value is the correct one**: the old was computed
  with χ_some = 0 at a node where Eq. (A1) requires 1. Every other printed line in both notebooks,
  and every figure, is unchanged.

---

## O. Open decisions

### O1. What fixes the scale's resolution, and so θ_L
- Status: **Settled 2026-09-21** as far as this phase goes, and **dissolved for the next one**.
- Decided by: the **user** (2026-09-21), in two parts.
  1. **This phase does not answer it, and does not need to.** The question is what fixes the
     resolution for a predicate whose atoms are unstable, and no such predicate is a modelled case
     here (the modelled classes are the two absolute ones, R17/S-2). The implementation stipulates
     n = 10, and §5.2's instantiation n = 4, and both are stipulations, said to be such.
  2. **A later phase does not fix it at all.** The resolution is **not a parameter to be chosen**:
     it is a **read-out of a learned θ_L**, recovered by Eq. (A5), n = (e^{θ_L} + 1)/2. This phase
     cannot learn θ_L, because Eq. (A4)'s gradient vanishes identically while ε_y ≡ 0 (φ_L is
     clamped); unclamping the utterance level is what sets θ_L running, and the resolution is then
     whatever the learned threshold implies, per predicate. Stated as the position for the next
     phase, not as a result of this one.
- **Naming, decided in the same breath.** δ and n are **the same quantity** (n = 1/δ), and δ is
  **our own name, not Xiang et al.'s** — their models are LG, QF and ST, and none of them uses it.
  So the dissertation keeps **one name, n**, with a two-part gloss: the atoms a counting predicate
  resolves, and the distinguishable steps of a scale where no count exists, in which case n need not
  be an integer. Eq. (A6)'s separate δ form goes. Tasks: `procedure_records/resolution_naming.md`
  (N0–N8). The clash with the **delta read-out** (A16, B7) is a second reason: "delta" already names
  the posterior of the construction.
- Appendix A derives θ_L from the scale's resolution, ς(−θ_L) = 1/2n (Eq. A5). The implementation
  takes n = 10.
- Findings added later: 2026-09-15 (agent), **this decision is consequential, not cosmetic.** Probing
  n while holding everything else fixed (O10, `procedure_records/side_quests_mirror_and_granularity.md`
  F9) crosses criterion readings: under N(0,1) the q shift criterion for *some* is unmet at
  n = 2…20 and met at n = 50, and under Beta(3,1) the q position and mode position criteria are
  unmet at n = 2, 3 and met at n ≥ 4. So what fixes δ also fixes which side of a crossing the
  reported criteria sit on. n enters only through θ_L = log(2n − 1); K does not track it (I6).

### O2. The exposure distribution p(y) is uniform, and the paper says so
- Status: **Settled 2026-09-21**
- Decided by: the **user** (2026-09-21), choosing option (a) of the four put to them: stipulate
  uniform and label it, rather than argue it from a principle, fit it to corpus frequencies, or
  add a sensitivity sweep.
- Decision: p(y) stays **uniform**, and every result is reported at uniform exposure, said to be a
  **stipulation of this phase** and not a finding. No number moves, since uniform is what the code
  already does.
- **The user's reason, and it holds exactly.** "Essentially the same philosophy as fixing all σ at
  1." Text cell 3 §3 item 3 fixes every σ at 1 because **this phase implements no precision
  inference**, and 1 is the multiplicative identity, so every connection carries equal weight; the
  log σ terms are kept in the objective "only to mark where a later precision-bearing version would
  reintroduce them". Uniform p(y) is the same move for exposure: **this phase models no exposure
  statistics**, so every utterance carries equal weight, and in both cases the stipulated value is
  the one that makes the quantity vanish from the formula — σ = 1 makes ε_y = r_y and the log σ
  terms constant; uniform p(y) makes 3·E_{p(y)}[c_y] the bare sum Σ_y c_y of Eq. (B3).
- **One asymmetry to state, not to hide.** σ is a variable in the code with a default of 1; p(y) is
  not a variable at all, being implicit in the batched sum, so a later frequency-bearing phase adds
  a weight vector where a precision-bearing phase only changes defaults (D11 for σ ≠ 1).
- Theoretical reason: A14 — implicature through θ_u is conventionalized, so the exposure ensemble is
  the mechanism, and its weights are a claim about what a listener hears. This phase declines the
  claim rather than inventing frequencies for it.
- Depends on it: every θ_u\*, hence every reported result; §5.6's prediction that exposure frequency
  shifts strengthening, which is now explicitly a prediction **about departures from the stipulated
  uniform**; Appendix B's "prior over utterances" sentence; O8, which asks the same question about
  ensemble **membership** for §5.2's predicates and inherits this principle.
- **What is not claimed.** Nothing here measures how far a non-uniform p(y) would move θ_u\* or the
  criteria. Code Cell B's *ALTERNATIVE SPACES* block varies ensemble **membership** (θ_u\* from
  −11.2844 for *no* alone to −65.7004 for *all* alone, −28.4375 for the three together), which is
  not the same probe. The sensitivity sweep of option (d) was considered and **not** adopted.
- Tasks: `procedure_records/exposure_stipulation.md` (X0–X5).

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
- Status: **Settled** (user, 2026-09-13). Sense 1 became "exact solvability", sense 3 became "collapses
  a contrast between exclusion sets", and sense 2 keeps "realizability". Opened 2026-09-13.
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
- Findings added later: 2026-09-13 (agent), elaborating the issue at the user's request.
  - **Senses 1 and 2 contradict each other, not only differ.** Appendix B argues that the model's
    θ_u is *not* realizable in sense 1: θ_u μ_u = c would need c ∥ μ_u, and at θ\* the residuals stay
    at ‖r_S‖ = 22.5, 15.8, 22.5 with F̃ = −420.209 rather than 0. Part D's guide and Code Cell 2 then
    call θ_u = 13.3749 "realizable", where the residuals do not vanish either. A reader who meets
    Appendix B's sense first reads Part D as asserting something Appendix B denies.
  - **The two senses have different logical types.** Sense 1 is a property of a generative model
    against data (can it fit exactly), close to learning theory's "realizable case" (to be checked
    before relying on it). Sense 2 is a property of a process (can the dynamics reach a quantity at an
    acceptable cost). Sense 3 is a property of a lattice (is a direction a combination of exclusion
    sets).
  - **Sense 2 also collides with a sense outside the notebooks.** The planned §5.4 argues about
    Marr's levels, where "realization" means implementation in a physical substrate, and the
    philosophical literature uses "multiple realizability". Read in §5.4, "realizable" would be taken
    as "physically implementable", which is near sense 2 but not the same claim: a process can be
    implementable and still cost 7.9e6 in timescale separation.
  - **Sense 2 is itself two quantities.** The least |θ_u| meeting the conjunction (2.126) is where
    the verdict first holds; the θ_u after one update (13.3749) is where the integrated run was done.
    One name for both blurs what §5.3 needs to keep apart: when the verdict is reached, and what
    learning costs after that.
  - **Every candidate replacement for sense 2 carries its own baggage.** "Reachable" (control theory:
    a state some input can drive the system to), "tractable" (complexity theory: polynomial time),
    "attainable" (weak but close), or a descriptive phrase such as "settling cost" (plain, longer).
  - **What renaming costs is uneven.** Senses 1 and 3 live in markdown plus one Code Cell B header.
    Sense 2 lives in a function name, a printed header, row labels and a docstring that E2 copies and
    E3 calls by name, so renaming it means re-running both notebooks.
- Findings added later: 2026-09-13, **senses 1 and 3 renamed by the user** (record
  `procedure_records/o7_renaming.md`).
  - Sense 1 → **"exact solvability"** (agent's proposal, approved by the user). Appendix B's
    preceding sentence already says θ v_p = u "is solvable". Changed: Appendix B's two sentences, and
    Code Cell B's header, now `EXACT SOLVABILITY AT theta_u*`. Rejected: "exact fit", because in the
    outline "fit" means fitting a model to data.
  - Sense 3 → **no term. The user's wording, "collapses a contrast between exclusion sets"**, matches
    existing usage (Text cell 5 Part A, "collapse {some, all}"; Appendix C's table, "collapses").
    Appendix C §7 now reads "$m=2$ collapses no contrast between exclusion sets" and "$m=1$ *does*
    collapse a contrast, the one between *some* and *all*". It is exact: every non-constant
    {−1,0,1} combination of intervals is χ_A − χ_B for two exclusion sets, and it lies in the unseen
    subspace iff the projection maps A and B to the same point. Rejected: "expressible" (Appendix C
    §1 uses it for the span, which §7 contrasts with the lattice) and "representable" (already used
    for s = 1 and in Appendix A, and the planned §5.4 argues about representation).
  - **O7 stays Open for sense 2**, which is now the only use of the word. R10 of
    `thesis_outline/revisions.md` adds that every "realizable θ_u" is located by the evaluator,
    using θ\* or Part C's criterion, not by the simulated system.
- Findings added later: 2026-09-13, **sense 2 settled by the user: the cost sense keeps
  "realizability" as it is; no change.** Code Cell 2, E2, E3, Text cell 4 Part D, B7 and O3 stay as
  written, and the interim rule above lapses. With senses 1 and 3 renamed, the word now has one sense
  in the notebooks. The outline may use it in that sense, keeping R10's point that a "realizable
  θ_u" is located by the evaluator.

### O8. θ_u\* and Λ for a single-predicate configuration (§5.2's probe)
- Status: **Settled 2026-09-21**, in both halves: Λ by the user's S-9 and the narrowing below, the
  ensemble by decision **A18**. Raised 2026-09-14.
- Decided by: not decided. Raised by the agent while re-examining `thesis_outline/sections_3-6.md`
  §5.2 (`thesis_outline/revisions.md` Q7).
- **The question.** A9 requires every configuration to carry its own θ\*, the maximizer of F̃ over an
  exposure ensemble. §5.2 evaluates predicates the notebooks do not contain (one threshold at an
  arbitrary cut), so two things are unfixed:
  1. **The exposure ensemble.**
     - Candidates: the predicate alone; the predicate and its complement; the predicate within a
       scale inventory.
     - Measured for the first two (`audits/2026-09-13-scale-structure/output.txt`): |θ\*| from 4.6
       to 91 across the tested priors and cuts, and E_q[s] contributions within about 5% of Eq. (24)'s
       limit. So the verdicts there do not depend on this choice; the numbers do, slightly.
  2. **Λ.** At Λ = 8 the Gaussian priors override endpoint cuts: q-mass on the excluded states is
     0.62 to 1.0 from s_t = 0.95 up. Options:
     - hold Λ at 8 and report the leak;
     - raise Λ per configuration until the entry is held, by an override threshold analogous to
       Eq. (41), which is derived for Beta(α, 1);
     - restrict comparisons to held entries.
- **Narrowed 2026-09-21.** The old line — "the user's choice on both, before any §5.2 number is
  printed" — was too broad. The ensemble half is answered for the modelled paradigm (the finding
  below), and the Λ half is settled for §5.2 by **S-1** (Λ is fitted, for H1 alone, labelled).
  **Settled 2026-09-21 by the user:**
  1. **§5.2 fits one Λ per class, not per (class, image type).** The user's reason, recorded as
     given: *a constrained model should carry as few fitted quantities as possible*. Fitting per
     image type would entail the stipulation that lexical strength depends on both class and image
     type, **and the user does not argue that stipulation is implausible** — there is no obvious
     reason it is. The paper therefore **opts out of the extra fit; it does not claim the dependence
     is absent.** §5.2 must be worded so: never "Λ does not depend on image type", only "we did not
     fit one". The two best-fitting values within the minimum class (shapes ≈ 6, artifacts ≈ 24,
     F9) are reported as a property of the fit, not as a second fitted parameter.
  2. **Λ outside the fitted setting:** a configuration holds its own stated Λ and **reports the
     leak** (B6: headroom before shifts), rather than raising Λ per configuration until the entry
     holds or restricting comparisons to held entries.
- **The user's principle, 2026-09-21, which governs how the ensemble may be argued.** What the
  inventory contains is **independent of what a participant met in one experiment**: presence in the
  inventory follows from exposure in the experiment, but **not the converse**. An adjective absent
  from a participant's trials is still in their lexicon. So no ensemble claim may rest on the
  experimental design, in either direction.
- **Checked 2026-09-21 (F20 in the scale-classes record).** Xiang et al.'s Experiments 2 and 3
  distribute the 96 items by latin square "such that the same participant did not see both
  adjectives that were paired to the same image set", 24 trials each, artifact and shape on separate
  groups; Experiment 1 elicits the priors with **no adjective at all**. So the {χ, 1 − χ} ensemble
  **cannot be argued from exposure in the experiment**; by the principle above it does not need to
  be, and it is argued instead from the inventory a speaker has.
- **The ensemble half is closed, 2026-09-21, by the user → new decision A18.** The ensemble is
  architectural: it holds at least {χ, ker χ}, and an antonym is never needed to define an entry, so
  the no-antonym case is not a gap. {χ, 1 − χ} in Xiang et al.'s paradigm is that pair, with ant(x)
  **coinciding** with ker(x) for those absolute classes — a prediction of this phase's single θ, not
  a definition, and not transported (O9's pattern). That the inventory contains the pair at all is
  this phase's stipulation, labelled as one (O2).
- **O8 is therefore settled in both halves.** Nothing in it blocks T0–T13.
- **Depends on it:** `sections_3-6.md` §5.2, §5.4, §6 item 4; `background_sections.md` §1.7.
- **Finding, 2026-09-17** (record `procedure_records/scale_classes_hypothesis.md`, raised under
  O13). **The ensemble question has an answer wherever the predicate is tested against an antonym.**
  In Xiang et al.'s paradigm every item pairs an adjective with its antonym, and in the uttered
  adjective's own orientation that antonym is the entry's **complement**: for a minimum-standard
  adjective the partner is *no* = 1 − χ_some, for a maximum-standard one it is the O corner
  1 − χ_all. So the exposure ensemble is {χ, 1 − χ}, which is one of the two illustrative ensembles
  already measured on 2026-09-14, and no further choice is needed **for that paradigm**. It says
  nothing about a predicate heard with no antonym.
  **The Λ question is sharper, not settled.** Fitting the model to those 96 items gives a different
  best Λ for each class (max: any Λ ≥ 8; min ≈ 32; rel ≈ 16), and within the minimum class a
  different best Λ for each image type (shapes ≈ 6, artifacts ≈ 24). Holding Λ at 8 for every
  configuration is therefore a choice the data argue against, and raising Λ per configuration until
  the entry is held would erase the one prior effect the data show (F8, F9).

### O9. Is the O corner {1} as representational as {0}?
- Status: **Settled 2026-09-21**
- Decided by: the **user** (2026-09-21), on the measurement below. Raised by the user as a side
  quest 2026-09-15, with the answer wanted as a sense rather than in full. Record:
  `procedure_records/side_quests_mirror_and_granularity.md`.
- **Decision.** The reflection is exact (finding 1), so **this implementation predicts that the O
  corner is just as representational**. The prediction is read as a fact about the implementation as
  it stands: it is **not transported to the proposed next phase**, where {0} and {1} stop being
  fixed by the same θ and become asymmetric (**O14**, the user's instinct). Any statement of the
  prediction carries that limit with it.
- **Where it is stated:** the paper, not the notebooks (B10, C7). `thesis_outline/sections_3-6.md`
  Tier B's O-corner bullet carries it; Appendix C §4's aside stands unchanged. If the prose quotes a
  number for the equivariance, C6 requires a cell to print it first — today the 7.11e-15 lives only
  in the audit, so state the prediction qualitatively or print it.
- **The question.** Appendix C §4 records that E = {1}, the O corner, costs the architecture
  nothing. The sharper form: does an inventory {*no*, *not all*, *all*} behave exactly as the
  mirror of {*no*, *some*, *all*}?
- **What is measured** (record F1-F5). Write R for the reflection ζ → −ζ and P = diag(−1, +1) on the
  (tilt, width) coordinates.
  1. **As representation, yes, exactly.** Rb₁ = −b₁ and Rb₂ = +b₂, so RB = BP and BᵀWR = P BᵀW;
     Rχ_no = χ_all and Rχ_some = χ_not all exactly. The model built on (inventory, ℓ₀, μ_u) and the
     model built on (mirrored inventory, Rℓ₀, Pμ_u) are reflections: the same θ_u\*, and φ_S\*, φ_u\*
     related by R and P, to 7.11e-15 under N(0,1) and under Beta(3,1) ↔ Beta(1,3).
  2. **As behaviour, no, and μ_u is the only reason.** The grid, W, b₁, b₂ and the default
     ℓ₀ = N(0,1) are R-invariant or of definite parity; **μ_u = 1 is not**, since Pμ_u = (−1, +1).
     At the stipulated μ_u, θ_u\* is −28.4375 on {*no*, *some*, *all*} against −19.7219 on
     {*no*, *not all*, *all*}, and under Beta(3,1) ↔ Beta(1,3) it changes sign, +55.0081 against
     −17.0332. The settled fields differ by only about 5e-2, because Eq. (24)'s limit k → c/2 is
     independent of θ_u, its sign included.
- **Resolved against the options raised 2026-09-15:** (a) as far as the notebooks go — Appendix C
  §4's aside stands and nothing new is claimed there; the paper adds the prediction and its limit.
  Option (c), what a principled μ_u for a mirrored scale would be, is **not** taken up; finding 2
  stays on record as the measured asymmetry, with our position reserved.
- **Depends on it:** Appendix C §4's aside; A5's stipulation μ_u = 1; nothing currently printed.
- Evidence: `audits/2026-09-15-side-quests/output.txt`. Class (e) under `agent.md` §3.3 until a cell
  prints it (C6).

### O10. Does the number of atoms n change what the evaluation reports?
- Status: **Addressed 2026-09-21** (user: "O10–O14 already had been addressed"). The measurement
  below is the answer and is not reopened. **One task it leaves:** the finding lives only in
  `procedure_records/side_quests_mirror_and_granularity.md`, and the user asked that how the
  evaluation varies with n be **reported in both the notebook and the paper** — tasks **T14–T16**
  of `procedure_records/scale_classes_hypothesis.md`, with the placement question **S-8** there.
  Until a cell prints them, these numbers are class (e) under `agent.md` §3.3.
- Decided by: the measurement is the agent's, raised by the user alongside O9; same record.
- **The question.** The implementation takes n = 10 (O1). Would three atoms, or exactly two, change
  essential results, and is the model degenerate at two?
- **What is measured** (record F6-F10):
  1. **n enters in one place only:** θ_L = log(2n − 1). K does **not** track n, being an accuracy
     parameter for the quadrature and not a state space (I6, Text cell 3 §1). θ_L < the grid
     half-width caps n at 201.
  2. **Nothing structural moves.** At n ∈ {2, 3, 4, 10, 50, 100} the three χ_y have rank 3, and
     rank 2 modulo the constant, so there are still two thresholds and m = 2 stays exactly right
     (Eq. C2). θ_u\* moves smoothly and keeps its sign.
  3. **n = 2 is not degenerate.** χ_some ≠ χ_all, the two thresholds stay distinct, and 19 grid
     nodes lie strictly between them. Degeneracy is at n = 1, where θ_L = 0 and the entries for
     *some* and *all* coincide; the constructor already rejects it.
     **Finding, 2026-09-17 (under O14):** that degeneracy is a property of the **single θ**, not of
     n. Eq. (A1) built with the 0 boundary at −θ_L and the 1 boundary at an independent θ_A keeps
     χ_some ≠ χ_all and keeps the Gram rank at 3, 2 modulo the constant, at n = 1 (record F19). The
     constructor's rejection of n < 2 is right for the model as it stands and would not be for a
     separated pair.
  4. **But the reported criteria cross with n**, which is the substantive answer: see the dated
     finding under O1.
- **Needed to decide:** O1 first. Until what fixes δ is settled, every criterion reading carries an
  unquantified dependence on a number nothing fixes.
- **Depends on it:** O1; Text cell 4 Parts C and D; Text cell 6's plane; every criterion reading.
- Evidence: as O9. Class (e) until a cell prints it (C6).

### O11. Eq. (27)'s all-region is open where its own gloss, and the rest of the notebook, are closed
- Status: **Settled** (user, 2026-09-17; record `procedure_records/all_region_closed.md`). Opened
  2026-09-17 while applying I13.
- Decided by: user (2026-09-17), choosing option 2 below: "the formula needs to be changed".
- **Decision.** Eq. (27)'s all-region is the **closed** R = {ζ ≥ θ_L}. Applied to 23 mask sites
  (14 in main, 9 in appendix_E), 3 printed labels, and the two prose statements in Text cell 4
  (the Eq. (27) definition, and "the region ζ ≥ θ_L is s ≥ 0.95"). All four regions are now closed
  at the endpoint, the all-region is the mirror of the no-region under O9's reflection, and it
  coincides with Appendix A's cell of *all* — which O12 records as a redundancy to resolve later.
- **Measured outcome.** No printed number moved anywhere in either notebook: the only differing
  printed lines are the 5 occurrences of the two relabelled headers. All 13 figures byte-identical;
  main 0 errors, 8 figures, 14/14; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS. The change is
  inert because no grid node lands on +θ_L for any θ_L the notebooks use, at any K in the ladder.
- **The framing below is how the question was put to the user on 2026-09-17, kept unedited**
  (`agent.md` §3.1: a decision's body is never rewritten after the fact). Its present tense
  describes the notebook as it stood before the change.
- **The disagreement.** Text cell 4 defines P(all-region) over R = {ζ > θ_L}, "where *all* is true".
  But *all* excludes E_all = {ζ < θ_L} (Eq. A1), so it is true on the **closed** {ζ ≥ θ_L}. Formula
  and gloss disagree at the single node ζ = θ_L.
- **The rest of the notebook already takes the closed form.** "The cell of *all*" is computed as
  `zeta >= theta_L` everywhere it appears: the mode position criterion (C7), Code Cell C's
  χ_not all, and the peak-of-ℓ₀ report. P(no-region) is closed too, R = {ζ ≤ −θ_L}. Eq. (27)'s
  all-region is the only open one of the four.
- **It also breaks the reflection of O9.** {ζ ≤ −θ_L} reflects to {ζ ≥ θ_L}, not to {ζ > θ_L}, so as
  written the no-region and the all-region are not mirror images of each other.
- **The options.**
  1. *The gloss is loose; keep the formula.* Reword "where *all* is true" to name the open region.
     Costs nothing computed, but leaves Eq. (27) inconsistent with the cell of *all* used elsewhere,
     and the two regions unmirrored.
  2. *The formula is wrong; make it R = {ζ ≥ θ_L}.* Restores the mirror, matches Eq. (A1) and the
     cell of *all*, and makes all four regions closed at the endpoint. This changes the definition of
     a **reported statistic**, and with it the q position criterion (B2, C7), which is why it is the
     user's call.
- **What option 2 would cost, measured.** Nothing printed, on the static evidence: the all-region is
  computed only at θ_L = log 19, and no grid node lands on ±log 19 at any K in the ladder (closest
  4.4e-03, at K = 201/401/801). The override table's θ_L = 1, 2, 3 — where θ_L = 3.0 *does* sit on a
  node — takes a leak from χ_no and never an all-region mass. **Authoritative confirmation is a full
  printed-output diff after the change, not this scan**: the equivalent scan gave three false
  all-clears before I13.
- **Depends on it:** Eq. (27); the q position criterion in Text cell 4 Part C and in Code Cells 2,
  2b, 4 and C; B2's conjunction; O9's symmetry statement.

### O12. The all-region and the cell of *all* are now the same set
- Status: **Settled** (user, 2026-09-17; record `procedure_records/all_region_closed.md`). Opened
  and settled the same day; recorded first, at the user's direction, before being acted on.
- Decided by: user (2026-09-17), in their words: "resolve the redundancy in prose. In code,
  preserve both 'upper_region' and 'inside', but add a comment next to the declaration statement of
  'upper_region' explaining that this is identical to 'inside' by implication of our theoretical
  commitment; however, it is left as a separate variable in case a reader want to experiment with
  different definitions."
- **Decision**, the second option below. **In prose**, the identity is stated once, in Text cell 4
  Part C where the all-region is introduced: the threshold of Eq. (A5) makes the all-region
  Appendix A's Voronoi cell of *all*, so the two names carry one region, *all-region* where a
  q-mass is taken over it and *cell of all* where a mode is placed against it. Part D's
  "Where the peak sits against the cell of *all*" now refers to Part C instead of re-deriving the
  cell. **In code** both variables stay, with a three-line comment at the canonical declaration of
  `upper_region` (Code Cell 2's `demonstrate`, mirrored in E2) recording that the two masks coincide
  by the threshold of Eq. (A5), and that the pair is kept so either definition can be varied on its
  own. Both names survive, so C4 is untouched.
- **The framing below is how the question was recorded on 2026-09-17, kept unedited**
  (`agent.md` §3.1). Its present tense describes the notebook before the prose was resolved.
- **What happened.** O11 made Eq. (27)'s all-region R = {ζ ≥ θ_L}, which is exactly Appendix A's
  Voronoi cell of *all*. One set now carries two names and two implementations:
  - **code:** `upper_region = (zeta >= theta_L)` (14 sites in main, 9 in appendix_E) beside
    `inside = zeta >= theta_L`, the cell-of-*all* masks (3 in main, 3 in appendix_E). They now
    evaluate identically at every node.
  - **prose:** Text cell 4's "The all-region is the continuous form of the top state" and "Where the
    peak sits against the cell of *all*" define the same region twice, in the same terms.
- **Options.** Unify under one name and one helper; keep both names but state the identity once in
  prose; leave as is.
- **Needed to decide:** the user's choice of name (C4). "All-region" runs through Text cells 4, 4b
  and 6 and `thesis_outline/sections_3-6.md`; "cell of *all*" carries Appendix A's Voronoi reading
  and is what B8's mode position criterion is stated against.
- **Depends on it:** nothing computed — the two already evaluate to the same mask, so this is naming
  and duplication, not a result.

### O13. Does lexical strength follow the stability of the predicate's atomicity?
- Status: **Addressed 2026-09-21** (user). How the dissertation treats it is settled by **R16**:
  §5.2 states H1, reports match and mismatch against Xiang et al. (2022), and makes no claim about
  the nature of the mismatch. The hypothesis itself is **not adopted** as a decision about Λ, and
  the entry stays as the record of that. Implementation: T0–T13 of
  `procedure_records/scale_classes_hypothesis.md`. Raised 2026-09-17.
- Decided by: not decided. Raised by the **user**, as a hypothesis to be checked before it is
  adopted: "1. scalar expressions with unstable atomicity are associated with weaker lexical
  strength; 2. open-scale adjectives behave similar to *some*; complete scale adjectives behave
  similar to endpoint(s)+*some*." Record: `procedure_records/scale_classes_hypothesis.md`.
- **What it would change.** Λ and θ_L are two independently fixed quantities of Text cell 3 §3
  (A5 gives θ_L its denotation through n; §3 item 6 fixes Λ = 8 "if not said otherwise"). H1 makes
  Λ a **function of how stably the predicate fixes** n, or δ in the gradable case of Eq. (A6). That
  is a new dependency between two fixed quantities, and it would give the Λ axis of the Λ×α plane a
  linguistic reading it does not now have: a position on it would be a property of the expression.
- **H2 needs no new machinery.** In each adjective's own orientation Eq. (A1) already supplies the
  three entries: maximum-standard absolute = *all*, minimum-standard absolute = *some*, and the
  antonym the expression is paired with is that entry's complement (for *some* it is *no*, for
  *all* it is Appendix C §4's O corner). A relative adjective needs one thing the model does not
  have: a cut at a context threshold t that is neither endpoint nor δ/2, so **t would be a second
  quantity beside θ_L**, and Appendix A's identification argument (θ_L A W X(θ_L) = I, "θ_L enters
  twice") is stated for a θ_L that is both the gain and the cut. That is the structural cost of H2.
- **What is measured** (record F1-F13, `audits/2026-09-17-scale-classes/`). Instantiating the five
  scale positions of Xiang, Kennedy, Xu & Leffel (2022) as the five Voronoi cells of n = 4:
  1. **H2's class-to-entry map is the one their data show**, class by class (F2).
  2. On their own 96 items with their own elicited priors, the model's posterior-degree R² is 0.81
     overall against their LG 0.78 and QF 0.82, and by class 0.95 / 0.40 / 0.80 (max / min / rel)
     against LG .94/.55/.69 and QF .97/.58/.78 (F3, F4). The literal listener alone gives
     .95/.09/.20, so the utility level is what earns the fit off the endpoint (F5).
  3. **H1's ordering is supported in the form "a finite Λ is required".** The maximum class's fit
     is flat from Λ = 8 to Λ = 2048; the minimum class peaks at Λ ≈ 32 and the relative class at
     Λ ≈ 16, both falling away above (F6).
  4. **H1 in a within-class form is what the one credible image-type effect asks for.** The model
     puts that effect in the minimum class and nowhere else, as the data do, but at one seventh of
     its size, and no single Λ fits both halves of that class: shapes want Λ ≈ 6, artifacts Λ ≈ 24
     (F8, F9). m = 3 and m = 4 do not help.
  5. What the model does not reproduce: the minimum class moves the belief up from the prior by the
     same ~2.1 positions in both conditions, and at fixed θ\* the model moves it to a place, not by
     a displacement (F10).
- **Needed to decide:** the user's, on three things. (a) Whether Λ becomes a function of anything,
  or stays a fixed quantity with the classes distinguished by their entries alone. (b) If it does,
  what fixes it — the record shows the data want it to vary with the object's familiarity as well as
  with the expression, which is a context dependence Λ does not now have. (c) Whether a relative
  adjective's cut t enters the model at all, which is what H2's open-scale half requires.
- **Depends on it:** `sections_3-6.md` §5.2 and §5.4, `background_sections.md` §1.7, revisions.md
  Q7; the reading of the Λ axis in Text cell 6 and Code Cell 4; A5's θ_L and §3 item 6's Λ = 8.
- Evidence: `audits/2026-09-17-scale-classes/output.txt` and `xiang_items_output.txt`. Class (e)
  under `agent.md` §3.3 until a cell prints it (C6); no cell does.
- **Finding, 2026-09-17 (later the same day).** The user has directed how §5.2 presents this, which
  narrows O13 without closing it: "state both H1 and H2, then report where the model's prediction
  match Xiang's data as well as where it doesn't. Refrain from making any claims on the nature of
  this mismatch. Every data quoted in this section must be reproducible. Add a new appendix F to
  main.ipynb printing the model results quoted in this section." So **the paper states H1 and H2 as
  the hypothesis under test and reports the comparison; whether the model adopts a Λ that varies
  with atomicity is still open here**, and the difference matters: a variable Λ would be a change to
  Text cell 3 §3, while a scanned Λ is a control (B4). Seven decisions block the implementation,
  listed as S-1 to S-7 in `procedure_records/scale_classes_hypothesis.md` §8; S-1 (whether a fitted
  Λ may be quoted, and what class of quantity it is) and S-2 (whether the relative cut *t* enters
  the model) are the two that reach back into this entry. **Both are now answered** (same record, §8): Λ is
  fitted for H1 and nowhere else, and *t* does not enter — the relative class is not modelled, so
  H2's open-scale half is stated and left untested (**O14**).

### O14. Are the two endpoints symmetric, or does the 1 boundary belong to another level?
- Status: **Addressed 2026-09-21** (user), in the same sense as O13: the treatment is settled and
  the question is not. **O9 now depends on it** — this implementation's prediction that the O corner
  is just as representational is explicitly not carried into the asymmetric phase this entry
  describes. Raised 2026-09-17. **What is settled** is how the paper treats it: §5.2 points
  to it as an instinct, once, promising nothing, and the relative class is not modelled with the
  current implementation (record `procedure_records/scale_classes_hypothesis.md` §8, S-2).
- Decided by: the instinct is the **user's** (2026-09-17), in their words:

  > even though we currently model the two endpoint as symmetric to each other, I do not think it is
  > actually the case. Recall our motivation for an alternatives level; under this proposed
  > architecture, the 0 and the 1 would no longer be defined by the same theta, but instead theta_L
  > and theta_A. I think our current model's symmetricity is the culprit of mismatch that we have
  > with Xiang's data. My instinct is that n can be properly represented by the architecture
  > (particularly as one of theta_L or theta_A) once the two thetas are separated from each other.
  > However, we want to avoid making too many promises in the paper over things we haven't
  > implemented yet, so my take is that we point to this intinct and leave it as an instinct.

- **Which level each boundary belongs to** (the user's clarification, 2026-09-17): "theta_L is the
  lexical level's property, and only theta_A is meant to be the alternative level's property. The
  lexical level infers the boundary of 0, and the alternative level infers the boundary of 1." So
  the pair does **not** live at one level: θ_L stays where it is, and only the 1 boundary moves.
- **What the model does now.** One θ_L fixes both ends: Eq. (A1) sends *no* to {ζ > −θ_L}, *some* to
  {ζ ≤ −θ_L} and *all* to {ζ < θ_L}. The first two are the 0 boundary and would be untouched; it is
  the third that would read {ζ < θ_A}. Eq. (A5) already gives n its denotation through the **0**
  boundary, σ(−θ_L) = 1/2n, and the user confirms n stays with θ_L: "As for n, we my instinct is
  that it is still dependent on theta_L." **What the separation would represent is t**, the relative
  class's midpoint — "the midpoint t of the relative class can be properly represented by one of
  theta_L or theta_A" — the quantity S-2 found nothing in the present model fixes.
  Eq. (A2) makes θ_L the gain of g_y as well as a cut, which is what identifies it (Appendix A,
  *θ_L enters twice*); θ_A would need an identification of its own.
- **The symmetry is exact, and it holds only because one θ does both ends.** At n = 4 the entries
  for *all* and *some* have identical tilt loadings and exactly opposite width loadings (difference
  0.0e+00, sum 0.0e+00), so at the utility level the two differ in the even coordinate alone. Moving
  the 1 boundary alone destroys it: at θ_A = 1.25 θ_L the tilts differ by 0.089 and the widths no
  longer cancel (+0.091); at θ_A = 2 θ_L, 0.470 and −0.158. O9 records the neighbouring fact that
  the whole construction is equivariant under ζ → −ζ, with μ_u the single asymmetry.
- **What separating them would change.** Appendix A's sentence that Eq. (A1) excludes the states
  outside each anchored cell "symmetrically at both ends"; the identification argument, which would
  have to be given for θ_A too; Appendix C's count, which counts thresholds (C2) and would now count
  two that need not be symmetric, so Appendix C §5's parity table is rebuilt; O11 and O12, since the
  all-region R = {ζ ≥ θ_L} and the cell of *all* would both become {ζ ≥ θ_A} and their identity
  needs rechecking; and §5.1, which is where an alternatives level able to carry θ_A is proposed.
- **Which of §5.2's two classes sits on which boundary**, as Eq. (A1) already stands: the minimum
  class is *some*, fixed by the **0** boundary, and the maximum class is *all*, fixed by the **1**
  boundary. That is bookkeeping about the present model, not a claim about the instinct.
- **n = 1.** The user adds: "since an architecture with an alternatives level has different
  dynamics, it is well possible that n=1 no longer causes degeneracy." Measured (record F19):
  **representationally this already holds.** O10's degeneracy at n = 1 is a property of the single
  θ, not of n — with the boundaries separated, θ_L = 0 leaves χ_some ≠ χ_all and the Gram rank stays
  3, 2 modulo the constant, so Eq. (C2) still counts two thresholds. The dynamical half is untested
  and stays an instinct. One obstacle the rank test does not reach: θ_L is also the gain of
  Eq. (A2), so θ_L = 0 zeroes the word-form prediction unless the separation also decides which θ
  gains which row of A.
- **Needed to decide:** nothing now. This is recorded so the instinct is not lost and is not
  overclaimed. Nothing in the notebooks depends on it, and no result here rests on it.
- **Depends on it:** `sections_3-6.md` §5.2's closing sentence and its pointer to §5.1. Nothing
  computed.
- Evidence: `audits/2026-09-17-scale-classes/xiang_items_output.txt` block 16(e) for the symmetry,
  and `procedure_records/scale_classes_hypothesis.md` F18 for what breaks it;
  the mismatch it is an instinct about is F8 to F10 and F17 of the record. **No measurement here
  tests the instinct**, and §5.2 does not say that it accounts for the mismatch (R16).

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

**E12. Code Cell 2b's quantities (added 2026-09-14, B9).** Classed by the agent, confirmed by the
user 2026-09-14.
- `STRONG_LAMBDA` = `DELTA_ALL_LAMBDA` = 512: class (c), a stated departure from the model's Λ = 8,
  justified by B3's override threshold and B9. Every row of Code Cell 2b carries it and the table
  prints it.
- The table, tempering/utility split, condition counts, realizability thresholds and delta read-out
  rows: class (b), the statistics of B2, B7, Eqs. (25)–(27) and (37), computed by Code Cell 2's
  functions.
- `strong_lambda_comparison` and `headroom_report`: class (b), the same statistics side by side
  (B6's headroom, for every row).
- `cell_margin_report`'s "nodes below" and "inside against outside": class (b) under B7's boundary
  check, extended from the delta-like row to every row. Not yet defined in prose: Text cell 4b is a
  scope paragraph until the prose pass.
- Every number Code Cell 2b prints is class (e) for prose until Text cell 4b or Parts C–D quote it
  against the executed output (`procedure_records/evaluation_partD_atStrongLambda.md` §5).

**E13. Part D quoted all-region masses no cell printed (found 2026-09-14, prose pass F15).** Class (e),
resolved. q_lit under *some* (0.0504 flat, 0.1368 Beta(3,1)) and the tempered control (0.0066, 0.1357,
0.2356) were quoted at four decimals and printed by no cell. `base_prior_sweep` now prints the
all-region masses of q_lit, the tempered control and the full network beside the tempering/utility
split, in Code Cells 2 and 2b (and E2, E2b).

**E14. The quantities T1-T3 added (2026-09-15).** Classed by the agent; the naming of the two
single-part fields is the user's (C8).
- Code Cells 2 and 2b (and E2, E2b): the modes in s, the mode shift in s and in grid steps k\* − k₀,
  the two mode criteria and their conjunction, the gap between the two largest nodes, and the counts
  and agreement: class (b), statistics of the delta read-out (B7, B8), defined in Text cell 4 Part D.
- The grid spacing printed in that block's legend: class (d), read from the grid of I6 rather than
  stored as a constant.
- Code Cell 4, `lambda_alpha_sweep`: per cell under *some*, the mode nodes of φ_S\*, ℓ₀ and ℓ₀ − φ_L,
  the modes of φ_S\* and ℓ₀ in s, whether φ_S\*'s mode lies outside the cell of *all*, and the
  smallest top-2 gap of the three fields: class (b). `plane_summary`'s counts, agreement, the 35-cell
  table and the six floors: class (b). Signs are read with I5's zero band.
- Code Cell C, `utility_split_report` (Appendix C §8): the tilt and width coefficients of the utility
  field, the span-B residual, the two slopes at the tempered control's mode, the modes and all-region
  masses of the four fields, the plane counts, the distances from c/2, the Gram and exact-form
  errors, and the limit field's mode and criteria: class (b), statistics of Eqs. (15), (16), (23) and
  (24) defined in Appendix C §8.
- The two single-part fields, the tempered control plus tilt alone and plus width alone:
  **counterfactual manipulations** (C8), controls in nature but not manipulations of the model, since
  no setting of θ_u, Λ or μ_u produces either. Their printed numbers are class (b). B4's list of
  retained fixed-θ_u controls is unaffected, since neither field is an evaluation the model is run in.
- Appendix C §1 writes every projection per unit Λ; §8's coefficients are the exception, each at its
  configuration's own Λ and θ_u\*, and §8 says so.
- Code Cell 2b's own quantities stay under E12, and E13's masses are unchanged.

**E15. The quantities Code Cell D's Sec. 5 adds (2026-09-18, task U3 of
`procedure_records/ell0_placement_and_counterforce.md`; entered 2026-09-21 in U14, having been
missed when U3 closed).** Classed by the agent. Nothing here is class (e): every number the prose of
Appendix D Sec. 5, §3.2, §3.3 and §4.1 quotes is printed by this block.
- The couplings c_y under Eq. (9) and under Eq. (D5), per utterance, and the two identities
  c(g_L) − c(g_S) = 2BᵀWℓ₀ and c(g_L) + c(g_S) = −2BᵀWφ_L: **class (a)**, c_y being Eq. (16)'s
  quantity and Eq. (D7) naming the identities.
- BᵀW1, ⟨1, ℓ₀ − φ_L⟩_W per utterance, and c_y's invariance to an additive constant on the field:
  **class (a)**, projections of Eq. (3) taken on Eq. (15)'s field, defined in Appendix D Sec. 5 and
  quoted by §3.3 as R19's warning.
- The σ-limit table, max |φ_S\* − (ℓ₀ − φ_L)| at σ_S = 1e6 and σ_L = 1e6 under both placements:
  **class (a)** in the fields compared; the two σ settings are **controls (c)**, labelled as such,
  and θ_u = 1 there is a fixed-θ_u control under B4, also labelled.
- The same-φ_u agreement, the (σ_L − σ_S)ℓ₀/S difference, and the φ_u\*/φ_S\* gaps at θ_u = 1:
  **class (a)**, with the same two controls.
- Part D's five priors under both placements at Λ = 8 and Λ = 512 — θ\*, q_lit, q_H, the shift and
  the two q criteria: **class (b)**, Text cell 4's statistics (Eqs. 25–27, 37) computed by Code
  Cell 2's own `criterion_for_some`.
- **The alternative placement itself** (g_L = −φ_S with g_S = ℓ₀ + θ_u Bφ_u, Eq. D5, and every field
  and θ\* built from it): a **counterfactual manipulation (C8)**, not a control, since no setting of
  the model produces it. The cell's labels and the prose both say so, and B4's list of retained
  fixed-θ_u controls is unaffected.
- Bogacz status: Eq. (D5) has Eq. (9)'s, an instance under restriction (A3, D3), so §3.2 registers
  no new divergence.
