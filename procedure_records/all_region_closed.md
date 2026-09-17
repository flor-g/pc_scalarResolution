# Eq. (27)'s all-region becomes closed

Working record for **O11**, settled by the user on 2026-09-17. It arose from finding F3 of
`exclusion_complement_fix.md`.

## 0. Instructions (the user's, verbatim, 2026-09-17)

> For 3, the formula needs to be changed. Can you inspect the scope of that change before
> implementing?

and, on the two judgment calls the scope raised:

> for 1, we will fix this redundancy later, record and don't do anything about it yet. For 2, leave
> it. Now go ahead and implement the changes.

Item 1 is the all-region / cell-of-*all* redundancy, recorded as **O12**. Item 2 is the comment at
Code Cell 2b line 25, left as written.

## 1. The disagreement, and which side was wrong

Text cell 4 defined P(all-region) over the **open** R = {ζ > θ_L} while glossing it "where *all* is
true". *all* excludes E_all = {ζ < θ_L} (Eq. A1), so it is true on the **closed** {ζ ≥ θ_L}. The
formula and its own gloss disagreed at the single node ζ = θ_L. Everything else in the notebook
already took the closed form: the cell of *all*, Code Cell C's χ_not all, P(no-region). The user
ruled that the formula was the wrong side.

## 2. Scope, as inspected before implementing

| What | Count | Where |
|---|---|---|
| mask sites | **23** | main cells 7 (7), 9 (2), 11 (1), 13 (2), 19 (2); appendix_E cells 3 (7), 4 (2) |
| printed labels | **3** | main c7 and E c3 column header; main c19 legend |
| prose | **2** | Text cell 4: the Eq. (27) definition, and "the region ζ ≥ θ_L is s ≥ 0.95" |
| must not change | **11** | the cell-of-*all* masks, already `>=`; plus `lower_region`, already `<=` |

Mirror pairs moved together: main cell 7 ↔ E2, main cell 9 ↔ E2b (I11). Cells 11, 13 and 19 are not
mirrored.

## 3. Tasks

- [x] T0 (2026-09-17): checkpoint e10f002, tree clean.
- [x] T1: `audits/2026-09-17-all-region-closed/acceptance.py`, run **before** applying. PASS: the
  site counts match the scope, and the open and closed masks agree on all 55 (θ_L, K) combinations
  the notebooks use — while differing, as expected, at θ_L = 3.0 on K = 101.
- [x] T2: `apply.py --apply`, every edit count-asserted, writer round-trip checked byte-identical
  first. 14 + 9 masks, 2 + 1 labels, 2 prose.
- [x] T3: both notebooks re-executed, main first.
- [x] T4: O11 settled; B2 given a dated finding; O12 recorded; this record.
- [x] T5 (2026-09-17): O12 resolved, on the user's instruction. Prose: Text cell 4 Part C states the
  identity once; Part D refers to Part C instead of re-deriving the cell. Code: both `upper_region`
  and `inside` kept, with a comment at the canonical declaration of `upper_region` (Code Cell 2's
  `demonstrate`, mirrored in E2). Acceptance: every code cell compiles; the only source changes are
  markdown in cell 6 (+7 −5) and three comment lines in each notebook; stored outputs byte-identical.
  **Notebooks not re-executed** — the sole code change is a comment, which cannot move any output
  (the precedent is T1 of `o5_o6_resolution.md`).

## 4. Verification

- Source diff against e10f002: **18 changed lines in main** (14 masks, 2 labels, 2 prose) and
  **10 in appendix_E** (9 masks, 1 label). Nothing else moved; `lower_region` and the Code Cell 2b
  comment are untouched.
- `main.ipynb` 0 errors, 8 figures, 14/14, 240 s. `appendix_E.ipynb` 0 errors, 5 figures, E2 18/18,
  E3 PASS, 703 s. Both within the §5.1 baseline.
- Printed-output diff against e10f002: **no numeric change anywhere**. The only differing lines are
  the 5 printed occurrences of the two relabelled headers (main cells 7, 9, 19; appendix_E cells 3,
  4). All 13 figures byte-identical.

## 5. Findings

- **F1 (the change is inert, and why).** No grid node lands on +θ_L for any θ_L the notebooks use —
  log 19, the explicit 2.9444, and log(2n − 1) across n — at any K in the ladder. The one
  node-on-threshold configuration, `override_threshold`'s θ_L = 3.0, takes its leak from χ_no and
  never computes an all-region mass. So the q position criterion reads identically in every
  configuration actually run; only its *definition at the boundary* changed.
- **F2 (a prediction corrected).** The scope said 3 printed label lines would change; 5 did. The
  column header is defined once, in Code Cell 2, but `delta_readout_report` is called from both
  Code Cell 2 and Code Cell 2b, so one source line prints in two cells. Source sites and printed
  occurrences are not the same count.
- **F3 (a third checker written with assumed expectations).** The post-apply check counted every
  `X.zeta >= X.theta_L` and compared against the number of *new* sites, so the cell-of-*all* masks
  that were already `>=` read as a MISMATCH. The edit was correct; the checker was not. This is the
  same failure as F0 of `exclusion_complement_fix.md` and the inverted acceptance expectations
  there. **The form that works is to count the pre-change state and assert new = old + delta**, which
  is what reconciled it. Prefer that to asserting an absolute number.
- **F4 (a gating bug in the runner).** The verification block and the two notebook runs were
  sequenced with `;`, so execution proceeded despite the checker reporting FAIL. Harmless here only
  because the edit was right. Use `&&` so a failed check stops the run.
- **F5 (the redundancy this creates).** The all-region and the cell of *all* are now the same set
  with two names and two implementations. Recorded as **O12** at the user's direction, then settled
  by them the same day: resolved in prose, retained in code behind a comment. See T5.
- **F6 (a fifth checker caught a real ambiguity, for once).** The comment insertion first anchored on
  the pair `proportion = logistic(net.zeta)` + `upper_region = ...`, which occurs **twice** in Code
  Cell 2 — in `demonstrate` and in `base_prior_sweep`. The assertion refused to patch rather than
  guessing, and the anchor was moved to the enclosing `def demonstrate(`. Unlike F3 and F4, this is
  the failure mode working as intended: assert the site count, never patch on a non-unique anchor.
