# Revisions to the thesis outline

Plan for revising `sections_3-6.md` and `background_sections.md`, written 2026-09-13. **Neither
outline has been edited.** This file lists what is stale, what is new, where each change goes, and
what the user still has to decide (§7). Numbers are quoted from the executed `main.ipynb` unless a
source is named; §8 says where each is printed.

---

## 0. Instructions (the user's, verbatim, 2026-09-13)

First message:

> the outline files in thesis_outline\ are stale in some contents since they were last updated
> before the changes recorded in theta_u_learned_reach.md. Specifically, after the change, we have
> found that the evaluation gives close form theta_u produces a posterior that satisfy both criteria
> (verify this). We need to change the outline in accordance with this updated finding. However,
> this updated finding does not undermine the motivation we provided for an added alternatives
> level, since the motivation mainly comes from the complexity it saves. There are several other
> added implications that should be discussed in the paper:
>
> 1. the two forms of read-out we provided in the codes and the theoretical assumptions that each
> entails.
> 2. the realizability issue and what it bears on our commitment to neural plausibility. Firstly, we
> had earlier wanted to claim that a halting mechanism is supplied by the maximizer of F. Given the
> realizability finding, this is not true any more. We would need a standalone halting mechanism if
> we don't implement the proposed alternatives level.
> 3. On a philosophical level, these points illustrate why attempts on algorithmic representation is
> needed besides computational representation. Under a computational modeling, all the questions
> raised above would be collapsed.
>
> based on these, would you propose what parts of the current outline files need to be changed?
> Don't edit the outlines themselves yet.

Second message:

> Increase the word budget for sections3-6 from 2400 words to 3000 words. Update agent.md for the
> correct file path. Compile your plan above into a revisions.md and place it under thesis_outline/
> directory. The possible link between q normalization and section5.1 is worth stating. The
> terminology clash needs to be handled more carefully, so mark it as open decision. For language
> use regarding "collapsed", I agree that it is too strong and invites criticism, say "not posable"
> instead.

## 1. Decisions this plan rests on

| ID | Decision | Decided by |
|---|---|---|
| R1 | The word budget for §§3–6 rises from 2,400 to 3,000 (§3 below). | user (2026-09-13) |
| R2 | The motivation for the alternatives level is the complexity it saves. That motivation does not depend on the criterion failing, so the level stays. | user (2026-09-13) |
| R3 | The paper discusses the two read-outs, realizability and halting, and why an algorithmic account is needed. | user (2026-09-13) |
| R4 | The link between q's normalization and §5.1's binarity argument is stated (§5, item 1). | user (2026-09-13) |
| R5 | Where the computational level cannot express a question, the text says the question is **not posable** there. It does not say the question "collapses". | user (2026-09-13) |
| R6 | The three uses of "realizability" are an open decision, `decisions.md` **O7**. Until O7 is settled, the outline does not introduce the term in a new sense. | user (2026-09-13) |

Decisions in `decisions.md` this plan relies on: A9–A11 (θ_u learned, start 0, timescale
commitment), A14 (conventionalized), A16 and B7 (q is a comparison read-out; the delta is the
construction's posterior), A17 (Eq. A4 non-local), B1–B2 (baseline and criterion), C3 (three
objects kept apart), O3 (the bare outline pointer).

## 2. The finding, checked

**The user's claim holds, with a narrower scope.** At each prior's own closed-form θ\*:

| prior | θ\* | q_lit | q_H(all \| some) | Δ_some | tempering | utility level | first | second |
|---|---|---|---|---|---|---|---|---|
| Gaussian | −28.44 | 0.0016 | 0.0025 | +0.0008 | +0.0175 | −0.0167 | no | yes |
| flat | +5950.63 | 0.0504 | 0.0799 | +0.0295 | +0.0854 | −0.0559 | no | yes |
| Beta(1,3) | −14.51 | 0.0001 | 0.0005 | +0.0004 | +0.0065 | −0.0061 | no | yes |
| Beta(3,1) | +55.01 | 0.1368 | 0.1788 | +0.0421 | +0.0988 | −0.0568 | no | yes |
| delta-like | +1407.77 | 0.9568 | **0.4351** | **−0.5217** | −0.0586 | −0.4631 | **yes** | **yes** |

(q_lit has no θ_u, so its column is unchanged from the outline's table.)

- **Scope.** Both conditions hold under **1 of Part D's 5 priors**, the delta-like one, and in
  **33 of the 121 cells** of the Λ×α plane. They do not hold under the four diffuse priors.
- **Not only in closed form.** The conjunction first holds at |θ_u| = 2.126 under the delta-like
  prior, and holds from there all the way to θ\*. An integrated run at the θ_u = 13.3749 that one
  update of Eq. (20) reaches gives Δ_some = −0.5182 and q_H = 0.4386, with nothing in closed form.
- **Wording.** Under A16 both conditions are stated on q, which is a read-out kept for comparison.
  The construction's posterior is the delta at φ_S\*. The outline says "the read-out q meets both
  conditions", never "the posterior satisfies both criteria".

Two further findings that change the outline as much as the headline does:

- **The utility level's own contribution is negative under all five priors** (reach.md F8, now
  printed). The positive shifts under the four diffuse priors are tempering alone.
- **The halting claim is not written anywhere.** Neither outline, neither notebook and no record
  says that the maximizer of F supplies a halting mechanism. So item 2 is new material, not a
  correction of existing text.

## 3. Word allocation at 3,000

| Section | Was | Now | What the change pays for |
|---|---:|---:|---|
| **3. The proposed architecture** | **800** | **920** | |
| 3.1 What the model must do | 90 | 90 | |
| 3.2 A continuous world state and a soft lexicon | 160 | 160 | |
| 3.3 The chain, and the semantics of its threshold | 200 | 200 | |
| 3.4 State units, error units, and what is local | 210 | 230 | Commitment 7 in exact form; θ_u learned, starting at the tempered control; conditioning |
| 3.5 Two choices the scale forces | 140 | 140 | |
| 3.6 Two read-outs (new) | — | 100 | Item 1 |
| **4. Evaluation** | **745** | **890** | |
| 4.1 What is compared | 100 | 110 | Naming (literal listener, tempered control) |
| 4.2 The criterion, and how to read the statistics | 170 | 170 | |
| 4.3 The specification holds | 90 | 90 | |
| 4.4 The five priors (retitled) | 220 | 240 | New table with tempering/utility split |
| 4.5 The plane, and where both conditions hold | 165 | 180 | Conjunction thresholds across the band |
| 4.6 What the verdict needs, against what θ\* costs (new) | — | 100 | The evidence item 2 rests on |
| **5. Discussion** | **705** | **1,040** | |
| 5.1 What an alternatives level would have to supply | 390 | 410 | Complexity-led; the q-normalization link |
| 5.2 Scale structure: a second prediction | 200 | 200 | |
| 5.3 Settling cost, halting, and the plausibility commitment (new; title subject to O7) | — | 170 | Item 2 |
| 5.4 What an algorithmic account makes posable (new) | — | 120 | Item 3 |
| 5.5 Limits (was 5.3) | 65 | 80 | Convergence of θ_u; conditioning |
| 5.6 Predictions (was 5.4) | 50 | 60 | The timescale separation as a prediction |
| **6. Conclusion** | **150** | **150** | |
| **Total** | **2,400** | **3,000** | |

**Renumbering this causes.** Limits and Predictions move from §5.3 and §5.4 to §5.5 and §5.6, so
four references change: `sections_3-6.md` lines 57, 63 and 77 (§5.3 → §5.5) and
`background_sections.md` line 392 (§5.3 → §5.5). §5.2 keeps its number, because the background
refers to it throughout.

**Conflict with the background (question Q3, §7).** `background_sections.md` lines 13–14 plan
3,595 words and leave "roughly 2,400 of a 6,000-word dissertation" for §§3–6. At 3,000 the total is
6,595.

---

## 4. `sections_3-6.md`, site by site

### Header and central claim

- **Line 4–5, scope line.** "Approximately 2,400 words" → 3,000. "Code cells 1–4, Appendices A–D"
  → add Code Cells A–D.
- **Lines 23–32, constructive claim. Rewrite.** It rests on "exactly one condition holds under every
  prior tested, never both and never neither", which is false at θ\*. Proposed basis, per R2: the
  architecture meets the criterion, under a concentrated prior and across a band of the plane. The
  case for a level representing alternatives is what that level would save:
  - branching logarithmic in the predicate's granularity;
  - one dimension per level, so plasticity is local without the relay;
  - an affine generative map that keeps the convergence proof;
  - a read-out that needs no normalization across the scale (item 1, §5 below);
  - a structural end to inference, which the present architecture lacks (item 2).

  "The pattern is the shape of its absence" is withdrawn, or kept only as the weaker point in Q2.
  The specification-not-built sentence (lines 28–32) survives unchanged.
- **Lines 34–37, standing qualification.** Survives.

### Scope tiers (lines 41–77)

- **Tier A.** The criterion row (line 52): "the spine of the constructive claim" → "the verdict,
  and the evidence that the conjunction is reachable". Relay row (line 57): §5.3 → §5.5, and "the
  cost it carries" → "τ_r ≤ τ_ε only" (F26). **Add** three rows:
  - the two read-outs, placed at §3.6 and §4.1, because they fix what a verdict is stated on;
  - commitment 7 and conditioning (Eq. 28, §8.3), placed at §3.4, §4.6 and §5.3, because they are
    the evidence for item 2;
  - the conjunction threshold against θ\*, placed at §4.6 and §5.3, because it is what dissolves
    the maximizer-as-halting claim.
- **Tier B, line 63.** §5.3 → §5.5.
- **Tier C, lines 74–77.** Remove "Conditioning and stiffness (Eq. 28)", which moves to Tier A.
  §5.3 → §5.5.

### Word allocation table (lines 81–103)

Replace with §3 above.

### §3.4 (lines 166–196)

- **Line 170.** τ_ε ≪ τ_φ ≪ τ_θ → τ_ε ≤ τ_φ/(4 λ_max(H)) ≪ τ_φ ≪ τ_θ (A11, Text cell 3
  commitment 7). The bound is critical damping of the stiffest mode and scales as θ_u⁻².
- **Add:**
  - θ_u is learned per configuration and starts at θ_u(0) = 0. There the network is the
    **tempered control**, not q_lit (A10, C3).
  - Strict concavity secures convergence for every θ_u, but conditioning governs whether that
    convergence is reachable: condition number about (1+θ_u²)/2, 404.8 at the Gaussian θ\*. This
    sentence sets up §4.6 and §5.3.
- **Lines 193–196, the relay's cost. Rewrite per F26.** Under commitment 7 the relay adds no
  stability requirement of its own. It needs only τ_r ≤ τ_ε, and the reason is monotone F, not
  oscillation. It inherits θ_u⁻² from τ_ε rather than carrying its own. Eq. (E6) keeps ≤, with the
  exception that at equality F is monotone under *some* only (O6).

### §3.6 Two read-outs (new, about 100 words)

Content in §5 below, item 1. It sits in §3 because it is a commitment about what the model outputs,
and §4.1 needs it.

### §4.1 (lines 218–232)

- **Line 222.** "Untempered literal posterior" → "untempered literal listener". Add one sentence
  saying that "literal" here denotes something distinct from what it denotes in RSA and the Gricean
  literature, with no further explanation (DEC5 of `procedure_records/d9_delta_readout.md`).
- **Lines 226–229.** "The θ_u=0 control" → "the tempered control". Add that it is also where
  learning starts.
- **Line 230.** q_H is the settled belief *read through q*. Point to §3.6.

### §4.2 (lines 234–253)

- **Lines 236–240.** Add one sentence that both conditions are stated on the read-out q (A16).
- **Lines 247–253, the guard.** Both measured instances are fixed-θ_u controls. Under learning the
  φ_S-contrast deviation across μ_u settings is 3.19e-2 (not 3.6e-15), and Δ_some's spread across
  the six μ_u settings collapses to +0.0008 to +0.0009 (Text cell 5 Part B). Either restate the
  guard with the invariance "at fixed θ_u", or take the instance from the learned model: the
  φ_S contrasts across Part D's priors agree to 3.6e-14 at a shared θ_u and differ by 0.0575 at each
  prior's own θ\*.

### §4.3 (lines 254–263)

- "Exact to 6.0e-11" → about 1e-9 (9.98e-10), since the stopping tolerance is now 1e-9 (I3).
- Grid tails "1.6e-3 … 1.8e-6" → 1.7e-3 and 3.3e-6.
- Add: θ\* from Eq. (B2) matches an independent bisection to 4.6e-14, and Eq. (20) ascends from 0.

### §4.4 (lines 265–297): rewrite

- **Title.** "One condition, every time" → e.g. "The five priors".
- **Table.** Replace with §2's table, with a θ\* column. Tempering and utility can be columns or one
  sentence.
- **Line 277.** "The conjunction holds under none" → holds under the delta-like prior alone. The
  four diffuse priors meet only the second condition. No prior meets neither.
- **Lines 280–286, decomposition.** "The utility level's own contribution is small and of either
  sign" is false. It is negative under all five, and the four positive shifts are tempering.
- **Lines 287–289, anti-exhaustive direction.** The shifts are still positive on four priors, but
  the utility level runs the other way. What this section says depends on Q1.
- **Lines 290–297, mechanism.** Survives. The Eq. (24) limit is −0.5217 and that prior's own θ\*
  delivers −0.5217.
- **Add one sentence** pointing to §4.6: the verdict is shown in the dynamics, not only in closed
  form.

### §4.5 (lines 298–317)

- **The band.** 22 cells → **33**; band (8,128)–(128,2048) → **(1,512)–(128,2048)**. The
  delta-like row is inside the band, at its lower edge in Λ.
- **Floors.**
  - First condition: Λ ≥ 512 at α = 1, 64 at α = 8, 16 at α = 64, and 2 from α = 128 to 512.
    At α = 1024 it reads 2048, which is the saturated row.
  - Second condition: Λ ≥ 2 up to α = 8, 64 at α = 16, 256 at α = 32, 512 at α = 64, 1024 at
    α = 128, and unreachable past α = 256.
  - The opposition of the two floors survives as the result.
- **Override law.** Learned slopes 1.9890 / 2.9334 / 4.3102, +36–45% over the tempered control
  ("severed" means that control). The 15–18% at θ_u = 1 is a control and is labelled as one, or cut.
- **Spread D.** 0.0061 → 0.0009 → 0.0002 becomes 0.0057 → 0.0012 → 0.0003.
- **Add.** Across the 33 cells the least |θ_u| meeting the conjunction runs from 0.100 to 4.250,
  with λ_max(H) between 2.0 and 20.1 there, so every cell is integrable at the θ_u its verdict
  needs. At their own θ\* the same cells have λ_max(H) between 3.5e4 and 3.6e7.

### §4.6 What the verdict needs, against what θ\* costs (new, about 100 words)

Evidence for §5.3, reported without interpretation:

- Under the delta-like prior the conjunction first holds at |θ_u| = 2.126, where λ_max(H) = 6.5
  and commitment 7 demands a separation 4λ = 26. Eq. (20) from 0 passes that θ_u in one update.
- The integrated run (39,035 Euler steps at θ_u = 13.3749) gives Δ_some = −0.5182 and
  q_H = 0.4386.
- The same inference at θ\* = 1407.77 would take 4.28e8 steps, hours, at a separation of 7.9e6.
- The Eq. (20) flow from 0 is not integrable to θ\*: it is not within 0.1% of θ\* after 5,000
  updates (F15). That θ\* is reached rests on the closed form and the monotone rise.

### §5.1 (lines 322–435)

- **Framing (lines 324–327).** Lead with the complexity argument (R2). Lines 344–397 survive
  intact: the negative search, what is searched versus what branches, the binary inventory, the
  *most* case, the dimension and locality payoff, and binarity at the generative map.
- **Lines 329–338, "Why the pattern points at such a level".** Its premise, never both, is gone.
  Keep at most one sentence on the opposing floors, depending on Q2.
- **Lines 339–343, the Cremers corroboration.** Depends on Q1.
- **Add after lines 388–397: the read-out link (R4, about 40 words).** Content in §5 below, item 1.
- **Lines 398–420, what is not derived.** Survives. Add to its list, or to §5.3, that a structural
  end to inference is also a claim about the unbuilt level.
- **Lines 422–431, the position on the current gain.** Survives. **Before quoting**, confirm that a
  cell prints the four exposure-only θ\* values (−11.28, −44.18, −65.70, −28.44) (C6). They are
  not in this plan's sources.
- **Lines 432–435, standing qualification.** Survives.

### §5.3 and §5.4 (new)

Content in §5 below, items 2 and 3.

### §5.5 Limits (was §5.3, lines 478–489)

- **Line 480–482.** θ_u convergence: from θ_u(0) = 0 the flow rises monotonically to θ\*. This
  holds in 145 of 145 configurations tested, by Appendix B's root argument. The flow is not
  integrable to θ\*, and θ\* is supplied in closed form.
- **Line 485.** "A fourth timescale scaling as θ_u⁻² (Eq. E6)" → τ_r ≤ τ_ε, inheriting θ_u⁻² from
  commitment 7.
- **Add.** Conditioning, and the separation commitment 7 demands, as a limit on plausibility
  (points to §5.3).

### §5.6 Predictions (was §5.4, lines 490–500)

- **Add one bullet.** Commitment 7 predicts error units at least 4λ_max(H) times faster than state
  units: 26× at the delta-like threshold. The prediction is conditional on this architecture
  without an alternatives level, and should be worded as such.

### §6 Conclusion (lines 503–518)

- **Item 3 (lines 511–516). Rewrite.** "Satisfies only one of the two conditions … under every
  prior tested" is false. Proposed: the network reaches the conjunction under a concentrated prior
  and across a band of the plane, at a |θ_u| of a few units. But what it pays for this, and the
  absence of any end to the computation other than an unreachable maximizer, are what a level
  representing alternatives would change. The rest of item 3 (the design and what is not derived)
  survives.
- **Add a clause** for item 3 of §5 below (not posable at the computational level), if §6's budget
  allows.

### Open items (lines 539–569)

- **Line 552.** `background_sections_outline.md` is now `background_sections.md`.
- **Add.** A pointer to this file.

---

## 5. The new material

### Item 1. The two read-outs (§3.6, about 100 words; link in §5.1, about 40 words)

**The delta at the settled state** (Bogacz §3, Eq. 34; A16).

- *Assumes:* the posterior is a point mass at (φ_S\*, φ_u\*). This is the Laplace/delta commitment
  the construction inherits (background §2.2, commitment 3).
- *Supplies:* the settled vector itself. No normalization, so the read-out is local.
- *Does not supply:* masses or expectations. Neither condition of the criterion has a direct
  analogue. The natural one is the Voronoi cell the peak of φ_S\* falls in (Appendix A).

**q** (Eq. 12; A13, A16).

- *Assumes:* φ_S codes unnormalized log-weights over the scale.
- *Supplies:* a normalized density, and with it every mass statistic and the RSA comparison. Both
  conditions are stated on q.
- *Costs:*
  - the normalizer Σ_j w_j e^{φ_S,j} sums across every node, so no unit could form it from its own
    afferents;
  - it sits outside the dynamics and takes no part in Eq. (20);
  - nothing in the architecture dictates it.

**What follows, all printed by Code Cell 2 (THE DELTA READ-OUT block):**

- **The mode is shared.** The peak of φ_S\* is also q's mode, since the exponential and the
  normalizer do not move it. The read-outs differ in what needs the normalizer.
- **Tempering is invisible to the delta.** Halving φ_S does not move its peak. So the
  tempering/utility confound in Δ is a property of q.
- **They can disagree in direction.** Under *some*:

  | | Gaussian | flat | Beta(1,3) | Beta(3,1) |
  |---|---|---|---|---|
  | ℓ₀ peak (s) | 0.50 | 0.50 | 0.25 | 0.75 |
  | learned peak (s) | 0.59 | 0.67 | 0.33 | 0.84 |

  The learned peak is up the scale of the ℓ₀ peak under all four diffuse priors, while the utility
  level's contribution to all-region q-mass is negative under each.
- **"Outside the cell of *all*" is already true of ℓ₀ alone** under those four priors (the cell
  starts at s = 0.95). Only under the delta-like prior does the model move the peak out: from
  0.9852 to 0.9468, one node below θ_L. It stays outside on grids of 201, 401 and 801 nodes.

**The link to §5.1 (R4).** q's normalizer is a normalization across a represented set, which is the
operation Appendix A says would not be local and §5.1 says binarity absorbs.

- **The second condition is binary already.** q_H(all | some) < ½ is the statement that the
  log-odds of the all-region against its complement is negative. That is a sign on a single
  opposition, and it is exactly the opposition ⟨E_all, ker E_all⟩ that one level of §5.1's cascade
  carries.
- **What binarity would give.** A level carrying that opposition as one log-odds unit reports the
  second condition as that unit's sign, with no normalization across the scale.
- **The qualification, stated in the same place, on the pattern of A17.**
  - A log-odds of two cell masses cancels the global normalizer but still sums within each cell.
  - The saving is complete only if the level's state is that log-odds unit.
  - Whether φ_a's value equals q's cell log-odds is part of the g_a algebra §5.1 already declares
    not derived.
  - The first condition, a difference against q_lit, has no such binary form.

### Item 2. Settling cost, halting, and the plausibility commitment (§5.3, about 170 words)

The section's title and its term for the cost sense wait on **O7**. The content:

- **Two halting questions, kept apart.**
  - *Fast:* at fixed θ_u, inference converges to the unique maximizer of F (§8.1). Convergence is
    guaranteed. The stopping rule in the code (a tolerance of 1e-9 on the largest derivative) is a
    numerical surrogate (I3), not a mechanism of the model.
  - *Slow:* θ_u's flow ascends F̃ toward θ\*.
  - The claim the user had in view concerns "the maximizer of F". Q4 asks which one it meant; the
    section should say which it addresses.
- **Why the maximizer cannot halt the process.** The verdict is fixed at |θ_u| = 2.126, within one
  update. θ\* is not reached in any feasible run (F15; 4.28e8 steps at θ\* under the delta-like
  prior). Convergence to θ\* therefore neither happens in time nor marks the point at which anything
  is decided.
- **Consequence without the alternatives level.** A standalone halting mechanism is needed. It is
  not a term of F, has no counterpart in Bogacz (2017), and would need its own locality argument and
  an entry in the Bogacz divergence register.
- **With the level.** A binary cascade ends when the scale is resolved to the predicate's
  granularity, after a number of levels set by n. That is a structural end. It is a claim about a
  level specified and not built, and must be worded as such (§5.1's lines 398–420 apply).
- **Neural plausibility.** Even at the threshold, commitment 7 demands a 26× separation between
  error and state units and tens of thousands of Euler steps per inference. At θ\* the separation is
  7.9e6. That is the cost the plausibility commitment (background §2.1, §2.7) has to answer for, and
  it is the argument main.ipynb's *Integration cost and conditioning* defers to the outline.
- **The cross-reference this repairs.** Text cell 4 says the question "is left where it is posed,
  in the background outline", and O3 cites `sections_3-5_outline.md` 3.4, 3.4.3 and 5.3. Neither
  current outline contains a settling-cost argument: §5.1's complexity case is about branching,
  not settling time. This section becomes the pointer's target. The pointer itself stays bare (O3).

### Item 3. What an algorithmic account makes posable (§5.4, about 120 words)

- **Claim.** Each question above is **not posable** at the computational level (R5). A
  computational theory specifies the posterior and is silent on resources and representation. So:
  - there is one posterior, and no choice between a delta and a normalized read-out;
  - θ\* is the answer however long it takes to reach, so the gap between the verdict's θ_u and θ\*
    does not exist;
  - there is no computation whose end could be asked about;
  - the ½ tempering, which comes from representing the utility level at finite σ_S, has no
    counterpart.

  The questions arise only once representations and a process are specified. Background opening
  move 3's definition extends from "a pattern the computational goal does not entail" to "a question
  the computational level cannot pose".
- **Counterargument to anticipate.** Resource-rational analysis brings costs into a
  computational-level analysis (Griffiths, Lieder & Goodman, 2015; Lieder & Griffiths, 2020).
  Answer: it prices a process, and so still needs one specified. The questions are posable there
  because an algorithm has been supplied, which is the point.
- **Guard.** Do not say the computational level is wrong or that these questions refute RSA.

## 6. `background_sections.md`

- **Lines 13–14, scale.** 2,400 → 3,000 for §§3–6. The total then exceeds 6,000 (Q3).
- **Lines 57–64, opening move 3.** Add the "not posable" clause (item 3) and a forward pointer to
  §5.4. One sentence.
- **Lines 189–192, §1.3 Beat 3 forward pointer.** Depends on Q1. As written ("exhibits the same
  anti-exhaustive direction on four of five priors, and treats the fact as corroboration") it
  misdescribes the utility level at θ\*.
- **§1.8 synthesis (lines 337–352).** Optional. One clause that the traditions share a
  computational-level framing under which the questions of §5.3 are not posable.
- **Lines 368–373, §2.1 claim levels.** The algorithmic claim now carries commitment 7, whose
  measured separation is a plausibility liability. One sentence, pointing to §5.3.
- **Line 392, §2.2 table, commitment 3.**
  - "§5.3 records as a limit" → §5.5.
  - Add that the Laplace/delta commitment is what makes the delta at φ_S\* the construction's
    posterior (item 1).
- **Lines 454–458, §2.4.** "Appendix E pays a fourth timescale to keep it at m>1" → the relay adds
  a time constant bounded only by τ_r ≤ τ_ε (F26).
- **Lines 483–490, §2.6.**
  - The ordering becomes τ_ε ≤ τ_φ/(4 λ_max(H)) ≪ τ_φ ≪ τ_θ.
  - Add that θ_u starts at 0, at the tempered control.
  - "Appendix E adds a fourth timescale" → as in §2.4.
- **Lines 524–528, §2.7 close.** "A testable consequence in the required speed of the relay" is
  stale. What a slow relay breaks is monotone F, a non-monotone transient. The implementational
  commitment with content is commitment 7's separation itself.
- **Reference list.** Add, marked **[verify]** as the list does for other entries:
  - Griffiths, T. L., Lieder, F., & Goodman, N. D. (2015). Rational use of cognitive resources:
    Levels of analysis between the computational and the algorithmic. *Topics in Cognitive Science,
    7*(2), 217–229.
  - Lieder, F., & Griffiths, T. L. (2020). Resource-rational analysis: Understanding human cognition
    as the optimal use of limited computational resources. *Behavioral and Brain Sciences, 43*, e1.

## 7. Questions for the user

- **Q1. The Cremers corroboration** (`sections_3-6.md` lines 339–343; background lines 189–192).
  At θ\* the positive shifts are tempering, and the utility level lowers all-region mass under every
  prior. "Both models derive strengthening from the prior and both inherit the liability" no longer
  describes this model's utility level. Options:
  - drop the parallel;
  - restate it about the q read-out against q_lit, where the tempering lives;
  - keep it with the decomposition stated.
- **Q2. The "shape of absence" argument.** The opposing floors survive, but the band is now reached
  by Λ from α = 1, and both conditions hold under the delta-like prior at Λ = 512. Keep one sentence
  on the opposition as a secondary motivation, or cut it and let §5.1 rest on complexity alone?
- **Q3. The dissertation's total length.** 3,595 (background) + 3,000 = 6,595 against the 6,000 the
  background outline assumes. Cut the background, or raise the total?
- **Q4. Which maximizer the halting claim concerned.** The fast one, of F at fixed θ_u, which is
  reached but at a cost; or the slow one, of F̃ at θ\*, which is not reached. And should §5.3 claim
  that the cascade supplies a structural end, or only that the present architecture lacks one?
- **O7 (in `decisions.md`).** The three senses of "realizability".

## 8. Where the numbers are printed

| Numbers | Source |
|---|---|
| θ\*, q_H, Δ, tempering/utility, conditions per prior; the 3.6e-14 / 0.0575 contrasts | `main.ipynb` Code Cell 2, BASE WORLD PRIOR SWEEP |
| 2.126, 6.5, 26, 13.3749, 39,035, −0.5182, 0.4386, 4.28e8, 7.9e6 | Code Cell 2, REALIZABILITY block (step and time figures on `cost:` lines) |
| Peaks, the cell of *all*, grids 201/401/801 | Code Cell 2, THE DELTA READ-OUT block |
| 33, band, floors, 0.100–4.250, 2.0–20.1, 3.5e4–3.6e7, D spread | Code Cell 4, `plane_summary`; Text cell 6 |
| 1.9890 / 2.9334 / 4.3102 | Code Cell 4, `override_threshold` |
| 3.19e-2, +0.0008 to +0.0009 | Code Cell 3, `mu_u_probe` |
| 9.98e-10, 4.6e-14, tails 1.7e-3 / 3.3e-6 | Code Cell 2, Part A |
| 404.8, Eq. (28) table | Text cell 4, *Integration cost and conditioning* |
| F15 (not within 0.1% after 5,000 updates), 145/145 | `procedure_records/theta_u_learned_reach.md` (recorded scripts, not a cell) |
| Exposure-only θ\* (−11.28, −44.18, −65.70) | **not located**; confirm before quoting |

## 9. Other stale pointers found

- `agent.md` §1 named the Desktop outlines. **Fixed 2026-09-13**: it now names `thesis_outline/`
  and lists the Desktop drafts as not maintained.
- `composition guide.md` line 3 names `sections_3-5_outline.md` and `background_sections_outline.md`.
- `decisions.md` B2 (line 275), O3 (line 456) and E4 (line 659) cite `sections_3-5_outline.md`. A
  dated finding under O3 records the new file and the missing target (item 2).
