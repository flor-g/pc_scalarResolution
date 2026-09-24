"""One inference, timed, at each theta_u a halt actually lands on. Ascending, so partial
output is already informative."""
import ast, time, nbformat
nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)
tree = ast.parse(nb.cells[7].source)
tree.body = [n for n in tree.body
             if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom))
             or (isinstance(n, (ast.Assign, ast.AnnAssign))
                 and not isinstance(getattr(n, "value", None), ast.Call))]
exec(compile(tree, "defs", "exec"), ns)
Net = ns["LexicalPredictiveCodingNetwork"]
rows = {**ns["part_d_priors"](), "delta (all)": ns["beta_world_prior"](64.0, 1.0)}
p = Net().respawn(base_prior=rows["delta (all)"], lexical_strength=512.0)
print(f"{'theta_u':>9}{'lambda':>10}{'steps':>12}{'seconds':>10}   note", flush=True)
for th, note in ((13.37, "TODAY's arrival row"), (34.70, "delta, tol=1"),
                 (52.07, "skewed high, tol=1"), (54.43, "flat, tol=1"),
                 (61.27, "flat, tol=1e-1"), (71.09, "delta, tol=1e-1")):
    t0 = time.perf_counter()
    r = p.infer("some", theta_u=th, record_history=False)
    dt = time.perf_counter() - t0
    print(f"{th:>9.2f}{float(p.stiffest_state_rate(th)):>10.1f}{r['steps']:>12d}"
          f"{dt:>10.2f}   {note}", flush=True)
