"""Dump every cell of main.ipynb and appendix_E.ipynb, and each code cell's stored text output.

Run from the project folder:  .venv/bin/python audits/2026-09-13/extract_cells.py OUTDIR
Files: m<NN>.md / m<NN>.py for main.ipynb cell NN, e<NN>.* for appendix_E.ipynb, and
<name>.out.txt holding the stored stream and text outputs of a code cell.
"""
import json, os, sys
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for f, tag in [("main.ipynb", "m"), ("appendix_E.ipynb", "e")]:
    nb = json.load(open(f))
    for i, c in enumerate(nb["cells"]):
        src = "".join(c["source"])
        ext = "py" if c["cell_type"] == "code" else "md"
        open(f"{out}/{tag}{i:02d}.{ext}", "w").write(src)
        if c["cell_type"] == "code":
            txt = []
            for o in c.get("outputs", []):
                if o["output_type"] == "stream":
                    txt.append("".join(o["text"]))
                elif o["output_type"] in ("execute_result", "display_data"):
                    d = o.get("data", {})
                    if "text/plain" in d and "image/png" not in d:
                        txt.append("".join(d["text/plain"]))
                elif o["output_type"] == "error":
                    txt.append("ERROR " + o["ename"])
            open(f"{out}/{tag}{i:02d}.out.txt", "w").write("\n".join(txt))
