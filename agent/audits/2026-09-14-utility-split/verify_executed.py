"""After T3's execution: output diffs against 2718404, checks, E2/E3, and Sec. 8's output against the test. Scratch."""
import difflib, json, pathlib, re, subprocess

ROOT = pathlib.Path("/Users/flog/Desktop/predictive coding")


def cells(rev, path):
    text = (subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, text=True,
                           check=True).stdout if rev else (ROOT / path).read_text())
    return json.loads(text)["cells"]


def stream(c):
    return "".join("".join(o.get("text", [])) for o in c.get("outputs", []) if o.get("output_type") == "stream")


def norm(text):
    return [re.sub(r"\s+", " ", l).strip() for l in text.splitlines()
            if l.strip() and not l.strip().startswith("cost:")]


for path in ("main.ipynb", "appendix_E.ipynb"):
    old, new = cells("2718404", path), cells(None, path)
    figs = sum(1 for c in new for o in c.get("outputs", []) if "image/png" in o.get("data", {}))
    errs = sum(1 for c in new for o in c.get("outputs", []) if o.get("output_type") == "error")
    print(f"{path}: figures {figs}, errors {errs}")
    for i, (a, b) in enumerate(zip(old, new)):
        if b["cell_type"] != "code" or norm(stream(a)) == norm(stream(b)):
            continue
        removed = [l for l in difflib.unified_diff(norm(stream(a)), norm(stream(b)), lineterm="", n=0)
                   if l.startswith("-") and not l.startswith("---")]
        added = [l for l in difflib.unified_diff(norm(stream(a)), norm(stream(b)), lineterm="", n=0)
                 if l.startswith("+") and not l.startswith("+++")]
        print(f"  cell {i} {''.join(b['source']).splitlines()[0][:50]}: {len(removed)} lines removed, "
              f"{len(added)} added")
        for l in removed[:20] + (added[:12] if i != 19 else []):
            print("     ", l[:160])
    if path == "main.ipynb":
        print("  checks:", re.findall(r"\d+/\d+ passed", stream(new[7])))
        printed = stream(new[19])
        section = printed[printed.index("APPENDIX C, Sec. 8"):]
        test = (ROOT / "audits/2026-09-14-utility-split/test_output.txt").read_text()
        print("  Sec. 8 output equals the pre-insertion test output:", norm(section) == norm(test))
        print("  'condition' or 'verdict' in Code Cell C source or output:",
              bool(re.search(r"condition|verdict", "".join(new[19]["source"]) + printed, re.I)))
    else:
        for c in new:
            src = "".join(c["source"])
            if src.startswith("# === Code Cell E2:"):
                print("  E2:", re.findall(r"\d+/\d+ passed", stream(c)))
            if src.startswith("# === Code Cell E3"):
                print("  E3:", [l.strip() for l in stream(c).splitlines() if re.match(r"\s*(PASS|FAIL)\s", l)])
