"""T2 of delta_criteria_printing.md: Code Cell 4 records the modes under "some" and prints the mode criteria."""
import nbformat


def replace_once(text, old, new):
    assert text.count(old) == 1, (text.count(old), old[:80])
    return text.replace(old, new)


nb = nbformat.read("main.ipynb", as_version=4)
cell = nb.cells[13]
assert cell.source.startswith("# === Code Cell 4:")
src = cell.source
assert "mode_model" not in src

src = replace_once(src, '''    grids["stiffness"] = np.full(shape, np.nan)
''', '''    grids["stiffness"] = np.full(shape, np.nan)
    # the delta read-out under "some" (B8): the mode nodes of phi_S*, ell_0 and ell_0 - phi_L, the
    # modes of phi_S* and ell_0 in s, whether phi_S*'s lies outside the cell of "all", and the
    # smallest gap between the two largest nodes of the three fields (argmax takes the first node)
    for field in ("mode_model", "mode_prior", "mode_literal", "mode_s_model", "mode_s_prior",
                  "mode_outside", "mode_gap"):
        grids[field] = np.full(shape, np.nan)
''')

src = replace_once(src, '''                full = probe.read_out(probe.closed_form_fixed_point(utterance)[0])
                base = probe.read_out(probe.literal_fixed_point(utterance))
''', '''                phi_S = probe.closed_form_fixed_point(utterance)[0]
                literal = probe.literal_fixed_point(utterance)
                full = probe.read_out(phi_S)
                base = probe.read_out(literal)
                if utterance == "some":
                    settled_fields = (phi_S, probe.base_log_prior, literal)
                    nodes = [int(torch.argmax(field)) for field in settled_fields]
                    grids["mode_model"][i, j], grids["mode_prior"][i, j], grids["mode_literal"][i, j] = nodes
                    grids["mode_s_model"][i, j] = float(logistic(probe.zeta[nodes[0]]))
                    grids["mode_s_prior"][i, j] = float(logistic(probe.zeta[nodes[1]]))
                    grids["mode_outside"][i, j] = float(float(probe.zeta[nodes[0]]) < probe.theta_L)
                    grids["mode_gap"][i, j] = min(float(torch.topk(field, 2).values.diff().abs())
                                                  for field in settled_fields)
''')

src = replace_once(src, '''        "second_floor": {alphas[i]: floor(second, i) for i in range(len(alphas))},
    }
''', '''        "second_floor": {alphas[i]: floor(second, i) for i in range(len(alphas))},
    }

    # the delta read-out's two criteria under "some" (B8), beside the q criteria. The mode is a
    # grid node, so the mode shift criterion is a node comparison; a mode that does not move has
    # a shift of 0 steps and does not meet it.
    mode_shift = grids["mode_model"] < grids["mode_prior"]
    mode_position = grids["mode_outside"] > 0.5
    mode_both = mode_shift & mode_position
    criteria = {"q shift": first, "q position": second, "q both": both,
                "mode shift": mode_shift, "mode position": mode_position, "mode both": mode_both}
    summary.update({
        "mode_shift": int(mode_shift.sum()),
        "mode_position": int(mode_position.sum()),
        "mode_both": int(mode_both.sum()),
        "floors": {name: {alphas[i]: floor(holds, i) for i in range(len(alphas))}
                   for name, holds in criteria.items()},
    })
''')

src = replace_once(src, '''                          f"{grids['theta_u'][delta, j]:.2f}")
        print()
    return summary
''', '''                          f"{grids['theta_u'][delta, j]:.2f}")
        print()

        print("  THE MODE SHIFT AND MODE POSITION CRITERIA ON THE PLANE, under \\"some\\" (B8), beside the q criteria")
        print("    mode shift: mode(phi_S*) - mode(ell_0) < 0;  mode position: mode(phi_S*) outside the cell of")
        print("    \\"all\\", zeta < theta_L. The mode is the grid node where the field is largest.")
        print(f"    the mode shift criterion is met in {int(mode_shift.sum())} of {len(cells)} cells, the mode "
              f"position criterion in {int(mode_position.sum())}, both in {int(mode_both.sum())}; the q shift "
              f"criterion in {int(first.sum())}, the q position criterion in {int(second.sum())}, both in "
              f"{int(both.sum())}")
        unmoved = int((grids["mode_model"] == grids["mode_prior"]).sum())
        print(f"    the mode of phi_S* is the node of mode(ell_0) in {unmoved} cells, a shift of 0 steps; "
              f"mode(ell_0 - phi_L) differs from mode(ell_0) in "
              f"{int((grids['mode_literal'] != grids['mode_prior']).sum())} cells")
        print(f"    smallest gap between the two largest nodes of phi_S*, ell_0 and ell_0 - phi_L: "
              f"{np.nanmin(grids['mode_gap']):.2e} (no ties)")
        print("    agreement, cell by cell:")
        for label, q, mode in (("the q and mode shift criteria", first, mode_shift),
                               ("the q and mode position criteria", second, mode_position),
                               ("the two conjunctions", both, mode_both)):
            print(f"      {label}: both met {int((q & mode).sum())}, only under q {int((q & ~mode).sum())}, "
                  f"only under the mode {int((~q & mode).sum())}, neither {int((~q & ~mode).sum())}")
        disagree = [c for c in cells if first[c] != mode_shift[c] or second[c] != mode_position[c]]
        yes = lambda flag: "yes" if flag else "no"
        print(f"    the {len(disagree)} cells where a q criterion and its mode counterpart disagree:")
        print(f"      {'alpha':>6}{'Lambda':>7}{'theta_u*':>12}{'P(all|some)':>12}{'shift':>9}{'tempering':>10}"
              f"{'utility':>9}{'mode ell_0':>11}{'mode phi_S*':>12}{'q shift':>8}{'mode shift':>11}"
              f"{'q position':>11}{'mode position':>14}")
        for i, j in disagree:
            print(f"      {alphas[i]:>6.0f}{lambdas[j]:>7.0f}{grids['theta_u'][i, j]:>12.2f}"
                  f"{grids['full_upper']['some'][i, j]:>12.4f}{shift['some'][i, j]:>+9.4f}"
                  f"{tempering['some'][i, j]:>+10.4f}{utility['some'][i, j]:>+9.4f}"
                  f"{grids['mode_s_prior'][i, j]:>11.4f}{grids['mode_s_model'][i, j]:>12.4f}"
                  f"{yes(first[i, j]):>8}{yes(mode_shift[i, j]):>11}{yes(second[i, j]):>11}"
                  f"{yes(mode_position[i, j]):>14}")
        print("    floors by alpha under both read-outs: the least Lambda from which a criterion holds at every")
        print("    larger Lambda on this grid; - where it does not hold at the largest, * where it also holds")
        print("    at some Lambda below its floor")
        names = list(criteria)
        print(f"      {'alpha':>6} |" + "".join(f"{name:>11}" for name in names[:3]) + " |"
              + "".join(f"{name:>14}" for name in names[3:]))
        for i, alpha in enumerate(alphas):
            marks = []
            for name in names:
                value = summary["floors"][name][alpha]
                cut = len(lambdas) if value is None else lambdas.index(value)
                marks.append(("-" if value is None else f"{value:.0f}")
                             + ("*" if criteria[name][i, :cut].any() else ""))
            print(f"      {alpha:>6.0f} |" + "".join(f"{m:>11}" for m in marks[:3]) + " |"
                  + "".join(f"{m:>14}" for m in marks[3:]))
        print()
    return summary
''')

compile(src, "code_cell_4", "exec")
cell.source = src
nbformat.write(nb, "main.ipynb")
print("applied T2; Code Cell 4 now", len(src.splitlines()), "lines")
