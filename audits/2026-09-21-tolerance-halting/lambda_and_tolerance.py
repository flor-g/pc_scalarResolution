"""What a FIXED tolerance buys at two lexical strengths -- the evidence for R23's footnote.

R23 hypothesizes that a case's representative tolerance scales with that case's Lambda. The
first draft of the footnote supported it with "the same 1e-1 halts the Lambda = 8 flow after
15 updates and the Lambda = 512 flow only after 61 to 173". That comparison was WRONG: it set
the gaussian prior at Lambda = 8 against three DIFFERENT priors at Lambda = 512. Matched by
prior, two of the five go down at 1e-1, because prior-specific slow starts (H5) dominate there.

This script reports the matched comparison. `halt_by_tolerance` is closed form, so the whole
table costs well under a second. Nothing here is written into the notebooks: these are class (e)
quantities under agent.md Sec. 3.3 until a cell prints them, and the footnote cites this file
rather than quoting them as printed results.

Run from the project folder:
    .venv/bin/python audits/2026-09-21-tolerance-halting/lambda_and_tolerance.py
"""
import ast, nbformat

nb = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(nb.cells[5].source, "code_cell_1", "exec"), ns)
tree = ast.parse(nb.cells[7].source)
tree.body = [x for x in tree.body
             if isinstance(x, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom))
             or (isinstance(x, (ast.Assign, ast.AnnAssign))
                 and not isinstance(getattr(x, "value", None), ast.Call))]
exec(compile(tree, "code_cell_2_defs", "exec"), ns)
Net, halt = ns["LexicalPredictiveCodingNetwork"], ns["halt_by_tolerance"]
base = Net()
rows = {**ns["part_d_priors"](), "delta (all)": ns["beta_world_prior"](64.0, 1.0)}
TOLS = (1.0, 1e-1, 1e-2)

print("(1) UPDATES TO HALT, matched by prior")
print(f"{'prior':<13}" + "".join(f"{f'L=8 {t:.0e}':>12}" for t in TOLS)
      + "".join(f"{f'L=512 {t:.0e}':>13}" for t in TOLS))
for name, spec in rows.items():
    prior, over = spec if isinstance(spec, tuple) else (spec, {})
    cells = []
    for lam in (8.0, 512.0):
        p = base.respawn(base_prior=prior, lexical_strength=lam, **over)
        for tol in TOLS:
            try:
                cells.append(str(halt(p, tolerance=tol)["updates"]))
            except RuntimeError:
                cells.append("cap")
    print(f"{name:<13}" + "".join(f"{c:>12}" for c in cells[:3])
          + "".join(f"{c:>13}" for c in cells[3:]))
print("\n    At tol = 1 EVERY prior takes three times as many updates at Lambda = 512")
print("    (1 -> 3, and 3 -> 7 for the delta-like row). At 1e-2 the rows that are not")
print("    slow-started go up 11 to 17 fold. At 1e-1 the comparison is contaminated by")
print("    slow starts (flat at Lambda = 8, skewed low at Lambda = 512) and is not monotone.")

print("\n(2) theta_halt / theta*: the fraction of the asymptote the flow reaches")
for tol in TOLS:
    print(f"\n  tolerance {tol:.0e}")
    print(f"  {'prior':<13}{'L=8':>12}{'L=512':>12}")
    for name, spec in rows.items():
        prior, over = spec if isinstance(spec, tuple) else (spec, {})
        fr = {}
        for lam in (8.0, 512.0):
            p = base.respawn(base_prior=prior, lexical_strength=lam, **over)
            fr[lam] = halt(p, tolerance=tol)["theta_u"] / p.theta_u
        print(f"  {name:<13}{fr[8.0]:>12.4f}{fr[512.0]:>12.4f}")
print("\n    At Lambda = 512 the flow halts at 3.5% to 5% of theta* under EVERY prior and")
print("    across a tenfold change of tolerance. At Lambda = 8 the same tolerances give")
print("    anywhere from 0% to 30%. So at large Lambda the tolerance barely moves where the")
print("    flow lands, which is the sharper form of the Lambda dependence.")
