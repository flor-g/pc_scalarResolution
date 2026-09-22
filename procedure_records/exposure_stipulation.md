# The exposure ensemble, stated as a stipulation: its weights and its membership

Working record for the change the user approved on 2026-09-21, settling `decisions.md` **O2** (the
ensemble's **weights**) and, from the same day, **A18** and **O8**'s ensemble half (its
**membership**). Pattern: `agent.md` §5.3.

**Task IDs here are `X0`–`X8`.** `N0`–`N8` (`resolution_naming.md`) and `T0`–`T16`
(`scale_classes_hypothesis.md`) are live at the same time; the prefixes keep them apart.

**Status, 2026-09-22: APPLIED.** All nine tasks closed; commit recorded at X5 below. Markdown
only, so no coupling fired and neither notebook was re-executed — verified rather than assumed
(X4). One correction to this record's own site table: Y2's pointer said "Text cell 3 §3, item 3",
but the σ sentence and the "exposure ensemble" clause are in Text cell 3's **preamble** items 3 and
6, not in §3, whose item 3 is the utility basis $B$.

---

## 1. The decision, in the user's words (2026-09-21)

> go with (a). Again, I think this is essentially the same philosophy as fixing all sigma at 1.

Option (a) of the four put to them: **stipulate uniform p(y) and label it**, rather than argue it
from a principle, fit it to corpus frequencies, or add a sensitivity sweep. Recorded as
`decisions.md` **O2**, settled.

---

## 2. Why the σ parallel is the right frame, checked

Text cell 3 §3 item 3: "At this phase, the model does not implement any precision inference. Hence,
every variance (σ) is fixed at 1. The value is the multiplicative identity because σ weights a
synaptic connection, so fixing every σ at 1 assigns equal weight to every connection." Text cell 3
§6 keeps the log σ terms "only to mark where a later precision-bearing version would reintroduce
them".

The parallel is exact on three counts, and the prose should use it rather than invent a new frame:

1. **The reason is the same.** A quantity the phase does not model (precision; exposure statistics)
   is fixed at the value that treats every channel, or every utterance, alike.
2. **The stipulated value is the one that makes the quantity vanish from the formula.** σ = 1 gives
   ε_y = r_y and constant log σ terms; uniform p(y) turns 3·E_{p(y)}[c_y] into the bare sum Σ_y c_y
   that Eq. (B3) already writes.
3. **Both are marked for a later phase**, not hidden: precision-bearing for σ, frequency-bearing for
   p(y).

**The one asymmetry, to be stated and not smoothed over.** σ is a variable in the code with a
default of 1, so a precision-bearing phase changes defaults (D11 covers σ ≠ 1). p(y) is not a
variable at all — it is implicit in the batched sum — so a frequency-bearing phase adds a weight
vector. Appendix B's per-presentation check (the batched and per-presentation flows agree to
3e-4) is where that would be felt, since it is exactly the place the ensemble is visited one
utterance at a time.

---

## 3. Sites

| # | Site | What changes |
|---|---|---|
| Y1 | `main.ipynb` cell 16, Appendix B, the "prior over utterances" sentence | It states the fact and stops. It gains the stipulation, the σ parallel in one clause, and what a later phase would add (a weight vector, not a default) |
| Y2 | `main.ipynb` cell 4, Text cell 3 §3 | Item 3 fixes σ; the exposure stipulation belongs beside it, one sentence, so the two stipulations of the phase are read together. Item 6 already lists "the exposure ensemble" among what fixes θ_u\*, and gains "uniform at this phase" |
| Y3 | `thesis_outline/sections_3-6.md` §5.6 | The exposure prediction reads as a prediction **about departures from a stipulated uniform**, which is what makes it a prediction at all |
| Y4 | `thesis_outline/sections_3-6.md` §5.5 Limits | One clause: results are reported at uniform exposure; a frequency-bearing version is not built |
| Y5 | `thesis_outline/revisions.md` | A site entry for Y3 and Y4, so the outline pass picks them up |
| Y6 | `decisions.md` | O2 settled (done 2026-09-21); A14's "see O2" pointer still reads correctly |

**No code changes and no numbers move**, because uniform is what the code already computes. Nothing
here is printed, so C6 does not arise and neither notebook is re-executed for this change alone.

---

## 4. Tasks, in order

- [x] **X0. Checkpoint** — clean tree at `f64d32e` (2026-09-22).
      *(original:)* **X0. Checkpoint** (`agent.md` §4.2). Record `git rev-parse --short HEAD`.
- [x] **X1. Appendix B (Y1)** — done. The stipulation and the σ parallel sit with the prior-over-utterances sentence; the asymmetry went to the per-presentation passage instead, since that is the place it would be felt. No claim about how far a non-uniform p(y) moves θ\*.
      *(original:)* **X1. Appendix B (Y1).** The stipulation, the σ parallel, the later-phase note, and the
      asymmetry of §2 in one short passage. It does **not** claim how far a non-uniform p(y) would
      move θ_u\*; that was option (d) and was not adopted. Position reserved (composition guide
      Entry 3b).
- [x] **X2. Text cell 3, preamble items 3 and 6 (Y2)** — done; see the site correction above.
      *(original:)* **X2. Text cell 3 §3 (Y2).** One sentence beside item 3, in item 3's own register, and the
      "uniform at this phase" clause in item 6. No new equation and no new notation: p(y) is already
      named in Appendix B, and if the sentence needs it here it is defined at first use.
- [x] **X3. The outline (Y3, Y4) and `revisions.md` (Y5)** — done: §5.6's exposure prediction now reads as one about departures from a stipulated uniform, §5.5 Limits carries both stipulations, and **R24** records the change.
      *(original:)* **X3. The outline (Y3, Y4) and `revisions.md` (Y5).** Written after X1 and X2, so the paper's
      wording follows the notebook's.
- [x] **X4. Couplings** — confirmed, not assumed: three markdown cells changed and no code cell; equation tags 61 → 61 with none added or removed; no anchor added or removed; stored outputs 41 → 41. So couplings 5, 6 and 9 are quiet, E3 cannot fire, the ToC is unaffected and **no execution is needed**.
      *(original:)* **X4. Couplings.** None is expected to fire: markdown only, no tag added, no anchor added,
      `code cell 1` untouched, E3 unaffected. Confirm rather than assume, and confirm the ToC needs
      no change (no heading and no equation range moves).
- [x] **X5. Commit** — done.
      *(original:)* **X5. Commit.** One logical change per commit, hashes recorded above. **No execution**, so the
      message says `Verified: not run`, with the reason.

**Sequencing note.** If this list runs in the same pass as `resolution_naming.md` N0–N8, X1 and X2
touch cells 16 and 4 while N touches 14, 15, 5, 0 and E1, so nothing collides; N6's execution then
covers both, and X5 folds into N8. Run alone, this change needs no execution at all.

---

## 5. The membership half (A18, added 2026-09-21)

**The decision.** The ensemble holds at least {χ, ker χ} (Appendix D Eq. (D2)); an antonym is never
needed to define an entry; antonymy is a lexical accident of two words sharing a scale, is not
invertible where ker is, and has no word at all where ker E_all = {1}, the O corner. In this phase
ant(x) may **coincide** with ker(x), which is a prediction of the single θ and is not transported
(O9's pattern). That the inventory holds the pair at all is this phase's stipulation, labelled as
one; under §5.1's proposed level, with at most two entries per level, it becomes a consequence
instead — and that is compatible with O14, since complementarity is **within** a level and O14's
asymmetry is **across** levels.

- [x] **X6. Appendix B and Appendix D** — done. Appendix D §2 takes the membership stipulation, beside Eq. (D2) where ker is defined and where ker E_all = {1} makes the point; Appendix B states membership beside weighting.
      *(original:)* **X6. Appendix B and Appendix D.** Appendix B's ensemble passage says what the ensemble
      contains, beside X1's sentence on how it is weighted, so membership and weights are stated
      together and both are labelled as this phase's stipulations. Appendix D §2, which already
      defines ker and tabulates where it escapes the family, gains the one sentence that the
      inventory holds {χ, ker χ} for any entry — it is the notation's home, and the E_all row is the
      case that makes the point.
- [x] **X7. §5.1 and §5.2** — done. §5.1's cascade is connected to A18 in one clause. §5.2's half went **into T10's task line** rather than into §5.2's prose, because T10 rewrites that section wholesale and prose written now would be overwritten; the constraint is therefore where the writer will read it.
      *(original:)* **X7. §5.1 and §5.2.** §5.1's cascade is already written ⟨E_some, ker E_some⟩ and
      ⟨E_all, ker E_all⟩; one clause connects it to A18 so the design and the commitment read as one
      claim. §5.2 states the ensemble as the inventory's, **not** as the experiment's: F20 shows the
      latin square denies the exposure reading, and the user's principle is that inventory follows
      from exposure but not conversely. It also says that ant coincides with ker for these absolute
      classes in this phase, with no thesis about antonymy.
- [x] **X8. Records** — done: R24 in `revisions.md`, the wording constraint on `scale_classes_hypothesis.md` T10, and this block.
      *(original:)* **X8. Records.** `decisions.md` A18 and O8 are written (2026-09-21); `revisions.md` gains the
      site entries for X6 and X7; `scale_classes_hypothesis.md` T2's block 1 and T10's prose carry
      the wording constraint of X7.

---

## 6. What this change does not do

- It does not measure the sensitivity of θ_u\* or of the criteria to p(y). Option (d) was declined.
- It does not touch Code Cell B's *ALTERNATIVE SPACES* block, which varies ensemble **membership**
  and is a different probe.
- It does not derive the inventory. A18 fixes what the ensemble contains; why a lexicon contains
  those entries is not this phase's question.
- It does not measure a no-antonym configuration. A18 says the ensemble is {χ, ker χ} whether or not
  a word lexicalizes ker χ, so nothing needs re-running; the audit's ensemble probes stand.
