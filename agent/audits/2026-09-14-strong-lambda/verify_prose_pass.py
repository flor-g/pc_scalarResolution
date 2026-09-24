"""After re-execution for the prose pass: output diffs against 8aaf9ff, E3 verdicts, figures,
ToC links, and every decimal in the changed markdown looked up in the executed outputs. Scratch."""
import difflib, json, pathlib, re, subprocess

ROOT = pathlib.Path("/Users/flog/Desktop/predictive coding")


def cells_at(rev, path):
    if rev is None:
        return json.loads((ROOT / path).read_text())["cells"]
    return json.loads(subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True,
                                     text=True, check=True).stdout)["cells"]


def stream(cell):
    return "".join("".join(o.get("text", [])) for o in cell.get("outputs", []) if o.get("output_type") == "stream")


def norm(text):
    return [re.sub(r"\s+", " ", l).strip() for l in text.splitlines()
            if l.strip() and not l.strip().startswith("cost:")]


report = []
for path in ("main.ipynb", "appendix_E.ipynb"):
    old, new = cells_at("8aaf9ff", path), cells_at(None, path)
    assert len(old) == len(new)
    figures = sum(1 for c in new for o in c.get("outputs", []) if "image/png" in o.get("data", {}))
    errors = sum(1 for c in new for o in c.get("outputs", []) if o.get("output_type") == "error")
    print(f"{path}: {len(new)} cells, figures {figures}, errors {errors}")
    for i, (a, b) in enumerate(zip(old, new)):
        if a["cell_type"] == "code":
            if norm(stream(a)) != norm(stream(b)):
                print(f"  code cell {i} ({''.join(b['source']).splitlines()[0][:50]}) output lines changed:")
                for l in difflib.unified_diff(norm(stream(a)), norm(stream(b)), lineterm="", n=0):
                    if not l.startswith(("---", "+++", "@@")):
                        print("     ", l)
        elif "".join(a["source"]) != "".join(b["source"]):
            report.append((path, i, "".join(a["source"]), "".join(b["source"])))
    if path == "main.ipynb":
        checks = re.search(r"\d+/\d+ passed", stream(new[7]))
        print("  specification checks:", checks.group(0) if checks else None)
        markdown = "\n".join("".join(c["source"]) for c in new if c["cell_type"] == "markdown")
        anchors = set(re.findall(r'<a id="([^"]+)"', markdown))
        links = re.findall(r"\]\(#([^)]+)\)", "".join(new[0]["source"]))
        print("  ToC unresolved links:", [l for l in links if l not in anchors])
        main_out = "".join(stream(c) for c in new if c["cell_type"] == "code")
    else:
        e3 = next(c for c in new if "".join(c["source"]).startswith("# === Code Cell E3"))
        print("  E3:", [l.strip() for l in stream(e3).splitlines() if re.match(r"\s*(PASS|FAIL)\s", l)])
        e2 = next(c for c in new if "".join(c["source"]).startswith("# === Code Cell E2:"))
        print("  E2:", re.findall(r"\d+/\d+ passed", stream(e2)))
        appx_out = "".join(stream(c) for c in new if c["cell_type"] == "code")

outputs = main_out + appx_out
print()
print("changed markdown cells:", [(p, i) for p, i, _, _ in report])
for path, i, before, after in report:
    added = "\n".join(l[1:] for l in difflib.ndiff(before.splitlines(), after.splitlines()) if l.startswith("+ "))
    missing = []
    for mant, exp in re.findall(r"(\d+\.\d+)\\times10\^\{(-?\d+)\}", added):
        if f"{mant}e{int(exp):+03d}" not in outputs:
            missing.append(f"{mant}e{int(exp):+03d}")
    for token in re.findall(r"\d+\.\d+", re.sub(r"\d+\.\d+\\times10\^\{-?\d+\}", "", added)):
        if token not in outputs:
            missing.append(token)
    print(f"  {path} cell {i}: decimals on changed lines not found in executed outputs: {sorted(set(missing))}")
