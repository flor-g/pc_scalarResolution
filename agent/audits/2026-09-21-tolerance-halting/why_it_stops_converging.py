"""Why does `infer` stop converging between lambda = 1206 and lambda = 2713?

Three candidate explanations, which mean very different things:
  (A) a genuinely slow mode of the dynamics at high theta_u -- a property of the MODEL;
  (B) an instability of explicit Euler at dt = tau_state / (8 lambda) -- an artifact of
      the SCHEME, which a better integrator would remove;
  (C) a ROUNDOFF FLOOR that rises with theta_u -- an artifact of PRECISION. The residuals
      are differences of nearly equal numbers and phi_S grows with theta_u, so the floor
      the derivative decays to may rise above the 1e-9 stopping tolerance, in which case
      the test can never fire however long the run.

(A) predicts the derivative decaying smoothly, just slowly. (B) predicts oscillation or
growth. (C) predicts a clean decay to a PLATEAU, with the plateau above 1e-9 and scaling
with the size of the state.

Method: run with the stopping test disabled (derivative_tolerance = 0.0) to a ladder of
step budgets, and recompute max|derivative| exactly as the loop does, from the returned
residuals and error units. No history is stored, so the ladder is cheap.
"""
import ast, nbformat, torch

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)
tree = ast.parse(nb.cells[7].source)
tree.body = [x for x in tree.body
             if isinstance(x, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom))
             or (isinstance(x, (ast.Assign, ast.AnnAssign))
                 and not isinstance(getattr(x, "value", None), ast.Call))]
exec(compile(tree, "defs", "exec"), ns)
Net = ns["LexicalPredictiveCodingNetwork"]
rows = {**ns["part_d_priors"](), "delta (all)": ns["beta_world_prior"](64.0, 1.0)}
net = Net().respawn(base_prior=rows["delta (all)"], lexical_strength=512.0)


def derivative_of(net, result):
    """max|derivative| at the state `infer` left, formed exactly as its loop forms it."""
    tau_error, tau_state, theta = result["tau_error"], 1.00, result["theta_u"]
    eps = result["error_units"]
    r = result["residuals"]
    dots = [
        (r["lexical"] / net.sigma_lexical - eps["lexical"]) / tau_error,
        (r["state"] / net.sigma_state - eps["state"]) / tau_error,
        (r["utility"] / net.sigma_utility - eps["utility"]) / tau_error,
        (-eps["state"] - eps["lexical"]) / tau_state,
        (-eps["utility"] + theta * net.project(eps["state"])) / tau_state,
    ]
    return max(float(d.abs().max()) for d in dots)


print("Stopping tolerance is 1e-9. dt = tau_state / (8 lambda), so a step budget of")
print("N steps simulates N / (8 lambda) time units.\n")
for theta in (34.70, 52.07):
    lam = float(net.stiffest_state_rate(theta))
    print(f"=== theta_u = {theta}  (lambda_max(H) = {lam:.1f}) ===", flush=True)
    print(f"  {'steps':>10}{'sim. time':>11}{'max|derivative|':>18}{'max|phi_S|':>13}"
          f"{'< 1e-9?':>9}")
    for budget in (50_000, 100_000, 200_000, 400_000, 800_000, 1_600_000):
        out = net.infer("some", theta_u=theta, derivative_tolerance=0.0,
                        max_steps=budget, record_history=False)
        d = derivative_of(net, out)
        print(f"  {budget:>10d}{budget * out['dt']:>11.1f}{d:>18.3e}"
              f"{float(out['phi_S'].abs().max()):>13.2f}{str(d < 1e-9):>9}", flush=True)
    print(flush=True)


# ---------------------------------------------------------------------------
# The floor against theta_u: is it a square law, and where does it cross 1e-9?
# Each run is given 50 simulated time units, well past the plateau the ladder
# above reaches by t = 37.
print("THE ROUNDOFF FLOOR AGAINST theta_u (each run to t = 50, past the plateau)")
print(f"  {'theta_u':>9}{'lambda':>10}{'floor':>13}{'floor/theta^2':>16}{'converges?':>12}")
reference = None
for theta in (13.37, 20.0, 34.70, 42.0, 46.9, 52.07, 61.27):
    lam = float(net.stiffest_state_rate(theta))
    out = net.infer("some", theta_u=theta, derivative_tolerance=0.0,
                    max_steps=int(50 * 8 * lam), record_history=False)
    floor = derivative_of(net, out)
    if reference is None:
        reference = floor / theta ** 2
    print(f"  {theta:>9.2f}{lam:>10.1f}{floor:>13.3e}{floor / theta ** 2:>16.3e}"
          f"{str(floor < 1e-9):>12}", flush=True)
print(f"\n  If the floor is c * theta_u^2 with c = {reference:.3e}, it crosses the 1e-9")
print(f"  stopping tolerance at theta_u = {(1e-9 / reference) ** 0.5:.1f}, where "
      f"lambda_max(H) = {float(net.stiffest_state_rate((1e-9 / reference) ** 0.5)):.0f}.")
