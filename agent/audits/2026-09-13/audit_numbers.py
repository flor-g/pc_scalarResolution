"""Audit helper: (1) every constant/default in the code cells; (2) every number quoted in prose vs stored outputs."""
import ast, glob, json, os, re, sys
C = sys.argv[1]; OUT = sys.argv[2]
REACH = "procedure_records/theta_u_learned_reach.md"

# ---------- (1) constants and defaults ----------
with open(f"{OUT}/constants.txt", "w") as fh:
    for f in ["m05.py", "m07.py", "m09.py", "m11.py", "e02.py", "e03.py", "e04.py"]:
        tree = ast.parse(open(f"{C}/{f}").read())
        fh.write(f"===== {f}\n")
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef,)):
                a = node.args
                pos = a.args[len(a.args) - len(a.defaults):] if a.defaults else []
                items = [(p.arg, d) for p, d in zip(pos, a.defaults)]
                items += [(p.arg, d) for p, d in zip(a.kwonlyargs, a.kw_defaults) if d is not None]
                for name, d in items:
                    try: val = ast.unparse(d)
                    except Exception: val = "?"
                    if name in ("self", "verbose"): continue
                    fh.write(f"  L{node.lineno:4d} def {node.name}: {name}={val}\n")
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        fh.write(f"  L{node.lineno:4d} MODULE {t.id} = {ast.unparse(node.value)[:90]}\n")
        # numeric literals inside function bodies (non-trivial)
        lits = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
                v = node.value
                if v in (0, 1, 2, -1, 0.5, 1.0, 0.0, 2.0, 3): continue
                lits.setdefault(repr(v), []).append(node.lineno)
        fh.write("  numeric literals: " + "; ".join(f"{k}@{','.join(map(str,v[:6]))}" for k, v in sorted(lits.items(), key=lambda kv: kv[1][0])) + "\n")

# ---------- (2) prose numbers vs outputs ----------
num_re = re.compile(r"-?\d+(?:,\d{3})*(?:\.\d+)?(?:[eE][-+]?\d+)?")
def floats(text):
    out = []
    t = re.sub(r"(\d+(?:\.\d+)?)\s*\\times\s*10\^\{?(-?\d+)\}?", r"\1e\2", text)
    t = t.replace("−", "-")
    for m in num_re.finditer(t):
        s = m.group().replace(",", "")
        try: out.append(float(s))
        except ValueError: pass
    return out
def keyset(vals):
    ks = set()
    for v in vals:
        a = abs(v)
        for k in range(0, 7): ks.add(("f", k, f"{a:.{k}f}"))
        if a != 0:
            for s in range(1, 7): ks.add(("e", s, f"{a:.{s-1}e}"))
    return ks
outs = ""
for f in sorted(glob.glob(f"{C}/*.out.txt")): outs += open(f).read() + "\n"
OUTK = keyset(floats(outs))
REACHK = keyset(floats(open(REACH).read()))

skip_ctx = re.compile(r"(§|Sec\.?\s*|Secs\.?\s*|Section\s*|Sections\s*|Eqs?\.\s*\(?|Part\s|cell\s|Cell\s|Appendix\s|outline\s|pp\.\s*|vol\.\s*|\(\d{4}|Fig\.\s*|T\d+\.|F\d)$")
tok_re = re.compile(r"(\d+(?:\.\d+)?)\s*\\times\s*10\^\{?(-?\d+)\}?|(?<![\w.$\\{])(\d{1,3}(?:,\d{3})+|\d+\.\d+(?:[eE][-+]?\d+)?|\d+[eE][-+]?\d+)(?![\w.])")
rows = []; tally = {}
for f in sorted(glob.glob(f"{C}/m*.md")) + sorted(glob.glob(f"{C}/e*.md")):
    name = os.path.basename(f)
    text = open(f).read()
    # the table of contents and the reference lists carry section numbers and DOIs, not results
    if 'id="toc"' in text or 'id="references"' in text or text.startswith("## References"):
        continue
    for m in tok_re.finditer(text):
        pre = text[max(0, m.start() - 14):m.start()]
        if skip_ctx.search(pre): continue
        if m.group(1):
            mant, ex = m.group(1), int(m.group(2)); s = len(mant.replace(".", "").lstrip("0")) or 1
            key = ("e", s, f"{float(mant+'e'+str(ex)):.{s-1}e}")
            shown = f"{mant}e{ex}"
        else:
            g = m.group(3)
            if re.fullmatch(r"\d{1,3}(?:,\d{3})+", g):
                key = ("f", 0, g.replace(",", "")); shown = g
            elif "e" in g.lower():
                mant = g.lower().split("e")[0]; s = len(mant.replace(".", "").lstrip("0")) or 1
                key = ("e", s, f"{float(g):.{s-1}e}"); shown = g
            else:
                k = len(g.split(".")[1]); key = ("f", k, g); shown = g
                # decimals that look like section numbers (x.y with small ints and no leading zero) inside headings are skipped above
        status = "out" if key in OUTK else ("reach" if key in REACHK else "NONE")
        tally.setdefault(name, {"out": 0, "reach": 0, "NONE": 0})[status] += 1
        if status != "out":
            line = text.count("\n", 0, m.start()) + 1
            ctx = text[max(0, m.start() - 60):m.end() + 40].replace("\n", " ")
            rows.append(f"{name}:{line}\t{status}\t{shown}\t…{ctx}…")
with open(f"{OUT}/prose_numbers.txt", "w") as fh:
    fh.write("\n".join(rows))
print("cell      in-output  reach-only  none")
for k, v in tally.items(): print(f"{k:9s} {v['out']:9d} {v['reach']:11d} {v['NONE']:5d}")
print("unmatched rows written:", len(rows))
