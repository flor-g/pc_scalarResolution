# Λ against ℓ₀: the counterforce, and where ℓ₀ enters

Working record for the change to §§3 and 4 (and background §§1.2–1.3) that the user opened on
2026-09-17, before T0–T13 of `scale_classes_hypothesis.md`. Pattern: `agent.md` §5.3.

**Task IDs in this record are `U0`–`U14`.** `scale_classes_hypothesis.md` uses `T0`–`T13` and both
lists are live; the prefixes keep them apart.

**Status, 2026-09-21: P-1 to P-10 are answered (§11), and U0–U14 are closed, so this change is
finished.** Q8, raised in U11, was settled by the user on 2026-09-21 (RSA's parameter is α_rsa,
`revisions.md` R21). Next: T0–T13 of `procedure_records/scale_classes_hypothesis.md`.

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

Code before prose (`agent.md` §5.3). P-1 to P-10 are answered (§11), so U3 onward are unblocked.

- [x] **U0. Checkpoint** (2026-09-17). Clean at `b548e0a` when the list was written; clean again at
      `90a9352` before U2.
- [x] **U1. Settle the blocking decisions** (2026-09-17). P-4 and P-5 in §8, P-1, P-2, P-3, P-7,
      P-8, P-9, P-10 in §11, each verbatim. Commit `1c473d8`, `90a9352`.
- [x] **U2. `decisions.md`** (2026-09-17, P-7 = amend). **A3 amended:** the two user reasons dated 2026-09-17, the third
      reason (G4), the evidence line pointing at `audits/2026-09-17-ell0-placement/`, and the
      widened "Depends on it". Add a dated finding under **B1/B2** if P-6 changes the criterion's
      reported scope. Register-E entries for every quantity a cell newly prints (U3), each classed
      under `agent.md` §3.3 — note that variant B's fields are a **counterfactual manipulation
      (C8)**, not a control, since no setting of the model produces them, and C8's wording must be
      used in both the cell's labels and the prose.
- [x] **U3. Code Cell D** (2026-09-17, P-1 = printed by Code Cell D). Appended
      `UtilityPlacementNetwork`, three helpers and `ell0_placement_report`, printing five blocks
      under the heading *Sec. 5: where ell_0 enters*, plus self-checks. Commit `23bdf23`.
      - **Built from 𝓕, not asserted.** The alternative is a subclass overriding `predict_lexical`
        and `predict_state` only, exactly as `TruthSetNetwork` already does in this cell, and it is
        solved by the cell's own `settle_by_newton` on Eq. (13). Its closed form agrees with Newton
        to **3.6e-15**, and its θ\* is **+22.57787** both in closed form and by the cell's
        `learned_by_bisection` on Eq. (20).
      - **Eq. (B2) over given couplings.** `theta_u_stationary_points` builds c_y inline, so a
        local `theta_star_over_couplings` takes c_y as an argument. Fed the model's own couplings it
        returns **−28.43749**, the parent's value, and that check prints before it is used.
      - **What it prints.** (1) the two couplings per entry and the identities c(g_L) − c(g_S) =
        2BᵀWℓ₀ to 2.8e-14 and c(g_L) + c(g_S) = −2BᵀWφ_L to 1.1e-14; (2) **R19's warning** —
        BᵀW1 = (+9.4e-17, −2.6e-17), the constant component ⟨1, ℓ₀ − φ_L⟩_W per entry
        (−154.5617, −107.5217, −154.5617, so it is **not the same for every entry**), and c_y
        unchanged to 1.4e-14 by adding 3.7·1; (3) the σ-limit table; (4) the same-φ_u agreement and
        the (σ_L − σ_S)ℓ₀/S difference; (5) Part D's five priors under both placements at Λ = 8 and
        Λ = 512, scored by the cell's own `criterion_for_some`.
      - **Constraints met.** Every helper is local to Code Cell D; `code cell 1` is untouched, so
        coupling 9 is quiet; no figure, so the 8-figure baseline holds; no wall-clock is printed, so
        coupling 3 does not arise. Every label says *counterfactual manipulation*, never *control*,
        and the two θ_u = 1 rows say "a control" as B4 requires.
      - **A dependency to record in U6/U8:** the block reads `part_d_priors` (Code Cell 2) and
        `STRONG_LAMBDA`, `DELTA_ALL_ALPHA` (Code Cell 2b). Renaming any of them raises `NameError`
        in Code Cell D — loud, not silent, so it is not a coupling of the §2 kind, but it is a new
        cross-cell dependency and belongs in the record.
      - **Verification.** `main.ipynb` re-executed: **0 errors, 8 figures, 14/14, 246 s**. Against
        the checkpoint only two cells differ — Code Cell D (source and output) and Code Cell 2b,
        whose only changed lines are `cost:` wall-clock. Appendix D §§1 and 3 reproduce every stored
        number exactly (θ_u\* −28.43749 under both conventions, Eq. (D3)'s +4.000000, the field
        norms, Eq. (D4)). `appendix_E.ipynb` is **not** re-executed here; that is U7.
- [x] **U4. Appendix D prose** (2026-09-17). New **Sec. 5, "Where ℓ₀ enters"**, with displays
      **(D5)–(D7)**; the body's (1)–(41) is untouched and coupling 5 does not fire. Commit `ccaccd4`.
      - **Content, kept to what the notebook can say and the paper cannot.** The logical space in
        three clauses (a bias belonging to no g is not a prediction and so has no error unit; μ_u is
        in ℝ^m; g_y is out while φ_L is clamped); Eq. (D5)'s Bogacz status, which is Eq. (9)'s, so
        one register entry covers both; Eq. (D6), the alternative's stationary point; Eq. (D7), the
        two coupling identities; then four short paragraphs — the one quantity that differs, what
        Eq. (9) makes available, what the coupling does not carry, and Part D under both. **The
        commitment framing and the reasons are not argued here; they are §3.2's.** Part D's rows are
        noted with our position reserved (composition guide Entry 3b), as Text cell 4b does.
      - **Sec. 4 rewritten** to close Secs. 1–3 and point forward to Sec. 5, instead of reading as
        the appendix's own close. Its "assymetry" typo is corrected in the same sentence.
      - **Appendix retitled**, "why emission is exclusion" → "why emission is exclusion, and where
        ℓ₀ enters", since the appendix now answers two questions about the same map. **Agent
        decision, named to the user.** Text cell 3's two references to Appendix D stay accurate (one
        already says it derives "ℓ₀'s place here"); cell 0's ToC row still reads "(D1)–(D4)" and
        carries the old title, which **U5** fixes.
      - **One number was quoted before it was printed**, and Code Cell D was corrected rather than
        the prose: block (4) printed the same-φ_u agreement as `0.0000`, so it now prints four
        significant figures (`1.776e-15`, and `6.306` against a predicted `6.306`). Every number
        Sec. 5 quotes is now in Code Cell D's output — checked one by one.
      - **Verification.** `main.ipynb` re-executed: **0 errors, 8 figures, 14/14, 250 s**. Against
        U3's commit, cells 20 (markdown) and 21 differ, and Code Cell 2b's output differs in 12
        lines, every one of them a `cost:` line.
- [x] **U5. Anchors and ToC** (2026-09-18). Commit `4b0eb71`. The `appd-5` anchor was already inline
      in the heading from U4 (coupling 6). Cell 0's Appendix D rows were **derived from cell 20's own
      headings and `\tag{}`s** rather than typed, so the titles and equation ranges cannot drift from
      the appendix: the header row now carries the new title and **(D1)–(D7)**, row 4 the rewritten
      heading, and a new row 5 `(D5)–(D7)`. Only those three lines of cell 0 change. **All 74 ToC
      links resolve** to an inline anchor. `appendix_E.ipynb` names Appendix D once, in a list of
      appendices, unaffected by the title. Markdown only: no execution needed, and the stored outputs
      are those U4 verified.
- [x] **U6. Couplings** (2026-09-18). **None fires.** Commit `84e45e8`. Against the checkpoint
      `b548e0a`, only cells 0, 20 and 21 of `main.ipynb` differ in source; the cell count is 23.
      - **1, 2, 7.** Code Cells 2 and 2b are source-identical to the checkpoint, and their headers
        still carry the exact prefixes `# === Code Cell 2:` and `# === Code Cell 2b:`, which are
        the only things E3 locates main's cells by. E3 never reads Code Cell D.
      - **3.** Code Cell D prints no run-dependent line. **5.** The body's tags are still exactly
        (1)–(41); Appendix D's run (D1)–(D7). **6.** Closed in U5. **8.** Code Cell D does not touch
        `sys.stdout`. **9.** `code cell 1` is source-identical to the checkpoint, so E1 needs no
        mirror. Figures 8 → 8.
      - **E.3 needs no line, and that is now measured rather than assumed.** E.3 lists Appendix D
        as *Unaffected* by the relay, a line written before Sec. 5 existed. Running Code Cell D's
        Sec. 5 report on E1's architecture — E1 for `code cell 1`, E2 and E2b's definitions for
        Code Cells 2 and 2b, Eq. (D5) written at the relay as g_S = ℓ₀ + θ_u r — reproduces **all
        61 lines** of main's stored Sec. 5 output, self-checks included. Script and output:
        `audits/2026-09-17-ell0-placement/relay_check.py`, `relay_check_output.txt`.
      - **Two loud dependencies, for U8 to record.** Neither is a coupling of `agent.md` §2's kind,
        because each fails with an exception rather than silently.
        1. *Names.* Code Cell D now reads `part_d_priors` and `criterion_for_some` (Code Cell 2)
           and `STRONG_LAMBDA`, `DELTA_ALL_ALPHA` (Code Cell 2b). Renaming any raises `NameError`.
        2. *A signature.* `UtilityPlacementNetwork.predict_state` overrides main's
           `predict_state(phi_u, theta_u=None)`. E1's version takes a third argument, `relay`, so
           the override **cannot run on E1 as written** — the relay check above had to restate it
           with E1's signature. If `code cell 1` ever gains that argument, Code Cell D raises
           `TypeError`. `TruthSetNetwork` is not exposed the same way: it overrides only
           `predict_lexical`, whose signature the two notebooks share.
- [x] **U7. Execute** (2026-09-18), main then appendix_E, by `agent.md` §5.1. Commit `bf746b1`.
      **Both at baseline, exactly.**
      - `main.ipynb`: **0 errors, 8 figures, 14/14, 249 s.** Every code cell source-identical to U6's
        commit; against its stored outputs the only differing lines are 12 `cost:` lines in Code
        Cell 2b.
      - `appendix_E.ipynb`: **0 errors, 5 figures, E2 18/18, E3 PASS on both cells, 679 s.** Code
        Cell 2: 203 lines identical, 0 deleted, 1 changed (the pass count), 4 inserted (the relay's
        checks). Code Cell 2b: 234 identical, none changed. Against the committed appendix_E, the
        only differing lines are 12 `cost:` lines in E2b.
      - Over the whole change (checkpoint `b548e0a` to here), the only stored output that differs
        in anything but wall-clock is Code Cell D's, which is the one U3 and U4 set out to change.
- [x] **U8. `agent.md`** (2026-09-18). Commit `1320fa1`.
      - **§1 cell map.** The Appendices A–D row now names "where ℓ₀ enters (Sec. 5, Eqs. (D5)–(D7),
        decision A3)". The cell count stays 23 and the Code Cells A–D row stays accurate.
      - **§2, the two loud dependencies from U6**, recorded under a new *Loud dependencies* paragraph
        after coupling 9, explicitly marked as not couplings of §2's kind.
      - **§2 coupling 9 corrected — a pre-existing inaccuracy found while writing the second
        dependency.** It said every `def` in `code cell 1` appears verbatim in E1. Measured: 24 of 30
        do; `__init__`, `predict_state`, `residuals`, `free_energy`, `infer` and `theta_u_gradient`
        carry the relay in E1. The "878 of 912 lines" figure beside it is right (re-measured). The
        correction matters because coupling 9 also instructs mirroring **by lifting the source
        verbatim**, which inside those six would delete E1's relay; the item now says so.
      - **§5.1 unchanged.** 249 s and 679 s against the stated "about 250 s" and "about 710 s", with
        every count identical.
- [x] **U9. §3 prose** (2026-09-18, commit `d667600`). `sections_3-6.md` §§3.2–3.3 only; headings raised to P-3's 270
      and 255. No number is quoted in either section, so C6 does not arise.
      - **§3.2, "The price of a soft lexicon"** now names the Λ → ∞ object as RSA's L₀ (G8.1), and
        defines ℓ₀ in place, since §3.2 is its first use in the outline.
      - **§3.2, a new bullet: the commitment (R18).** The contest between Λ and ℓ₀ is staged at one
        error unit because ℓ₀ sits in g_L; Eq. (D5) is as local and has the same Bogacz status, so
        locality does not decide it (A3). The three reasons, one clause each: (a) cleaner, in G3's
        exact form; (b) the counteraction hypothesis, with G5's empirical content; the agent's
        fixed-point reason (G4), tied to §4.1. It closes on Eq. (D7) and points to §4.4, and calls
        the Eq. (D5) rows a counterfactual manipulation (C8).
      - **§3.3, the g_S bullet** says g_S carries nothing else and ℓ₀ enters at g_L. **A
        pre-existing Entry 5 slip fixed in passing:** the bullet used c_y (Appendix B's condition)
        before anything defined it; it now glosses c_y in place.
      - **§3.3, a new bullet: the projection and its warning (R19)**, in G10's exact form, with the
        coupling/model nuance. Two calibrations under composition-guide Entry 2: the utility level's
        drive is described as each utility unit's own afferent sum (Eq. 19), so the reading is
        local; and ℓ₀ − φ_L is log L₀ only with −∞ softened to −Λ, so the parallel says so.
      - **One agent addition, flagged in the bullet:** the sentence that RSA's informativity runs on
        the normalizer (for two utterances true at one state, S₁'s preference comes from their
        normalizers alone, cost aside). It follows from §1.2's three equations, so it quotes no
        number, and it makes concrete why forgetting the difference is dangerous. The bullet names it
        as the first to cut.
      - **Not done here, by the plan:** G8.3 (no RSA counterpart to a finite Λ; nothing plays
        Λ_crit) and G8.4 (P(s) in both L₀ and L₁) go to the background (U11). The outline's own
        word table and §3 heading still carry pre-R1 figures; replacing them is `revisions.md` §4's
        "Word allocation table" entry, which no U task owns.
- [x] **U10. §4.4 and §4.5, rebuilt on Λ = 512** (2026-09-18, commit `bab65cc`). `sections_3-6.md` §§4.1, 4.4, 4.5;
      headings to P-3's 140, 285, 255. No new code: every number is in the stored output of Code
      Cells 2, 2b or 4, checked by script against the outputs, not against the text cells.
      - **§4.1.** The A3 clause (G4): q_lit is a fixed point **because** ℓ₀ enters at g_L. The
        renamings (literal listener, tempered control) come in with it, because §4.4 now uses them
        and Entry 5 needs them defined first; DEC5's sentence goes in with a writer's note that it
        does not contradict U9's §3.2 (L₀ only as Λ → ∞, a limit and not a setting).
      - **§4.4 "The five priors".** Text cell 4b's table with tempering and utility columns; the
        conjunction under three of five, position under five, nested among these rows and not on
        the plane; the Λ = 8 contrast in one bullet (P-10), placing the change in the utility
        level's contribution, the one quantity the placement changes (Eq. D7), and the prior
        mattering less (contrasts agree to 0.0001 against 0.0575); P-9's two counts; the Cremers
        guards; the Eq. (23)–(24) mechanism.
      - **§4.5.** 33 cells, band (1,512)–(128,2048); the floors as the source of the trade-off
        claim (P-8); the V under both read-outs (R14); Eq. (41) as the exchange rate of §3.2's
        contest; spread D and the least-|θ_u| sentence at the printed values.
      - **Three things the plan had wrong, found against the printed rows** (details in
        `revisions.md` §4's §4.4 entry): (1) the utility level's contribution is **positive under
        Beta(1,3) at Λ = 512** (+0.0024), so "negative under all five" and item 1's Cremers guard hold
        at Λ = 8 only; (2) "four of five at Λ = 8" is really **all four priors with a Λ = 8 row**, the
        delta-like prior having none; (3) raising Λ **removes** the anti-exhaustive direction under
        flat and Beta(3,1) but **enlarges** it under Gaussian and Beta(1,3), so §10's gloss on P-9
        ("something raising Λ removes") was half true. P-9's decision itself, both counts in one
        sentence, stands and is applied. Also corrected: the floors cross between α = 8 and 16; the
        Eq. (41) match is 4.1%, not 4%.
      - **Deliberately not carried:** Text cell 4b's claim that every θ\* at Λ = 512 sits in
        Eq. (24)'s saturation (no cell prints it for the four diffuse rows); item 1's delta read-out
        results (they need §3.6 first).
- [x] **U11. Background §1.3** (2026-09-18, commit `4510beb`). `background_sections.md` only.
      - **Beat 2** gains G8.1 (the hard limit is L₀, a forward pointer), G8.4 (P(s) in L₀ and again in
        L₁; the prior enters this model once, and the commitment is which map), G8.3 (latent variables,
        not a strength: lexical uncertainty, threshold uncertainty, wonkiness; nothing plays the
        override law), and R19's foreshadowing with the warning in the same sentence and the
        coupling/model guard. All in Beat 2, not §1.2, because §1.3 carries P-3's added budget.
      - **Beat 3 (V11, taken here because it is the same subsection)**: pointer to §4.4, both counts
        as U10 corrected them, the tempering named, "corroboration" and the drain dropped (R7).
      - **Headings and totals** moved by P-3's +75: §1.3 415, Part I 2,110, target 3,670.
      - **Reference added:** Lassiter & Goodman (2017), *Synthese*, marked [verify], including
        whether Xiang et al.'s LG model builds on it or on the 2013 SALT paper.
      - **Found: α names two quantities** — RSA's speaker optimality (§1.2) and the Beta concentration
        of Eq. (41). The background states the override law in words; the clash is `revisions.md`
        **Q8**, open, for the user.
      - **Found for U12:** Beat 1's "redeployment" bullet says human robustness to prior concentration
        is "precisely the profile a drain scaling with prior mass on the all-region cannot produce" and
        flags it forward to §5.1. That is the trade-off claim in another form, and after P-8 it must
        point at §4.5's floors or go.
- [x] **U12. The verdict sites** (2026-09-18, commit `7f03135`). Against §9's table:
      - **V1**, central claim: the verdict on Λ = 512 and the plane, then R2's list with P-8's floors
        argument as its last item, marked argued and not measured; "shape of its absence" withdrawn.
      - **V2**, Tier A criterion row: reworded as planned.
      - **V7, V8**, §5.1: the two bullets become one (P-8 (i)), stated on §4.5's floors.
      - **V9, V10**, §6: item 1 flags the placement as a commitment; item 3 rewritten. Heading 165.
      - **Background Beat 1** (found in U11): the "drain scaling with prior mass" line now states the
        rising floor (§4.5) and points to §5.1's argument.
      - **Already done or elsewhere:** V4–V6 (U10), V11–V12 (U11); V3 and V14 are not R20's; V13 is
        U13's. A grep for the old headline's phrases ("every prior tested", "four of five", "under
        none", "exactly one condition", "shape of its absence", "only one of the two") finds only
        the sentences in §4.5 and §5.1 that bar the phrase; the outline's word table still titles
        §4.4 "One condition, every time", which U13 replaces.
- [x] **U13. `revisions.md`, the outline's table, and the stale pointers** (2026-09-21, commit `1bdeeea`).
      - **`revisions.md`.** R18–R20 and §3's table were already in place from U1. Now: the
        2026-09-15 note in §2 is **closed** and its table re-scoped as the 2026-09-13 record rather
        than the paper's evidence (site **V13**); §8's ℓ₀-placement row names **Code Cell D's Sec. 5**
        as the source and drops class (e), keeping the audit as the derivation; the scope-line and
        word-table entries in §4 are marked applied.
      - **`sections_3-6.md`.** The scope line reads 3,450 and names Code Cells A–D. The word table is
        replaced by §3's, with a "was" column and a note saying which sections have bodies written to
        the new budget. Headings brought into line: §3 1,085, §3.4 230, §4 1,020, §4.3 70, §5 1,180,
        §5.1 350, §5.2 400. **The renumbering is applied**: Limits → §5.5, Predictions → §5.6, with
        the three references in the scope tiers and one in `background_sections.md` (commitment 3)
        following. §§3.6, 4.6, 5.3 and 5.4 appear in the table with no bodies yet, and the note says
        so; the central claim's pointer to the new §5.3 now works.
      - **`decisions.md` A3.** The Evidence line no longer says the numbers are "to be printed" or
        class (e): Code Cell D prints them (U3, `23bdf23`), and the audit is named as the derivation.
      - **Not done, and not U13's:** the outline bodies whose budgets moved under R1–R17 but whose
        text U9–U12 did not touch (§3.4, §4.3, §5.1, §5.2, §5.5, §5.6). The table's note flags them.
- [x] **U14. Close the change** (2026-09-21, commit `a580599`). One logical change per commit throughout; every task
      line above carries its hash. The closing checklist of `agent.md` §6, item by item:
      - **Bogacz.** One new operation in the change, Eq. (D5), and it has Eq. (9)'s status, an
        instance under restriction (A3, D3). No divergence entry is needed.
      - **Quantities.** **A gap found and closed here:** U2 required Register-E entries for
        everything Code Cell D newly prints, and U3 closed without writing them. `decisions.md`
        now carries **E15**, classing the couplings and identities (a), BᵀW1 and the constant
        component (a), the σ-limit and same-φ_u blocks (a) with their two σ controls and the θ_u = 1
        control labelled, Part D under both placements (b), and Eq. (D5) itself as a counterfactual
        manipulation (C8). **Nothing in the change is class (e).**
      - **Decisions.** A3 amended (U2) and its Evidence line corrected (U13); R18–R21 in
        `revisions.md` §1; the agent decisions named to the user as they were made (Appendix D's
        retitle in U4, the §4.1 renamings in U10, the normalizer sentence in U9). **Q8 settled by
        the user 2026-09-21: RSA's parameter is α_rsa** → R21, applied in `background_sections.md`
        §§1.2 and 1.3. The notebooks never write RSA's α, so neither changed.
      - **Mirror.** `main.ipynb` is 23 cells; Code Cells 2 and 2b keep the exact `# === Code Cell 2:`
        and `# === Code Cell 2b:` prefixes E3 locates them by; `code cell 1` untouched since the
        checkpoint, so coupling 9 stays quiet.
      - **Execution.** Neither notebook has changed since **U7** (`bf746b1`), which ran both at
        baseline: main 0 errors, 8 figures, 14/14, 249 s; appendix_E 0 errors, 5 figures, E2 18/18,
        E3 PASS, 679 s. U8–U14 touched no notebook, so nothing needed re-running.
      - **Numbers.** Re-checked by script at close: the 68 decimal figures in everything U9–U13
        wrote (the central claim, §§3.2–3.3, 4.1, 4.4, 4.5, §5.1's new bullet, §6, background Beat 2
        and Beat 3) all appear in the stored output of a code cell. C6 holds.
      - **Anchors and numbering.** All 74 ToC links resolve; the body's tags run (1)–(41) complete;
        Appendix D's run (D1)–(D7).
      - **One deviation, reported rather than repaired.** The ten commits from U9 to U13 carry the
        subject line and the attribution but not `agent.md` §4.3's `Why:` and `Verified:` lines;
        U0–U8's commits do. The history is not rewritten for it (that needs the user under §4.5);
        this entry is the record that the tasks were prose-only and that no notebook was executed
        for them.

      **The change is closed.** Open items it leaves: the user has not confirmed U4's retitle of
      Appendix D, and `revisions.md` §7's older questions (Q2's residue, Q7's remainder) are
      untouched by it. Next is **T0–T13** of `procedure_records/scale_classes_hypothesis.md`.

---

## 7. Prose sites, to be written only after U3 and U7

- `main.ipynb` Appendix D (cell 20), new section; Code Cell D (cell 21); cell 0 ToC.
- `sections_3-6.md` §3.2 (lines 124–141) and §3.3's g_S bullet (lines 155–165).
- `sections_3-6.md` §4.1 (lines 218–232): the dependency of q_lit's status on A3.
- `sections_3-6.md` §4.4 (lines 265–297) and §4.5 (lines 298–317): the Λ = 512 rebuild.
- `sections_3-6.md` §3's word table (lines 81–103) and the scope tiers (lines 41–77).
- `background_sections.md` §1.2 and §1.3 Beat 2.
- Whatever U12 turns up in §5.1, §6 and the background's forward pointers.

---

## 8. The user's answers (2026-09-17), and what they open

> For P-5, state at an appropriate place that our utility level is a linear projection of the same
> log quantity. In the background section, foreshadow the similarity; however, we should also
> explicitly warn reader that, mathematically, projection does NOT imply equivalence and it is
> dangerous to forget that difference. For P-6, all verdicts associated should be reworked; tell me
> about it if you need further decisions/clarifications on my end.

**P-5 settled.** The parallel is stated; the background foreshadows it; and the warning that a
projection is not an equivalence is explicit, not left to the reader. **P-4** is settled with it:
all four parts of G8 are stated.

**P-6 settled in principle** — every verdict is reworked. The inventory is §9 below, and three
choices inside it are raised as P-8 to P-10.

### G10. The warning has an exact form, and it is measured

$B$ is orthogonal to the constant: $B^{\mathsf T}W\mathbf 1 = 9.4\times10^{-17}$ (m = 2, the
constant column dropped in Part A). So the utility level's drive is **invariant to an additive
constant** on the field it reads: adding $3.7\cdot\mathbf 1$ to $\ell_0-\varphi_L$ leaves
$c_{\textit{some}} = (9.119088, -24.367443)$ unchanged to $1.4\times10^{-14}$.

- **The statement.** $S_1$ reads $\log L_0(s\mid u)$, normalizer included. The utility level reads
  $B^{\mathsf T}W(\ell_0-\varphi_L)$: **rank 2, and blind to exactly the direction the normalizer
  lives in.** Two of the scale's coordinates — the tilt and the width of Appendix C — and nothing
  else. That is the warning in its exact form, and it is stronger than a caution: the projection
  discards the one component that makes $\log L_0$ a normalized quantity.
- **The nuance that must not be got wrong.** The invariance is a property of $c_y$, not of the
  model. $\varphi_S^\ast$ is *not* defined up to a constant — Text cell 3 §9.1 establishes there is
  no flat direction, and Appendix D §3's third reading turns on it — because the
  $\sigma_S(\ell_0-\varphi_L)$ term of Eq. (15) carries the constant directly. Say the invariance of
  the *coupling*; never write that the model is constant-invariant.

### G11. The trade-off survives, but as a property of the plane, not of the five priors

The floors table (Code Cell 4, already printed) gives the least Λ from which each criterion holds at
every larger Λ, by α on Beta(α,1):

| α | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| q shift | 512 | 256 | 128 | 64 | 32 | 32 | 16 | 2 | 2 | 2 | 2048 |
| q position | 2 | 2 | 2 | 2 | 64 | 256 | 512 | 1024 | — | — | — |

The two floors run in opposite directions and cross at α = 16. **§4.5's opposing-floors result is
untouched**, and so is the argument that a drain keyed to the alternative would not consume the
headroom the position criterion needs. What is false is the Part D framing: at Λ = 512 the
conjunction holds for α = 1 to 64 (7 of the 11 rows), because 512 lies above both floors over most
of the range, and among Part D's five priors the position criterion holds under **all five**. So
"prior concentration buys the first and spends the second" is a statement about the **floors**, and
it can no longer be carried by "under every prior tested".

### G12. The Λ = 512 picture, for the rework

From Text cell 4b, already printed: the q position criterion holds under **five of five**; the q
shift criterion under **three** (flat, Beta(3,1), delta-like); **no prior meets the shift criterion
alone**. So the two conditions no longer separate the rows — the shift criterion is strictly the
harder one, and the three that meet it are the three with the most prior mass on the all-region
(0.0479, 0.1367, 0.9568), the shift deepening with that mass. The anti-exhaustive direction holds
under **two of five** at Λ = 512 (Gaussian +0.0071, Beta(1,3) +0.0089), against four of five at
Λ = 8.

---

## 9. Every verdict site, and what it needs (P-6)

`sections_3-6.md` unless noted. "Planned" means `revisions.md` §4 already has an entry, written
against the Λ = 8 count; those entries are corrected here, not only the outline.

| # | Site | What is wrong | Status |
|---|---|---|---|
| V1 | Central claim, constructive claim (lines 21–32) | "Exactly one condition holds under every prior tested, never both and never neither" — false twice over at Λ = 512 | Planned rewrite; its **replacement** was written at 1 of 5 and needs 3 of 5 |
| V2 | Scope tiers, Tier A criterion row (line 52) | "The spine of the constructive claim" | Planned: → "the verdict, and the evidence that the conjunction is reachable". Still right, and stronger |
| V3 | §4.2 (lines 234–253) | The criterion itself survives; the guard's instances are fixed-θ_u controls | Planned, unaffected by P-6 |
| V4 | §4.4 table and lines 277–289 (lines 265–297) | The whole section is the Λ = 8 table | **U10.** Needs P-10 |
| V5 | §4.4 line 288, anti-exhaustive "four of five" | Two of five at Λ = 512 | **P-9** |
| V6 | §4.5 (lines 298–317) | 22 cells → 33; band (1,512)–(128,2048) | Planned; **G11 adds** that the floors are now where the trade-off is stated |
| V7 | §5.1 lines 329–338, "Why the pattern points at such a level" | Removed under R14 already; but its *claim* is what §6 item 3 still asserts | **P-8** |
| V8 | §5.1 lines 339–343, Cremers corroboration, "four of five" | Moved to §4.4 under R7; the count changes with it | **P-9** |
| V9 | §6 item 3 (lines 511–516) | "Satisfies only one of the two conditions … under every prior tested" — false | Planned rewrite; restate per P-8 |
| V10 | §6 item 1 (lines 505–508) | Nothing wrong. It already says the entry "compet[es] additively against the world prior in the same log-density" | **Carries R18's commitment** with a clause; no rework |
| V11 | `background_sections.md` line 189, §1.3 Beat 3 | "§5.1 reports … four of five priors"; R7 redirects it to §4.4 | **P-9** |
| V12 | `background_sections.md` §1.3 Beat 2 (lines 166–185) | Nothing wrong; gains the RSA material | U11 |
| V13 | `revisions.md` §2's table and scope sentence | Part D as of 2026-09-13 | U13 |
| V14 | §6 item 4, §5.2, §5.6 | Depend on Q7/R16 | Belongs to T0–T13, not here |

**Not a verdict site:** the notebooks. Under B10/C7 they report criteria and take no position, and
Text cell 4b already states the Λ = 512 counts in that register. Nothing in `main.ipynb` or
`appendix_E.ipynb` needs a verdict rework; U7 only re-executes them.

---

## 10. Further decisions this opens (P-8 to P-10)

- **P-8. What replaces the trade-off claim, and where it is sourced.** The claim "prior
  concentration buys the first condition and spends the second" motivates the drain keyed to the
  alternative, and it appears at V7 and V9. By G11 it is true of the **floors** and false of the
  five priors. Options: (i) restate it on the floors — §4.5's own result, unchanged — and drop
  "under every prior tested" wherever it appears; (ii) withdraw it entirely and let R2's complexity
  argument carry §5.1 alone; (iii) keep it only inside §4.5 and let §5.1 and §6 point there.
  **Recommendation (i)**, because the result it rests on is untouched and printed, and because
  removing it would leave §6 item 3 with nothing to say about what a level would change. This
  rewrites an interpretive argument, so under `agent.md` §5.4 it is the user's.
- **P-9. Which Λ the anti-exhaustive count is stated at** (V5, V8, V11). Four of five at Λ = 8, two
  of five at Λ = 512. Stating it at Λ = 512 is consistent with the rest of §4.4 and makes the
  direction **something raising Λ removes**, which is R18's counterforce doing visible work — but it
  weakens the Cremers tie, which background §1.3 Beat 3 offers as "a second, independent reason".
  Options: Λ = 512 only; Λ = 8 only, labelled; or both, as the contrast. **Recommendation: both**,
  in one sentence — it costs about 15 words and it is the cleanest demonstration of the commitment.
- **P-10. Whether §4.4 reports one Λ or two.** The notebook keeps both (Part D at Λ = 8, Text cell
  4b at Λ = 512). Reporting only Λ = 512 is cheaper and is where the verdict now lives; reporting
  both is what makes the counterforce visible in the evaluation rather than only asserted in §3.2.
  **Recommendation: the Λ = 512 table, with Λ = 8 as a one-line contrast**, which resolves P-9 the
  same way and joins P-6 to R18.

**Tasks these change.** U9 gains the P-5 statement in §3.3 and the exact warning of G10; U11 gains
the background foreshadowing and the same warning; U12 is no longer a sweep for stragglers but the
worked list V1–V13 above; U10 absorbs V4–V6.


---

## 11. The user's answers, round three (2026-09-17), verbatim

> P-8: do as you recommended. P-9: both, as you recommend. P-10: do as you recommend. P-1: printed
> by Code Cell D. P-2: yes, 3.2 as the host. P-3: word budget is fine. P-7: amend.

**Every blocking decision is now answered.** In the form they take in the tasks:

| | Settled as |
|---|---|
| **P-1** | The alternative placement is **reported with numbers, printed by Code Cell D** (option (ii)). U3 is live; until it runs, A3's numbers are class (e) under `agent.md` §3.3. |
| **P-2** | **§3.2 hosts the commitment**; §3.3 takes the g_S clause and, under R19, the projection statement. |
| **P-3** | **The budget is raised, not trimmed.** §§3–6 go 3,200 → **3,450**; background §1.3 goes 340 → about 415. Applied to `revisions.md` §3. |
| **P-4, P-5** | All four parts of G8 are stated; the background foreshadows; the warning is explicit and takes G10's exact form. R19. |
| **P-6** | Every verdict reworked; sites V1–V13. R20. |
| **P-7** | **Amend A3 in place.** Done (U2). |
| **P-8** | **Option (i):** the trade-off claim is restated on the **floors** (§4.5, G11) and "under every prior tested" goes wherever it appears — V7 and V9. §5.1 and §6 point at §4.5 for it. |
| **P-9** | **Both counts**, in one sentence: four of five at Λ = 8, two of five at Λ = 512, the direction being what raising Λ removes. Applies at V5, V8 and V11. |
| **P-10** | **§4.4 carries the Λ = 512 table with Λ = 8 as a one-line contrast.** This is also how P-9 is discharged, so P-6's rework and R18's commitment become one piece of writing. |

**Found while applying P-3.** `revisions.md` §3's §5 subtotal read 980 after S-6 raised §5.2 from
200 to 400; the correct figure is 1,180 (the grand total 3,200 was right). Corrected in the same
pass and noted under the table.

**What U3 must now print**, given P-1 and the decisions above — the numbers §3.2, §3.3, §4.1 and
Appendix D will quote:

1. c_y under both placements, per utterance, and the two identities of G1 (2BᵀWℓ₀ and −2BᵀWφ_L).
2. The σ_L = σ_S agreement at a shared φ_u (1.8e-15) and the (σ_L − σ_S)ℓ₀/S difference at σ_L = 2.
3. The σ-limit table of G4: ℓ₀ − φ_L reached under g_L and under no σ under g_S.
4. **R19's warning, which is a new requirement on U3:** BᵀW1, and c_y's invariance to an additive
   constant on the field. Neither is in the audit's eight blocks — they were measured separately
   and must be added.
5. Part D under both placements (G6), at Λ = 8 and Λ = 512, since P-10 puts both Λ in §4.4 and
   P-1 puts the alternative's numbers in a cell.

All of it labelled **counterfactual manipulation (C8)**, never "control".
