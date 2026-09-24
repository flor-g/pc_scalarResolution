"""Run Code Cell 1, the new Code Cell 2 and Code Cell 2b outside the notebook, and check
that every line the old Code Cell 2 printed is still printed by one of the two (scratch)."""
import contextlib, io, json, os, pathlib, re, subprocess, sys, time
from collections import Counter

os.environ["MPLBACKEND"] = "Agg"
S = pathlib.Path(__file__).parent
ROOT = pathlib.Path("/Users/flog/Desktop/predictive coding")
os.chdir(ROOT)
nb = json.loads(subprocess.run(["git", "show", "a202cdb:main.ipynb"], capture_output=True,
                               text=True, check=True).stdout)
old_out = "".join("".join(o.get("text", [])) for o in nb["cells"][7]["outputs"]
                  if o.get("output_type") == "stream")

ns = {}
exec("".join(nb["cells"][5]["source"]), ns)
outs = {}
for label, path in (("2", "new_cell2.py"), ("2b", "new_cell2b.py")):
    buffer = io.StringIO()
    t0 = time.time()
    with contextlib.redirect_stdout(buffer):
        exec((S / path).read_text(), ns)
    outs[label] = buffer.getvalue()
    (S / f"test_out_{label}.txt").write_text(outs[label])
    print(f"Code Cell {label}: {time.time() - t0:.0f} s, {len(outs[label].splitlines())} lines",
          file=sys.stderr)


def norm(text):
    return [re.sub(r"\s+", " ", l).strip() for l in text.splitlines()
            if l.strip() and not l.strip().startswith("cost:")]


old, new2, new2b = Counter(norm(old_out)), Counter(norm(outs["2"])), Counter(norm(outs["2b"]))
lost = old - (new2 + new2b)
print("old lines not printed by either new cell:", sum(lost.values()))
for l, n in lost.items():
    print("  -", n, "x", l)
print()
print("lines only in the new Code Cell 2 (not in old):")
for l, n in (new2 - old).items():
    print("  +", n, "x", l)
