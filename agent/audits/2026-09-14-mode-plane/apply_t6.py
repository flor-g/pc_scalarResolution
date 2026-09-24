"""T6: the approved prose into Text cells 4, 4b and 6 (record §6, E1-E6)."""
import re, nbformat

nb = nbformat.read("main.ipynb", as_version=4)
tc4, tc4b, tc6 = nb.cells[6], nb.cells[8], nb.cells[12]
edits = []

# E1: Part C, the criteria paragraph
edits.append((tc4, """criterion of its own. Eq. (37) is this shift, written out where
Text cell 6 maps it.""", """criterion of its own. The two pairs are not assumed to agree, and they do not always: over the
plane of Text cell 6 the two position criteria agree in all $121$ cells and the two shift criteria
disagree in $35$. Eq. (37) is this shift, written out where Text cell 6 maps it."""))

# E6b: Part C, the first "delta-like"
edits.append((tc4, """and the delta-like prior concentrated on the all-region, which needs that $\\Lambda$""",
              """and the delta-like prior concentrated on the all-region, a $\\mathrm{Beta}(64,1)$
approaching a point mass at $s=1$, which needs that $\\Lambda$"""))

# E3: Part D, the spike paragraph (R15)
edits.append((tc4, """The movement of the mode up the
scale between the two is what the positive $\\Delta_{\\textit{some}}$ records.""",
              """The movement of the mode up the scale between $q_{\\mathrm{lit}}$ and the full network is the
utility level's, since the $\\theta_u$ control, $\\tfrac12(\\ell_0-\\varphi_L)$, keeps its maximum where
$q_{\\mathrm{lit}}$ has it; Appendix C §8 splits the utility field into the part that moves the mode
and the part that lowers the all-region mass. What $\\Delta_{\\textit{some}}$ records is not that
movement: the shift under these two priors, $+0.0295$ and $+0.0421$, is all-region mass that the
tempering adds to $q_{\\mathrm{lit}}$ and that the utility level then fails to take away, as the
paragraph above reports."""))

# E6a: Part D, why the read-out is called the delta read-out
edits.append((tc4, """each prior and utterance at that prior's $\\theta_u^\\ast$. Code Cell 2b prints""",
              """each prior and utterance at that prior's $\\theta_u^\\ast$. The name is the delta *distribution* of
Text cell 3 §4 item 5, the point mass at $(\\varphi_S^\\ast,\\varphi_u^\\ast)$, and the same word in the
*delta-like* prior names a $\\mathrm{Beta}(\\alpha,1)$ approaching a point mass at $s=1$. Neither use
carries any relation to $\\Delta_y$, the shift of Eq. (37). Code Cell 2b prints"""))

# E2: Part D, the delta read-out's two criteria
edits.append((tc4, """**The delta read-out's two criteria.** Under *some*, Code Cell 2 also prints two criteria on the
peak of $\\varphi_S^\\ast$, which it calls the mode: the **mode shift criterion**, met when the mode
lies below the $\\ell_0$ peak on the scale, and the **mode position criterion**, met when the mode
lies outside the cell of *all*. They are the counterparts on the delta read-out of the q shift and
q position criteria and are not assumed to agree with them, so the cell prints the four side by
side, with how often each pair agrees. As with the q criteria, this notebook takes no position on
how they should be interpreted.""",
              """**The delta read-out's two criteria.** Under *some*, Code Cell 2 also prints two criteria on the
peak of $\\varphi_S^\\ast$, which it calls the mode. Writing $k^\\ast$ for the grid node where
$\\varphi_S^\\ast$ is largest and $k_0$ for the node where $\\ell_0$ is, the **mode shift criterion** is

$$k^\\ast<k_0,$$

met when the mode lies below the $\\ell_0$ peak on the scale, and the **mode position criterion** is

$$\\zeta_{k^\\ast}<\\theta_L,$$

met when the mode lies outside the cell of *all*. Both are statistics of the delta read-out, as the
q criteria are of $q$, and neither is a model quantity. Being comparisons of grid nodes, they resolve
a movement of the mode to one node; a tie would go to the first node, and the cell prints the gap
between the two largest values of $\\varphi_S^\\ast$, which is never zero in these rows. The cell
prints the mode shift in $s$ and in grid steps, $k^\\ast-k_0$. The grid is uniform in $\\zeta$ while
$s$ compresses toward the ends of the scale, so the steps, multiplied by the grid spacing of $0.12$,
give the shift in $\\zeta$. The mode criteria are the counterparts on the delta read-out of the q
shift and q position criteria and are not assumed to agree with them, so the cell prints the four
side by side, with how often each pair agrees. As with the q criteria, this notebook takes no
position on how they should be interpreted. At $\\Lambda=8$ the mode lies $3$, $6$, $3$ and $5$ grid
steps above the $\\ell_0$ peak under the Gaussian, flat, $\\mathrm{Beta}(1,3)$ and
$\\mathrm{Beta}(3,1)$ priors, so the mode shift criterion is met under none and the mode position
criterion under all four, and each agrees with its q counterpart in all four rows."""))

# E4: Text cell 4b, the delta read-out at Lambda = 512
edits.append((tc4b, """We note the difference and reserve our position on it. Under *no*
and *all* the peak sits at""",
              """We note the difference and reserve our position on it.

Over the eight rows Code Cell 2b prints, the five at $\\theta_u^\\ast$ and the three realizable, the
mode position criterion is met in all eight and the mode shift criterion in two, the delta-like
prior's; the mode and q shift criteria agree in four of the eight. In grid steps the mode lies $19$,
$20$, $27$ and $11$ nodes above the $\\ell_0$ peak under the four diffuse priors and $11$ below it
under the delta-like prior. The flat row is the plane's cell $(1,512)$, one of the $21$ cells
Appendix C §8 tabulates where the q shift criterion is met and the mode shift criterion is not.

Under *no*
and *all* the peak sits at"""))

# E5: Text cell 6, the conjunction section
edits.append((tc6, """4, *Integration cost and conditioning*).

<a id="code4\"""",
              """4, *Integration cost and conditioning*).

**The same plane under the delta read-out.** Code Cell 4 also reads the mode shift and mode position
criteria of Text cell 4 Part D off every cell. The mode position criterion holds in the same $59$
cells as the q position criterion. The mode shift criterion holds in $67$ cells against the q shift
criterion's $74$, and the two disagree in $35$: the q shift criterion alone is met in $21$, all at
$\\alpha\\le16$, and the mode shift criterion alone in $14$, which are ten cells of the saturated
$\\alpha=1024$ row and $(32,16)$, $(64,2)$, $(64,4)$ and $(64,8)$. Both mode criteria hold together in
$13$ cells, every one of them inside the band of $33$, so the two conjunctions part in $20$ cells,
all of them met under q alone.

Under the delta read-out the band keeps its right arm and loses its left. The mode position
criterion's floor is the q position criterion's at every $\\alpha$. The mode shift criterion is never
met at $\\alpha\\le8$; from $\\alpha=16$ its floor is $256$, then $16$ at $\\alpha=32$, then $2$ from
$\\alpha=64$ on. The floor of both mode criteria is therefore absent at $\\alpha\\le8$ and reads $256$,
$256$, $512$ and $1024$ at $\\alpha=16$, $32$, $64$ and $128$, against the q conjunction's $64$,
$256$, $512$ and $1024$. The right arm, set by the position criteria, is shared from $\\alpha=32$; the
left arm, where the q shift criterion's floor falls as the prior sharpens, exists only under q.
Appendix C §8 measures what the mode does there. Every cell where the mode moves up has the tempered
control's mode at $s\\le0.9405$, and every cell where it moves down has it at $s\\ge0.9405$; at
$\\alpha=1$, $2$, $4$ and $8$ the $\\ell_0$ peak, which is the tempered control's mode, sits at
$s=0.5000$, $0.6726$, $0.8085$ and $0.8849$.

<a id="code4\""""))

added = []
for cell, old, new in edits:
    assert cell.source.count(old) == 1, ("anchor not unique or missing", old[:70])
    cell.source = cell.source.replace(old, new)
    added.append(new)
for cell in (tc4, tc4b, tc6):
    assert "\n\n\n" not in cell.source and not re.search(r"[ \t]+\n", cell.source), "spacing"
nbformat.write(nb, "main.ipynb")

record = open("procedure_records/delta_criteria_printing.md").read()
draft = record[record.index("## 6. Draft for review: T6 prose"):]
flat = lambda t: re.sub(r"\s+", " ", t).strip()
draft_flat = flat("\n".join(l[2:] if l.startswith("> ") else l for l in draft.splitlines()))
for new in added:
    for sentence in [s for s in flat(new).split(". ") if len(s) > 60][:3]:
        if sentence not in draft_flat:
            print("NOT IN THE RECORD DRAFT:", sentence[:90])
text = "\n".join(c.source for c in nb.cells if c.cell_type == "markdown")
anchors = re.findall(r'<a id="([^"]+)" name="\1"></a>', text)
links = re.findall(r"\]\(#([^)]+)\)", nb.cells[0].source)
print("anchors", len(anchors), "| ToC links", len(links), "unresolved", [l for l in links if l not in anchors])
print("'condition'/'verdict' in the added text:", re.findall(r"\b(condition|verdict)\w*", " ".join(added), re.I))
