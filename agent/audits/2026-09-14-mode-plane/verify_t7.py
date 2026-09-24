"""After the C8 naming change: main's outputs against HEAD, expecting only Code Cell C's legend to differ."""
import difflib, json, pathlib, re, subprocess

ROOT = pathlib.Path("/Users/flog/Desktop/predictive coding")


def cells(rev):
    text = (subprocess.run(["git", "show", f"{rev}:main.ipynb"], cwd=ROOT, capture_output=True, text=True,
                           check=True).stdout if rev else (ROOT / "main.ipynb").read_text())
    return json.loads(text)["cells"]


def stream(c):
    return "".join("".join(o.get("text", [])) for o in c.get("outputs", []) if o.get("output_type") == "stream")


def norm(text):
    return [re.sub(r"\s+", " ", l).strip() for l in text.splitlines()
            if l.strip() and not l.strip().startswith("cost:")]


old, new = cells("HEAD"), cells(None)
figs = sum(1 for c in new for o in c.get("outputs", []) if "image/png" in o.get("data", {}))
errs = sum(1 for c in new for o in c.get("outputs", []) if o.get("output_type") == "error")
print(f"main.ipynb: figures {figs}, errors {errs}")
print("checks:", re.findall(r"\d+/\d+ passed", stream(new[7])))
for i, (a, b) in enumerate(zip(old, new)):
    if b["cell_type"] != "code" or norm(stream(a)) == norm(stream(b)):
        continue
    print(f"  cell {i} {''.join(b['source']).splitlines()[0][:50]}:")
    for l in difflib.unified_diff(norm(stream(a)), norm(stream(b)), lineterm="", n=0):
        if l.startswith(("-", "+")) and not l.startswith(("---", "+++")):
            print("     ", l[:150])
printed = stream(new[19])
print("  'counterfactual manipulations' printed once:", printed.count("counterfactual manipulations") == 1)
print("  the word 'control' in Code Cell C's output:",
      sorted({m.group(0) for m in re.finditer(r"[\w ]{0,18}control[\w ]{0,12}", printed)}))
print("  Code Cell 2 and 2b outputs unchanged (E3's baselines):",
      norm(stream(old[7])) == norm(stream(new[7])) and norm(stream(old[9])) == norm(stream(new[9])))
