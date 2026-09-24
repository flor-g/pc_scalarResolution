"""Audit verifications V1-V4 against main.ipynb's code cell 1 (read-only)."""
import math, torch
exec(open(__import__("sys").argv[1]).read())
net = LexicalPredictiveCodingNetwork()
W = net.weights; B = net.basis; th = net.theta_u
torch.manual_seed(0)
print(f"theta_u* = {th:.4f}")

# V1: is Eq. (19)'s first line the Euclidean partial dF/dphi_S, or the quadrature-metric gradient?
y = "some"; phi_L = net.lexical_field(y)
phi_S = net.base_log_prior + 0.3 * torch.randn(net.num_nodes, dtype=DTYPE)
phi_u = net.mu_u + 0.3 * torch.randn(net.num_basis, dtype=DTYPE)
phi_S.requires_grad_(True)
F = net.free_energy(phi_S, phi_u, phi_L); F.backward()
rL, rS, ru = net.residuals(phi_S.detach(), phi_u, phi_L)
msg = -(rS + rL)                                   # Eq. (19): -eps_S - eps_L at sigma = 1
g = phi_S.grad
print("V1 max|dF/dphi_S - (-eps_S-eps_L)|      =", f"{float((g - msg).abs().max()):.3e}")
print("V1 max|dF/dphi_S - W(-eps_S-eps_L)|     =", f"{float((g - W * msg).abs().max()):.3e}")
print("V1 max|W^-1 dF/dphi_S - (-eps_S-eps_L)| =", f"{float((g / W - msg).abs().max()):.3e}")

# V2: which matrix is "H" of Sec. 8.3?  Euclidean -Hessian vs flow Jacobian (quadrature metric)
K, m = net.num_nodes, net.num_basis
def euclidean_H(theta):
    top = torch.cat([2.0 * torch.diag(W), -theta * (W[:, None] * B)], 1)
    bot = torch.cat([-theta * (W[:, None] * B).T, torch.eye(m, dtype=DTYPE) + theta**2 * B.T @ (W[:, None] * B)], 1)
    return torch.cat([top, bot], 0)
for theta in (1.0, th):
    HE = euclidean_H(theta)
    lam_E = float(torch.linalg.eigvalsh(HE).max())
    G_inv = torch.diag(torch.cat([1.0 / W, torch.ones(m, dtype=DTYPE)]))
    lam_flow = float(torch.linalg.eigvals(G_inv @ HE).real.max())
    print(f"V2 theta={theta:9.4f}: code stiffest_state_rate {net.stiffest_state_rate(theta):.4f} | "
          f"lambda_max(-grad^2 F, Euclidean) {lam_E:.4f} | lambda_max(W^-1-preconditioned) {lam_flow:.4f}")
    # the Euclidean Hessian's quadratic form equals Eq. (21)/(22)?
    v = torch.randn(K, dtype=DTYPE); t = torch.randn(m, dtype=DTYPE); z = torch.cat([v, t])
    print(f"   Eq. (22) form vs Euclidean z^T(-H)z: {float(net.hessian_quadratic_form(v, t, theta_u=theta)):+.6f} vs {float(-(z @ HE @ z)):+.6f}")

# V3: is infer() exactly Bogacz Eqs. (53)-(54) at Sigma = I in coordinates phi~ = W^1/2 phi?
theta = 1.0; tau_e = net.fast_time_constant(theta); dt = 0.5 * tau_e; steps = 400
res = net.infer(y, theta_u=theta, max_steps=steps, record_history=False, derivative_tolerance=0.0)
Wh = torch.sqrt(W); Bt = Wh[:, None] * B; l0t = Wh * net.base_log_prior; pLt = Wh * phi_L
pS = l0t.clone(); pu = net.mu_u.clone(); eL = torch.zeros(K, dtype=DTYPE); eS = torch.zeros(K, dtype=DTYPE); eu = torch.zeros(m, dtype=DTYPE)
for _ in range(steps):
    # Bogacz (54): eps_i' = phi_i - Theta_i h(phi_{i+1}) - Sigma eps_i, with Sigma = I, and the tonic inputs of his Fig. 3
    dL = ((pLt - (l0t - pS)) - eL) / tau_e
    dS = ((pS - theta * Bt @ pu) - eS) / tau_e
    du = ((pu - net.mu_u) - eu) / tau_e
    eL = eL + dt * dL; eS = eS + dt * dS; eu = eu + dt * du
    # Bogacz (53): phi_i' = -eps_i + Theta_{i-1}^T eps_{i-1}, Theta_L = -I, Theta_S = theta B~
    pS_new = pS + dt * (-eS - eL) / 1.0
    pu = pu + dt * (-eu + theta * Bt.T @ eS) / 1.0
    pS = pS_new
print(f"V3 after {res['steps']} steps: max|W^1/2 phi_S(infer) - phi~_S(Bogacz)| = {float((Wh*res['phi_S'] - pS).abs().max()):.2e}, "
      f"max|phi_u diff| = {float((res['phi_u'] - pu).abs().max()):.2e}")

# V4: the gradient of F~ at theta_u = 0
total = sum(net.project(net.base_log_prior - net.lexical_field(u)) for u in UTTERANCES)
inner = float(net.dot(net.mu_u, total)); S_ = net.sigma_lexical + net.sigma_state; n = len(UTTERANCES)
grads = []
for u in UTTERANCES:
    pS0, pu0 = net.closed_form_fixed_point(u, theta_u=0.0)
    _, rS0, _ = net.residuals(pS0, pu0, net.lexical_field(u), theta_u=0.0)
    grads.append(float(net.dot(pu0, net.project(rS0 / net.sigma_state))))
print(f"V4 <mu,sum c> = {inner:.4f}; mean_y dF/dtheta at 0 = {sum(grads)/n:.4f}; "
      f"<mu,sum c>/|Y| = {inner/n:.4f}; <mu,sum c>/S = {inner/S_:.4f}; <mu,sum c>/(S|Y|) = {inner/(S_*n):.4f}")
# and at sigma_L != sigma_S with S = 2 is impossible under the floor; check S dependence at sigma_S = 3
net3 = net.respawn(sigma_state=3.0, theta_u=0.0)
g3 = []
for u in UTTERANCES:
    pS0, pu0 = net3.closed_form_fixed_point(u, theta_u=0.0)
    _, rS0, _ = net3.residuals(pS0, pu0, net3.lexical_field(u), theta_u=0.0)
    g3.append(float(net3.dot(pu0, net3.project(rS0 / net3.sigma_state))))
tot3 = sum(net3.project(net3.base_log_prior - net3.lexical_field(u)) for u in UTTERANCES)
print(f"V4 sigma_S=3 (S=4): mean grad {sum(g3)/n:.4f}; <mu,sum c>/(S|Y|) = {float(net3.dot(net3.mu_u, tot3))/(4*n):.4f}; /(2|Y|) = {float(net3.dot(net3.mu_u, tot3))/(2*n):.4f}")
