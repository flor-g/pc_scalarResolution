# Reach of "θ_u learned in every evaluation, per configuration"

All numbers below are computed on the current `main.ipynb` code: θ* is Eq. (B2)'s
closed-form maximizer for each configuration, and every fixed point is evaluated in closed
form (exact by §8.6), except Part A, which was integrated. Where a cell shows `old → new`,
*old* is the stored output at θ_u = 1, which the harness reproduces exactly.

---

## 0. Decisions the change needs

| # | Question | Why it has to be settled | Suggested option |
|---|---|---|---|
| D1 | What "learned" means in code | From the constructor's start θ_u(0) = +1, the flow of Eq. (20) reaches θ* only where θ* > 0. Where θ* < 0 (Gaussian, Beta(1,3), and plane cells (1,2), (1,4), (2,2)) the minimum sits at θ_min = −2/θ* (0.0703 Gaussian, 0.1379 Beta(1,3)), so +1 lies past it and the flow runs to +∞. The notebook avoids this today by `copysign`. Integrating the flow to θ* is also infeasible where \|θ*\| is large. | θ* := the closed-form stationary point (`theta_u_stationary_point`, moved to Code cell 1), with the premise "θ_u(0) on θ*'s side of θ_min" stated in Appendix B. θ* beats the asymptote in every configuration tested (margin > 0 in all 5 priors and all 121 cells), so it is the global maximum, not only a local one. |
| D2 | Scope of "each configuration" | `respawn` re-learns for every override: prior, and also Λ, μ_u, K, the smooth mask, θ_L and m. | Re-learn for every override. |
| D3 | Code Cell 3 Part B (μ_u probes) | That section's result *is* a fixed-θ_u decomposition. Re-learning per μ_u destroys the invariance the section is about (contrast deviation 3.6e-15 → 3.2e-2). | Hold θ_u at the learned default θ* = −28.4375 for the decomposition, and report the re-learned values beside it as the model's prediction. |
| D4 | Dynamics at large θ* | The φ_u rate is 1 + θ*²: 810 (Gaussian), 211 (Beta(1,3)), 3.0e3 (Beta(3,1)), 2.0e6 (delta), 3.5e7 (flat); on the plane \|θ*\| reaches 1.2e4. Integration takes ~37k steps at the Gaussian θ* (1.7 s) and ~140k at Beta(3,1); flat and delta need 1e8–1e9 steps and are infeasible. | Closed form everywhere (already exact by §8.6); verify against `infer` only in configurations where it is feasible. |
| D5 | §8.2 F-monotonicity fails at θ* (see §1) | This is physical, not an Euler artefact. | Either (a) a new timescale commitment τ_ε ≪ τ_φ/(1+θ_u²), paralleling Appendix E's relay, or (b) restate §8.2 for the separated flow and test convergence only (Bogacz notes oscillation in the joint network, his Exercise 3). |

---

## 1. Code

### Code cell 1 (architecture), mirrored in Code Cell E1
- `theta_u=1.0` constructor default → learned (closed form). This single change propagates through `respawn` to every configuration.
- Move `theta_u_stationary_point` (or the Eq. B2 quadratic) here from Code Cell 2; Code Cells 3 and 4 and Appendix E already call it.
- `infer`: callers pass `dt=0.02`, which the stability guard **rejects** at θ* (bound 0.0025 Gaussian). Make dt automatic. `max_steps=20000` is too small (~37k needed at the Gaussian θ*).
- `learn_theta_u` / docstrings: the start value becomes an explicit argument (D1).

### Code Cell 2 (evaluation), mirrored in Code Cell E2
- **Every `dt=0.02` call** (check_specification, demonstrate, lexical_strength_sweep, scalar_implicature_probe, base_prior_sweep) raises at θ*.
- `check_specification`, measured at θ* with automatic dt: **12/13**.
  - **FAIL: Sec. 8.2 F non-decreasing**, min step −18.3. Physical: at dt/4 it is −4.6, over 1,605 decreasing steps instead of 400. It vanishes at τ_ε = 1e-4 < τ_φ/(1+θ*²) = 1.2e-3. At θ_u = 1 there are 0 decreasing steps.
  - **Vacuous: "Eq. (20) ascends toward it"**, which now starts at copysign(θ*) = θ* and passes with \|grad\| 9e-14 → 9e-14. It needs an explicit start (D1).
  - Before max_steps was raised, `learn_theta_u` threw "fast subsystem did not equilibrate".
  - Runtime goes from a few seconds to 158 s.
  - Contraction per step is 0.99930 (was ~0.978), still equal across utterances, so the §8.1(iii) check passes.
- `theta_u_learning_probe`: starts at θ* unless given a start.
- `theta_u_dependence`: the "reported (1)" column and the prints "the rest of this cell reports θ_u = 1" / "worst case for this" need relabelling.
- `base_prior_sweep`: the column `max |phi_S - phi_S*|` cannot be computed by integration for flat or delta. The printed delta-row narrative "sheds a third" becomes "more than half" (0.9568 → 0.4351).
- Figures: all three redraw. The comment "peaking at 6.1e3 under all against 2.4e1 under some" is a θ_u = 1 number.
- *Pre-existing, not caused by the change:* the second figure's suptitle says the shift is taken "against the θ_u control" (it is against q_lit). The third figure's suptitle and comment say "the control peaks inside that region", but the panels draw q_lit.

### Code Cell 3 (probes)
- Part A (basis parity): untouched.
- `mu_u_probe`, `mu_u_scale_probe` and `mu_u_sign_probe` take `theta_u=1.0` explicitly (D3). The `mu_u_plane_probe` invariance block also hard-codes `theta_u=1.0`.
- Its θ* table is already per-μ_u and stays.

### Code Cell 4 (Λ×α sweep)
- The plane is automatic via `respawn` and is closed form.
- The verification re-runs 6 random cells through `infer`. Those cells' θ* reach 1.2e4, so the sample must be restricted to feasible cells.
- `override_threshold`: the columns pass θ explicitly. It needs a learned column, re-learning θ* at each Λ probed.
- The comment "3.50–3.55 α at θ_u = 1" needs updating.

### appendix_E.ipynb
- E1/E2 mirror the changes above. E3's diff will report every moved line and must be re-baselined.
- E2 "a lagged relay settles where the instant one does" uses τ_relay = 0.01. That is unstable once \|θ_u\| > ~10 (τ_crit ≈ θ⁻²), so it fails at every learned θ* except near Beta(1,3)'s.

---

## 2. Results (old at θ_u = 1 → new at each configuration's own θ*)

**Gaussian, Λ = 8 (θ* = −28.4375)**

| quantity | no | some | all |
|---|---|---|---|
| E[s] | 0.2683 → 0.2715 | 0.5448 → 0.5684 | 0.7597 → 0.7262 |
| leak | 0.530 → 0.622 | 0.000 → 0.000 | 0.485 → **0.626** |
| shift vs q_lit | +0.0041 → +0.0003 | +0.0098 → +0.0008 | −0.3144 → −0.4557 |
| φ_u | [−2.373, −3.611] → [+0.322, +0.453] | [+3.706, −7.456] → [−0.317, +0.857] | [+3.706, −3.611] → [−0.317, +0.453] |

The verdict for *some* is unchanged (not met). Leak for *all* crosses 1/2.

**Λ sweep**: each Λ has its own θ*: −18.73, −19.19, −20.90, −28.44, −76.64, +1535.4, +342.3 for Λ = 1…64. Leak at Λ = 8 goes 0.530 → 0.626; still monotone.

**Part D (Δ_some ; q_H(all | some))**

| prior | own θ* | θ_u = 1 | learned | conditions |
|---|---|---|---|---|
| Gaussian | −28.44 | +0.0098 ; 0.0114 | +0.0008 ; 0.0025 | 2nd → 2nd |
| flat | +5950.6 | +0.0880 ; 0.1384 | +0.0295 ; 0.0799 | 2nd → 2nd |
| Beta(1,3) | −14.51 | +0.0032 ; 0.0033 | +0.0004 ; 0.0005 | 2nd → 2nd |
| Beta(3,1) | +55.01 | +0.1130 ; 0.2498 | +0.0421 ; 0.1788 | 2nd → 2nd |
| delta | +1407.8 | −0.3488 ; 0.6080 | −0.5217 ; 0.4351 | 1st → **both** |

- Utility level's own part (q_H − control): −0.0077, +0.0027, −0.0033, +0.0142, −0.2902 → **−0.0167, −0.0559, −0.0061, −0.0568, −0.4631**, negative under all five. The tempering parts (+0.0175, +0.0854, +0.0065, +0.0988, −0.0586) are θ-independent.
- Beta(1,3): **E[s | all] 0.334 < E[s | some] 0.361** (was 0.407 > 0.353); leak(all) 0.803 → 0.910.
- Beta(3,1): leak(no) 0.845 → 0.908.
- The φ_S contrasts across priors at a common Λ are no longer ℓ₀-invariant: max deviation 2.5e-14 → 0.026.
- Spike paragraph, full network under *some*: flat mode s = 0.62 → 0.67, density 0.2119 → 0.2767, top node 0.0126 → 0.0013. Beta(3,1): s = 0.83 → 0.84, 0.2493 → 0.3285, top node 0.0211 → 0.0023. The q_lit values are unchanged.
- Gaussian at Λ = 512 (Part C's control): +0.0373 → +0.0071 (θ* = 1580.8). The argument survives: +0.0071 is still further from the criterion than +0.0008.

**Text cell 6 plane (121 cells)**

| statistic | θ_u = 1 | learned |
|---|---|---|
| differential < 0 / < −1e-3 / < −1e-2 | 95 / 65 / 50 | 97 / 72 / 62 |
| most negative differential | −0.8109 at (64, 2048) | −1.2470 at (64, 256) |
| max differential | +0.1279 at (1, 128) | +0.0656 at (1, 64) |
| raw Δ_some < 0 | 82 | 77 |
| min Δ_some | −0.8109 | −0.9466 |
| positive differential cells | 26, all α ≤ 8 | 18, α ≤ 4 plus one saturated cell (1024, 128) |
| Δ_some > 0 cells | 39, up to α = 32 | 37, up to α = 64 |
| \|differential\| < 1e-3 (of which Λ ≤ α) | 30 (28) | 32 (30) |
| tempering larger than utility | 74 | 59 |
| sign(Δ_some) ≠ sign(utility) | 43 | 63 |
| utility some−no difference, median / max | 0.0153 / 0.7523 | 0.0405 / 1.1884 |
| differential agrees with utility | 109 | 99 |
| max \|Δ_no\| | 0.1539 | **1.0000** |
| second condition / both | 55 / 22 | 59 / **33** |
| band | (8, 128)–(128, 2048) | (1, 512)–(128, 2048) |
| delta row at Λ = 512 / 1024 / 2048 (q_H ; shift) | 0.6080 ; −0.3488 / 0.3780 ; −0.5789 / 0.1459 ; −0.8109 | 0.4351 ; −0.5217 / 0.1352 ; −0.8217 / 0.0102 ; −0.9466 |

- First-condition floor by α (1…128): 2048, 1024, 512, 128, 64, 4, 2, 2 → 512, 256, 128, 64, 32, 32, 16, 2.
- Second-condition floor: 2, 2, 2, 2, 128, 512, 1024, 2048 → 2, 2, 2, 2, 64, 256, 512, 1024.
- **Override moves**: on the diagonal Λ = 4α at α = 32…512, the entry for *no* held at θ_u = 1 (leak 0.000) and is overridden at θ* (leak 0.835–1.000). The \|Δ_no\| = 1 cells are these. The smallest Λ holding *no* doubles for α ≥ 32, and α = 512 is no longer held anywhere.
- The α = 1024 row is saturated (\|shifts\| < 1e-4), so its floor entries are sign noise.
- Override slopes at α = 1024, learned: 1.9890, 2.9334, 4.3102 (+45.4%, +36.0%, +41.6% over the severed level). Compare 1.6122, 2.4839, 3.5480 at θ_u = 1.
- μ_u sensitivity (Text cell 6 §Quantities): at (1, 8), E[s] range 0.14 → 0.001 and Δ_some +0.0422…+0.2457 → +0.0295…+0.0305. At (16, 128), **no sign change** (−0.2003…−0.2034). At learned θ*, μ_u is nearly inert on the maps.

**Code Cell 3 / Text cell 5 Part B**
- Eq. (33): ∂φ_S*/∂μ_u = B/3 → **−0.0351 B** (10× smaller, and the sign flips because θ* < 0).
- θ held at θ* = −28.4375: the contrast invariance survives (3.6e-15). E[s] barely moves (*no* 0.2703–0.2726), and the tilt reading reverses: *no* falls along [0,1] → [1,1] → [2,1]. Δ_some is +0.0008 in every setting; Δ_all runs −0.4535…−0.4578.
- Re-learned per μ_u (θ* −23.40, +127.94, −28.44, −12.72, −35.99): contrast deviation 3.2e-2, Δ_all −0.4514…−0.4641.
- The claim that each Δ varies "by more than a fifth of its own size" fails both ways.

**Appendices**
- Appendix C §6 (m = 1 odd basis, own θ* = +26.774): Δ some/all vs q_lit +0.0300 / −0.1912 → +0.0604 / −0.0473; vs control +0.0125 / +0.1276 → +0.0429 / +0.2715. The table row *no* vs *all* moves; (C3) is untouched.
- Appendix D: ‖r_S‖ under E 23.19, 18.08, 23.10 → 22.47, 15.76, 22.47; under T 10.56, 9.43, 10.36 → 8.88, 3.18, 8.88.
- Appendix E relay bound τ_r ≲ θ*⁻² (relative to τ_ε = 0.1): Gaussian 1.2e-3 (81×), Beta(1,3) 4.8e-3 (21×), Beta(3,1) 3.3e-4 (303×), delta 5.1e-7 (**2.0e5×**), flat 2.8e-8 (**3.5e6×**).

---

## 3. Prose (line numbers from the cell sources as of 2026-09-10)

### Text cell 3
- §7 Eq. (20) ordering (line ~345) and §8.3 (lines ~404–409): τ_ε ≪ τ_φ is not sufficient at learned θ*; the operative ratio is τ_φ/(1+θ_u²) (D5).
- Otherwise untouched: the proofs hold for every θ_u.

### Text cell 4
- Part A, lines 23–31, "Everything else in this cell is reported at θ_u = 1 …": rewrite. The contrast chain 9.6995 → 10.9524 → 13.9124 stays as a θ-sweep.
- Part A list (line 7–8): it claims F-monotonicity is tested (D5).
- Part C, lines 81–92: "+0.0098 at θ_u = 1 … utility part −0.0077 … tempering +0.0175 …" → +0.0008; utility −0.0167; tempering +0.0175. **"the conjunction holds under none" → holds under the delta-like prior.**
- Part C, lines 94–96: *all* −0.3144 → −0.4557, *no* +0.0041 → +0.0003.
- Part C, lines 105–106: Λ = 512 control +0.0373 → +0.0071, against +0.0008.
- Part C, lines 126–128: "θ* delivers −0.5222" → own θ* delivers −0.5217 (= the limit). The −0.5222 was at the Gaussian θ* carried over.
- Part C, lines 153–160: "second condition not met alongside it there, q_H 0.6080 … 22 of 121 … the delta-like row is that band's neighbour … Part D's priors are simply not where it is reached" → all inverted (0.4351; 33; a member).
- Part D, lines 203 and 210–213: "leaks below 8e-71" → 1.1e-74. **"φ_S contrasts exactly ℓ₀-invariant, 2.5e-14"** holds only at a shared θ_u, so it needs the qualifier (0.026 at per-prior θ*). "max |φ_S − φ_S*| = 6.0e-11" is not computable by integration for flat or delta (D4).
- Part D, lines 215–221: θ-independent (q_lit and the control); stays.
- Part D, lines 223–234: the five Δ values; the ℓ₀-invariance argument needs "at fixed θ_u".
- Part D, lines 236–251: the table and **"The conjunction holds under none of the five"**.
- Part D, lines 253–263: **"utility level's own contribution … of either sign, −0.0077, +0.0027, −0.0033, +0.0142 … −0.2902"** → negative in all five (−0.0167, −0.0559, −0.0061, −0.0568, −0.4631).
- Part D, lines 265–279: spike modes and densities (flat and Beta(3,1)); the q_H masses 0.1384 / 0.2498 → 0.0799 / 0.1788.
- Integration cost, lines 342–379: now load-bearing. Add the per-prior θ* stiffness (up to 3.5e7) and the F-monotonicity finding. "each inference costs some 405×" becomes the Gaussian's case, not the worst.

### Text cell 5
- Part B header, lines 81–83: "θ_u = 1" → D3 choice.
- Lines 102–108: Eq. (33) = B/3 → −0.0351 B.
- Lines 114–120: "Everything in this report was computed at θ_u = 1".
- Lines 126–128: the Δ ranges and "by more than a fifth".
- Lines 143–149 and 186–187: tilt/width directions (they reverse at θ* < 0 by Eq. 35).
- Lines 151–156: "θ_u μ_{u,j} b_j has norm θ_u|μ_{u,j}|" is fine, but "one unit buys 1.00 nat" is per unit θ_u.
- Lines 164–167: "At θ_u = 1 … 21× below" → effective coefficient 0.035, so about 600× below.
- Lines 179–184 and 196–219: both E[s] tables.
- Line 231, §4 premise 1: "θ_u held at 1".
- Lines 310–316: "At fixed θ_u = 1" → the D3 value.

### Text cell 6
- Lines 8–10: "everything below holds θ_u = 1" → everything below is learned, so μ_u and ℓ₀ now do reach the maps through θ*.
- Lines 52–61: "No other quantity is varied: θ_u = 1" (θ_u now varies per cell, −557.7 to +12228). The μ_u-sensitivity paragraph inverts: μ_u is nearly inert at learned θ*.
- Lines 79–90: 74 → 59, 43 → 63; delta cell −0.3488 → −0.5217.
- Lines 105–115: 0.0153 / 0.7523 → 0.0405 / 1.1884; 109 → 99; 78 → 58; 0.1539 → 1.0000 (override cells); −0.8109 → −0.9466.
- Lines 141–150: slopes and "36–45% at θ*" → learned 1.9890 / 2.9334 / 4.3102. The μ_u-independence check at θ_u = 1 should be re-read at θ*.
- Lines 182–209: every geography count. The "26 positive cells all at α ≤ 8" bullet changes. The override bullet must add the Λ = 4α diagonal flipping. The band claim changes, and the delta row now reads −0.5217.
- Lines 216–246: 55 / 22 → 59 / 33, both floors, the band, **"Part D's rows sit outside that band" → the delta row is inside it**, the Λ-raising sequence, and the verification cell (64, 2048) (q_H 0.0102; integration there is infeasible at θ* ≈ 2.7e3).

### Appendices
- Appendix B: add the initialization premise (D1). The statement "reaches it from any τ_θ started on the same side of zero" is true, but the code's start is on the wrong side for θ* < 0. Everything else is already at θ*.
- Appendix C §6, lines 136–137 and 157–158: the numbers above.
- Appendix D, lines 40–41: the ‖r_S‖ numbers.
- Appendix E, E.1 lines 85–87: "eighty times faster" → prior-relative, up to 3.5e6×. E.2 line 40 (ringing) is sharpened. E.3 row "θ* = −28.4375 stands" is unchanged.

### Unaffected
Text cells 1–2; Text cell 3 apart from §7/§8.3; Appendix A; Appendix B's reduced objective, exposure table and alternatives argument; Code Cell 3 Part A; the Hessian proof and check; the θ-sweep diagnostics (they sweep θ by design).
