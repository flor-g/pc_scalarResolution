# Λ against ℓ₀: the counterforce, and where ℓ₀ enters

Working record for the change to §§3 and 4 (and background §§1.2–1.3) that the user opened on
2026-09-17, before T0–T13 of `scale_classes_hypothesis.md`. Pattern: `agent.md` §5.3.

**Task IDs in this record are `U0`–`U14`.** `scale_classes_hypothesis.md` uses `T0`–`T13` and both
lists are live; the prefixes keep them apart. **Status: nothing started.** The user's "do not start
the edits and implementations yet" from the §5.2 instruction has not been lifted, and P-1 to P-7
below are unanswered.

**Checkpoint.** Tree clean at `b548e0a` as this list is written.

---

## 1. The user's instruction, verbatim (2026-09-17)

> Before we do T0-T13, we need to clear something else first. Recall that we have made new changes
> to the evaluation since we last edited sections 3 and 4. The new important take-away is this:
> under a strong Lambda, the shift criterion is more robustly met for different priors; this is
> thanks to the mechanism that Lambda and ell_0 are so to speak couterforces to each other. This is
> a commitment that the model makes. We would want to inform the reader more about what this
> commitment concerns:
>
> 1. does this commitment have any parallel in RSA architecures?
> 2. logically speaking, is g_L the only place where ell_0 could enter the model? Of course not! We
> could have placed ell_0 at g_s instead. That would not have allowed ell_0 and Lambda to counteract
> as directly. However, we have made a commitment (that is, a choice not forced by construction) to
> place ell_0 at g_L for serveral different reasons that the reader should be aware of: (a) it would
> have been messy node wise to put ell_0 at g_S, and the architecture would not have been as clean.
> (b) philosophically speaking, it is intuitive to hypothesize that the world prior and lexical
> strength have counteractive dynamics.

Then, after the report below: *"write it up as tasks."*

---

## 2. What is already on record

- **`decisions.md` A3** — *ℓ₀ sits in g_L: g_L(φ_S) = ℓ₀ − φ_S*. **Settled**, decided by the user
  (2026-09-06), against g_S by name. One theoretical reason recorded (the order-reversing affine
  involution), implementational reason "none recorded". So the alternative the user names is the
  model's own earlier form, not a hypothetical. `code cell 1`'s `closed_form_fixed_point` and
  `predict_state` still carry the changelog wording ("coupled to the sum ell_0 + phi_L before"),
  which `decisions.md` **E9** lists as reader-facing hygiene to remove.
- **`decisions.md` D3** — Bogacz status of the placement: instance under restriction.
- **Appendix D §3, last paragraph** — already argues ℓ₀'s place in g_L from where the involution's
  fixed point sits (φ_S = ℓ₀/2, the field the model settles on at φ_L = 0, θ_u = 0). This is the
  closest existing prose to the commitment, and it is one paragraph inside an appendix about a
  *different* question (exclusion against truth sets).
- **`revisions.md` §2, dated 2026-09-15** — "Rebuilding those arguments on the Λ = 512 data is
  open." §§4.4, 4.5 and 6 rest on the Λ = 8 table. The user's take-away is that rebuild's headline.
- **`revisions.md` §4, §4.4 entry** — written 2026-09-13 against the Λ = 8 table. **That entry is
  itself stale** and is corrected by U10 below, not only the outline it describes.
- **`background_sections.md` §1.3 Beat 2** — already states the inverted parallel: wRSA makes *the
  prior* defeasible against the utterance, this architecture makes *the lexical entry* defeasible
  against the prior. The RSA answer extends this beat; it does not open a new one.
- **`background_sections.md` §1.2** — fixes the RSA notation the answer to question 1 uses
  (L₀ ∝ ⟦u⟧(s)P(s); S₁ ∝ exp{α[log L₀ − C]}; L₁ ∝ S₁P(s)).

**What is *not* on record:** either of the user's two reasons; the third reason found below; the
evaluation-side consequence; the RSA parallel; and any statement anywhere that the placement was a
choice at all.

---

## 3. What was measured

- **Script:** `audits/2026-09-17-ell0-placement/ell0_placement.py`, output `output.txt` beside it,
  commit `b548e0a`. Run from the project folder with `.venv/bin/python`. It execs `code cell 1` and
  Code Cell 2's definitions verbatim; Code Cell 2's RUN block is not executed. No project code was
  changed and variant B is implemented as local closed forms, never as a method on the class.
- **Variant A** (the model, A3): g_L(φ_S) = ℓ₀ − φ_S, g_S(φ_u) = θ_u Bφ_u.
- **Variant B** (the alternative): g_L(φ_S) = −φ_S, g_S(φ_u) = ℓ₀ + θ_u Bφ_u.
- Everything else held: same 𝓕 (Eq. 13), same chain, same B, same μ_u, same σ, same read-out
  (Eq. 12), same exclusion convention (Eq. 5), same Λ.
- **Self-checks.** θ\* = −28.43749 recovered for the default inventory both from the network's own
  `learned_theta_u` and from the record's re-derivation of Eq. (B2); BᵀWB − I is 2.2e-16; and
  θ\*^B is the argmax of variant B's own 𝓕 on a ±50 % scan of 201 points under every prior at both
  Λ (block 8).

### Variant B in closed form, for the record

    r_L = φ_L + φ_S,   r_S = φ_S − ℓ₀ − θ_u Bφ_u,   r_u = φ_u − μ_u

    ∂𝓕/∂φ_S = 0  →  φ_S* = [σ_L(ℓ₀ + θ_u Bφ_u) − σ_S φ_L] / S
    ∂𝓕/∂φ_u = 0  →  (I + σ_u θ² G / S) φ_u* = μ_u + σ_u θ c_B / S,   c_B = −BᵀW(ℓ₀ + φ_L)

with S = σ_L + σ_S, G = BᵀWB. Against Eqs. (15)–(16), only the coupling and the σ-weighting of ℓ₀
differ.

---

## 4. Findings

- **G1. The placement changes exactly one quantity: the utility level's drive.**
  c_y = BᵀW(ℓ₀ − φ_L) under A, and −BᵀW(ℓ₀ + φ_L) under B. Measured as identities over the three
  entries: `c^A − c^B − 2BᵀWℓ₀` is at most 2.8e-14 and `c^A + c^B + 2BᵀWφ_L` at most 1.1e-14. So
  **the entry enters both placements the same way and the whole difference is the sign the prior
  carries against it**, and that difference is 2BᵀWℓ₀ = (−0.0, −37.1992) at the default settings,
  independent of the utterance.

- **G2. It is not a difference in the belief formula.** At σ_L = σ_S the two give the same φ_S given
  φ_u, to 1.8e-15. What differs is φ_u\* itself (by 12.3997 at θ_u = 1), and through it φ_S\* (by
  3.9996). The user's "not as directly" is the accurate phrasing: ℓ₀ and Λχ_y still oppose each
  other inside φ_S\* under B.

- **G3. Reason (a), made exact.** Under A the opposition is one error unit's activity:
  ε_L = φ_L − ℓ₀ + φ_S computes the difference at a node. Under B, ε_L computes φ_L + φ_S and ε_S
  computes φ_S − ℓ₀ − θ_u Bφ_u; ℓ₀ − φ_L is never any unit's activity and exists only as a
  combination of two residuals. The counterforce is a fact about a node under A and a fact about the
  algebra under B.

- **G4. A third reason, not on record anywhere and stronger than either of the user's.** Under A the
  literal listener is a fixed point of the network: φ_S\* → ℓ₀ − φ_L as σ_S → ∞ (agreement 2.7e-5
  at σ_S = 1e6). **Under B no σ produces it.** σ_S → ∞ gives −φ_L (the entry, prior discarded);
  σ_L → ∞ gives ℓ₀ + θ_u Bφ_u (the prior, entry discarded); ℓ₀ − φ_L is unreachable. §4.1's
  sentence — that q_lit "is a fixed point of this network rather than an external construction",
  which "removes the obvious objection that the baseline was built to be beaten" — is available
  only under A, and the outline states it without knowing it depends on A3.

- **G5. Reason (b) has empirical content.** The two placements are distinguishable as soon as
  σ_L ≠ σ_S: the φ_S difference at a shared φ_u is exactly (σ_L − σ_S)ℓ₀/S. At σ_L = 2, σ_S = 1 the
  measured max is 6.3063 against a predicted 6.3063. Under A the prior travels with the lexical
  channel's precision, under B with the utility channel's, so a later precision-bearing phase
  (Text cell 3 §5: the log σ terms are "carried only to mark where a later precision-bearing version
  would reintroduce them") tests the placement instead of inheriting it.

- **G6. The take-away is placement-dependent.** Shift for *some*, both variants scored against the
  same literal listener ℓ₀ − φ_L, which B cannot itself produce (G4):

  | prior | Λ=8, A | Λ=8, B | Λ=512, A | Λ=512, B |
  |---|---:|---:|---:|---:|
  | Gaussian | +0.0008 | +0.3815 | +0.0071 | +0.0587 |
  | flat | +0.0295 | +0.3159 | **−0.0146** | +0.0071 |
  | Beta(1,3) | +0.0004 | +0.3405 | +0.0089 | +0.0546 |
  | Beta(3,1) | +0.0421 | +0.2016 | **−0.0955** | **−0.0820** |
  | delta-like | +0.0030 | **−0.5067** | **−0.5217** | **−0.9494** |

  At Λ = 512 the conjunction holds under **3 of 5** priors under A (flat, Beta(3,1), delta-like) and
  **2 of 5** under B. The sharper contrast is at Λ = 8, where the anti-exhaustive shift is two to
  three orders of magnitude larger under B (+0.3405 against +0.0004 on Beta(1,3)): the direction
  §4.4 names, and background §1.3 Beat 3 ties to Cremers et al. (2023), is one the model's placement
  suppresses before Λ is raised at all. The A columns reproduce Text cell 4b and Part D in every
  printed digit.

- **G7. How Λ reaches the utility level.** |c_y| under the Gaussian prior for *some*: at Λ → 0 the
  two couplings are exact negatives, (0, −18.5996) and (0, +18.5996); as Λ grows both approach
  −Λ BᵀWχ_y, and |c^A| − |c^B| saturates at +19.88. So the placements agree in the entry's leading
  term and differ in the prior's sign against it, at every Λ.

- **G8. The answer to question 1, in four parts.**
  1. **Λ → ∞ *is* RSA's literal listener.** log L₀ = log P(s) + log⟦u⟧(s), and a hard semantics puts
     log⟦u⟧ ∈ {0, −∞}. φ_S = ℓ₀ − Λχ_y is that with −∞ replaced by −Λ. Text cell 3 §3 item 6 already
     says Λ → ∞ recovers a hard truth-conditional constraint; what is not said is that the object at
     that limit is RSA's L₀. This is the tightest parallel and costs one clause.
  2. **The parallel to c_y is S₁'s utility, not any RSA parameter.** S₁ reads log L₀(s|u), the log
     of the literal posterior; the utility level reads BᵀW(ℓ₀ − φ_L), a linear projection of the
     same log quantity. Under B the level above would read ℓ₀ + φ_L, which corresponds to no RSA
     quantity. **But see P-5:** background line 373 explicitly forbids equating the mapping with
     RSA's social recursion, so this part is not free to state.
  3. **Finite Λ has no single RSA counterpart.** RSA lets prior and semantics trade off with a
     latent variable rather than a strength: lexical uncertainty marginalizes over hard lexica
     (Potts et al., 2016, in the background bibliography); threshold uncertainty infers the cut
     jointly with the state (Lassiter & Goodman — hence Xiang et al.'s LG model, so this touches
     §5.2); wonky worlds (Degen, Tessler & Goodman, 2015) makes *the prior* defeasible instead,
     which is the inversion §1.3 Beat 2 already states. The nearest strength parameter is α, which
     sharpens informativity, not the lexicon. **Nothing in RSA plays the role of Eq. (41)'s
     Λ_crit ≈ α log 2n**, the quantified exchange rate — that is the part of the commitment with no
     parallel at all.
  4. **The placement question itself has a contrastive parallel.** RSA also has a "where does the
     prior enter" degree of freedom and resolves it the other way: P(s) appears in L₀ *and again* in
     L₁ ∝ S₁(u|s)P(s). In this chain ℓ₀ enters once, and the commitment is which map it enters. One
     sentence, stated as a contrast.

- **G9. Nothing here contradicts a settled decision.** A3 is confirmed, not challenged: every
  finding above is a reason for it. Under `agent.md` §3.1 the reasons and the evidence are added to
  A3 as a dated amendment, and A3 is not reopened.

---

## 5. What must be settled before any code (blocking)

- **P-1. Does the paper report the alternative placement with numbers, or state the commitment
  without them?**
  - (i) *Assert only.* §3.2 gains a bullet; no number is quoted; no cell changes. Cheapest; the
    commitment is then unfalsifiable in the text.
  - (ii) **(recommended)** *The structural facts, printed.* The identity c^A − c^B = 2BᵀWℓ₀, the
    node-level statement (G3) and the σ-limit fact (G4) are stated and printed by **Code Cell D**,
    with the prose in a new Appendix D section. The body quotes at most one number.
  - (iii) *The full counterfactual.* Part D under both placements (G6) as well. This is a second
    evaluation of a model the paper does not hold, and it needs its own appendix.
  Recommendation (ii): Appendix D is already the home of the question "which map carries the
  entry into a field", the placement is its sibling question, and (ii) satisfies C6 without
  spending body words.
- **P-2. Where the commitment sits in the body: §3.2 or §3.3?** §3.2 holds the Λ material ("the
  price of a soft lexicon"), §3.3 holds the chain and g_S. Recommendation: **§3.2**, one bullet,
  because the commitment is about Λ against ℓ₀; §3.3's g_S bullet gets a clause pointing to it.
- **P-3. Word budget.** §3 is at 920 and §4 at 950 after R1/S-6, and background §1.3 at 340. The
  commitment needs roughly 90 words in §3.2, 20 in §3.3, 30 in §4.1, and 50 in background §1.3.
  Raise the budget, or trim, and by how much? The §3 word table in `revisions.md` §3 is **not**
  edited until this is answered.
- **P-4. Which of G8's four parts the paper states.** Parts 1, 3 and 4 are safe. Part 2 is P-5.
- **P-5. Is the c_y ↔ log L₀ parallel (G8.2) stated at all?** It is the sharpest parallel and it
  invites exactly the reading `background_sections.md` line 373 tells the writer to block ("do not
  equate this mapping with RSA's social recursion"). Options: state it with that qualification
  attached; state it only in Appendix D, away from the background's framing; or drop it.
  **This one is genuinely the user's call.**
- **P-6. The Λ = 512 headline.** Rebuilding §§4.4–4.5 moves the verdict from "the conjunction holds
  under none" (outline) / "under one" (`revisions.md` §2) to **"under three of five"**. Under
  `agent.md` §5.4 a headline result changing is a stop-and-ask. §5.1, §6 and the background's
  forward pointers lean on the old count. Confirm the new headline sentence before any prose moves.
- **P-7. How A3 is updated.** Recommendation: a dated amendment in place — the user's reasons (a)
  and (b), the third reason G4, the evidence pointer, and an expanded "Depends on it" naming Eq.
  (16)'s c_y, §4.1's baseline sentence and the Λ = 512 result. Not a new entry, and not a reopening
  (G9). Agent decision, pending the user.

---

## 6. Tasks, in order

Code before prose (`agent.md` §5.3). Nothing below starts until P-1 to P-7 are answered.

- [ ] **U0. Checkpoint.** `git status` clean, record `git rev-parse --short HEAD`. Clean at
      `b548e0a` as this list is written.
- [ ] **U1. Settle P-1 to P-7 with the user.** Record each answer here verbatim, as §8 of
      `scale_classes_hypothesis.md` does.
- [ ] **U2. `decisions.md`.** Amend **A3** per P-7: the two user reasons dated 2026-09-17, the third
      reason (G4), the evidence line pointing at `audits/2026-09-17-ell0-placement/`, and the
      widened "Depends on it". Add a dated finding under **B1/B2** if P-6 changes the criterion's
      reported scope. Register-E entries for every quantity a cell newly prints (U3), each classed
      under `agent.md` §3.3 — note that variant B's fields are a **counterfactual manipulation
      (C8)**, not a control, since no setting of the model produces them, and C8's wording must be
      used in both the cell's labels and the prose.
- [ ] **U3. Code Cell D** (only if P-1 is (ii) or (iii)). Append a block printing: the two couplings
      per utterance; the two identities of G1 with their residuals; the σ-limit table of G4; and, if
      (iii), G6's table. Constraints: **every helper local to the cell** — `code cell 1` is not
      touched, so coupling 9 stays quiet and variant B never becomes a method on the class; no
      figure, so the 8-figure baseline holds; any wall-clock line behind `cost:` (coupling 3);
      labels say "counterfactual manipulation", never "control". Acceptance: every number the new
      prose quotes is printed here, and no number in the new prose is absent from it.
- [ ] **U4. Appendix D prose.** A new section — "Where ℓ₀ enters" — covering: the logical space
      (g_L, g_S, or a bias belonging to no g and therefore to no error unit; μ_u and g_y are ruled
      out by rank and by the clamp); variant B's closed form; G1, G3, G4, G5. New numbered displays
      continue the appendix's own sequence as **D5, D6, …**, so the body's (1)–(41) is untouched and
      coupling 5 does not fire. Also update Appendix D §4's closing sentence, which currently says
      the appendix settles the E–T asymmetry and nothing else.
- [ ] **U5. Anchors and ToC.** A new Appendix D heading needs an inline anchor (`appd-5`) and a ToC
      row (coupling 6). Regenerate cell 0; do not hand-edit it.
- [ ] **U6. Couplings.** Confirm none fires: E3 replays Code Cells 2 and 2b only, so a new printing
      call in Code Cell D is outside its list (couplings 1, 2, 7); `code cell 1` untouched, so
      coupling 9 is quiet; no new figure. Check whether `appendix_E.ipynb` §E.3 ("claims in main
      restated") needs a line for the commitment.
- [ ] **U7. Execute** main, then appendix_E (`agent.md` §5.1). Acceptance: main 0 errors, 8 figures,
      14/14; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS on both cells. Diff every other
      cell's stored output against U0: only Code Cell D may differ.
- [ ] **U8. `agent.md`.** Cell count is unchanged if U3 appends to Code Cell D rather than adding a
      cell; update §5.1's baseline only if the runtime moves materially. If U3 is skipped (P-1 = (i))
      this task is empty.
- [ ] **U9. §3 prose.** §3.2 gains the commitment bullet (P-2) and, per P-4, the clause naming
      Λ → ∞ as RSA's literal listener; §3.3's g_S bullet gains the pointer. Both written against
      U7's output.
- [ ] **U10. §4.4 and §4.5, rebuilt on Λ = 512.** The larger prose job, and it subsumes
      `revisions.md` §2's open note of 2026-09-15. Sources: Text cell 4b and Code Cell 2b, already
      executed — **no new code is needed for this task**. It must also correct the §4.4 entry in
      `revisions.md` §4, which was written against the Λ = 8 table and is itself stale. §4.1 gains
      the sentence recording that q_lit's status as a fixed point depends on A3 (G4).
- [ ] **U11. Background §1.3 Beat 2**, extended with the RSA parallel per P-4/P-5, and §1.2 if
      G8.4's contrast (P(s) in both L₀ and L₁) is stated there instead. Note `background_sections.md`
      line numbers run one lower than `revisions.md` cites, after R8.
- [ ] **U12. Anything leaning on the old headline.** §5.1, §6 and the background's forward pointers
      that say the conjunction holds under none or one prior. Blocked on P-6.
- [ ] **U13. `revisions.md`.** R18–R20 rows once P-1 to P-7 are answered; the §3 word table per
      P-3; close the 2026-09-15 note in §2; a §8 source row for the placement numbers; and mark the
      §4.4 entry corrected by U10.
- [ ] **U14. Commit**, one logical change per commit, hashes recorded on each task line above.

---

## 7. Prose sites, to be written only after U3 and U7

- `main.ipynb` Appendix D (cell 20), new section; Code Cell D (cell 21); cell 0 ToC.
- `sections_3-6.md` §3.2 (lines 124–141) and §3.3's g_S bullet (lines 155–165).
- `sections_3-6.md` §4.1 (lines 218–232): the dependency of q_lit's status on A3.
- `sections_3-6.md` §4.4 (lines 265–297) and §4.5 (lines 298–317): the Λ = 512 rebuild.
- `sections_3-6.md` §3's word table (lines 81–103) and the scope tiers (lines 41–77).
- `background_sections.md` §1.2 and §1.3 Beat 2.
- Whatever U12 turns up in §5.1, §6 and the background's forward pointers.
