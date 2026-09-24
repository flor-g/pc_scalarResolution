# The outline's organization, and what belongs in the notebook (opened 2026-09-24)

Working record under `agent/agent.md` §5.3. Fold into `agent/history.md` when it closes. IDs carry
the prefix **OR** (organization review) so they do not collide with `thesis_outline/revisions.md`'s
series or with decisions' O entries. **Nothing is applied yet**: this record is the review; the
tasks in §5 wait for the user.

## 1. The user's instruction

> Now review the entire outline and inspect the organization of content. Determine:
>
> 1. if any organization should be improved
> 2. if any content should be in the notebook instead following the rule that rationale and
>    discussions belong to the dissertation while technicality belongs to the notebook.
> 3. if any content in the outline already overlap with content in the notwbook. These should be
>    replaced by a pointer to the notebook.

**Scope read as**: `thesis_outline/sections_3-6.md` and `thesis_outline/background_sections.md`.
`thesis_outline/revisions.md` is the revision log, not the outline, and is where bookkeeping moved
out of the two files would go.

## 2. The line between "result" and "technicality" (OR-D1, confirmed by the user 2026-09-24)

A dissertation's §4 must report results, and a pointer cannot replace a number the discussion argues
from. The agent's proposed line, **pending the user**:

- **Stays in the outline:** every rationale and discussion; every number a claim in §§4–6 argues
  from (§4.4's table; the 33 and 13; the 15 and 9; one ladder figure per guard); the drafting
  guards a writer needs ("never write …").
- **Becomes a pointer:** derivations; verification and precision figures (1.8e-15, 3.6e-15,
  7.4e-13, slope ratios); enumerations the argument does not use item by item (floor lists, the V's
  list, peak lists); and notes about how a count was computed.
- **Moves out to `revisions.md`:** provenance and history (raise chains, supersession notes, closed
  open items, ticked checklists).

Every finding in §§3–4 below is classed on this line. If the user draws it elsewhere, §4's list
shrinks or grows but its entries stay valid.

## 3. Findings: organization (question 1)

- **OR1. The header is stale.** `sections_3-6.md` line 4 says "approximately **5,600 words**"
  (the table sums to 6,310) and lists Appendices A–D, omitting F, which §5.2 is written against.
- **OR2. Bookkeeping sits inside both outlines.** In `sections_3-6.md`: the word-allocation raise
  chain and its "does not reconcile" note (lines ~139–157), "What this table does not do" (~186),
  "Open items" (all four closed, ~1538), and "Sources for §5.2" (a note on where §5.1's citations
  went, misnamed). In `background_sections.md`: the header's revision history, the raise history
  in "Target length", the thirteen-item drafting checklist (all ticked, with audit evidence), and
  the reference list's verification log. **Proposal:** move all of it to `revisions.md`; keep the
  table, the targets and the reference entries.
- **OR3. Provenance runs through the prose instructions.** Tags like "(R2)", "(PP10)", "since
  2026-09-23", "supersedes the 2026-09-23 ruling", "the agent's addition to R19" appear mid-bullet
  throughout. **Proposal:** keep a decision ID only where a writer must honour a ruling; move
  histories to `revisions.md`; set writer's notes in one consistent form (*(Writer's note: …)*),
  which the file already half-uses.
- **OR4. §5.1 contradicts its own ordering instruction.** Its frame says **the complexity saving
  leads** and the conjecture is second, but the body puts the P-8 floors bullet, the five-move
  conjecture and its four-move weighting **before** "The design: resolution as a negative search".
  **Proposal:** frame → the design and its savings (the specification, first motivation) → what the
  criteria add (floors, conjecture, its weight) → what is not derived → the gain and the standing
  qualification. Optionally split the criteria reading into its own subsection. Word count
  unchanged.
- **OR5. §5.5 is overloaded and unsorted** (745 words, thirteen bullets mixing four kinds of
  limit). **Proposal:** group it under four run-in heads — *the numerical substrate* (Z, K, the
  (K, Z)(n) proposal); *the architecture* (linear-Gaussian, the relay, m = 2, not learned);
  *stipulations* (uniform exposure, the inventory, Tier B); *open* (the read-out's locality). Two
  bullets duplicate other sections and shrink to a line each (OR7).
- **OR6. The scope decision's Tier C no longer describes the outline.** Tier C says grid refinement
  and the μ_u/ℓ₀ common-mode invariance are "left in the notebook and cited", but §4.2 quotes the
  invariance's measured instance and §§4.3, 5.5 carry grid refinement at length. Resolved either by
  the pointers of OR-P7, OR-P9 and OR-P15, or by moving those items to Tier A. The agent recommends
  the pointers.
- **OR7. The same content is stated in several sections of the outline.**
  1. The constructive claim's numbers appear three times (Central claim, §§4.4–4.5, §6 item 3), and
     the Central claim also carries the Z-ladder figures (32, 15, 0, 0, 0 / 22, 9, 0, 0, 0). Keep
     the numbers in §4.5 and the claim in words, with "(§4.5)", in the other two.
  2. How Z reaches the verdict (B orthonormalized under the grid's measure; the peak moves; the
     mode position criterion moves by definition) is explained in both §4.2 and §5.5. Keep the
     guard in §4.2 and the mechanism in §5.5.
  3. Halting by tolerance is argued in §5.3 and again in a §5.5 bullet. §5.5 keeps one line and a
     pointer.
  4. §4.6's numbers (2.126, 26, 4,823, 7.9e6) reappear in §5.3. §5.3 cites §4.6.
  5. Commitment 7 and the relay's ordering τ_r ≤ τ_ε (F26) are stated in §3.4, §5.5, and
     background §§2.1, 2.4, 2.6 and 2.7. State the ordering once in background §2.6 and once in
     §3.4; the rest point.
  6. The override law appears in background §1.3, §4.5 and §5.6, and the Cremers parallel's counts
     in background §1.3 and §4.4 (see OR8).
- **OR8. The background quotes measured counts, against its own rule.** Background §1.3 Beat 3
  gives the anti-exhaustive direction's counts ("under all four priors that have a row at the
  weaker lexical strength, and under two of five at the stronger …"), while §2.2 closes on
  "nothing measured enters the background (BG7)". **Proposal:** the forward pointer names the
  parallel and sends the counts to §4.4.

## 4. Findings: content (questions 2 and 3)

Checked against the notebooks' markdown on 2026-09-24. "In the notebook" means the passage or its
numbers are already stated there. "Not in the notebook" means the technical content lives only in
the outline.

### Technical content not yet in a notebook (question 2)

- **OR-N1. §5.1's cascade derivation.** Substituting χ_D for **1** in Eq. (C1), so that a
  complementary pair within a domain costs no dimension at any cascade depth, is a derivation,
  and no notebook carries it (no "χ_D" or "cascade" in any markdown cell). **Proposal:** a short
  section of Appendix C states and proves it; §5.1 keeps the claim ("a binary cascade needs m = 1
  at every level, so it is local without the relay") and points there.
- **OR-N2. §5.5's claim that the Z dependence sits below the criterion.** "A projection taken in
  L²([−Z, Z]) … only a projection under a fixed reference measure would [remove it], and that
  breaks the BᵀWB = I that Eq. (B2) assumes" is a technical claim that no notebook states
  (Text cell 3 §1 has the L² fact, not the consequence). **Proposal:** a sentence in Appendix A's
  half-width paragraph or in Text cell 3 §1; §5.5 keeps "reformulating the criterion cannot remove
  it" and points.
- Nothing else found. The rest of §5.1's design argument (log-odds absorbing the normalization,
  the anchoring proviso) is rationale, and its technical conditions already point to Text cell 3
  §8.6.

### Content already in a notebook, to become a pointer (question 3)

| ID | Outline site | Already in | Keep in the outline |
|---|---|---|---|
| OR-P1 | §3.2, the grid's two parameters | Text cell 3 §1 | one sentence: K discretizes, Z bounds |
| OR-P2 | §3.2, R18 reason 2's formula (σ_L − σ_S)ℓ₀/S; Eq. D7's 2BᵀWℓ₀ | Appendix D §5 | the three reasons in words |
| OR-P3 | §3.3, the projection warning's exact form (BᵀW**1** = 0; Eq. 15 carries the constant) | Appendix D §5 | the parallel and the warning in words |
| OR-P4 | §3.4, the four convergence results; the stiffness ratio 404.8 and the 810.69 writer's note | Text cell 3 §8.2; Text cell 4, *Integration cost and conditioning* | "four results kept apart"; "conditioning decides what is reachable" |
| OR-P5 | §3.4, the relay's mechanics (Eqs. E1, E4, E4a, E6; F26; O6) | `appendix_E.ipynb` E.1 | the sum relocated, not removed; the cost is an ordering |
| OR-P6 | §3.5, the parity derivation's steps | Appendix C §5 | the rationale for m = 2 and the scoped necessity |
| OR-P7 | §4.2, the invariance instance (3.6e-15 over sixty settings; a fifth of Δ) | Text cell 5 | the guard in words |
| OR-P8 | §4.2, the Z ladder's peak list and the two cautions (brackets; decayed sign flips) | Appendix A (half-width paragraphs) | the guard and one figure |
| OR-P9 | §4.3, the check-by-check figures | Code Cell 2's check table | "reported as a table"; the K/Z pair; the K warning |
| OR-P10 | §4.4, the diffuse priors' peak lists; the 8-rows/5-priors note; "exact to 1.8e-15" | Text cells 4 and 4b | the table, the conjunction counts, the delta-like row |
| OR-P11 | §4.5, the floor enumerations, the V's list, the override slopes and ratios, the spread D, the least-θ_u ranges | Text cell 6 | the floors' directions and crossing, the band, 33 / 13 / 15 / 9, the Z caveat |
| OR-P12 | §4.6, the integration numbers | Text cells 4 and 4b | the three facts §5.3 uses, once (OR7.4) |
| OR-P13 | §5.1, θ_u\* by inventory (−11.28, −44.18, −65.70, −28.44) | Appendix B | "depends substantially on the inventory" |
| OR-P14 | §5.2, the Eq. (F3) derivation and both "(Note for the notebook …)" asides (medians; the midpoint node's 0.0194) | Appendix F | the sign result in words; **delete the two notes**, since the notebook already has them |
| OR-P15 | §5.5, the K bullet's finer- and coarse-end numbers | Appendix A, *A third axis* | the suspected bound, what the evidence allows, the directions, the (K, Z)(n) proposal |
| OR-P16 | §5.5, the read-out bullet's "Sourced (C6)" counts | Appendix A, *Finding the peak* | the nuances and the candidate stipulation |
| OR-P17 | §5.6, θ_u\* set by 3𝔼_{p(y)}[c_y] | Appendix B | the prediction |

The background (`background_sections.md`) has no technical overlap beyond OR7.5 and OR8. Its
content is rationale and literature, as the rule wants.

## 5. Proposed tasks (not started; wait for the user)

- [ ] **OR0.** Checkpoint.
- [x] **OR-D1.** Confirmed by the user 2026-09-24 ("Your decisions are confirmed"), with the proposals of §§3–4.
- [ ] **OR-A. Housekeeping** (OR1, OR2, OR3): header, bookkeeping moved to `revisions.md`, one
  form for writer's notes. No content change.
- [ ] **OR-B. Notebook first** (OR-N1, OR-N2): Appendix C and Appendix A (or Text cell 3 §1) gain
  the two technical passages; no code changes, so no re-execution is needed. Code before prose does
  not bind here, since neither passage quotes a number, but each is checked against the equations it
  cites.
- [ ] **OR-C. Pointers** (OR-P1 to P17), section by section, keeping what the table's right column
  names.
- [ ] **OR-D. Restructure** (OR4 §5.1 order; OR5 §5.5 grouping; OR6 Tier C; OR7 de-duplication;
  OR8 background §1.3).
- [ ] **OR-E. Word budget.** Pointers shorten the outline, not the dissertation's budget, unless a
  budget line was paying for the moved detail; re-sum where it was.
- [ ] **OR-F. Close**: dangling references, C6 sweep, `revisions.md` §16, fold.

## 6. Findings log

(empty)
