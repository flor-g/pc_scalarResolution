# One name for the scale's resolution, and what fixes it

Working record for the change the user opened on 2026-09-21, after closing the Λ–ℓ₀ change
(`ell0_placement_and_counterforce.md`, U0–U14). Pattern: `agent.md` §5.3.

**Task IDs here are `N0`–`N8`.** `T0`–`T16` (`scale_classes_hypothesis.md`) are live at the same
time; the prefixes keep them apart.

**Status, 2026-09-21: the plan is approved and nothing is implemented.** Q-N1 is answered by the
user — option (i), Eq. (A6) goes — so N0–N8 are unblocked, and the user's instruction is
**"Don't start implementing yet"**: no task below begins without their word.

---

## 1. The user's instruction, verbatim (2026-09-21)

> We currently don't have an answer for what fixes delta since we don't include predicates with
> unstable atoms as one of the modeled cases in this phase; in addition, for subsequent phases, I
> don't think we will fix delta at all, it should be a read-out that is derived from a learned
> theta_L. Also, unless the name comes from Xiang's papers, I don't think we should give it a
> separate name from n, since they are essentially the same quantity.

Recorded as **`decisions.md` O1**, now settled: the question is out of scope in this phase and
dissolved in the next, and the dissertation keeps one name.

---

## 2. What is on record already

- **Eq. (A5)**, ς(−θ_L) = 1/2n ⟺ θ_L = log(2n − 1), n = (e^{θ_L} + 1)/2: n is the number of atoms
  the predicate resolves.
- **Eq. (A6)**, ς(−θ_L) = δ/2 ⟺ θ_L = log(2/δ − 1), for a gradable predicate that supplies no
  count, with the appendix's own remark that "Eq. (A5) is the case δ = 1/n, and the two are the
  same statement".
- **The open part of Appendix A**: what fixes δ, with two candidates that disagree near the
  endpoints — δ constant in s (the counting case) and δ constant in ζ (Weber-type).
- **Eq. (A4)**: θ_L's gradient vanishes identically while ε_y ≡ 0, so this phase cannot learn it;
  unclamping φ_L sets it running.
- **δ is ours.** Xiang et al. (2022) name their models LG, QF and ST; none uses δ or a JND. Checked
  2026-09-21 against `procedure_records/scale_classes_hypothesis.md` and the 2026-09-17 audit.
- **"Delta" is already taken** by the delta read-out, the posterior of the construction (A16, B7),
  and by the delta-like prior's row label.

---

## 3. Every site that names δ

Found 2026-09-21 by a search of both notebooks, the outlines and the records.

| # | Site | What is there |
|---|---|---|
| S1 | `main.ipynb` cell 14, Appendix A | The gradable-case paragraph, **Eq. (A6)**, the grid cap restated as δ > 0.004945, and the open-part paragraph |
| S2 | `main.ipynb` cell 15, Code Cell A | Prints "the same cap on a just-noticeable difference: delta > 2/(e^Z + 1) = 0.004945" under the heading *Appendix A: theta_L AND ITS DENOTATION n (Eqs. A5-A6)* |
| S3 | `main.ipynb` cell 5, `code cell 1` | Comment: "the predicate has atoms, else 1/delta for a JND delta (Eq. A6, Appendix A)" |
| S4 | `appendix_E.ipynb` cell 2, E1 | The same comment, mirrored (**coupling 9**) |
| S5 | `main.ipynb` cell 0, ToC | Appendix A's row reads **(A1)–(A6)** |
| S6 | `thesis_outline/sections_3-6.md` §3.3 | "Where no atom count exists, the same declaration reads ς(−θ_L) = δ/2 for a just-noticeable difference δ (Eq. A6)" |
| S7 | `procedure_records/scale_classes_hypothesis.md` §2 | "H1 makes Λ a function of how stably the predicate fixes δ"; §2's H2 line "anchored by neither endpoint nor δ" |
| S8 | `decisions.md` O1 | Rewritten 2026-09-21 with this decision; its 2026-09-15 finding still says "what fixes δ" |

Nothing else computes with it: no code reads a δ variable, and no printed number other than S2's
0.004945 depends on the name.

---

## 4. What must be settled before any edit (blocking)

- **Q-N1. Does Eq. (A6) go, or stay restated in n? — ANSWERED by the user 2026-09-21: option (i),
  the agent's recommendation. Eq. (A6) goes; Appendix A runs (A1)–(A5); nothing renumbers.** The two
  candidate readings of the resolution (constant in s, constant in ζ) are kept as a noted fact with
  our position reserved, as N1 sets out.
  - **(i) (recommended) It goes.** Its content moves into a paragraph under Eq. (A5): n need not be
    an integer; where the predicate counts, n is its atoms; where it does not, n is the number of
    distinguishable steps of the scale, and Eq. (A5) is read with a real n. Appendix A then runs
    (A1)–(A5), the ToC row follows, and **nothing renumbers**, since (A6) is the appendix's last
    tag. This is what "one name" means applied to the equations as well as the prose.
  - **(ii) It stays, restated in n.** But then two numbered equations state one declaration, which
    is the duplication the decision removes.
  - **(iii) It stays as is.** Rejected by the decision.

Everything else in §5 follows from the answer and needs no further decision. **No question is
outstanding**; what the list waits on is the user's go-ahead to start.

---

## 5. Tasks, in order

Code before prose (`agent.md` §5.3). The only code here is one comment and one printed line, but
S2's line changes Code Cell A's output, so both notebooks are re-executed (N6).

- [ ] **N0. Checkpoint** (`agent.md` §4.2). Record `git rev-parse --short HEAD`.
- [ ] **N1. Appendix A (S1), markdown.** Under Q-N1(i): Eq. (A6) is removed and its content folded
      into Eq. (A5)'s discussion — the two-part gloss of n, the non-integer reading, the grid cap
      stated once as n < 202.21, and the observation that a counting predicate and a gradable one
      differ in where n comes from and not in the formula. **The open-part paragraph is replaced by
      O1's decision**: this phase stipulates n and says so; the two candidate readings (constant in
      s, constant in ζ) are kept as the statement of what a resolution could mean, with our position
      reserved (Entry 3b); and the position for the next phase is stated — n is not a parameter to
      fix but a **read-out of a learned θ_L** by Eq. (A5), which Eq. (A4) says this phase cannot
      learn while φ_L is clamped. No verdict on which reading is right.
- [ ] **N2. Code Cell A (S2).** The δ line goes; the n cap stays. The block heading becomes
      *Eqs. (A5)* rather than *(A5-A6)*. No number that any prose quotes is removed except 0.004945,
      which N1 removes from the prose in the same change.
- [ ] **N3. `code cell 1` (S3) and E1 (S4).** One comment, mirrored. **Coupling 9 fires**: the two
      cells stay source-identical in this comment, and E1's relay arguments are untouched.
- [ ] **N4. ToC (S5).** Appendix A's row → (A1)–(A5), derived from the cell's own tags, not typed.
      Re-check that all 74 links resolve.
- [ ] **N5. Couplings.** 5 (equation numbers: (A6) removed, nothing renumbered, no body tag moves),
      6 (anchors), 9 (N3), and E3's prefixes untouched.
- [ ] **N6. Execute** main then appendix_E (`agent.md` §5.1). Acceptance: main 0 errors, 8 figures,
      14/14; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS. The only stored-output change should
      be Code Cell A's two lines and `cost:` lines.
- [ ] **N7. Prose and records.** `sections_3-6.md` §3.3 (S6) drops the δ clause and states the
      two-part gloss of n in one sentence; `scale_classes_hypothesis.md` §2 (S7) reads n for δ, which
      also makes H1's wording match S-4's n = 4; `decisions.md` O1's 2026-09-15 finding (S8) reads n;
      `agent.md` §5.5's naming list gains the one-name rule if it is the kind of clash that list
      records.
- [ ] **N8. Commit**, one logical change per commit, hashes recorded above.

**Sequencing note (2026-09-21).** `procedure_records/exposure_stipulation.md` (X0–X5, decision O2)
is approved and waiting too. It touches cells 16 and 4 where this list touches 14, 15, 5, 0 and E1,
so the two do not collide, and N6's execution would cover both. Running them in one pass saves an
`appendix_E.ipynb` run of about 11 minutes.

---

## 6. What this change does not do

- It does not choose between δ constant in s and δ constant in ζ. That choice is what O1 says this
  phase does not make.
- It does not make θ_L learnable. Eq. (A4) already says what would set it running, and the next
  phase is where that happens.
- It does not touch n = 10 or §5.2's n = 4. Both are stipulations and stay.
