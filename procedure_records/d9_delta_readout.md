# D9: q as a comparison read-out, and the delta read-out reported

Working record for D9 of `decisions.md`, on the pattern of `theta_u_learned_reach.md`.

## 0. Instructions (the user's, verbatim, 2026-09-13)

> Here is my take on D9:
>
> 1. we have constructed the read-out q mainly to find a parallel interpretation to the RSA
> literature. Nevertheless, the framework that our model is built upon is quite different from the
> foundational assumptions that standard RSA make. Hence, any inclusion of the read-out q is purely
> for comparison and conventional purpose. There is nothing in our architecture or the construction
> that dictates this form of read-out.
> 2. The posterior read-out that is more native to the construction is delta phi_s*, which
> corresponds with Bogacz's implementation. Therefore, in the evaluation section, after the q graphs
> for different priors, we should also print and report the table that you gave me above.
> Accordingly, include in the corresponding text cell a guide of how to read this table. Cross refer
> to the definition of Voronoi Cell in the appendix and note that the posterior of all four
> different priors fall outside the Voronoi Cell of [[all]].

Answers to the agent's questions (verbatim):

> Voronoi note: "with literal baseline. But don't call it literal baseline there, call it ell_0
> peak."
> Point 1 scope: "Framing sites only (Recommended)" (rewrite Eq. (12)'s paragraph, the Reporting
> statistics opening, and the q_lit 'posterior' naming; Parts C-D keep their verdicts in q, with one
> sentence that the conditions are stated on the comparison read-out).
> Table: "Exactly as given".
> Placement: "End of Code Cell 2 (Recommended)" (printed after the three q figures in Code Cell 2,
> mirrored into E2, both notebooks re-run; the guide in Text cell 4 Part D, after the figure
> discussion, linking to Appendix A).

## 1. Decisions

- **DEC1 (user).** q (Eq. 12) is a read-out constructed for comparison with the RSA literature;
  nothing in the architecture dictates it. The posterior native to the construction is the delta at
  the settled state, Bogacz's Eq. (34).
- **DEC2 (user).** Part D reports the delta read-out table after the q figures, with a reading guide
  in Text cell 4 Part D that cites Appendix A's Voronoi cell and states the ℓ₀ peak beside the peak
  of φ_S\* under *some*.
- **DEC3 (user).** Framing sites only: Eq. (12)'s paragraph, the Reporting statistics opening, the
  q_lit naming; the Part C/D verdicts stay in q with one sentence on their status.
- **DEC4 (agent, pending user confirmation).** C6 requires the ℓ₀ peaks and the boundary check the
  note quotes to be printed; they print as two blocks below the table, which stays as given.
- **DEC5 (agent, pending user confirmation).** q_lit's "untempered literal posterior" becomes
  "untempered literal listener".

## 2. Tasks

Record format: `[x] Tn (date): what changed; acceptance result; commit`.

- [x] T0 (2026-09-13): checkpoint. HEAD e03268a; the notebooks, `decisions.md` and `agent.md` are
  unchanged since. `thesis_outline/` is staged by the user and is not part of this change; commits
  here name their paths with `git commit --`.
- [x] T1 (2026-09-13): code. `delta_readout_report` in Code Cell 2, defined before RUN and called
  after the figures; the same text inserted into E2 (checked identical); E3 replays it as
  `delta_readout_report(probe_network, realizability_report(probe_network))`. Acceptance: run
  outside the notebook on code cell 1 and Code Cell 2's definitions, it printed the table of the
  scratch computation exactly (5.5 s).
- [x] T2 (2026-09-13): executed main, then appendix_E. main 0 errors, 6 figures, 14/14, 245 s;
  appendix_E 0 errors, 3 figures, E2 18/18, E3 PASS (260 lines identical, up from 221; 0 deleted,
  1 changed, 4 inserted), 672 s. The table printed after the figures matches T1's.
- [x] T3 (2026-09-13): prose against the outputs (§4), 10 edits in Text cells 3, 4 and 6. Acceptance:
  each landed once; the 25 decimals the guide quotes are all in main's executed Code Cell 2 output.
  Markdown only, so no stored output changes and E3 is unaffected.
- [x] T4 (2026-09-13): `decisions.md`: A13 status, A16 and B7 added, dated findings under B1 and C3,
  D9 resolved and its register row. `agent.md`: §2 item 7 (E3 replay), §5.1 baseline.
- [ ] T5: commit.

## 3. Findings

- **F1 (the peak is the mode of q).** Placing the delta on the scale of s means reading its peak,
  the grid node where φ_S\* is largest. The exponential and normalizer of Eq. (12) do not move it,
  so it is also the mode of q. The delta read-out departs from q in what needs the normalizer
  (masses, E[s]), not in the peak.
- **F2 (ℓ₀ peak).** Under *some* the peak of φ_S\* lies outside the cell of *all* under all five
  priors. Under the four at Λ = 8 the ℓ₀ peak already does (s = 0.50, 0.50, 0.25, 0.75), and the
  learned peak sits above it (0.59, 0.67, 0.33, 0.84). Under the delta-like row the ℓ₀ peak is
  inside (0.985) and the learned peak outside (0.947). Under *some* φ_L vanishes at the ℓ₀ peak of
  every prior, so ℓ₀ − φ_L peaks there too.
- **F3 (boundary).** The delta-like row's peak is one node below θ_L. On grids of 201, 401 and 801
  nodes it stays outside, the gap to the best node inside shrinking (−0.114, −0.053, −0.031) and
  the peak moving toward s = 0.95.
- **F4 (own cell).** The learned peak leaves the uttered entry's own cell under *all* with
  Beta(1,3) (s = 0.25) and under *no* with Beta(3,1) (s = 0.75).
- **F5 (E3 replay).** E3 replays Code Cell 2's printing calls by name, so a new printing call in
  Code Cell 2 must be added to E3's replay or E3 reports its lines as deleted.

## 4. Prose sites

Applied by `prose_d9.py` (scratch), which writes nothing unless every edit lands once and every
decimal the guide quotes is in main's executed Code Cell 2 output.

- Text cell 3 §4 item 5 (Eq. 12): the delta at the settled state is the construction's posterior
  (Bogacz §3, Eq. 34); q is read for comparison with the RSA literature; nothing in the architecture
  dictates Eq. (12).
- Text cell 3 §9 caveats: "read-out (10)" → "(12)" (stale number); "A parametric posterior" →
  "A parametric read-out".
- Text cell 4 Part C: q_lit "untempered literal posterior" → "untempered literal listener" (DEC5); one
  sentence after the criterion: both conditions are stated on q, the delta is reported in Part D.
- Text cell 4 Part D, after the figure discussion: the reading guide (table columns; the peak is
  also q's mode; φ_u\* comparable only at shared θ_u; the ℓ₀ peak against the cell of *all*, citing
  Appendix A; the boundary check; F4's two rows noted with position reserved).
- Text cell 4 Reporting statistics: the opening no longer says the model's output is q; "Only
  q-mass is a statement about what the model concluded" → "about the read-out q".
- Text cell 6: "the untempered literal posterior" → "untempered".
