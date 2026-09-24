"""Build the new Code Cell 2 and Code Cell 2b sources from main.ipynb at HEAD (scratch).

Every cut is by line number of the original Code Cell 2 source, with the boundary lines
asserted by content, so a stale line number fails loudly instead of cutting the wrong text.
"""
import pathlib, subprocess, json, textwrap

S = pathlib.Path(__file__).parent
ROOT = pathlib.Path("/Users/flog/Desktop/predictive coding")
nb = json.loads(subprocess.run(["git", "show", "a202cdb:main.ipynb"], cwd=ROOT,
                               capture_output=True, text=True, check=True).stdout)
src = "".join(nb["cells"][7]["source"])
assert src.startswith("# === Code Cell 2: EVALUATION")
L = src.split("\n")            # L[i - 1] is source line i


def line(i):
    return L[i - 1]


def block(a, b):
    return L[a - 1:b]


def expect(i, text):
    assert line(i).strip().startswith(text), (i, line(i), text)


def dedent(lines, n):
    out = []
    for s in lines:
        assert s[:n].strip() == "", s
        out.append(s[n:])
    return out


def indent(lines, n):
    return [(" " * n + s) if s else s for s in lines]


# ---- boundary checks ----
expect(558, 'print("  above), and that its sign is prior-dependent (Part D).")')
expect(737, "# The delta-like row. Part D's other four priors")
expect(757, "DELTA_ALL_LAMBDA = 8.0 * DELTA_ALL_ALPHA")
expect(760, "def part_d_priors():")
expect(770, "}")
expect(788, "A prior may be given either as a log-density")
expect(790, "Lambda: its whole point is a prior sharp enough to need one.")
expect(912, 'print("  Whether it is met is therefore NOT a property')
expect(914, 'print("  criterion as much as about the model. Text cell 4 Part C reads this.")')
expect(922, "# Lambda is held at this network's own for every prior here, the delta row's")
expect(923, "# included: the comparison is across ell_0 alone")
expect(941, 'print(f"  ell_0-invariance of the phi_S contrasts across these five priors, all at "')
expect(949, "# === is it the prior or the raised Lambda? a control for Part C ===")
expect(961, "print()")
expect(976, "# === the delta-like row, and the headroom that makes it readable ===")
expect(977, 'if "delta (all)" in rows:')
expect(1051, "print()")
expect(1053, "for name, entry in rows.items():")
expect(1062, "# Part D reads the criterion at each prior's learned theta_u*")
expect(1063, "# prior that is theta_u* = 1408")
expect(1074, "# The block ends with one both-conditions configuration run end to end")
expect(1075, "# closed form: Eq. (20) integrated for those updates")
expect(1113, "Returns None where the conjunction fails at theta_u* itself, which is the")
expect(1114, 'four-of-five case of Part D."""')
expect(1172, "def realizability_report(net, priors=None, *, tau_theta=20.0, verbose=True):")
expect(1193, "# === the table of Text cell 4's Integration cost and conditioning (Eq. 28) ===")
expect(1206, "print()")
expect(1208, 'print("REALIZABILITY: WHAT THE CONJUNCTION NEEDS')
expect(1226, "met = [name for name, row in rows.items()")
expect(1232, "print()")
expect(1237, "print()")
expect(1239, "# ---- one both-conditions configuration, end to end")
expect(1249, 'probe = row["network"].respawn()')
expect(1250, 'print(f"  RUN, NOTHING IN CLOSED FORM')
expect(1323, '"closed_form_gap": closed_form_gap}')
expect(1324, "return rows")
expect(1337, "(Appendix A). Rows are the Part D priors at theta_u*, and the delta-like row again at")
expect(1338, "the realizable theta_u of the block above, integrated.")
expect(1356, 'if row["arrival"] is not None:')
expect(1479, '# second figure: "some" under each base world prior (Part D).')
expect(1488, "}")
expect(1513, "# third figure: the delta-like row of Part D")
expect(1557, "plt.show()")
expect(1437, "realizability = realizability_report(evaluation_network)")

# ---- pieces that move to Code Cell 2b ----
constants = block(737, 757)
constants = [s.replace("Part D's other four priors", "Part D's four priors")
              .replace("the case Code Cell 3 is built around", "the case Code Cell 4 is built around")
             for s in constants]
control = dedent(block(949, 961), 4)
delta_block = dedent(block(978, 1051), 8)
run_body = block(1250, 1323)
cost_table = block(1194, 1206)

# ---- the new Code Cell 2, assembled from the bottom up so line numbers stay valid ----
new = list(L)


def replace(a, b, lines):
    new[a - 1:b] = lines


# figures: drop the third, reword the second's comment
replace(1513, 1558, [])
replace(1479, 1488, [
    '    # second figure: "some" under each base world prior (Part D). Each panel carries its',
    "    # own prior, so the gray line differs from panel to panel. Panels on a shared y-axis",
    "    # have to be comparable, so only rows sharing this network's Lambda are drawn; Part",
    "    # D's all do. The same priors at a strong Lambda are Code Cell 2b's.",
    "    comparable = {",
    '        name: entry for name, entry in prior_rows.items()',
    '        if entry["lexical_strength"] == evaluation_network.lexical_strength',
    "    }",
])
replace(1437, 1437, ["integration_cost_report(evaluation_network)",
                     "realizability = realizability_report(evaluation_network)"])
replace(1356, 1356, ['        if row.get("run") is not None:'])
replace(1337, 1338, [
    "    (Appendix A). Rows are the given priors at theta_u*, and again at the realizable",
    "    theta_u of the block above, integrated, for every row that block ran end to end.\"\"\"",
])

realizability = [
    "def integration_cost_report(net):",
    '    """The table of Text cell 4\'s Integration cost and conditioning (Eq. 28), at this',
    '    network\'s theta_u*."""',
] + cost_table + [
    "",
    "",
    "def realizability_report(net, priors=None, *, tau_theta=20.0, verbose=True):",
    '    """What the conjunction costs, against what theta_u* costs, on the given rows',
    '    (Part D\'s by default)."""',
] + block(1174, 1191) + [""] + block(1208, 1229) + [
    "    if met:",
] + indent(block(1230, 1237), 4) + [
    "    else:",
    "        print()",
    "",
    "    # ---- each both-conditions configuration, end to end, nothing in closed form ----",
    "    # Every row with a threshold is run where the theta_u its flow arrives at is",
    "    # integrable; a row that is not is named.",
    "    for name in met:",
    '        arrival = rows[name]["arrival"]',
    '        if arrival is None or arrival["rate"] > FEASIBLE_STIFFNESS:',
    '            reason = ("not passed within the updates tried" if arrival is None else',
    "                      f\"at lambda_max(H) = {arrival['rate']:.1e}, above {FEASIBLE_STIFFNESS:.0e}\")",
    '            print(f"  \\"{name}\\" is not run end to end: its arrival theta_u is {reason}.")',
    "            print()",
    "    for name in met:",
    '        row, arrival = rows[name], rows[name]["arrival"]',
    '        if arrival is None or arrival["rate"] > FEASIBLE_STIFFNESS:',
    "            continue",
    '        probe = row["network"].respawn()',
] + indent(run_body, 4) + [
    "    return rows",
]
replace(1172, 1324, realizability)

replace(1113, 1114, [
    "    Returns None where the conjunction fails at theta_u* itself, as it does under every",
    '    prior of Part D."""',
])
replace(1074, 1075, [
    "# The block ends with each both-conditions configuration run end to end with nothing in",
    "# closed form, where its arrival is integrable: Eq. (20) integrated for those updates,",
    "# with the fast subsystem integrated",
])
replace(1062, 1063, [
    "# The criterion is read at each prior's learned theta_u*. Under the delta-like prior of",
    "# Code Cell 2b that is theta_u* = 1408, where lambda_max(H) = 2.0e6 and one inference is hours:",
])
replace(976, 1052, [])          # the delta-like row's blocks, and the blank line after them
replace(949, 962, [])           # the raised-Lambda control, and its blank line
replace(941, 941, [
    '        print(f"  ell_0-invariance of the phi_S contrasts across these '
    '{count_in_words(len(fields))} priors, all at "'
])
replace(922, 923, [
    "        # Lambda is held at this network's own for every prior here, whatever Lambda the",
    "        # rows carry: the comparison is across ell_0 alone, and phi_L must not move with it.",
])
replace(912, 914, [
    "        if 0 < len(first) < len(rows) or 0 < len(both) < len(rows):",
] + indent(block(912, 914), 4))
replace(788, 790, [
    "    A prior may be given either as a log-density or as a (log_density, overrides) pair,",
    "    the overrides passed on to `respawn`. That is how Code Cell 2b gives every row a",
    "    Lambda of its own.",
])
replace(737, 770, [
    "def part_d_priors():",
    '    """The rows Part D sweeps: the four base world priors, all at this network\'s Lambda.',
    "    Shared with the realizability block below, so the two report the same configurations.",
    "    The delta-like prior, which needs a Lambda of its own, is Code Cell 2b's.\"\"\"",
    "    return dict(BASE_WORLD_PRIORS)",
])
replace(558, 558, ['        print("  above), and that its sign is prior-dependent (Code Cell 2b).")'])

# helper for printed counts, after describe_theta
i = new.index("def settle(net, utterance, theta_u=None):")
new[i:i] = [
    "def count_in_words(n):",
    '    """A small count spelled out, for printed sentences."""',
    '    words = ("none", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")',
    "    return words[n] if 0 <= n < len(words) else str(n)",
    "",
    "",
]
cell2 = "\n".join(new)
(S / "new_cell2.py").write_text(cell2)

# ---- Code Cell 2b ----
template = (S / "cell2b_template.py").read_text()
cell2b = (template
          .replace("#{{CONSTANTS}}", "\n".join(constants))
          .replace("    #{{CONTROL}}", "\n".join(control))           # already at 4 spaces
          .replace("    #{{DELTA_BLOCK}}", "\n".join(delta_block)))  # already at 4 spaces
compile(cell2b, "new_cell2b.py", "exec")
compile(cell2, "new_cell2.py", "exec")
assert "{{" not in cell2b
(S / "new_cell2b.py").write_text(cell2b)
print("new Code Cell 2:", len(cell2.split("\n")), "lines (was", len(L), "); Code Cell 2b:",
      len(cell2b.split("\n")), "lines")
