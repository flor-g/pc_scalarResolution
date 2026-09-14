"""After execution: compare the notebooks' stored outputs with the outside-notebook test,
count figures per cell, check the ToC links resolve, and read appendix E's verdicts (scratch)."""
import json, pathlib, re, subprocess

S = pathlib.Path(__file__).parent
ROOT = pathlib.Path("/Users/flog/Desktop/predictive coding")


def stream(cell):
    return "".join("".join(o.get("text", [])) for o in cell["outputs"] if o.get("output_type") == "stream")


def norm(text):
    return [re.sub(r"\s+", " ", l).strip() for l in text.splitlines()
            if l.strip() and not l.strip().startswith("cost:")]


def figures(cell):
    return sum(1 for o in cell.get("outputs", []) if "image/png" in o.get("data", {}))


main = json.loads((ROOT / "main.ipynb").read_text())
cells = main["cells"]
print("main.ipynb cells:", len(cells))
code = {"".join(c["source"]).split("\n")[0]: i for i, c in enumerate(cells) if c["cell_type"] == "code"}
for header, i in code.items():
    print(f"  cell {i:>2}: {header[:70]:<70} figures {figures(cells[i])}, "
          f"errors {sum(o.get('output_type') == 'error' for o in cells[i]['outputs'])}")

i2 = next(i for h, i in code.items() if h.startswith("# === Code Cell 2:"))
i2b = next(i for h, i in code.items() if h.startswith("# === Code Cell 2b:"))
for label, i, test in (("2", i2, "test_out_2.txt"), ("2b", i2b, "test_out_2b.txt")):
    stored, expected = norm(stream(cells[i])), norm((S / test).read_text())
    same = stored == expected
    print(f"Code Cell {label} stored output equals the outside-notebook test: {same} "
          f"({len(stored)} lines against {len(expected)})")
    if not same:
        import difflib
        for l in list(difflib.unified_diff(expected, stored, lineterm="", n=0))[:40]:
            print("   ", l)

checks = re.search(r"(\d+)/(\d+) passed", stream(cells[i2]))
print("specification checks:", checks.group(0) if checks else "not found")

# every ToC link resolves to an anchor
markdown = "\n".join("".join(c["source"]) for c in cells if c["cell_type"] == "markdown")
anchors = set(re.findall(r'<a id="([^"]+)"', markdown))
links = re.findall(r"\]\(#([^)]+)\)", "".join(cells[0]["source"]))
missing = [l for l in links if l not in anchors]
print(f"ToC: {len(links)} links, {len(anchors)} anchors, unresolved: {missing}")
toc_rows = [int(m) for m in re.findall(r"^\| (\d+) \|", "".join(cells[0]["source"]), re.M)]
print("ToC cell indices consistent with the notebook:",
      all(0 < n < len(cells) for n in toc_rows) and toc_rows == sorted(toc_rows)
      and toc_rows[-1] == len(cells) - 1)

appendix = json.loads((ROOT / "appendix_E.ipynb").read_text())
print("appendix_E.ipynb cells:", len(appendix["cells"]))
for i, c in enumerate(appendix["cells"]):
    if c["cell_type"] != "code":
        continue
    text = stream(c)
    head = "".join(c["source"]).split("\n")[0]
    passed = re.findall(r"(\d+/\d+ passed)", text)
    verdicts = [l.strip() for l in text.splitlines() if re.match(r"\s*(PASS|FAIL)\s+(the relay|nor in)", l)]
    print(f"  cell {i}: {head[:60]:<60} figures {figures(c)}, errors "
          f"{sum(o.get('output_type') == 'error' for o in c['outputs'])}, {passed} {verdicts}")
    if "Code Cell E3" in head:
        print("   ", "\n    ".join(l for l in text.splitlines() if "lines " in l))
