# runnb.py NOTEBOOK
import sys, time, nbformat
from nbclient import NotebookClient
path = sys.argv[1]; nb = nbformat.read(path, as_version=4); t0 = time.time()
client = NotebookClient(nb, timeout=3600, kernel_name="python3", resources={"metadata": {"path": "."}})
try:
    client.execute(); status = "OK"
except Exception as exc:
    status = f"FAILED: {type(exc).__name__}: {str(exc)[-600:]}"
nbformat.write(nb, path)
errors = sum(1 for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", []) if o.output_type == "error")
figures = sum(1 for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", [])
              if o.output_type in ("display_data", "execute_result") and "image/png" in o.get("data", {}))
print(f"RUNNER {status}  {path}: error outputs {errors}, figures {figures}, runtime {time.time() - t0:.0f} s")
