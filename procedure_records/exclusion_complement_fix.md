# exclusion_indicator: χ_some as the complement of χ_no

Working record for the change settled as decision **I13**, on the pattern of
`theta_u_learned_reach.md`. It arose from finding F11 of
`side_quests_mirror_and_granularity.md`.

## 0. Instructions (the user's, verbatim, 2026-09-16)

> let's look into 2. Why is it that the code defines < instead of <=?

and, after the account below was put to them and two fixes were compared:

> good. go with the complement fix

On the uncommitted Appendix C line the user chose, when asked, to **fold it into the fix commit**.

## 1. The divergence

Eq. (A1) writes E_some ↦ {ζ ≤ −θ_L}, non-strict. `exclusion_indicator` computed
`margin = -(zeta + theta_L)` and excluded where `margin > 0`, i.e. the strict ζ < −θ_L. Its own
docstring stated the non-strict form, so the code disagreed with both the docstring and Eq. (A1).

**Why it read that way.** The function computes a signed margin and applies one shared
`margin > 0` to all three entries. That factorization exists for the `sharpness` branch, which
feeds the margin to a logistic and never compares it. Two of three entries are strict in Eq. (A1),
so the shared test gets them right; *some* is the only non-strict one, and it was the one built as
the **negation** of another entry's margin. Negating a margin and re-applying a strict test gives
`<`, never `≤`. The strictness was inherited from the factorization, not chosen.

Present since the initial snapshot 499918c and never edited; the docstring carried the correct `≤`
from that same commit.

## 2. Why the complement form, and not `margin >= 0`

Both match Eq. (A1). The complement form was chosen because it keeps one shared comparison and one
shared smooth map, and makes χ_no + χ_some = 1 exact **by construction** — the identity Appendix C
§2 and Eq. (C1) rest on — rather than as something that happens to hold away from the boundary.
Its only cost is that 1 − σ(x) and σ(−x) differ in the last ulp: worst 2.22e-16, inside the 1e-12
zero band (I5) and invisible at four printed decimals.

A uniform *test* is not achievable anyway: Eq. (A1) mixes one closed region with two open ones, and
one comparison cannot express that. The old uniformity was bought by getting one entry wrong.

## 3. Tasks

- [x] T0 (2026-09-16): checkpoint be47516. The tree carried one uncommitted line in `main.ipynb`
  cell 18, the user's; folded into this change's commit at their direction.
- [x] T1: `audits/2026-09-16-exclusion-complement/acceptance.py`, run **before** applying.
  ACCEPTANCE PASS.
- [x] T2: `apply.py --apply` patched `main.ipynb` cell 5 and `appendix_E.ipynb` cell 2, one site
  each. Writer round-trip verified byte-identical first, so nothing outside the hunk moved. The two
  copies remain IDENTICAL.
- [x] T3: both notebooks re-executed, main first (E3 reads its stored outputs).
- [x] T4: Text cell 6's quoted θ_u\* range corrected, 14946 → 14937 (C6).
- [x] T5: decision I13; F11 corrected in the side-quest record; this record.

## 4. Verification

- Acceptance, before applying: step branch identical to the old function over 3000 shipped
  configurations (K ladder × n ∈ [2, 201] × three utterances); smooth branch within 2.22e-16;
  *no* and *all* bit-identical. At a grid with a node on the threshold: old χ_some = 0 where
  Eq. (A1) requires 1, new χ_some = 1; χ_no + χ_some = 1 exact; Eq. (C1) residual 3.0e-02 → 3.3e-16.
- Acceptance against the **patched** notebooks: same results, and the default network still learns
  θ_u\* = −28.437487, matching the settled value.
- `main.ipynb` 0 errors, 8 figures, 14/14, 249 s. `appendix_E.ipynb` 0 errors, 5 figures, E2 18/18,
  E3 PASS, 672 s. Both within the §5.1 baseline.
- Printed-output diff against be47516: `appendix_E` 0 differing lines; `main` 2, being the one
  θ_u\* value in Code Cell 4's override-threshold table. All 13 figures byte-identical.

## 5. Findings

- **F1 (the fix was not output-neutral, contrary to what was first reported).** The agent told the
  user the change would alter nothing printed, on the strength of a scan that swept θ_L = log(2n − 1)
  for integer n and the K ladder. That scan never covered the explicit θ_L values the notebooks
  pass. `override_threshold(boundaries=(1.0, 2.0, 3.0))` puts **θ_L = 3.0 exactly on node 25** of
  the K = 101 grid — the only such coincidence in either notebook. That row's θ_u\* moved
  14946.06 → 14937.23, stable across the six preceding commits, so the move is the fix and not
  run-to-run noise. **The new value is correct**; the old was computed with χ_some = 0 where
  Eq. (A1) requires 1.
- **F2 (the general lesson).** A static scan for literals is not a reachability test — it gave a
  false all-clear three times here. The authoritative test is a full printed-output diff of both
  notebooks before and after.
- **F3 (noticed, not changed).** The notebooks carry two conventions at the top of the scale:
  `zeta > theta_L` for Eq. (27)'s all-region q-mass, and `zeta >= theta_L` for "the cell of *all*"
  (the mode-position criterion, Code Cell C's *not all*). After I13, 1 − χ_all = {ζ ≥ θ_L} agrees
  with the second. The residual tension is that Eq. (27)'s all-region is strict while its own gloss
  reads "where *all* is true", which is the closed cell. Same class of latent issue, in prose, and
  out of scope here.
- **F4 (a coupling `agent.md` §2 does not list).** Code cell 1 and Code Cell E1 both define
  `exclusion_indicator`, byte-identically. §2's coupling list covers Code Cell 2 ↔ E2 but not this
  one. Worth adding, for the next agent.
- **F5 (a fragility worth the user's attention).** The override table's θ_L = 3.0 boundary sits
  exactly on a grid node, so that row's printed θ_u\* is sensitive to the boundary convention in a
  way the other two rows are not. Whether the boundaries should be nudged off the grid is a question
  for the user, not this change.
