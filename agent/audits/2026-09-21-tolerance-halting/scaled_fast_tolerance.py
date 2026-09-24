"""AUDIT: what happens if `infer`'s stopping tolerance becomes k * lambda_max(H)?

Today the tolerance is a fixed 1e-9 (decision I3), chosen to sit above the roundoff floor
measured at the theta_u of the time (F34). H12/H13 show the floor is not fixed: it is
4.547e-13 * lambda_max(H), flat to four significant figures, so a CONSTANT tolerance means
a shrinking margin as theta_u grows, and above theta_u ~ 46.6 no margin at all -- the test
can never fire and the run ends at the cap.

The proposal is to key the tolerance to the same quantity the floor tracks, which is also
the quantity `fast_time_constant` already computes and D4 already assumes the system has.
MARGIN = k / 4.547e-13 is how far above the floor the test sits; 1e-9 at lambda = 180.8 is
a margin of 12.2, which is what I3 bought.

What this audit must establish, because each could sink the proposal:
  1. does it converge where 1e-9 cannot, and still converge where 1e-9 can;
  2. what it costs in steps;
  3. whether the FIXED POINT moves (against Eqs. 15-16, which are exact);
  4. whether the step count is REPRODUCIBLE -- F34's pathology is that a tolerance inside
     the roundoff band makes the stopping step depend on which roundoff-level sample lands
     below it, so a change in theta_u of one part in 1e15 moves it by hundreds, and
     Appendix E's different summation order disagrees with main on the same trajectory.
"""
import ast, time, nbformat, torch

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

FLOOR_PER_LAMBDA = 4.547e-13
KS = (2.0e-12, 5.5e-12, 2.0e-11)          # margins of 4.4, 12.1, 44.0
strong = Net().respawn(base_prior=rows["delta (all)"], lexical_strength=512.0)
weak = Net()

def run(net, theta, tol, cap_time=1000.0):
    lam = float(net.stiffest_state_rate(theta))
    t0 = time.perf_counter()
    out = net.infer("some", theta_u=theta, derivative_tolerance=tol,
                    record_history=False)
    secs = time.perf_counter() - t0
    gap = float((out["phi_S"] - net.closed_form_fixed_point("some", theta_u=theta)[0])
                .abs().max())
    return lam, out["converged"], out["steps"], secs, gap

print("(1) DOES IT CONVERGE, AND WHAT DOES THE FIXED POINT COST?")
print(f"  {'theta_u':>8}{'lambda':>9}{'rule':>14}{'tolerance':>12}{'margin':>8}"
      f"{'conv':>6}{'steps':>11}{'steps/lam':>10}{'|phi-phi*|':>12}{'s':>7}")
for net, label, thetas in ((strong, "512", (13.37, 34.70, 52.07, 61.27)),
                           (weak, "8", (5.29, 28.44))):
    for theta in thetas:
        lam0 = float(net.stiffest_state_rate(theta))
        trials = [("1e-9 (today)", 1e-9)]
        if lam0 * FLOOR_PER_LAMBDA >= 1e-9:
            trials = [("1e-9 SKIPPED", None)]     # known to run to the cap; do not pay for it
        trials += [(f"k={k:.1e}", k * lam0) for k in KS]
        for rule, tol in trials:
            if tol is None:
                print(f"  {theta:>8.2f}{lam0:>9.1f}{rule:>14}{'-':>12}{'<1':>8}"
                      f"{'False':>6}{'(cap)':>11}{'8000':>10}{'-':>12}{'-':>7}", flush=True)
                continue
            lam, conv, steps, secs, gap = run(net, theta, tol)
            print(f"  {theta:>8.2f}{lam:>9.1f}{rule:>14}{tol:>12.2e}"
                  f"{tol / (FLOOR_PER_LAMBDA * lam):>8.1f}{str(conv):>6}{steps:>11d}"
                  f"{steps / lam:>10.1f}{gap:>12.1e}{secs:>7.1f}", flush=True)
    print(flush=True)

print("(2) IS THE STEP COUNT REPRODUCIBLE? (F34's pathology)")
print("    theta_u perturbed by one part in 1e15; a tolerance inside the roundoff band")
print("    moves the stopping step by hundreds.")
print(f"  {'theta_u':>8}{'rule':>14}{'steps':>11}{'steps (nudged)':>16}{'difference':>12}")
for theta in (34.70, 13.37):
    lam0 = float(strong.stiffest_state_rate(theta))
    for rule, tol in [("1e-9 (today)", 1e-9)] + [(f"k={k:.1e}", k * lam0) for k in KS]:
        a = strong.infer("some", theta_u=theta, derivative_tolerance=tol,
                         record_history=False)["steps"]
        b = strong.infer("some", theta_u=theta * (1 + 1e-15), derivative_tolerance=tol,
                         record_history=False)["steps"]
        print(f"  {theta:>8.2f}{rule:>14}{a:>11d}{b:>16d}{b - a:>12d}", flush=True)
