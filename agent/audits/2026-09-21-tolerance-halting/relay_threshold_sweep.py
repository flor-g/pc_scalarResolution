"""H15's unmeasured corner: appendix_E's two relay checks against theta_u.

  worst_relay_gradient < 1e-12  -- the relay form of Eq. (20) against the column form.
      Same number, different summation order, so the residual is roundoff on terms that
      scale with phi_u and eps_S, both of which grow with theta_u.
  worst_lagged < 1e-9           -- an instantaneous relay against one lagged by
      tau_relay = tau_error / 2. Both runs stop within their own tolerance, so their
      difference should scale WITH the tolerance, not sit at a fixed 1e-9.
"""
import ast, nbformat, torch

nbE = nbformat.read("appendix_E.ipynb", as_version=4)
ns = {}
exec(compile(nbE.cells[2].source, "E1", "exec"), ns)
tree = ast.parse(nbE.cells[3].source)
tree.body = [x for x in tree.body
             if isinstance(x, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom))
             or (isinstance(x, (ast.Assign, ast.AnnAssign))
                 and not isinstance(getattr(x, "value", None), ast.Call))]
exec(compile(tree, "E2defs", "exec"), ns)
Net, UTT = ns["LexicalPredictiveCodingNetwork"], ns["UTTERANCES"]
rows = {**ns["part_d_priors"](), "delta (all)": ns["beta_world_prior"](64.0, 1.0)}
K = 5.5e-12

print(f"tolerance = k * lambda_max(H), k = {K:.1e};  thresholds today: relay 1e-12, lagged 1e-9\n")
print(f"{'net':>6}{'theta_u':>9}{'lambda':>9}{'tol':>11}{'relay grad':>13}{'/tol':>9}"
      f"{'lagged':>12}{'/tol':>8}{'min F step':>13}")
for label, net, thetas in (("L=8", Net(), (5.29, 28.44)),
                           ("L=512", Net().respawn(base_prior=rows["delta (all)"],
                                                   lexical_strength=512.0),
                            (13.37, 34.70))):
    for theta in thetas:
        lam = float(net.stiffest_state_rate(theta))
        tol = K * lam
        w_relay = w_lag = 0.0
        w_step = 0.0
        tau_relay = 0.5 * net.fast_time_constant(theta)
        for y in UTT:
            inst = net.infer(y, theta_u=theta, derivative_tolerance=tol,
                             record_history=False)
            w_relay = max(w_relay, abs(float(net.theta_u_gradient(inst))
                                       - float(net.theta_u_gradient_columns(inst).sum())))
            lag = net.infer(y, theta_u=theta, derivative_tolerance=tol,
                            tau_relay=tau_relay, record_history=True)
            w_lag = max(w_lag,
                        float((inst["phi_S"] - lag["phi_S"]).abs().max()),
                        float((inst["phi_u"] - lag["phi_u"]).abs().max()),
                        float((lag["relay"] - net.relay(lag["phi_u"])).abs().max()))
            tr = [e["free_energy"] for e in lag["history"]]
            w_step = min(w_step, min(tr[i+1] - tr[i] for i in range(len(tr)-1)))
        print(f"{label:>6}{theta:>9.2f}{lam:>9.1f}{tol:>11.2e}{w_relay:>13.2e}"
              f"{w_relay/tol:>9.2f}{w_lag:>12.2e}{w_lag/tol:>8.2f}{w_step:>+13.1e}",
              flush=True)
