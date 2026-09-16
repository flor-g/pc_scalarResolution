# Revisions to the thesis outline

Plan for revising `sections_3-6.md` and `background_sections.md`, written 2026-09-13. **Neither
outline has been edited yet, except `background_sections.md` lines 13–14 (R8).** This file lists
what is stale, what is new, where each change goes, and what the user still has to decide (§7).
Numbers are quoted from the executed `main.ipynb` unless a source is named; §8 says where each is
printed.

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

Third message:

> For Q1, save the parallel to q read-out discussions. For Q3, update the background so that it
> doesn't assume any combined word count. For Q4, I meant slow maximizer of F at closed form
> theta_u; remember that our model commits to learned theta_u and we never assume a fixed theta_u
> unless it is a control. For Q2 and O7, can you elaborate on the issue a bit more?

Fourth message:

> For Q5, theta_u* stays the commitment. At an appropriate place, we might want to explain the
> reason for choosing so: our mathematical model predicts theta_u* as the halting value, but the
> simulation exposes a cost problem. We have not yet determined a self-contained halting mechanism
> for the simulation. Any "realizable" theta_u are defined adhoc given theta_u* value known by
> closed form. However, in a simulation, we would want to assume that the system is agnostic to the
> value of the closed-form theta_u*, hence an adhoc realizable theta_u is insufficient to be adopted
> to our theoretical commitment yet.
> ---
> With that said, let's address O7 first. Would you propose a renaming for senses 1 and 3?

Fifth and sixth messages (O7; recorded in full in `procedure_records/o7_renaming.md`):

> Sense 1 renaming approved. For sense 3 maybe say "this map collapses contrasts between exclusion
> sets"? Reads easier this way.

> The cost sense retain the "realizability" name as is; no change needed. Now let's work on Q2.
> Here are my thoughts:
>
> 1. the delta read-out still comes with two criteria: a. whether mode(phi_s*) - mode(ell_0) is
> negative; this is shift_some. b. whether mode(phi_s*) falls outside the cell of [[all]]. Just be
> careful that even though these two criteria are meant to mirror the two criteria as already
> defined, their satisfaction may not be equivalent.
> 2. The V-shape is instereting and it definitely needs to be discussed,
> 3. I am not sure what you mean with the unstated premise and what level is it a motivation of.

## 1. Decisions this plan rests on

| ID | Decision | Decided by |
|---|---|---|
| R1 | The word budget for §§3–6 rises from 2,400 to 3,000 (§3 below). | user (2026-09-13) |
| R2 | The motivation for the alternatives level is the complexity it saves. That motivation does not depend on the criterion failing, so the level stays. | user (2026-09-13) |
| R3 | The paper discusses the two read-outs, the settling cost and halting, and why an algorithmic account is needed. | user (2026-09-13) |
| R4 | The link between q's normalization and §5.1's binarity argument is stated (§5, item 1). | user (2026-09-13) |
| R5 | Where the computational level cannot express a question, the text says the question is **not posable** there. It does not say the question "collapses". | user (2026-09-13) |
| R6 | The three uses of "realizability" are an open decision, `decisions.md` **O7**. Until O7 is settled, the outline does not introduce the term in a new sense. | user (2026-09-13) |
| R7 | **Q1.** The Cremers parallel is kept, and moves into the discussion of the q read-out. It is stated about q against q_lit, where the tempering lives, and not about the utility level. It no longer serves §5.1 as corroboration. | user (2026-09-13) |
| R8 | **Q3.** The background states only its own length and assumes no combined word count. **Applied** to `background_sections.md` lines 13–14, 2026-09-13. | user (2026-09-13) |
| R9 | **Q4.** The halting claim concerned the **slow** maximizer: θ\* of F̃, in closed form (Eq. B2). The model commits to a learned θ_u; a fixed θ_u appears only as a stated control (A9, B4), and the outline's wording follows that. | user (2026-09-13) |
| R10 | **Q5.** θ\* stays the commitment, and A9 is unchanged. The paper explains why at an appropriate place, recommended §5.3 (item 2). The model predicts θ\* as the halting value, but the simulation exposes a cost problem, and no self-contained halting mechanism for the simulation has been determined. Every "realizable" θ_u is defined ad hoc, given the closed-form θ\*. A simulated system should be assumed agnostic to that value, so an ad hoc θ_u cannot yet be adopted as the commitment. | user (2026-09-13) |
| R11 | **O7.** The cost sense keeps "realizability" unchanged. Senses 1 and 3 were renamed ("exact solvability"; "collapses a contrast between exclusion sets"). | user (2026-09-13) |
| R12 | **The delta read-out's two criteria** (`decisions.md` B8), under *some*: (a) mode(φ_S\*) − mode(ℓ₀) < 0, the delta analogue of the shift; (b) mode(φ_S\*) outside the cell of *all*. They mirror Part C's two conditions, and satisfying one need not mean satisfying the other. | user (2026-09-13) |
| R13 | **The V shape is discussed in the paper** (Q2). | user (2026-09-13) |
| R14 | **Q2, option (a).** §4.5 reports the V under both read-outs as a result: the shared right arm, the left arm that exists only under q, and the 20 cells where the conjunctions part. §5.1 does not use the V, and its lines 329–338 go. **No evidence for a missing level is derived from the V.** Budget: §4.5 240, §5.1 350, §4.3 70. The code edits that let the prose quote these numbers are open tasks in `procedure_records/delta_criteria_printing.md`. | user (2026-09-13) |
| R15 | **Q6, option (i).** The Cremers parallel stays with q, and item 1's sentence is corrected. Under q the positive shift is the tempering. Under the delta read-out the mode's upward movement is the utility level's, and is not a probability of *all*. **Why a similar movement emerges under the delta read-out is to be investigated** (open task in the same record). | user (2026-09-13) |

Decisions in `decisions.md` this plan relies on: A9–A11 (θ_u learned, start 0, timescale
commitment), A14 (conventionalized), A16 and B7 (q is a comparison read-out; the delta is the
construction's posterior), A17 (Eq. A4 non-local), B1–B2 (baseline and criterion), B4 (fixed θ_u
only as a control), C3 (three objects kept apart), O3 (the bare outline pointer).

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
- **Not only in closed form.** On the flow's way from 0 to θ\*, the conjunction first holds at
  |θ_u| = 2.126 under the delta-like prior, and holds from there all the way to θ\*. An integrated
  run at the θ_u = 13.3749 that one update of Eq. (20) reaches gives Δ_some = −0.5182 and
  q_H = 0.4386, with nothing in closed form. These are points on the learning trajectory, not
  fixed-θ_u controls.
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
| **4. Evaluation** | **745** | **950** | |
| 4.1 What is compared | 100 | 110 | Naming (literal listener, tempered control) |
| 4.2 The criterion, and how to read the statistics | 170 | 170 | |
| 4.3 The specification holds | 90 | 70 | Trimmed to fund §4.5 (R14) |
| 4.4 The five priors (retitled) | 220 | 260 | New table with tempering/utility split; the Cremers parallel on q (R7) |
| 4.5 The plane, and where both conditions hold | 165 | 240 | Conjunction thresholds across the band; the V under both read-outs (R14) |
| 4.6 What the verdict needs, against what θ\* costs (new) | — | 100 | The evidence item 2 rests on |
| **5. Discussion** | **705** | **980** | |
| 5.1 What an alternatives level would have to supply | 390 | 350 | Complexity-led; the q-normalization link added, the Cremers bullet moved out (R7), lines 329–338 removed (R14) |
| 5.2 Scale structure: a second prediction | 200 | 200 | |
| 5.3 Realizability, halting, and the plausibility commitment (new) | — | 170 | Item 2 |
| 5.4 What an algorithmic account makes posable (new) | — | 120 | Item 3 |
| 5.5 Limits (was 5.3) | 65 | 80 | Convergence of θ_u; conditioning |
| 5.6 Predictions (was 5.4) | 50 | 60 | The timescale separation as a prediction |
| **6. Conclusion** | **150** | **150** | |
| **Total** | **2,400** | **3,000** | |

**Renumbering this causes.** Limits and Predictions move from §5.3 and §5.4 to §5.5 and §5.6, so
four references change: `sections_3-6.md` lines 57, 63 and 77 (§5.3 → §5.5) and
`background_sections.md` line 392 (§5.3 → §5.5). §5.2 keeps its number, because the background
refers to it throughout.

**The background (R8).** `background_sections.md` no longer assumes a combined word count. Its
lines 13–14 now state only its own target.

---

## 4. `sections_3-6.md`, site by site

### Header and central claim

- **Lines 4–5, scope line.** "Approximately 2,400 words" → 3,000. "Code cells 1–4, Appendices A–D"
  → add Code Cells A–D.
- **Lines 23–32, constructive claim. Rewrite.** It rests on "exactly one condition holds under every
  prior tested, never both and never neither", which is false at θ\*. Proposed basis, per R2: the
  architecture meets the criterion, under a concentrated prior and across a band of the plane. The
  case for a level representing alternatives is what that level would save:
  - branching logarithmic in the predicate's granularity;
  - one dimension per level, so plasticity is local without the relay;
  - an affine generative map that keeps the convergence proof;
  - a read-out that needs no normalization across the scale (item 1, §5 below);
  - an end to learning short of a maximizer the slow flow never reaches, which the present
    architecture lacks (item 2; to be argued, not derived).

  "The pattern is the shape of its absence" is withdrawn (R14).
  The specification-not-built sentence (lines 28–32) survives unchanged.
- **Lines 34–37, standing qualification.** Survives.

### Scope tiers (lines 41–77)

- **Tier A.** The criterion row (line 52): "the spine of the constructive claim" → "the verdict,
  and the evidence that the conjunction is reachable". Relay row (line 57): §5.3 → §5.5, and "the
  cost it carries" → "τ_r ≤ τ_ε only" (F26). **Add** three rows:
  - the two read-outs, placed at §3.6, §4.1 and §4.4, because they fix what a verdict is stated on
    and where the Cremers parallel lives;
  - commitment 7 and conditioning (Eq. 28, §8.3), placed at §3.4, §4.6 and §5.3, because they are
    the evidence for item 2;
  - the conjunction threshold against θ\*, placed at §4.6 and §5.3, because it is what dissolves
    the maximizer-as-halting claim.
- **Tier A, the closed-vs-open-scale row (line 60).** Its "second empirical anchor" depends on Q7.
  The row stays in Tier A only if §5.2's prediction is rebuilt on the learned model.
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
  - Strict concavity secures convergence of the fast subsystem at every θ_u the slow flow passes
    through, but conditioning governs whether that convergence is reachable: condition number about
    (1+θ_u²)/2, 404.8 at the Gaussian θ\*. This sentence sets up §4.6 and §5.3.
- **Lines 193–196, the relay's cost. Rewrite per F26.** Under commitment 7 the relay adds no
  stability requirement of its own. It needs only τ_r ≤ τ_ε, and the reason is monotone F, not
  oscillation. It inherits θ_u⁻² from τ_ε rather than carrying its own. Eq. (E6) keeps ≤, with the
  exception that at equality F is monotone under *some* only (O6).

### §3.5 (lines 197–213)

- **Lines 201–209, the parity bullet.** Survives.
- **Lines 212–213**, "Every result in §4.4 and §5.2 turns on which of the two an entry loads".
  - Under learning, what the utility level doubles is the literal field's loading, the prior's
    included (F5).
  - §5.2's measured contribution is carried by the tilt (§5.2 entry below).
  - Restate: the results turn on the literal field's tilt and width.

### §3.6 Two read-outs (new, about 100 words)

Content in §5 below, item 1. It sits in §3 because it is a commitment about what the model outputs,
and §4.1 and §4.4 need it.

### §4.1 (lines 218–232)

- **Line 222.** "Untempered literal posterior" → "untempered literal listener". Add one sentence
  saying that "literal" here denotes something distinct from what it denotes in RSA and the Gricean
  literature, with no further explanation (DEC5 of `procedure_records/d9_delta_readout.md`).
- **Lines 226–229.** "The θ_u=0 control" → "the tempered control". Add that it is also where
  learning starts.
- **Line 230.** q_H is the settled belief *read through q*. Point to §3.6.

### §4.2 (lines 234–253)

- **Lines 236–240.** Add one sentence that both conditions are stated on the read-out q (A16).
- **Lines 247–253, the guard.** Both measured instances in the outline are fixed-θ_u controls, which
  under B4 may appear only as stated controls. Under learning the φ_S-contrast deviation across μ_u
  settings is 3.19e-2 (not 3.6e-15), and Δ_some's spread across the six μ_u settings collapses to
  +0.0008 to +0.0009 (Text cell 5 Part B). Either label the instance as a control and say what it
  controls for, or take the instance from the learned model: the φ_S contrasts across Part D's
  priors agree to 3.6e-14 at a shared θ_u (a control) and differ by 0.0575 at each prior's own θ\*.

### §4.3 (lines 254–263)

- "Exact to 6.0e-11" → about 1e-9 (9.98e-10), since the stopping tolerance is now 1e-9 (I3).
- Grid tails "1.6e-3 … 1.8e-6" → 1.7e-3 and 3.3e-6.
- Add: θ\* from Eq. (B2) matches an independent bisection to 4.6e-14, and Eq. (20) ascends from 0.
- Budget 70 words (R14): report the checks as a table and keep the prose to the grid-tail point.

### §4.4 (lines 265–297): rewrite

- **Title.** "One condition, every time" → e.g. "The five priors".
- **Table.** Replace with §2's table, with a θ\* column. Tempering and utility can be columns or one
  sentence.
- **Line 277.** "The conjunction holds under none" → holds under the delta-like prior alone. The
  four diffuse priors meet only the second condition. No prior meets neither.
- **Lines 280–286, decomposition.** "The utility level's own contribution is small and of either
  sign" is false. It is negative under all five, and the four positive shifts are tempering.
- **Lines 287–289, anti-exhaustive direction. Rewrite per R7.** The Cremers parallel lands here,
  stated as a property of the read-out q against q_lit. Content in §5 below, item 1.
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
  - The opposition of the two floors survives as the result. Discuss the V under both read-outs
    (R13, R14), with Q2's table:
    - the right arm is shared, at Λ = 8α;
    - the left arm exists only under q;
    - in 20 cells the conjunctions part.

    Report it as a result, and derive no evidence for a missing level from it. Its numbers wait on
    the printing tasks (C6).
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
- The integrated run (39,035 Euler steps at the θ_u = 13.3749 that update reaches) gives
  Δ_some = −0.5182 and q_H = 0.4386. There λ_max(H) = 180.9, a separation of about 724.
- The same inference at θ\* = 1407.77 would take 4.28e8 steps, hours, at a separation of 7.9e6.
- The Eq. (20) flow from 0 is not integrable to θ\*: it is not within 0.1% of θ\* after 5,000
  updates (F15). That θ\* is reached rests on the closed form and the monotone rise.

### §5.1 (lines 322–435)

- **Framing (lines 324–327).** Lead with the complexity argument (R2). Lines 344–397 survive
  intact: the negative search, what is searched versus what branches, the binary inventory, the
  *most* case, the dimension and locality payoff, and binarity at the generative map.
- **Lines 329–338, "Why the pattern points at such a level". Removed (R14).** The V is reported in
  §4.5 and motivates nothing here.
- **Lines 339–343, the Cremers corroboration. Removed from §5.1 (R7).** The parallel moves to §4.4.
- **Add after lines 388–397: the read-out link (R4, about 40 words).** Content in §5 below, item 1.
- **Lines 398–420, what is not derived.** Survives. Add to its list that an end to learning short
  of the slow maximizer is also a claim about the unbuilt level (item 2).
- **Lines 422–431, the position on the current gain.** Survives. The four exposure-only θ\* values
  (−11.2844, −44.1766, −65.7004, −28.4375) are printed by Code Cell B, *ALTERNATIVE SPACES*.
- **Lines 432–435, standing qualification.** Survives.

### §5.2 (lines 436–477): re-examined 2026-09-14

**Source.** `audits/2026-09-13-scale-structure/` (script and `output.txt`).
- The audit uses Code Cell 1's closed form (agreement 0.0), and recovers θ\* = −28.4375 for the
  default network.
- A single-threshold predicate excludes the states below its cut: χ_t = 1[ζ < logit s_t], Λ = 8.
- **No notebook cell prints any of this.**

**Where §5.2's numbers come from.** No probe survives, in the project or on the Desktop. The numbers
appear only in the outline.
- **Gaussian precision 2, at θ_u = 1:** reproduces exactly. −0.0055 at s = 0.50 and +0.0200 at 0.98,
  against the quoted −0.005 and +0.020.
- **Flat prior:**
  - at θ_u = 1, +0.0324 and +0.0669, against the quoted +0.034 and +0.070;
  - at θ_u = −28.4375, the default prior's θ\* carried into another configuration (the F9/F23
    pattern), +0.0455 and +0.0945, against the quoted "+0.047 → +0.099 at θ_u\*".

  Close but not exact, so the flat setup differed slightly.
- **Loading ratios:** 0.219 at 0.73 and 0.633 at 0.95 reproduce. At 0.99 the ratio is 0.994, not 1.07.
- **So every magnitude in §5.2 is a θ_u = 1 control or a carried θ\*.** Under A9 and B4 neither can
  stand as the model's result, and under C6 none is printed.

**What the learned model gives.**
- **Which θ\*.** A single predicate's θ\* needs an exposure ensemble, and that is undecided
  (`decisions.md` O8). Two illustrative ensembles, the predicate alone and the predicate with its
  complement, give |θ\*| from 4.6 to 91. Their contributions are within about 5% of Eq. (24)'s
  limit.
- **So the limit is used.** It needs no θ\*, and by F5 it decides every verdict on the plane.
- **Contribution** = E_q[s] of the limit field minus E_q[s] of the tempered field. An asterisk marks
  a cut the prior overrides: q-mass on the excluded states is at least 0.4 in the limit field.

| s_t | 0.50 | 0.60 | 0.73 | 0.80 | 0.90 | 0.95 | 0.98 | 0.99 |
|---|---|---|---|---|---|---|---|---|
| flat | +0.0469 | +0.0460 | +0.0439 | +0.0436 | +0.0485 | +0.0619 | +0.0953 | +0.1158 |
| Gaussian, precision 1 | −0.0084 | −0.0083 | −0.0015 | +0.0050 | +0.0149 | −0.0059\* | +0.0149\* | +0.0341\* |
| Gaussian, precision 2 | −0.0196 | −0.0186 | −0.0129 | −0.0192 | −0.0704\* | +0.0109\* | +0.0336\* | +0.0242\* |
| Gaussian, precision 4 | −0.0219 | −0.0205 | −0.0399 | −0.0908\* | +0.0087\* | +0.0229\* | +0.0177\* | +0.0124\* |

**Findings.**
1. **"Rises monotonically" fails.** Under the flat prior the contribution falls slightly, from
   +0.0473 at 0.55 to +0.0436 at 0.80, and rises only above 0.80. The same dip appears at
   θ_u = 1.
2. **The sharp-prior comparison mixes held and overridden entries.**
   - At Λ = 8 a Gaussian prior overrides an endpoint cut. In the limit field the q-mass on excluded
     states is 0.62 at 0.95 and 0.97 at 0.98 under precision 1, and above 0.99 from 0.95 under
     precision 2.
   - The positive endpoint value §5.2 relies on (precision 2, "+0.020 at 0.98") comes from an entry
     the prior has fully overridden: the literal listener's leak there is 1.0000.
   - Among held entries, precision 1 turns from negative (up to 0.73) to positive (0.76 to 0.90),
     which is the reversal §5.2 describes. Precisions 2 and 4 are negative at every held cut.
3. **The tilt carries the contribution, not the width.** Splitting the limit field as in F4:
   - under the flat prior, the tilt part runs +0.049 to +0.117 and the width part −0.043 to +0.017;
   - under the Gaussians, the width part is negative at every cut.

   §5.2's mechanism, that the entry's width loading grows toward the endpoint and is zero at the
   midpoint, is exact as a statement about κ. It is not what produces the measured contribution.
4. **Under learning, the doubled width is the prior's plus the entry's** (F5).
   - c_width from the prior: −4.94 (flat), −18.60, −37.20, −74.40 (precisions 1, 2, 4).
   - c_width from the entry: 0 at 0.50, rising to +5.82 at 0.98.
   - So the width part favours the extremes only where the entry's width outweighs the prior's:
     under the flat prior for cuts 0.93 to 0.98 (it is zero at 0.90), and never under the Gaussians
     tested.
5. **Read-out.** "Posterior degree" is E_q[s], a statistic of q (A16).
   - Under the delta read-out (flat prior, limit), the mode moves above the cut for a mid-scale
     predicate: 0.81 at s_t = 0.50, 0.87 at 0.73.
   - From 0.95 up it stays at the cut's node, so the utility level does not move an endpoint
     predicate's peak at all.
   - R12's caution applies: §5.2 must say which read-out the prediction is stated on.
6. **What survives.**
   - The parity result, exactly: a midpoint cut has zero width loading, with the node half-weighted.
   - The loading ratios at 0.73 and 0.95.
   - Qualitatively: under the flat prior an endpoint cut's contribution exceeds the midpoint's
     (+0.1158 against +0.0469). Under the default Gaussian prior a held mid-scale cut's contribution
     is negative, while cuts from 0.76 to 0.90 are positive.

**Site changes.**
- **Remove, or recompute on the learned model:** the magnitudes, "monotonically", the sharp-prior
  sentence, and the "(and from … at θ_u\*)" parenthetical.
- **The parity paragraph survives**, restated as a fact about the entry's loading and not about the
  measured contribution.
- **The mechanism paragraph needs rewriting around F4/F5.** The utility level doubles the literal
  field's tilt and width. The tilt carries the contribution to E[s], and the width favours the
  extremes only where the entry's width outweighs the prior's (Q7).
- **Downstream of Q7:** the prediction paragraph and the empirical-fit paragraph.
- **The numerical note stays** (half-weighting the midpoint node).
- **Before any rebuilt number is quoted:** a printing cell (C6) and an answer to O8.

### §5.3 and §5.4 (new)

Content in §5 below, items 2 and 3.

### §5.5 Limits (was §5.3, lines 478–489)

- **Lines 480–482.** θ_u convergence: from θ_u(0) = 0 the flow rises monotonically to θ\*. This
  holds in 145 of 145 configurations tested, by Appendix B's root argument. The flow is not
  integrable to θ\*, and θ\* is supplied in closed form.
- **Line 485.** "A fourth timescale scaling as θ_u⁻² (Eq. E6)" → τ_r ≤ τ_ε, inheriting θ_u⁻² from
  commitment 7.
- **Add.** Conditioning, and the separation commitment 7 demands, as a limit on plausibility
  (points to §5.3).

### §5.6 Predictions (was §5.4, lines 490–500)

- **Add one bullet.** Commitment 7 predicts error units at least 4λ_max(H) times faster than state
  units: 26× where the conjunction first holds, rising as learning proceeds. The prediction is
  conditional on this architecture without an alternatives level, and should be worded as such.
- **Lines 499–500, the scale-structure interaction.** Depends on Q7.

### §6 Conclusion (lines 503–518)

- **Item 3 (lines 511–516). Rewrite.** "Satisfies only one of the two conditions … under every
  prior tested" is false. Proposed: the network reaches the conjunction under a concentrated prior
  and across a band of the plane, early in learning. But what it pays for this, and the absence of
  any end to learning other than a maximizer the slow flow never reaches, are what a level
  representing alternatives would change. The rest of item 3 (the design and what is not derived)
  survives.
- **Add a clause** for item 3 of §5 below (not posable at the computational level), if §6's budget
  allows.
- **Item 4 (lines 517–518). Depends on Q7.** It says the threshold semantics predicts "an
  endpoint-orientation asymmetry … sharpest where prior knowledge is weakest". Under the learned
  model the weak-prior half holds under the flat prior. The sharp-prior half rests on entries that
  are overridden at Λ = 8.

### Open items (lines 539–569)

- **Open item 1 (lines 541–549). Rewrite.**
  - Its "validated by reproducing every published quantity" predates learned θ_u.
  - The drafted probe it mentions cannot be found.
  - It is replaced by Q7 and O8, plus a printing task once §5.2's numbers are rebuilt.
- **Line 552.** `background_sections_outline.md` is now `background_sections.md`.
- **Add.** A pointer to this file.

---

## 5. The new material

### Item 1. The two read-outs (§3.6, about 100 words; results in §4.4; link in §5.1, about 40 words)

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

**The Cremers parallel, on q (R7; §4.4, about 40 words of its 260).**

- **What survives.** Read through q, the settled belief under *some* holds more all-region mass than
  q_lit on the four non-delta priors (+0.0008, +0.0295, +0.0004, +0.0421). That is the
  anti-exhaustive direction Cremers, Wilcox and Spector (2023) identify as a liability of baseline
  RSA, and which human participants do not show.
- **What it is in this model.** It is the tempering (+0.0175, +0.0854, +0.0065, +0.0988). The
  utility level's own contribution runs the other way under every prior. The tempering exists only
  for a read-out that normalizes: the delta's peak does not move under the halving. Under q,
  therefore, the positive shift is the tempering. Under the delta read-out the mode of φ_S\* also moves up the
  scale on the same four priors (R12). Because halving does not move a mode, that movement is the
  utility level's. It is not a probability of *all*: the mode stays outside the cell of *all*. Why
  the utility level produces it is under investigation (R15).
- **Guards.**
  - The parallel is in direction, not in conditions. Here it appears under all four non-delta
    priors, the flat one included, while background §1.3 states the RSA liability for skewed priors.
  - The mechanisms differ: the ½ temperature of a finite σ_S here, the prior acting through the
    speaker model there. Say "parallel", not "shared liability".
  - §5.1 no longer uses the parallel as evidence for the alternatives level. That argument rests on
    complexity (R2).

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

The cost sense keeps the name "realizability" (O7, settled). The content, per R9 and R10:

- **What halts, and on which timescale.** The claim concerns the slow flow of Eq. (20), which
  ascends F̃ toward θ\* (Eq. B2), the value A9 commits the model's θ_u to. Since θ_u is an exposure
  statistic across trials (A14), "halting" here is the end of plasticity across exposures, not the
  end of one inference. (Within an inference the fast subsystem settles at whatever θ_u the slow
  flow currently carries, by §8.1. The code's stopping tolerance there is a numerical surrogate, I3,
  and is not the halting in question.)
- **Why the maximizer does not halt the flow.** A flow halts where its gradient vanishes, at θ\*.
  From θ_u(0) = 0 the flow rises monotonically toward θ\* but is not within 0.1% of it after 5,000
  updates (F15): F̃ flattens toward its asymptote, so the flow approaches without arriving. Nothing
  in F̃ stops it earlier.
- **Why that matters: cost rises while the verdict stands still.** Commitment 7 ties the error
  units' speed to λ_max(H), which grows as θ_u². Under the delta-like prior the conjunction holds
  from the first update on, at a separation of 26 where it first holds. Every later update leaves the
  verdict as it is and makes each later inference costlier: about 724 at θ_u = 13.37, rising toward
  7.9e6 at θ\*. Across the 33 both-condition cells of the plane, the separation needed where the
  conjunction first holds is at most about 80 (4 × 20.1), against 4 × (3.5e4 to 3.6e7) at θ\*.
- **Consequence without the alternatives level.** A mechanism outside F̃ must stop or slow the flow.
  It is not a term of F̃, and its locality and its standing against Bogacz (2017) would both need
  arguing (a new entry in the divergence register). Check the tutorial's own remarks on parameter
  convergence before citing it either way (agent.md §3.2).
- **Why θ\* stays the commitment (R10; the paper's explanation goes here).**
  - The mathematical model predicts θ\* as the value at which the slow flow halts.
  - The simulation exposes a cost problem, and no self-contained halting mechanism for it has been
    determined.
  - The lower θ_u values the evaluation reports are ad hoc: each is located using θ\* already known
    in closed form. A simulated system should be assumed agnostic to that value, so none of them can
    yet be adopted as the commitment.

  Code Cell 2 shows the dependence concretely (checked 2026-09-13):
  - the threshold (2.126) is a bisection on fractions of θ\*, and the run is attempted only where
    the conjunction already holds at θ\*;
  - the one-update θ_u (13.3749) is computed without θ\*, but the flow is stopped there by Part C's
    criterion. That criterion is a statistic of the read-out q against q_lit, computed outside the
    network: an evaluator's stopping rule, not one the simulated system has.

  So these values measure what the verdict needs. The model's commitment remains θ\*, and the
  missing halting mechanism is an open problem of the simulation.
- **With the level.** Under R9, what §5.3 has to claim for the alternatives level concerns the slow
  flow, not how one inference ends. Either the level's slow objective has a maximizer its flow
  reaches, or its verdict does not depend on growing a gain whose cost grows with it. Neither is
  derived. The one-dimension-per-level result of §5.1 is where an argument would start, and §5.1's
  lines 398–420 apply to it.
- **Neural plausibility.** Commitment 7's separation, and tens of thousands of Euler steps per
  inference even where the conjunction first holds, are the cost the plausibility commitment
  (background §2.1, §2.7) has to answer for. This is the argument main.ipynb's *Integration cost and
  conditioning* defers to the outline.
- **The cross-reference this repairs.** Text cell 4 says the question "is left where it is posed,
  in the background outline", and O3 cites `sections_3-5_outline.md` 3.4, 3.4.3 and 5.3. Neither
  current outline contains a settling-cost argument: §5.1's complexity case is about branching,
  not settling time. This section becomes the pointer's target. The pointer itself stays bare (O3).

### Item 3. What an algorithmic account makes posable (§5.4, about 120 words)

- **Claim.** Each question above is **not posable** at the computational level (R5). A
  computational theory specifies the posterior and is silent on resources and representation. So:
  - there is one posterior, and no choice between a delta and a normalized read-out;
  - θ\* is the answer however long the flow takes toward it, so there is no gap between where the
    verdict is reached and where learning would stop;
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

**Line numbers below are from before R8's edit.** That edit joined lines 13–14 into one, so every
later line is now one lower (for example, §1.3 Beat 3's forward pointer is at line 188 and the §2.2
table's commitment 3 row at line 391).

- **Lines 13–14, scale. Done 2026-09-13 (R8).** Now "Target length: approximately 3,595 words.",
  with no combined count.
- **Lines 57–64, opening move 3.** Add the "not posable" clause (item 3) and a forward pointer to
  §5.4. One sentence.
- **Lines 186–192, §1.3 Beat 3. Rewrite the forward pointer per R7.** It points to §4.4's
  discussion of the q read-out, not to §5.1. It states the anti-exhaustive direction as a property of
  the read-out q against the literal listener, with the tempering named. It drops "treats the fact as
  corroboration" and "what avoids it is a drain keyed to the alternative". The RSA side (lines
  183–188) survives.
- **§1.7 (lines 309–334), the answer to Q3b.**
  - The outline says of Q3b "Do not answer it here. §5.2 answers it from the parity structure of the
    utility basis". That overstates what §5.2 can now claim. Parity fixes the entry's width loading,
    but the measured contribution is carried by the tilt, and under learning the prior's width enters
    too.
  - Soften to "§5.2 takes it up", pending Q7.
  - The literature bullets survive. The Leffel et al. check is still pending.
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
  - Add that θ_u is learned and its flow starts at 0, at the tempered control.
  - "Appendix E adds a fourth timescale" → as in §2.4.
  - Lines 502–504 ("updating the slow parameter once per utterance") survive, and are where item 2's
    point that halting concerns plasticity across exposures connects.
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

**Resolved:** Q1 as R7, Q3 as R8, Q4 as R9, Q5 as R10, Q2 as R14, Q6 as R15.

### Q2. The "shape of absence" argument, the delta criteria, and the V (resolved, R14)

**Settled so far (R12, R13).** The delta read-out carries two criteria of its own, mirroring Part
C's, and need not agree with them. The V shape is discussed in the paper.

#### The audit

`audits/2026-09-13-delta-criteria/` (script and `output.txt`). It executes Code Cell 1 and Code
Cell 2's definitions, and reproduces Code Cell 2's Part D rows and Code Cell 4's counts (second
condition 59, both 33). Everything is under *some*, each configuration at its own θ\*. **2026-09-15:
every number in this subsection is printed**, by Code Cells 2, 2b and 4.

**Part D's five rows agree row by row.**
- Criterion (a) is met only under the delta-like prior, where the mode moves from 0.9852 to 0.9468.
- Under the four diffuse priors the mode moves *up* the scale: 0.50 → 0.59, 0.50 → 0.67,
  0.25 → 0.33, 0.75 → 0.84.
- Criterion (b) is met under all five.

**The plane (121 cells):**

| | q read-out | delta read-out | disagree |
|---|---|---|---|
| first condition / criterion (a) | 74 | 67 | 35 cells |
| second condition / criterion (b) | 59 | 59 | none |
| both | 33 | 13 | 20 cells |

- **The second conditions coincide in every cell** and in Part D's rows. That is measured, not
  proved. A mode outside the cell and a minority of mass inside it are different statements, and
  could part under a prior or grid not tested here.
- **The first conditions disagree in 35 cells, in two groups.**
  - *q's first condition without (a): 21 cells, all at α ≤ 16, at or above q's floor.*
    - All-region mass falls: the utility part runs −0.03 to −0.40 and outweighs the tempering
      (+0.02 to +0.10).
    - The mode moves up the scale, e.g. from 0.50 to 0.92 at α = 1. At (16, 128) it does not move.
  - *(a) without q's first condition: 14 cells, all where the prior overrides the entry.* These
    are (32, 16), (64, 2 to 8), and the α = 1024 row up to Λ = 1024. The mode moves down while the
    mass does not fall:
    - at (32, 16) and (64, 2 to 8) the utility part of the shift is positive;
    - on the α = 1024 row q is saturated at 1.0000, and cannot register the movement the mode shows
      (0.9975 → 0.979, still inside the cell).
- **Every delta conjunction is a q conjunction.** The reverse fails in 20 of q's 33 cells, all at
  α ≤ 16.
- **The tempering does not explain the difference.** A mode is unmoved by the halving, so
  criterion (a) sees only the utility level. What separates the two first criteria is that the
  utility level can lower the all-region mass and raise the mode at the same time.
  - Likely reading, from §3.5's two columns: the even (width) column lowers both tails, and the odd
    (tilt) column slides the peak.
  - This reading is not decomposed in the audit.
- **Grid facts.**
  - Modes are grid nodes, 0.12 apart in ζ. Four cells have an unmoved mode, where (a) fails by a
    zero shift.
  - The smallest gap between the two largest nodes is 5.6e-5, so no mode is a tie.
  - mode(ℓ₀) equals mode(ℓ₀ − φ_L) in every cell under *some*, so R12's baseline coincides with the
    literal listener's mode. Under *no* or *all* the two would differ.

**The V under each read-out.** For each α, the least Λ at which both hold, holding at every larger
Λ (every condition's set of cells is upward closed on this grid):

| α | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | ≥ 256 |
|---|---|---|---|---|---|---|---|---|---|
| q read-out | 512 | 256 | 128 | 64 | 64 | 256 | 512 | 1024 | none |
| delta read-out | none | none | none | none | 256 | 256 | 512 | 1024 | none |

- **The right arm is shared.** The second condition sets it, and there the read-outs coincide. It
  runs at Λ = 8α for α = 32, 64 and 128, on a grid with factor-2 resolution.
- **The left arm exists only under q.** Under the delta read-out, criterion (a) holds from Λ = 256 at
  α = 16, Λ = 16 at α = 32, and Λ = 2 from α = 64. For α ≤ 8 no Λ on the grid moves the mode down.
- **So the V is the q read-out's shape.** Under the delta read-out the conjunction needs a prior
  concentrated enough (α ≥ 16 here) and a lexical strength that rises with the concentration.
- **Correction to this file's earlier Q2 text.** It said the left arm depends on the read-out
  because of the tempering. The dependence is confirmed, but the reason is the mass/mode
  divergence, since the delta read-out does not see the tempering.

#### The premise, explained

- **Which level.** Lines 329–338 of `sections_3-6.md` used the one-condition-per-prior pattern as a
  motivation for the **alternatives level** of §5.1: the proposed, unbuilt level that would
  represent competition among alternatives within a trial.
- **The argument the V would have to make.** Carried over into that role it would run: the
  architecture meets both conditions only when Λ is matched to α; a level keyed to the alternative
  would not need that; so the level is motivated.
- **The unstated premise.** The step from "the model needs Λ matched to α" to "the model is missing
  something" needs a premise the outline never states: that human listeners strengthen *some* across
  prior concentrations *without* a comparable adjustment, with one lexical entry of fixed strength.
  - Nothing in the dissertation measures that.
  - Degen, Tessler and Goodman (2015) show strengthening is robust across priors. That is about how
    far the prior moves the posterior, not about lexical strength, which has no direct human measure.
- **Without the premise, the V is a property of this model, not evidence of a missing level.**
  - Since R2 rests the level on complexity, the V does not need to motivate anything.
  - The audit adds a second reason not to use it that way: the V's left arm belongs to the q
    read-out.

#### Options for the V (R13)

- **(a)** §4.5 reports the V under both read-outs as a result: the right arm shared, the left arm
  q-only, and the 20 cells where the conjunctions part. §5.1 does not use it. Its lines 329–338 go
  entirely.
- **(b)** As (a), plus one sentence in §5.1 that states the premise as a premise.

**Agent's recommendation: (a). Approved by the user (R14)**, who added that no evidence for a
missing level needs to be derived from the V.

**Budget, proposed.** §4.5 goes from 180 to 240 words. The extra 60 would come from §5.1 (390 → 350,
since lines 329–338 go) and §4.3 (90 → 70).

**Printing (C6).** Every delta-criterion number above comes from the audit script, so it is class (e)
for prose until a cell prints it. Before §4.5 or the paper quotes one:
- Code Cell 4's `plane_summary` and Code Cell 2's delta read-out block would print criteria (a) and
  (b) and their floors;
- Code Cell 2's addition is copied into E2 and replayed by E3;
- both notebooks are re-executed.

These are now open tasks, in `procedure_records/delta_criteria_printing.md` (R14).

### Q6. Does R7's supporting sentence survive the delta criteria? (resolved, R15; investigation open)

**What R7 rests on.** R7 placed the Cremers parallel in the q read-out discussion. Its supporting
sentence (item 1) said the anti-exhaustive direction belongs to q "not to the level that produces
strengthening", because the delta cannot see the tempering.

**What the audit shows.** Under criterion (a) that no longer holds.
- On the four diffuse Part D rows the mode of φ_S\* moves up the scale.
- A mode is unmoved by the halving, so that movement is the utility level's alone.
- So under q the utility level moves all-region mass down, and under the delta it moves the mode up.

R7's placement is the user's decision and has not been changed; only the sentence is marked.

**Options.**
- **(i)** Keep the parallel with q, and correct the sentence. Cremers, Wilcox and Spector's quantity
  is a probability of the all-state, which only q supplies. Under q the positive shift is the
  tempering; under the delta the upward movement of the mode is the utility level's, and it is not
  a probability of *all* (the mode stays outside the cell).
- **(ii)** Discuss the parallel under both read-outs.
- **(iii)** Drop it.

**Agent's recommendation: (i). Approved by the user (R15)**, who asked that the reason a similar
movement emerges under the delta read-out be investigated. The sentence in item 1 is corrected, and
the investigation is an open task in `procedure_records/delta_criteria_printing.md`.

**Preliminary result** (record F4; printed by Code Cell C and reported in Appendix C §8 since
2026-09-15). **The two movements share a direction, not a source.**

- **The split.** By Eq. (24) the model doubles the literal field's span-B component, which splits
  into B's odd (tilt) and even (width) parts.
- **The width** is negative in every configuration tested. It concentrates the belief toward the
  centre of the scale, lowering the all-region mass (all 121 plane cells) and pulling the peak
  inward.
- **The tilt** carries the literal field's skew, prior and entry together, and slides the peak that
  way.
- **Which one wins.** The mode moves up wherever the tilt wins (50 cells, the literal mode at
  s ≤ 0.94), and down wherever the width wins (67 cells, s ≥ 0.94).
- **Why the read-outs part.** q's first condition reads the tail, which the width governs.
  Criterion (a) reads the peak, which near the centre the tilt governs.
- **Part D's diffuse rows.** The upward movement is the tilt, except under Beta(1,3), where the
  width's inward pull lifts a mode that sits below the centre.
- **q's positive shift** is the tempering, which a mode cannot see.
- **Bearing on the V.** The same result explains the missing left arm under the delta read-out: for
  α ≤ 8 the literal mode sits where the tilt wins at every Λ.
- **Checked across the plane (record F5).** The halving of Eq. (24) is close in every cell: within
  1e-3 in 111 of 121, and 17% on the tilt at worst, at the smallest |θ\*| (6.51). Eq. (24)'s limit
  field gives the model's mode and all four verdicts in all 121 cells and in Part D's five rows. So
  the reading does not rest on θ\* being large.

### Q5. How a halting mechanism stands with A9 (resolved, R10)

θ\* stays the commitment, and A9 is unchanged. The reason, and where the paper gives it, are in
item 2. Recorded under A9 in `decisions.md`.

### O7. The three senses of "realizability" (settled, in `decisions.md`)

Settled 2026-09-13 by the user. Appendix B now says "exact solvability", and Appendix C §7 says that a
projection "collapses a contrast between exclusion sets". The cost sense keeps "realizability"
unchanged, so §5.3 may use the word in that sense. It still says, per R10, that a realizable θ_u is
located by the evaluator.

### Q7. How to rebuild §5.2's prediction (open, new, 2026-09-14)

The re-examination is §4's §5.2 entry. It leaves four choices, all interpretive and all the user's:
- **What the prediction is stated on.** E_q[s], as §5.2 does now; the delta read-out's mode; or both,
  following R12's pattern.
- **Which mechanism the text gives.**
  - The parity of the entry's width loading, which is true of κ but not of the measured contribution.
  - Or F4/F5's doubling of the literal field's tilt and width, which is what the measurement shows.
- **How the sharp-prior half is posed.** At Λ = 8 the Gaussian priors override endpoint cuts, so
  either:
  - Λ is raised until every compared entry is held (the rule for that belongs to O8); or
  - the comparison is restricted to held entries, where precisions 2 and 4 give negative
    contributions at every cut.
- **Whether the empirical-fit paragraph still holds.** Whether Leffel, Xiang and Kennedy (2017) and
  Xiang et al. (2022) still describe the model depends on the three choices above.

## 8. Where the numbers are printed

| Numbers | Source |
|---|---|
| θ\*, q_H, Δ, tempering/utility, conditions per prior; the 3.6e-14 / 0.0575 contrasts | `main.ipynb` Code Cell 2, BASE WORLD PRIOR SWEEP |
| 2.126, 6.5, 26, 13.3749, 180.9, 39,035, −0.5182, 0.4386, 4.28e8, 7.9e6 | Code Cell 2, REALIZABILITY block (step and time figures on `cost:` lines). The separation of about 724 is 4 × 180.9. |
| Peaks, the cell of *all*, grids 201/401/801 | Code Cell 2, THE DELTA READ-OUT block |
| 33, band, floors, 59 of 121, 0.100–4.250, 2.0–20.1, 3.5e4–3.6e7, D spread | Code Cell 4, `plane_summary`; Text cell 6 |
| 1.9890 / 2.9334 / 4.3102 | Code Cell 4, `override_threshold` |
| 3.19e-2, +0.0008 to +0.0009 | Code Cell 3, `mu_u_probe` |
| 9.98e-10, 4.6e-14, tails 1.7e-3 / 3.3e-6 | Code Cell 2, Part A |
| 404.8, Eq. (28) table | Text cell 4, *Integration cost and conditioning* |
| F15 (not within 0.1% after 5,000 updates), 145/145 | `procedure_records/theta_u_learned_reach.md` (recorded scripts, not a cell) |
| Exposure-only θ\* (−11.2844, −44.1766, −65.7004, −28.4375) | Code Cell B, ALTERNATIVE SPACES |
| §5.2's re-examination: contributions, leaks, loadings, illustrative θ\* | `audits/2026-09-13-scale-structure/output.txt` (an audit script, not a cell) |
| Q2's Part D and Λ = 512 rows: the modes, the mode shift in s and in grid steps, the two mode criteria | `main.ipynb` Code Cells 2 and 2b, the mode criteria block |
| Q2's plane counts (67, 59, 13 against 74, 59, 33), the 35 disagreeing cells, the four unmoved modes, the 5.6e-5 gap, and the V under both read-outs | Code Cell 4, `plane_summary` |
| Q6's tilt/width split, the 50 and 67 up/down counts, Eq. (24)'s halving and the limit field | Code Cell C, `utility_split_report`; Appendix C §8 |

(2026-09-15: R14's and R15's code and prose tasks, T1-T3, T6 and T7 of
`procedure_records/delta_criteria_printing.md`, are closed.)

## 9. Other stale pointers found

- `agent.md` §1 named the Desktop outlines. **Fixed 2026-09-13**: it now names `thesis_outline/`
  and lists the Desktop drafts as not maintained.
- `composition guide.md` line 3 names `sections_3-5_outline.md` and `background_sections_outline.md`.
- `decisions.md` B2 (line 275), O3 (line 456) and E4 (line 659) cite `sections_3-5_outline.md`. A
  dated finding under O3 records the new file and the missing target (item 2).
