"""T2 test: run Code Cell 4's sweep and summary outside the notebook; existing lines unchanged; new lines equal the audit."""
import ast, contextlib, io, json, re, subprocess, nbformat

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)
for index in (7, 13):
    for node in ast.parse(nb.cells[index].source).body:
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)) or (
                isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) and t.id.isupper() for t in node.targets)):
            exec(compile(ast.Module([node], []), f"cell_{index}", "exec"), ns)
net = ns["LexicalPredictiveCodingNetwork"]()
buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    grids = ns["lambda_alpha_sweep"](net)
    summary = ns["plane_summary"](grids)
out = buffer.getvalue()
open("audits/2026-09-14-mode-plane/test_output.txt", "w").write(out)

norm = lambda t: [re.sub(r"\s+", " ", l).strip() for l in t.splitlines() if l.strip()]
stored = json.loads(subprocess.run(["git", "show", "HEAD:main.ipynb"], capture_output=True, text=True).stdout)["cells"][13]
stored = "".join("".join(o.get("text", [])) for o in stored["outputs"] if o.get("output_type") == "stream")
stored = stored[: stored.index("MU_U SENSITIVITY")]
new_block = out[out.index("THE MODE SHIFT AND MODE POSITION CRITERIA ON THE PLANE"):]
before = out[: out.index("  THE MODE SHIFT AND MODE POSITION CRITERIA ON THE PLANE")]
print("existing lines unchanged:", norm(before) == norm(stored))
print(new_block)

audit = open("audits/2026-09-13-delta-criteria/output.txt").read()
fails = []
nums = lambda l: [float(x) for x in re.findall(r"(?<![\w.])[-+]?\d+\.?\d*(?:e[-+]\d+)?", l)]
def expect(pattern, values):
    line = next((l for l in new_block.splitlines() if pattern in l), "")
    if nums(line)[-len(values):] != values and nums(line) != values:
        fails.append((pattern, line.strip(), values))
expect("the mode shift criterion is met in", [67, 121, 59, 13, 74, 59, 33])
expect("a shift of 0 steps", [4, 0, 0])
expect("smallest gap between the two largest", [5.60e-05])
expect("the q and mode shift criteria:", [53, 21, 14, 33])
expect("the q and mode position criteria:", [59, 0, 0, 62])
expect("the two conjunctions:", [13, 20, 0, 88])
a_rows = audit[audit.index("CELLS WHERE THE READ-OUTS DISAGREE"):audit.index("FLOORS AND THE V")].splitlines()[2:]
a_rows = [l for l in a_rows if l.strip()]
n_start = new_block.index("cells where a q criterion and its mode counterpart disagree")
n_rows = new_block[n_start:new_block.index("floors by alpha")].splitlines()[2:]
n_rows = [l for l in n_rows if l.strip()]
if len(a_rows) != len(n_rows):
    fails.append(("row count", len(a_rows), len(n_rows)))
for a, n in zip(a_rows, n_rows):
    a_flags = re.sub(r"yes", " yes ", re.sub(r"no", " no ", a.split("0.", 1)[0] + a[a.rindex("  "):] if False else a)).split()
    a_yn = re.findall(r"yes|no", a); n_yn = re.findall(r"yes|no", n)
    if [round(x, 4) for x in nums(re.sub(r"yes|no", " ", a))] != [round(x, 4) for x in nums(re.sub(r"yes|no", " ", n))] or a_yn != n_yn:
        fails.append(("row", a.strip(), n.strip()))
a_v = [l.split() for l in audit[audit.index("FLOORS AND THE V"):].splitlines()[2:] if l.strip()]
n_v = [l.split() for l in new_block[new_block.index("floors by alpha"):].splitlines()[4:] if l.strip()]
if a_v != n_v:
    fails.append(("V table", a_v, n_v))
print("summary keys:", {k: summary[k] for k in ("mode_shift", "mode_position", "mode_both")})
print("ACCEPTANCE", "PASS" if not fails else "FAIL")
for f in fails:
    print("  ", f)
