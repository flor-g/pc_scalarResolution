"""SWEEP: which of the notebooks' fixed numeric thresholds are brittle under theta_u?

H12/H13 found that `infer`'s 1e-9 is a constant bounding a quantity that scales as
4.547e-13 * lambda_max(H). The same mistake may be repeated elsewhere: any constant
calibrated by looking at a quantity that scales with lambda_max or theta_u will silently
erode its own margin as theta_u grows, then FAIL rather than warn.

Measured here, at each theta_u, under a tolerance of k * lambda_max(H) with k = 5.5e-12
(the recommended value, today's margin made scale-free). A quantity whose column grows
with lambda is brittle against the fixed threshold in its row.
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
UTT = ns["UTTERANCES"]
rows = {**ns["part_d_priors"](), "delta (all)": ns["beta_world_prior"](64.0, 1.0)}
K = 5.5e-12

weak = Net()
strong = Net().respawn(base_prior=rows["delta (all)"], lexical_strength=512.0)

print(f"tolerance = k * lambda_max(H), k = {K:.1e}\n")
print(f"{'net':>5}{'theta_u':>9}{'lambda':>9}{'tol':>10}{'|phi-phi*|':>12}"
      f"{'Eq17 id_1':>12}{'Eq17 id_2':>12}{'|1-q mass|':>12}{'min dF step':>13}")
for net, label, thetas, hist in ((weak, "L=8", (5.29, 28.44), True),
                                 (strong, "L=512", (13.37, 34.70, 52.07), False)):
    for theta in thetas:
        lam = float(net.stiffest_state_rate(theta))
        tol = K * lam
        w_state = w_id1 = w_id2 = w_q = 0.0
        w_mono = 0.0
        for y in UTT:
            r = net.infer(y, theta_u=theta, derivative_tolerance=tol,
                          record_history=hist)
            sS, su = net.closed_form_fixed_point(y, theta_u=theta)
            w_state = max(w_state, float((r["phi_S"] - sS).abs().max()),
                          float((r["phi_u"] - su).abs().max()))
            u = r["error_units"]
            w_id1 = max(w_id1, float((u["state"] + u["lexical"]).abs().max()))
            w_id2 = max(w_id2, float((u["utility"] - theta * net.project(u["state"]))
                                     .abs().max()))
            w_q = max(w_q, abs(float((net.weights * r["q"]).sum()) - 1.0))
            if hist:
                tr = [e["free_energy"] for e in r["history"]]
                w_mono = min(w_mono, min(tr[i+1] - tr[i] for i in range(len(tr)-1)))
        mono = f"{w_mono:+.1e}" if hist else "-"
        print(f"{label:>5}{theta:>9.2f}{lam:>9.1f}{tol:>10.2e}{w_state:>12.2e}"
              f"{w_id1:>12.2e}{w_id2:>12.2e}{w_q:>12.2e}{mono:>13}", flush=True)

print("\nFixed thresholds these are checked against (main cell 7 / E cell 3):")
print("  |phi - phi*|  < 1e-8      Eq17 id_1 < 1e-8      Eq17 id_2 < 1e-8")
print("  |1 - q mass|  < 1e-10     min dF step > -1e-9")
