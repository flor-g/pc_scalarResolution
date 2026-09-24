# Composition guide

Working rules for prose in `main.ipynb` and `appendix_E.ipynb` (text cells, appendices, and in-code comments), `thesis_outline/sections_3-6.md`, and `thesis_outline/background_sections.md`. *(Filenames corrected at BG8–BG12, 2026-09-22; the two named before were the 2026-09-01 Desktop drafts, which `agent/agent.md` §1 lists as not maintained.)*

**How to use it.** Entry 1 is a drafting rule: hold it in mind while the first draft is
written, because a claim that violates it is not repaired by editing. Entries 2, 3, and 4
are editing rules: on revision, assess and apply them **in the order listed** — significance
first, then necessity, then language. The order matters, since a sentence cut under Entry 3
never needs Entry 4, and a claim recalibrated under Entry 2 often changes what Entry 3
judges essential. Entry 5 was given without a stage assignment; it is placed last here but
runs at both stages, since a name introduced in the first draft is the one later edits inherit.

---

## 1. Awareness of construction constraints

The model is built under the **locality constraint** of Bogacz (2017): computation is local
(a unit's update uses only quantities available at that unit) and plasticity is local
(a weight's update uses only the activities it connects).

Before a claim goes into the draft, run it through three steps:

1. **Does the claim satisfy the constraint?** If it does not, the claim is not about this
   model, and either the claim or the construction has to change.
2. **If it does, is that immediate to a reader?** Ask whether a reader who knows Bogacz
   (2017) would see the locality of the claim without being told.
3. **If it is not immediate, clarify with proper reasoning.** Show which quantities the
   update actually uses, and where they sit.

A claim can be true of the mathematics and still fail step 1 — a quantity that a global
computation would furnish is not available to a unit that cannot see it. Step 3 is where
most of the work falls: the reasoning is usually short, but it has to name the quantities,
not gesture at them.

---

## 2. Calibrating the significance of a result

When attributing significance, err in neither direction. Both failures are failures of
bookkeeping about what the model assumes.

**a. Overstating.** The claim asserts what the evidence or reasoning does not support,
because it silently borrows an intermediate assumption from a theoretical framework outside
this model's foundation. Test: name every assumption the claim needs. If one of them is not
in the model, either state it as an assumption or weaken the claim to what the model gives.

**b. Understating.** The claim credits the result with less than it establishes, because the
model's own foundational assumptions were not brought to bear. Test: ask what the model
already grants. A result that looks narrow in isolation may be general once the standing
assumptions are counted, and the reader should not be left to discover that.

Both directions are corrected the same way — by making the assumption ledger explicit — so
when a claim's strength is in doubt, write out what it rests on before choosing the verb.

---

## 3. Necessity of statements

Do not make unnecessary statements.

**a. Statements that do not serve the argument being pursued.** Cut them. A true, even
interesting, remark that the argument does not use is a cost to the reader with no return.

**b. Statements that are not essential to the argument but that a reader should weigh.**
These are not cut and not asserted. They belong to the reader's own judgment, so **note the
relevant fact and mark our position as reserved.** State the fact plainly; do not argue
either way from it.

The distinction is between what the argument needs (keep and use), what it does not need and
the reader does not need (cut), and what the argument does not need but the reader does
(record, without a verdict).

---

## 4. Abuse of language

**a. Reference words.** Do not lean on demonstratives and pronouns — *this*, *that*, *it*,
*these* — where the preceding phrase offers more than one candidate antecedent. When there
are several, replace the reference word with the referent named outright, so that the
reference is indexed rather than inferred.

**b. Negation phrases.** Before writing *is … rather than …*, *is … not …*, or
*is … instead of …*, run three checks in order:

1. Is the negated statement already recoverable from the preceding context? If it is, the
   negation is telling the reader something they have; drop it and assert the positive.
2. Is the asserted half an overstatement or an understatement, by Entry 2? A contrast frame
   makes a claim feel sharper than its evidence, so it invites overstatement in particular.
3. Is the whole construction too loose against the result it is attributed to? A contrast
   pitched more broadly than the measurement or derivation behind it is redundant for a
   reader, who cannot use the extra breadth.

**c. Parallel constructions.** Before setting two statements in parallel, ask first whether
the paralleled statement is already immediate to the reader — if it is, the parallel is
padding. If it is not immediate, ask whether a **connecting phrase** would do better, by
carrying the reader through the logical progression of the argument instead of leaving the
relation between the two halves to be inferred from their shape.

---

## 5. Alignment of names

Assess every name and variable that plays a significant role in a statement.

**a. Unsourced convention.** A name taken from convention, with no source behind it, must be
**defined explicitly in our own composition before it is used**.

**b. Sourced.** A name or variable that the preceding context has not defined and that comes
from a specific source or line of thought must be **properly cited** — `("work")`,
`(c.f. "work")`, or `(as in "work")`.

**c. Unsourced notation.** Every variable or piece of notation that is not sourced must be
**defined explicitly, in a proper place, before any statement incurs it**.

"Proper place" means the place a reader will already be looking when the notation first
does work, not merely somewhere earlier in the document.

---

## Pass checklist

Drafting:

- [ ] Every claim checked against locality; the non-immediate ones carry their reasoning (1)
- [ ] Every name and notation defined or cited before first use (5)

Editing, in order:

- [ ] Entry 2 — assumption ledger written out for each load-bearing claim; verbs matched to it
- [ ] Entry 3 — non-serving statements cut; reader-relevant non-essentials reduced to a
      noted fact with our position reserved
- [ ] Entry 4a — demonstratives and pronouns with competing antecedents replaced by referents
- [ ] Entry 4b — each negation frame passed through recoverability, calibration, looseness
- [ ] Entry 4c — each parallel passed through immediacy, then connective
- [ ] Entry 5 — names re-checked, since Entries 2-4 move text across the first-use point
