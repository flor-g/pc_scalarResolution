"""Is the step blow-up the CONDITION NUMBER of H? dt ~ 1/lambda_max, and the simulated
time to settle ~ 1/lambda_min, so steps ~ lambda_max/lambda_min if that is the story."""
import ast, nbformat, torch
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

def spectrum(net, theta):
    rw = torch.sqrt(net.weights)[:, None] * net.basis
    gram = net.basis.T @ (net.weights[:, None] * net.basis)
    eK = torch.eye(net.num_nodes, dtype=net.dtype)
    em = torch.eye(net.num_basis, dtype=net.dtype)
    H = torch.cat([
        torch.cat([(1/net.sigma_lexical + 1/net.sigma_state) * eK,
                   -theta * rw / net.sigma_state], dim=1),
        torch.cat([-theta * rw.T / net.sigma_state,
                   em / net.sigma_utility + theta**2 * gram / net.sigma_state], dim=1)], dim=0)
    e = torch.linalg.eigvalsh(H)
    return float(e.max()), float(e.min())

MEAS = {13.37: 39007, 34.70: 264724, 52.07: 21706280, 54.43: 23717000, 61.27: 30048104, 71.09: 40446305}
print(f"{'theta_u':>8}{'lambda_max':>12}{'lambda_min':>12}{'cond':>10}"
      f"{'steps':>12}{'steps/lmax':>11}{'steps/cond':>11}")
for th, steps in MEAS.items():
    lmax, lmin = spectrum(p, th)
    cond = lmax / lmin
    print(f"{th:>8.2f}{lmax:>12.1f}{lmin:>12.5f}{cond:>10.1f}{steps:>12d}"
          f"{steps/lmax:>11.1f}{steps/cond:>11.1f}")
