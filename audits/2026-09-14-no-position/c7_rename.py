r"""C7 / B10 wording pass: the four criteria's names, the stance sentence, and no "condition" or
"verdict" (fixed technical compounds kept). Every replacement is asserted exactly once. Scratch."""
import re
import nbformat

ROOT = "/Users/flog/Desktop/predictive coding/"
main = nbformat.read(ROOT + "main.ipynb", as_version=4)
appx = nbformat.read(ROOT + "appendix_E.ipynb", as_version=4)


def patch(cells, pairs):
    for cell in cells:
        text = cell.source
        for old, new in pairs:
            assert text.count(old) == 1, (text.splitlines()[0][:40], old[:80], text.count(old))
            text = text.replace(old, new)
        cell.source = text


STANCE = (r"The reader, in accordance with their own judgement, may take satisfaction of the disjunction, "
          r"the conjunction, either one of the two alone, or even neither criteria as scalar "
          r"strengthening. This notebook takes no position on how the criteria should be interpreted.")

# ---------------------------------------------------------------- table of contents
patch([main.cells[0]], [
    ("9.1 The flat direction: resolved, with a standing condition", "9.1 The flat direction: resolved, with a standing requirement"),
    ("Where both of Part C's conditions hold", "Where both of Part C's q criteria hold"),
])

# ---------------------------------------------------------------- pseudocode
patch([main.cells[3]], [("(optional, conditions how much we care", "(optional, sets how much we care")])

# ---------------------------------------------------------------- Text cell 3
patch([main.cells[4]], [
    ("the exact condition\n   is stated in Appendix B", "the exact requirement\n   is stated in Appendix B"),
    ("condition it needs in the exact form the implementation enforces.", "requirement it needs in the exact form the implementation enforces."),
    ("$\\theta_u^\\ast$ the evaluation's criterion turns out to need.", "$\\theta_u^\\ast$ the evaluation's criteria turn out to need."),
    ("Text cell 4 shows that the criterion it is judged by is\nreached long before", "Text cell 4 shows that the q criteria it reports are\nmet long before"),
    ("the criterion Text cell 4 adopts is met at a", "the q criteria Text cell 4 reports are met at a"),
    ("depend on three conditions:", "depend on three assumptions:"),
    ("that last condition is the one Eq. (22) needs.", "that last assumption is the one Eq. (22) needs."),
    ("9.1 The flat direction: resolved, with a standing condition", "9.1 The flat direction: resolved, with a standing requirement"),
])

# ---------------------------------------------------------------- Code Cell 1 and E1
patch([main.cells[5], appx.cells[2]], [
    ("else. This is the baseline the strengthening conditions of Text cell 4 Part C\n        are measured against.",
     "else. This is the baseline the q shift criterion of Text cell 4 Part C\n        is measured against."),
    ("whose stationarity condition is the quadratic", "whose stationarity equation is the quadratic"),
    ("# necessary part only; the full condition is Appendix B's", "# necessary part only; the full requirement is Appendix B's"),
])

# ---------------------------------------------------------------- Text cell 4
patch([main.cells[6]], [
(r"""form, and we adopt one rather than derive it. Three quantities have to be named first, because the
criterion is a relation between them.""",
 r"""form, and Part C states two criteria for it rather than deriving one. Three quantities have to be
named first, because the criteria are relations between them."""),
("literal listener the criterion names;", "literal listener the q shift criterion names;"),
(r"""**The criterion.** We take scalar strengthening to be the conjunction of two conditions on the
all-region mass under *some*: that
$q_H(\text{all}\mid\textit{some})<q_{\mathrm{lit}}(\text{all}\mid\textit{some})$, the hierarchy
lowering the mass the entry and prior already assign; and that
$q_H(\text{all}\mid\textit{some})<\tfrac12$, the strengthened reading being the majority outcome
and not merely the suppressed alternative. Neither is sufficient alone. The second can hold on
literal conditioning by itself, since the non-all states stand together against the single all
state; the first can hold while *all* remains the most probable single outcome. Writing
$\Delta_{\textit{some}}=P(\text{all-region};q_{\textit{some}})-P(\text{all-region};q_{\mathrm{lit},\textit{some}})$
for the **shift**, the first condition is $\Delta_{\textit{some}}<0$. All of this is a stipulation
about how such an effect would have to show up *in this model*, not a definition of scalar
implicature, and every verdict below is relative to it. Both conditions are stated on the read-out
$q$ of Eq. (12), which is kept for comparison with the probabilistic accounts; the posterior of the
construction itself, the delta at the settled state, is reported beside them in Part D and Text
cell 4b.""",
 r"""**The criteria.** Two criteria are stated on the all-region mass under *some*. The **shift
criterion**, $q_H(\text{all}\mid\textit{some})<q_{\mathrm{lit}}(\text{all}\mid\textit{some})$, is
met when the hierarchy lowers the mass the entry and prior already assign. The **position
criterion**, $q_H(\text{all}\mid\textit{some})<\tfrac12$, is met when the states other than *all*
together hold the majority. The position criterion can be met on literal conditioning by itself,
since the non-all states stand together against the single all state; the shift criterion can be
met while *all* remains the most probable single outcome. """ + STANCE + r""" Writing
$\Delta_{\textit{some}}=P(\text{all-region};q_{\textit{some}})-P(\text{all-region};q_{\mathrm{lit},\textit{some}})$
for the **shift**, the shift criterion is $\Delta_{\textit{some}}<0$. Both criteria are stipulations
about how such an effect could show up *in this model*, not a definition of scalar implicature, and
everything reported below is relative to them. Both are stated on the read-out $q$ of Eq. (12),
which is kept for comparison with the probabilistic accounts, and are called the **q shift
criterion** and the **q position criterion** where the read-out needs naming; the posterior of the
construction itself, the delta at the settled state, is reported beside them in Part D and Text
cell 4b, with a mode shift and a mode position criterion of its own."""),
("**The criterion is not met under the default Gaussian prior.** There",
 "**Under the default Gaussian prior the q shift criterion is not met.** There"),
("so the first condition fails while the second holds\ncomfortably",
 "so the q shift criterion fails while the q position\ncriterion holds comfortably"),
("moves the shift *toward* the\ncriterion without reaching it:", "moves the shift *toward* the\nq shift criterion without meeting it:"),
("the conjunction holds under none**: the second condition holds under each and\nthe first under none.",
 "the conjunction holds under none**: the q position criterion holds under each and\nthe q shift criterion under none."),
("which is why the verdict can be shown in the dynamics", "which is why the conjunction can be shown in the dynamics"),
("*Nor is the first condition, where it is met, specific to* some.", "*Nor is the q shift criterion, where it is met, specific to* some."),
("Whether the verdict for *all* at $\\Lambda=8$", "Whether the result for *all* at $\\Lambda=8$"),
("Two things have to be stated about the row where the first condition is met,",
 "Two things have to be stated about the rows where the q shift criterion is met,"),
("it carries the Gaussian prior away from the criterion,", "it carries the Gaussian prior further from meeting the q shift criterion,"),
("Where the first condition is met it is therefore met *without* a", "Where the q shift criterion is met it is therefore met *without* a"),
("is narrower, and is about the first condition alone:", "is narrower, and is about the q shift criterion alone:"),
("The second condition is met alongside it in all three, $q_H$ holding\n$0.0357$, $0.0413$ and $0.4351$ of the all-region against the half the condition allows, and in all\nthree both conditions are also met off an integrated fixed point.",
 "The q position criterion is met alongside it in all three, $q_H$ holding\n$0.0357$, $0.0413$ and $0.4351$ of the all-region against the half the criterion allows, and in all\nthree both criteria are also met off an integrated fixed point."),
("all-region and the two conditions are all as Part C defines them.", "all-region and the two criteria are all as Part C defines them."),
("the flat condition\nis $\\mathrm{Beta}(1,1)$", "the flat prior\nis $\\mathrm{Beta}(1,1)$"),
("how much of it the criterion actually needs.", "how much of it the criteria actually need."),
("**Where each of Part C's two conditions is met.**", "**Where each of Part C's two criteria is met.**"),
("| $\\Delta_{\\textit{some}}$ | first | second |", "| $\\Delta_{\\textit{some}}$ | q shift | q position |"),
("The second condition holds under each, $q_H$ at\nmost $0.1788$, and the first under none,",
 "The q position criterion holds under each, $q_H$ at\nmost $0.1788$, and the q shift criterion under none,"),
("priors meet both conditions and two meet the second alone.", "priors meet both criteria and two meet the q position criterion alone."),
("violation of the second condition nor a mode of either belief. It is not a violation because the\ncondition is on mass:",
 "violation of the q position criterion nor a mode of either belief. It is not a violation because the\ncriterion is on mass:"),
("priors, against the half the condition allows.", "priors, against the half the criterion allows."),
("still leaves the second condition met.", "still leaves the q position criterion met."),
(r"""and the peak of $\varphi_S^\ast$ lies above it on the scale, nearer the cell than the prior's.""",
 r"""and the peak of $\varphi_S^\ast$ lies above it on the scale, nearer the cell than the prior's.

**The delta read-out's two criteria.** Under *some*, Code Cell 2 also prints two criteria on the
peak of $\varphi_S^\ast$, which it calls the mode: the **mode shift criterion**, met when the mode
lies below the $\ell_0$ peak on the scale, and the **mode position criterion**, met when the mode
lies outside the cell of *all*. They are the counterparts on the delta read-out of the q shift and
q position criteria and are not assumed to agree with them, so the cell prints the four side by
side, with how often each pair agrees. As with the q criteria, this notebook takes no position on
how they should be interpreted."""),
("**How much of $\\theta_u^\\ast$ the criterion needs.**", "**How much of $\\theta_u^\\ast$ the criteria need.**"),
("across Text cell 6's $33$ both-condition cells", "across the $33$ cells of Text cell 6 where both q criteria are met"),
("$\\theta_u$ its verdict needs**", "$\\theta_u$ the conjunction needs**"),
("both conditions met in each. So Part C's verdict is demonstrated in the dynamics.",
 "both criteria met in each. So what Part C reports is demonstrated in the dynamics."),
("What the closed form carries is the verdict *at $\\theta_u^\\ast$*", "What the closed form carries is the result *at $\\theta_u^\\ast$*"),
])

# ---------------------------------------------------------------- Code Cell 2 and E2
patch([main.cells[7], appx.cells[3]], [
("# Part C asks whether it produces a scalar implicature, under the criterion Text\n# cell 4 Part C adopts; that cell states what the reading commits us to.",
 "# Part C reports the q shift and q position criteria of Text cell 4 Part C, on which a\n# reader may judge whether it produces a scalar implicature; no position is taken on them."),
("whose stationarity condition is the quadratic", "whose stationarity equation is the quadratic"),
('''    A scalar implicature for "some" would move q-mass AWAY from the region where
    "all" is true. The measured quantity is therefore the change in P(s in all-region)
    between q_lit and the full network, the shift of Eq. (37), and Text cell 4 Part C's
    criterion is the conjunction of two conditions: the shift for "some" is NEGATIVE
    (first), and the full network's P(all-region | "some") is below 1/2 (second).''',
 '''    The measured quantity is the change in P(s in all-region) between q_lit and the
    full network, the shift of Eq. (37). Text cell 4 Part C reports two criteria on it
    and takes no position on them (B10): the q shift criterion, that the shift for
    "some" is negative, and the q position criterion, that the full network's
    P(all-region | "some") is below 1/2.'''),
('''        print(f"  first condition, shift for \\"some\\" < 0:        "
              f"{'met' if first else 'NOT met'} ({shift:+.4f})")
        print(f"  second condition, P(all-region | \\"some\\") < 1/2: "
              f"{'met' if second else 'NOT met'} ({upper:.4f})")
        print(f"  Under the criterion of Text cell 4 Part C, the conjunction, the "
              f"criterion is {'met' if first and second else 'NOT met'}:")
        print(f"  under \\"some\\" the settled belief holds {abs(shift):.4f} "
              f"{'less' if shift < 0 else 'MORE'} all-region q-mass than q_lit.")
        print("  Whether the criterion is met is a measurement; what meeting it commits")
        print("  the model to is argued in Text cell 4 Part C, not here. Note that the")
        print("  same criterion is met by other utterances too (see the shift column")
        print("  above), and that its sign is prior-dependent (Code Cell 2b).")''',
 '''        print(f"  q shift criterion, shift for \\"some\\" < 0:              "
              f"{'met' if first else 'NOT met'} ({shift:+.4f})")
        print(f"  q position criterion, P(all-region | \\"some\\") < 1/2:    "
              f"{'met' if second else 'NOT met'} ({upper:.4f})")
        print(f"  both q criteria: {'met' if first and second else 'NOT met'}; "
              f"under \\"some\\" the settled belief holds {abs(shift):.4f} "
              f"{'less' if shift < 0 else 'MORE'} all-region q-mass than q_lit.")
        print("  Whether the criteria are met is a measurement, and this notebook takes no")
        print("  position on how they should be interpreted (Text cell 4 Part C). Note that")
        print("  the q shift criterion is met by other utterances too (see the shift column")
        print("  above), and that the shift's sign is prior-dependent (Code Cell 2b).")'''),
('f"the first condition of Text cell 4 Part C, and "', 'f"the q shift criterion of Text cell 4 Part C, and "'),
('print("  the criterion: raising |theta_u| amplifies the span(B) component of")',
 'print("  the q shift criterion: raising |theta_u| amplifies the span(B) component of")'),
("The flat condition is a literal Uniform(0, 1) over the proportion, not a", "The flat prior is a literal Uniform(0, 1) over the proportion, not a"),
('print("  (a scalar implicature for \\"some\\" requires a NEGATIVE shift)")',
 'print("  (the q shift criterion for \\"some\\" is a NEGATIVE shift)")'),
('''        print(f"  First condition (shift for \\"some\\" < 0) met under {len(first)} of "
              f"{len(rows)} priors: " + (", ".join(first) if first else "none") + ".")
        print(f"  Conjunction (also P(all-region | \\"some\\") < 1/2) met under {len(both)}: "
              + (", ".join(both) if both else "none") + ".")
        if 0 < len(first) < len(rows) or 0 < len(both) < len(rows):
            print("  Whether it is met is therefore NOT a property of the model alone; it")
            print("  depends on the prior the model is run against, which is a fact about the")
            print("  criterion as much as about the model. Text cell 4 Part C reads this.")''',
 '''        print(f"  q shift criterion (shift for \\"some\\" < 0) met under {len(first)} of "
              f"{len(rows)} priors: " + (", ".join(first) if first else "none") + ".")
        print(f"  both q criteria (also P(all-region | \\"some\\") < 1/2) met under {len(both)}: "
              + (", ".join(both) if both else "none") + ".")
        if 0 < len(first) < len(rows) or 0 < len(both) < len(rows):
            print("  Whether they are met is therefore NOT a property of the model alone; it")
            print("  depends on the prior the model is run against, which is a fact about the")
            print("  criteria as much as about the model. Text cell 4 Part C reports this.")'''),
("# The block ends with each both-conditions configuration run end to end with nothing in",
 "# The block ends with each configuration meeting both q criteria run end to end with nothing in"),
('''"""Text cell 4 Part C's two conditions for "some", as one record.''',
 '''"""Text cell 4 Part C's q shift and q position criteria for "some", as one record.'''),
('''at which BOTH conditions hold.''', '''at which BOTH q criteria are met.'''),
('''print("  the maximizer of F~, that costs hours. Part C's verdict does not wait for it.")''',
 '''print("  the maximizer of F~, that costs hours. What Part C reports does not wait for it.")'''),
("# ---- each both-conditions configuration, end to end, nothing in closed form ----",
 "# ---- each configuration meeting both q criteria, end to end, nothing in closed form ----"),
('''print(f"    both conditions met by the integrated run: {scored['both']}; "''',
 '''print(f"    both q criteria met by the integrated run: {scored['both']}; "'''),
('''    # === the delta read-out's two criteria under "some" (B8), beside the two conditions on q ===
    # Each is reported as a measurement, and neither set is read as a verdict (B10). The mode is
    # the grid node where the field is largest; torch.argmax takes the first such node, so the
    # gap between the two largest nodes of phi_S* is printed, and a tie would show as 0.
    print("  THE DELTA READ-OUT'S TWO CRITERIA UNDER \\"some\\" (B8), BESIDE THE TWO CONDITIONS ON q (Part C)")
    print("    (a) mode(phi_S*) - mode(ell_0) < 0;  (b) mode(phi_S*) outside the cell of \\"all\\", zeta < theta_L;")
    print("    first: shift for \\"some\\" < 0;  second: P(all-region | \\"some\\") < 1/2.  Modes in s.")
    print(f"    {'prior':<13}{'theta_u':<24}{'ell_0':>8}{'ell_0-phi_L':>12}{'phi_S*':>8}{'shift':>9}"
          f"{'(a)':>5}{'(b)':>5}{'both':>6}{'first':>7}{'second':>8}{'both':>6}{'top-2 gap':>11}")''',
 '''    # === the mode shift and mode position criteria under "some" (B8), beside the q criteria ===
    # Each is reported as a measurement, and no position is taken on how to read them (B10).
    # The mode is the grid node where the field is largest; torch.argmax takes the first such
    # node, so the gap between the two largest nodes of phi_S* is printed, and a tie shows as 0.
    print("  THE MODE SHIFT AND MODE POSITION CRITERIA UNDER \\"some\\" (B8), BESIDE THE q SHIFT AND q POSITION")
    print("  CRITERIA (Part C)")
    print("    mode shift: mode(phi_S*) - mode(ell_0) < 0;  mode position: mode(phi_S*) outside the cell of")
    print("    \\"all\\", zeta < theta_L;  q shift: shift for \\"some\\" < 0;  q position: P(all-region | \\"some\\") < 1/2.")
    print("    Modes in s.")
    print(f"    {'prior':<13}{'theta_u':<24}{'ell_0':>8}{'ell_0-phi_L':>12}{'phi_S*':>8}{'shift':>9}"
          f"{'mode shift':>11}{'mode position':>14}{'both':>6}{'q shift':>8}{'q position':>11}"
          f"{'both':>6}{'top-2 gap':>11}")'''),
('''              f"{at_s(k) - at_s(k0):>+9.4f}{yes(a):>5}{yes(b):>5}{yes(a and b):>6}{yes(first):>7}"
              f"{yes(second):>8}{yes(first and second):>6}{float(largest[0] - largest[1]):>11.1e}")''',
 '''              f"{at_s(k) - at_s(k0):>+9.4f}{yes(a):>11}{yes(b):>14}{yes(a and b):>6}{yes(first):>8}"
              f"{yes(second):>11}{yes(first and second):>6}{float(largest[0] - largest[1]):>11.1e}")'''),
('''    print(f"    over these {counted} rows: (a) holds in {tally['a']}, (b) in {tally['b']}, both in "
          f"{tally['delta_both']}; on q the first condition holds in {tally['first']}, the second in "
          f"{tally['second']}, both in {tally['q_both']}")
    print(f"    (a) and the first condition agree in {tally['agree_first']} of {counted} rows, (b) and the "
          f"second in {tally['agree_second']}, the two conjunctions in {tally['agree_both']}")''',
 '''    print(f"    over these {counted} rows: the mode shift criterion is met in {tally['a']}, the mode "
          f"position criterion in {tally['b']}, both in {tally['delta_both']}; the q shift criterion in "
          f"{tally['first']}, the q position criterion in {tally['second']}, both in {tally['q_both']}")
    print(f"    the mode and q shift criteria agree in {tally['agree_first']} of {counted} rows, the mode "
          f"and q position criteria in {tally['agree_second']}, the two conjunctions in "
          f"{tally['agree_both']}")'''),
])

# ---------------------------------------------------------------- Text cell 4b
patch([main.cells[8]], [
("$\\theta_u$ control, the all-region and the two conditions are as Part C defines them",
 "$\\theta_u$ control, the all-region and the two criteria are as Part C defines them"),
("entry excludes, and those columns of Part D measure the prior overriding the entry as well as the\ncriterion.",
 "entry excludes, and those columns of Part D measure the prior overriding the entry as well as the\ncriteria."),
("**Where each of Part C's two conditions is met, at $\\Lambda=512$.**", "**Where each of Part C's two criteria is met, at $\\Lambda=512$.**"),
("| $\\Delta_{\\textit{some}}$ | first | second |", "| $\\Delta_{\\textit{some}}$ | q shift | q position |"),
("priors. The second condition holds under all five and the first under those three, so no prior\nmeets the first alone.",
 "priors. The q position criterion holds under all five and the q shift criterion under those three,\nso no prior meets the q shift criterion alone."),
("and moves the Gaussian and $\\mathrm{Beta}(1,3)$ priors away from the criterion,",
 "and moves the Gaussian and $\\mathrm{Beta}(1,3)$ priors further from meeting the q shift criterion,"),
(r"""Under the flat and $\mathrm{Beta}(3,1)$ priors, then, the read-out $q$ meets both of Part C's
conditions while the peak of the delta read-out lies above the $\ell_0$ peak; under the delta-like
prior that peak lies below it.""",
 r"""Under the flat and $\mathrm{Beta}(3,1)$ priors, then, both q criteria are met while the mode shift
criterion is not, the peak of the delta read-out lying above the $\ell_0$ peak; under the delta-like
prior that peak lies below it, and all four criteria are met."""),
])

# ---------------------------------------------------------------- Code Cell 2b and E2b
patch([main.cells[9], appx.cells[4]], [
('''          f"{'max leak':>11}{'first':>7}{'second':>8}")''', '''          f"{'max leak':>11}{'q shift':>9}{'q position':>12}")'''),
('''                  f"{leak:>11.1e}{('met' if some['shift'] < 0 else '-'):>7}"
                  f"{('met' if some['full_upper'] < 0.5 else '-'):>8}")''',
 '''                  f"{leak:>11.1e}{('met' if some['shift'] < 0 else '-'):>9}"
                  f"{('met' if some['full_upper'] < 0.5 else '-'):>12}")'''),
('''    print("    (first: shift for \\"some\\" < 0; second: P(all-region | \\"some\\") < 1/2. The")
    print("     delta-like prior has no row at Part D's Lambda, since it needs this one.)")''',
 '''    print("    (q shift criterion: shift for \\"some\\" < 0; q position criterion: P(all-region | \\"some\\") < 1/2.")
    print("     The delta-like prior has no row at Part D's Lambda, since it needs this one.)")'''),
('print("  AWAY from the criterion. At the same Lambda the delta-like row reads "',
 'print("  AWAY from the q shift criterion. At the same Lambda the delta-like row reads "'),
])

# ---------------------------------------------------------------- Text cell 5
patch([main.cells[10]], [
("and the stationarity condition Eq. (B2).", "and the stationarity equation Eq. (B2)."),
("The criterion adopted in Text cell 4 Part C is not a contrast between", "The q shift criterion reported in Text cell 4 Part C is not a contrast between"),
("which is a condition on **direction**", "which is a requirement on **direction**"),
("That is Appendix B's condition made visible:", "That is Appendix B's requirement made visible:"),
])

# ---------------------------------------------------------------- Code Cell 3
patch([main.cells[11]], [
("which is a condition on\n       DIRECTION", "which is a requirement on\n       DIRECTION"),
('print(f"  condition <mu_u, sum_y c_y> != 0 fails on the two rays at")', 'print(f"  requirement <mu_u, sum_y c_y> != 0 fails on the two rays at")'),
])

# ---------------------------------------------------------------- Text cell 6
patch([main.cells[12]], [
("the flat condition of Part D.", "the flat prior of Part D."),
("Part C's first condition is\n$\\Delta_{\\textit{some}}<0$.", "Part C's q shift criterion is\n$\\Delta_{\\textit{some}}<0$."),
("Part C's second condition,\n$P(\\text{all-region};q_y)<\\tfrac12$,", "Part C's q position criterion,\n$P(\\text{all-region};q_y)<\\tfrac12$,"),
("not a second criterion, since the criterion is stipulated on the raw", "not a second criterion, since the q shift criterion is stated on the raw"),
("Both are mapped, and both verdicts are\nreported below.", "Both are mapped, and both readings are\nreported below."),
("The cells where the criterion is met are not among them", "The cells where both q criteria are met are not among them"),
("the much smaller $\\theta_u$ the criterion itself needs", "the much smaller $\\theta_u$ the conjunction itself needs"),
("Under the first of Part C's two conditions\nan implicature", "Under Part C's q shift criterion\nan implicature"),
("and Part C's first condition is met over most of the plane.", "and Part C's q shift criterion is met over most of the plane."),
("So Part C's first condition is met over most of this plane", "So Part C's q shift criterion is met over most of this plane"),
("Where both of Part C's conditions hold", "Where both of Part C's q criteria hold"),
("The second condition, $q_H(\\text{all}\\mid\\textit{some})<\\tfrac12$, is a statement",
 "The q position criterion, $q_H(\\text{all}\\mid\\textit{some})<\\tfrac12$, is a statement"),
("**both conditions hold together in $33$**", "**both q criteria hold together in $33$**"),
("Each condition\nholds above a floor in $\\Lambda$ and keeps holding above it. The first condition's floor **falls**",
 "Each criterion\nholds above a floor in $\\Lambda$ and keeps holding above it. The q shift criterion's floor **falls**"),
("The second condition's floor **rises**", "The q position criterion's floor **rises**"),
("which clears the second condition's\nfloor of $2$ at $\\alpha\\le8$ but the first condition's floor only at $\\alpha\\ge128$;",
 "which clears the q position criterion's\nfloor of $2$ at $\\alpha\\le8$ but the q shift criterion's floor only at $\\alpha\\ge128$;"),
("and meets the second condition alone.", "and meets the q position criterion alone."),
("the flat prior meets the first condition's floor of $512$ and clears the second's,",
 "the flat prior meets the q shift criterion's floor of $512$ and clears the q position criterion's,"),
("the delta-like prior clears the first condition's floor of $16$ and meets\nthe second's of $512$.",
 "the delta-like prior clears the q shift criterion's floor of $16$ and meets\nthe q position criterion's of $512$."),
("at which both conditions hold runs from", "at which both q criteria hold runs from"),
("the $\\theta_u$ its verdict needs**", "the $\\theta_u$ its conjunction needs**"),
])

# ---------------------------------------------------------------- Code Cell 4
patch([main.cells[13]], [
('''Part C's first condition is
    shift(some) < 0 and its second P(all-region | "some") < 1/2. A condition's floor''',
 '''Part C's q shift criterion is
    shift(some) < 0 and its q position criterion P(all-region | "some") < 1/2. A criterion's floor'''),
("    def floor(condition, i):", "    def floor(holds, i):"),
("            if not condition[i, j]:", "            if not holds[i, j]:"),
('''print("  raw shift for \\"some\\" (Part C's first condition):")''', '''print("  raw shift for \\"some\\" (Part C's q shift criterion):")'''),
('''print(f"    second condition, P(all-region | \\"some\\") < 1/2, in {int(second.sum())} "
              f"cells; both conditions in {int(both.sum())}"''',
 '''print(f"    q position criterion, P(all-region | \\"some\\") < 1/2, in {int(second.sum())} "
              f"cells; both q criteria in {int(both.sum())}"'''),
('''print("    floor in Lambda by alpha (first / second condition):")''', '''print("    floor in Lambda by alpha (q shift / q position criterion):")'''),
])

# ---------------------------------------------------------------- Appendices A, B, C; Code Cell A
patch([main.cells[14]], [("fixed-point condition in $\\theta_L$", "fixed-point equation in $\\theta_L$")])
patch([main.cells[15]], [
    ('            verdict = "accepted"', '            outcome = "accepted"'),
    ('            verdict = "rejected"', '            outcome = "rejected"'),
    ("{verdict} by the constructor", "{outcome} by the constructor"),
])
patch([main.cells[16]], [
    ("That is the condition for a single utterance.", "That is the stationarity equation for a single utterance."),
    ("the baseline the criterion is measured against.", "the baseline the q shift criterion is measured against."),
    ("Text cell 4 shows that the criterion it is judged by is met at a", "Text cell 4 shows that the q criteria it reports are met at a"),
    ("**The standing condition, stated exactly.**", "**The standing requirement, stated exactly.**"),
    ("nonzero by exactly the standing condition above", "nonzero by exactly the standing requirement above"),
])
patch([main.cells[18]], [
    ("since every condition below is a", "since every requirement below is a"),
    ("Two conditions can be asked of $B$, and they are not the same condition:", "Two requirements can be asked of $B$, and they are not the same requirement:"),
    ("This model's verdict is that the gap", "This model's answer is that the gap"),
])

# ---------------------------------------------------------------- Appendix E: E3 names, E.3
patch([appx.cells[5]], [
    ("verdict = (", "passed = ("),
    ("strong_verdict = not (strong_deleted", "strong_passed = not (strong_deleted"),
    ("{'PASS' if verdict else 'FAIL'}", "{'PASS' if passed else 'FAIL'}"),
    ("{'PASS' if strong_verdict else 'FAIL'}", "{'PASS' if strong_passed else 'FAIL'}"),
    ("if not (verdict and strong_verdict):", "if not (passed and strong_passed):"),
])
patch([appx.cells[8]], [("the standing condition $\\langle", "the standing requirement $\\langle")])

assert main.cells[9].source == appx.cells[4].source.split("\n", 5)[5]      # E2b still mirrors 2b
nbformat.write(main, ROOT + "main.ipynb")
nbformat.write(appx, ROOT + "appendix_E.ipynb")
print("C7 wording applied")

# ---------------------------------------------------------------- what is left
left = re.compile(r"condition|verdict|first condition|second condition|the first under|the second alone|the second's|\(a\)|\(b\)", re.I)
for f, nb in (("main.ipynb", main), ("appendix_E.ipynb", appx)):
    for i, c in enumerate(nb.cells):
        for n, l in enumerate(c.source.splitlines(), 1):
            if left.search(l):
                print(f"  left {f} cell {i} line {n}: {l.strip()[:150]}")
