# === Code Cell 2b: EVALUATION, Part D's priors at a strong Lambda ===
#
# Part D's four base world priors and the delta-like prior, all at Lambda = 512, each
# configuration at its own learned theta_u* (Text cell 4b). Code Cell 2's functions do
# the measuring; this cell supplies the rows, the blocks about the delta-like row, and
# the figures.

import math
import torch


# ============================================================================
# THE STRONG LAMBDA
# ============================================================================

#{{CONSTANTS}}

# Every row of this cell carries that Lambda. At Part D's own Lambda the diffuse priors
# override the entries for "no" and "all" (Code Cell 2 prints the leak), so the same
# priors are read again here with every entry holding.
STRONG_LAMBDA = DELTA_ALL_LAMBDA


def delta_like_row():
    """The delta-like row, with the Lambda it needs (the derivation above)."""
    return {"delta (all)": (beta_world_prior(DELTA_ALL_ALPHA, 1.0),
                            {"lexical_strength": DELTA_ALL_LAMBDA})}


def strong_lambda_priors():
    """Part D's priors and the delta-like row, every one at STRONG_LAMBDA."""
    rows = {name: (prior, {"lexical_strength": STRONG_LAMBDA})
            for name, prior in part_d_priors().items()}
    return {**rows, **delta_like_row()}


def strong_lambda_comparison(base_rows, rows):
    """Each prior at Part D's Lambda beside the same prior at STRONG_LAMBDA, under "some"."""
    print(f"  THE SAME PRIORS AT PART D'S LAMBDA AND AT LAMBDA = {STRONG_LAMBDA:.0f}, under \"some\"")
    print(f"    {'prior':<13}{'Lambda':>8}{'theta_u*':>12}{'shift':>10}{'P(all|some)':>13}"
          f"{'max leak':>11}{'first':>7}{'second':>8}")
    for name, entry in rows.items():
        pairs = ([base_rows[name]] if name in base_rows else []) + [entry]
        for i, row in enumerate(pairs):
            some = row["utterances"]["some"]
            leak = max(row["utterances"][y]["leak"] for y in UTTERANCES)
            print(f"    {(name if i == 0 else ''):<13}{row['lexical_strength']:>8.0f}"
                  f"{row['theta_u']:>12.4f}{some['shift']:>+10.4f}{some['full_upper']:>13.4f}"
                  f"{leak:>11.1e}{('met' if some['shift'] < 0 else '-'):>7}"
                  f"{('met' if some['full_upper'] < 0.5 else '-'):>8}")
    print("    (first: shift for \"some\" < 0; second: P(all-region | \"some\") < 1/2. The")
    print("     delta-like prior has no row at Part D's Lambda, since it needs this one.)")
    print()


def headroom_report(rows):
    """Room to fall and to rise in all-region mass, for every row and utterance."""
    print("  HEADROOM, EVERY ROW. A zero shift where q_lit holds none of the all-region, or all")
    print("  of it, is saturation and not restraint, so read these columns before the shifts.")
    print(f"    {'prior':<13}{'utterance':<10}{'P(all) base':>13}{'P(all) full':>13}{'shift':>10}"
          f"{'room to fall':>14}{'room to rise':>14}")
    for name, entry in rows.items():
        for y in UTTERANCES:
            row = entry["utterances"][y]
            print(f"    {(name if y == UTTERANCES[0] else ''):<13}{y:<10}"
                  f"{row['baseline_upper']:>13.6f}{row['full_upper']:>13.6f}{row['shift']:>+10.4f}"
                  f"{row['baseline_upper']:>14.2e}{1.0 - row['baseline_upper']:>14.2e}")
    print()


def delta_like_row_report(net, rows):
    """The delta-like row's headroom and mechanism (Text cell 4 Part C, Eqs. 23-24).

    `net` is the default network: Eq. (23) is also checked at its theta_u*."""
    upper_region = (net.zeta > net.theta_L).to(net.dtype)
    #{{DELTA_BLOCK}}


def raised_lambda_control(net, rows):
    """The default Gaussian prior at the delta-like row's Lambda, against Part D's row."""
    upper_region = (net.zeta > net.theta_L).to(net.dtype)
    #{{CONTROL}}


def strong_lambda_report(net, base_rows):
    """Part D's evaluations with every prior at STRONG_LAMBDA.

    `net` is the default network and `base_rows` Part D's rows from `base_prior_sweep`.
    Returns the strong network, its rows, and its realizability rows."""
    strong = net.respawn(lexical_strength=STRONG_LAMBDA)
    priors = strong_lambda_priors()
    print(f"PART D AT A STRONG LAMBDA: EVERY PRIOR AT LAMBDA = {STRONG_LAMBDA:.0f}")
    print()
    rows = base_prior_sweep(strong, priors)
    strong_lambda_comparison(base_rows, rows)
    headroom_report(rows)
    delta_like_row_report(net, rows)
    raised_lambda_control(net, base_rows)
    realizability = realizability_report(strong, priors)
    return {"network": strong, "rows": rows, "realizability": realizability}


def cell_margin_report(realizability):
    """How far below the cell of "all" the peak of phi_S*("some") sits, every row at theta_u*."""
    print("  THE PEAK OF phi_S*(\"some\") AGAINST THE CELL OF \"all\", every row at theta_u*")
    print(f"    {'prior':<13}{'peak (s)':>10}{'nodes below':>13}{'inside against outside':>24}")
    for name, row in realizability.items():
        probe = row["network"]
        phi_S = probe.closed_form_fixed_point("some")[0]
        k = int(torch.argmax(phi_S))
        inside = probe.zeta >= probe.theta_L
        first_inside = int(torch.nonzero(inside)[0])
        margin = float(phi_S[inside].max() - phi_S[~inside].max())
        print(f"    {name:<13}{float(logistic(probe.zeta[k])):>10.4f}"
              f"{max(0, first_inside - k):>13d}{margin:>+24.3f}")
    print("    (nodes below: grid steps from the peak up to the first node inside the cell, 0 if")
    print("     the peak is inside it; the last column is the largest phi_S* inside the cell")
    print("     less the largest outside it)")
    print()


# ============================================================================
# RUN
# ============================================================================

strong = strong_lambda_report(evaluation_network, prior_rows)


# ---- figures ----

try:
    import matplotlib.pyplot as plt

    strong_network, strong_rows = strong["network"], strong["rows"]
    proportion = logistic(strong_network.zeta).numpy()
    ds_dzeta = proportion * (1.0 - proportion)          # densities in s, as in Code Cell 2

    def to_s_density(field):
        return field.numpy() / ds_dzeta

    all_region_start = float(logistic(torch.tensor(strong_network.theta_L)))

    # All three figures use a LOGARITHMIC vertical axis. At this Lambda every entry holds,
    # so the settled densities pile against the ends of the scale and span several orders
    # of magnitude between panels; on a linear axis most panels would be a flat line under
    # one spike. The comparison to read is the full network against the literal listener
    # WITHIN each panel. The upper limit is set from the curves themselves.
    def draw(axis, prior, row, title):
        axis.plot(proportion, to_s_density(prior), color="0.6", linewidth=1.0,
                  label="base world prior")
        axis.plot(proportion, to_s_density(row["baseline_q"]), linestyle="--",
                  label="literal listener $q_{\\mathrm{lit}}$")
        axis.plot(proportion, to_s_density(row["full_q"]), label="full network")
        axis.axvspan(all_region_start, 1.0, alpha=0.12, color="tab:red")
        axis.set_yscale("log")
        axis.set_title(title, fontsize=9)
        axis.set_xlabel("proportion $s$")

    def ceiling(curves):
        return 3.0 * max(float(to_s_density(curve).max()) for curve in curves)

    # first figure: the three utterances under the default Gaussian prior
    gaussian = strong_rows["gaussian"]
    gaussian_prior = torch.exp(gaussian["network"].base_log_prior)
    figure, axes = plt.subplots(1, 3, figsize=(13, 3.6), sharey=True)
    for axis, utterance in zip(axes, UTTERANCES):
        row = gaussian["utterances"][utterance]
        draw(axis, gaussian_prior, row, f'"{utterance}"  (shift {row["shift"]:+.4f})')
    top = ceiling([gaussian_prior] + [gaussian["utterances"][y][key] for y in UTTERANCES
                                      for key in ("baseline_q", "full_q")])
    for axis in axes:
        axis.set_ylim(1e-4, top)
    axes[0].set_ylabel("read-out density $q(s)$, log scale")
    axes[0].legend(fontsize=8, loc="upper center")
    figure.suptitle(
        "Settled belief against the literal listener under the Gaussian prior at "
        "$\\Lambda=%g$, $\\theta_u^\\ast=%.2f$ (shaded: the region where \"all\" is true)"
        % (STRONG_LAMBDA, gaussian["theta_u"]), fontsize=10)
    figure.tight_layout()
    plt.show()

    # second figure: "some" under all five priors, which at this Lambda share their panels
    prior_figure, prior_axes = plt.subplots(
        1, len(strong_rows), figsize=(3.4 * len(strong_rows), 3.4), sharey=True
    )
    curves = []
    for axis, (name, entry) in zip(prior_axes, strong_rows.items()):
        row = entry["utterances"]["some"]
        prior = torch.exp(entry["network"].base_log_prior)
        draw(axis, prior, row, f"{name}\n(shift {row['shift']:+.4f})")
        curves += [prior, row["baseline_q"], row["full_q"]]
    top = ceiling(curves)
    for axis in prior_axes:
        axis.set_ylim(1e-4, top)
    prior_axes[0].set_ylabel("read-out density $q(s)$, log scale")
    prior_axes[0].legend(fontsize=8, loc="upper left")
    prior_figure.suptitle(
        '"some" under the five base world priors at $\\Lambda=%g$, each at its own learned '
        "$\\theta_u^\\ast$" % STRONG_LAMBDA, fontsize=10)
    prior_figure.tight_layout()
    plt.show()

    # third figure: the three utterances under the delta-like prior, the sharp prior the
    # criterion is under most pressure from, and the case Code Cell 4 is built around
    delta_entry = strong_rows["delta (all)"]
    delta_prior = torch.exp(delta_entry["network"].base_log_prior)
    delta_peak = max(
        float(to_s_density(curve).max())
        for y in UTTERANCES
        for curve in (delta_entry["utterances"][y]["baseline_q"],
                      delta_entry["utterances"][y]["full_q"], delta_prior)
    )
    delta_figure, delta_axes = plt.subplots(1, 3, figsize=(13, 3.6), sharey=True)
    for axis, utterance in zip(delta_axes, UTTERANCES):
        row = delta_entry["utterances"][utterance]
        draw(axis, delta_prior, row, f'"{utterance}"  (shift {row["shift"]:+.4f})')
        axis.set_ylim(1e-4, 3.0 * delta_peak)
    delta_axes[0].set_ylabel("read-out density $q(s)$, log scale")
    delta_axes[0].legend(fontsize=8, loc="upper left")
    delta_some = delta_entry["utterances"]["some"]
    delta_figure.suptitle(
        "The delta-like base world prior, $\\mathrm{Beta}(%g,1)$ at "
        "$\\Lambda=%g$ (shaded: the region where \"all\" is true).\nUnder "
        "\"some\" the literal listener holds %.1f%% of its mass inside that region "
        "and the full network %.1f%%"
        % (DELTA_ALL_ALPHA, DELTA_ALL_LAMBDA, 100 * delta_some["baseline_upper"],
           100 * delta_some["full_upper"]), fontsize=10)
    delta_figure.tight_layout()
    plt.show()

except ImportError:
    print("matplotlib unavailable; skipping the figures")


# ---- the delta read-out, after the q figures ----

delta_readout_report(strong["network"], strong["realizability"])
cell_margin_report(strong["realizability"])
