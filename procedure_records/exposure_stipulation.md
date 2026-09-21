# Uniform exposure, stated as a stipulation

Working record for the change the user approved on 2026-09-21, settling `decisions.md` **O2**.
Pattern: `agent.md` §5.3.

**Task IDs here are `X0`–`X5`.** `N0`–`N8` (`resolution_naming.md`) and `T0`–`T16`
(`scale_classes_hypothesis.md`) are live at the same time; the prefixes keep them apart.

**Status, 2026-09-21: approved, nothing implemented.** No question is outstanding. The user's
standing instruction on the N list — do not start implementing — is taken to cover this one too
until they say otherwise.

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

- [ ] **X0. Checkpoint** (`agent.md` §4.2). Record `git rev-parse --short HEAD`.
- [ ] **X1. Appendix B (Y1).** The stipulation, the σ parallel, the later-phase note, and the
      asymmetry of §2 in one short passage. It does **not** claim how far a non-uniform p(y) would
      move θ_u\*; that was option (d) and was not adopted. Position reserved (composition guide
      Entry 3b).
- [ ] **X2. Text cell 3 §3 (Y2).** One sentence beside item 3, in item 3's own register, and the
      "uniform at this phase" clause in item 6. No new equation and no new notation: p(y) is already
      named in Appendix B, and if the sentence needs it here it is defined at first use.
- [ ] **X3. The outline (Y3, Y4) and `revisions.md` (Y5).** Written after X1 and X2, so the paper's
      wording follows the notebook's.
- [ ] **X4. Couplings.** None is expected to fire: markdown only, no tag added, no anchor added,
      `code cell 1` untouched, E3 unaffected. Confirm rather than assume, and confirm the ToC needs
      no change (no heading and no equation range moves).
- [ ] **X5. Commit.** One logical change per commit, hashes recorded above. **No execution**, so the
      message says `Verified: not run`, with the reason.

**Sequencing note.** If this list runs in the same pass as `resolution_naming.md` N0–N8, X1 and X2
touch cells 16 and 4 while N touches 14, 15, 5, 0 and E1, so nothing collides; N6's execution then
covers both, and X5 folds into N8. Run alone, this change needs no execution at all.

---

## 5. What this change does not do

- It does not measure the sensitivity of θ_u\* or of the criteria to p(y). Option (d) was declined.
- It does not touch Code Cell B's *ALTERNATIVE SPACES* block, which varies ensemble **membership**
  and is a different probe.
- It does not settle **O8**, which asks what ensemble a single-predicate configuration has. O8
  inherits this entry's principle — stipulate, label, and decline to invent — but its membership
  question is still the user's to answer.
