

# ---- Sec. 8: the utility field under "some", split into tilt and width ----
#
# By Eq. (23) the utility field phi_S* - phi_S*(theta_u = 0) lies in span B: one coefficient on B's
# odd column (tilt) and one on its even column (width). Each part is added alone to the tempered
# control; those two fields are counterfactual, not states of the network. The limit field is the
# right-hand side of Eq. (24). Coefficients are at each configuration's own Lambda and theta_u*, not
# per unit Lambda. Counts over the plane read signs with the 1e-12 zero band.


def utility_split_report(net, priors, alphas, lambdas):
    ROUNDOFF = 1e-12
    parity = []
    for j in range(net.num_basis):
        column = net.basis[:, j]
        parity.append("odd" if float((column + column.flip(0)).abs().max()) < 1e-9
                      else "even" if float((column - column.flip(0)).abs().max()) < 1e-9 else "mixed")
    if sorted(parity) != ["even", "odd"]:
        raise RuntimeError(f"Sec. 8 needs one odd and one even column of B, found {parity}")
    TILT, WIDTH = parity.index("odd"), parity.index("even")
    PARTS = ("tempered", "tilt", "width", "model")
    CRITERIA = ("mode shift", "mode position", "q shift", "q position")

    def split(probe):
        if not probe.sigma_lexical == probe.sigma_state == probe.sigma_utility == 1.0:
            raise RuntimeError("Sec. 8's exact form is written at sigma = 1")
        B, w, theta = probe.basis, probe.weights, float(probe.theta_u)
        gram = B.T @ (w[:, None] * B)
        literal = probe.literal_fixed_point("some")
        phi_S = probe.closed_form_fixed_point("some")[0]
        tempered = probe.closed_form_fixed_point("some", theta_u=0.0)[0]
        utility = phi_S - tempered
        k = torch.linalg.solve(gram, probe.project(utility))
        c = probe.project(literal)
        exact = (theta / 2) * (probe.mu_u + (theta / 2) * c) / (1 + theta ** 2 / 2)
        fields = {"tempered": tempered, "tilt": tempered + B[:, TILT] * k[TILT],
                  "width": tempered + B[:, WIDTH] * k[WIDTH], "model": phi_S,
                  "limit": tempered + B @ (c / 2)}
        upper = (probe.zeta > probe.theta_L).to(probe.dtype)

        def mass(field):
            return float((w * probe.read_out(field) * upper).sum())

        node = {key: int(torch.argmax(field)) for key, field in fields.items()}
        masses = {key: mass(field) for key, field in fields.items()}
        literal_mass = mass(literal)
        k0 = int(torch.argmax(probe.base_log_prior))
        at = min(max(node["tempered"], 1), len(probe.zeta) - 2)

        def slope(field):
            return float(field[at + 1] - field[at - 1]) / float(probe.zeta[at + 1] - probe.zeta[at - 1])

        def criteria(key):
            return (node[key] < k0, float(probe.zeta[node[key]]) < probe.theta_L,
                    masses[key] - literal_mass < -ROUNDOFF, masses[key] < 0.5)

        return {
            "theta": theta, "k": (float(k[TILT]), float(k[WIDTH])), "c": (float(c[TILT]), float(c[WIDTH])),
            "relative": tuple(abs(float(k[j] - c[j] / 2)) / abs(float(c[j] / 2)) for j in (TILT, WIDTH)),
            "residual": float((utility - B @ k).abs().max()),
            "gram_error": float((gram - torch.eye(gram.shape[0], dtype=gram.dtype)).abs().max()),
            "exact_error": float((k - exact).abs().max()) / max(1.0, float(k.abs().max())),
            "node": node, "k0": k0, "s": {key: float(logistic(probe.zeta[n])) for key, n in node.items()},
            "mass": masses, "literal_mass": literal_mass,
            "slope": (slope(B[:, TILT] * k[TILT]), slope(B[:, WIDTH] * k[WIDTH])),
            "criteria": {key: criteria(key) for key in ("model", "limit")},
        }

    def direction(a, b):
        return (a > b) - (a < b)

    step = float(net.zeta[1] - net.zeta[0])
    part_d = {name: split(net.respawn(base_prior=prior)) for name, prior in priors.items()}
    plane = []
    for alpha in alphas:
        for strength in lambdas:
            row = split(net.respawn(base_prior=beta_world_prior(alpha, 1.0), lexical_strength=strength))
            row["alpha"], row["Lambda"] = alpha, strength
            plane.append(row)

    print("APPENDIX C, Sec. 8: THE UTILITY FIELD UNDER \"some\", SPLIT INTO TILT (odd b_1) AND WIDTH (even b_2)")
    print("  Each configuration at its own Lambda and theta_u*. \"+ tilt\" and \"+ width\" add that part alone to")
    print("  the tempered control (theta_u = 0); they are counterfactual fields, not states of the network.")
    print()

    print(f"  Block 1. PART D'S PRIORS AT Lambda = {net.lexical_strength:g}")
    print(f"    {'prior':<13}{'theta_u*':>10}{'tilt':>9}{'width':>9}{'span-B residual':>17}"
          f"{'slope of tilt':>15}{'slope of width':>16}   (slopes at the tempered control's mode)")
    for name, row in part_d.items():
        print(f"    {name:<13}{row['theta']:>10.2f}{row['k'][0]:>+9.2f}{row['k'][1]:>+9.2f}{row['residual']:>17.1e}"
              f"{row['slope'][0]:>+15.3f}{row['slope'][1]:>+16.3f}")
    print("    Modes in s, and in grid steps from the tempered control's mode; multiplying the steps by the")
    print(f"    grid spacing, {step:.2f}, recovers the distance in zeta.")
    print(f"    {'prior':<13}{'tempered':>9}{'+ tilt':>9}{'steps':>7}{'+ width':>9}{'steps':>7}{'model':>9}{'steps':>7}")
    for name, row in part_d.items():
        s, n = row["s"], row["node"]
        print(f"    {name:<13}{s['tempered']:>9.4f}"
              + "".join(f"{s[key]:>9.4f}{n[key] - n['tempered']:>+7d}" for key in ("tilt", "width", "model")))
    print("    All-region q-mass, zeta > theta_L (Eq. 27)")
    print(f"    {'prior':<13}{'q_lit':>9}{'tempered':>10}{'+ tilt':>9}{'+ width':>9}{'model':>9}")
    for name, row in part_d.items():
        print(f"    {name:<13}{row['literal_mass']:>9.4f}"
              + "".join(f"{row['mass'][key]:>{10 if key == 'tempered' else 9}.4f}" for key in PARTS))
    print(f"    the tempered control's mode node is ell_0's under every prior: "
          f"{all(row['node']['tempered'] == row['k0'] for row in part_d.values())}")
    print()

    n = len(plane)
    print(f"  Block 2. THE PLANE, {n} cells (alpha, Lambda) of Code Cell 4")
    print(f"    largest span-B residual of the utility field: {max(row['residual'] for row in plane):.1e}")
    sign = lambda x: "+" if x > ROUNDOFF else "-" if x < -ROUNDOFF else "0"
    print("    signs of the coefficients (tilt, width): "
          + ", ".join(f"({a},{b}) {sum(1 for row in plane if (sign(row['k'][0]), sign(row['k'][1])) == (a, b))}"
                      for a in "+-" for b in "+-"))
    print(f"    the tempered control's mode node is ell_0's in {sum(1 for row in plane if row['node']['tempered'] == row['k0'])}"
          f" of {n} cells")
    groups = {label: [row for row in plane if direction(row["node"]["model"], row["node"]["tempered"]) == d]
              for label, d in (("up", 1), ("down", -1), ("unmoved", 0))}
    print("    the model's mode against the tempered control's: "
          + ", ".join(f"{label} {len(group)}" for label, group in groups.items()))
    for label, d in (("up", 1), ("down", -1)):
        group = groups[label]
        tilt = sum(1 for row in group if direction(row["node"]["tilt"], row["node"]["tempered"]) == d)
        width = sum(1 for row in group if direction(row["node"]["width"], row["node"]["tempered"]) == d)
        first = sum(1 for row in group if direction(row["slope"][0] + row["slope"][1], 0.0) == d)
        print(f"      {label}: the tilt part alone moves it the same way in {tilt}, the width part alone in {width};"
              f" the sign of the two parts' summed slope agrees in {first} of {len(group)}")
    print("    all-region q-mass below the tempered control's: "
          + ", ".join(f"{label} {sum(1 for row in plane if row['mass'][key] < row['mass']['tempered'] - ROUNDOFF)}"
                      for label, key in (("+ tilt", "tilt"), ("+ width", "width"), ("model", "model"))))
    for label in ("up", "down"):
        print(f"    where the tempered control's mode sits in the {label} cells (s): "
              + ", ".join(f"{s:.4f}" for s in sorted({round(row['s']['tempered'], 4) for row in groups[label]})))
    split_cells = [row for row in plane if row["criteria"]["model"][2] and not row["criteria"]["model"][0]]
    print(f"    the {len(split_cells)} cells where the q shift criterion is met and the mode shift criterion is not:")
    print(f"      {'alpha':>6}{'Lambda':>7}{'tilt':>9}{'width':>9} | {'mode, s:':<9}{'tempered':>9}{'+ tilt':>8}"
          f"{'+ width':>8}{'model':>8} | {'q-mass:':<8}{'tempered':>9}{'+ tilt':>8}{'+ width':>8}{'model':>8}")
    for row in split_cells:
        print(f"      {row['alpha']:>6.0f}{row['Lambda']:>7.0f}{row['k'][0]:>+9.2f}{row['k'][1]:>+9.2f} | {'':<9}"
              + "".join(f"{row['s'][key]:>{9 if key == 'tempered' else 8}.4f}" for key in PARTS) + f" | {'':<8}"
              + "".join(f"{row['mass'][key]:>{9 if key == 'tempered' else 8}.4f}" for key in PARTS))
    print()

    print("  Block 3. THE HALVING OF Eq. (24): the utility coefficients k against half the literal field's, c/2,")
    print("  with c = B^T W (ell_0 - phi_L). At sigma = 1 and B^T W B = I, Eqs. (15)-(16) give exactly")
    print("  k = (theta_u/2)(mu_u + (theta_u/2) c) / (1 + theta_u^2/2). The limit field is ell_0 - phi_L, halved,")
    print("  plus B c/2.")
    print(f"    B^T W B = I to {max(row['gram_error'] for row in plane):.1e}; k against the exact form to "
          f"{max(row['exact_error'] for row in plane):.1e} (relative)")
    tilt_rel = sorted(row["relative"][0] for row in plane)
    width_rel = sorted(row["relative"][1] for row in plane)
    print(f"    |k - c/2| / |c/2|: tilt largest {tilt_rel[-1]:.2e}, median {tilt_rel[n // 2]:.2e}; "
          f"width largest {width_rel[-1]:.2e}, median {width_rel[n // 2]:.2e}")
    for bound in (1e-1, 1e-2, 1e-3):
        print(f"      cells with both columns within {bound:g} of c/2: "
              f"{sum(1 for row in plane if max(row['relative']) < bound)}")
    print(f"    sign of k = sign of c in both columns: "
          f"{sum(1 for row in plane if all(sign(a) == sign(b) for a, b in zip(row['k'], row['c'])))} of {n}")
    print("    signs of c (tilt, width): "
          + ", ".join(f"({a},{b}) {sum(1 for row in plane if (sign(row['c'][0]), sign(row['c'][1])) == (a, b))}"
                      for a in "+-" for b in "+-"))
    print(f"    the limit field's mode node is the model's in "
          f"{sum(1 for row in plane if row['node']['limit'] == row['node']['model'])} of {n} cells; largest gap "
          f"{max(abs(row['node']['limit'] - row['node']['model']) for row in plane)} nodes")
    for index, label in enumerate(CRITERIA):
        print(f"    the {label} criterion reads the same off the limit field as off the model in "
              f"{sum(1 for row in plane if row['criteria']['limit'][index] == row['criteria']['model'][index])} of {n}")
    print(f"    all four the same: {sum(1 for row in plane if row['criteria']['limit'] == row['criteria']['model'])} of {n}")

    def halving_row(label, row):
        print(f"      {label}{row['theta']:>11.2f}{row['c'][0]:>+10.2f}{row['c'][1]:>+10.2f}{row['k'][0]:>+10.2f}"
              f"{row['k'][1]:>+10.2f}{row['relative'][0]:>9.1e}{row['relative'][1]:>9.1e}{row['s']['model']:>8.4f}"
              f"{row['s']['limit']:>9.4f}{row['mass']['model']:>8.4f}{row['mass']['limit']:>9.4f}"
              f"{'yes' if row['criteria']['limit'] == row['criteria']['model'] else 'no':>12}")

    columns = (f"{'theta_u*':>11}{'c tilt':>10}{'c width':>10}{'k tilt':>10}{'k width':>10}{'rel tilt':>9}"
               f"{'rel wid':>9}{'mode':>8}{'mode lim':>9}{'mass':>8}{'mass lim':>9}{'same four':>12}")
    print("    the ten cells furthest from the halving (the larger of the two relative distances):")
    print(f"      {'alpha':>6}{'Lambda':>7}" + columns)
    for row in sorted(plane, key=lambda row: -max(row["relative"]))[:10]:
        halving_row(f"{row['alpha']:>6.0f}{row['Lambda']:>7.0f}", row)
    print(f"    Part D's priors at Lambda = {net.lexical_strength:g} (modes in s; \"lim\" is the limit field):")
    print(f"      {'prior':<13}" + columns)
    for name, row in part_d.items():
        halving_row(f"{name:<13}", row)
    print()
