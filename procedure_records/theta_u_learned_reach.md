# Reach of "θ_u learned in every evaluation"

> **Status 2026-09-13: code and prose both done.** T0–T11 are closed. main.ipynb executes clean
> (0 errors, 6 figures, 223 s, 14/14 checks) and appendix_E.ipynb likewise (0 errors, 3 figures,
> 562 s, E2 18/18, E3 PASS). T11 moved `infer`'s stopping tolerance from 1e-10 to 1e-9, off the
> roundoff floor F34 identified: step counts are now reproducible, an inference costs about 9% fewer
> steps, and the settled state is accurate to about 1e-9. The markdown cells of both notebooks have been rewritten against the
> executed outputs. What is deliberately left open is listed in §4 as F27's residue (Appendix C and D
> numbers come from §7.1's recorded script, by the T5.1 decision) and A11's outline pointer, which
> stays bare until the background outline is finalized.

Status: **code complete, 2026-09-11.** Every task in §3 (T0–T7) is closed. main.ipynb and appendix_E.ipynb
have been changed and re-executed: main 14/14 checks, 0 errors, 245 s; appendix E 18/18, E3 PASS, 604 s.
The originals are in `backups/2026-09-11/`. §4 logs findings F1–F27. §5 is the final prose list,
written against the executed outputs. **No prose cell has been changed.** OPEN-1 was resolved three
times the same day, finally as θ_u(0) = 0 (§2). §6 is kept as the audit's targets; F24 supersedes its
plane sign counts and F26 its Appendix E relay values.

---

## 0. Working instructions (the user's, verbatim)

> Backup before you start the change. First work through codes procedurally and record everything
> done as closed task on the reach.md. Record any unexpected findings/issues as well. After you are
> finished with the codes, list/update in reach.md everything in need of change in the prose.

What that means in this file:

1. §3 **T0** (backup) comes first.
2. The code tasks in §3 are worked **in order**. Each one is ticked `[x]` when done, with a one-line
   record of what was changed and the acceptance result.
3. Anything unexpected goes into §4 at once, before moving on.
4. Only after every code task in §3 is closed is §5 (prose) rewritten against the new outputs.
   Until then §5 is **preliminary**, drawn from the audit.

---

## 1. Settled decisions (user, 2026-09-11)

- **D1. θ\* is closed form, and the starting value is 1.** θ\* is the maximizer of F̃ given by
  Eq. (B2). It is defined as **specific to every set of inputs and hyperparameters the model
  receives**: base prior ℓ₀, Λ, μ_u, θ_L (n), K and grid half-width, the lexical mask sharpness, B
  (m), every σ, and the exposure ensemble (currently the three utterances at uniform p(y), which
  Appendix B already names as a prior over utterances). The flow of Eq. (20) starts from
  **θ_u(0) = 0** in every configuration (OPEN-1, resolved as reading (c); this supersedes
  readings (a) and (b)). The network at that start is the **tempered** control
  (θ_u = 0 at finite σ_S), not the literal listener q_lit (θ_u = 0 **and** σ_S → ∞); see §2.
- **D2. Re-learn on every override.** A variational θ_u is a commitment of the model, so every
  configuration carries its own θ\*. An evaluation may still hold θ_u fixed **as a control** when that
  serves its purpose. Wherever it does, the prose must state the justification explicitly. The
  controls are listed in §5.C.
- **D3. Text cell 5 Part B keeps its fixed-θ_u = 1 table as it is now, and gains a second table at
  learned θ\***.
- **D4. Add the new timescale commitment.** The error units must be fast relative to the stiffest
  state mode, not only relative to τ_φ. Written with Eq. (28):

      τ_ε ≪ τ_φ / (1/σ_u + θ_u² λ_max(BᵀWB)/σ_S)     (= τ_φ/(1+θ_u²) at the present settings)

  This joins the ordering τ_ε ≪ τ_φ ≪ τ_θ and, in Appendix E, τ_r ≪ τ_ε.
  **Sharpened during T1.3 (F14):** the exact form is τ_ε ≤ τ_φ/(4 λ_max(H)), critical damping of the
  stiffest mode, and it is what the code implements. **Revised during T6.4 (F26):** in Appendix E the
  relay needs only τ_r ≤ τ_ε, for monotone F; the spectrum no longer binds.
- **D5. Closed form wherever integration is infeasible.** This was not separately confirmed; it is
  adopted of necessity. Fixed points come from Eqs. (15)–(16), which §8.6 makes exact. The dynamics
  are verified only in configurations where integration is feasible, and the output says which those
  are. (The φ_u rate reaches 3.5e7 under the flat prior and \|θ\*\| reaches 1.2e4 on the plane.)

## 2. OPEN-1: RESOLVED 2026-09-11, reading (c), θ_u(0) = 0

**History.** OPEN-1 was resolved three times on 2026-09-11, each superseding the last.
- **(a) θ_u(0) = +1 literally.** Withdrawn: it misses θ\* in 21 of 145 configurations, the default
  among them (F12).
- **(b) |θ_u(0)| = 1, on θ\*'s side of zero.** Withdrawn: the start differs between configurations,
  which the user judged conceptually poor practice, and it needs a sign rule.
- **(c) θ_u(0) = 0. Adopted.** It is one start shared by every configuration, and it reaches θ\*
  in all of them.

**The user's correction on what the start is, recorded verbatim in substance.** The control q_lit has
θ_u = 0 **and σ_S → ∞**. The control must not be equated with the model's start. Nevertheless, the
prose must state that the model starts at the **tempered version of the control**.

Checked (`qlit_check.py`). At θ_u = 0 the fixed point is φ_S = σ_S/(σ_L+σ_S)·(ℓ₀−φ_L), which is
½(ℓ₀−φ_L) at the present σ's, to 0.0 exactly. It tends to the q_lit field ℓ₀−φ_L only as σ_S → ∞
(max error 2.7e-2 at σ_S = 1e3, 2.7e-5 at 1e6). So the three objects are:

| object | θ_u | σ_S | field | role |
|---|---|---|---|---|
| q_lit, the literal listener | 0 | → ∞ | ℓ₀−φ_L | baseline of the shift Δ_y (Eq. 37), Part C's literal listener |
| tempered control | 0 | model value | ½(ℓ₀−φ_L) | the θ_u = 0 control of Parts C/D and Eq. (37)'s decomposition; **the model's start** |
| the model | θ\* | model value | Eq. (15) | every evaluation |

Wording rule for code comments and prose: the start is "the tempered control" or "θ_u = 0 at the
model's σ's". It is never "the control" unqualified and never "q_lit". The label "severed" (used in
`override_threshold`) refers to the tempered control, and must not be read as q_lit either.

**What this commits the implementation to:**

- **T1.2:** `theta_u_initial = 0.0`.
- **T1.4:** `learn_theta_u` starts at θ_u = 0. No sign rule is needed. The only precondition is
  Appendix B's non-degeneracy ⟨μ_u, Σ_y c_y⟩ ≠ 0, which T1.1 already raises on. At θ_u = 0 the update
  is ⟨μ_u, Σ_y c_y⟩-driven and nonzero, so θ_u leaves zero at the first step, toward θ\*. D4's τ_ε
  and dt are recomputed as θ_u grows, since the stiff rate goes as 1 + θ_u².
- **T2.3c:** the Sec. 8.5 learning check starts from 0, not from θ\* where it passes vacuously
  today. It asserts approach to θ\* and monotone F̃. The `copysign` start in `check_specification`
  (Code Cell 2, line ~283) is removed.
- **T2.5:** `theta_u_learning_probe` drops its sign rule (`ascent_at_zero`, `copysign`, Code Cell 2
  lines ~485–494) and starts at 0. It reports the endpoint next to the closed-form θ\*, and prints the
  first-step gradient, which is what moves θ_u off zero.
- **T6.2:** Appendix E mirrors all of this (E3.txt lines ~378 and ~589).
- **Prose:** its own task in 5.A ("Start value").

**Verification (2026-09-11, `signstart.py`).** It ran over 145 configurations: the five Part D priors,
the 121 plane cells, the Λ sweep, four μ_u settings, the K ladder and the four smooth masks.

- F̃ rises monotonically from θ_u = 0 to θ\* in **145/145**. That is Appendix B's root argument: the
  roots of Eq. (B2) multiply to −S/σ_u < 0, so θ\* and the minimum θ_min lie on opposite sides of
  zero, and 0 lies between them on θ\*'s rising side.
- sign(dF̃/dθ_u at 0) = sign(θ\*) in 145/145, the same fact read at the start.
- For the record: +1 would miss θ\* in 21/145 (F12), and ±1 on θ\*'s side would reach it in 145/145.

The analysis that motivated the question is kept below for the record.

**From θ_u(0) = 1, the flow does not reach θ\* wherever θ\* < 0.** The roots of Eq. (B2)
multiply to −S/σ_u = −2. So when θ\* < 0 the minimum sits at θ_min = −2/θ\* > 0: 0.0703 under the
Gaussian and 0.1379 under Beta(1,3). A start of +1 lies past that minimum, and ascent carries θ_u to
+∞, toward an asymptote 0.2398 below F̃(θ\*) under the Gaussian. The configurations affected are the
Gaussian default, Beta(1,3), and plane cells (α, Λ) = (1, 2), (1, 4), (2, 2). Every other configuration
has θ\* > 0 and is reached from 1. Today's code avoids the issue by starting at
`copysign(1, dF̃/dθ at 0)`. There are two readings of "starting value at 1":

- **(a) θ_u(0) = +1 literally.** *(Chosen first, then withdrawn.)* Then the Gaussian network does not learn θ\*, and the
  evaluation's θ\* is a value this network would not reach from its own start. The learning check
  must then assert approach to θ\* only where +1 lies in θ\*'s basin, and report "runs to the
  asymptote" elsewhere. The prose must say so.
- **(b) |θ_u(0)| = 1, with the sign on θ\*'s side of zero**, as the code does now. *(Chosen second, then withdrawn in favour of θ_u(0) = 0.)* The flow then
  reaches θ\* in every configuration. Appendix B states the start premise.

The list of affected configurations above was incomplete; see F12.

---

## 3. Code tasks, in order

Record format when closing a task: `[x] Tn.m (date): what changed; acceptance result.`

### T0. Backup
- [x] T0.1 Copy `main.ipynb` and `appendix_E.ipynb` to `backups/2026-09-11/` in the project folder.
  Record byte sizes and sha256 of the originals and the copies. Acceptance: hashes equal.
  **Closed 2026-09-11:** backups/2026-09-11/ holds main.ipynb (755341 B, sha256 126995e8…ace0b) and appendix_E.ipynb (370242 B, sha256 7e0252af…25e0b1); copies hash-equal to originals. The project folder's older reach.md draft (16644 B, 09:15) was kept there as theta_u_learned_reach.earlier_draft.md and replaced by this finalized file, which is the working record from here on.

### T1. Code cell 1 (architecture), mirrored into Code Cell E1 at T6.1
- [x] T1.1 **θ\* in the class.** Add a method returning the closed-form θ\* from Eq. (B2), in its
  general-σ form over the exposure ensemble. Raise on the degenerate case ⟨μ_u, Σ_y c_y⟩ = 0.
  Acceptance: it agrees with the bisection `theta_u_stationary_point` to ≤1e-8 relative for all
  five Part D priors and all 121 plane cells, and reproduces −28.4375 for the default.
  **Closed 2026-09-11:** Added `theta_u_stationary_points(utterances=None)` (both roots of Eq. B2, numerically stable form, general σ, exposure ensemble = the utterance list at uniform weight; raises ValueError on ⟨μ_u, Σc⟩ = 0 and NotImplementedError if BᵀWB ≠ I) and `learned_theta_u()`. Acceptance: Gaussian −28.4374874017 (bisection agrees to 4.1e-14); Beta(1,3) 1.2e-14, Beta(3,1) 1.9e-13, delta 8.0e-11, flat 6.9e-9; plane max 3.9e-8 (t11.py). The four plane cells above 1e-8 all have |θ*| > 6000, and there the closed form equals a 50-digit root of the same coefficients exactly, while the bisection is off by 1.1e-8 to 3.9e-8 (t11b.py): the gap is the bisection's error, since its gradient flattens at large θ. Target met in substance; see F17.
- [x] T1.2 **Constructor.** Default `theta_u="learned"`, which sets `self.theta_u = θ*`. Store the
  flow's start separately as `theta_u_initial=0.0` (OPEN-1 (c)). `_configuration` must carry
  `"learned"` so that `respawn` re-learns on every override. A numeric `theta_u` stays available for
  controls. Acceptance: `respawn(base_prior=…)`, `respawn(lexical_strength=…)` and `respawn(mu_u=…)`
  each return their own θ\*, matching the audit values in §6.
  **Closed 2026-09-11:** Constructor takes `theta_u="learned"` (default) or a number (a fixed control), and `theta_u_initial=0.0`; both are carried in `_configuration`, so `respawn` re-learns unless θ_u was fixed. θ_u is resolved last in `__init__`. `self.theta_u_learned` records which. Acceptance (t11.py, t13.py): respawn(base_prior=flat) +5950.6256, Λ=32 +1535.417, Λ=64 +342.254, μ_u=[1,0] +127.940, [1,2] −12.721, K=51 −28.2355, mask 0.1 −28.385, all matching §6; respawn(theta_u=1.0) stays at 1 through further respawns; μ_u = 0 under learning raises Appendix B's ValueError.
- [x] T1.3 **Timescale commitment (D4) in `infer`.** Derive the default `tau_error` from the φ_u
  rate of Eq. (28) with a fixed ratio. Set the ratio empirically: the smallest factor that makes F
  monotone at the Gaussian θ\* (τ_ε = 1e-4 against τ_φ/(1+θ\*²) = 1.23e-3 was monotone; record the
  ratio chosen). Make `dt` automatic, satisfying both dt ≤ τ_ε and the Euler bound, and scale
  `max_steps` accordingly. Keep a guard that refuses a τ_ε violating the commitment. Acceptance: at
  the Gaussian θ\*, zero decreasing F steps and the fixed point within 1e-8 of closed form. Record the
  runtime per inference.
  **Closed 2026-09-11:** Added `stiffest_state_rate(theta_u)` = λ_max(H) (exact, symmetrized Hessian) and `fast_time_constant(theta_u, tau_state)` = τ_φ/(4 λ_max(H)), the critical-damping bound of F14. `infer` defaults: tau_error = that bound, dt = tau_error/2, max_steps = ceil(max_time/dt) with max_time = 1000 (the old horizon, 20000 × 0.05). Guards: dt ≤ tau_error, tau_error < tau_state, and tau_error ≤ bound (refuses a violating τ_ε; the old dt stability check is implied and replaced by a comment). **Ratio chosen: 4, derived (F14), not fitted.** Acceptance at the Gaussian θ* (t13.py): 3/3 converged, 0 decreasing F steps (min step −1.7e-13, roundoff), fixed point within 1.0e-10 (φ_S) and 3.9e-12 (φ_u); 163,037–163,138 steps; **runtime 7.7 s per inference without history, 11.5 s with**. The guard rejects τ_ε = 0.1 at θ* and at θ_u = 1 (bound 0.0833 there). Also fixed `steps` to count steps taken rather than len(history), which read 0 whenever history was off (F16).
- [x] T1.4 **`learn_theta_u`.** Start at `theta_u_initial = 0.0` and use the D4 time constants,
  recomputed as θ_u grows. No sign rule. Comment the start as "the tempered control", never as q_lit.
  See §2.
  **Closed 2026-09-11:** `learn_theta_u` now starts at `theta_u_initial` (default the network's, 0.0; overridable per call), re-derives τ_ε and dt at every update through `infer`'s defaults, refuses a fixed dt or tau_error, and clears `theta_u_learned` because θ_u then follows the flow. The per-update automatic-dt block is removed (superseded by T1.3). Acceptance (t14.py): Gaussian 0 → −6.0602 in 25 updates at τ_θ = 20 (15.6 s), first gradient −6.8187, |grad| 6.82 → 1.29, F̃ monotone (min step +8.8e-2); Beta(3,1) 0 → +6.2211. Path matches the closed-form map of thmap.py (−5.996 at update 24).
- [x] T1.5 Docstrings and comments: class header, the `theta_u` default, `predict_state`,
  `learn_theta_u`, and `infer`'s time-constant notes, all pointing to the D4 commitment.
  **Closed 2026-09-11:** Docstrings updated: class header (θ_u learned; start 0 = the tempered control, not q_lit), constructor comments, `respawn`, `predict_state`, `literal_fixed_point` (the tempered control is the flow's start), `theta_u_stationary_points`, `stiffest_state_rate`, `fast_time_constant` (the D4 derivation), `infer`, `learn_theta_u`. Cell 1 written into main.ipynb (cell index 5; nbformat round-trip is byte-identical, so only that cell changed).

### T2. Code Cell 2 (evaluation), mirrored into Code Cell E2 at T6.2
- [x] T2.1 Make `theta_u_stationary_point` call the T1.1 method. Keep a bisection as the
  **independent cross-check** inside the Sec. 8.5 check.
  **Closed 2026-09-11:** `theta_u_stationary_point(net)` now returns `net.learned_theta_u()` (valid for learned and control networks alike). Part A keeps its bisection as the independent cross-check, in a new check "Sec. 8.5 theta_u* of Eq. (B2) matches an independent bisection" (tolerance 1e-8 relative; it also asserts the evaluation network carries exactly that θ*): gap 4.6e-14.
- [x] T2.2 Remove every hard-coded `dt=0.02` (check_specification, demonstrate,
  lexical_strength_sweep, scalar_implicature_probe, base_prior_sweep). Today these are rejected by
  the stability guard at θ\*.
  **Closed 2026-09-11:** Removed the `dt` parameter and every `dt=0.02` from check_specification, demonstrate, lexical_strength_sweep, scalar_implicature_probe and base_prior_sweep; all integration uses `infer`'s D4 defaults. Added a helper `settle(net, y, theta_u)` that integrates where λ_max(H) ≤ FEASIBLE_STIFFNESS = 1e3 (about 8 s per inference) and reads the closed form elsewhere, returning which (D5), and `describe_theta(net)` for headers.
- [x] T2.3 `check_specification` at learned θ\*:
  - a. Run every dynamics check under D4; the F-monotone check must pass.
  - b. The Hessian over θ ∈ {−50, −1, 0, 1, 50} is a θ-sweep control; keep it (§5.C).
  - c. "Eq. (20) ascends toward it" must start from θ_u(0), not from θ\*, where it passes
    vacuously today. Start at θ_u(0) = 0 (OPEN-1 (c)); remove the `copysign` start; assert approach
    to θ\*; see §2.
  - d. Record the runtime (158 s at τ_ε = 0.1; expected longer under D4).
  **Closed 2026-09-11:** check_specification at the learned θ*: **14/14 pass** (13 before plus the new θ* cross-check). (a) Dynamics under D4: F non-decreasing, min step −1.71e-13 at τ_ε = 3.084e-4; fixed point 9.98e-11. Runs are reused across the fixed-point, relaxation and gradient checks (3 integrations, not 7). (b) Hessian θ list kept as a sweep, with the network's θ* added. (c) Learning check starts at θ_u(0) = 0 via `net.respawn()`; asserts start 0, approach, correct sign, shrinking gradient and monotone F̃: 0.000 → −6.060 (target −28.437), |grad| 6.82 → 1.29, min dF̃ step +8.7e-2. The Sec. 8.1(iii) relaxation check first FAILED (spread 4.6e-4) because its window reached the roundoff floor; re-estimated by value-selected window and least squares (F18), it passes: rates 1.000231 across utterances. Smooth masks each at their own θ*: 9.98e-11. (d) **Runtime 101–103 s** (158 s before, at τ_ε = 0.1 and θ = 1).
- [x] T2.4 `demonstrate`, `lexical_strength_sweep` and `scalar_implicature_probe` read the learned
  θ\*, closed form where integration is infeasible (D5). Λ = 32 has θ\* = 1535, so the Λ sweep must
  be closed form. Print θ\* in each header. The demonstration's `steps` column is either reported
  from a feasible integration or dropped, and the choice recorded.
  **Closed 2026-09-11:** demonstrate integrates via `settle` (the Gaussian is feasible) and prints θ* in the header; **steps column kept**, from the integration (163,037–163,138 steps at dt = 1.54e-4, stated under the table). lexical_strength_sweep reads the closed form at every Λ, each at its own θ* (new column: −18.730 … +1535.417, +342.254); leaks match §6 to six decimals, 5.03e-20 at Λ = 64, monotone. scalar_implicature_probe integrates the full network via `settle` and prints θ*. Shifts +0.0003 / +0.0008 / −0.4557 as in §6. Its verdict now tests the **conjunction** and prints both conditions (F19), and the line attributing the shift to "the utility level" is reworded (F20).
- [x] T2.5 `theta_u_learning_probe`: delete the sign rule and its comment ("Start on the half-line
  that contains the maximizer … The magnitude of the start is left as configured"), start at
  θ_u(0) = 0, and report the first-step gradient, the endpoint and θ\*. Rewrite the docstring's
  start premise.
  **Closed 2026-09-11:** theta_u_learning_probe: sign rule and copysign deleted; starts at θ_u(0) = 0 ("the tempered control"). Prints the first-step gradient (−6.8187), the endpoint (−7.567163 after 60 updates), θ* (−28.4375), monotone F̃ (True) and the final gradient (−0.627, still ascending). Its narrative is now data-driven: shift for "some" +0.0175 at the start, +0.0009 at the endpoint, +0.0008 at θ*, so ascending F̃ moves the shift down toward the first condition without reaching it. The unverified claim that the effect "is the same for either sign" is dropped in favour of a pointer to theta_u_dependence. Runtime 63 s.
- [x] T2.6 `theta_u_dependence` becomes a θ-sweep control with the columns tempered control (0,
  which is also the flow's start), +1, −1, and learned (θ\*). Label the 0 column "tempered control",
  not "control", to keep it apart from q_lit. Rewrite its docstring and prints ("the rest of this cell
  reports θ_u = 1", "worst case").
  **Closed 2026-09-11:** theta_u_dependence is now a stated control: columns "tempered (0)" (also the flow's start), "+1", "−1", "learned" (θ*); docstring and prints rewritten, no remaining "reported at θ_u = 1" or "worst case" text. The ±|θ| gap table peaks at |θ| = 1 (0.0483 / 0.0902) and falls to 0.0041 / 0.0083 at |θ*|, which the closing lines now state.
- [x] T2.7 `base_prior_sweep`:
  - Print θ\* per prior.
  - Compute the dynamics-vs-closed-form column only where feasible, and mark the other rows.
  - Replace the hard-coded "sheds a third" with the computed fraction (at θ\* it is 0.9568 → 0.4351).
  - *Proposed:* also print which rows meet the **conjunction**, since Parts C and D read it and the
    cell prints only the first-condition count.
  **Closed 2026-09-11:** base_prior_sweep: each prior at its own θ* (new column: −28.4375, +5950.6256, −14.5079, +55.0081, +1407.7691). Dynamics via `settle`: integrated for the Gaussian (1.0e-10) and Beta(1,3) (9.9e-11); flat, Beta(3,1) and delta are closed form and marked "closed form (stiff)" (λ_max(H) > 1e3). New P(all|some) column. Prints both the first-condition count (1 of 5: delta) and the **conjunction** (1: delta). "Sheds a third" replaced by the computed 54.5%, and the "all" row prints its signed change (+0e0). "The θ_u control" in the headroom text, which meant q_lit, now reads "the literal listener" (F13). Docstring: ℓ₀ moves θ*, and with it the stiffness, not the convergence results. Runtime 27 s.
- [x] T2.8 Figures: redraw all three, and update the comment on peak densities (6.1e3 / 2.4e1 are
  θ_u = 1 values). **Fix the two captions that are wrong already, independent of this change:**
  figure 2's suptitle says the shift is taken "against the θ_u control" (it is against q_lit);
  figure 3's suptitle and comment say "the control peaks inside that region" (the panels draw q_lit).
  **Closed 2026-09-11:** Figures redrawn (checked as PNGs). Fig. 2's suptitle was wrong already (said "against the θ_u control"); it now says "against the literal listener", notes each prior's own θ*, and computes whether the sign is constant: under learning all four shifts are positive, so it reads "of one sign" (under θ_u = 1 it was not). Fig. 3: the peak-density comment (6.1e3 / 2.4e1, θ_u = 1 values) is replaced by a data-set upper y-limit; the suptitle's wrong "the control peaks inside" now reports the computed masses (q_lit 95.7%, full network 43.5%), and it is split onto two lines because it was clipped. Cells 1 and 2 are written into main.ipynb. **Runtime of Code Cells 1–2 together: 238 s.**

### T3. Code Cell 3 (probes)
- [x] T3.1 Leave Part A (basis parity) untouched. Acceptance: its output is unchanged.
  **Closed 2026-09-11:** Part A untouched; its output is byte-identical to the stored output (diff of the first 45 lines empty).
- [x] T3.2 `mu_u_probe`: keep the θ_u = 1 table **as now** (D3). Add a second table at learned θ\*
  per setting, with the [0,0] row printed as "degenerate: no θ\*". Report the φ_S contrast
  deviation under learning (audit: 3.2e-2) beside the fixed-θ 3.6e-15.
  **Closed 2026-09-11:** mu_u_probe: the θ_u = 1 table is kept as it is (D3) and is byte-identical to the stored output. Its networks are now built as explicit θ-fixed controls (`respawn(..., theta_u=theta_u)`), because under the learned default μ_u = [0,0] raises Appendix B's error. Added a second table, each setting at its own θ*: [0,0] prints "degenerate: no θ* (Appendix B)"; θ* −23.402, +127.940, −28.437, −12.721, −35.993; shift some +0.0008 to +0.0009, shift all −0.4514 to −0.4641. Learned contrast deviation **3.19e-2** is printed beside the fixed-θ 3.6e-15. The docstring and cell header state that the fixed-θ table is a control and why.
- [x] T3.3 `mu_u_scale_probe`: keep it, and add the learned coefficient of Eq. (33)
  (audit: −0.0351 B against B/3).
  **Closed 2026-09-11:** The learned Eq. (33) coefficient (−0.0351 b_j at θ* against +1/3 at θ_u = 1, opposite sign) is printed in mu_u_probe, next to the sensitivity check it belongs to. mu_u_scale_probe keeps its θ_u = 1 line and adds the learned comparison: |θ*|‖μ_u‖ = 40.2167, **1.33× ‖ℓ₀‖** (against 21× below at θ_u = 1).
- [x] T3.4 `mu_u_sign_probe`: keep the θ_u = 1 sweep. *Proposed:* add learned E[s] columns. The
  midpoint identity φ(+v) + φ(−v) = 2φ(0) cannot be tested under learning, because θ\*(μ_u = 0) does
  not exist; the output says so.
  **Closed 2026-09-11:** mu_u_sign_probe keeps its θ_u = 1 sweep (byte-identical; spawns now θ-fixed, and it says it is a control). Added a learned table: θ*(±v) and E[s] at ±v per utterance. **Finding F22:** θ*(−v) = −θ*(+v) and E[s](−v) = E[s](+v), both exactly (0.0e+00), so under learning the sign of μ_u is invisible. The output says so, and that the midpoint identity cannot be posed because θ*(0) does not exist.
- [x] T3.5 `mu_u_plane_probe`: keep the invariance block at θ_u = 1 and the symmetry check at
  θ ∈ {0.7, 1, 4} as controls. The θ\* table is already learned.
  **Closed 2026-09-11:** mu_u_plane_probe: probes are built as θ-fixed controls (θ is passed explicitly throughout, and this keeps a degenerate-ray setting constructible). The symmetry check is labelled as an identity in θ at θ ∈ {0.7, 1, 4}, and the invariance block as a control that holds at any fixed θ. The θ* table is unchanged (it was already learned). Cell 3 runtime 0.1 s (all closed form). Written into main.ipynb.

### T4. Code Cell 4 (Λ×α sweep)
- [x] T4.1 `lambda_alpha_sweep` becomes learned automatically through `respawn`. Print the θ\*
  range (audit: −557.67 to 12228.42).
  **Closed 2026-09-11:** lambda_alpha_sweep is learned through `respawn` (each cell at its own θ*) and records θ*, λ_max(H) and the tempered (θ_u = 0) grid, so that the shift can be split into tempering and utility. It prints the θ* range: **−557.67 to +12228.42, negative at (1, 2), (1, 4), (2, 2)**, matching §6. `dt` parameter removed. The header comment's "3.50–3.55 α at θ_u = 1" is replaced by a pointer to `override_threshold`.
- [x] T4.2 Restrict the dynamics verification sample to cells where integration is feasible under
  D4, and state the rule in the output.
  **Closed 2026-09-11:** Verification restricted to cells with λ_max(H) ≤ FEASIBLE_STIFFNESS and the rule printed: **only 2 of 121 cells are feasible**, (1, 2) and (1, 4), both re-run (worst 9.90e-11, converged). The old sample of 6 random cells is no longer possible, since 119 cells have θ* too large (F4). The verification cell Text cell 6 quotes, (64, 2048) at θ* = 5531, is infeasible.
- [x] T4.3 `override_threshold`: add a learned column that re-learns θ\* at every Λ the bisection
  probes (audit: 1.9890, 2.9334, 4.3102). Keep θ = 0 (severed), ±1 and the magnitude sweep as
  controls. Re-read the μ_u-independence check at learned θ\* as well. Update the comment
  "3.50–3.55 α at θ_u = 1".
  **Closed 2026-09-11:** override_threshold: `critical(boundary, theta=None)` re-learns θ* at every Λ the bisection visits. **Learned slopes 1.9890 / 2.9334 / 4.3102** (+45.4 / +36.0 / +41.6% over severed), matching §6. θ* at the threshold is 13378 / 13908 / 14946. The old "theta_u*" column applied the Gaussian's θ* (−28.4375) to Beta(1024,1) (F23) and is replaced by the learned column. θ = 0, ±1 and the magnitude sweep are kept and labelled as controls; the "15–18% / 36–45%" text is now computed. The μ_u-independence check is re-read at learned θ*: **1.9890 for all five μ_u**, including both signs and a hundredfold range.
- [x] T4.4 *Proposed:* print the plane summaries Text cell 6 quotes: the differential counts,
  tempering/utility counts, both floors, the both-condition count and band, and the delta-row Λ
  sequence. **None of these is printed by any cell today** (see §4, F10).
  **Closed 2026-09-11:** New `plane_summary(grids)` prints every plane statistic Text cell 6 quotes: the differential counts and extremes, positive and flat cells, the raw-shift counts, the tempering/utility split, sign agreement, both floors, the conjunction count and band, and the delta row at Λ = 512/1024/2048. **Signs are read with a 1e-12 zero band** because the α = 1024 row is saturated and its shifts are roundoff (F24). Learned results: differential negative 94 (72 below −1e-3, 62 below −1e-2), 10 saturated, 17 positive (all at α ≤ 4); raw shift negative 74, minimum −0.9466, positive 37 up to α = 64; tempering larger in 59; opposite signs in 53; agreement 104 / 84; second condition 59, **both 33, band (1, 512)–(128, 2048)**; delta row q_H 0.4351 / 0.1352 / 0.0102 with shifts −0.5217 / −0.8217 / −0.9466. Floors, first / second: 512/2, 256/2, 128/2, 64/2, 32/64, 32/256, 16/512, 2/1024, 2/–, 2/–, 2048/–.
- [x] T4.5 Redraw the heat maps.
  **Closed 2026-09-11:** Heat maps redrawn and checked as PNGs. The third figure's suptitle was clipped at both edges (as in F21); it is now two lines and names the learned θ*. Cell 4 runtime 3.4 s. Written into main.ipynb (cell index 11).

### T5. Numbers quoted by appendices that no cell prints
- [x] T5.1 Appendix C §6 (m = 1, odd basis) and Appendix D (‖r_S‖ under E and T). Recompute at
  learned θ\*, and decide whether to add a printing cell or record the script. Values are in §6.
  **Closed 2026-09-11:** **Decision: record the script, do not add a cell to main** (a new code cell would change main's cell structure and numbering, which nobody asked for). The script is `appendix_numbers.py`; it reads Code Cell 1 from main.ipynb and is reproduced in §7 of this file. Output, learned against the θ_u = 1 control. **Appendix C §6** (m = 1, θ* = +26.7740): some vs all |dφ_u*| 0, |dφ_S*| 4.0000 (θ-independent, C3), |dE[s]| 0.2534 (0.2525); no vs all |dφ_u*| 0.68 (6.08), |dφ_S*| 8.5464 (5.5197), |dE[s]| 0.7818 (0.6018); Δ vs q_lit some +0.0604, all −0.0473 (+0.0300, −0.1912); vs the tempered control +0.0429, +0.2715 (+0.0125, +0.1276). (C3) at m = 1 holds to 8.9e-16 with θ* added to the list; the m = 2 comparison figure grows from 3.445 to 3.712 when θ* is included. **Appendix D §1** ‖r_S‖: E 22.47, 15.76, 22.47 and T 8.88, 3.18, 8.88 (23.19, 18.08, 23.10 and 10.56, 9.43, 10.36). All match §6. The θ_u = 1 control reproduces the appendices' stored numbers except the pre-existing items in F25.

### T6. appendix_E.ipynb (after main has been executed)
- [x] T6.1 Mirror T1 into Code Cell E1 (relay variant).
  **Closed 2026-09-11:** Code Cell E1 rebuilt by replaying T1 on it (`buildE1.py`): learned θ_u, `theta_u_initial`, the θ* methods, `stiffest_state_rate`, `fast_time_constant`, D4 defaults and guard, `steps`/dt/tau_error in the result, and `learn_theta_u` from 0. The relay additions are kept. The diff against main's new Code Cell 1 is exactly the relay additions. Also factored the relay-loop spectrum into a method `relay_loop_abscissa`, which the guard and E2 both call. The docstring's claim that at the learned θ_u a slow relay tips the loop into oscillation is rewritten per F26. The ordering guard's message now gives its real reason (F monotone). With a relay, default dt = min(τ_ε, τ_relay)/2.
- [x] T6.2 Mirror T2 into Code Cell E2, including the θ_u(0) = 0 start and removal of both
  `copysign` sites; see §2.
  **Closed 2026-09-11:** Code Cell E2 = main's new Code Cell 2 + E2's header + the four relay checks, inserted after the read-out check as before, plus E2's one pre-existing comment variant ("Code Cell 4 is built around"). The two relay-gradient checks reuse Part A's runs. θ_u(0) = 0 and every other T2 change come with the copy. E2 Part A: **18/18 pass** (167.7 s).
- [x] T6.3 E2's "lagged relay settles" check uses τ_relay = 0.01, which is unstable at any
  \|θ\| > ~10. Set τ_relay from the ordering τ_r ≪ τ_ε under D4.
  **Closed 2026-09-11:** The lagged-relay check now uses τ_relay = τ_ε/2 = 1.54e-4 at θ* (the ordering τ_r ≤ τ_ε under D4; dt = τ_r/2) and also asserts that F is monotone: max |instantaneous − lagged| 7.62e-12, min F step −2.3e-13. Not τ_ε/10: there roundoff in the relay derivative, amplified by 1/τ_r, keeps the 1e-10 settling test from firing although the state is at the fixed point (1.1e-10) (F26).
- [x] T6.4 `relay_boundary`: re-measure under D4's τ_ε. The E5 matrix was measured with τ_ε fixed
  at 0.1, and the boundary θ² τ_crit → 1 will move. Report the per-prior requirement.
  **Closed 2026-09-11:** Re-measured under D4 (`relayb.py`, `relayspec.py`, `relayF.py`). **The relay's speed requirement collapses into D4 (F26).** At τ_ε = τ_φ/(4λ_max(H)) the relay loop's spectrum is stable for every τ_relay tested, up to 10⁴ τ_ε, at θ = −5 … −1000. The largest stable τ_relay below τ_ε is τ_ε itself (ratio 1.0000 at every θ and every prior). The old boundary θ²τ_crit → 1 is reproduced exactly (1.0257, 1.0125, 1.0063, 1.0016) only at the τ_ε = 0.1 that D4 forbids. What a slow relay still breaks is monotone F: 0 decreasing steps at τ_r ≤ τ_ε, 6 at 2τ_ε (worst −1.57), 58 at 10τ_ε (worst −8.35). Check renamed "Sec. 7 the relay need only be faster than the error units": it asserts ratio 1 under D4 and reproduces the old boundary as a control. **Per-prior requirement τ_r < τ_ε(θ*):** Gaussian 3.08e-4, Beta(1,3) 1.18e-3, Beta(3,1) 8.26e-5, delta 1.26e-7, flat 7.06e-9. E1–E3 written into appendix_E.ipynb (cells 2–4; nbformat round-trip byte-identical).
- [x] T6.5 E3: confirm that it locates main's Code Cell 2 baseline (prefix `# === Code Cell 2`).
  Re-run and record the new diff tally; it was 139/140 identical, 1 changed (13/13 → 17/17),
  4 inserted.
  **Closed 2026-09-11:** E3 still locates main's baseline by the `# === Code Cell 2` prefix. Its expected pass count is now derived from the recorded one, n/n → (n+4)/(n+4), instead of the hard-coded 13 → 17. **Tally: 151 lines recorded, 150 identical, 0 deleted, 1 changed (14/14 → 18/18), 4 inserted (the four relay checks, all PASS); verdict PASS.** (Before: 139/140, 13/13 → 17/17.)

### T7. Execute and verify
- [x] T7.1 Execute `main.ipynb` end to end. Record: errors 0, figure count, checks passed, runtime.
  **Do not pipe the runner to `tail`; check the runner's own success line.**
  **Closed 2026-09-11:** main.ipynb executed end to end by `runnb.py` (nbclient, kernel python3, in place). Runner's own line: **RUNNER OK, error outputs 0, figures 6, runtime 245 s.** Specification checks 14/14.
- [x] T7.2 Execute `appendix_E.ipynb`. Record the same, plus E3's tally.
  **Closed 2026-09-11:** appendix_E.ipynb executed the same way: **RUNNER OK, error outputs 0, figures 3, runtime 604 s** (E3 re-runs the whole Code Cell 2 sequence). E2 18/18; E3 tally as in T6.5, PASS.
- [x] T7.3 Scan the code and outputs for surviving "θ_u = 1" strings not intended as controls.
  **Closed 2026-09-11:** Scanned main's code and outputs for θ_u = 1, dt = 0.02, τ_ε = 0.1 and copysign. Every θ_u = 1 left is a labelled control: Code Cell 3's fixed-θ tables (headers say "theta_u fixed at 1" / "a control") and Code Cell 4's override control columns and μ_u check. No dt = 0.02 or τ_ε = 0.1 remains. The one copysign is the numerically stable root formula in `theta_u_stationary_points`, not a start rule.
- [x] T7.4 Check every new printed number against §6. Any disagreement goes to §4.
  **Closed 2026-09-11:** Checked programmatically against §6 (72 target strings): all present, with F24's roundoff-robust plane counts in place of the superseded ones. Differences from §6, all explained: (i) plane sign counts per F24; (ii) Part A "contraction per step 0.99930" is now a rate per unit time, 1.000231 (F18); (iii) the gradient-check error is 9.74e-8, not 7.3e-8, because the θ* added to the Hessian sweep shifts the seeded random stream; (iv) Appendix E relay values per F26. Tempering and utility parts per prior, the spike modes and densities in Part D, and the Text cell 6 μ_u-sensitivity numbers are still printed by no cell (F27).

### T8. Code: the minimum learning the criterion needs, run (user, 2026-09-12)

User's instruction, 2026-09-12: "add such a run to the notebook just to be particular about the
minimum steps required to reach the criteria", with the qualification that a cost of seconds per
inference is in any case beyond what the process being modelled could plausibly pay; that this is
the complexity issue the outline raises about a hypothesized alternative representation level; and
that, since that level is not implemented, main.ipynb must not discuss it at length but cross-refer
to the outline instead.

- [x] T8.1 Code Cell 2: add a realizability block after Part D reporting, per prior, the threshold
  θ_u the conjunction needs (bisection on the ray 0 → θ\*), the cost there, and the number of
  Eq. (20) updates from 0 that pass it; then one both-conditions configuration run end to end with
  nothing in closed form.
  **Closed 2026-09-12.** Backup first: `backups/2026-09-12/` (main.ipynb, theta_u_learned_reach.md).
  Code Cell 2 (cell 7) gains `import time`, a `part_d_priors()` helper (Part D's default now reads
  from it, so the two blocks report the same rows and Part D's output is byte-identical), and the
  block **REALIZABILITY: HOW MUCH OF θ_u\* THE CRITERION NEEDS**, placed after Part D and called
  from RUN as `realizability = realizability_report(evaluation_network)`. Four new functions:
  `criterion_for_some` (Part C's two conditions as one record; takes an integrated belief so the
  run and the table are scored by the same code), `criterion_threshold` (bisection on the ray
  0 → θ\*, plus a 200-point check that the conjunction then holds along the whole ray; None where
  it fails at θ\*), `theta_u_gradient_at_equilibrium` (Eq. 20's gradient at the closed-form
  equilibrium, which is what makes the survey affordable), `updates_to_criterion`. The block ends
  with the end-to-end run: **1 integrated update of Eq. (20) then Eqs. (18)-(19) integrated at the
  θ_u it reaches, nothing in closed form.** Block runtime about 2 s.
  **Code Cell 4 (cell 11) too:** the sweep now records `theta_crit`, `crit_rate`, `crit_holds`,
  `crit_updates` per cell (about 3.5 s for the 121 cells) and `plane_summary` prints them under
  Part C's conjunction, so Text cell 6's claim about the 33 cells has a printed source rather than
  a recorded script (this one is not an F27 gap).
- [x] T8.2 Record the measured numbers in §4 as a finding, and reconcile them with F28 and A10(ii).
  **Closed 2026-09-12:** recorded as **F29**, which supersedes F28's pessimistic half and A10(ii)
  as written; A10(ii) and (iii) rewritten against it, A11 added.
- [x] T8.3 Re-execute main.ipynb; record errors, figures, checks, runtime.
  **Closed 2026-09-12:** `runnb.py` own line: **RUNNER OK, error outputs 0, figures 6, runtime
  250 s** (was 245 s). Specification checks **14/14**. Diff of the executed outputs against
  `backups/2026-09-12/main.ipynb`: cell 7 **+31 lines, no deletions or changes**; cell 11 **+5
  lines, no deletions or changes**; cells 5 and 9 byte-identical. So nothing already reported
  moved.

### T9. Prose: realizability (OPEN, the prose pass has not started)

The work A10 specifies, kept as a task so it is not lost inside §5. Nothing here is done.

- [x] T9.1 A10(i)–(iv) at the sites A10 lists: Text cell 3 §8.3 and §8.6; Text cell 4 *Integration
  cost and conditioning* (the main site); Text cell 4 Part D, one sentence on which rows are
  integrated; Text cell 6 *Method*; Appendix E E.2.
- [x] T9.2 A11's cost-plausibility sentence and the outline cross-reference. Two or three sentences
  in main.ipynb at most: the alternative representation level is not implemented here, so the
  discussion belongs to the outline. **The pointer stays bare**: no file name, no section numbers,
  since the outline is not finalized (user, 2026-09-12).
- [x] T9.3 State the conjunction's threshold θ_u alongside θ\* wherever Part C's verdict is given,
  so the reader is not left with θ\*'s cost as the cost of the implicature.
- [x] T9.4 Announce the two new printed blocks, which currently have no prose: Code Cell 2's
  realizability block (Text cell 4, after Part D, in *Integration cost and conditioning*) and Code
  Cell 4's conjunction-threshold lines (Text cell 6, where the 33 cells are discussed). Both print
  under headings no markdown cell mentions.
- [x] T9.5 Check whether Text cell 4's "the evaluation has four parts" needs amending. The block is
  deliberately not lettered as a Part E, so the sentence stands as written; confirm when the prose
  pass reaches it.

**T9 closed 2026-09-12, inside T10.** Every item was carried out as part of the cell-by-cell pass:
T9.1 in Text cell 3 §8.3 and §8.6, Text cell 4 *Integration cost and conditioning* and Part D, and
Text cell 6 *Method*; T9.2 in *Integration cost*, with the pointer left bare; T9.3 in Part C beside
the verdict and again in Text cell 6's conjunction section; T9.4 by announcing the realizability
block in *Integration cost* and the threshold lines in Text cell 6; T9.5 resolved as written, since
the block is deliberately not a fifth Part and "the evaluation has four parts" still holds.

### T11. The stopping tolerance, 1e-10 -> 1e-9 (user, 2026-09-13)

User's instruction after F34: "set the tolerance to 1e-9 and re-run both". The old value sat inside
the roundoff floor, so the stopping step was decided by noise (F34).

- [x] T11.1 `infer(derivative_tolerance=...)` default 1e-10 -> **1e-9** in main Code Cell 1 and in
  appendix_E Code Cell E1, each with the argument for the choice written into the docstring: the
  floor runs about 8e-11 to 1.6e-10, a tolerance inside it is crossed by roundoff, and at 1e-9 the
  test fires while the derivative is still decaying. E1's note adds why it matters there in
  particular (its gradient is ⟨ε_S, r⟩ against main's Σ_j φ_u,j⟨ε_S,b_j⟩).
- [x] T11.2 Verify reproducibility. **Step counts are now invariant** under relative perturbations of
  θ_u from 1e-16 to 1e-9 (39,035 at every one, against 42,550 / 42,629 / 42,765 / 42,544 / 42,624 /
  42,567 / 42,608 before), and main and Appendix E agree **exactly** at their own learned θ_u
  (39,035 each; the θ_u they reach still differ, now by 3e-15).
- [x] T11.3 Re-execute both. main.ipynb **RUNNER OK, 0 errors, 6 figures, 223 s** (was 254 s),
  **14/14**; appendix_E recorded in T11.5.
- [x] T11.4 Update every number the change moved, in the cells' own comments and in the prose:
  - an inference is about **180 λ_max(H)** steps, not 200; the feasibility cap is about **7 s**;
  - the demonstration is **148,081–148,104** steps, not 163,037–163,138 (**9% cheaper**);
  - the realizability run is **39,035** steps, not 42,551; the θ\* projection **4.28e8**, not 4.66e8;
  - agreement with Eqs. (15)-(16) is now **9.98e-10** (Part A), **1.0e-9 / 9.9e-10** (Part D),
    **9.95e-10** (the plane), **1e-09** (the realizability run), against ~1e-10 before;
  - Text cell 4 carries a paragraph saying where the integration is stopped and why, and that the
    first choice was wrong; Text cell 3 §8.6 and Text cell 6 *Method* quote the new figure.
- [x] T11.5 Re-execute appendix_E after the last mirror, and record the E3 tally.
  **Closed 2026-09-13:** **RUNNER OK, 0 errors, 3 figures, 562 s** (was 613 s), E2 **18/18**, E3
  **PASS**: 202 lines recorded, 201 identical, 0 deleted, 1 changed (the pass count), 4 inserted.
  E2's source differs from main's Code Cell 2 only by its header and the relay insertions.
  **Note on the `cost:` exclusion, now that step counts are reproducible:** it is still needed, but
  only for the wall clock. The step counts that function as a claim are compared untagged, in Part
  B's demonstration table (148,081 / 148,104, identical in both notebooks), so E3 would still catch a
  genuine divergence between the two implementations.

### T10. The prose pass itself (started 2026-09-12)

Worked cell by cell against §5. Every item is the §5 list; this block records only what was done and
anything §5 got wrong. Markdown only: no code cell is touched, so no re-execution is needed, but the
equation numbering (1)–(41) and the anchor ids must survive every edit.

- [x] T10.1 Text cell 3 (cell 4): A1, A2, A3, A10(iv), A11 clause, 5.B's §8.5 site.
  **Closed 2026-09-12.** Commitments **6** (θ_u learned, with the full enumeration of what θ\* depends
  on, and the θ_u(0) = 0 start) and **7** (the timescale commitment) added to the opening list. Inventory:
  θ_u row now "learned, θ_u\* of Eq. (B2), per configuration"; τ row carries the bound. Eq. (20)'s
  ordering restated in place, **no new equation number** (41 tags, all unique, 1–41 intact after the
  pass). New paragraph under Eq. (20), *Where the flow starts, and what the network is there*: the
  tempered control, explicitly not q_lit, the nonzero gradient at 0 tied to §3's μ_u ≠ 0, and the
  opposite-sign roots. **§8.3 rewritten**: the characteristic equation τ_ε τ_φ s² + τ_φ s + λ = 0, the
  bound τ_ε ≤ τ_φ/(4λ_max(H)) and dt = τ_ε/2 as unnumbered displays, the s = −1/τ_ε root, the θ_u²
  growth, Eq. (28) as H's diagonal entry (809.69 vs 810.69), then *What the commitment secures, and
  what it asserts* (A10(iv) + A11's clause: monotone F not convergence; 1e3 and 1e8 separations; the
  conditional). §8.5 gains the start-at-0 and the not-integrated-to-θ\* paragraph (A6).
- [x] T10.2 Text cell 4 (cell 6): A4, A5, A6, A10, A11, and 5.B's twenty-odd sites.
  **Closed 2026-09-12.** Part A: the three learned-parameter checks named (bisection 4.6e-14, interior
  maximum +0.2398, Eq. 20 ascending from 0), the per-unit-time relaxation rate explained (F18), tails
  1.7e-3 / 3.3e-6 / 1.1e-2. The "everything is reported at θ_u = 1" paragraph is replaced by
  "everything is reported at the learned θ_u\*", with `theta_u_dependence` labelled a control and the
  ±θ gap numbers (0.0483/0.0902 at 1, 0.0041/0.0083 at θ\*). Part B: the per-Λ θ\* series and the
  closed-form reading above Λ = 32. Part C: the control paragraph gains "and it is where learning
  starts"; the elicited-prior paragraph is rewritten to +0.0008 with the −0.0167 utility part; the
  delta-like prior now **meets both conditions** and the band is 33 cells; Eq. (24)'s check is
  −0.5217 against its own θ\* = +1407.77; the Λ = 512 Gaussian control is +0.0071 at θ\* = +1580.81.
  Part D: leak 1.1e-74, spreads 0.0057 / 0.0003, the ℓ₀-invariance restated as holding **at a shared
  θ_u** (3.6e-14) and no longer across rows (up to 0.058 at each prior's own θ\*), which rows are
  integrated, the five shifts, the table (with a θ\* column), the verdict paragraph, the
  tempering/utility split now printed, and the spike paragraph rewritten from figure 2 (the rise is
  q_lit's; the full network turns down at the edge). *Integration cost and conditioning* rewritten in
  full per A5 + A10 + A11, including the realizability block's announcement and the bare outline
  pointer.
  **Deviation from §5, recorded:** 5.B said the learned contrasts "differ by 0.026 across priors";
  measured here as **0.058** (max over the all−some and no−some contrasts, five priors at Λ = 8). The
  prose carries the measured value. See F30.
- [x] T10.3 Text cell 5 (cell 8): D3's second reading, A8, 5.C labels.
  **Closed 2026-09-12.** Part B's preamble now states that θ_u = 1 is a **control**, why holding it is
  the point (θ\* is itself a function of μ_u, so a learned table mixes the two paths), that the
  invariance holds at any fixed θ_u, and that every table is reported twice. Eq. (33) keeps its
  +1/3 B and gains the learned coefficient −0.0351 B, a tenth the size and opposite in sign. The
  qualifier paragraph now cites 3.19e-2 against 3.6e-15. §1's "what it does not settle" gains the
  learned ranges (+0.0008 to +0.0009; −0.4514 to −0.4641) and the reading that the spread collapses.
  Tilt/width gain the learned reversal and A8's invisibility of sign (relative gap 0.0). The scale
  block keeps 21× as the control's and adds the learned field norm 40.2167, 1.33×. The midpoint
  identity is labelled a control and stated as not posable under learning (no θ\* at μ_u = 0), with
  the symmetry reported instead. The six-setting table is labelled the control and followed by the
  learned reading (θ\* from −35.993 to +127.940; E[s] under *some* 0.5671 to 0.5692 against 0.5373 to
  0.5523). §4's premise 1 and §6's opening now name the control.
- [x] T10.4 Text cell 6 (cell 10): every count, floor, band and override column, plus A10's *Method*.
  **Closed 2026-09-12.** Opening: each cell carries its own θ\*, −557.67 to +12228.42, negative at
  (1,2), (1,4), (2,2). Grid caveat: 0.0057 → 0.0012 → 0.0003 and the 0.980 ceiling. The μ_u paragraph
  is **inverted** and now has a printed source (new `mu_u_sensitivity` block in Code Cell 4): at fixed
  θ_u = 1, (1,8) moves E[s] 0.5774–0.7191 and Δ_some +0.0422–+0.2457, and (16,128) crosses zero
  (−0.1473 to +0.0029); learned, the same range moves E[s] by 0.0026 and 0.0002 with Δ_some +0.0278
  to +0.0305 and −0.2033 to −0.2003, no sign change. Eq. (37)'s split 59 and 53; delta cell −0.5217.
  Differential scale: utility median 0.0405, max 1.1884; sign agreement 104/84; the Δ_no ≤ 0.1539
  claim replaced by the override diagonal, where Δ_no reaches 1.0000. Override threshold: the learned
  column 1.9890/2.9334/4.3102, +36–45%, θ\* at the threshold 13378–14946, and the μ_u check at
  learned θ\* (1.9890 for all five). *Method* rewritten per A10: 2 of 121 integrable at θ\*, both
  re-run, 9.90e-11, and the criterion's own θ_u is integrable everywhere it holds. Plane counts:
  94 negative (+10 saturated), 72, 62, −1.2470 at (64,256), +0.0656 at (1,64), raw *some* 74 and
  −0.9466; 17 positive at α ≤ 4; 37 reaching α = 64; 32 flat cells, 30 with Λ ≤ α. Conjunction:
  59 and **33**, both floors restated, band (1,512)–(128,2048), the delta-like row **inside** it,
  and the (64,2048) verification claim (not integrable, θ\* = 5531) replaced by the threshold result.
  F7's override diagonal added with measured values (+0.8348, +0.9996, +1.0000 ×3 at Λ = 4α) and the
  leak map's floors.
  **Correction to §5:** 5.B listed the override diagonal as five cells all at shift(no) = +1; measured,
  (32,128) is +0.8348 and (64,256) is +0.9996. The prose carries the measured values.
- [x] T10.5 Appendices A–D (cells 12–15): A3 in A; A1, A2, A6 in B; F25 and the learned values in C;
  the learned norms in D.
  **Closed 2026-09-12.** A: the ordering at line 67 now carries the bound. B: a new paragraph
  enumerating what θ\* is a function of (A1), and, at the old "reaches it from any τ_θ started on the
  same side of zero", three new paragraphs (A2, A6) that are now the main site: **why zero** (it lies
  between the roots, so ascent from it reaches θ\* whatever the sign, and +1 does not), the exact
  gradient there (⟨μ_u, Σc_y⟩/(2|Y|) = −40.9119/6 = −6.8187, derived rather than quoted), the
  **tempered control** and its distinctness from q_lit, and what the flow shows against what the
  closed form supplies (−7.567 after 60 updates, gradient −0.627; bisection gap 4.6e-14). C: F25
  fixed at the definition, κ_y = ΛBᵀWχ_y with the table declared **per unit Λ** and Code Cell 3's
  ±9.11909 reconciled as 8×; §6's table replaced by the learned values (0.0000/4.0000/0.2534 and
  0.6793/8.5464/0.7818 at θ\* = +26.774, positive where m = 2's is negative); (C3) now measured over
  {0,1,−1,5,θ\*}; Δ_y +0.0604/−0.0473 against q_lit and +0.0429/+0.2715 against the control. D: the
  learned norms 22.47/15.76/22.47 and 8.88/3.18/8.88, with the θ_u = 1 values kept as the control.
  **Deviation from §5, recorded as F31:** 5.B's "m = 2 comparison is 3.445, or 3.712 with θ\*" is not
  reproducible; measured, the all−some contrast's spread over {0,1,−1,5} is **3.87** in the
  quadrature norm (4.21 with θ\*) and **1.72** in max-abs (1.86 with θ\*). The prose carries 3.87 and
  4.21 and names the norm.
- [x] T10.6 Appendix E: main.ipynb has no Appendix E cell; the markdown lives in appendix_E.ipynb, so
  F26's rewrite is applied there (E.1, E.2, E.3).
  **Closed 2026-09-12.** E.1: the "τ_r ≲ θ_u⁻², eighty times faster" passage replaced by the measured
  result (stable at every τ_r tested up to 1e4 τ_ε; largest stable ratio 1.0000 at all four θ_u),
  Eq. (E6) restated as τ_r ≤ τ_ε ≤ τ_φ/(4λ_max(H)) ≪ τ_φ ≪ τ_θ, the θ⁻² scaling attributed to
  commitment 7, the per-prior bounds listed, and the old boundary kept as a **control** at τ_ε = 0.1
  (1.0257, 1.0125, 1.0063, 1.0016) with the monotonicity cost (0 / 6 / 58 decreasing steps).
  E.2: the empirical prediction restated as a non-monotone transient rather than ringing. E.3: the
  ordering row rewritten; 17/17 → 18/18.
  **Unplanned code work this forced (§5 did not anticipate it):** E3 compares appendix E's Code Cell
  E2 output against main's Code Cell 2 line by line, so main's new blocks made it **FAIL** (150
  identical, 43 deleted). Code Cell E2 has been re-mirrored from main's cell verbatim (`mirrorE2.py`
  lifts the realizability block, `part_d_priors`, the tempering/utility split and the spike block out
  of main's source rather than retyping them), leaving E2 different from main's cell only by its
  header and the relay insertions. Re-executed; tally recorded in T10.7.
- [x] T10.7 Final sweep: equation numbers unchanged, anchors intact, no "θ_u = 1" left unlabelled,
  every number in the prose matched against the executed outputs.
  **Closed 2026-09-12.**
  - **Equation numbers:** 41 numbered tags, each exactly once, 1–41 complete; lettered tags A1–A6,
    B1–B4, C1–C3, D1–D4 unchanged. D4's bound and §8.3's characteristic equation are **unnumbered
    displays**, as A3 required. No anchor id was touched.
  - **θ_u = 1:** every surviving mention is inside a labelled control (Text cell 5 Part B's preamble
    and its tables, Text cell 6's override columns, Appendix C §6 and D §1 comparisons).
  - **Numbers:** 149 quoted values checked programmatically against the executed outputs
    (`verify.py`). All are printed, except: q_lit = 0.0504 under the flat prior (arithmetic from two
    printed values, 0.0799 − 0.0295); Appendix C §6's and Appendix D §1's values and Appendix B's
    −40.9119, which are script-sourced by the T5.1 decision. Four values that were audit-only when
    the pass began are now printed (see §6): the tempering/utility split, the spike modes, the
    ℓ₀-invariance pair and the Λ = 512 Gaussian control, plus Code Cell 4's μ_u sensitivity, override
    diagonal and grid ceiling.
  - **Machine-dependent numbers removed from the prose.** Wall-clock seconds drift between runs
    (5.9 h / 6.2 h, 1.93 s / 2.05 s), so Text cell 4 now quotes step counts and says "hours" and "a
    couple of seconds"; the cell's own cost lines carry the seconds.
  - **Executions.** main.ipynb: **RUNNER OK, 0 errors, 6 figures, 252 s, 14/14 checks.**
    appendix_E.ipynb: **RUNNER OK, 0 errors, 3 figures, 639 s, E2 18/18, E3 PASS** (202 lines
    recorded, 201 identical, 0 deleted, 1 changed, 4 inserted).
  - **New in this pass, recorded:** cost lines. Code Cell 2's realizability run now tags its wall
    clock and step counts `cost:`, and E3 drops those lines from the comparison, because the relay
    reaches the same fixed point along a slightly different path (42,551 steps in main, 42,637 in the
    appendix) and a strict line diff would otherwise fail on a difference that is not a quantity.

---

## 4. Findings and issues log

Pre-populated from the audit (2026-09-11). New entries are appended during T0–T7; T8's are appended
2026-09-12.

- **F1** OPEN-1 (above): from θ_u(0) = +1 the flow misses θ\* wherever θ\* < 0. Resolved
  2026-09-11 first as (a) +1, then (b) ±1 on θ\*'s side, finally (c) θ_u(0) = 0, which reaches θ\* in
  all 145 configurations tested.
- **F2** The Sec. 8.2 F-monotone check fails at θ\* under τ_ε = 0.1 (min step −18.3). It is
  physical: −4.6 at dt/4, over 1,605 decreasing steps instead of 400. It is cured by τ_ε = 1e-4.
  This is the origin of D4.
- **F3** `infer`'s guard rejects dt = 0.02 at θ\* (bound 0.0025), and `max_steps` = 20000 is too
  short (~37k needed at τ_ε = 0.1). `learn_theta_u` threw "fast subsystem did not equilibrate"
  inside Part A.
- **F4** Integration is infeasible under the flat (θ\* = 5950.6) and delta-like (θ\* = 1407.8) priors
  and at most plane cells. Under D4 it gets costlier still, since τ_ε scales as θ⁻².
- **F5** Two figure captions in Code Cell 2 were already wrong (T2.8).
- **F6** At θ\*, Beta(1,3) gives E[s | all] 0.334 < E[s | some] 0.361, so the scale inverts.
- **F7** At θ\*, the plane's Λ = 4α diagonal (α = 32…512) flips from entry-held (leak 0.000) to
  overridden (leak 0.835–1.000).
- **F8** At θ\*, the utility level's own contribution to Δ_some is negative under all five Part D
  priors. The positive shifts are tempering alone.
- **F9** Part C's "θ_u\* delivers −0.5222" under the delta-like prior was the **Gaussian** θ\*
  carried over. Its own θ\* gives −0.5217.
- **F10** Text cell 6's geography numbers (95, 65, 50, 82, 26, 39, 30/28, 74, 43, 109, 78, 55, 22,
  the floors) and Appendix C §6 / Appendix D numbers are printed by no cell. They were computed off
  notebook. The audit script reproduces them exactly at θ_u = 1.
- **F12** §2's first list of configurations with θ\* < 0 was incomplete. Beyond the Gaussian,
  Beta(1,3) and plane cells (1, 2), (1, 4), (2, 2), θ\* < 0 also holds for Λ = 1…16 of the Λ sweep,
  μ_u = [0,1], [1,2] and [2,1], every K of the ladder, and all four smooth masks: 21 of 145 in all.
  These are the Gaussian-based evaluations. Under reading (c) none of them is missed; the count
  matters for the prose explaining why +1 is not the start.
- **F13** The θ_u = 0 network is the **tempered** control, φ_S = ½(ℓ₀−φ_L), and not q_lit, which
  also needs σ_S → ∞ (user correction, checked in `qlit_check.py`). My earlier answer called the start
  "the network the notebook presents as the control", which blurred the two. Any existing prose or
  comment that says "the θ_u = 0 control" where q_lit is meant, or vice versa, is a prose item (5.B).
  T2.8's figure captions are an instance already known.
- **F14 (during T1.3) D4 has an exact form, and it is a factor of 4.** Eliminating the error units
  from Eqs. (18)–(19) gives, for each eigenvalue λ of the state Hessian H = −∇²F (in the quadrature
  metric), the pair of system eigenvalues s solving τ_ε τ_φ s² + τ_φ s + λ = 0, plus s = −1/τ_ε with
  multiplicity K. Checked: every predicted s is an eigenvalue of the full 307-dimensional system, to
  σ_min(A − sI)/‖A‖ ≤ 1.3e-18 (`d4crit2.py`). So **no mode oscillates iff τ_ε ≤ τ_φ/(4 λ_max(H))**.
  λ_max(H) is 810.69 at the Gaussian θ\*, one above Eq. (28)'s 809.69; Eq. (28) is H's diagonal φ_u
  entry, not its top eigenvalue.
  - **Empirical.** With τ_ε = τ_φ/(k λ), the F-monotone threshold measured by Euler (`d4k.py`,
    `d4crit.py`) rises with |θ| toward 4: k ∈ (0.5, 1] at θ = 14.5, (1.75, 2] at 28.44, (2, 4] at 55,
    and k = 3 fails at θ = 200. At k = 4, F is monotone at every θ tested (5 to 200, dt = τ_ε/2 and
    τ_ε/4). The decreasing steps sit in the opening transient, t ≈ 2τ_ε. Starting the error units at
    their residuals instead of silent makes them worse, not better (`d4init.py`), so the effect is lag,
    not initialization.
  - **Consequence.** The ratio T1.3 asked for is 4, derived rather than fitted: critical damping of
    the stiffest mode. A fixed ratio smaller than 4 is tuned to a range of θ and fails beyond it.
  - **Side fact.** At θ_u = 1, λ_max(H) = 3, so the old default τ_ε = 0.1 exceeded 1/12 and the stiff
    mode was mildly oscillatory there too. F stayed monotone only because k = 0.83 is above that θ's
    threshold.
  - **Prose.** D4 is stated as τ_ε ≤ τ_φ/(4 λ_max(H)), with "≪" replaced by the critical-damping factor.
- **F15 (during T1.3/T1.4) The θ_u flow from 0 cannot be integrated to θ\*.** F̃ flattens toward its
  asymptote at large |θ|. The discrete Eq. (20) map (one update per settled fast subsystem, step
  (τ_φ/τ_θ) dF̃/dθ) gives θ ≈ −6.0 after 25 and −7.2 after 50 updates at τ_θ = 20 (θ\* = −28.44), and
  is not within 0.1% of θ\* after 5,000 (`thmap.py`). The same holds at τ_θ = 5 and 2, and for
  Beta(1,3) and Beta(3,1). So the dynamics verify direction, monotone F̃ and a shrinking gradient
  only. Arrival at θ\* rests on the closed form and the monotone rise (145/145), i.e. on D1/D5. The
  prose must not say the flow is run to θ\*.
- **F16 (T1.3) `infer` reported `steps` as `len(history)`**, which is 0 whenever
  `record_history=False`. Pre-existing and harmless so far, since every caller that printed steps
  recorded history. Fixed: `steps` is now the count of steps taken.
- **F17 (T1.1) The bisection `theta_u_stationary_point` is accurate only to ~4e-8 at |θ\*| > 6000.**
  The closed form is exact there (it equals a 50-digit root of the same coefficients). T2.1's
  independent cross-check must therefore use a tolerance that scales with |θ\*|, or run only where
  |θ\*| is moderate. The Gaussian, where the check runs, agrees to 4e-14.
- **F18 (T2.3) The Sec. 8.1(iii) relaxation check reached the roundoff floor under D4.** It took the
  second half of the max-derivative trace, whose end sits at the 1e-10 tolerance. Under D4, roundoff in
  ε̇ is amplified by 1/τ_ε ≈ 3,200 at θ\*, and the local rate scatters by ~1e-3 below ~1e-8
  (`tail.py`). Rates per unit time came out 1.000378 / 0.999922 / 1.000379, a FAIL at spread 4.6e-4.
  Fixed: window chosen by value (1e3 to 1e6 times the tolerance) and a least-squares slope, rate per
  unit time rather than per step (a per-step factor at dt = 1.5e-4 is ~1 − 1.5e-4, which a 1e-6
  tolerance cannot test). Rates now 1.000231 for all three, spread 7.7e-7 at θ\*, 2.4e-10 at
  θ_u = 1 (`tail2.py`); tolerance set to 1e-5 relative. The prose describing the check (Text cell 4
  Part A) must follow: "contraction per step" becomes "rate per unit time".
- **F19 (T2.4) The implicature probe's verdict tested only the first condition.** It printed "the
  criterion is met / NOT met" from Δ_some < 0 alone, while Text cell 4 Part C defines the criterion as
  the conjunction. At θ_u = 1 and at the Gaussian θ\* the two agree (the first condition fails), so no
  stored conclusion was wrong. Fixed: both conditions and the conjunction are printed.
- **F20 (T2.4) Wording in the probe attributed the shift to "the utility level".** The shift of
  Eq. (37) is against q_lit, and so includes the tempering; Text cell 6 says Δ is not a measure of the
  utility level. Reworded to "the settled belief holds … more/less all-region q-mass than q_lit".
- **F21 (T2.8) Figure 3's suptitle was clipped at both edges** (one long line). Now two lines.
- **F22 (T3.4) Under learning, the sign of μ_u is invisible, exactly.** Reversing μ_u flips the outer
  coefficients of Eq. (B2) and not the middle one, so θ\*(−μ_u) = −θ\*(μ_u). With the symmetry
  φ_S\*(θ, μ) = φ_S\*(−θ, −μ), every read-out is then identical. Measured: relative gap 0.0 and E[s]
  gap 0.0 over the eight signed settings. Learned E[s] is also nearly flat in |μ_u| (0.2718–0.2759
  under *no*). For the prose: Text cell 5's reading of the tilt and width directions (Eq. 35,
  lines 143–149, 186–187) holds at fixed θ_u only, and the learned-θ statement is "μ_u's sign carries
  nothing". This agrees with Text cell 6's μ_u-sensitivity paragraph inverting (5.B).
- **F23 (T4.3) `override_threshold`'s "θ_u\*" column used the Gaussian's θ\* on Beta(1024, 1).**
  It called `theta_u_stationary_point(net)` on the evaluation network (θ\* = −28.4375) and applied
  that value to a different prior, which is F9's mistake again. Text cell 6's "36–45% at
  θ_u\* = −28.4375" is therefore a fixed-θ control mislabelled as learned. Replaced by the learned
  column. The learned range happens to read the same, 36–45%, because the effect saturates in
  |θ_u| and both θ values are past saturation. The prose must relabel it, not renumber it.
- **F24 (T4.4) Plane sign counts are roundoff-sensitive at learned θ\*.** The α = 1024 row is
  saturated (the prior overrides the entry), and its differentials are ±2e-16 up to 4e-13. Both
  the audit and the first run counted their signs. So §6's "97 negative" and "18 positive plus
  saturated (1024, 128)" were roundoff. Also the first-condition floor at α = 1024 ("512", via a
  −6.7e-16 shift) is an artefact. With a 1e-12 zero band the robust values are: differential
  negative 94, positive 17, saturated 10; raw shift negative 74; opposite signs 53; agreement 104 / 84;
  first floor at α = 1024 = 2048 (only Λ = 2048 is resolved). These **supersede §6** for T7.4.
  Unaffected: 72 / 62, the extremes, 32 (30), 59, 33, the band, the delta row, the other floors.
  At θ_u = 1 (the stored Text cell 6 numbers) no cell was saturated (95 + 26 = 121).
- **F25 (T5.1, pre-existing, not caused by this change) Appendix C §6 quotes two values inconsistently
  with the code.** (i) "κ_some = κ_all = −1.13989" is the projection of χ_y, while κ is defined as the
  projection of φ_L = Λχ_y (Code Cell 3 Part A prints −9.11909 = 8 × −1.13989). Either the text
  says χ or the value is −9.11909. (ii) The *no* vs *all* row reads 6.0790 / 5.5200, where the
  current code gives 6.0794 / 5.5197 at θ_u = 1, most likely from an earlier revision. Both go on the
  prose list. The rest of §6's θ_u = 1 values reproduce exactly. **Widened during §5:** the per-unit-Λ
  κ is used throughout Appendix C (lines 38, 79–84, 131, 171), not only in §6, while line 18 defines
  κ on φ_L.
- **F26 (T6.4) Under D4 the relay adds no stability requirement of its own; Appendix E's "the relay
  must be fast, tightening as θ_u⁻²" came from τ_ε = 0.1.** Two lags are stable at any gain and three
  are not. With τ_ε = 0.1 the error lag was the third, so the relay had to be faster than ~θ⁻²
  (80× faster than τ_ε at the Gaussian). At D4's τ_ε the loop is effectively two lags: the spectrum
  is stable for every τ_relay tested (to 10⁴ τ_ε), and the largest stable τ_relay below τ_ε is τ_ε
  itself. The ordering τ_r ≤ τ_ε survives for a different reason: a relay slower than the error units
  makes F non-monotone (6 decreasing steps at 2τ_ε, 58 at 10τ_ε), exactly as slow error units do.
  τ_r therefore inherits θ⁻² from τ_ε rather than carrying its own. Also: at τ_r = τ_ε/10 the
  settling test fails on roundoff amplified by 1/τ_r, though the state is at the fixed point.
  **Prose:** Appendix E E.1 (lines 85–87, "τ_r < 1.25e-3, eighty times faster") and E.2 (line 40, "the
  relay must be fast") must be rewritten around this, and §0 of appendix E if it states the
  cost. This supersedes the E-relay entries in §6 and 5.B.
- **F27 (T7.4) Some numbers Text cell 4 Part D and Text cell 6 quote are still printed by no cell.**
  These are the tempering and utility parts of Δ_some per prior (§6: −0.0167 … and +0.0175 …), the
  spike modes and densities under *some* for flat and Beta(3,1), the φ_S-contrast deviation across
  priors (0.026), and the μ_u-sensitivity rows at (1, 8) and (16, 128). F10 was fixed for the plane
  (T4.4) but not for these, because no task asked for them. For the Gaussian, both parts can be
  derived from printed columns (+0.0175 = 0.0191 − 0.0016; −0.0167 = +0.0008 − 0.0175). **Open
  suggestion, not done:** add tempering and utility columns to `base_prior_sweep`, which would make
  F8's "negative under all five" printed rather than quoted. It needs a re-execution (~15 min for both
  notebooks).
- **F28 (2026-09-12, answering the user's question about F15 and F4) The verdicts do not depend on
  reaching θ\*, and at the θ_u a feasible run reaches they can be integrated.** Measured with the
  closed-form Eq. (20) map from θ_u(0) = 0 at τ_θ = 20 (`reach15_4.py`, `reach_feas60.py`).
  - **Part D at the reachable θ_u** (θ after 25 and 60 updates; Δ_some and q_H there against θ\*):

    | prior | θ\* | θ@25 | θ@60 | Δ_some @60 | q_H @60 | Δ_some at θ\* | q_H at θ\* | verdict |
    |---|---|---|---|---|---|---|---|---|
    | Gaussian | −28.44 | −6.06 | −7.57 | +0.0009 | 0.0025 | +0.0008 | 0.0025 | second only, both ways |
    | flat | +5950.6 | +4.02 | +5.58 | +0.0397 | 0.0901 | +0.0295 | 0.0799 | second only, both ways |
    | Beta(1,3) | −14.51 | −5.15 | −6.37 | +0.0004 | 0.0005 | +0.0004 | 0.0005 | second only, both ways |
    | Beta(3,1) | +55.01 | +6.22 | +7.81 | +0.0513 | 0.1880 | +0.0421 | 0.1788 | second only, both ways |
    | delta | +1407.8 | +45.09 | +55.15 | −0.5212 | 0.4357 | −0.5217 | 0.4351 | **both, already at 25 updates** |

  - **Plane:** the set of cells meeting both conditions at the 60-update endpoint is **identical** to the
    set at θ\*, the same 33 cells. The effects saturate in |θ_u| long before θ\*.
  - **Cost.** At θ\*: delta and (64, 512) 5.2 h per inference, (128, 2048) 75 h, (8, 64) 327 s. At the
    60-update endpoint the same configurations cost **22 s to 100 s** (delta 29 s, (8, 64) 22 s,
    (16, 128) 27 s, (1, 512) 35 s, (128, 2048) 100 s). None falls under FEASIBLE_STIFFNESS = 1e3
    (about 8 s), so none is integrated as the code now stands, but all are minutes, not hours.
  - **What is integrable as it stands:** the Gaussian and Beta(1,3) rows of Part D and 2 of 121 plane
    cells, (1, 2) and (1, 4). **None of them meets both conditions** (Δ_some +0.0104 and +0.0176,
    q_H 0.0604 and 0.0679). So every configuration where the conjunction holds is currently reported
    in closed form only. **Superseded by F29:** true of θ\* and of the 25/60-update endpoints, false
    of the criterion itself, which is met far earlier and is integrable there.
  - **Consequence for the prose (A10):** the criterion verdicts rest on the closed form, but they are
    not an artefact of an unreachable θ\*: a partially learned network gives the same verdicts, and the
    dynamics could be shown there at about 30 s per inference. **Superseded by F29:** the dynamics
    are now shown, at 1.9 s, and the notebook does it.
- **F29 (2026-09-12, T8) The conjunction is met at a |θ_u| of a few units, and is demonstrated in
  the dynamics with nothing in closed form.** The question F28 did not ask was how much of θ\* the
  criterion needs. Very little, and that changes what the realizability paragraph has to concede.
  Measured by the new block (printed in the executed notebook, so not an F27 gap).
  - **Threshold.** The least |θ_u| on the ray 0 → θ\* at which both conditions hold is **2.126** for
    the delta-like prior (λ_max(H) = 6.5 there, separation 4λ = 26), against θ\* = 1407.8 with
    λ_max(H) = 1.98e6. Of the five Part D priors, the delta-like row is the only one with a threshold
    at all, which is Part C's verdict restated. The conjunction holds from the threshold all the way
    to θ\* (200-point check on the ray).
  - **Plane.** Over the 33 both-condition cells: |θ_crit| from **0.100 to 4.250**, λ_max(H) there from
    **2.0 to 20.1**, so **all 33 are integrable** under FEASIBLE_STIFFNESS = 1e3, against 3.5e4 to
    3.6e7 at their θ\*. Eq. (20) from 0 passes the threshold in **at most 2 updates**, and the
    conjunction then holds to θ\* in all 33.
  - **The run.** Delta-like row, end to end, nothing in closed form: one integrated update of Eq. (20)
    (all three utterances integrated inside it, 0.03 s) takes θ_u from 0 to **13.374852**, agreeing
    with the closed-form-equilibrated update to **6.8e-14**; then Eqs. (18)-(19) at that θ_u,
    **42,551 steps, 1.95 s, 46 µs/step, λ_max(H) = 180.9, τ_ε ≤ 1.38e-3**. Off that integrated fixed
    point: **Δ_some = −0.5182 and q_H = 0.4386, both conditions met**, and max |φ_S − φ_S\*| against
    Eqs. (15)-(16) = 9.5e-11. The same inference at θ\* would be 4.66e8 steps, about **5.9 h**, at a
    separation of 7.9e6.
  - **What this settles.** Part C's verdict is now demonstrated dynamically, not only in closed form.
    What remains reported in closed form is the verdict **at θ\***, and the honest statement is that
    the expensive object is the maximizer of F̃, not the implicature. A10(ii) is rewritten accordingly.
  - **What it does not settle (user, 2026-09-12).** 1.9 s, or 0.06 s at the cheapest plane threshold,
    is still not a plausible cost for the process being modelled; what the seconds stand for is tens
    of thousands of Euler steps and a 26× to 7.9e6× separation between error and state units. That is
    the complexity issue the outline raises about a hypothesized alternative representation level, and
    it stays in the outline (A11).
- **F30 (2026-09-12, T10.2) The learned contrasts' spread across priors is 0.058, not 0.026.**
  §5.B's line for Text cell 4 lines 207-213 quoted 0.026 from the audit. Recomputed against the
  executed model (`g512.py`): the largest disagreement between two priors' φ_S contrasts, taken over
  the all−some and no−some contrasts at a common Λ = 8, is **3.55e-14 at a shared θ_u = 1** and
  **0.0575 at each prior's own θ\***. The audit's 0.026 was presumably a different contrast or a
  mean; the prose carries 0.058 with its definition stated, so it is reproducible.
- **F31 (2026-09-12, T10.5) Appendix C's m = 2 comparison figure is not reproducible as recorded.**
  §5.B carried "3.445 over {0, 1, −1, 5}, and 3.712 with θ\* included" for the spread of the
  all−some φ_S contrast at m = 2. Measured against the executed model (`appc.py`): **3.87** in the
  quadrature norm over that set and **4.21** with θ\* (the printed 9.6995 → 13.9124 series), or
  **1.72** and **1.86** in max-abs, which is the norm Appendix C's own table uses. Neither pair
  gives 3.445. The prose now states the norm alongside the number.
- **F32 (2026-09-12, T10.6) main's new blocks broke Appendix E's E3 check, which §5 did not
  anticipate.** E3 diffs Code Cell E2's output against main's Code Cell 2 output line by line, so
  adding the realizability block and the two Part D prints to main alone produced **FAIL: 150
  identical, 43 deleted**. Any future addition to main's Code Cell 2 must be mirrored into E2 in the
  same commit. E2 is now re-mirrored by lifting the blocks verbatim out of main's source, so the two
  cannot drift by retyping.
- **F33 (2026-09-12, my error) The pre-T8 backup was overwritten at the end of the session.**
  `backups/2026-09-12/` was taken before T8 and held main.ipynb and this file as they stood after T7.
  A final `cp` of the finished files into the same folder overwrote both. The snapshot is
  unrecoverable. Surviving snapshots: `backups/2026-09-11/` (before T0, i.e. before θ_u was learned
  anywhere) and `backups/2026-09-12-after-prose/` (the finished state, byte-identical to what
  `backups/2026-09-12/` now holds). A README in that folder says so. **Rule for next time: never
  copy into an existing dated backup folder; make a new one.**
- **F34 (2026-09-13, running down F32) A step count's last digits are set by the roundoff floor, not
  by the dynamics.** Chasing why main and Appendix E disagreed on the realizability run's step count
  (42,551 against 42,637) gave a more general fact about every `steps` this notebook prints.
  - **The two implementations agree exactly on the dynamics.** Settled at a *common* θ_u, main's class
    and E1's take **42,550 steps each**. They differ only because E1 forms Eq. (20)'s gradient as
    ⟨ε_S, r⟩ where main forms Σ_j φ_u,j⟨ε_S, b_j⟩: mathematically identical, different summation
    order, so the gradient at θ_u = 0 comes out 267.49704880934354 against 267.49704880934377 and the
    θ_u after one update differs by **1.07e-14**.
  - **That difference is amplified because the stopping test sits on a floor.** `infer` stops when
    max|derivative| < 1e-10 for 10 consecutive steps. Over the last 2,000 steps the derivative is not
    decaying: it hops between ULP-quantized values in a band of about **8.2e-11 to 1.6e-10** (observed
    step-to-step ratios of exactly 0.75, 1.5, 2.0; mean ratio 1.004), and the tolerance lies inside
    that band. Convergence is therefore declared when ten consecutive roundoff-level samples happen to
    land below 1e-10.
  - **Measured sensitivity, in main's class alone, no relay anywhere:** perturbing θ_u by a relative
    1e-16 / 1e-15 / 1e-14 / 1e-13 / 1e-12 / 1e-9 / 1e-6 gives 42,550 / 42,629 / 42,765 / 42,544 /
    42,624 / 42,567 / 42,608 steps. Non-monotone, ±0.3%, at perturbations far below anything the model
    means.
  - **What this does and does not touch.** The fixed point is unaffected: the floor is the same order
    as the agreement with Eqs. (15)-(16) already reported (9.5e-11), which is the accuracy the
    integration tops out at, and every verdict is read off the converged state. What it touches is the
    *reporting* of step counts: their leading digits are the cost, their last two or three are noise.
    The prose now quotes them to three significant figures and says so; the cells still print the exact
    integer, which is correct for the run that produced it.
- **F11** The margin of F̃(θ\*) over the asymptote is positive in every configuration tested. It is
  ~0 to four decimals under the flat prior (θ\* = 5950.6), where the maximum is extremely shallow.

---

## 5. Prose: everything that must change (FINAL, 2026-09-11, written against the executed outputs)

Line numbers refer to the markdown cells as they stand (unchanged by T0–T7). "Printed" means a
cell now prints the number; "not printed" means it comes from a recorded script (§7) or the audit
and is flagged in F27. Conventions apply throughout: no dashes in notebook prose, loose lists, and the
equation-numbering scheme of the settled conventions.

### 5.A New statements the decisions and findings require

- **A1. θ\* is learned, and is specific to every configuration (D1, D2).** Say that θ_u carries
  θ\*, the maximizer of F̃ by Eq. (B2). θ\* is a function of every input and hyperparameter,
  enumerated: ℓ₀, Λ, μ_u, θ_L (n), K and grid half-width, the mask sharpness, B (m), every σ, and the
  exposure ensemble. Every configuration an evaluation visits carries its own θ\*. Sites:
  - Text cell 3 commitments list (lines 3–13): add θ_u learned per configuration as a commitment.
  - Text cell 3 §2 inventory (line 71, the θ_u row): "variational (slow); learned, θ_u\* of Eq. (B2)".
  - Text cell 3 §7 under Eq. (20) (lines 347–353).
  - Text cell 3 §8.5 (lines 440–452).
  - Appendix B, where the exposure ensemble is introduced (lines 55–58).
- **A2. The start θ_u(0) = 0 and what the network is there (OPEN-1 (c), F13).** State:
  - θ_u(0) = 0 is one start shared by every configuration.
  - At θ_u = 0 the model sits at the **tempered version of the control**,
    φ_S = σ_S/(σ_L+σ_S)·(ℓ₀−φ_L) = ½(ℓ₀−φ_L). It is **not** the literal listener q_lit, which also
    needs σ_S → ∞. Do not equate the two.
  - θ_u leaves zero because the gradient there is ⟨μ_u, Σ_y c_y⟩/S ≠ 0 (printed: −6.8187). Tie this
    to Text cell 3 §3's reason μ_u ≠ 0.
  - It rises monotonically to θ\*, because the roots of Eq. (B2) have opposite signs and zero lies
    between them (145/145 configurations).
  - One sentence on why not +1: it misses θ\* in 21 of 145 configurations, the default among them (F12).

  Sites:
  - Appendix B lines 65–66, replacing "the flow reaches it from any τ_θ started on the same side of
    zero". This is the main site.
  - Text cell 3 §7 and §8.5: one sentence each, pointing to Appendix B.
  - Text cell 4 Part A's description of the Sec. 8.5 check (the check now starts from 0).
  - Text cell 4 lines 52–58 (the θ_u control paragraph): the tempered control is also the flow's start.
  - Text cell 6 line 137 ("with the utility level severed"): say that "severed" means the tempered
    control.
  - Appendix E E.3 table, mirrored.
- **A3. The timescale commitment D4, in its exact form (F14).** Eliminating the error units gives
  τ_ε τ_φ s² + τ_φ s + λ = 0 for each eigenvalue λ of H = −∇²F. No mode oscillates iff
  **τ_ε ≤ τ_φ/(4 λ_max(H))**. λ_max(H) is 810.69 at θ\*, one above Eq. (28)'s 809.69, since Eq. (28)
  is H's diagonal φ_u entry. The commitment replaces "τ_ε ≪ τ_φ" by a critical-damping bound that
  scales as θ_u⁻². Evidence to cite:
  - F2: F non-monotone at τ_ε = 0.1 (min step −18.3).
  - The measured thresholds k ∈ (0.5,1], (1.75,2], (2,4] at θ = 14.5, 28.4, 55, and failure at k = 3
    for θ = 200, rising toward 4.
  - F monotone at k = 4 for every θ tested.
  - Pre-settled error units do not help (the effect is lag, not initialization).

  Sites:
  - Text cell 3 commitments list: a new item.
  - The inventory's τ row (line 84: "τ_ε ≪ τ_φ ≪ τ_θ").
  - Eq. (20)'s ordering (line 345) and lines 351–353.
  - §8.3 (lines 404–409): give the derivation and dt = τ_ε/2.
  - Appendix A line 67 (the ordering quoted there).
  - **Numbering:** state D4 without adding a numbered equation (fold it into Eq. (20)'s ordering, or
    display it unnumbered in §8.3). A new number would shift (21)–(41).
- **A4. Closed form where integration is infeasible (D5), and the rule.** Integration is used
  where λ_max(H) ≤ 1e3, about 8 s per inference. Elsewhere the closed form is used, exact by §8.6,
  and every output says which. Which configurations integrate:
  - the Gaussian and Beta(1,3) among Part D's priors;
  - 2 of the 121 plane cells, (1, 2) and (1, 4).

  Sites:
  - Text cell 4 Part B (the Λ sweep is now closed form, since θ\* reaches 1535 at Λ = 32).
  - Text cell 4 Part D (lines 207–212).
  - Text cell 6 *Method* (lines 164–168) and its verification sentence (lines 250–253).
  - Text cell 4 *Integration cost* (A5).
- **A5. Text cell 4 *Integration cost and conditioning* (lines 342–379): rewrite in full.** The present
  text sets dt by the Euler bound at τ_ε = 0.1 and says Part A "tests the stationary point in closed
  form instead of integrating to it". Both are now false.
  - Part A integrates at θ\* under D4 (163,037–163,138 steps at dt = 1.54e-4; 7.7 s per inference, 11.5 s
    with history; check_specification 101 s; main.ipynb 245 s).
  - The flow of Eq. (20) is integrated for 25 and 60 updates from 0 and does not reach θ\* (F15).
  - Replacement table (values computed):

    | \|θ_u\| | 0 | 1 | 10 | 28.44 | 50 |
    |---|---|---|---|---|---|
    | Eq. (28) rate | 1 | 2 | 101 | 809.69 | 2501 |
    | λ_max(H) | 2 | 3 | 102.0 | 810.69 | 2502 |
    | τ_ε bound τ_φ/(4λ_max) | 0.125 | 0.0833 | 2.45e-3 | 3.08e-4 | 9.99e-5 |
    | dt = τ_ε/2 | 0.0625 | 0.0417 | 1.23e-3 | 1.54e-4 | 5.00e-5 |

  - Per prior at its own θ\*: λ_max(H) 810.7 (Gaussian), 3.54e7 (flat), 212.5 (Beta(1,3)), 3028
    (Beta(3,1)), 1.98e6 (delta); about 201 λ_max(H) steps per inference, so 1.6e5 steps for the
    Gaussian and 7e9 for the flat prior.
  - The conditioning paragraph (condition number (1+θ²)/2, 404.8 at θ\*) stands, and gains the
    corollary that conditioning now also sets τ_ε, not only dt.
  - Add the realizability discussion of A10 here: what is integrated, what is not, and the physical
    reading of the separation D4 demands.
- **A6. The flow from 0 is not integrated to θ\* (F15).** The dynamics verify direction, monotone F̃
  and a shrinking gradient (0 → −6.060 in 25 updates; 0 → −7.567 in 60, gradient −0.627, "still
  ascending"). Arrival rests on the closed form and the monotone rise. No sentence may say the flow is
  run to θ\*. Add what F28 measures: the verdicts at the reachable θ_u are the ones at θ\* (the
  delta-like prior meets both conditions after 25 updates, at θ_u = 45.09), so nothing in Part C or
  Text cell 6 depends on the flow completing. Sites: Text cell 3 §8.5; Text cell 4 lines 85–87 ("the settled θ_u of the learning
  probe" is −7.567, which the prose should name); Appendix B.
- **A7. Every retained control gets its justification (D2).** See 5.C.
- **A8. Under learning the sign of μ_u is invisible (F22), and μ_u is nearly inert.** θ\*(−μ_u) =
  −θ\*(μ_u) exactly, and every read-out is identical (printed: gap 0.0). Learned E[s] moves by at most
  0.0041 across the eight signed settings. Sites: Text cell 5 §2 (lines 143–149, 169–186); Text cell 6
  lines 50–61.
- **A9. The relay's speed requirement collapses into D4 (F26).** Appendix E; see 5.B.
- **A10. Realizability: report the closed form, and say plainly what could and could not be run.**
  The user's instruction (2026-09-12): evaluations are reported under the closed form, and the prose
  additionally raises the realizability issue. Four things to state, with the numbers.
  - **(i) What is integrated and what is not (F4).** An inference costs about 200 λ_max(H) Euler steps
    under D4, so: Gaussian 7.7 s, Beta(1,3) 2 s, Beta(3,1) 30 s, delta-like 5.2 h, flat about 4 days;
    on the plane, 2 of 121 cells. The evaluation integrates where λ_max(H) ≤ 1e3 and reads the closed
    form elsewhere, exact by §8.6 and verified against the dynamics wherever both are available
    (9.9e-11 to 1.0e-10). Correctness is not at stake; what is missing is a demonstration that the
    dynamics reach those fixed points **at large θ_u**, which is now the only thing missing: at the
    θ_u the criterion needs, they are integrated (F29).
  - **(ii) What is reported in closed form is the verdict AT θ\*, not the verdict (F29, replacing the
    earlier reading of F28).** The conjunction is met at |θ_u| = 2.126 under the delta-like prior, and
    between 0.100 and 4.250 across the 33 plane cells, where λ_max(H) is 2.0 to 20.1 and every one of
    them is integrable. Eq. (20) from θ_u(0) = 0 passes that threshold in at most two updates, and the
    conjunction holds from there to θ\*. The notebook now runs one such case end to end with nothing in
    closed form: Δ_some = −0.5182 and q_H = 0.4386 off an integrated fixed point, 42,551 steps, 1.95 s.
    So say that Part C's verdict is demonstrated in the dynamics, and that the closed form is what
    carries it to θ\*, 5.9 h away. Do not write that the verdict rests on the closed form.
  - **(iii) The verdicts do not depend on reaching θ\* (F28 + F29).** The effects saturate in |θ_u|
    (Eq. 24's limit is the same point): at the 25-update θ_u the delta-like prior already gives
    −0.5210 and 0.4358 against −0.5217 and 0.4351 at θ\* = 1407.8, and the plane's both-condition set
    is the same 33 cells at the threshold, at the 60-update endpoint and at θ\*. So nothing in Part C,
    Part D or Text cell 6 waits for the flow to arrive. What θ\* adds, at a cost of hours, is the
    maximizer of F̃, not the implicature.
  - **(iv) The timescale separation D4 demands, as a physical claim (F14 + F4).** τ_ε ≤ τ_φ/(4 λ_max(H))
    means error units about 3,000× faster than the state units at the Gaussian θ\*, about 1.2e4× at
    Beta(3,1), 8e6× at the delta-like prior and 1.4e8× at the flat prior. No neural circuit has
    separations of that order. What D4 buys is §8.2's monotone rise of F, **not** convergence: at
    τ_ε = 0.1 the system still reaches the same fixed point, with F dipping during the transient.
    So the honest statement is a conditional: either the model asserts those separations, or §8.2's
    claim weakens to convergence with a non-monotone transient at large learned θ_u. Recommend stating
    it as a limitation of the model at large θ\*, not as a numerical detail.

  All of (i)–(iii) are now printed by the notebook: Code Cell 2's realizability block (the per-prior
  threshold table and the end-to-end run) and Code Cell 4's conjunction block (the 33 cells). The
  prose reads those outputs; nothing here is quoted from a script.

  Sites: Text cell 3 §8.3 (the commitment and what it demands) and §8.6 (what the convergence does and
  does not show); Text cell 4 *Integration cost and conditioning*, which becomes the main site (A5);
  Text cell 4 Part D, one sentence saying which rows are integrated; Text cell 6 *Method* and its
  verification sentence; Appendix E E.2, where the same θ⁻² scaling is now the model's own rather than
  the relay's.

- **A11. The cost is implausible whatever its size, and that is the outline's argument, not this
  notebook's (user, 2026-09-12).** Say two things, briefly. **(a)** Seconds of settling per inference,
  whether 0.06 s at the threshold or hours at θ\*, is not a cost the process being modelled could
  plausibly pay; the figure that matters is not the wall clock but what it stands for, a settling of
  tens of thousands of steps and a timescale separation of 4 λ_max(H) between error and state units.
  **(b)** This is the complexity issue the background outline raises about a hypothesized alternative
  representation level. That level is not implemented here, so main.ipynb states the fact and defers
  rather than arguing it: two or three sentences, then a bare pointer to the background outline, with
  **no section numbers and no file name** (user, 2026-09-12: the outline is not finalized, and the
  stale copies have been moved out of the project folder). Whoever finalizes the outline supplies the
  target; until then the notebook says "see the background outline" and nothing more precise. Do not
  import the outline's argument into the notebook, and do not name the alternative level's mechanism.
  Sites: Text cell 4 *Integration cost and conditioning* (with A10); Text cell 3 §8.3 one clause;
  nowhere else.

### 5.B Sites whose content changes

**Text cell 3** (beyond A1–A3, A6)
- Lines 440–452, §8.5: start at 0; the flow's rise is monotone by Appendix B; the closed form supplies
  θ\* (A2, A6).

**Text cell 4**
- Lines 7–11 (Part A list): add the θ\* cross-check against an independent bisection (4.6e-14) and
  the learning check from θ_u = 0. Say that the relaxation rate is compared **per unit time** by a
  least-squares slope over a value-selected window (1.000231 for all three utterances, spread 7.7e-7),
  since per-step factors at small dt test nothing (F18). Part A is now 14 checks.
- Lines 13–20: tails 1.6e-3 / 1.8e-6 / 1.0e-2 → **1.7e-3 / 3.3e-6 / 1.1e-2** (printed).
- Lines 22–31: "**Everything else in this cell is reported at θ_u = 1** … the pinned value is close to
  the worst case" is replaced. Everything is reported at θ\*, and `theta_u_dependence` is a stated
  control (5.C). Kept: the contrast growth 9.6995 → 10.9524 → 13.9124; the ±θ gap is largest near
  |θ| = 1 (0.0483 / 0.0902) and falls to 0.0041 / 0.0083 at |θ\*| (printed). Dropped: the
  "worst case" sentence.
- Lines 33–35 (Part B): each Λ carries its own θ\* (−18.730 … +1535.417, +342.254), read in closed form.
- Lines 81–92: Δ_some **+0.0098 → +0.0008** at θ\*; utility part −0.0077 → **−0.0167** (derivable from
  printed columns); tempering +0.0175 unchanged. Delta-like prior: **both conditions are met**
  (Δ_some −0.5217, q_H 0.4351). "**The conjunction holds under none**" is false; it holds under the
  delta-like prior. The "not out of reach … Text cell 6" sentence becomes "reached here and over a band
  of Text cell 6's plane".
- Lines 94–98: keep the θ\* values only: *all* −0.4557, *no* +0.0003.
- Lines 103–108: Gaussian at Λ = 512 at its own θ\* (+1580.814): Δ_some **+0.0071**, against +0.0008 at
  Λ = 8 (not printed; audit).
- Lines 113–128: Eq. (23)'s identity is still exact to 1.8e-15 at θ\*. Eq. (24) predicts −0.5217, and
  the delta-like prior's **own** θ\* gives **−0.5217**. The −0.5222 was the Gaussian θ\* carried over
  (F9). "Every θ_u ≠ 0 … −0.0664 as θ_u → 0" is a θ-sweep statement and stays.
- Lines 151–160: "the second condition is not met alongside it there, q_H still holding 0.6080" is
  false: q_H = **0.4351**, met. "met alongside it at 22 of the 121 cells" → **33**. "The delta-like row
  is that band's neighbour rather than a member" → it is a member. "Part D's priors are simply not
  where it is reached" is inverted.
- Lines 199–204: "still 0.0061 apart in E[s] … 0.0002 by α = 1024" (the Λ = 8 spreads) →
  **0.0057 / 0.0003** under learning (recomputed, not printed). Leak bound 8e-71 → **1.1e-74** (printed).
- Lines 207–212: the ℓ₀-invariance of φ_S contrasts holds **at a shared fixed θ_u** only. At each
  prior's own θ\* the contrasts differ by 0.026 across priors. The closed-form agreement line
  (6.0e-11) becomes 1.0e-10 (Gaussian) and 9.9e-11 (Beta(1,3)), with the flat, Beta(3,1) and delta
  rows closed form (A4).
- Lines 214–221 (q_lit against the tempered belief): θ-independent, unchanged.
- Lines 223–234: Δ_some **+0.0008, +0.0295, +0.0004, +0.0421, −0.5217** (printed). The sign still
  follows the prior (four positive, delta negative). The "premise is right" sentence must say
  ℓ₀-invariance holds at fixed θ_u, and that under learning ℓ₀ also moves θ\*.
- Lines 236–244, table: q_lit unchanged; q_H **0.0025, 0.0799, 0.0005, 0.1788, 0.4351**; Δ as above;
  delta-like row: first met, **second met**.
- Lines 246–251: "**The conjunction holds under none of the five**" is replaced: it holds under the
  delta-like prior, and only there.
- Lines 253–263: prior masses unchanged. "The utility level's own contribution is small there and
  **of either sign**, −0.0077, +0.0027, −0.0033, +0.0142" → **negative in all four**, −0.0167, −0.0559,
  −0.0061, −0.0568, so the positive shifts are tempering alone (F8). Delta-like: −0.2902 → **−0.4631**.
  These are not printed (F27).
- Lines 265–279 (the spike): q_H 0.1384 / 0.2498 → **0.0799 / 0.1788** (printed). Full-network
  ζ-modes s = 0.62 / 0.83, densities 0.2119 / 0.2493, top node 0.0126 / 0.0211 → **s = 0.67 / 0.84,
  0.2767 / 0.3285, top node 0.0013 / 0.0023** (audit, not printed). q_lit's modes are unchanged.
  **Re-describe from the new figure 2:** the full network's s-density now turns sharply *down* at the
  top edge under both priors, while q_lit rises. So "the rise appears in the control and the full
  network alike" is false twice over. The panels draw q_lit, not the control (F13), and the full
  network no longer rises at the edge.
- Lines 342–379: A5.

**Text cell 5** (D3: the θ_u = 1 text stays; the learned reading is added beside it)
- Lines 80–84: state that θ_u = 1 is a **control**: fixing θ_u isolates μ_u's direct path, and the
  invariance holds at any fixed θ_u. Add that every setting is also reported at its own θ\*.
- Lines 100–108: keep Eq. (33) for θ_u = 1. Add the learned coefficient: **−0.0351 B at θ\*, opposite in
  sign and about ten times smaller** (printed).
- Lines 114–120: "Everything in this report was computed at θ_u = 1" → "the tables are at θ_u = 1, a
  control, beside a learned table". Add that re-learning θ\* per setting moves the φ_S contrasts by
  **3.19e-2** (printed), against 3.6e-15 at fixed θ_u.
- Lines 124–128: keep the θ_u = 1 ranges as the control; add learned: Δ_some **+0.0008 to +0.0009**,
  Δ_all **−0.4514 to −0.4641** (printed).
- Lines 143–149 (tilt and width): at θ\* both effects reverse sign and shrink tenfold (coefficient
  −0.0351). Under learning the sign of μ_u is invisible (A8).
- Lines 164–167: "21× below" holds at θ_u = 1. At θ\* the terminating field θ\*Bμ_u has norm
  **40.2167, 1.33× ‖ℓ₀‖** (printed), so "φ_u is set by ε_S from below rather than by μ_u from above"
  and "an order of magnitude below everything around it" hold only at the control.
- Lines 169–186 (the midpoint, Eq. 34): a θ_u = 1 control. Add that under learning it cannot be posed,
  since θ\*(0) does not exist, and that ±v give identical beliefs (A8).
- Line 205: "Computed … at θ_u = 1" → "at θ_u = 1, a control". **New:** the second table (printed),
  and a sentence reading it: E[s] is nearly flat across μ_u under learning.
- Lines 290–318 (§6 plane): unchanged in substance. Label the fixed-θ_u = 1 invariance block and the
  symmetry at θ ∈ {0.7, 1, 4} as controls (5.C).

**Text cell 6**
- Lines 3–10: "(… everything below holds θ_u = 1 …)" → every cell carries its own θ\*,
  **−557.67 to +12228.42, negative at (1, 2), (1, 4), (2, 2)** (printed).
- Lines 41–48 (grid caveat): D at Λ = 8 is 0.0061 → 0.0009 → 0.0002 at θ_u = 1, and **0.0057 → 0.0012 →
  0.0003** learned (recomputed). The E[s] ceiling of about 0.984 should be re-read, since learned
  E[s] at α = 1024, Λ = 8 is 0.980.
- Lines 50–61: "No other quantity is varied: θ_u = 1" → θ_u learned per cell. The μ_u-sensitivity
  paragraph **inverts**. At θ\*, μ_u is nearly inert: at (1, 8), E[s] 0.6449–0.6459 and Δ_some +0.0295 to
  +0.0305; at (16, 128), Δ_some −0.2003 to −0.2034 with no sign change (audit, not printed, F27). The
  "failure mode of Part B §4" reading holds at fixed θ_u only.
- Lines 76–83: tempering larger in **59** (was 74) of 121; Δ_some and the utility part disagree in sign
  in **53** (was 43). The Part D cross-check "−0.3488 in both places" → **−0.5217** (printed).
- Lines 103–113: tempering median 0.0007, max 0.0988 (unchanged); utility median 0.0153, max 0.7523 →
  **0.0405, 1.1884**. Sign agreement 109 / 78 → **104 / 84**. "Δ_no never exceeds 0.1539 in magnitude"
  is false: **max |Δ_no| = 1.0000**, on the override diagonal. So "wherever the effect is large the
  differential simply is the raw shift" fails there; restate.
- Lines 137–150 (override): severed and θ_u = 1 columns unchanged (controls). "At θ_u\* = −28.4375 it
  needs 36–45% more" is a fixed-θ control mislabelled as learned (F23). Replace with the **learned
  column, θ\* re-learned at every Λ: 1.9890 / 2.9334 / 4.3102, +45.4 / +36.0 / +41.6%** (printed); θ\* at
  the threshold is 13378–14946. The μ_u check now also runs at learned θ\*: **1.9890 for all five**.
- Lines 158–168 (*Method*): "a random sample of cells is re-run through infer" → only 2 of 121 cells
  are feasible under D4, and both are re-run (9.90e-11) (A4).
- Lines 182–187: negative in 95 → **94** (plus **10 saturated at roundoff**, the α = 1024 row, F24);
  65 → **72**; 50 → **62**; most negative −0.8109 at (64, 2048) → **−1.2470 at (64, 256)**; maximum
  +0.1279 at (1, 128) → **+0.0656 at (1, 64)**; raw *some* negative in 82 → **74**, reaching **−0.9466**.
- Lines 191–195: 26 positive cells at α ≤ 8 → **17, all at α ≤ 4**. Δ_some positive in 39 cells
  reaching α = 32 → **37, reaching α = 64**.
- Lines 197–201: |differential| < 1e-3 in 30, 28 with Λ ≤ α → **32, 30** (printed).
- Lines 203–210: the band's description and the delta-like cell: Δ_some −0.3488 → **−0.5217**.
- Lines 219–235: second condition 55 → **59**; both 22 → **33** (printed). First-condition floor → **512
  at α = 1, 64 at α = 8, 16 at α = 64, 2 at α = 128 to 512** (and 2048 at α = 1024, where only the last
  column resolves, F24). Second-condition floor → **2 up to α = 8, 64 at 16, 256 at 32, 512 at 64,
  1024 at 128, unreachable from α = 256**. Band (8, 128)–(128, 2048) → **(1, 512)–(128, 2048)**.
- Lines 237–246: "**Part D's rows sit outside that band, and the delta-like row sits just beside
  it** … clears the first floor of 2 but not the second's of 1024 … What the row lacks is lexical
  strength" is false. The delta-like row (64, 512) is inside the band (floors 16 and 512). As Λ rises:
  q_H **0.4351 → 0.1352 → 0.0102**, shift **−0.5217 → −0.8217 → −0.9466** (printed).
- Lines 248–253: "the delta-like row misses it by a factor of two in Λ" is false. The verification at
  (64, 2048) "to four decimals at 0.1459" cannot be run: θ\* = 5531 there, beyond integration under D4.
  Rewrite around the two feasible cells, or drop.
- **New:** the override diagonal (F7). At θ\*, shift(*no*) = +1 on a diagonal where the prior overrides
  *no*: (32, 128), (64, 256), (128, 512), (256, 1024), (512, 2048), visible in figure 3. The leak map's
  "smallest Λ holding *no*": 256, 512, 1024, 2048 for α = 32 … 256, none at α ≥ 512 (printed).
- **Figure captions** in prose, if any refer to "the θ_u control" in figures that draw q_lit, follow F13.

**Appendix A**
- Line 67: the ordering "τ_ε ≪ τ_φ ≪ τ_θ" → D4's form (A3).

**Appendix B**
- Lines 55–58: add the enumeration of what θ\* depends on (A1).
- Lines 65–66: the start premise (A2, A6). This is the main site.

**Appendix C**
- §6, lines 131–158: replace the θ_u = 1 values by the learned ones at m = 1, θ\* = +26.774, from §7.1:
  - *some* vs *all*: |dφ_S\*| **4.0000**, unchanged by (C3); |dE[s]| **0.2534**.
  - *no* vs *all*: |dφ_u\*| **0.68**, |dφ_S\*| **8.5464**, |dE[s]| **0.7818**.
  - Δ: **+0.0604 / −0.0473** against q_lit, **+0.0429 / +0.2715** against the tempered control.

  If the θ_u = 1 values are kept, justify them as a control (5.C).
- Line 150: (C3) holds with θ\* added (8.9e-16). The m = 2 comparison is 3.445 over {0, 1, −1, 5} and
  **3.712** with θ\* included.
- **F25 (pre-existing):** Appendix C defines κ_y = BᵀWφ_{L,y} (line 18) but tabulates it per unit Λ
  throughout (lines 38, 79–84, 131, 171: ±1.13989, ±0.72098, 0.72097). Code Cell 3 prints
  ±9.11909 = 8 × 1.13989. Either define κ on χ_y in Appendix C or scale the values. Also, the *no*
  vs *all* row (6.0790 / 5.5200) differs from the current code at θ_u = 1 (6.0794 / 5.5197).

**Appendix D**
- Lines 39–41: ‖r_S‖ at θ_u = 1 (23.19, 18.08, 23.10 under E; 10.56, 9.43, 10.36 under T) →
  learned **22.47, 15.76, 22.47** and **8.88, 3.18, 8.88** (§7.1). "θ_u\* is −28.43749 under both"
  stands.

**Appendix E** (F26)
- E.1 lines 84–93: "Code Cell E2 finds θ_u²τ_crit → 1, so τ_r ≲ θ_u⁻² … τ_r < 1.25e-3, some eighty
  times faster than the error units" and "refining dt … does not recover convergence" are true only at
  τ_ε = 0.1, which D4 forbids. Under D4:
  - The relay loop (Eq. E5) is stable for every τ_relay tested, to 10⁴ τ_ε. The largest stable
    τ_relay below τ_ε is τ_ε itself (printed: 1.0000 at θ = −20, θ\*, −40, −80).
  - The old boundary is reproduced as a control at τ_ε = 0.1 (1.0257, 1.0125, 1.0063, 1.0016).
  - What a slow relay still breaks is monotone F: 6 decreasing steps at 2τ_ε, 58 at 10τ_ε.
  - The ordering becomes τ_r ≤ τ_ε ≤ τ_φ/(4λ_max(H)), and τ_r inherits θ⁻² from τ_ε.
  - Per-prior bound τ_r < τ_ε(θ\*): 3.08e-4, 1.18e-3, 8.26e-5, 1.26e-7, 7.06e-9.
  - Eq. (E6), line 89, is restated accordingly.
- E.2 lines 30–40, 55: "the stronger the u → S gain … the faster its relay must be, on pain of
  oscillation … predicts ringing" must be re-argued. With D4 the relay must merely be no slower than
  the error units, which already scale as θ⁻²; there is no separate oscillation. The testable
  prediction becomes a non-monotone transient, not ringing.
- E.3 table: line 15 (Eq. E6: "a new commitment, with the separation scaling as θ_u⁻²") →
  D4 carries the θ⁻² scaling and E6 adds only τ_r ≤ τ_ε. Line 29: "Verified again here at 17/17" →
  **18/18**. Line 36 (θ\* −28.4375 stands): unchanged.
- E3's tally, if quoted anywhere: 151 recorded, 150 identical, 1 changed (14/14 → 18/18), 4 inserted.

### 5.C Retained θ-fixed controls: each needs its justification stated in prose

| control | where | justification to state |
|---|---|---|
| θ_u = 0, the tempered control | Parts C/D, Text cell 6 decomposition, Eq. (23) | separates the tempering from the utility level (stated already). Also the model's start (A2); keep it apart from q_lit (F13) |
| θ-sweep {0, +1, −1, θ\*} | `theta_u_dependence` | shows which quantities depend on θ_u and on its sign; the learned column is the model |
| Hessian over θ ∈ {−50, −1, 0, 1, 50, θ\*} | Part A | §8.1(ii) claims every θ_u |
| θ_u = 1 tables (six settings, scale, sign sweep, plane invariance) | Text cell 5 Part B, Code Cell 3 | isolate μ_u's direct path; the invariance holds at any fixed θ_u. θ_u = 1 is **not** the start any more (it is 0), so that cannot be the reason |
| (θ, μ) symmetry at θ ∈ {0.7, 1, 4} | Text cell 5 §6 | an identity in θ |
| override columns θ ∈ {0, ±1, 3, 10, 100, 1e4}; μ_u check at θ_u = 1 | Text cell 6 | separate amplification (θ²) from regression toward μ_u; the learned column is the model |
| Eq. (24) limit and "every θ ≠ 0" | Text cell 4 Part C | the mechanism, as a function of θ |
| (C3) over θ ∈ {0, 1, −1, 5} (θ\* now added) | Appendix C §6 | an identity in θ |
| θ_u = 1 values in Appendix C §6 and D §1, if kept | Appendices C, D | only if the prose wants the comparison; otherwise replace (5.B) |
| relay spectrum at τ_ε = 0.1 | Appendix E, E2's fourth check | shows where the old requirement came from; τ_ε = 0.1 violates D4 |

### 5.D Unaffected
- Text cells 1–2 and the pseudocode cell.
- Text cell 3 §§1–6, §§8.1–8.2, §8.4, §8.6 and §9, apart from A1–A3.
- Text cell 4: the *Reporting statistics* note, the Part D push-forward paragraphs, and the
  q_lit/tempered masses.
- Appendix A apart from line 67.
- Appendix B's reduced objective, exposure table and *Alternative Spaces* argument.
- Appendix C §§1–5 in substance (F25 aside).
- Appendix D §§2–3.
- Code Cell 3 Part A and its prose (Text cell 5 Part A).

---

## 6. Reference values from the audit (acceptance targets for T7.4)

The θ_u = 1 column is the stored output, reproduced exactly by the audit harness. The learned column
is each configuration's own θ\*, closed form.

**Realizability, T8 (2026-09-12, printed by the executed notebook)**
- Threshold: delta-like θ_crit = 2.126, λ_max(H) = 6.5, separation 26, one Eq. (20) update; no
  threshold under the other four Part D priors.
- Plane, the 33 both-condition cells: |θ_crit| 0.100 to 4.250, λ_max(H) 2.0 to 20.1, all 33
  integrable, at most 2 updates, conjunction holds to θ\* in all 33.
- End-to-end run: θ_u 0 → 13.374852 (closed-form-equilibrated agreement 6.8e-14), 42,551 steps,
  1.95 s, 46 µs/step, λ_max(H) = 180.9, τ_ε ≤ 1.38e-3, Δ_some = −0.5182, q_H = 0.4386, gap to
  Eqs. (15)-(16) 9.5e-11; the same inference at θ\* = 1407.8 is 4.66e8 steps, 5.9 h, separation 7.9e6.
- Execution after T8: errors 0, figures 6, 250 s, checks 14/14.

**Numbers the prose pass added to the cells (T10, 2026-09-12), so no text cell quotes an
unprinted value**
- Code Cell 2, Part D: the *some* shift split into tempering and utility per prior (+0.0175/−0.0167,
  +0.0854/−0.0559, +0.0065/−0.0061, +0.0988/−0.0568, −0.0586/−0.4631); the right-edge spike table
  (q_lit 0.50/0.2639/0.0026 and 0.75/0.3188/0.0074; full 0.67/0.2767/0.0013 and 0.84/0.3285/0.0023);
  ℓ₀-invariance of the φ_S contrasts across the five priors at a common Λ = 8, **3.6e-14 at a shared
  θ_u = 1 against 0.0575 at each prior's own θ\***; and the elicited prior at Λ = 512
  (θ\* = +1580.81, shift +0.0071 against +0.0008 at Λ = 8).
- Code Cell 4: `mu_u_sensitivity` at (1, 8) and (16, 128), control against learned; the override
  diagonal (32,128) +0.8348, (64,256) +0.9996, (128,512)/(256,1024)/(512,2048) +1.0000; and the grid
  ceiling at Λ = 8 (D = 0.0057 / 0.0012 / 0.0003 and max E[s] = 0.9791 / 0.9799 / 0.9803 at
  α = 64 / 256 / 1024).
- Still script-sourced, by the T5.1 decision rather than an oversight: Appendix C §6's m = 1 values
  and Appendix D §1's residual norms (§7.1's `appendix_numbers.py`), and Appendix B's ⟨μ_u, Σc_y⟩
  = −40.9119, which Appendix B tabulates itself.

**θ\* by configuration**
- Gaussian −28.4375; flat +5950.6256; Beta(1,3) −14.5079; Beta(3,1) +55.0081; delta +1407.7691.
- Λ sweep (Gaussian, Λ = 1…64): −18.730, −19.192, −20.897, −28.437, −76.638, +1535.417, +342.254.
- μ_u settings [0,1], [1,0], [1,1], [1,2], [2,1]: −23.402, +127.94, −28.437, −12.721, −35.993.
- K ladder 51…801: −28.2355, −28.4375, −28.3287, −28.3812, −28.4075.
- Smooth mask 0.1 / 0.5 / 1 / 2: −28.385, −27.593, −25.99, −23.764.
- m = 1 (odd basis): +26.774. Gaussian at Λ = 512: +1580.814.
- Plane: −557.67 to +12228.42; negative only at (1, 2), (1, 4), (2, 2).

**Code Cell 2 at the Gaussian θ\***
- Demonstration E[s]: 0.2715 / 0.5684 / 0.7262. Leak: 0.6220 / 0.0000 / 0.6260.
  φ_u: [+0.322, +0.453], [−0.317, +0.857], [−0.317, +0.453].
- Λ sweep max leak (Λ = 1…64): 0.996621, 0.992925, 0.969597, 0.625972, 0.004976, 0.000000,
  0.000000 (5.03e-20). Still monotone.
- Implicature shifts: +0.0003 / +0.0008 / −0.4557. P(all) full: 0.0006 / 0.0025 / 0.3740.

**Part D (Δ_no, Δ_some, Δ_all; q_H(all | some); max leak)**

| prior | Δ_no | Δ_some | Δ_all | q_H(all \| some) | max leak |
|---|---|---|---|---|---|
| Gaussian | +0.0003 | +0.0008 | −0.4557 | 0.0025 | 0.63 |
| flat | +0.0004 | +0.0295 | −0.0160 | 0.0799 | 0.023 |
| Beta(1,3) | +0.0000 | +0.0004 | −0.1849 | 0.0005 | 0.91 |
| Beta(3,1) | +0.0547 | +0.0421 | −0.0087 | 0.1788 | 0.91 |
| delta | +0.0000 | −0.5217 | +0.0000 | 0.4351 | 1.1e-74 |

- E[s] by prior (no / some / all): Gaussian 0.271 / 0.568 / 0.726; flat 0.024 / 0.645 / 0.976;
  Beta(1,3) 0.019 / 0.361 / 0.334; Beta(3,1) 0.665 / 0.808 / 0.982; delta 0.003 / 0.946 / 0.998.
- Utility part: −0.0167, −0.0559, −0.0061, −0.0568, −0.4631. Tempering: +0.0175, +0.0854, +0.0065,
  +0.0988, −0.0586.
- Spike, full network under *some*: flat mode s = 0.67, density 0.2767, top node 0.0013;
  Beta(3,1) mode s = 0.84, density 0.3285, top node 0.0023.
- φ_S contrast deviation across the five priors at Λ = 8: 0.026.

**Plane (121 cells), learned**

| statistic | value |
|---|---|
| differential < 0 / < −1e-3 / < −1e-2 | 97 / 72 / 62 |
| differential min / max | −1.2470 at (64, 256) / +0.0656 at (1, 64) |
| Δ_some < 0; min Δ_some | 77; −0.9466 |
| positive differential cells | 18: α ≤ 4 plus saturated (1024, 128) |
| Δ_some > 0 cells | 37, up to α = 64 |
| \|differential\| < 1e-3 (of which Λ ≤ α) | 32 (30) |
| tempering larger than utility | 59 |
| sign(Δ_some) ≠ sign(utility) | 63 |
| tempering some−no difference, median / max | 0.0007 / 0.0988 |
| utility some−no difference, median / max | 0.0405 / 1.1884 |
| differential agrees with utility | 99 |
| max \|Δ_no\| | 1.0000 (override cells) |
| second condition / both | 59 / 33 |
| band | (1, 512)–(128, 2048) |
| delta row at Λ = 512 / 1024 / 2048 (q_H ; shift) | 0.4351 ; −0.5217 / 0.1352 ; −0.8217 / 0.0102 ; −0.9466 |

- First-condition floor, α = 1…128: 512, 256, 128, 64, 32, 32, 16, 2.
- Second-condition floor: 2, 2, 2, 2, 64, 256, 512, 1024.
- Smallest Λ holding *no*: unchanged up to α = 16; 256, 512, 1024, 2048 for α = 32…256; none at
  α ≥ 512.
- Override slopes at α = 1024: 1.9890, 2.9334, 4.3102.
- μ_u sensitivity: at (1, 8), E[s] 0.6449–0.6459 and Δ_some +0.0295…+0.0305; at (16, 128), Δ_some
  −0.2003…−0.2034 with no sign change.

**Code Cell 3 / Text cell 5 at learned θ\***
- Eq. (33) coefficient: −0.03508.
- Held at θ\* = −28.4375: contrast deviation 3.6e-15; E[s] *no* 0.2703–0.2726; Δ_some +0.0008
  throughout; Δ_all −0.4535…−0.4578.
- Re-learned per μ_u: contrast deviation 3.2e-2; Δ_all −0.4514…−0.4641.

**Appendices**
- Appendix C §6 (m = 1): Δ some/all vs q_lit +0.0604 / −0.0473; vs control +0.0429 / +0.2715;
  \|ΔE[s]\| some−all 0.2534.
- Appendix D ‖r_S‖: under E 22.47, 15.76, 22.47; under T 8.88, 3.18, 8.88.
- Appendix E relay, τ_r ≲ θ\*⁻² at τ_ε = 0.1 (superseded by T6.4): Gaussian 1.2e-3,
  Beta(1,3) 4.8e-3, Beta(3,1) 3.3e-4, delta 5.1e-7, flat 2.8e-8.

**Part A at the Gaussian θ\*, τ_ε = 0.1 (superseded by T1.3/T2.3)**
- 12/13, with the Sec. 8.2 check failing.
- Contraction per step 0.99930.
- Tails |401−801|: 1.7e-3 (hard), 3.3e-6 (smooth); coarse spread 1.1e-2.
- Gradient check error 7.3e-8. Runtime 158 s.

---

## 7. Recorded scripts

### 7.1 `appendix_numbers.py` (T5.1)

```python
"""Numbers Appendix C Sec. 6 and Appendix D Sec. 1 quote, which no notebook cell prints (T5.1).

Reads Code Cell 1 from main.ipynb, so it measures the notebook's own class. Each quantity is
given at the theta_u = 1 control (the value the appendices were written at) and at the learned
theta_u* of the configuration in question.
Run:  .venv/bin/python appendix_numbers.py   (from the project folder)
"""
import json, math, torch
nb = json.load(open("main.ipynb"))
exec("".join(nb["cells"][5]["source"]))
Net = LexicalPredictiveCodingNetwork


def p_all(net, phi):
    return float((net.weights * net.read_out(phi) * (net.zeta > net.theta_L)).sum())


def e_s(net, phi):
    return float((net.weights * net.read_out(phi) * logistic(net.zeta)).sum())


print("APPENDIX C SEC. 6: the odd m = 1 basis (b = zeta)")
kappa = {y: float(Net(basis_degree=1).project(Net(basis_degree=1).lexical_field(y))[0])
         for y in UTTERANCES}
print(f"  kappa: " + ", ".join(f"{y} {v:+.5f}" for y, v in kappa.items()))
for label, theta in (("theta_u = 1 control", 1.0), ("learned", "learned")):
    n = Net(basis_degree=1, theta_u=theta)
    fix = {y: n.closed_form_fixed_point(y) for y in UTTERANCES}
    print(f"  {label}: theta_u = {n.theta_u:.4f}")
    for a, b in (("some", "all"), ("no", "all")):
        du = float((fix[a][1] - fix[b][1]).abs().max())
        ds = float((fix[a][0] - fix[b][0]).abs().max())
        de = abs(e_s(n, fix[a][0]) - e_s(n, fix[b][0]))
        print(f"    {a} vs {b}: |d phi_u*| {du:.1e}  |d phi_S*| {ds:.4f}  |d E[s]| {de:.4f}")
    lit = {y: p_all(n, n.literal_fixed_point(y)) for y in UTTERANCES}
    temp = {y: p_all(n, n.closed_form_fixed_point(y, theta_u=0.0)[0]) for y in UTTERANCES}
    full = {y: p_all(n, fix[y][0]) for y in UTTERANCES}
    print(f"    Delta (vs q_lit): some {full['some'] - lit['some']:+.4f}, all {full['all'] - lit['all']:+.4f};"
          f"  vs the tempered control: some {full['some'] - temp['some']:+.4f}, all {full['all'] - temp['all']:+.4f}")
thetas = (0.0, 1.0, -1.0, 5.0)
for m in (1, 2):
    n = Net(basis_degree=m)
    thetas_m = thetas + (n.theta_u,)
    cs = [n.closed_form_fixed_point("all", theta_u=t)[0] - n.closed_form_fixed_point("some", theta_u=t)[0]
          for t in thetas_m]
    spread = max(float((c - cs[0]).abs().max()) for c in cs[1:])
    print(f"  (C3) m = {m}: max change of phi_S*(all) - phi_S*(some) over theta_u in "
          f"{{0, 1, -1, 5, theta* = {n.theta_u:.3f}}}: {spread:.3e}"
          f"   (over {{0, 1, -1, 5}} only: "
          f"{max(float((c - cs[0]).abs().max()) for c in cs[1:4]):.3e})")

print()
print("APPENDIX D SEC. 1: ||r_S|| at the fixed point under E and under T")
print("  (T = E + sigma_S Lambda / (sigma_L + sigma_S) * 1 by Eq. D3; g_S is common to both)")
for label, theta in (("theta_u = 1 control", 1.0), ("learned", "learned")):
    n = Net(theta_u=theta)
    shift = n.sigma_state * n.lexical_strength / (n.sigma_lexical + n.sigma_state)
    rows = []
    for y in UTTERANCES:
        phi_S, phi_u = n.closed_form_fixed_point(y)
        r_S = phi_S - n.predict_state(phi_u)
        rows.append((float(n.squared_norm(r_S)) ** 0.5, float(n.squared_norm(r_S + shift)) ** 0.5))
    print(f"  {label} (theta_u = {n.theta_u:.4f}): E " + ", ".join(f"{a:.2f}" for a, _ in rows)
          + "   T " + ", ".join(f"{b:.2f}" for _, b in rows))
```
