# Audit of 2026-09-13

The audits behind registers D (operations against Bogacz, 2017) and E (quantities against the
prose) of `decisions.md`, run against commit 76df22e.

| File | What it is |
|---|---|
| `extract_cells.py` | Dumps every cell of both notebooks and each code cell's stored text output. |
| `audit_numbers.py` | Lists every default, module constant and numeric literal in the code cells (`constants.txt`), and matches every number quoted in the markdown against the stored outputs and then against `theta_u_learned_reach.md` (`prose_numbers.txt` lists the unmatched ones; `audit_numbers_summary.txt` the counts). It matches values, not provenance, so a number with few significant figures can match by coincidence. |
| `verify_audit.py` | Checks V1 to V4 of the registers against code cell 1: V1 which gradient Eq. (19) is, V2 which matrix `stiffest_state_rate` computes, V3 that `infer` is Bogacz's Eqs. (53)-(54) in the coordinates W^1/2 phi, V4 the gradient of F~ at theta_u = 0. Output in `verify_output.txt`. |

Run from the project folder, with OUT any scratch directory:

```bash
.venv/bin/python audits/2026-09-13/extract_cells.py OUT
.venv/bin/python audits/2026-09-13/audit_numbers.py OUT audits/2026-09-13
.venv/bin/python audits/2026-09-13/verify_audit.py OUT/m05.py
```
