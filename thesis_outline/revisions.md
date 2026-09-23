# Revisions to the thesis outline

Plan for revising `sections_3-6.md` and `background_sections.md`, written 2026-09-13. **Neither
outline has been edited yet, except `background_sections.md` lines 13–14 (R8) and
`sections_3-6.md` §§3.2–3.3 (R18, R19; task U9 of `procedure_records/ell0_placement_and_counterforce.md`,
2026-09-18).** This file lists
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
| R16 | **Q7.** §5.2 states H1 (expressions with unstable atomicity carry weaker lexical strength) and H2 (open-scale adjectives behave like *some*; complete-scale adjectives like endpoint(s) + *some*), then reports where the model's prediction matches Xiang et al.'s data and where it does not, **making no claim about the nature of the mismatch**. Every number it quotes is printed by a new Appendix F and Code Cell F in `main.ipynb`. Tasks and blocking decisions: `procedure_records/scale_classes_hypothesis.md` §§7–10. | user (2026-09-17) |
| R17 | **S-2 and S-7.** §5.2 models the two **absolute** classes only. The relative class is not modelled, so no context cut *t* enters and Appendix A is untouched; H2 is stated in full and its open-scale half is left untested. The κ parity paragraph stays in §5.2, restated at n = 4, where it states the symmetry the user's instinct doubts. That instinct — that the two endpoints are not symmetric, the **0** boundary being the lexical level's θ_L and the **1** boundary an alternatives level's θ_A — is stated once, as an instinct, with no promise and no claim that it accounts for the mismatch (`decisions.md` **O14**). | user (2026-09-17) |
| R18 | **The Λ–ℓ₀ counterforce is stated as a commitment.** Under a strong Λ the q shift criterion is met under more priors, and the mechanism is that Λ and ℓ₀ counteract each other. The reader is told that this is a **choice not forced by construction**: ℓ₀ could have been placed at g_S, which would not have let the two counteract as directly. The reasons given are (a) putting ℓ₀ at g_S is messy node-wise and leaves the architecture less clean, and (b) it is intuitive to hypothesize that the world prior and lexical strength have counteractive dynamics. §§3–4 also say whether the commitment has a parallel in RSA. `decisions.md` **A3** is confirmed, not reopened. Tasks U0–U14 and the blocking decisions P-1 to P-7: `procedure_records/ell0_placement_and_counterforce.md`. | user (2026-09-17) |
| R19 | **The RSA projection parallel is stated, with an explicit warning.** The paper says that the utility level reads a **linear projection of the same log quantity** S₁ reads, log L₀(s|u). The background **foreshadows** the similarity. Both places warn the reader explicitly that, mathematically, **a projection does not imply an equivalence**, and that forgetting the difference is dangerous. The warning has an exact form: BᵀW1 = 0, so the coupling is rank 2 and blind to the constant direction — the one the normalizer lives in (G10 of the record). The coupling is constant-invariant; **the model is not** (§9.1, no flat direction). | user (2026-09-17) |
| R24 | **Both of this phase's ensemble stipulations are stated and labelled** (`decisions.md` **O2** for the weights, **A18** for the membership). *Weights*: $p(y)$ is uniform, which is the same move as fixing every σ at 1 — a quantity the phase does not model set to the value that treats every utterance alike, and which makes the ensemble vanish from Eq. (B2). The paper does not measure how far a non-uniform $p(y)$ would move θ\*; it claims only that it would, which is what makes §5.6's exposure prediction a prediction **about departures from a stipulated uniform**. One asymmetry is stated rather than smoothed: σ is a variable with a default, so a precision-bearing phase changes defaults, whereas $p(y)$ is not a variable at all but implicit in the batched sum, so a frequency-bearing phase adds a weight vector — and Appendix B's per-presentation check is the one place that would feel it. *Membership*: the inventory holds at least $\{\chi,\ker\chi\}$ for any entry; an antonym is never needed to define one, ker is an involution where antonymy is not, and the pair is present whether or not a word lexicalizes the second member (ker E_all = {1}, the O corner). Membership follows from exposure **somewhere**, not from exposure in a given experiment, and the converse does not hold. Sites: Appendix B, Appendix D §2, Text cell 3's preamble items 3 and 6, §5.1's cascade, §5.5 Limits, §5.6 Predictions, and a wording constraint on §5.2 carried by `scale_classes_hypothesis.md` T10. Markdown only — no coupling fires and no cell is re-executed. | user (2026-09-21), applied 2026-09-22 |
| R25 | **§4.2 gains a second guard: the evaluation's verdicts are relative to n** (`decisions.md` **O1**, **O10**; S-8, tasks T14–T16 of `scale_classes_hypothesis.md`). θ_L = log(2n − 1) fixes the cell of *all*, and n = 10 is a stipulation, not a measurement. Code Cell A's `granularity_report` now prints all four criteria at every (n, Λ, ℓ_0) — 80 rows over n ∈ {2,3,4,5,10,15,20,50,100,201}, Λ ∈ {8, 512} and all four `BASE_WORLD_PRIORS` — and the q shift criterion changes status somewhere on the sweep in every one of the eight (Λ, ℓ_0) blocks, while **where** it changes depends on Λ: **granularity and lexical strength are not separable** in what §4 reports. Two cautions the prose must carry, neither visible in a status column: a ladder **brackets** a change rather than locating it, and a status change may be the sign flip of a quantity already decayed to −7.593e-07 (N(0,1) at Λ = 8) as against −9.546e-02 (*skewed high* at Λ = 512) — not findings of equal weight. Sites: §4.2 (about 90 words, 170 → 260, total → 3,610), a clause in §5.2's *Calibrate the claim* bullet, Appendix A's markdown cell, and Code Cell A. **Not claimed:** anything about what should fix n; O1's two parts stand. | user (2026-09-21, "that cost … worth reporting… they need to be mentioned in the paper"; scope set at S-8), applied 2026-09-22 |
| R26 | **§5.2 is rewritten against Code Cell F, and Appendix F is added** (`decisions.md` **A20**, **O13**, **O14**; S-1 to S-9, tasks T0–T13 of `scale_classes_hypothesis.md`). Two new cells in `main.ipynb` (22, 23; cell count 23 → 25), one new data file (`data/xiang_2022/`, the only file either notebook reads), and §5.2 at 400 → **550 words** (total → 3,760). §5.2 states H1 and H2 as hypotheses and adopts neither, reports match and mismatch, and **says nothing about what any mismatch is due to** (R16). Λ is fitted per class — here and nowhere else in the dissertation, because H1 is a claim about Λ — and the ladder is reported as a **bracket**, not a location (R25's lesson, applied again). The relative class is **not modelled**, so H2's open-scale half is stated and left untested, and the instinct about separating θ_L from θ_A closes the section with no promise attached (O14; site confirmed by the user, 2026-09-22). **Two corrections carried:** the source audit had scored the model against 10 rows of an item with no Experiment 3 data, which moves the maximum class's R² 0.953 → **0.993** and the minimum class's 0.401 → **0.434** (`decisions.md` E16); and F12's backwards prior-manipulation sentence is fixed here and in background §1.7. Sites: §5.2, the scope-tier row, the word table, background §1.7, the References of both the notebook and the outline (Kennedy 2007; Xiang et al. 2022, the Leffel et al. manuscript dropped at T5). | user (2026-09-17, "state both H1 and H2… refrain from making any claims on the nature of this mismatch"; S-1 to S-9), applied 2026-09-22 |
| R27 | **The dissertation takes no position on H1, and says why** (`decisions.md` **O13**; probes in `audits/2026-09-22-o13-options/`). Two things prompted it. §5.2 said the finite-versus-unbounded Λ contrast "is H1's content", which credits the hypothesis with more than the maximum class can carry: that class's R² stays between 0.989 and 0.993 for **every** cut from ζ = −1.0 to +4.0, and its literal, tempered and settled beliefs agree to three decimals, so it fixes a lower bound on Λ and **does not** establish that its threshold is endpoint-anchored. And the agent proposed rejecting H1 outright, on the ground that one shared Λ costs 0.001 of R². **The user refused the rejection**, and the reason is now stated in the paper rather than left to inference: the comparison runs at a **single n**, so the quantity H1 is about does not vary across the classes compared; and it runs under architectural commitments — one θ_L fixing both endpoints, no alternatives level — that §5.1 and §5.2's own instinct put in doubt, so a match or mismatch obtained under them is evidence about **this phase**. H1 is posed for what it would mean for how the model develops, and is left open on purpose. Sites: §5.2 gains a *Why no position is taken* bullet and its *Calibrate the claim* bullet now guards **both** directions; the max-class sentence is softened; §5.6's prediction bullet, §6 item 4, the scope-tier row and Appendix F's opening all carry the reservation. §5.2 550 → **650**, §6 165 → **185**, total → **3,880**. | user (2026-09-22, "it is a bit rash to commit to a position that rejects H1 completely at this phase") |
| R28 | **A mechanism reaches §5.2, and one hedged causal statement with it** (`decisions.md` **O13**, **A5**; probes in `audits/2026-09-22-theta-u-sign/`, printed by Appendix F block **F.9** and Eq. **(F3)**). The user relaxed R16's bar: *"The R16 bar on section 5.2 is a soft one, so we might consider promoting a mechanism claim to be included by section 5.2 if it is sufficently plausible."* **What is promoted.** (i) Eq. (F3): because the ensemble is $\{\chi,\ker\chi\}$, $\sum_y c_y = 2B^{\mathsf T}W\ell_0$ exactly (7.4e-13), so **$\theta_u^\ast$'s sign is fixed by the prior alone**, independent of $\Lambda$ and of the entry uttered; and the sign does not reach the belief, the settled field sitting within 4.9e-03 of Eq. (24)'s two-sided limit. (ii) Eq. (24)'s doubling displaces the read-out **+1.12** under shapes and **+1.39** under artifacts against data displacements of **+0.16** and **+1.06**, and §5.2 now says **"we think"** that near-constant displacement is the cause of the minimum class's misfit — the one causal statement the section makes, framed as a belief about **this phase**, since the class concerned is the one whose threshold O14 would reassign to $\theta_A$. §§5.1, 5.6 and 6 may not restate it as established. **What this corrects:** the agent had reported a $\theta_u^\ast$ sign flip between image conditions (−871 against +1605) and offered it as the mechanism; those were means of a sign-varying, ray-divergent quantity, and by median both conditions are negative (−720.9, −769.8). **B10/C7 is untouched** — the cell prints the quantities, Appendix F §6 describes them, and no notebook text says what the mismatch is due to. §5.2 650 → **800**, total → **4,030**; Appendix F gains §6 and Eq. (F3), cell count unchanged. | user (2026-09-22), applied the same day |
| R23 | **A footnote to §5.3 states the hypothesis that a case's representative tolerance scales with that case's Λ**, and the notebook demonstrates at two named ad hoc values, 1e-1 at Λ = 8 and 1 at Λ = 512. **The footnote states the claim qualitatively and cites the audit for numbers** (`audits/2026-09-21-tolerance-halting/lambda_and_tolerance.py`), because nothing in the notebooks prints a *matched* comparison — the Λ = 8 table reports updates at 1e-1 and the Λ = 512 table at 1, which is the keying itself. What the audit shows, matched by prior: at a fixed tolerance of 1 **every** prior takes three times as many updates at Λ = 512 as at Λ = 8, and at 1e-2 the rows that are not slow-started take eleven to seventeen times as many. The sharper form, and the one the footnote should lead with: **at Λ = 512 the flow halts at between 3.5% and 5% of θ\* under every prior and across a tenfold change of tolerance, while at Λ = 8 the same tolerances land anywhere from 0% to 30%** — so at large Λ the tolerance barely moves where the flow lands. The footnote is careful on four points. (i) It is a **hypothesis, not a fit**: two demonstration values are named, nothing is interpolated, no functional form is claimed, and the notebook raises on an unlisted Λ rather than guessing. (ii) It is **not** the relative tolerance |Δθ| < tol·|θ| that A19 rejects as a guard — Λ is a standing property of the configuration, fixed before the flow starts, whereas |θ| is where the trajectory has got to. (iii) It does **not** rest on any claim that integration cost is super-linear in Λ; that claim was the agent's error and is withdrawn (H9). (iv) It does **not** rest on the comparison the first draft gave — "the same 1e-1 halts the Λ = 8 flow after 15 updates and the Λ = 512 flow only after 61 to 173" — which set the gaussian prior at Λ = 8 against three *different* priors at Λ = 512. Matched by prior, two of the five go **down** at 1e-1, because prior-specific slow starts (H5) dominate at that tolerance. **Corrected 2026-09-22.** | user (2026-09-21), evidence corrected 2026-09-22 |
| R22 | **The paper OFFERS halting by tolerance as a direction, not a commitment** (`decisions.md` **A19**, demoted 2026-09-22; **D12**). The flow halts when its own update falls below a tolerance; θ\* stays the commitment (R10 unchanged); the tolerance is **ad hoc**, so no reported result depends on it. **The paper admits an unsettled locality violation and presents the hypothesis as a direction that could resolve the halting problem**: the *fast* loop's tolerance is keyed to λ_max(H), a global spectral quantity, which is a problem of the same kind as D4 and is not licensed by it, since D4 is itself an instance only under restriction. The *slow* rule |Δθ_u| < tol carries no such debt — it reads only the magnitude of the update the plasticity rule already forms — and the paper says which of the two is clean rather than treating them alike. The halting problem itself is **not** written off as an artefact of batching: it is real for the organism as well as the simulation (user, 2026-09-22), and Bogacz's own remark that parameters never converge is context in D12, not a dissolution. Beyond that, and the paper declines both to claim that an organism needs a tolerance for a computer's reason and to stipulate a value representative of the brain. What it argues is that a representative tolerance is almost certainly greater than 1e-9, so a real system halts earlier than the asymptote. §5.3 rests on the measured agreement (H2–H4 of `procedure_records/tolerance_halting.md`): the verdicts at a halted θ_u are the verdicts at θ\*, at about **1e-3** of the cost. **Corrected 2026-09-21**: this row first said 1e-4, which overstates it by an order of magnitude — the separation 4λ goes 9.3e6 at θ\* to 1.19e4 at the halt, and the step count 4.48e8 to 5.74e5, both ratios near 1/780. | user (2026-09-21) |
| R21 | **RSA's speaker-optimality parameter is written α_rsa throughout the dissertation** (Q8). The bare α stays the concentration of the prior Beta(α,1), as `main.ipynb` and `sections_3-6.md` §§4.5 and 5.2 write it, so Eq. (41)'s Λ_crit ≈ α log 2n is unambiguous where §1.3 cites it. Applied to `background_sections.md` §1.2 (the S₁ equation and its gloss) and §1.3; the notebooks never use α in the RSA sense, so none of them changes. | user (2026-09-21) |
| R20 | **Every verdict is reworked on the Λ = 512 data.** The conjunction holds under three of five priors, not none and not one, and the q position criterion under all five, so no prior meets the shift criterion alone. Sites V1–V13 and the three choices this opens (P-8 to P-10) are in the record §§9–10. §4.5's opposing floors are untouched and are where the trade-off claim is now sourced. The notebooks are **not** verdict sites (B10/C7). | user (2026-09-17) |

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

**2026-09-15, closed 2026-09-18 by U10 (site V13).** The table above is Part D as it stood on
2026-09-13 and is kept as the record of that state; it is **not** the paper's evidence any more.
The evidence is Text cell 4b's five rows at Λ = 512, which §4's §4.4 entry and `sections_3-6.md`
§4.4 now carry: the conjunction under **three** of five (flat, Beta(3,1), delta-like), the q
position criterion under **five**, no prior meeting the q shift criterion alone, and 33 of the 121
plane cells. Read the scope paragraph below as historical. Since B9 the
notebook reports Part D's four diffuse priors at Λ = 8, and in Text cell 4b all five priors at
Λ = 512, where the conjunction holds under **three** (flat, Beta(3,1) and the delta-like prior). The
scope sentence above therefore understates what the notebook now shows, and §§4.4, 4.5 and 6 below
rest on it. Rebuilding those arguments on the Λ = 512 data is open.

**2026-09-17.** That rebuild is now task **U10** of `procedure_records/ell0_placement_and_counterforce.md`, and it needs no new code: Text cell 4b and Code Cell 2b already print every row. The count moves to **three of five** (flat, Beta(3,1), delta-like), which under `agent.md` §5.4 is a headline change and is blocking decision **P-6** there. The §4.4 entry in §4 below was written against the Λ = 8 table and is stale in the same way; U10 corrects it too.

Two further findings that change the outline as much as the headline does:

- **The utility level's own contribution is negative under all five priors** (reach.md F8, now
  printed). The positive shifts under the four diffuse priors are tempering alone.
- **The halting claim is not written anywhere.** Neither outline, neither notebook and no record
  says that the maximizer of F supplies a halting mechanism. So item 2 is new material, not a
  correction of existing text.

## 3. Word allocation at 3,000, raised to 3,200 on 2026-09-17 (S-6), then to 3,450 the same day (P-3), then to 3,520 on 2026-09-22 (§5.5, for A19), then to 3,610 the same day (§4.2, for S-8/T15's n guard), then to 3,760 the same day (§5.2, for T10), then to 3,880 the same day (§5.2 and §6, for R27), then to 4,030 the same day (§5.2, for R28), then to 4,100 (§4.4, for item 1's delta read-out results once §3.6 existed)

| Section | Was | Now | What the change pays for |
|---|---:|---:|---|
| **3. The proposed architecture** | **800** | **1,085** | |
| 3.1 What the model must do | 90 | 90 | |
| 3.2 A continuous world state and a soft lexicon | 160 | **270** | R18: the Λ–ℓ₀ commitment and the g_S alternative (90); Λ → ∞ is RSA's literal listener (20) |
| 3.3 The chain, and the semantics of its threshold | 200 | **255** | R18: g_S carries no offset because ℓ₀ sits in g_L (10); R19: the projection parallel and the warning that it is not an equivalence (45) |
| 3.4 State units, error units, and what is local | 210 | 230 | Commitment 7 in exact form; θ_u learned, starting at the tempered control; conditioning |
| 3.5 Two choices the scale forces | 140 | 140 | |
| 3.6 Two read-outs (new) | — | 100 | Item 1 |
| **4. Evaluation** | **745** | **1,180** | |
| 4.1 What is compared | 100 | **140** | Naming (literal listener, tempered control); R18: q_lit is a fixed point only because ℓ₀ sits in g_L |
| 4.2 The criterion, and how to read the statistics | 170 | **260** | R25's n guard |
| 4.3 The specification holds | 90 | 70 | Trimmed to fund §4.5 (R14) |
| 4.4 The five priors (retitled) | 220 | **285** | New table with tempering/utility split; the Cremers parallel on q (R7); R20/P-10: the Λ = 512 table with Λ = 8 as a one-line contrast, and P-9's two counts |
| 4.5 The plane, and where both conditions hold | 165 | **255** | Conjunction thresholds across the band; the V under both read-outs (R14); P-8: the opposing floors are now where the trade-off claim is sourced |
| 4.6 What the verdict needs, against what θ\* costs (new) | — | 100 | The evidence item 2 rests on |
| **5. Discussion** | **705** | **1,650** | (the 980 written here on 2026-09-17 was stale: it predated §5.2's 200 → 400; 1,180 was stale in turn, predating §5.5's 80 → 150 on 2026-09-22 — corrected the same day. The grand total was right both times; this subtotal was not. Raised again to 1,400 on 2026-09-22 for §5.2's 400 → 550 at T10.) |
| 5.1 What an alternatives level would have to supply | 390 | 350 | Complexity-led; the q-normalization link added, the Cremers bullet moved out (R7), lines 329–338 removed (R14) |
| 5.2 Scale structure: a second prediction | 200 | **400** | R16/R17: H1 and H2 stated; the instantiation; the parity of the two entries; match and mismatch; the O14 sentence. The user raised the budget rather than trim §5.1 (S-6). |
| 5.3 Realizability, halting, and the plausibility commitment (new) | — | 170 | Item 2 |
| 5.4 What an algorithmic account makes posable (new) | — | 120 | Item 3 |
| 5.5 Limits (was 5.3) | 65 | **150** | Convergence of θ_u; conditioning; halting by tolerance (raised 80 → 150 on 2026-09-22 for A19) |
| 5.6 Predictions (was 5.4) | 50 | 60 | The timescale separation as a prediction |
| **6. Conclusion** | **150** | **165** | R18: one clause on item 1, which already names the counterforce without flagging it |
| **Total** | **2,400** | **3,610** | |

**2026-09-17, P-3 settled by the user: the budget is fine.** The table above is raised rather than
trimmed, 3,200 → **3,450**. The background pays separately: `background_sections.md` §1.3 goes from
340 to about **415** (R19's parallel and its warning), and under R8 the background states only its
own length, so no combined count changes.

**An arithmetic error found while applying this.** The §5 subtotal row read **980** after S-6 raised
§5.2 from 200 to 400: 350 + 400 + 170 + 120 + 80 + 60 = **1,180**. The grand total 3,200 was
correct, so only the subtotal was wrong. Corrected above.

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
  → add Code Cells A–D. **2026-09-21, applied by U13**, at P-3's 3,450 rather than R1's 3,000.
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

  **2026-09-17 (R20, site V1).** The replacement above was written when the conjunction held
  under **one** of Part D's five priors. On the Λ = 512 data it holds under **three**, and the
  q position criterion under all five, so the positive thesis is stronger and the sentence being
  replaced is false twice over, not once. R2's complexity basis is unchanged and needs no new
  decision; only its scope sentence moves. Consider adding the one structured fact that survives:
  **no prior meets the shift criterion alone**, so the two conditions are nested rather than
  opposed among these five.
  The specification-not-built sentence (lines 28–32) survives unchanged.
  **2026-09-18, applied by U12.** The constructive claim now states the verdict on Λ = 512 (three of
  five, the second condition under all five, nested among these rows) and on the plane (33 of 121,
  opposed floors), then R2's list, with P-8's floors argument added as its last item, marked as
  argued rather than measured. "The shape of its absence" is gone. The scope line (lines 4–5) is U13's.
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
- **2026-09-18, U12:** the criterion row's rewording is applied. The relay row and the three new rows
  are not, since they belong to R1–R17's revision and not to R20.
- **Tier A, the closed-vs-open-scale row (line 60).** Its "second empirical anchor" depends on Q7.
  The row stays in Tier A only if §5.2's prediction is rebuilt on the learned model.
- **Tier B, line 63.** §5.3 → §5.5.
- **Tier B, the O-corner bullet (2026-09-21, `decisions.md` O9 settled).** Applied: the bullet now
  states that this implementation predicts the O corner is just as representational, **and** that the
  prediction does not transport to the asymmetric phase of O14, with our position reserved on μ_u
  and no number quoted until a cell prints the equivariance.
- **Tier C, lines 74–77.** Remove "Conditioning and stiffness (Eq. 28)", which moves to Tier A.
  §5.3 → §5.5.

### Word allocation table (lines 81–103)

Replace with §3 above.

**2026-09-21, applied by U13** (the user folded this into U13 on 2026-09-18). The outline's table now
carries §3's figures with a "was" column, and the headings of §3, §3.4, §4, §4.3, §5, §5.1 and §5.2
are brought into line; §§3.2, 3.3, 4.1, 4.4, 4.5 and 6 were already moved by U9–U12. A note under
the table says which sections have bodies written to the new budget and which do not.
**The renumbering of §3's "Renumbering this causes" paragraph is applied with it:** Limits and
Predictions become §5.5 and §5.6 in the outline, and the four references follow
(`sections_3-6.md` Tier A's relay row, Tier B, Tier C, and `background_sections.md`'s commitment 3
row). §§3.6, 4.6, 5.3 and 5.4 are listed in the table but have no bodies yet; the note says so.

### §3.2 (lines 124–141) and §3.3's g_S bullet (lines 155–165): new, 2026-09-17 (R18)

- **§3.2, one bullet after "The price of a soft lexicon".** The commitment: ℓ₀ enters through g_L
  (Eq. 9), so the entry and the prior meet as a **difference** at one error unit,
  ε_L = φ_L − ℓ₀ + φ_S, and the level above reads that difference as c_y = BᵀW(ℓ₀ − φ_L). ℓ₀ could
  have entered at g_S instead; that is `decisions.md` **A3**, and it is a choice, not a consequence.
  Under the alternative the two never meet at a node, and the coupling becomes −BᵀW(ℓ₀ + φ_L) — the
  entry enters the same way under both, and the whole difference is the sign the prior carries
  against it. Reasons (a) and (b) of R18, plus the third: under g_L the literal listener is a fixed
  point of the network (σ_S → ∞), and under g_S it is not reachable at any σ. Detail and numbers go
  to Appendix D (P-1); the body quotes at most one.
- **§3.2, same bullet or the one above it (P-4).** Λ → ∞ is not merely "a hard truth-conditional
  constraint" but **RSA's literal listener**: log L₀ = log P(s) + log⟦u⟧(s) with log⟦u⟧ ∈ {0, −∞},
  and φ_S = ℓ₀ − Λχ_y is that with −∞ replaced by −Λ. One clause; the background's §1.2 notation
  is already fixed for it.
- **§3.3, the g_S bullet.** One clause: g_S carries no tonic offset **because** ℓ₀ sits in g_L, with
  the pointer to §3.2. The bullet currently reads as though g_S having no offset were given.
- **§3.3, "The chain terminates in utility" (R19).** This is the appropriate place for the
  projection statement, because it is where the coupling lives: the utility level reads
  c_y = BᵀW(ℓ₀ − φ_L), **a linear projection of the same log quantity RSA's S₁ reads**. Attach the
  warning here, in its exact form (G10): rank 2, BᵀW1 = 0, blind to the constant the normalizer
  occupies — so the similarity is a projection and **not** an equivalence, and treating it as one is
  dangerous. Roughly 45 words, part of P-3's total.
- **Budget.** About 90 words in §3.2 and 20 in §3.3 — **blocked on P-3**, and §3's word table is not
  edited until it is answered.
- **Not a reopening.** Every finding behind this block is a reason **for** A3 as it stands
  (`agent.md` §3.1); A3 gains a dated amendment (U2) and stays settled.

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
- **Lines 222–225 (2026-09-17, R18).** The sentence that q_lit "is a fixed point of this network rather than an external construction" is true **because** ℓ₀ sits in g_L (A3). Under the g_S placement ℓ₀ − φ_L is reachable at no σ, so the sentence that removes the "built to be beaten" objection would not be available. Add the dependency in a clause and point to §3.2.
- **2026-09-18, applied by U10.** The A3 clause, the two renamings, "where learning starts", and
  DEC5's one sentence, with a writer's note that it does not contradict §3.2 (the L₀ identification
  holds only as Λ → ∞, a limit and not a setting). Heading 100 → 140 (P-3). **The line 230 pointer
  to §3.6 is APPLIED, 2026-09-22**, §3.6 now existing: the bullet reads "q_H, the settled belief
  read through q".

### §4.2 (lines 234–253)

- **Lines 236–240.** Add one sentence that both conditions are stated on the read-out q (A16).
- **Lines 247–253, the guard.** Both measured instances in the outline are fixed-θ_u controls, which
  under B4 may appear only as stated controls. Under learning the φ_S-contrast deviation across μ_u
  settings is 3.19e-2 (not 3.6e-15), and Δ_some's spread across the six μ_u settings collapses to
  +0.0008 to +0.0009 (Text cell 5 Part B). Either label the instance as a control and say what it
  controls for, or take the instance from the learned model: the φ_S contrasts across Part D's
  priors agree to 5.3e-15 at a shared θ_u (a control) and differ by 0.0575 at each prior's own θ\*.

- **New bullet at the end, R25 (S-8/T15, applied 2026-09-22): the second guard, that the verdicts
  are relative to n.** About 90 words, raising §4.2 from 170 to 260 and the total to 3,610. Says:
  θ_L = log(2n − 1) fixes the cell of *all* and n = 10 is stipulated, not measured; across both
  Λ and all four base priors the q shift criterion changes status somewhere on a sweep of n, and
  **where** it changes depends on Λ, so granularity and lexical strength are not separable; and two
  cautions — a sweep **brackets** a change rather than locating it, and a status change may be the
  sign flip of a quantity decayed to 1e-07. Source: Code Cell A, `granularity_report`. A companion
  clause goes to §5.2's *Calibrate the claim* bullet. **Not claimed here:** anything about what
  should fix n (O1 is untouched).

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

**2026-09-17 (R20, sites V4 and V5): this entry is itself stale.** It was written against the Λ = 8
table. Rebuild the section on Text cell 4b's Λ = 512 rows, which are already printed and need no new
code: the q position criterion under **five of five**, the q shift criterion under **three** (flat,
Beta(3,1), delta-like), **no prior meeting the shift criterion alone**, and the shift deepening with
prior mass on the all-region (0.0479, 0.1367, 0.9568). Whether the section carries one Λ or two is
**P-10**; the anti-exhaustive count — four of five at Λ = 8, **two of five** at Λ = 512 — is **P-9**.
The Eq. (24) mechanism paragraph (lines 290–297) survives either way.

**2026-09-18, applied by U10, and three corrections to this entry.** §4.4 is rebuilt on Text cell
4b's Λ = 512 table (with the tempering and utility columns from Code Cell 2b), Λ = 8 as one bullet
of contrast, retitled "The five priors", heading 220 → 285.
1. **"Negative under all five" holds at Λ = 8 only.** At Λ = 512 the utility level's contribution is
   negative under four priors and **positive under Beta(1,3), +0.0024** (Code Cell 2b). The
   decomposition bullet says so.
2. **"Four of five at Λ = 8" (P-9) is imprecise.** The delta-like prior has no Λ = 8 row; it needs
   Λ = 512. At Λ = 8 the anti-exhaustive direction holds under **all four priors that have a row**.
   §4.4 states it that way.
3. **"The direction being what raising Λ removes" (the gloss on P-9) is half true.** Raising Λ
   removes it under the flat and Beta(3,1) priors and **enlarges** it under the Gaussian
   (+0.0008 → +0.0071) and Beta(1,3) (+0.0004 → +0.0089). §4.4 states both halves.
- The mechanism bullet survives, with its evidence confined to what is printed: Eq. (23) at the
  Gaussian θ\*, and the Eq. (24) limit on the delta-like row. The claim that every θ\* at Λ = 512
  sits in Eq. (24)'s saturation is Text cell 4b's prose and is **not** carried, since no cell prints
  it for the four diffuse rows.
- **APPLIED 2026-09-22**, §3.6 now defining the read-outs: item 1's delta read-out results are in
  §4.4, each with its Λ named, and with the guard that neither read-out is the corrected version of
  the other. §4.4 285 → 355. The §4.6 pointer is still one sentence pointing to a section not yet
  written.

### §4.5 (lines 298–317)

- **The band.** 22 cells → **33**; band (8,128)–(128,2048) → **(1,512)–(128,2048)**. The
  delta-like row is inside the band, at its lower edge in Λ.
- **2026-09-17 (R20, site V6).** §4.5 is now where the trade-off claim is **sourced**, not merely
  illustrated. The floors table (Code Cell 4, printed) gives q shift 512/256/128/64/32/32/16/2/2/2/2048
  and q position 2/2/2/2/64/256/512/1024/—/—/— over α = 1…1024: opposing directions, crossing at
  α = 16. At Λ = 512 both hold for α = 1 to 64, which is why Part D's five rows no longer show the
  tension. Keep the floors sentence and let §5.1 and §6 point here (P-8).
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

    Report it as a result, and derive no evidence for a missing level from it. Its numbers are
    printed by Code Cell 4's `plane_summary` (2026-09-15).
- **Override law.** Learned slopes 1.9890 / 2.9334 / 4.3102, +36–45% over the tempered control
  ("severed" means that control). The 15–18% at θ_u = 1 is a control and is labelled as one, or cut.
- **Spread D.** 0.0061 → 0.0009 → 0.0002 becomes 0.0057 → 0.0012 → 0.0003.
- **Add.** Across the 33 cells the least |θ_u| meeting the conjunction runs from 0.100 to 4.250,
  with λ_max(H) between 2.0 and 20.1 there, so every cell is integrable at the θ_u its verdict
  needs. At their own θ\* the same cells have λ_max(H) between 3.5e4 and 3.6e7.
- **2026-09-18, applied by U10**, heading 165 → 255. The trade-off claim is stated on the floors
  (P-8 (i)), "under every prior tested" is barred there, and Eq. (41) is named as the exchange rate of
  §3.2's contest. The θ_u = 1 control slopes are **cut**. Two small corrections: the floors cross
  **between α = 8 and α = 16**, not at 16 (64/2 at α = 8, 32/64 at α = 16); and the severed-level
  slopes match Eq. (41) to within **4.1%**, not 4% (ratio 1.041 at θ_L = 1). The V refers to the
  delta read-out's criteria by §3.6 and R12, which §3.6 must define when it is written.

### §4.6 What the verdict needs, against what θ\* costs (new, about 100 words)

Evidence for §5.3, reported without interpretation:

- Under the delta-like prior the conjunction first holds at |θ_u| = 2.126, where λ_max(H) = 6.5
  and commitment 7 demands a separation 4λ = 26. Eq. (20) from 0 passes that θ_u in one update.
- **Updated 2026-09-21 (A19, HA4):** the realizable θ_u is no longer the one that update reaches.
  It is where the flow **halts**, its own update having fallen below the tolerance — the only
  stopping rule the model has. Under the delta-like prior at Λ = 512 that is θ_u = **34.695** after
  **7** updates, and the integrated run there (**242,163** Euler steps) gives Δ_some = **−0.5208**
  and q_H = **0.4361**, both criteria met. λ_max(H) = **1205.8**, a separation of **4,823**. The
  superseded figures — 39,035 steps at θ_u = 13.3749, Δ_some = −0.5182, q_H = 0.4386, λ = 180.9 —
  came from stopping the flow on the evaluator's own criterion, which A19 no longer counts as
  locating a realizable θ_u.
- The same inference at θ\* = 1407.77 would take **3.98e8** steps, about **5.0 hours**, at a
  separation of 7.9e6. (Was "4.28e8 steps, hours". The step count moved because the stopping
  tolerance is now keyed to λ_max(H); the *claim* is unchanged and the figure is now a within-regime
  extrapolation rather than one across the convergence boundary a fixed tolerance created — see
  H9/H11/H12 of `procedure_records/tolerance_halting.md`.)
- The Eq. (20) flow from 0 is not integrable to θ\*: it is not within 0.1% of θ\* after 5,000
  updates (F15). That θ\* is reached rests on the closed form and the monotone rise.

### §5.1 (lines 322–435)

- **Framing (lines 324–327).** Lead with the complexity argument (R2). Lines 344–397 survive
  intact: the negative search, what is searched versus what branches, the binary inventory, the
  *most* case, the dimension and locality payoff, and binarity at the generative map.
- **Lines 329–338, "Why the pattern points at such a level". Removed (R14).** The V is reported in
  §4.5 and motivates nothing here.
- **Lines 339–343, the Cremers corroboration. Removed from §5.1 (R7).** The parallel moves to §4.4.

  **2026-09-17 (R20, sites V7 and V8).** The removed bullet's *claim* — prior concentration buys
  the first condition and spends the second — still stands in §6 item 3, and on the Λ = 512 data it
  is false of the five priors and true of the **floors** (record G11: the two floors run in opposite
  directions and cross at α = 16; §4.5's result is untouched). Where that claim is sourced from now
  is blocking decision **P-8**. The Cremers count moving with it is **P-9**.

  **2026-09-18, applied by U12 (P-8 (i)).** Both bullets are replaced by one: the case is complexity
  (R2); the criterion adds what the level would change, stated on §4.5's floors, marked as argued
  from them and not measured; "under every prior tested" is barred; the old reading (R14) and the
  corroboration (R7) are named as withdrawn. The framing paragraph (lines 324–327, "lead with the
  complexity argument") is **not** rewritten here; it belongs to R2's own revision of §5.1.
- **Add after lines 388–397: the read-out link (R4, about 40 words).** Content in §5 below, item 1.
- **Lines 398–420, what is not derived.** Survives. Add to its list that an end to learning short
  of the slow maximizer is also a claim about the unbuilt level (item 2).
- **Lines 422–431, the position on the current gain.** Survives. The four exposure-only θ\* values
  (−11.2844, −44.1766, −65.7004, −28.4375) are printed by Code Cell B, *ALTERNATIVE SPACES*.
- **Lines 432–435, standing qualification.** Survives.

### §5.2: **CLOSED 2026-09-22 by T0–T13** (re-examined 2026-09-14, rewritten at T10)

**The rewrite is applied.** §5.2 is now *Scale structure: two hypotheses, and where the model
matches*, 400 → **550 words** (§3's budget rises to 3,760). Every number it quotes is printed by
**Code Cell F** of `main.ipynb` (Appendix F, cells 22–23), so none of it is class (e) any more, and
the audit below is no longer a source the prose cites. What the rewrite carries: H1 and H2 stated as
hypotheses and not adopted; the relative class **not modelled**, so H2's open-scale half is stated
and left untested (O14); Λ fitted per class, for H1 alone, with the ladder reported as a **bracket**;
match and mismatch reported with **no sentence about what any mismatch is due to** (R16); the
ensemble stated as the inventory's, never the experiment's (X7/F20); the parity paragraph kept and
restated at n = 4 (S-7); and the instinct at the close, pointing back to §5.1 (the user's choice of
site, 2026-09-22). The old prediction — the monotone trend in the cut's position and its reversal
under a sharp prior — is **gone**, per F13.

**Two corrections the rewrite had to make**, both recorded in `decisions.md` E16:
- The 2026-09-17 audit scored the model against 10 rows of an item that drew **no** Experiment 3
  response. Dropping them moves the maximum class's R² from 0.953 to **0.993** and the minimum
  class's from 0.401 to **0.434**, and the measured image-type difference from −1.13 to **−0.83**.
- F12's backwards prior-manipulation sentence is fixed here and in background §1.7 (T11).

The re-examination that follows is kept as the record of how §5.2 got here.

#### The 2026-09-14 re-examination (superseded above)

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

**2026-09-17: the user's scale-class hypothesis, checked against Xiang et al.'s own data.**
Record `procedure_records/scale_classes_hypothesis.md`; audit `audits/2026-09-17-scale-classes/`;
decision O13; the 2026-09-14 findings above are unaffected and still hold.

The user proposes that (H1) scalar expressions with unstable atomicity carry weaker lexical
strength Λ, and (H2) open-scale adjectives behave like *some* while complete-scale adjectives behave
like endpoint(s) + *some*. Instantiating Xiang et al.'s five scale positions as the five Voronoi
cells of a predicate resolving n = 4 atoms (Eq. A5, θ_L = log 7), Eq. (A1) supplies the three
classes directly: maximum-standard = *all*, minimum-standard = *some*, relative = a cut at a
context threshold. The antonym each item pairs the adjective with is, in that adjective's own
orientation, the entry's complement, so the exposure ensemble is {χ, 1 − χ} throughout, which
answers half of O8 for this paradigm.

- **The model was run on their 96 items, with their elicited priors, against their Experiment 3.**
  Posterior-degree R² **0.81** overall, against their LG 0.78 and QF 0.82; by class **0.95 / 0.40 /
  0.80** (max / min / rel) against LG .94/.55/.69 and QF .97/.58/.78. The literal listener alone
  gives .95/.09/.20, so **the utility level is what earns the fit wherever an endpoint does not
  already fix the answer** — a result §5.1 and §5.2 can both use, and one the outline does not
  currently have.
- **The minimum class is this model's residual too**, as it is every model's in their paper (their
  ST model .19, their hybrid .32). §5.2 must not claim otherwise.
- **H1's ordering holds in the form "a finite Λ is required".** The maximum class's fit is flat from
  Λ = 8 to Λ = 2048, so the data put no upper bound on its lexical strength; the minimum class peaks
  at Λ ≈ 32 and the relative class at Λ ≈ 16, both falling away above. A predicate anchored at the
  scale's own endpoint behaves as a hard entry; the two whose thresholds depend on something
  unstable do not.
- **The one credible empirical interaction is reproduced in the right class and the right direction,
  at one seventh of its size.** Xiang et al. find an image-type effect for the minimum class only,
  in both experiments. In mean scale position, shapes minus artifacts: their prior +0.84 / −1.12 /
  −0.00, their data −0.22 / **−1.13** / +0.23, this model +0.03 / **−0.16** / +0.01. The model
  matches −1.13 only at Λ ≲ 2, where the class's fit collapses; **no single Λ fits both halves**
  (shapes want Λ ≈ 6, artifacts Λ ≈ 24). That is H1 in a within-class form, and nothing else in the
  model produces it: m = 3 and m = 4 leave the effect at −0.17 and −0.04.
- **The between-class interaction §5.2 claims is there.** The maximum-minus-minimum gap is larger in
  the shape condition than the artifact one, in the data (1.32 against 0.41) and in the model (0.61
  against 0.42).
- **§5.2's and §1.7's description of the prior manipulation is backwards.** Both call shapes the
  impoverished-prior condition and artifacts the rich-prior one. The authors report the opposite
  about the priors themselves — "artifacts tend to have a less categorical distribution than shapes,
  in particular for the dimensions corresponding to absolute adjectives" (9:19) — and their elicited
  priors bear it out (minimum class, mean position 1.19 for shapes against 2.31 for artifacts). The
  shape condition is impoverished in world knowledge and **sharper** in elicited prior. Any sentence
  about prior sharpness must be stated on the elicited priors, not on the labels. This is a
  correction to the empirical-fit paragraph and to background §1.7, whichever way Q7 goes.
- **What this does to the prediction.** The comparison the data make is not a monotone trend in the
  cut's position under one prior sharpened: the classes differ in **which cut** they carry and in
  **Λ**. A §5.2 rebuilt on this would state (i) the class-to-entry map, which is H2 and which the
  data support; (ii) that the utility level is required off the endpoint and not at it; (iii) the
  Λ ordering of F6; and (iv) the one interaction, with its size named as a shortfall rather than a
  match. Whether to state any of it is Q7, and whether H1 and H2 are adopted at all is O13.
- **Costs to weigh under O13.** H2's open-scale half needs a cut t that is neither endpoint nor
  1/2n, so t joins θ_L as a quantity of the entry, and Appendix A's identification argument ("θ_L
  enters twice") is written for a θ_L that is both the gain and the cut. H1 makes Λ a function of
  atomicity, which gives the Λ axis of the plane a linguistic reading (a position on it becomes a
  property of the expression — worth §4.5) but couples two quantities Text cell 3 §3 now fixes
  independently.
- **Nothing is printed by a cell**, so every number here is class (e) under `agent.md` §3.3. Quoting
  any of it needs a five-position configuration the notebooks do not contain.

**2026-09-17, the change the user directed (R16).** §5.2 is to **state both H1 and H2, then report
where the model's prediction matches Xiang et al.'s data and where it does not, making no claim
about the nature of the mismatch**, with every quoted number reproducible — which under C6 means
printed by a new **Appendix F** and **Code Cell F** in `main.ipynb`. The task list, the acceptance
test for each task, and the seven decisions that block the first of them are in
`procedure_records/scale_classes_hypothesis.md` §§7–10. In outline:

- **Blocking (S-1 to S-7, the user's).** Whether a fitted Λ may be quoted at all and what class of
  quantity it would be (nothing in this project is fitted, so a best-fit Λ is class (e) as things
  stand); whether the relative class enters, which needs a cut *t* beside θ_L and touches Appendix
  A's identification argument; whether their data may sit in the repository, without which no R²
  can be printed; n = 4; whether a cell may print a published number; §5.2's word budget; and
  whether the κ parity paragraph stays.
- **Tasks (T0–T13).** Checkpoint; the data file; Code Cell F; the Appendix F markdown cell;
  structure and ToC; references; the coupling check; execution; `agent.md`; `decisions.md`; the
  §5.2 prose; background §1.7; this file; commits.
- **What this closes and what it cancels.** Q7 is answered on three of its four points by the
  instruction itself, and the fourth (the empirical-fit paragraph) becomes T10. The 2026-09-14 site
  changes stand: the magnitudes, "monotonically", the sharp-prior sentence and the "(… at θ_u\*)"
  parenthetical go. **The mechanism paragraph goes with them**, since a mechanism *for the mismatch*
  is what the instruction rules out; a mechanism for what the model does predict is still allowed,
  and is where the κ parity paragraph would sit if S-7 keeps it.
- **Word budget.** Settled: §5.2 goes from 200 to 400 and the §§3–6 total from 3,000 to 3,200. The
  user raised the budget rather than take it out of §5.1 (S-6).
- **Scope, settled 2026-09-17 as R17.** §5.2 models the **two absolute classes only**. The 56 items
  those classes carry give R² 0.953 (maximum) and 0.401 (minimum), 0.804 over both, against 0.728
  for the literal listener and 0.789 for the tempered control — so the utility level's whole
  contribution sits in the minimum class. **The relative class's 0.80 is not reported**, since it
  comes from a configuration the model does not have. H2 is stated in full and its open-scale half
  is named as untested.
- **The parity paragraph stays** (S-7), restated at n = 4: the entries for *all* and for *some* have
  identical tilt loadings and exactly opposite width loadings, so at the utility level they differ
  in the even coordinate alone. The old ratios (0.219, 0.633, 1.07) go with the old prediction. This
  is also where the symmetry O14's instinct doubts is stated, which is why it earns its place.
- **One sentence of instinct** (O14), at the close, pointing back to §5.1: the two endpoints may not
  be symmetric. **θ_L is the lexical level's and stays there, inferring the boundary of 0; only the
  boundary of 1, θ_A, would belong to an alternatives level.** Stated as an instinct, promising
  nothing, and **not** offered as an account of the mismatch — R16 still holds over the rest of the
  section. §5.1 is not altered: naming θ_A among what the level "would have to supply" would turn
  the instinct into a promise.
- **Which boundary each modelled class sits on**, as Eq. (A1) already stands: the minimum class is
  *some*, fixed by the 0 boundary; the maximum class is *all*, fixed by the 1 boundary. §5.2 may say
  that much, since it describes the present model. It draws nothing from it.
- **Not started.** No notebook cell, no outline line and no `agent.md` row has been touched for this
  change.

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

  **2026-09-17 (R20, site V9).** "Under every prior tested" must go whatever P-8 decides: at
  Λ = 512 the position criterion holds under all five and the conjunction under three. If P-8 takes
  option (i) the clause becomes a pointer to §4.5's floors, not to Part D. **Item 1 (lines 505–508)
  needs no rework and is the natural home for one clause of R18** — it already says the entry
  "compet[es] additively against the world prior in the same log-density", which is the counterforce
  named without being flagged as a commitment.

  **2026-09-18, applied by U12.** Item 1 gains the clause flagging the placement as a commitment
  (§3.2). Item 3 now says the network meets both conditions (three of five at Λ = 512, a band of the
  plane, within two updates of learning) and that what a level would change is the cost: the
  opposed floors (§4.5, P-8) and the missing end to learning. Heading 150 → 165 (P-3). Item 4 is
  Q7's and untouched.
- **Add a clause** for item 3 of §5 below (not posable at the computational level), if §6's budget
  allows.
- **Item 4. RESOLVED 2026-09-22 at T10, with Q7.** It said the threshold semantics predicts "an
  endpoint-orientation asymmetry … sharpest where prior knowledge is weakest" — the old §5.2
  prediction, whose sharp-prior half rested on entries overridden at Λ = 8 and whose open-scale term
  names a class the model does not carry (O14). **Rewritten**: the classes are distinguished by the
  entry each carries and by the lexical strength each requires, the endpoint-anchored class putting
  no upper bound on Λ and the other requiring a finite one, with the residual reported and not
  explained. §5.6's corresponding prediction bullet is rewritten the same way.

### Open items (lines 539–569)

- **Open item 1 (lines 541–549). CLOSED 2026-09-22 at T2/T7.** It said "the §5.2 magnitudes are not
  yet in the notebook". They are: Code Cell F prints every one, and the C6 sweep over the rewritten
  §5.2 returns no number without a printed source. The magnitudes themselves are not the old ones —
  the loading ratios and utility contributions went with the withdrawn prediction (F13) — and what
  replaces them is the class comparison. The drafted probe it mentions was never found and is not
  needed.
- **Line 552.** `background_sections_outline.md` is now `background_sections.md`.
- **Add.** A pointer to this file.

---

## 5. The new material

### Item 1. The two read-outs — **§3.6 WRITTEN 2026-09-22; results applied in §4.4** (about 100 words; link in §5.1, about 40 words)

**§3.6 now exists** in `sections_3-6.md`, between §3.5 and §4: the delta at the settled state and
$q$, each with what it assumes, supplies and costs; the shared mode; that tempering is invisible to
the delta, so the tempering/utility confound in $\Delta$ is a property of $q$; and the forward link
to §5.1 (the normalizer is a normalization across a represented set). No number is quoted in it —
the results belong to §4.4.

**The two entries that were blocked on it are applied.** §4.1's last bullet now reads "$q_H$, the
settled belief read through $q$", pointing to §3.6. And §4.4 gains item 1's delta read-out results,
with **each configuration named**, since the two read-outs are reported at different $\Lambda$:
Part D's four diffuse priors at $\Lambda=8$ (peaks $0.5000\to0.5890$, $0.5000\to0.6726$,
$0.2535\to0.3274$, $0.7465\to0.8429$, all moving **up** the scale while the utility contribution to
all-region $q$-mass is negative — the read-outs disagreeing in direction); the mode position
criterion already met by $\ell_0$ alone on those four, the cell of *all* starting at $s=0.9500$;
and the delta-like row at $\Lambda=512$, the one place the model moves the peak out, $0.9852$
inside to $0.9468$ outside, stable on grids of 201, 401 and 801 nodes. §4.4 285 → **355**, §4
1,110 → **1,180**, total → **4,100**.

**Three stale section-heading totals were found and fixed in passing**: §4 said 1,020 against the
table's 1,110, §5 said 1,250 against 1,650, and §6 said 165 against 185. Every heading now agrees
with the word table, and the table adds up at every level. The §5 and §6 figures were this session's
own (R27/R28); §4's predates it.

**Still open from this item:** the §5.1 link of about 40 words. §3.6 now supplies the sentence it
would point at.

#### The plan, as written

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

**What follows, printed by Code Cell 2's delta read-out block, and by Code Cell 2b for the
delta-like prior (B9, 2026-09-15):**

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
  utility level's own contribution runs the other way under every prior. **(2026-09-18, U10: true at Λ = 8
  only. At Λ = 512 it runs the same way under Beta(1,3), +0.0024 of a +0.0089 shift. §4.4 carries
  the correction.)** The tempering exists only
  for a read-out that normalizes: the delta's peak does not move under the halving. Under q,
  therefore, the positive shift is the tempering. Under the delta read-out the mode of φ_S\* also moves up the
  scale on the same four priors (R12). Because halving does not move a mode, that movement is the
  utility level's. It is not a probability of *all*: the mode stays outside the cell of *all*. Why
  the utility level produces it is measured in Appendix C §8 (2026-09-15): the utility field's tilt
  part moves the mode, and its width part is what lowers the all-region mass.
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

The cost sense keeps the name "realizability" (O7, settled). The content, per R9 and R10.

> **Revised 2026-09-21 by `decisions.md` A19.** When this item was written, no self-contained
> halting mechanism was known and the section's argument was built around that gap. There is one:
> **halting is by tolerance**, and it is implemented (`procedure_records/tolerance_halting.md`
> HA1–HA9). The bullets below are updated where that changes them and marked where it does not.
> **R10 is unchanged in its conclusion and changed in its reason** — θ\* stays the commitment, but
> now because the tolerance is *ad hoc*, not because no mechanism exists.

- **What halts, and on which timescale.** The claim concerns the slow flow of Eq. (20), which
  ascends F̃ toward θ\* (Eq. B2), the value A9 commits the model's θ_u to. Since θ_u is an exposure
  statistic across trials (A14), "halting" here is the end of plasticity across exposures, not the
  end of one inference. (Within an inference the fast subsystem settles at whatever θ_u the slow
  flow currently carries, by §8.1.) **Revised:** the fast subsystem's stopping tolerance is no
  longer a mere numerical surrogate set beside the real question. It is **the same mechanism at the
  other timescale**, and I3 is revised to key it to λ_max(H), because the roundoff floor it must sit
  above is not a constant. That the same kind of rule ends both loops is part of what §5.3 says, not
  an implementation aside.
- **Why the maximizer does not halt the flow.** A flow halts where its gradient vanishes, at θ\*.
  From θ_u(0) = 0 the flow rises monotonically toward θ\* but is not within 0.1% of it after 5,000
  updates (F15): F̃ flattens toward its asymptote, so the flow approaches without arriving. Nothing
  **in F̃** stops it earlier — which is the point, because what stops it is not in F̃.
- **What does halt it (A19, new).** The flow halts when **its own update falls below a tolerance**.
  The rule is self-contained in the way the old ad hoc stopping rules were not: it reads the size of
  the step the unit has just taken and nothing else — no closed form, and nothing about the shape of
  the trajectory, to which the unit has no access (H1). No guard is attached, on the user's
  principle that a guard would require exactly the knowledge of its own trajectory the commitment
  denies the system. **The value is ad hoc**: the paper offers halting *by* a tolerance, not any
  particular tolerance, and declines both to claim an organism needs one for a computer's reason
  and to stipulate a value representative of a brain. **And it is offered as a direction, not a
  commitment** (A19 demoted 2026-09-22): §5.3 admits the unsettled locality violation of **D12** —
  the fast loop's tolerance is keyed to λ_max(H), a problem of the same kind as D4 — and presents
  the hypothesis as something that *could* resolve the halting problem. The slow rule carries no
  such debt and §5.3 says so, rather than demoting both loops alike. Two implications follow and are stated as such:
  a plausible tolerance halts **far short of θ\***, and where the flow *starts* slowly the same rule
  halts it **at once**, leaving the belief at the tempered control (H5).
- **Why that matters: cost rises while the verdict stands still.** Commitment 7 ties the error
  units' speed to λ_max(H), which grows as θ_u². Under the delta-like prior the conjunction holds
  from the first update on, at a separation of 26 where it first holds. Every later update leaves the
  verdict as it is and makes each later inference costlier: **4,823 at the θ_u = 34.695 where the
  flow halts**, rising toward 7.9e6 at θ\*. (Was "about 724 at θ_u = 13.37", the criterion-stopped
  value A19 retires.) Across the 33 both-condition cells of the plane, the separation needed where the
  conjunction first holds is at most about 80 (4 × 20.1), against 4 × (3.5e4 to 3.6e7) at θ\*.
- **Consequence without the alternatives level.** A mechanism outside F̃ must stop or slow the
  flow. **It has been supplied and it is a tolerance** — not a term of F̃, exactly as this bullet
  anticipated. What it still owes is the argument this bullet asks for: its locality (it reads one
  scalar the unit already has, so this looks cheap to make) and its standing against Bogacz (2017),
  which needs a divergence-register entry. Check the tutorial's own remarks on parameter convergence
  before citing it either way (agent.md §3.2). **Not yet written.**
- **Why θ\* stays the commitment (R10; the paper's explanation goes here). The conclusion stands;
  the reason is now the opposite of what it was.**
  - The mathematical model predicts θ\* as the value the slow flow ascends toward. It is the
    **asymptote**, and it carries no tolerance.
  - **Formerly:** no self-contained halting mechanism had been determined, and every lower θ_u the
    evaluation reported was located using θ\* already known in closed form — by bisecting fractions
    of it, or by stopping the flow on Part C's criterion, a statistic of q against q_lit computed
    outside the network. A simulated system must be assumed agnostic to θ\*, so none of those could
    be adopted.
  - **Now:** a mechanism exists and is implemented, and the halted θ_u never mentions θ\*. What
    keeps θ\* as the commitment is no longer the absence of a mechanism but the **ad hoc status of
    the tolerance**: a result reported at a halted θ_u would carry a number this study declines to
    fix, so predictions are reported in closed form at the asymptote, which carries none.
  - The two old stopping rules are **retained and relabelled**, not deleted. θ_crit = 2.126 and the
    one-update arrival still measure *where the conjunction is first met*, which the evaluation
    reports as a fact about the **shape of the update** and explicitly not as a halting rule.
    A realizable θ_u is now the halted one, and it is reported with the tolerance it halted at on
    its face.
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
- **Lines 166–185, §1.3 Beat 2, and §1.2 (2026-09-17, R18).** Beat 2 already states the inverted
  parallel — wRSA makes *the prior* defeasible against the utterance, this architecture makes *the
  lexical entry* defeasible against the prior. Extend it, about 50 words, with what RSA has and does
  not have. Has: the Λ → ∞ limit **is** RSA's literal listener (§3.2 states it there too); and a
  "where does the prior enter" degree of freedom of its own, resolved the other way, P(s) appearing
  in L₀ and again in L₁ ∝ S₁(u|s)P(s) — a contrast, in one sentence, possibly better placed in §1.2
  where the three equations already sit. Does not have: any single counterpart to a finite Λ. RSA's
  ways of letting prior and semantics trade off use a **latent variable** rather than a strength —
  lexical uncertainty (Potts et al., 2016), threshold uncertainty (Lassiter & Goodman, hence Xiang
  et al.'s LG model, which ties this to §5.2), and wonkiness (Degen et al., 2015) — and **nothing in
  RSA plays the role of Eq. (41)'s Λ_crit ≈ α log 2n**, the exchange rate that quantifies the
  counterforce. That last point is the part of the commitment with no parallel at all, and is the
  one worth the words.
- **The projection parallel, foreshadowed here and warned about (2026-09-17, R19; P-4 and P-5
  settled).** S₁ reads log L₀(s|u); the utility level reads BᵀW(ℓ₀ − φ_L), a **linear projection of
  the same log quantity**. The background foreshadows the similarity and, in the same breath, warns
  that **a projection is not an equivalence** and that forgetting the difference is dangerous. Give
  the warning its exact form rather than as a caution: BᵀW1 = 0 (9.4e-17), so the coupling is rank 2
  and **blind to the constant direction — exactly where log L₀'s normalizer lives**; adding 3.7·1 to
  the field leaves c_y unchanged to 1.4e-14. Two coordinates of the scale, the tilt and the width of
  Appendix C, and nothing else. **The nuance that must not be got wrong:** the invariance is of the
  *coupling*, not of the model — φ_S\* is not defined up to a constant (§9.1 has no flat direction,
  and Appendix D §3's third reading turns on it). This satisfies line 373's instruction by making
  the disanalogy precise, rather than by leaving the parallel out.
- **2026-09-18, applied by U11** (the two bullets above, and Beat 3's forward pointer, V11). All
  three RSA points go in Beat 2, including the P(s)-twice contrast: §1.2's budget was not raised,
  §1.3's was (P-3), and Beat 2 can point back at §1.2's equations. Beat 2's heading 100 → 175, §1.3's
  340 → 415, Part I's 2,035 → 2,110, and the target length 3,595 → 3,670 (R8: the background's own
  length only). Lassiter & Goodman (2017) is added to the reference list, marked [verify]. Beat 3's
  pointer now goes to §4.4, gives P-9's two counts as U10 corrected them, names the tempering, and
  drops "corroboration" and the drain. **Found:** α names two things, RSA's speaker optimality
  (§1.2) and the Beta concentration of Eq. (41) and §4.5; the background states the override law in
  words for that reason, and the clash is open question **Q8** below.
- **§1.7 (lines 309–334), the answer to Q3b.**
  - The outline says of Q3b "Do not answer it here. §5.2 answers it from the parity structure of the
    utility basis". That overstates what §5.2 can now claim. Parity fixes the entry's width loading,
    but the measured contribution is carried by the tilt, and under learning the prior's width enters
    too.
  - Soften to "§5.2 takes it up", pending Q7.
  - The literature bullets survive. The Leffel et al. check is still pending.
  - **2026-09-17: one bullet is wrong and must change whatever Q7 decides.** "the difference is most
    dramatic in the impoverished-prior (geometric shapes) condition rather than the rich-prior
    (familiar artifacts) one" has the prior manipulation backwards. Xiang et al. report that the
    elicited shape priors are the **more** categorical ones (9:19), and their data agree. The
    between-class difference is indeed larger in the shape condition (1.32 against 0.41 in mean
    scale position), so the claim survives; its explanation does not. State it as a contrast between
    novel and familiar objects, and say which way the elicited priors actually go.
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

**Resolved:** Q1 as R7, Q3 as R8, Q4 as R9, Q5 as R10, Q2 as R14, Q6 as R15, Q7 as R16.

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

**Printing (C6). Done 2026-09-15.** Every delta-criterion number above is printed: the per-row
criteria by Code Cells 2 and 2b, mirrored in E2 and E2b and replayed by E3, and the plane counts, the
35 disagreeing cells and the floors by Code Cell 4's `plane_summary`. Both notebooks were
re-executed. The tasks are closed in `procedure_records/delta_criteria_printing.md`.

### Q6. Does R7's supporting sentence survive the delta criteria? (resolved, R15; investigation closed 2026-09-15)

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
the investigation is closed: Appendix C §8 reports it (T3 of
`procedure_records/delta_criteria_printing.md`, 2026-09-15).

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

### Q7. How to rebuild §5.2's prediction — **CLOSED 2026-09-22** (answered by the user 2026-09-17 as R16; implemented by T0–T13)

**All four choices are now made, and made against printed output.** *What the prediction is stated
on:* E_q over the five cells, the statistic Xiang et al. collect. *Which mechanism:* neither of the
two originally on offer — the section reports that the utility level is required off the endpoint
and not at it (+0.331 of R² on the minimum class, +0.001 on the maximum), and offers no account of
the residual. *How the sharp-prior half is posed:* it is not posed at all; the old prediction is
withdrawn (F13), and what replaces it is the class comparison on the elicited priors. *The
empirical-fit paragraph:* rewritten, with the Leffel et al. (2017) manuscript dropped in favour of
the published article (T5). The remaining "still the user's" below is answered too: §5.2 **is**
stated, the numbers **may** be quoted because Code Cell F prints them, and the five-position
configuration the notebooks lacked is now Appendix F's n = 4.

#### The 2026-09-17 assessment (kept as the record)

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

**2026-09-17, what the new audit answers and what it leaves.** Three of the four choices can now be
made against measurement rather than guessed (the §5.2 entry above, O13):
- *What the prediction is stated on.* The posterior-degree comparison is E_q over the five cells,
  which is the statistic Xiang et al. collect, so a prediction meant to meet their data is stated on
  q. The delta read-out's mode is a separate statement and would have to be made separately.
- *Which mechanism.* Neither of the two on offer. The classes differ in which cut they carry and in
  Λ, and the measured mechanism is that the utility level is required off the endpoint and not at it
  (R² .09 → .40 for the minimum class, .20 → .80 for the relative class, .95 → .95 for the maximum
  class).
- *How the sharp-prior half is posed.* On the elicited priors, not on the labels: the shape
  condition is the sharper one (F12), which reverses the sentence the outline now has.
- *The empirical-fit paragraph.* It needs correcting whatever else is decided, and the corrected
  version has more to say than the current one: the model reaches the same overall fit as the
  models in the paper, on the same items, and fails on the same class.
**Still the user's:** whether the rebuilt §5.2 is stated at all (O13), and whether any of these
numbers may be quoted, which needs a cell to print them (C6) and a five-position configuration the
notebooks do not have.

### Q8. α names two quantities (settled by the user 2026-09-21 → R21)

Background §1.2 fixes α as RSA's speaker optimality, S₁ ∝ exp{α[log L₀ − C(u)]}. `sections_3-6.md`
§4.5, Eq. (36) and Eq. (41) use α for the concentration of the prior Beta(α,1), and Λ_crit ≈ α log 2n
is the law the background now cites as having no RSA counterpart, so the two meet in the one
sentence where a reader compares them. The notebooks use α only in the Beta sense. Options were to rename the Beta concentration
(κ is taken by Appendix C, so it would need a fresh letter) or to subscript RSA's. **The user chose
the subscript, α_rsa** (2026-09-21) = R21. Applied in `background_sections.md` §1.2, where the
gloss now says why the subscript is there, and in §1.3's override-law bullet. The Beta
concentration keeps the bare α everywhere, including both notebooks, which never write RSA's.

## 8. Where the numbers are printed

| Numbers | Source |
|---|---|
| θ\*, q_H, Δ, tempering/utility, conditions per prior; the 5.3e-15 / 0.0575 contrasts | `main.ipynb` Code Cell 2, BASE WORLD PRIOR SWEEP |
| 2.126, 6.5, 26, 34.695, 1205.8, 242,163, −0.5208, 0.4361, 3.98e8, 7.9e6, 4,823 | Code Cell 2b, REALIZABILITY block (step and time figures on `cost:` lines). 4,823 is 4 × 1205.8. **Updated 2026-09-21**: the realizable θ_u is the halted one, not the criterion-stopped 13.3749. |
| 4.547e-13, 12.1, 0.74/0.81/1.82 floors, λ = 2199 | Code Cell 2b, THE ROUNDOFF FLOOR block — the floor per unit of λ_max(H) at three λ, the margin the keyed tolerance holds, and what a fixed 1e-9 would have bought there (decision I3, revised) |
| 1.00, 1.00, 0.04, 1.00 × the stopping tolerance | Code Cell 2, Part A — the specification checks, which compare in multiples of the tolerance rather than against a constant (`TOLERANCE_MARGIN`) |
| Peaks, the cell of *all*, grids 201/401/801 | Code Cell 2, THE DELTA READ-OUT block |
| 33, band, floors, 59 of 121, 0.100–4.250, 2.0–20.1, 3.5e4–3.6e7, D spread | Code Cell 4, `plane_summary`; Text cell 6 |
| 1.9890 / 2.9334 / 4.3102 | Code Cell 4, `override_threshold` |
| 3.19e-2, +0.0008 to +0.0009 | Code Cell 3, `mu_u_probe` |
| 4.45e-09 / 4.46e-09, 4.6e-14, tails 1.7e-3 / 3.3e-6 | Code Cell 2, Part A. **Corrected 2026-09-22**: the first was 9.98e-10 while the stopping tolerance was a fixed 1e-9; I3 now keys it to lambda_max(H), so Part A reports in multiples of a tolerance that moves. |
| 404.8, Eq. (28) table | Text cell 4, *Integration cost and conditioning* |
| F15 (not within 0.1% after 5,000 updates), 145/145 | `procedure_records/theta_u_learned_reach.md` (recorded scripts, not a cell) |
| Exposure-only θ\* (−11.2844, −44.1766, −65.7004, −28.4375) | Code Cell B, ALTERNATIVE SPACES |
| §5.2's re-examination: contributions, leaks, loadings, illustrative θ\* | `audits/2026-09-13-scale-structure/output.txt` (an audit script, not a cell) |
| The scale classes against Xiang et al. (2022): the class profiles by image type, R² by class and pooled for the model and q_lit, the Λ ladder per class and its bracket, the image-type difference, the between-class gaps, the displacement from the elicited prior, and the κ parity at n = 4 | `main.ipynb` **Code Cell F**, `appendix_f_report` (printed since T2/T7, 2026-09-22; **no longer class (e)**). Reads `data/xiang_2022/xiang_items.csv` — the only file either notebook reads (`agent.md` §2 coupling 10). Two absolute classes only: the relative class is not modelled (O14). The superseding audit, `audits/2026-09-17-scale-classes/`, is kept as the derivation and is **not** a source the prose cites; what remains only there — the relative class's fit, the m = 3/m = 4 comparison, the per-image-type Λ — stays class (e) and reaches no prose. |
| Where ℓ₀ enters: the two couplings, the 2BᵀWℓ₀ identity, BᵀW1 and the constant component, the σ-limit table, Part D under both placements at Λ = 8 and 512 | `main.ipynb` **Code Cell D**, *Sec. 5: where ell_0 enters* (printed since U3, 2026-09-17; no longer class (e)). The audit that established them, `audits/2026-09-17-ell0-placement/`, is kept as the derivation and is not the source the prose cites. |
| Q2's Part D and Λ = 512 rows: the modes, the mode shift in s and in grid steps, the two mode criteria | `main.ipynb` Code Cells 2 and 2b, the mode criteria block |
| Q2's plane counts (67, 59, 13 against 74, 59, 33), the 35 disagreeing cells, the four unmoved modes, the 5.6e-5 gap, and the V under both read-outs | Code Cell 4, `plane_summary` |
| Q6's tilt/width split, the 50 and 67 up/down counts, Eq. (24)'s halving and the limit field | Code Cell C, `utility_split_report`; Appendix C §8 |
| §4.2's n guard: θ_L and θ_u\* per n, ⟨μ_u, Σc⟩, the q shift and P(all∣*some*), the mode step, and the status of all four criteria at every (n, Λ, ℓ_0); the κ separation ladder and its n = 15 peak; the n = 1 refusal | `main.ipynb` **Code Cell A**, `granularity_report` (printed since T14, 2026-09-22; O10's numbers are no longer class (e)). 80 rows: n ∈ {2,3,4,5,10,15,20,50,100,201} × Λ ∈ {8, 512} × all four `BASE_WORLD_PRIORS`. The +1.017e-01 → −7.593e-07 decay and the −9.546e-02 contrast the prose uses are rows of this table. |

(2026-09-15: R14's and R15's code and prose tasks, T1-T3, T6 and T7 of
`procedure_records/delta_criteria_printing.md`, are closed.)

## 9. Other stale pointers found

- `agent.md` §1 named the Desktop outlines. **Fixed 2026-09-13**: it now names `thesis_outline/`
  and lists the Desktop drafts as not maintained.
- `composition guide.md` line 3 names `sections_3-5_outline.md` and `background_sections_outline.md`.
- `decisions.md` B2 (line 275), O3 (line 456) and E4 (line 659) cite `sections_3-5_outline.md`. A
  dated finding under O3 records the new file and the missing target (item 2).
