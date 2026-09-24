"""T7 (record §7) plus C8's naming: decisions.md B8/C8/E14/I12, revisions.md §8, Code Cell C and Appendix C §8."""
import re, nbformat


def replace_once(text, old, new):
    assert text.count(old) == 1, (text.count(old), old[:70])
    return text.replace(old, new)


# ---------------------------------------------------------------- decisions.md
path = "decisions.md"
doc = open(path).read()

doc = replace_once(doc, """    Beta(3,1) priors the q conjunction holds and criterion (a) does not (peaks move up to s = 0.917).
""", """    Beta(3,1) priors the q conjunction holds and criterion (a) does not (peaks move up to s = 0.917).
  - **2026-09-15. The criteria are printed, and so is the mechanism under them.**
    - T1 (2718404): Code Cells 2 and 2b, mirrored in E2 and E2b, print per row the modes of ℓ₀,
      ℓ₀ − φ_L and φ_S\\* in s, the mode shift in s and in grid steps, the two mode criteria beside the
      two q criteria, the gap between the two largest nodes, and the counts and pairwise agreement. At
      Λ = 8 the pairs agree in 4 of 4 rows; at Λ = 512 the shift criteria agree in 4 of 8 and the
      position criteria in 8 of 8.
    - T2 (5ee04a6): Code Cell 4 prints the same criteria over the 121 cells: 67, 59 and 13 against q's
      74, 59 and 33, the 35 cells where a shift criterion and its counterpart disagree, the four
      unmoved modes, the 5.6e-5 smallest gap, and the floors under both read-outs.
    - T3 (27a4122, prose 5a7bc8e): Code Cell C prints the tilt/width split, the plane counts and
      Eq. (24)'s halving, reported in the new Appendix C §8.
    - T6 (af971c4): Text cell 4 Parts C and D, Text cell 4b and Text cell 6 carry the criteria in
      prose, under C7's names and B10's stance.
    - Every number in this entry's *Evidence* and in the F4 and F5 findings above is therefore printed
      by a cell, and the numbers Q2 and Q6 of `thesis_outline/revisions.md` quote are sourced (C6).
""")

doc = replace_once(doc, """### C6. Every number the prose quotes is computed by explicit code and printed by a code cell""",
"""### C8. "Control" names a manipulation of the model; an algebraic one is a counterfactual manipulation
- Status: Settled
- Decided by: user (2026-09-15)
- Decision: both kinds are controls in nature. The notebooks keep **control** for a manipulation of
  the model, a configuration the network is actually run in with a parameter held off its learned
  value: Part C's θ_u control, Text cell 5's θ_u = 1 tables, the μ_u settings, the m = 1 basis. A
  quantity built by algebra on settled fields, which no setting of the model produces, is a
  **counterfactual manipulation**: Appendix C §8's two single-part fields, the tempered control plus
  the tilt part alone and plus the width part alone.
- Theoretical reason: none. The distinction is for the reader (the user: "for the sake of not
  confusing the reader").
- Implementational reason: `agent.md` §3.3 keeps q_lit, the tempered control and the model apart, and
  B4 lists the retained fixed-θ_u controls in `procedure_records/theta_u_learned_reach.md` §5.C. A
  field that is the tempered control plus part of the utility field would take a third name
  confusable with the second, and would enter that list without matching any run.
- Bogacz status: naming convention; no operation.
- Depends on it: Appendix C §8's prose, Code Cell C's printed block, E14's classing.
- Evidence: no setting of θ_u, Λ, μ_u or B makes the network settle on either field; each is
  φ_S\\*(θ_u = 0) plus one column's share of Eq. (23)'s utility field.

### C6. Every number the prose quotes is computed by explicit code and printed by a code cell""")

doc = replace_once(doc, """- Depends on it: agent.md §1 (cell maps) and §2 (couplings 1, 2, 7).
""", """- Depends on it: agent.md §1 (cell maps) and §2 (couplings 1, 2, 7).

### I12. The mode is the first node of an argmax, and the gap is printed
- Status: Settled
- Decided by: agent, confirmed by user (2026-09-15)
- Decision: the mode of a field is `torch.argmax`, which takes the **first** node when two nodes tie.
  Every block that reports a mode also prints the gap between the two largest values of φ_S\\*, so a
  tie would print as 0. Observed smallest: 3.4e-3 over Part D's rows at Λ = 8, 7.8e-3 over Code Cell
  2b's rows, 5.6e-5 over the plane.
- Theoretical reason: none. B7 defines the mode as the largest node and is silent on ties.
- Implementational reason: a tie has to resolve somehow, and B8's mode shift criterion is a strict
  node comparison, so in a tie the tie-break would decide the criterion. Printing the gap makes the
  rule's reach visible instead of assumed.
- Bogacz status: statistic of the delta read-out (his Eq. 34); no counterpart in the tutorial.
- Depends on it: B8's two criteria; Code Cells 2, 2b, 4 and C.
- Evidence: the gaps printed in those cells; `audits/2026-09-13-delta-criteria/output.txt`.
""")

doc = replace_once(doc, """all-region masses of q_lit, the tempered control and the full network beside the tempering/utility
split, in Code Cells 2 and 2b (and E2, E2b).""", """all-region masses of q_lit, the tempered control and the full network beside the tempering/utility
split, in Code Cells 2 and 2b (and E2, E2b).

**E14. The quantities T1-T3 added (2026-09-15).** Classed by the agent; the naming of the two
single-part fields is the user's (C8).
- Code Cells 2 and 2b (and E2, E2b): the modes in s, the mode shift in s and in grid steps k\\* − k₀,
  the two mode criteria and their conjunction, the gap between the two largest nodes, and the counts
  and agreement: class (b), statistics of the delta read-out (B7, B8), defined in Text cell 4 Part D.
- The grid spacing printed in that block's legend: class (d), read from the grid of I6 rather than
  stored as a constant.
- Code Cell 4, `lambda_alpha_sweep`: per cell under *some*, the mode nodes of φ_S\\*, ℓ₀ and ℓ₀ − φ_L,
  the modes of φ_S\\* and ℓ₀ in s, whether φ_S\\*'s mode lies outside the cell of *all*, and the
  smallest top-2 gap of the three fields: class (b). `plane_summary`'s counts, agreement, the 35-cell
  table and the six floors: class (b). Signs are read with I5's zero band.
- Code Cell C, `utility_split_report` (Appendix C §8): the tilt and width coefficients of the utility
  field, the span-B residual, the two slopes at the tempered control's mode, the modes and all-region
  masses of the four fields, the plane counts, the distances from c/2, the Gram and exact-form
  errors, and the limit field's mode and criteria: class (b), statistics of Eqs. (15), (16), (23) and
  (24) defined in Appendix C §8.
- The two single-part fields, the tempered control plus tilt alone and plus width alone:
  **counterfactual manipulations** (C8), controls in nature but not manipulations of the model, since
  no setting of θ_u, Λ or μ_u produces either. Their printed numbers are class (b). B4's list of
  retained fixed-θ_u controls is unaffected, since neither field is an evaluation the model is run in.
- Appendix C §1 writes every projection per unit Λ; §8's coefficients are the exception, each at its
  configuration's own Λ and θ_u\\*, and §8 says so.
- Code Cell 2b's own quantities stay under E12, and E13's masses are unchanged.""")

open(path, "w").write(doc)

# ---------------------------------------------------------------- revisions.md
path = "thesis_outline/revisions.md"
doc = open(path).read()

doc = replace_once(doc, """| §5.2's re-examination: contributions, leaks, loadings, illustrative θ\\* | `audits/2026-09-13-scale-structure/output.txt` (an audit script, not a cell) |""",
"""| §5.2's re-examination: contributions, leaks, loadings, illustrative θ\\* | `audits/2026-09-13-scale-structure/output.txt` (an audit script, not a cell) |
| Q2's Part D and Λ = 512 rows: the modes, the mode shift in s and in grid steps, the two mode criteria | `main.ipynb` Code Cells 2 and 2b, the mode criteria block |
| Q2's plane counts (67, 59, 13 against 74, 59, 33), the 35 disagreeing cells, the four unmoved modes, the 5.6e-5 gap, and the V under both read-outs | Code Cell 4, `plane_summary` |
| Q6's tilt/width split, the 50 and 67 up/down counts, Eq. (24)'s halving and the limit field | Code Cell C, `utility_split_report`; Appendix C §8 |

(2026-09-15: R14's and R15's code tasks, T1-T3 and T6 of
`procedure_records/delta_criteria_printing.md`, are closed; T7 and T8 remain.)""")

doc = replace_once(doc, """Cell 2's definitions, and reproduces Code Cell 2's Part D rows and Code Cell 4's counts (second
condition 59, both 33). Everything is under *some*, each configuration at its own θ\\*. **Nothing in
this subsection is printed by a notebook cell yet** (see "Printing" below).""",
"""Cell 2's definitions, and reproduces Code Cell 2's Part D rows and Code Cell 4's counts (second
condition 59, both 33). Everything is under *some*, each configuration at its own θ\\*. **2026-09-15:
every number in this subsection is printed**, by Code Cells 2, 2b and 4.""")

doc = replace_once(doc, """**Preliminary result** (record F4; `audits/2026-09-13-delta-criteria/mode_mechanism_output.txt`; not
printed by any cell). **The two movements share a direction, not a source.**""",
"""**Preliminary result** (record F4; printed by Code Cell C and reported in Appendix C §8 since
2026-09-15). **The two movements share a direction, not a source.**""")

open(path, "w").write(doc)

# ---------------------------------------------------------------- main.ipynb: C8's naming
nb = nbformat.read("main.ipynb", as_version=4)
code_c, app_c = nb.cells[19], nb.cells[18]

code_c.source = replace_once(code_c.source, """# odd column (tilt) and one on its even column (width). Each part is added alone to the tempered
# control; those two fields are counterfactual, not states of the network. The limit field is the
# right-hand side of Eq. (24).""",
"""# odd column (tilt) and one on its even column (width). Each part is added alone to the tempered
# control: a counterfactual manipulation of the settled field (Sec. 8), not a manipulation of the
# model, since no setting of theta_u, Lambda or mu_u produces either field. The limit field is the
# right-hand side of Eq. (24).""")

code_c.source = replace_once(code_c.source, """    print("  the tempered control (theta_u = 0); they are counterfactual fields, not states of the network.")""",
"""    print("  the tempered control (theta_u = 0): counterfactual manipulations of the settled field, which no")
    print("  setting of the model produces.")""")
compile(code_c.source, "code_cell_c", "exec")

app_c.source = replace_once(app_c.source, """Those two fields are constructed for the comparison; the network does not settle on
either.""",
"""Adding one part alone is a **counterfactual manipulation** of the settled field and not a
manipulation of the model: no setting of $\\theta_u$, $\\Lambda$ or $\\mu_u$ makes the network settle
on either field, and *control* is kept for a configuration the model is run in, such as the
$\\theta_u$ control itself.""")
assert "\n\n\n" not in app_c.source and not re.search(r"[ \t]+\n", app_c.source)

nbformat.write(nb, "main.ipynb")
print("applied: decisions.md (B8 finding, C8, I12, E14), revisions.md (§8 rows, two stale lines),",
      "main.ipynb (Code Cell C comment and printed lines, Appendix C §8)")
