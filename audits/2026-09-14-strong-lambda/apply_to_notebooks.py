"""Apply the new Code Cell 2 and Code Cell 2b to main.ipynb and mirror both into appendix_E.ipynb.

Reads both notebooks at commit a202cdb, so it is safe to re-run. Outputs of changed cells are
cleared; the notebooks are executed afterwards (agent.md §5.1)."""
import difflib, json, pathlib, re, subprocess
import nbformat

S = pathlib.Path(__file__).parent
ROOT = pathlib.Path("/Users/flog/Desktop/predictive coding")


def at_head(path):
    text = subprocess.run(["git", "show", f"a202cdb:{path}"], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout
    return nbformat.reads(text, as_version=4)


cell2 = (S / "new_cell2.py").read_text()
cell2b = (S / "new_cell2b.py").read_text()

# ============================== main.ipynb ==============================
main = at_head("main.ipynb")
old_cell2 = main.cells[7].source
assert old_cell2.startswith("# === Code Cell 2: EVALUATION")
assert main.cells[8].source.startswith("## <a id=\"tc5\"")
main.cells[7].source = cell2
main.cells[7].outputs = []
main.cells[7].execution_count = None

text4b = nbformat.v4.new_markdown_cell(
    '## <a id="tc4b" name="tc4b"></a>Text cell 4b: Part D at a strong $\\Lambda$\n'
    "\n"
    "Code Cell 2b repeats the evaluations of Part D with $\\Lambda=512$ for every base world prior\n"
    "and every utterance, each configuration at its own learned $\\theta_u^\\ast$, and it carries the\n"
    "delta-like prior, which needs that $\\Lambda$. The beliefs compared, the $\\theta_u$ control, the\n"
    "all-region and the two conditions are as Part C defines them, and the delta read-out is as\n"
    "Part D defines it.\n"
    "\n"
    '<a id="code2b" name="code2b"></a>'
)
code2b = nbformat.v4.new_code_cell(cell2b)
main.cells[8:8] = [text4b, code2b]

# table of contents: shift every cell index from 8 on by two, then add the two rows
toc = main.cells[0].source.split("\n")
shifted = []
for row in toc:
    match = re.match(r"^\| (\d+) \|(.*)$", row)
    if match and int(match.group(1)) >= 8:
        row = f"| {int(match.group(1)) + 2} |{match.group(2)}"
    shifted.append(row)
anchor = next(i for i, row in enumerate(shifted) if "(#code2)" in row)
shifted[anchor + 1:anchor + 1] = [
    "| 8 | [**Text cell 4b.** Part D at a strong $\\Lambda$](#tc4b) |  |",
    "| 9 | [**Code cell 2b.** Part D's evaluations with every prior at $\\Lambda=512$. "
    "**Evaluation**](#code2b) |  |",
]
main.cells[0].source = "\n".join(shifted)
nbformat.write(main, ROOT / "main.ipynb")

# ============================== appendix_E.ipynb ==============================
appendix = at_head("appendix_E.ipynb")
old_e2 = appendix.cells[3].source
assert old_e2.startswith("# === Code Cell E2: EVALUATION ===")

# E2 = its header, then main's Code Cell 2 with the relay checks inserted where they were
old_main, old_mirror = old_cell2.split("\n"), old_e2.split("\n")
header, checks, anchor_line = None, None, None
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old_main, old_mirror,
                                                   autojunk=False).get_opcodes():
    if tag == "insert" and i1 == 0:
        header = old_mirror[j1:j2]
    elif tag == "insert":
        assert checks is None
        checks, anchor_line = old_mirror[j1:j2], old_main[i1 - 1]
    elif tag == "replace":
        # the one comment E2 had corrected, which now lives in Code Cell 2b
        assert "Code Cell 3 is built around" in "".join(old_main[i1:i2])
new_main = cell2.split("\n")
assert new_main.count(anchor_line) == 1
k = new_main.index(anchor_line) + 1
new_mirror = header + new_main[:k] + checks + new_main[k:]
appendix.cells[3].source = "\n".join(new_mirror)
appendix.cells[3].outputs = []

# check the mirror: exactly the two insertions against main
ops = [op for op in difflib.SequenceMatcher(None, new_main, new_mirror, autojunk=False).get_opcodes()
       if op[0] != "equal"]
assert [op[0] for op in ops] == ["insert", "insert"], ops

e2b = nbformat.v4.new_code_cell(
    "# === Code Cell E2b: EVALUATION AT A STRONG LAMBDA ===\n"
    "#\n"
    "# Code Cell 2b of main.ipynb, unchanged. Code Cell E3 runs its sequence again with the\n"
    "# output captured and requires every line to match what main.ipynb stored.\n"
    "\n" + cell2b
)

e3 = (S / "new_e3.py").read_text()
old_e3 = appendix.cells[4].source
assert old_e3.startswith("# === Code Cell E3")
appendix.cells[4].source = e3
appendix.cells[4].outputs = []

old_e4 = appendix.cells[5].source
assert old_e4.startswith("# === Code Cell E4")
e4 = old_e4
for before, after in (
    ("# Two things: the bound a relay inherits from the timescale commitment under each prior of\n"
     "# Part D, and what a relay SLOWER",
     "# Two things: the bound a relay inherits from the timescale commitment under each prior of\n"
     "# Part D and the delta-like prior of Code Cell E2b, and what a relay SLOWER"),
    ("relay_bound_report(evaluation_network)\n",
     "relay_bound_report(evaluation_network, {**part_d_priors(), **delta_like_row()})\n"),
):
    assert e4.count(before) == 1, before
    e4 = e4.replace(before, after)
appendix.cells[5].source = e4
appendix.cells[5].outputs = []
appendix.cells[4:4] = [e2b]
nbformat.write(appendix, ROOT / "appendix_E.ipynb")

print("main.ipynb:", len(main.cells), "cells; appendix_E.ipynb:", len(appendix.cells), "cells")
print("E2 mirror: header", len(header), "lines, relay checks", len(checks), "lines, after:", anchor_line.strip())
