"""T1 acceptance (delta_criteria_printing.md): outputs differ from 7854b8f only by insertions, and the
new rows equal audits/2026-09-13-delta-criteria/output.txt (Lambda = 8 rows, delta row) and the
strong-Lambda probe's F7 table (Lambda = 512). Scratch."""
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
    old, new = cells("7854b8f", path), cells(None, path)
    figs = sum(1 for c in new for o in c.get("outputs", []) if "image/png" in o.get("data", {}))
    errs = sum(1 for c in new for o in c.get("outputs", []) if o.get("output_type") == "error")
    print(f"{path}: figures {figs}, errors {errs}")
    for i, (a, b) in enumerate(zip(old, new)):
        if b["cell_type"] != "code" or norm(stream(a)) == norm(stream(b)):
            continue
        ops = difflib.SequenceMatcher(None, norm(stream(a)), norm(stream(b)), autojunk=False).get_opcodes()
        kinds = {op[0] for op in ops if op[0] != "equal"}
        inserted = sum(op[4] - op[3] for op in ops if op[0] == "insert")
        head = "".join(b["source"]).splitlines()[0][:45]
        print(f"  cell {i} {head}: changes {sorted(kinds)}, {inserted} lines inserted")
        if kinds - {"insert"}:
            for l in difflib.unified_diff(norm(stream(a)), norm(stream(b)), lineterm="", n=0):
                if l.startswith(("-", "+")) and not l.startswith(("---", "+++")):
                    print("     ", l)
    if path == "main.ipynb":
        print("  checks:", re.findall(r"\d+/\d+ passed", stream(new[7])))
        rows = {}
        for idx in (7, 9):
            text = stream(new[idx])
            block = text[text.index("THE DELTA READ-OUT'S TWO CRITERIA"):]
            for line in block.splitlines()[4:]:
                parts = line.split()
                if not parts or parts[0] in ("over", "(a)"):
                    break
                # name may be two words; label is "theta_u* = x" or "realizable x"
                m = re.match(r"\s*(.+?)\s{2,}(theta_u\* = \S+|realizable \S+)\s+(.*)", line)
                name, label, rest = m.group(1), m.group(2), m.group(3).split()
                rows[(idx, name, label)] = rest
            print(f"  cell {idx} summary:", [l.strip() for l in block.splitlines() if l.strip().startswith(("over", "(a) and"))])
        for key, rest in rows.items():
            print("   ", key, rest)
    else:
        e3 = next(c for c in new if "".join(c["source"]).startswith("# === Code Cell E3"))
        print("  E3:", [l.strip() for l in stream(e3).splitlines() if re.match(r"\s*(PASS|FAIL)\s", l)])
        e2 = next(c for c in new if "".join(c["source"]).startswith("# === Code Cell E2:"))
        print("  E2:", re.findall(r"\d+/\d+ passed", stream(e2)))

print()
print("reference, audits/2026-09-13-delta-criteria/output.txt PART D ROWS:")
ref = (ROOT / "audits/2026-09-13-delta-criteria/output.txt").read_text()
print(ref[ref.index("PART D ROWS"):ref.index("PLANE")])
