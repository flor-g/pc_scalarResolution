"""O11 option 2: Eq. (27)'s all-region becomes closed, R = {zeta >= theta_L}.

23 mask sites, 3 printed labels, 2 prose sites. Every edit is count-asserted.
Run from the project root; pass --apply to write.
"""
import json, pathlib, re, sys

MASK = re.compile(r"(\w+)\.zeta > \1\.theta_L")
TARGETS = {("main.ipynb", 7): 7, ("main.ipynb", 9): 2, ("main.ipynb", 11): 1,
           ("main.ipynb", 13): 2, ("main.ipynb", 19): 2,
           ("appendix_E.ipynb", 3): 7, ("appendix_E.ipynb", 4): 2}
LABELS = {("main.ipynb", 7): ("'q-mass, zeta > theta_L':>24", "'q-mass, zeta >= theta_L':>24"),
          ("appendix_E.ipynb", 3): ("'q-mass, zeta > theta_L':>24", "'q-mass, zeta >= theta_L':>24"),
          ("main.ipynb", 19): ("All-region q-mass, zeta > theta_L (Eq. 27)",
                               "All-region q-mass, zeta >= theta_L (Eq. 27)")}
PROSE = [
    (94, r'$\varsigma(-\theta_L)=1/2n$ at $n=10$ (Eq. A5), so the region $\zeta>\theta_L$ is $s>0.95$, which on' + "\n",
         r'$\varsigma(-\theta_L)=1/2n$ at $n=10$ (Eq. A5), so the region $\zeta\ge\theta_L$ is $s\ge0.95$, which on' + "\n"),
    (445, r'Three regions are used. $P(\text{all-region})$ takes $R=\{\zeta>\theta_L\}$, where *all* is true, and' + "\n",
          r'Three regions are used. $P(\text{all-region})$ takes $R=\{\zeta\ge\theta_L\}$, where *all* is true, and' + "\n"),
]
DRY = "--apply" not in sys.argv

for path in ("main.ipynb", "appendix_E.ipynb"):
    raw = pathlib.Path(path).read_bytes()
    nb = json.loads(raw)
    assert (json.dumps(nb, indent=1, ensure_ascii=False) + "\n").encode() == raw, \
        f"{path}: writer would reformat the file; aborting"
    masks = labels = prose = 0
    for (p, cell), want in TARGETS.items():
        if p != path:
            continue
        src = nb["cells"][cell]["source"]
        got = sum(len(MASK.findall(l)) for l in src)
        assert got == want, f"{path} cell {cell}: {got} mask sites, expected {want}"
        nb["cells"][cell]["source"] = [MASK.sub(r"\1.zeta >= \1.theta_L", l) for l in src]
        masks += got
        if (p, cell) in LABELS:
            old, new = LABELS[(p, cell)]
            src = nb["cells"][cell]["source"]
            n = sum(l.count(old) for l in src)
            assert n == 1, f"{path} cell {cell}: {n} label sites, expected 1"
            nb["cells"][cell]["source"] = [l.replace(old, new) for l in src]
            labels += 1
    if path == "main.ipynb":
        src = nb["cells"][6]["source"]
        for idx, old, new in PROSE:
            assert src[idx] == old, f"prose line {idx} does not match"
            src[idx] = new
            prose += 1
    print(f"  {path}: {masks} masks, {labels} labels, {prose} prose")
    if not DRY:
        pathlib.Path(path).write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
print("dry run; pass --apply to write" if DRY else "written")
