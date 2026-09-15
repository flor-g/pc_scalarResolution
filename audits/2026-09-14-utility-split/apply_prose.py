"""Insert the approved Appendix C §8 (record §5), renumber §8 -> §9, re-scope its first sentence, add the ToC row."""
import re, nbformat
record = open("procedure_records/delta_criteria_printing.md").read()
start = record.index("> ### 8. Which part of the utility field moves the mode")
end = record.index("> Modes here are grid nodes")
end = record.index("\n", end)
block = [l[2:] if l.startswith("> ") else ("" if l == ">" else l) for l in record[start:end].splitlines()]
assert all(not l.startswith(">") for l in block)
section = "\n".join(block).replace("### 8. Which part", '### <a id="appc-8" name="appc-8"></a>8. Which part', 1)
nb = nbformat.read("main.ipynb", as_version=4)
cell = nb.cells[18]
old_heading = '### <a id="appc-8" name="appc-8"></a>8. What this appendix does not settle'
assert cell.source.count(old_heading) == 1
old_first = "Everything above concerns separation and spanning. It does not address"
assert cell.source.count(old_first) == 1
cell.source = cell.source.replace(old_heading, section + "\n\n" + old_heading.replace("appc-8", "appc-9").replace(">8. ", ">9. "))
cell.source = cell.source.replace(old_first, "Sections 1–7 concern separation and spanning. They do not address")
toc = nb.cells[0]
old_row = "|  | &emsp;[8. What this appendix does not settle](#appc-8) |  |"
assert toc.source.count(old_row) == 1
toc.source = toc.source.replace(old_row, "|  | &emsp;[8. Which part of the utility field moves the mode](#appc-8) |  |\n"
                                "|  | &emsp;[9. What this appendix does not settle](#appc-9) |  |")
for c in (cell, toc):
    assert "\n\n\n" not in c.source and not re.search(r"[ \t]+\n", c.source)
nbformat.write(nb, "main.ipynb")
# links
text = "\n".join(c.source for c in nb.cells if c.cell_type == "markdown")
anchors = re.findall(r'<a id="([^"]+)" name="\1"></a>', text)
links = re.findall(r"\]\(#([^)]+)\)", toc.source)
print("anchors", len(anchors), "duplicates", len(anchors) - len(set(anchors)),
      "| ToC links", len(links), "unresolved", [l for l in links if l not in anchors])
print("condition/verdict in cell 18:", re.findall(r"\b(condition|verdict)\w*", cell.source, re.I))
print("dashes as punctuation in the new section:", re.findall(r" — | -- ", section))
