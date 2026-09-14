# O7: renaming senses 1 and 3 of "realizability"

Working record for O7 of `decisions.md`, on the pattern of `theta_u_learned_reach.md`.

## 0. Instructions (the user's, verbatim, 2026-09-13)

> With that said, let's address O7 first. Would you propose a renaming for senses 1 and 3?

> Sense 1 renaming approved. For sense 3 maybe say "this map collapses contrasts between exclusion
> sets"? Reads easier this way.

## 1. Decisions

- **DEC1 (agent's proposal, approved by the user, 2026-09-13).** Sense 1 (Appendix B: at θ\* both
  residuals vanish and F = 0) is renamed **exact solvability**. Appendix B's own preceding sentence
  already says θ v_p = u "is solvable". "Exact fit" was not used, because in the outline "fit" means
  fitting a model to data.
- **DEC2 (user, 2026-09-13).** Sense 3 (Appendix C §7) takes no term. It is phrased as a projection
  that "collapses a contrast between exclusion sets", which matches existing usage (Text cell 5
  Part A; Appendix C's table). The agent named the subject as "$m=2$" and "$m=1$" rather than "this
  map", following that table. "Expressible" and "representable" were avoided (decisions.md O7).
- Sense 2 (the cost sense) is untouched, and O7 stays open for it.

## 2. Tasks

- [x] T0 (2026-09-13): checkpoint. Clean tree at HEAD 07f4eae.
- [x] T1 (2026-09-13): edits to main.ipynb, applied by script. Each replacement was asserted to occur
  exactly once. Afterwards no "realiz" is left in cells 14–16, and the diff is 7 lines.
  - Appendix B (cell 14): "it is **realizability** that identifies θ" → "it is **exact
    solvability** that identifies θ"; "is not realizability but a nonzero" → "is not exact
    solvability but a nonzero".
  - Code Cell B (cell 15): header `REALIZABILITY AT theta_u*` → `EXACT SOLVABILITY AT theta_u*`.
  - Appendix C §7 (cell 16): "Yet **no exclusion set realizes it**" → "Yet **$m=2$ collapses no
    contrast between exclusion sets**". "the direction $m=1$ misses *is* realizable, being the
    middle interval … an exclusion-set difference, which is why $m=1$ actually fails" → "the
    direction $m=1$ misses is the middle interval …, a difference of two exclusion sets, so $m=1$
    *does* collapse a contrast, the one between *some* and *all*, and that is why $m=1$ actually
    fails."
- [x] T2 (2026-09-13): executed main, then appendix_E (agent.md §5.1).
  - main.ipynb: RUNNER OK, 0 errors, 6 figures, 244 s.
  - appendix_E.ipynb: RUNNER OK, 0 errors, 3 figures, 684 s.
  - Stored outputs against HEAD: main cell 15 differs in the one header line only; main cell 7 and
    appendix_E cell 3 differ only in wall-clock `cost:` lines; every other output line is identical.
    Read off the new outputs: main 14/14 specification checks passed; appendix_E E2 18/18 passed,
    and E3 PASS, "the relay changes no reported quantity: 260 lines identical, 0 deleted".
- [x] T3 (2026-09-13): `decisions.md` O7 finding; `thesis_outline/revisions.md` §7 note.

## 3. Findings

- **F1.** Sense 3's new wording is exact, not a paraphrase. Every non-constant {−1,0,1} combination of
  the intervals is χ_A − χ_B for two exclusion sets A and B, and it lies in the projection's unseen
  subspace iff A and B are sent to the same point. So "no combination lies in the unseen subspace"
  and "no contrast between exclusion sets collapses" are the same statement. The trivial pair (empty
  set, whole scale) is excluded by "non-constant" and by §7's "nonempty proper unions".
- **F2.** Bogacz (2017) uses neither "realizable" nor "solvable", so no citation depends on sense 1's
  old name.
