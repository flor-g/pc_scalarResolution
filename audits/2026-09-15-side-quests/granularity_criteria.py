"""Side quest 2: do the reported criteria move with n?

Uses the notebook's own methods throughout (no custom fixed point), so every
number here is the network's. Scratch probe (C6).
"""
import math, pathlib, torch

SRC = pathlib.Path("/private/tmp/claude-501/-Users-flog-Desktop-predictive-coding/"
                   "cdd84152-de05-44ad-92e9-458bc1738ed8/scratchpad/cells/cell05_code.txt")
ns = {}
exec(compile(SRC.read_text(), "code_cell_1", "exec"), ns)
Net, beta, gauss = (ns["LexicalPredictiveCodingNetwork"], ns["beta_world_prior"],
                    ns["gaussian_world_prior"])

def row(net, y="some"):
    w, up = net.weights, (net.zeta > net.theta_L).to(net.dtype)
    lit = net.read_out(net.literal_fixed_point(y))
    full_f = net.closed_form_fixed_point(y)[0]
    temp_f = net.closed_form_fixed_point(y, theta_u=0.0)[0]
    full = net.read_out(full_f)
    P = lambda q: float((w * q * up).sum())
    return (net.theta_u, P(full) - P(lit), P(full),
            int(torch.argmax(full_f)) - int(torch.argmax(temp_f)),
            float(net.zeta[int(torch.argmax(full_f))]))

for pname, prior in (("N(0,1) in zeta (default)", None), ("Beta(3,1) in s", beta(3.0, 1.0))):
    print(f"\n== criteria for \"some\", base prior {pname} ==")
    print(f"  {'n':>4}{'theta_L':>9}{'theta_u*':>11}{'q shift':>10}{'q shift':>9}"
          f"{'P(all)':>9}{'q pos':>7}{'mode step':>11}{'mode pos':>10}")
    for n in [2, 3, 4, 5, 10, 20, 50]:
        net = Net(num_atoms=n) if prior is None else Net(num_atoms=n, base_prior=prior)
        th, sh, pos, dmode, zmode = row(net)
        print(f"  {n:>4}{net.theta_L:>9.4f}{th:>11.4f}{sh:>+10.4f}"
              f"{('met' if sh < 0 else 'no'):>9}{pos:>9.4f}"
              f"{('met' if pos < 0.5 else 'no'):>7}{dmode:>+11d}"
              f"{('met' if zmode < net.theta_L else 'no'):>10}")
    print("  q shift: P(all|some) - P(all|q_lit) < 0.  q pos: P(all|some) < 1/2.")
    print("  mode step: grid steps from the tempered control's mode to the model's.")
    print("  mode pos: the model's mode lies outside the cell of 'all'.")
