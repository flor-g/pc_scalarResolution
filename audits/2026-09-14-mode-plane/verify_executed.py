"""After T2's execution: output diffs against 5a7bc8e, checks, E2/E3, and Code Cell 4's new block against the test. Scratch."""
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
    old, new = cells("5a7bc8e", path), cells(None, path)
    figs = sum(1 for c in new for o in c.get("outputs", []) if "image/png" in o.get("data", {}))
    errs = sum(1 for c in new for o in c.get("outputs", []) if o.get("output_type") == "error")
    print(f"{path}: figures {figs}, errors {errs}")
    for i, (a, b) in enumerate(zip(old, new)):
        if b["cell_type"] != "code" or norm(stream(a)) == norm(stream(b)):
            continue
        diff = list(difflib.unified_diff(norm(stream(a)), norm(stream(b)), lineterm="", n=0))
        removed = [l for l in diff if l.startswith("-") and not l.startswith("---")]
        added = [l for l in diff if l.startswith("+") and not l.startswith("+++")]
        print(f"  cell {i} {''.join(b['source']).splitlines()[0][:50]}: {len(removed)} lines removed, "
              f"{len(added)} added")
        for l in removed[:20]:
            print("     ", l[:160])
    if path == "main.ipynb":
        print("  checks:", re.findall(r"\d+/\d+ passed", stream(new[7])))
        printed = stream(new[13])
        block = printed[printed.index("THE MODE SHIFT AND MODE POSITION CRITERIA ON THE PLANE"):printed.index("MU_U SENSITIVITY")]
        test = (ROOT / "audits/2026-09-14-mode-plane/test_output.txt").read_text()
        test = test[test.index("THE MODE SHIFT AND MODE POSITION CRITERIA ON THE PLANE"):]
        print("  Code Cell 4's new block equals the pre-execution test output:", norm(block) == norm(test))
        print("  'condition' or 'verdict' in Code Cell 4 source or output:",
              re.findall(r"\b(condition|verdict)\w*", "".join(new[13]["source"]) + printed, re.I))
    else:
        for c in new:
            src = "".join(c["source"])
            if src.startswith("# === Code Cell E2:"):
                print("  E2:", re.findall(r"\d+/\d+ passed", stream(c)))
            if src.startswith("# === Code Cell E3"):
                print("  E3:", [l.strip() for l in stream(c).splitlines() if re.match(r"\s*(PASS|FAIL)\s", l)])
