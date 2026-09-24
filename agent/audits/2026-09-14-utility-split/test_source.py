"""Run Sec. 8's function outside the notebook, on Code Cell 1 and Code Cell 2's definitions. Scratch test."""
import ast, contextlib, io, nbformat, time

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)
for node in ast.parse(nb.cells[7].source).body:
    if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)) or (
            isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) and t.id.isupper() for t in node.targets)):
        exec(compile(ast.Module([node], []), "code_cell_2", "exec"), ns)
source = open("audits/2026-09-14-utility-split/utility_split_source.py").read()
compile(source, "sec8", "exec")
exec(source, ns)
net = ns["LexicalPredictiveCodingNetwork"]()
t0 = time.time()
buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    ns["utility_split_report"](net, ns["part_d_priors"](), [2.0 ** k for k in range(11)], [2.0 ** k for k in range(1, 12)])
open("audits/2026-09-14-utility-split/test_output.txt", "w").write(buffer.getvalue())
print(buffer.getvalue())
print(f"runtime {time.time() - t0:.1f} s")
