"""T3 acceptance: every number in the audit outputs' rows appears in the same row of Sec. 8's output. Scratch."""
import re
new = open("2026-09-14-utility-split/test_output.txt").read().splitlines()
num = lambda l: re.findall(r"[-+]?\d+\.\d+(?:e[-+]\d+)?|(?<![\w.])[-+]?\d+(?![\w.])", l)
def row(lines, key, after=None):
    start = 0 if after is None else next(i for i, l in enumerate(lines) if after in l)
    return next(l for l in lines[start:] if l.strip().startswith(key))
failures = 0
mm = open("2026-09-13-delta-criteria/mode_mechanism_output.txt").read().splitlines()
hc = open("2026-09-13-delta-criteria/halving_check_output.txt").read().splitlines()
for name in ("gaussian", "flat", "skewed low", "skewed high"):
    old = num(row(mm, name).split("(span")[0])
    got = {float(x) for x in num(row(new, name, "Block 1.")) + num(row(new, name, "Modes in s")) + num(row(new, name, "All-region"))}
    resid = re.search(r"residual ([\d.e+-]+)\)", row(mm, name)).group(1)
    missing = [x for x in old + [resid] if float(x) not in got]
    old_h = num(row(hc, name))
    got_h = set(num(row(new, name, "Part D's priors at Lambda")))
    missing_h = [x for x in old_h if x not in got_h]
    print(name, "mode_mechanism missing:", missing, "| halving missing:", missing_h)
    failures += bool(missing) + bool(missing_h)
for a, b in (("largest span-B residual", "largest span-B residual"), ("sign of the coefficients", "signs of the coefficients"),
             ("mode of the model", "the model's mode"), ("    up:", "      up:"), ("    down:", "      down:"),
             ("all-region q-mass below", "all-region q-mass below"), ("down cells, where", "in the down cells"),
             ("up cells, where", "in the up cells"), ("B^T W B = I to", "B^T W B = I to"), ("|k - c/2|", "|k - c/2|"),
             ("cells with both columns within 0.1 ", "within 0.1 "), ("within 0.01 ", "within 0.01 "),
             ("within 0.001 ", "within 0.001 "), ("sign(k) = sign(c)", "sign of k = sign of c"), ("sign of c (tilt", "signs of c (tilt"),
             ("mode node of the limit", "limit field's mode node"), ("all four verdicts", "all four the same")):
    o = next(l for l in mm + hc if a in l); g = next(l for l in new if b in l)
    norm = lambda xs: sorted(float(x) for x in xs)
    ok = norm(num(o.replace("(+,+)", "").replace("(+,-)", "").replace("(-,+)", "").replace("(-,-)", "").replace("0.1 ", "").replace("0.01 ", "").replace("0.001 ", ""))) == \
         norm(num(g.replace("(+,+)", "").replace("(+,-)", "").replace("(-,+)", "").replace("(-,-)", "").replace("0.1 ", "").replace("0.01 ", "").replace("0.001 ", "")))
    if not ok:
        print("MISMATCH", a, "|", o.strip(), "||", g.strip()); failures += 1
for table_old, table_new, width in ((mm, "the 21 cells", 21), (hc, "the ten cells furthest", 10)):
    so = next(i for i, l in enumerate(table_old) if ("the 21 cells" in l if width == 21 else "ten cells furthest" in l)) + 2
    sn = next(i for i, l in enumerate(new) if table_new in l) + 2
    for o, g in zip(table_old[so:so + width], new[sn:sn + width]):
        if [float(x) for x in num(o)] != [float(x) for x in num(g)][:len(num(o))] and not all(x in num(g) for x in num(o)):
            print("MISMATCH row", o.strip(), "||", g.strip()); failures += 1
print("ACCEPTANCE", "PASS" if failures == 0 else f"FAIL ({failures})")
