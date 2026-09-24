"""Insert Sec. 8's function and call into main's Code Cell C (T3). Run once."""
import nbformat
nb = nbformat.read("main.ipynb", as_version=4)
cell = nb.cells[19]
assert cell.cell_type == "code" and cell.source.startswith("# === Code Cell C:"), cell.source[:40]
call = "\n\nappendix_c_report(evaluation_network)"
assert cell.source.rstrip().endswith(call.strip()) and cell.source.count(call) == 1
assert "utility_split_report" not in cell.source
source = open("audits/2026-09-14-utility-split/utility_split_source.py").read().strip("\n")
head = cell.source.rstrip()[: -len(call.strip())].rstrip("\n")
cell.source = (head + "\n\n\n" + source + "\n\n\nappendix_c_report(evaluation_network)\n"
               "utility_split_report(evaluation_network, part_d_priors(), sweep_grids[\"alphas\"], "
               "sweep_grids[\"lambdas\"])")
compile(cell.source, "code_cell_c", "exec")
nbformat.write(nb, "main.ipynb")
print("applied; Code Cell C now", len(cell.source.splitlines()), "lines")
