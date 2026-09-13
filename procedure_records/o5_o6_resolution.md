# O5 and O6: the sign sentence and the relay bound

Working record for two open decisions of `decisions.md`, on the pattern of
`theta_u_learned_reach.md`.

## 0. Instructions (the user's, verbatim, 2026-09-13)

> O5: choose "both signs reversed, +28.4375";
> O6: Keep ≤ and state the exception for now. State in prose what it requires to Make the bound
> strict (τr < τε) as in option 2. Add comment at the 'infer' code concisely explaining how this is
> different from the text definitions and why.

## 1. Decisions

- **O5 (user).** Appendix B's counterfactual is both signs reversed, c_y → −c_y, whose maximizer is
  +28.4375 (Code Cell B prints it). The sign of θ_u\* is then read against the relative sign of ℓ₀
  and φ_L.
- **O6 (user).** Eq. (E6) keeps τ_r ≤ τ_ε. The prose states the exception (at equality F is monotone
  under *some* only) and what a strict bound would require. `infer`'s strict guard stays, with a
  comment saying how it differs from Eq. (E6) and why.

## 2. Tasks

Record format: `[x] Tn (date): what changed; acceptance result; commit`.

- [x] T0 (2026-09-13): checkpoint. The notebooks and `decisions.md` are unchanged since b1236f2. The
  uncommitted move of the change records into `procedure_records/` is the user's and is not folded
  into this change.
- [x] T1 (2026-09-13): code. Code Cell E1, `infer`: a comment at the `tau_relay >= tau_error`
  guard; the guard's error message reads "as slow as" in place of "slower than", since equality is
  refused. Acceptance: the cell parses; no stored output can change (a comment, and a message no
  run raises). Notebooks not re-executed.
- [x] T2 (2026-09-13): prose, applied by a script requiring each edit to land exactly once.
  Acceptance: every edit landed once; both notebooks validate.
- [x] T3 (2026-09-13): `decisions.md`: O5 and O6 settled by the user; a dated finding under A11; commit 235cb59 (T1-T3).

## 3. Findings

- **F1 (continuity of the strict bound).** τ_r < τ_ε excludes only the equality: `infer` still
  admits a relay arbitrarily close to τ_ε, and no relay strictly between the instantaneous one and
  τ_ε has been integrated under *no* or *all*. A strict bound carries monotonicity only with a
  measured margin, which is what the new E.1 paragraph states.
- **F2.** E.1 quoted the relay bound at θ_u\* as τ_r < 3.08e-4, stricter than Eq. (E6). Now ≤.
- **F3 (noticed, not changed).** Code Cell E1's `infer` docstring still quotes the roundoff floor as
  "about 8e-11 to 1.6e-10"; the prose was corrected to 8.2e-11 to 2.4e-10 under E7 (F7 of
  `e4_e7_sourcing.md`). Code comments were outside E7's scope.
- **F4 (noticed, not changed).** Both notebooks fail `nbformat.validate` at b1236f2 already: cells
  carry `id` fields while the files declare `nbformat_minor` 0. Jupyter and nbclient run them; T2's
  acceptance was therefore that each edit landed once and the JSON loads, not strict validation.

## 4. Prose sites

- `main.ipynb` cell 14 (Appendix B): "were the two signs reversed … +22.578" → "were both signs
  reversed … +28.437".
- `appendix_E.ipynb` cell 1 (E.1): the bound at θ_u\* written with ≤; a paragraph after the
  slow-relay counts stating the exception and what a strict bound requires.
- `appendix_E.ipynb` cell 6 (E.2): "suffices at every θ_u tested" narrowed to stability, and the
  non-monotone transient extended to a relay at the error units' own speed under *no* and *all*.
- `appendix_E.ipynb` cell 7 (E.3, the Text cell 3 §7 row): the same narrowing.
