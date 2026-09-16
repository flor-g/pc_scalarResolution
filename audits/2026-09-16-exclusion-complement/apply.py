"""Apply the complement fix to exclusion_indicator in both notebooks.

Requires the replacement to land exactly once per notebook, and leaves every other
byte of the file alone. Run from the project root.
"""
import json, pathlib, sys

OLD = [
    '    # signed distance into the excluded region, positive where excluded\n',
    '    if utterance == "no":\n',
    '        margin = zeta + theta_L\n',
    '    elif utterance == "some":\n',
    '        margin = -(zeta + theta_L)\n',
    '    else:  # "all"\n',
    '        margin = theta_L - zeta\n',
    '\n',
    '    if sharpness is None:\n',
    '        return (margin > 0).to(zeta.dtype)\n',
    '    return torch.sigmoid(margin / sharpness)\n',
]

NEW = [
    '    # Signed distance into the excluded region, positive where excluded. "some" has\n',
    '    # no margin of its own: E_some is the complement of E_no (Eq. 5), so chi_some is\n',
    '    # built as 1 - chi_no. That holds chi_no + chi_some = 1 at every node, the\n',
    '    # boundary zeta = -theta_L included, as Eq. (A1) states it and Eq. (C1) requires;\n',
    '    # a margin of its own would need a non-strict test the shared step cannot express.\n',
    '    complement = utterance == "some"\n',
    '    if utterance == "all":\n',
    '        margin = theta_L - zeta\n',
    '    else:  # "no", and "some" through its complement\n',
    '        margin = zeta + theta_L\n',
    '\n',
    '    if sharpness is None:\n',
    '        chi = (margin > 0).to(zeta.dtype)\n',
    '    else:\n',
    '        chi = torch.sigmoid(margin / sharpness)\n',
    '    return 1.0 - chi if complement else chi\n',
]

TARGETS = (("main.ipynb", 5), ("appendix_E.ipynb", 2))


def apply(path, cell_index, dry_run):
    nb = json.loads(pathlib.Path(path).read_text())
    src = nb["cells"][cell_index]["source"]
    hits = [i for i in range(len(src) - len(OLD) + 1) if src[i:i + len(OLD)] == OLD]
    if len(hits) != 1:
        raise SystemExit(f"{path}: expected exactly one site, found {len(hits)}")
    i = hits[0]
    if not dry_run:
        nb["cells"][cell_index]["source"] = src[:i] + NEW + src[i + len(OLD):]
        pathlib.Path(path).write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
    return i


if __name__ == "__main__":
    dry = "--apply" not in sys.argv
    for path, cell in TARGETS:
        at = apply(path, cell, dry)
        print(f"  {'would patch' if dry else 'patched'} {path} cell {cell} at source line {at}")
    print("dry run; pass --apply to write" if dry else "written")
