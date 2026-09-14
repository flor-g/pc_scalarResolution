# === Code Cell E3: the appendix's only claim, checked ===
#
# Every number Code Cells E2 and E2b printed must be a number main.ipynb already printed.
# That is checkable rather than assertable: main.ipynb stores the output of its own Code
# Cells 2 and 2b, so run the same sequences again with stdout captured and compare the
# texts line by line. Running them twice also shows the runs are deterministic.
#
# Whitespace is normalized and rules of "=" are dropped, because the claim column is
# padded to the width of the longest claim and this appendix adds four longer ones.
# Lines main's cells tag "cost:" are dropped as well: they are wall clock and step
# counts, which belong to the machine and to the integration path rather than to the
# model, and the relay reaches the same fixed point along a slightly different path.
# Nothing else is allowed to differ: against Code Cell 2 the permitted changes are
# exactly the four inserted PASS lines and the pass count; against Code Cell 2b, none.

import contextlib
import difflib
import io
import json
import pathlib
import re

transcript = io.StringIO()
with contextlib.redirect_stdout(transcript):
    probe_network = LexicalPredictiveCodingNetwork()
    check_specification(probe_network)
    demonstrate(probe_network)
    lexical_strength_sweep(probe_network)
    scalar_implicature_probe(probe_network)
    theta_u_learning_probe(probe_network)
    theta_u_dependence(probe_network)
    probe_rows = base_prior_sweep(probe_network)
    integration_cost_report(probe_network)
    delta_readout_report(probe_network, realizability_report(probe_network))

strong_transcript = io.StringIO()
with contextlib.redirect_stdout(strong_transcript):
    strong_probe = strong_lambda_report(probe_network, probe_rows)
    delta_readout_report(strong_probe["network"], strong_probe["realizability"])
    cell_margin_report(strong_probe["realizability"])


def normalize(text):
    """Line list, runs of spaces collapsed and separator rules dropped."""
    kept = []
    for line in text.splitlines():
        line = re.sub(r"\s+", " ", line).strip()
        if line and set(line) != {"="} and not line.startswith("cost:"):
            kept.append(line)
    return kept


BASELINE = pathlib.Path("main.ipynb")
if not BASELINE.exists():
    raise FileNotFoundError(
        "main.ipynb must sit beside this notebook: it is the recorded output "
        "this appendix is checked against."
    )
cells = json.load(BASELINE.open())["cells"]


def stored_output(prefix):
    """Normalized stream output of the one main.ipynb code cell whose source starts with prefix."""
    matches = [cell for cell in cells if cell["cell_type"] == "code"
               and "".join(cell["source"]).startswith(prefix)]
    if len(matches) != 1:
        raise LookupError(f"expected one cell starting {prefix!r} in main.ipynb, found {len(matches)}")
    return normalize("".join("".join(output.get("text", []))
                             for output in matches[0]["outputs"]
                             if output.get("output_type") == "stream"))


def compare(title, baseline, current):
    inserted, deleted, replaced = [], [], []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(
        None, baseline, current, autojunk=False
    ).get_opcodes():
        if tag == "insert":
            inserted += current[j1:j2]
        elif tag == "delete":
            deleted += baseline[i1:i2]
        elif tag == "replace":
            replaced += list(zip(baseline[i1:i2], current[j1:j2]))
    unchanged = len(baseline) - len(deleted) - len(replaced)

    print(title)
    print("=" * 78)
    print(f"  lines recorded in main.ipynb   {len(baseline)}")
    print(f"  lines identical                     {unchanged}")
    print(f"  lines deleted                       {len(deleted)}")
    print(f"  lines changed                       {len(replaced)}")
    print(f"  lines inserted                      {len(inserted)}")
    print("=" * 78)
    if deleted:
        print()
        print("DELETED (must be empty):")
        for line in deleted:
            print("  -", line)
    if replaced:
        print()
        print("CHANGED:")
        for before, after in replaced:
            print("  -", before)
            print("  +", after)
    if inserted:
        print()
        print("INSERTED:")
        for line in inserted:
            print("  +", line)
    print()
    return unchanged, deleted, replaced, inserted


baseline = stored_output("# === Code Cell 2:")
unchanged, deleted, replaced, inserted = compare(
    "APPENDIX E vs main.ipynb, Code Cell 2 output", baseline, normalize(transcript.getvalue())
)

# the pass count main.ipynb recorded, n/n, must become (n + 4)/(n + 4) and nothing else
recorded = next(
    (int(match.group(1)) for line in baseline
     if (match := re.fullmatch(r"(\d+)/\1 passed", line))),
    None,
)
expected_change = (
    recorded is not None
    and len(replaced) == 1
    and replaced[0][0] == f"{recorded}/{recorded} passed"
    and replaced[0][1] == f"{recorded + 4}/{recorded + 4} passed"
)
verdict = (
    not deleted
    and expected_change
    and len(inserted) == 4
    and all(line.startswith("PASS") for line in inserted)
)

strong_unchanged, strong_deleted, strong_replaced, strong_inserted = compare(
    "APPENDIX E vs main.ipynb, Code Cell 2b output",
    stored_output("# === Code Cell 2b:"), normalize(strong_transcript.getvalue())
)
strong_verdict = not (strong_deleted or strong_replaced or strong_inserted)

print("=" * 78)
print(
    f"  {'PASS' if verdict else 'FAIL'}  the relay changes no reported quantity in Code Cell 2: "
    f"{unchanged} lines identical, {len(deleted)} deleted,"
)
print(
    f"        {len(replaced)} changed (the pass count), "
    f"{len(inserted)} inserted (the checks the relay adds)"
)
print(
    f"  {'PASS' if strong_verdict else 'FAIL'}  nor in Code Cell 2b: "
    f"{strong_unchanged} lines identical, {len(strong_deleted)} deleted, "
    f"{len(strong_replaced)} changed, {len(strong_inserted)} inserted"
)
print("=" * 78)

if not (verdict and strong_verdict):
    raise AssertionError(
        "Appendix E must reproduce main.ipynb exactly apart from the four added "
        "checks and the pass count; see the report above."
    )
