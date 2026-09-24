# history.md

The closed working records of this project, in one file, ordered by when each was opened.

**What this is.** While a change was in progress it had a working record in
`procedure_records/`, on the pattern `agent/agent.md` §5.3 describes: the user's instruction
verbatim, the decisions it rested on, a numbered task list, the verification, and numbered
findings. All sixteen closed. They are consolidated here on 2026-09-23 and the directory is
removed. Records opened since are written in `agent/` and folded in here as they close (§§17–18
on 2026-09-24).

**What was kept, and what was not.** Each record keeps its **findings** and task outcomes,
because those carry numbered IDs that `agent/decisions.md` and `thesis_outline/revisions.md` cite
as evidence, and those citations now resolve here. Dropped: drafts, superseded prose,
repeated output dumps and the long narration of steps that landed. **Nothing is lost**: each
section ends with the command that prints its full original out of git.

**Times are git commit times**, which is what the project has: *opened* is the commit that
added the file, *closed* the last commit that touched it. Where a record states its own
opening date in the user's words it is quoted under **Opened by**, and the two can differ by
a few hours, the record being written after the instruction.

Decisions are `agent/decisions.md` entries. `agent/agent.md` §5.3 is the standard the records were
written to, and it still governs any new one.

---

## The ledger

| # | Record | Opened | Closed | Commits | Settled |
|---|---|---|---|---:|---|
| 1 | [O5 and O6: the sign sentence and the relay bound](#r1) | 2026-09-13 15:05 | 2026-09-13 15:05 | 3 | O5, O6 |
| 2 | [E4 and E7: the default base prior, and every quoted number printed](#r2) | 2026-09-13 15:14 | 2026-09-13 15:15 | 2 | E4, E7; I10 |
| 3 | [Reach of "θ_u learned in every evaluation"](#r3) | 2026-09-13 15:14 | 2026-09-21 21:27 | 2 | A9, B4, C8, I8 |
| 4 | [D9: q as a comparison read-out, and the delta read-out reported](#r4) | 2026-09-13 16:59 | 2026-09-13 19:44 | 3 | D9 (resolved), A16, B7 |
| 5 | [O7: renaming senses 1 and 3 of "realizability"](#r5) | 2026-09-13 22:15 | 2026-09-13 22:15 | 1 | O7 |
| 6 | [Printing the delta read-out's criteria, and why its mode moves](#r6) | 2026-09-13 23:02 | 2026-09-15 21:13 | 16 | B8, B9, B10; I12 |
| 7 | [Part D at a strong Λ, and the new cell after Code Cell 2](#r7) | 2026-09-14 13:51 | 2026-09-14 20:05 | 5 | B3, B8, B9, I11 |
| 8 | [B10: reporting the conditions without taking a position](#r8) | 2026-09-14 20:05 | 2026-09-14 20:05 | 1 | B10, C7 |
| 9 | [Side quests: the mirrored inventory, and the number of atoms](#r9) | 2026-09-15 21:53 | 2026-09-22 13:35 | 4 | O9 (settled), O10 (settled), O1 |
| 10 | [exclusion_indicator: χ_some as the complement of χ_no](#r10) | 2026-09-16 08:23 | 2026-09-17 11:43 | 3 | I13 |
| 11 | [Eq. (27)'s all-region becomes closed](#r11) | 2026-09-17 11:43 | 2026-09-17 11:56 | 2 | O11 (settled), O12 (opened) |
| 12 | [The scale-class hypothesis, against Xiang et al. (2022)](#r12) | 2026-09-17 13:06 | 2026-09-22 16:16 | 16 | A20, E16, O13, O14; revisions.md T0-T13 |
| 13 | [Λ against ℓ₀: the counterforce, and where ℓ₀ enters](#r13) | 2026-09-17 20:19 | 2026-09-21 13:13 | 29 | A3, E9, E15; revisions.md U0-U14 |
| 14 | [One name for the scale's resolution, and what fixes it](#r14) | 2026-09-21 13:25 | 2026-09-22 14:36 | 5 | O1 |
| 15 | [The exposure ensemble, stated as a stipulation: its weights and its membership](#r15) | 2026-09-21 13:38 | 2026-09-22 11:26 | 4 | O2 (settled), A18, O8's ensemble half |
| 16 | [Halting by tolerance: can the realizable maximizer be defined that way?](#r16) | 2026-09-21 15:45 | 2026-09-22 12:18 | 25 | A19 (demoted to a direction), D12, I3 |
| 17 | [The node count K: printing what was found, and what it implies](#r17) | 2026-09-24 12:25 | 2026-09-24 | 4 | I6, I10, E19; revisions.md §15 |
| 18 | [The outline's organization, and what belongs in the notebook](#r18) | 2026-09-24 14:19 | 2026-09-24 | 5 | OR-D1, OR9; revisions.md §16 |

---

<a id="r1" name="r1"></a>

## 1. O5 and O6: the sign sentence and the relay bound

*Was* `procedure_records/o5_o6_resolution.md`

**Opened** 2026-09-13 15:05 · **Closed** 2026-09-13 15:05 · 3 commits

**Settled** O5, O6

**Opened by**

> O5: choose "both signs reversed, +28.4375";
> O6: Keep ≤ and state the exception for now. State in prose what it requires to Make the bound
> strict (τr < τε) as in option 2. Add comment at the 'infer' code concisely explaining how this is
> different from the text definitions and why.

#### 1. Decisions

- **O5 (user).** Appendix B's counterfactual is both signs reversed, c_y → −c_y, whose maximizer is
  +28.4375 (Code Cell B prints it). The sign of θ_u\* is then read against the relative sign of ℓ₀
  and φ_L.
- **O6 (user).** Eq. (E6) keeps τ_r ≤ τ_ε. The prose states the exception (at equality F is monotone
  under *some* only) and what a strict bound would require. `infer`'s strict guard stays, with a
  comment saying how it differs from Eq. (E6) and why.

#### 2. Tasks

Record format: `[x] Tn (date): what changed; acceptance result; commit`.

- [x] T0 (2026-09-13): checkpoint. The notebooks and `agent/decisions.md` are unchanged since b1236f2. The
  uncommitted move of the change records into `procedure_records/` is the user's and is not folded
  into this change.
- [x] T1 (2026-09-13): code. Code Cell E1, `infer`: a comment at the `tau_relay >= tau_error`
  guard; the guard's error message reads "as slow as" in place of "slower than", since equality is
  refused. Acceptance: the cell parses; no stored output can change (a comment, and a message no
  run raises). Notebooks not re-executed.
- [x] T2 (2026-09-13): prose, applied by a script requiring each edit to land exactly once.
  Acceptance: every edit landed once; both notebooks load as JSON (strict validation already fails
  at b1236f2, F4).
- [x] T3 (2026-09-13): `agent/decisions.md`: O5 and O6 settled by the user; a dated finding under A11; commit 235cb59 (T1-T3).

#### 3. Findings

- **F1 (continuity of the strict bound).** τ_r < τ_ε excludes only the equality: `infer` still
  admits a relay arbitrarily close to τ_ε, and no relay strictly between the instantaneous one and
  τ_ε has been integrated under *no* or *all*. A strict bound carries monotonicity only with a
  measured margin, which is what the new E.1 paragraph states.
- **F2.** E.1 quoted the relay bound at θ_u\* as τ_r < 3.08e-4, stricter than Eq. (E6). Now ≤.
- **F3 (noticed, not changed).** Code Cell E1's `infer` docstring still quotes the roundoff floor as
  "about 8e-11 to 1.6e-10"; the prose was corrected to 8.2e-11 to 2.4e-10 under E7 (F7 of
  `e4_e7_sourcing.md`). Code comments were outside E7's scope.
- **F4 (noticed, not changed).** Both notebooks fail `nbformat.validate` at b1236f2 already: cells
  carry `id` fields while the files declare `nbformat_minor` 0. Jupyter and nbclient run them; T2's
  acceptance was therefore that each edit landed once and the JSON loads, not strict validation.

#### 4. Prose sites

- `main.ipynb` cell 14 (Appendix B): "were the two signs reversed … +22.578" → "were both signs
  reversed … +28.437".
- `appendix_E.ipynb` cell 1 (E.1): the bound at θ_u\* written with ≤; a paragraph after the
  slow-relay counts stating the exception and what a strict bound requires.
- `appendix_E.ipynb` cell 6 (E.2): "suffices at every θ_u tested" narrowed to stability, and the
  non-monotone transient extended to a relay at the error units' own speed under *no* and *all*.
- `appendix_E.ipynb` cell 7 (E.3, the Text cell 3 §7 row): the same narrowing.

*Full original:* `git show eb20c4f:procedure_records/o5_o6_resolution.md`

---

<a id="r2" name="r2"></a>

## 2. E4 and E7: the default base prior, and every quoted number printed

*Was* `procedure_records/e4_e7_sourcing.md`

**Opened** 2026-09-13 15:14 · **Closed** 2026-09-13 15:15 · 2 commits

**Settled** E4, E7; I10

**Opened by**

> E4: the Gaussian base-world-prior is one of the several base-world-priors we tested our model on.
> It is indeed not elicited from any experiments. ell_0 can be supplied by an elicited distribution
> but it doesn't have to be. When an elicited distribution is not supplied, the default is N(0,1).
> It may be helpful to clarify the the reason that we chose N(0,1) as default : the pc framework as
> in Bogacz operates on the fundamental assumption that a system represents states with gaussian;
> now although ell_0 is not a state unit and does not have to be gaussian by construction, it makes
> more sense that it is defaulted to gaussian given the framework's assumption.
>
> E7: all unsourced numbers must be computed by an explicit script and printed in some code cell.

#### 3. Findings

- **F1 (Text cell 4 Part C).** "at most −0.0664 as θ_u → 0" is not what the closed form gives.
  Under the delta-like prior the shift for *some* tends to the tempering, −0.0586, as θ_u → 0;
  −0.0664 is its value at θ_u = +0.1. Over the θ_u swept (±1e-8 to ±1e7) the least negative value
  is −0.0585 (θ_u = 0.01) and the most negative −0.5219 (θ_u = −100), which overshoots the limit
  −0.5217: the approach to the limit is not monotone on the negative side. Every swept value is
  negative.
- **F2 (Appendix B, sign).** "were the two signs reversed the maximizer would be +22.578". Reversing
  both signs gives +28.4375, by the exact symmetry. +22.578 is the maximizer with ℓ₀'s sign reversed
  alone; reversing φ_L's sign alone (c from ℓ₀ + φ_L) gives −22.578. The sentence carries the sign
  argument, so its rewording is **the user's**.
- **F3 (Appendix B, batching).** Reproduced in closed form, the batched and per-presentation flows
  differ by 1.5e-3 where the batched flow passes −16.73 and by 6.8e-5 where it passes −24.83 (prose:
  4e-3 and 1.6e-4). At a constant step the per-presentation flow does not close on θ\*: it stays
  about 3e-4 away after 400,000 cycles. "reaches the same fixed point" holds to that.
- **F4 (Appendix C §§3, 7).** The quoted unseen direction [0.512, −0.485, 1.000, 0.043] lies in the
  two-dimensional unseen subspace but is one arbitrary representative of it. The representative
  orthogonal to the constant is [−0.325, 1.000, −0.974, 0.298]. §7's claim is better stated as a
  count: the non-constant {−1, 0, 1} combinations of intervals that B cannot see.
- **F5 (Appendix C §5).** The even-column entry is 1.44196, not 1.44190.
- **F6 (roundoff-level values).** θ_L AWX = I₃ to 3.3e-15 (prose 2.4e-15); dF̃/dθ_u at θ\* 3.3e-16
  (5.5e-16); φ_u\* rebuilt from c_y 0.0 (2.2e-16). Appendix D's agreements depend on the solver; by
  Newton's method φ_u\* agrees to 1.8e-15 (5.3e-15) and the read-out to 8.7e-14 (4.4e-16).
- **F7 (Text cell 4, roundoff floor).** Over 2000 steps past convergence at θ_u = 13.3749 the
  largest derivative runs 8.2e-11 to 2.4e-10 (prose: 8e-11 to 1.6e-10). The 1e-9 tolerance is still
  above it.
- **F8 (Appendix E.1, slow relay).** The quoted counts (none at τ_r = τ_ε, six at 2τ_ε,
  fifty-eight at 10τ_ε, worst −8.35) are *some*'s. Under *no* and *all*, 3 steps of F fall at
  τ_r = τ_ε (worst −2.9e-2), 9 at 2τ_ε and 65 at 10τ_ε. This bears on Eq. (E6)'s τ_r ≤ τ_ε as the
  bound for a monotone F; `infer` already requires τ_r < τ_ε strictly. **The user's.**
- **F11 (the audit tool).** `audit_numbers.py` chose which cells to skip by index, so after the
  renumbering it skipped Appendix C and audited the reference lists. It now skips by content.
- **F10 (my error, caught by the T4 gate).** The first version of the roundoff-floor block read the
  2000 steps immediately after convergence, which are still the tail of the decay: it printed
  2.4e-10 to 9.9e-10, the upper end being the derivative at the converged step. The prose gate
  refused to quote it. The block now integrates 4000 steps past convergence and reads the last 2000,
  which is what T1 measured (8.2e-11 to 2.4e-10); both notebooks re-executed.
- **F9 (Appendix E.1, bounds).** The four bounds quoted for "the other priors of Part D" are
  unlabelled and not in Part D's order: Beta(1,3) 1.18e-3, Beta(3,1) 8.26e-5, delta-like 1.26e-7,
  flat 7.06e-9.


- **DEC1 (user).** The Gaussian N(0,1) in ζ is the *default* base world prior, one of several the
  model is tested on, and not elicited. ℓ₀ may be supplied by an elicited distribution. Reason for a
  Gaussian default: the framework (Bogacz) represents states with Gaussians; ℓ₀ is not a state unit
  and need not be Gaussian, but a Gaussian default is the choice consistent with that assumption.
  The reason for the parameter values (mean 0, precision 1) is not recorded.

- **DEC2 (user).** Every number the prose quotes is computed by an explicit script and printed in a
  code cell. This replaces the earlier allowance for a script recorded only in a change record
  (I8).

- **DEC3 (agent, confirmed by user 2026-09-13).** Placement: numbers quoted in Text cells 4 and 5 are
  printed by Code Cells 2 and 3; each of Appendices A–D gets its own code cell directly after it
  (Code Cells A–D); numbers quoted in Appendix E.1 are printed by a new Code Cell E4.

*Full original:* `git show e03268a:procedure_records/e4_e7_sourcing.md`

---

<a id="r3" name="r3"></a>

## 3. Reach of "θ_u learned in every evaluation"

*Was* `procedure_records/theta_u_learned_reach.md`

**Opened** 2026-09-13 15:14 · **Closed** 2026-09-21 21:27 · 2 commits

**Settled** A9, B4, C8, I8

**Opened by**

> **Status 2026-09-13: code and prose both done.** T0–T11 are closed. main.ipynb executes clean
> (0 errors, 6 figures, 223 s, 14/14 checks) and appendix_E.ipynb likewise (0 errors, 3 figures,
> 562 s, E2 18/18, E3 PASS). T11 moved `infer`'s stopping tolerance from 1e-10 to 1e-9, off the
> roundoff floor F34 identified: step counts are now reproducible, an inference costs about 9% fewer
> steps, and the settled state is accurate to about 1e-9. The markdown cells of both notebooks have been rewritten against the
> executed outputs. What is deliberately left open is listed in §4 as F27's residue (Appendix C and D
> numbers come from §7.1's recorded script, by the T5.1 decision) and A11's outline pointer, which
> stays bare until the background outline is finalized.
> Backup before you start the change. First work through codes procedurally and record everything
> done as closed task on the reach.md. Record any unexpected findings/issues as well. After you are
> …

##### T0. Backup
- [x] T0.1 Copy `main.ipynb` and `appendix_E.ipynb` to `backups/2026-09-11/` in the project folder.
  Record byte sizes and sha256 of the originals and the copies. Acceptance: hashes equal.
  **Closed 2026-09-11:** backups/2026-09-11/ holds main.ipynb (755341 B, sha256 126995e8…ace0b) and appendix_E.ipynb (370242 B, sha256 7e0252af…25e0b1); copies hash-equal to originals. The project folder's older reach.md draft (16644 B, 09:15) was kept there as theta_u_learned_reach.earlier_draft.md and replaced by this finalized file, which is the working record from here on.


##### T1. Code cell 1 (architecture), mirrored into Code Cell E1 at T6.1
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


##### T2. Code Cell 2 (evaluation), mirrored into Code Cell E2 at T6.2
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


##### T3. Code Cell 3 (probes)
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


##### T4. Code Cell 4 (Λ×α sweep)
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


##### T5. Numbers quoted by appendices that no cell prints
- [x] T5.1 Appendix C §6 (m = 1, odd basis) and Appendix D (‖r_S‖ under E and T). Recompute at
  learned θ\*, and decide whether to add a printing cell or record the script. Values are in §6.
  **Closed 2026-09-11:** **Decision: record the script, do not add a cell to main** (a new code cell would change main's cell structure and numbering, which nobody asked for). The script is `appendix_numbers.py`; it reads Code Cell 1 from main.ipynb and is reproduced in §7 of this file. Output, learned against the θ_u = 1 control. **Appendix C §6** (m = 1, θ* = +26.7740): some vs all |dφ_u*| 0, |dφ_S*| 4.0000 (θ-independent, C3), |dE[s]| 0.2534 (0.2525); no vs all |dφ_u*| 0.68 (6.08), |dφ_S*| 8.5464 (5.5197), |dE[s]| 0.7818 (0.6018); Δ vs q_lit some +0.0604, all −0.0473 (+0.0300, −0.1912); vs the tempered control +0.0429, +0.2715 (+0.0125, +0.1276). (C3) at m = 1 holds to 8.9e-16 with θ* added to the list; the m = 2 comparison figure grows from 3.445 to 3.712 when θ* is included. **Appendix D §1** ‖r_S‖: E 22.47, 15.76, 22.47 and T 8.88, 3.18, 8.88 (23.19, 18.08, 23.10 and 10.56, 9.43, 10.36). All match §6. The θ_u = 1 control reproduces the appendices' stored numbers except the pre-existing items in F25.


##### T6. appendix_E.ipynb (after main has been executed)
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


##### T7. Execute and verify
- [x] T7.1 Execute `main.ipynb` end to end. Record: errors 0, figure count, checks passed, runtime.
  **Do not pipe the runner to `tail`; check the runner's own success line.**
  **Closed 2026-09-11:** main.ipynb executed end to end by `runnb.py` (nbclient, kernel python3, in place). Runner's own line: **RUNNER OK, error outputs 0, figures 6, runtime 245 s.** Specification checks 14/14.
- [x] T7.2 Execute `appendix_E.ipynb`. Record the same, plus E3's tally.
  **Closed 2026-09-11:** appendix_E.ipynb executed the same way: **RUNNER OK, error outputs 0, figures 3, runtime 604 s** (E3 re-runs the whole Code Cell 2 sequence). E2 18/18; E3 tally as in T6.5, PASS.
- [x] T7.3 Scan the code and outputs for surviving "θ_u = 1" strings not intended as controls.
  **Closed 2026-09-11:** Scanned main's code and outputs for θ_u = 1, dt = 0.02, τ_ε = 0.1 and copysign. Every θ_u = 1 left is a labelled control: Code Cell 3's fixed-θ tables (headers say "theta_u fixed at 1" / "a control") and Code Cell 4's override control columns and μ_u check. No dt = 0.02 or τ_ε = 0.1 remains. The one copysign is the numerically stable root formula in `theta_u_stationary_points`, not a start rule.
- [x] T7.4 Check every new printed number against §6. Any disagreement goes to §4.
  **Closed 2026-09-11:** Checked programmatically against §6 (72 target strings): all present, with F24's roundoff-robust plane counts in place of the superseded ones. Differences from §6, all explained: (i) plane sign counts per F24; (ii) Part A "contraction per step 0.99930" is now a rate per unit time, 1.000231 (F18); (iii) the gradient-check error is 9.74e-8, not 7.3e-8, because the θ* added to the Hessian sweep shifts the seeded random stream; (iv) Appendix E relay values per F26. Tempering and utility parts per prior, the spike modes and densities in Part D, and the Text cell 6 μ_u-sensitivity numbers are still printed by no cell (F27).


##### T8. Code: the minimum learning the criterion needs, run (user, 2026-09-12)

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


##### T9. Prose: realizability (OPEN, the prose pass has not started)

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


##### T11. The stopping tolerance, 1e-10 -> 1e-9 (user, 2026-09-13)

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


##### T10. The prose pass itself (started 2026-09-12)

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


#### 4. Findings and issues log

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
  - **NOTE ADDED 2026-09-21 (H12, `agent/history.md` §16): the band below is the
    floor AT THIS theta_u, not the floor.** The floor is **4.547e-13 x lambda_max(H)**, flat to four
    significant figures from theta_u = 13.4 to 61.3, and 8.2e-11 to 1.6e-10 is what that gives at
    the lambda of this run. F34's conclusion is unaffected and in fact generalized; what it
    licensed - a single fixed tolerance above the band - is what did not survive, and I3 is revised
    accordingly.
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


##### 5.A New statements the decisions and findings require

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

- **F25 (pre-existing):** Appendix C defines κ_y = BᵀWφ_{L,y} (line 18) but tabulates it per unit Λ
  throughout (lines 38, 79–84, 131, 171: ±1.13989, ±0.72098, 0.72097). Code Cell 3 prints
  ±9.11909 = 8 × 1.13989. Either define κ on χ_y in Appendix C or scale the values. Also, the *no*
  vs *all* row (6.0790 / 5.5200) differs from the current code at θ_u = 1 (6.0794 / 5.5197).

**Appendix D**

*Full original:* `git show c137f8d:procedure_records/theta_u_learned_reach.md`

---

<a id="r4" name="r4"></a>

## 4. D9: q as a comparison read-out, and the delta read-out reported

*Was* `procedure_records/d9_delta_readout.md`

**Opened** 2026-09-13 16:59 · **Closed** 2026-09-13 19:44 · 3 commits

**Settled** D9 (resolved), A16, B7

**Opened by**

> Here is my take on D9:
>
> 1. we have constructed the read-out q mainly to find a parallel interpretation to the RSA
> literature. Nevertheless, the framework that our model is built upon is quite different from the
> foundational assumptions that standard RSA make. Hence, any inclusion of the read-out q is purely
> for comparison and conventional purpose. There is nothing in our architecture or the construction
> that dictates this form of read-out.
> 2. The posterior read-out that is more native to the construction is delta phi_s*, which
> corresponds with Bogacz's implementation. Therefore, in the evaluation section, after the q graphs
> for different priors, we should also print and report the table that you gave me above.
> …

#### 1. Decisions

- **DEC1 (user).** q (Eq. 12) is a read-out constructed for comparison with the RSA literature;
  nothing in the architecture dictates it. The posterior native to the construction is the delta at
  the settled state, Bogacz's Eq. (34).
- **DEC2 (user).** Part D reports the delta read-out table after the q figures, with a reading guide
  in Text cell 4 Part D that cites Appendix A's Voronoi cell and states the ℓ₀ peak beside the peak
  of φ_S\* under *some*.
- **DEC3 (user).** Framing sites only: Eq. (12)'s paragraph, the Reporting statistics opening, the
  q_lit naming; the Part C/D verdicts stay in q with one sentence on their status.
- **DEC4 (agent, confirmed by user 2026-09-13).** C6 requires the ℓ₀ peaks and the boundary check the
  note quotes to be printed; they print as two blocks below the table, which stays as given.
- **DEC5 (agent, confirmed by user 2026-09-13).** q_lit's "untempered literal posterior" becomes
  "untempered literal listener". The user added (verbatim): "clarify at first mention that what
  "literal" denotes here is distinct from what "literal" denotes in RSA and Gricean literature. Just
  one sentence and no further explanation is needed on how our denotation is distinct."

#### 2. Tasks

Record format: `[x] Tn (date): what changed; acceptance result; commit`.

- [x] T0 (2026-09-13): checkpoint. HEAD e03268a; the notebooks, `agent/decisions.md` and `agent/agent.md` are
  unchanged since. `thesis_outline/` is staged by the user and is not part of this change; commits
  here name their paths with `git commit --`.
- [x] T1 (2026-09-13): code. `delta_readout_report` in Code Cell 2, defined before RUN and called
  after the figures; the same text inserted into E2 (checked identical); E3 replays it as
  `delta_readout_report(probe_network, realizability_report(probe_network))`. Acceptance: run
  outside the notebook on code cell 1 and Code Cell 2's definitions, it printed the table of the
  scratch computation exactly (5.5 s).
- [x] T2 (2026-09-13): executed main, then appendix_E. main 0 errors, 6 figures, 14/14, 245 s;
  appendix_E 0 errors, 3 figures, E2 18/18, E3 PASS (260 lines identical, up from 221; 0 deleted,
  1 changed, 4 inserted), 672 s. The table printed after the figures matches T1's.
- [x] T3 (2026-09-13): prose against the outputs (§4), 10 edits in Text cells 3, 4 and 6. Acceptance:
  each landed once; the 25 decimals the guide quotes are all in main's executed Code Cell 2 output.
  Markdown only, so no stored output changes and E3 is unaffected.
- [x] T4 (2026-09-13): `agent/decisions.md`: A13 status, A16 and B7 added, dated findings under B1 and C3,
  D9 resolved and its register row. `agent/agent.md`: §2 item 7 (E3 replay), §5.1 baseline.
- [x] T5 (2026-09-13): committed T1-T4 as cb8cc6a, by explicit paths; `thesis_outline/` left staged.
- [x] T6 (2026-09-13): DEC4 and DEC5 confirmed. Text cell 3 §7, at the first mention of *literal*:
  one sentence that its denotation here is distinct from RSA's (Frank & Goodman, 2012) and the
  Gricean literature's (Grice, 1975); both works already in the references. Markdown only, not
  re-executed; committed with this line.

#### 3. Findings

- **F1 (the peak is the mode of q).** Placing the delta on the scale of s means reading its peak,
  the grid node where φ_S\* is largest. The exponential and normalizer of Eq. (12) do not move it,
  so it is also the mode of q. The delta read-out departs from q in what needs the normalizer
  (masses, E[s]), not in the peak.
- **F2 (ℓ₀ peak).** Under *some* the peak of φ_S\* lies outside the cell of *all* under all five
  priors. Under the four at Λ = 8 the ℓ₀ peak already does (s = 0.50, 0.50, 0.25, 0.75), and the
  learned peak sits above it (0.59, 0.67, 0.33, 0.84). Under the delta-like row the ℓ₀ peak is
  inside (0.985) and the learned peak outside (0.947). Under *some* φ_L vanishes at the ℓ₀ peak of
  every prior, so ℓ₀ − φ_L peaks there too.
- **F3 (boundary).** The delta-like row's peak is one node below θ_L. On grids of 201, 401 and 801
  nodes it stays outside, the gap to the best node inside shrinking (−0.114, −0.053, −0.031) and
  the peak moving toward s = 0.95.
- **F4 (own cell).** The learned peak leaves the uttered entry's own cell under *all* with
  Beta(1,3) (s = 0.25) and under *no* with Beta(3,1) (s = 0.75).
- **F5 (E3 replay).** E3 replays Code Cell 2's printing calls by name, so a new printing call in
  Code Cell 2 must be added to E3's replay or E3 reports its lines as deleted.

#### 4. Prose sites

Applied by `prose_d9.py` (scratch), which writes nothing unless every edit lands once and every
decimal the guide quotes is in main's executed Code Cell 2 output.

- Text cell 3 §4 item 5 (Eq. 12): the delta at the settled state is the construction's posterior
  (Bogacz §3, Eq. 34); q is read for comparison with the RSA literature; nothing in the architecture
  dictates Eq. (12).
- Text cell 3 §9 caveats: "read-out (10)" → "(12)" (stale number); "A parametric posterior" →
  "A parametric read-out".
- Text cell 4 Part C: q_lit "untempered literal posterior" → "untempered literal listener" (DEC5); one
  sentence after the criterion: both conditions are stated on q, the delta is reported in Part D.
- Text cell 4 Part D, after the figure discussion: the reading guide (table columns; the peak is
  also q's mode; φ_u\* comparable only at shared θ_u; the ℓ₀ peak against the cell of *all*, citing
  Appendix A; the boundary check; F4's two rows noted with position reserved).
- Text cell 4 Reporting statistics: the opening no longer says the model's output is q; "Only
  q-mass is a statement about what the model concluded" → "about the read-out q".
- Text cell 6: "the untempered literal posterior" → "untempered".

*Full original:* `git show 65e0904:procedure_records/d9_delta_readout.md`

---

<a id="r5" name="r5"></a>

## 5. O7: renaming senses 1 and 3 of "realizability"

*Was* `procedure_records/o7_renaming.md`

**Opened** 2026-09-13 22:15 · **Closed** 2026-09-13 22:15 · 1 commit

**Settled** O7

**Opened by**

> With that said, let's address O7 first. Would you propose a renaming for senses 1 and 3?
> Sense 1 renaming approved. For sense 3 maybe say "this map collapses contrasts between exclusion
> sets"? Reads easier this way.

#### 1. Decisions

- **DEC1 (agent's proposal, approved by the user, 2026-09-13).** Sense 1 (Appendix B: at θ\* both
  residuals vanish and F = 0) is renamed **exact solvability**. Appendix B's own preceding sentence
  already says θ v_p = u "is solvable". "Exact fit" was not used, because in the outline "fit" means
  fitting a model to data.
- **DEC2 (user, 2026-09-13).** Sense 3 (Appendix C §7) takes no term. It is phrased as a projection
  that "collapses a contrast between exclusion sets", which matches existing usage (Text cell 5
  Part A; Appendix C's table). The agent named the subject as "$m=2$" and "$m=1$" rather than "this
  map", following that table. "Expressible" and "representable" were avoided (agent/decisions.md O7).
- Sense 2 (the cost sense) is untouched, and O7 stays open for it.

#### 2. Tasks

- [x] T0 (2026-09-13): checkpoint. Clean tree at HEAD 07f4eae.
- [x] T1 (2026-09-13): edits to main.ipynb, applied by script. Each replacement was asserted to occur
  exactly once. Afterwards no "realiz" is left in cells 14–16, and the diff is 7 lines.
  - Appendix B (cell 14): "it is **realizability** that identifies θ" → "it is **exact
    solvability** that identifies θ"; "is not realizability but a nonzero" → "is not exact
    solvability but a nonzero".
  - Code Cell B (cell 15): header `REALIZABILITY AT theta_u*` → `EXACT SOLVABILITY AT theta_u*`.
  - Appendix C §7 (cell 16): "Yet **no exclusion set realizes it**" → "Yet **$m=2$ collapses no
    contrast between exclusion sets**". "the direction $m=1$ misses *is* realizable, being the
    middle interval … an exclusion-set difference, which is why $m=1$ actually fails" → "the
    direction $m=1$ misses is the middle interval …, a difference of two exclusion sets, so $m=1$
    *does* collapse a contrast, the one between *some* and *all*, and that is why $m=1$ actually
    fails."
- [x] T2 (2026-09-13): executed main, then appendix_E (agent/agent.md §5.1).
  - main.ipynb: RUNNER OK, 0 errors, 6 figures, 244 s.
  - appendix_E.ipynb: RUNNER OK, 0 errors, 3 figures, 684 s.
  - Stored outputs against HEAD: main cell 15 differs in the one header line only; main cell 7 and
    appendix_E cell 3 differ only in wall-clock `cost:` lines; every other output line is identical.
    Read off the new outputs: main 14/14 specification checks passed; appendix_E E2 18/18 passed,
    and E3 PASS, "the relay changes no reported quantity: 260 lines identical, 0 deleted".
- [x] T3 (2026-09-13): `agent/decisions.md` O7 finding; `thesis_outline/revisions.md` §7 note.

#### 3. Findings

- **F1.** Sense 3's new wording is exact, not a paraphrase. Every non-constant {−1,0,1} combination of
  the intervals is χ_A − χ_B for two exclusion sets A and B, and it lies in the projection's unseen
  subspace iff A and B are sent to the same point. So "no combination lies in the unseen subspace"
  and "no contrast between exclusion sets collapses" are the same statement. The trivial pair (empty
  set, whole scale) is excluded by "non-constant" and by §7's "nonempty proper unions".
- **F2.** Bogacz (2017) uses neither "realizable" nor "solvable", so no citation depends on sense 1's
  old name.

*Full original:* `git show a831711:procedure_records/o7_renaming.md`

---

<a id="r6" name="r6"></a>

## 6. Printing the delta read-out's criteria, and why its mode moves

*Was* `procedure_records/delta_criteria_printing.md`

**Opened** 2026-09-13 23:02 · **Closed** 2026-09-15 21:13 · 16 commits

**Settled** B8, B9, B10; I12

**Opened by**

> The cost sense retain the "realizability" name as is; no change needed. Now let's work on Q2.
> Here are my thoughts:
>
> 1. the delta read-out still comes with two criteria: a. whether mode(phi_s*) - mode(ell_0) is
> negative; this is shift_some. b. whether mode(phi_s*) falls outside the cell of [[all]]. Just be
> careful that even though these two criteria are meant to mirror the two criteria as already
> defined, their satisfaction may not be equivalent.
> 2. The V-shape is instereting and it definitely needs to be discussed,
> 3. I am not sure what you mean with the unstated premise and what level is it a motivation of.
> good. Your solution to Q2 is approved. No evidence for a missing level needs to be derived from
> …

#### 3. Findings

- **F1 (2026-09-13, `output.txt`). The second conditions coincide; the first do not.**
  - On Part D's five rows, B8 and B2 agree row by row.
  - On the 121 plane cells:
    - q's second condition and (b) hold in the same 59 cells;
    - q's first condition holds in 74 cells and (a) in 67, disagreeing in 35;
    - the conjunctions hold in 33 and 13 cells, with every delta conjunction a q conjunction.
- **F2 (same). The V's left arm exists only under q.**
  - Least Λ for both:
    - under q: 512, 256, 128, 64, 64, 256, 512, 1024 at α = 1 … 128;
    - under the delta: none at α ≤ 8, then 256, 256, 512, 1024.
  - The right arm is shared, at Λ = 8α for α = 32–128.
- **F3 (same). Grid facts.**
  - mode(ℓ₀) = mode(ℓ₀ − φ_L) in every cell under *some*.
  - In 4 cells the mode does not move at all.
  - The smallest gap between the two largest nodes is 5.6e-5, so there are no ties.
- **F4 (2026-09-13, `mode_mechanism_output.txt`, preliminary). Why the mode moves up under the delta
  read-out.**
  - **The split.** The utility field φ_S\* − φ_S\*(θ_u = 0) lies in span B to 1.7e-12 (Eq. 23). It
    is split into B's odd (tilt) and even (width) columns.
  - **Signs.** On all 121 plane cells the tilt coefficient is positive and the width coefficient
    negative. On Part D the same holds, except that Beta(1,3)'s tilt is negative. Width is negative
    in all 126 configurations.
  - **Mass.** The width part alone lowers the all-region q-mass in all 121 cells; the tilt part alone
    never does.
  - **Mode.**
    - Where the model's mode moves up (50 cells), the tilt part alone moves it up and the width part
      alone never does.
    - Where it moves down (67 cells), the width part alone moves it down and the tilt part alone
      never does.
    - The sign of the two parts' combined slope at the literal mode predicts the direction in all
      117 cells where the mode moves. That is the first-order argument: at a smooth peak of the
      tempered field, adding g moves the peak by about g′/curvature.
    - The mode moves up where the literal mode sits at s ≤ 0.9405, and down where it sits at
      s ≥ 0.9405.
  - **Reading.**
    - A negative width coefficient concentrates the belief toward the centre of the scale. That
      lowers both tails, the all-region among them, and pulls the peak inward. The pull is zero at
      the centre, where the even column is flat, and grows toward the ends.
    - The tilt slides the peak in its own direction.
    - Near the centre the tilt wins and the peak moves up; near the upper end the width wins and the
      peak moves down.
    - q's first condition reads the tail, which the width governs. Criterion (a) reads the peak,
      which the tilt governs near the centre.
  - **Where the signs come from.** By Eq. (24), at large |θ_u| the utility field is half the literal
    field's span-B component, so the model doubles that component.
    - Under the delta-like prior the coefficients are exactly half of Part C's c_some:
      +480.83 = 961.66/2, and −264.89 ≈ −529.77/2.
    - So the tilt carries the skew of the literal field, the prior and the entry together. Even the
      symmetric Gaussian gets a positive tilt, because *some* excludes the bottom of the scale.
    - The width is negative because every log-density tested falls off toward both ends.
  - **Part D's four diffuse rows.**
    - Gaussian and flat: the literal mode is at the centre, where the width has no pull (slope 0),
      so the tilt alone moves the peak up.
    - Beta(3,1): the tilt's push (slope +0.881) outweighs the width's inward pull (−0.453).
    - Beta(1,3): the tilt pushes down (−0.125), but the mode sits below the centre, where the
      width's inward pull is upward (+0.454) and wins.
  - **What it says about the V.**
    - For α ≤ 8 the literal mode sits at s ≤ 0.885, inside the tilt-dominated range, so no Λ moves
      the mode down and (a) never holds.
    - From α = 32 the literal mode sits at s ≥ 0.970, where the width dominates.
    - α = 16 is at the crossover (0.9405).
  - **What it says about Q6.** The delta read-out's upward movement and q's positive shift share a
    direction and not a source. q's positive shift is the tempering, which a mode cannot see. The
    delta's movement is the tilt, plus the width's inward pull below the centre.
  - **Caveats.**
    - Modes are grid nodes.
    - The direction argument is first order.
    - The Eq. (24) halving was checked exactly only on the delta-like row. **Discharged by F5.**
    - No cell prints any of it.

- **F5 (2026-09-13, `halving_check_output.txt`). Eq. (24)'s halving holds across the plane, and the
  limit field carries F4's reading in every configuration tested.**
  - **Exact form.** At σ = 1 with BᵀWB = I (checked to 2.2e-16), Eqs. (15)–(16) give the utility
    coefficients as k = (θ/2)(μ_u + (θ/2)c)/(1 + θ²/2), with c = BᵀW(ℓ₀ − φ_L). The fitted coefficients
    match that to 1.2e-15. So k − c/2 = ((θ/2)μ_u − c/2)/(1 + θ²/2), which vanishes as |θ_u\*| grows.
  - **Distance from c/2, relative.**
    - Plane: the median is 8.6e-7 for the tilt and 4.8e-6 for the width. Both columns are within
      1e-3 in 111 cells, within 1e-2 in 119, and within 1e-1 in 120.
    - The worst cell is (α, Λ) = (1, 2), at θ\* = −6.51, the smallest |θ\*| on the plane: its tilt is
      17% below half (+0.94 against +1.14). The next is (1, 4), at θ\* = −16.39, with 3.4%.
    - Part D: Gaussian tilt 1.0e-2, Beta(1,3) tilt 3.8e-2, everything else ≤ 3e-3. The delta-like
      row is at 4.7e-7 and 3.7e-6.
  - **Signs.** sign(k) = sign(c) in both columns in all 121 cells and all five Part D rows. c is
    (+, −) in every plane cell; on Part D, Beta(1,3)'s c tilt is negative (−2.88). Part C's c_some
    under the delta-like prior is reproduced: +961.66, −529.77.
  - **The limit field.** ½(ℓ₀ − φ_L) + B c/2 has the model's mode node in all 121 cells.
    Criteria (a) and (b) and q's two conditions read the same off it as off the model, in all 121
    cells and in Part D's five rows. The q-masses differ slightly (flat 0.0798 against 0.0799;
    Beta(3,1) 0.1775 against 0.1788) without changing a verdict.
  - **Consequence.** F4's reading holds already at the smallest |θ_u\*| on the plane. In every
    configuration tested, the verdicts of both read-outs are those of the model doubling the literal
    field's own tilt and width. F4's caveat on the halving is discharged. Its other two caveats, grid
    modes and the first-order argument, stand.


#### 6. T6 prose: approved by the user 2026-09-15 and applied (af971c4)

Written 2026-09-15 against the executed outputs of 5ee04a6. Every number is printed by Code Cell 2's
or 2b's criteria block, Code Cell 4's new block, or Code Cell C. What the C7 pass (98c2df8) already
covers is kept; the edits below fill what T6 asks for. No heading is added, so the ToC does not change.

**E1. Text cell 4, Part C, "The criteria" paragraph: one clause (T6 item 3).** The sentence ending
"with a mode shift and a mode position criterion of its own." becomes:

> …with a mode shift and a mode position criterion of its own. The two pairs are not assumed to
> agree, and they do not always: over the plane of Text cell 6 the two position criteria agree in all
> $121$ cells and the two shift criteria disagree in $35$.

**E2. Text cell 4, Part D, "The delta read-out's two criteria": definitions as unnumbered displays,
the new columns, and the Λ = 8 result (T6 item 1).** The paragraph becomes:

> **The delta read-out's two criteria.** Under *some*, Code Cell 2 also prints two criteria on the
> peak of $\varphi_S^\ast$, which it calls the mode. Writing $k^\ast$ for the grid node where
> $\varphi_S^\ast$ is largest and $k_0$ for the node where $\ell_0$ is, the **mode shift criterion**
> is
>
> $$k^\ast<k_0,$$
>
> met when the mode lies below the $\ell_0$ peak on the scale, and the **mode position criterion** is
>
> $$\zeta_{k^\ast}<\theta_L,$$
>
> met when the mode lies outside the cell of *all*. Both are statistics of the delta read-out, as the
> q criteria are of $q$, and neither is a model quantity. Being comparisons of grid nodes, they resolve
> a movement of the mode to one node; a tie would go to the first node, and the cell prints the gap
> between the two largest values of $\varphi_S^\ast$, which is never zero in these rows. The cell
> prints the mode shift in $s$ and in grid steps, $k^\ast-k_0$. The grid is uniform in $\zeta$ while
> $s$ compresses toward the ends of the scale, so the steps, multiplied by the grid spacing of
> $0.12$, give the shift in $\zeta$. The mode criteria are the counterparts on the delta read-out of
> the q shift and q position criteria and are not assumed to agree with them, so the cell prints the
> four side by side, with how often each pair agrees. As with the q criteria, this notebook takes no
> position on how they should be interpreted. At $\Lambda=8$ the mode lies $3$, $6$, $3$ and $5$
> grid steps above the $\ell_0$ peak under the Gaussian, flat, $\mathrm{Beta}(1,3)$ and
> $\mathrm{Beta}(3,1)$ priors, so the mode shift criterion is met under none and the mode position
> criterion under all four, and each agrees with its q counterpart in all four rows.

**E3. Text cell 4, Part D, the spike paragraph: a correction (R15).** The sentence "The movement of
the mode up the scale between the two is what the positive $\Delta_{\textit{some}}$ records." no
longer holds: by the paragraph above it, the positive shift is tempering, and halving a field does not
move its maximum. Proposed replacement:

> The movement of the mode up the scale between $q_{\mathrm{lit}}$ and the full network is the
> utility level's, since the $\theta_u$ control, $\tfrac12(\ell_0-\varphi_L)$, keeps its maximum where
> $q_{\mathrm{lit}}$ has it; Appendix C §8 splits the utility field into the part that moves the mode
> and the part that lowers the all-region mass. What $\Delta_{\textit{some}}$ records is not that
> movement: the shift under these two priors, $+0.0295$ and $+0.0421$, is all-region mass that the
> tempering adds to $q_{\mathrm{lit}}$ and that the utility level then fails to take away, as the
> paragraph above reports.

**E6. The word "delta" (user, 2026-09-15).** Two sites, so that the name is read as the distribution
and not as a difference. In Text cell 4 Part D, after "one row for each prior and utterance at that
prior's $\theta_u^\ast$.":

> The name is the delta *distribution* of Text cell 3 §4 item 5, the point mass at
> $(\varphi_S^\ast,\varphi_u^\ast)$, and the same word in the *delta-like* prior names a
> $\mathrm{Beta}(\alpha,1)$ approaching a point mass at $s=1$. Neither use carries any relation to
> $\Delta_y$, the shift of Eq. (37).

and in Part C, at the first occurrence of "delta-like", which precedes Part D:

> …and the delta-like prior concentrated on the all-region, a $\mathrm{Beta}(64,1)$ approaching a
> point mass at $s=1$, which needs that $\Lambda$…

**E4. Text cell 4b, after "We note the difference and reserve our position on it." (T6 item 1, for
Code Cell 2b).** Inserted before "Under *no* and *all*…", which then opens a new paragraph:

> Over the eight rows Code Cell 2b prints, the five at $\theta_u^\ast$ and the three realizable, the
> mode position criterion is met in all eight and the mode shift criterion in two, the delta-like
> prior's; the mode and q shift criteria agree in four of the eight. In grid steps the mode lies $19$,
> $20$, $27$ and $11$ nodes above the $\ell_0$ peak under the four diffuse priors and $11$ below it
> under the delta-like prior. The flat row is the plane's cell $(1,512)$, one of the $21$ cells
> Appendix C §8 tabulates where the q shift criterion is met and the mode shift criterion is not.

**E5. Text cell 6, section *Where both of Part C's q criteria hold*: two paragraphs after "What the
conjunction costs" (T6 item 2, R14).**

> **The same plane under the delta read-out.** Code Cell 4 also reads the mode shift and mode
> position criteria of Text cell 4 Part D off every cell. The mode position criterion holds in the
> same $59$ cells as the q position criterion. The mode shift criterion holds in $67$ cells against
> the q shift criterion's $74$, and the two disagree in $35$: the q shift criterion alone is met in
> $21$, all at $\alpha\le16$, and the mode shift criterion alone in $14$, which are ten cells of the
> saturated $\alpha=1024$ row and $(32,16)$, $(64,2)$, $(64,4)$ and $(64,8)$. Both mode criteria hold
> together in $13$ cells, every one of them inside the band of $33$, so the two conjunctions part in
> $20$ cells, all of them met under q alone.
>
> Under the delta read-out the band keeps its right arm and loses its left. The mode position
> criterion's floor is the q position criterion's at every $\alpha$. The mode shift criterion is never
> met at $\alpha\le8$; from $\alpha=16$ its floor is $256$, then $16$ at $\alpha=32$, then $2$ from
> $\alpha=64$ on. The floor of both mode criteria is therefore absent at $\alpha\le8$ and reads $256$,
> $256$, $512$ and $1024$ at $\alpha=16$, $32$, $64$ and $128$, against the q conjunction's $64$,
> $256$, $512$ and $1024$. The right arm, set by the position criteria, is shared from $\alpha=32$;
> the left arm, where the q shift criterion's floor falls as the prior sharpens, exists only under q.
> Appendix C §8 measures what the mode does there. Every cell where the mode moves up has the
> tempered control's mode at $s\le0.9405$, and every cell where it moves down has it at
> $s\ge0.9405$; at $\alpha=1$, $2$, $4$ and $8$ the $\ell_0$ peak, which is the tempered control's
> mode, sits at $s=0.5000$, $0.6726$, $0.8085$ and $0.8849$.

Choices put to the user, all approved 2026-09-15:
- E3 corrects an interpretive sentence (agent/agent.md §5.4); its replacement follows R15.
- E2 writes the mode as the node $k^\ast$, following $k$ as the node index of Eqs. (25)–(27).
  Appendix C §8 writes $k_1,k_2$ for the utility coefficients, in a separate cell.
- E5 gives the V as a result and stops at the measurement: the two paragraphs do not say which
  criterion reads which part of the field.


#### 7. T7 records: approved by the user 2026-09-15 and applied

Six changes, in `agent/decisions.md`, `thesis_outline/revisions.md`, `agent/agent.md` and the notebook. Under
agent/agent.md §3.1 a settled decision is never edited, so B8 takes a dated finding rather than a rewrite.

**A. `agent/decisions.md` B8, appended under *Findings added later*.**

> - **2026-09-15. The criteria are printed, and so is the mechanism under them.**
>   - T1 (2718404): Code Cells 2 and 2b, mirrored in E2 and E2b, print per row the modes of ℓ₀,
>     ℓ₀ − φ_L and φ_S\* in s, the mode shift in s and in grid steps, the two mode criteria beside the
>     two q criteria, the gap between the two largest nodes, and the counts and pairwise agreement.
>     At Λ = 8 the pairs agree in 4 of 4 rows; at Λ = 512 the shift criteria agree in 4 of 8 and the
>     position criteria in 8 of 8.
>   - T2 (5ee04a6): Code Cell 4 prints the same criteria over the 121 cells: 67, 59 and 13 against
>     q's 74, 59 and 33, the 35 cells where a shift criterion and its counterpart disagree, the four
>     unmoved modes, the 5.6e-5 smallest gap, and the floors under both read-outs.
>   - T3 (27a4122, prose 5a7bc8e): Code Cell C prints the tilt/width split, the plane counts and
>     Eq. (24)'s halving, reported in the new Appendix C §8.
>   - T6 (af971c4): Text cell 4 Parts C and D, Text cell 4b and Text cell 6 carry the criteria in
>     prose, under C7's names and B10's stance.
>   - Every number in this entry's *Evidence* and in the F4/F5 findings above is therefore printed
>     by a cell, and the numbers Q2 and Q6 of `thesis_outline/revisions.md` quote are sourced (C6).

**B. `agent/decisions.md` E register, new entry E14.**

> **E14. The quantities T1–T3 added (2026-09-15).** Classed by the agent; the counterfactual label
> was confirmed by the user 2026-09-14.
> - Code Cells 2 and 2b (and E2, E2b): the modes in s, the mode shift in s and in grid steps
>   $k^\ast-k_0$, the two mode criteria and their conjunction, the top-2 gap, and the counts and
>   agreement: class (b), statistics of the delta read-out (B7, B8), defined in Text cell 4 Part D
>   since T6.
> - The grid spacing printed in that block's legend: class (d), read from the grid of I6 rather than
>   stored as a constant.
> - Code Cell 4, `lambda_alpha_sweep`: per cell under *some*, the mode nodes of φ_S\*, ℓ₀ and
>   ℓ₀ − φ_L, the modes of φ_S\* and ℓ₀ in s, whether φ_S\*'s mode lies outside the cell of *all*, and
>   the smallest top-2 gap of the three fields: class (b). `plane_summary`'s counts, agreement, the
>   35-cell table and the six floors: class (b). Signs are read with I5's zero band.
> - Code Cell C, `utility_split_report` (Appendix C §8): the tilt and width coefficients of the
>   utility field, the span-B residual, the two slopes at the tempered control's mode, the modes and
>   all-region masses of the four fields, the plane counts, the distances from c/2, the Gram and
>   exact-form errors, and the limit field's mode and criteria: class (b), statistics of Eqs. (15),
>   (16), (23) and (24) defined in Appendix C §8.
> - The two single-part fields, the tempered control plus tilt alone and plus width alone:
>   **counterfactual manipulations** (C8), controls in nature but not manipulations of the model,
>   since no setting of θ_u, Λ or μ_u produces either. Their printed numbers are class (b). B4's list
>   of retained fixed-θ_u controls (`theta_u_learned_reach.md` §5.C) is unaffected, since neither
>   field is an evaluation the model is run in. The printed block and Appendix C §8 name them so.
> - Appendix C §1 writes every projection per unit Λ; §8's coefficients are the exception, each at
>   its configuration's own Λ and θ_u\*, and §8 says so.
> - Code Cell 2b's own quantities stay under E12, and E13's masses are unchanged.

**B2. `agent/decisions.md` C section, new entry C8 (the user, 2026-09-15).**

> ### C8. "Control" names a manipulation of the model; an algebraic one is a counterfactual manipulation
> - Status: Settled
> - Decided by: user (2026-09-15)
> - Decision: both kinds are controls in nature. The notebooks keep **control** for a manipulation of
>   the model, a configuration the network is actually run in with a parameter held off its learned
>   value: Part C's θ_u control, Text cell 5's θ_u = 1 tables, the μ_u settings, the m = 1 basis. A
>   quantity built by algebra on settled fields, which no setting of the model produces, is a
>   **counterfactual manipulation**: Appendix C §8's two single-part fields, the tempered control plus
>   the tilt part alone and plus the width part alone.
> - Theoretical reason: none. The distinction is for the reader (the user: "for the sake of not
>   confusing the reader").
> - Implementational reason: agent/agent.md §3.3 keeps q_lit, the tempered control and the model apart, and
>   B4 lists the retained fixed-θ_u controls in `theta_u_learned_reach.md` §5.C. A field that is the
>   tempered control plus part of the utility field would take a third name confusable with the
>   second, and would enter that list without matching any run.
> - Bogacz status: naming convention; no operation.
> - Depends on it: Appendix C §8's prose, Code Cell C's printed block, E14's classing.
> - Evidence: no setting of θ_u, Λ, μ_u or B makes the network settle on either field; each is
>   φ_S\*(θ_u = 0) plus one column's share of Eq. (23)'s utility field.

**C. `agent/decisions.md` I register, new entry I12.**

> ### I12. The mode is the first node of an argmax, and the gap is printed
> - Status: Settled
> - Decided by: agent, pending user confirmation (2026-09-15)
> - Decision: the mode of a field is `torch.argmax`, which takes the **first** node when two nodes
>   tie. Every block that reports a mode also prints the gap between the two largest values of
>   φ_S\*, so a tie would print as 0. Observed smallest: 3.4e-3 over Part D's rows at Λ = 8,
>   7.8e-3 over Code Cell 2b's rows, 5.6e-5 over the plane.
> - Theoretical reason: none. B7 defines the mode as the largest node and is silent on ties.
> - Implementational reason: a tie has to resolve somehow, and B8's mode shift criterion is a strict
>   node comparison, so which way it resolves would decide the criterion in a tie. Printing the gap
>   makes the rule's reach visible instead of assumed.
> - Bogacz status: statistic of the delta read-out (his Eq. 34); no counterpart in the tutorial.
> - Depends on it: B8's two criteria; Code Cells 2, 2b, 4 and C.
> - Evidence: the gaps printed in those cells; `agent/audits/2026-09-13-delta-criteria/output.txt`.

**D. `thesis_outline/revisions.md`.** Three rows in §8, and two stale lines corrected. The R14 and
R15 rows are the user's and are not edited; the note goes in §8.

> | Q2's Part D and Λ = 512 rows: the modes, the mode shift in s and in grid steps, the two mode
> criteria | `main.ipynb` Code Cells 2 and 2b, the mode criteria block |
> | Q2's plane counts (67, 59, 13 against 74, 59, 33), the 35 disagreeing cells, the four unmoved
> modes, the 5.6e-5 gap, and the V under both read-outs | Code Cell 4, `plane_summary` |
> | Q6's tilt/width split, the 50 and 67 up/down counts, Eq. (24)'s halving and the limit field |
> Code Cell C, `utility_split_report`; Appendix C §8 |
>
> (2026-09-15: R14's and R15's code tasks, T1–T3 and T6 of
> `agent/history.md` §6, are closed; T7 and T8 remain.)

- Q2, under *The audit*: "**Nothing in this subsection is printed by a notebook cell yet** (see
  "Printing" below)." becomes "**2026-09-15: every number in this subsection is printed**, by Code
  Cells 2, 2b and 4."
- Q6, at *Preliminary result*: "(record F4; `agent/audits/…/mode_mechanism_output.txt`; not printed by any
  cell)" becomes "(record F4; printed by Code Cell C and reported in Appendix C §8 since 2026-09-15)".

**E. `agent/agent.md` §3.3, the class (c) row (the user, 2026-09-15: "fix the error in agent/agent.md").** The row
cited "decision E4" for the rule that a control states its justification in the prose; the entry
about controls is **B4** (E4 in `agent/decisions.md` is the elicited-prior finding, and Code Cell E4 in
`appendix_E.ipynb` is a third thing with that label). The row now cites B4, says a control is a
configuration the network is actually run in, and adds C8's distinction: a quantity built by algebra
on settled fields is a counterfactual manipulation, not a control.

**F. The naming applied with C8 (the user, 2026-09-15).** Code Cell C's comment and printed legend and
Appendix C §8's sentence now say *counterfactual manipulation* and reserve *control* for a
configuration the model is run in. Code Cell C's printed legend grows by one line, so main was
re-executed; `appendix_E.ipynb` was not, since E3 reads main's Code Cell 2 and 2b outputs and Code
Cell C is not mirrored there.

Confirmed by the user 2026-09-15: I12; the Q2 and Q6 corrections made in place; C8's naming, so
E14 classes the two single-part fields as counterfactual manipulations rather than as controls; and
the `agent/agent.md` fix. Nothing in T7 is left open.

- [x] **T0 (2026-09-14). Checkpoint.** HEAD 7854b8f, clean tree. T1 prints in Code Cell 2, and so in
  Code Cell 2b, which calls the same function (S-5 of `evaluation_partD_atStrongLambda.md`).

- [x] **T1 (2026-09-14). Code Cell 2, `delta_readout_report`: print the mode shift and mode position
  criteria (C7 names; (a) and (b) below).** Closed: one block at the end of `delta_readout_report`, so
  it prints in Code Cell 2 (Part D's four rows at Λ = 8) and Code Cell 2b (five rows at θ_u\* and three
  realizable rows at Λ = 512). Per row: modes of ℓ₀, ℓ₀ − φ_L and φ_S\* in s, the signed mode shift, the
  mode shift / mode position criteria and both, the q shift / q position criteria and both, the gap
  between the two largest nodes; then counts and pairwise agreement. Wording under B10/C7. Modes are
  printed in s only, not also in ζ (agent, pending user confirmation).
  **Superseded 2026-09-14 by the user:** "Print the mode shift in grid steps alongside s, then add a
  concise guide in code comment or text explaining to the reader that they can recover zeta by
  multiplying by 0.12." Added: a `steps` column (k − k0, signed) beside the shift in s; a printed
  legend line giving the grid spacing, read from the grid, and saying that steps times the spacing is
  the shift in ζ; a two-line code comment on why (s compresses toward the ends of the scale).
  Hand check before execution, from the printed s values: +3 for the Gaussian at Λ = 8, −11 for the
  delta-like row.
  Executed 2026-09-14: the column reads +3, +6, +3, +5 at Λ = 8 and +19, +20, +27, +11, −11 at Λ = 512
  (realizable rows equal their θ_u\* rows), matching the hand check; printed spacing 0.12. Only the legend,
  the column and E3's line counts changed. main 0 errors, 8 figures, 14/14, 249 s; appendix_E 0 errors,
  5 figures, E2 18/18, E3 PASS (203 and 234 lines identical).
  Acceptance: Λ = 8 rows equal `output.txt` §PART D ROWS in every mode and yes/no; the delta-like row
  equals it too; the Λ = 512 rows equal `evaluation_partD_atStrongLambda.md` F7. Smallest top-2 gap
  3.4e−3 (no ties). Code Cell 2 at Λ = 8: the pairs agree in 4 of 4 rows. Code Cell 2b at Λ = 512: mode
  and q shift criteria agree in 4 of 8 rows (flat and Beta(3,1), each at θ_u\* and realizable, have
  the q shift criterion met and the mode shift criterion not), position criteria in 8 of 8.
  Every previously printed line unchanged apart from the C7 renames. Originally:
  - For each Part D row under *some*, at θ_u\* and at the realizable θ_u row B7 already prints,
    print:
    - mode(ℓ₀), mode(ℓ₀ − φ_L) and mode(φ_S\*), in ζ and in s;
    - the signed mode shift, and whether (a) is met;
    - whether the mode is outside the cell, i.e. whether (b) is met;
    - both criteria together;
    - q's two conditions beside them, so the rows can be compared.
  - The mode is the grid node where the field is largest, as B7 defines it. Say that ties are
    resolved to the first index, and print the smallest gap between the two largest nodes.
  - Acceptance: the values equal `agent/audits/2026-09-13-delta-criteria/output.txt` §PART D ROWS, and every
    line the cell printed before is unchanged.

- [x] **T2 (2026-09-14). Code Cell 4: the mode criteria recorded and summarized on the plane.** Closed:
  `lambda_alpha_sweep` stores, under *some* per cell, the mode nodes of φ_S\*, ℓ₀ and ℓ₀ − φ_L, the modes
  of φ_S\* and ℓ₀ in s, whether φ_S\*'s mode is outside the cell of *all*, and the smallest top-2 gap of
  the three fields. `plane_summary` adds `mode_shift`, `mode_position`, `mode_both` and `floors` (all six
  criteria) to its returned summary, and prints one block after the existing lines: the counts under
  both read-outs, unmoved modes and the ℓ₀ / ℓ₀ − φ_L comparison, the smallest gap, agreement for the
  shift criteria, the position criteria and the conjunctions, the 35 cells where a q criterion and its
  mode counterpart disagree (θ\*, P(all|some), shift, tempering, utility, both modes, the four yes/no),
  and the floors by α under both read-outs (the V), with * where a criterion also holds below its floor
  (none do). C7 names throughout. Acceptance (`agent/audits/2026-09-14-mode-plane/test_t2.py`, before
  execution): existing lines unchanged; counts 67/59/13 against 74/59/33, unmoved 4, differing modes 0,
  gap 5.60e−05, agreement 53/21/14/33, 59/0/0/62, 13/20/0/88, all 35 rows and the V table equal to
  `output.txt`: PASS. Executed: main 0 errors, 8 figures, 14/14, 251 s; the only output change is Code
  Cell 4's 62 added lines, equal to the test; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS (203
  and 234 identical), 703 s. Code Cell 4 is not mirrored in appendix_E. The unmoved-mode count is
  printed as a node comparison (a shift of 0 steps). Commit 5ee04a6. Originally:

- **T2. Code Cell 4: record and summarize the delta criteria on the plane.**
  - `lambda_alpha_sweep` stores mode(φ_S\*), mode(ℓ₀) and mode(ℓ₀ − φ_L) under *some* per cell.
  - `plane_summary` prints, for the delta read-out:
    - the counts for (a), (b) and both;
    - the agreement of (a) with q's first condition, of (b) with the second, and of the two
      conjunctions;
    - the cells where the read-outs disagree, with θ\*, q_H, shift, tempering, utility and the two
      modes;
    - the floors for (a), (b) and both;
    - **the V table under both read-outs**;
    - the unmoved-mode count, and whether mode(ℓ₀) and mode(ℓ₀ − φ_L) ever differ.
  - Acceptance: equal to `output.txt` §PLANE, §AGREEMENT, §CELLS WHERE THE READ-OUTS DISAGREE and §FLOORS
    AND THE V; the existing lines unchanged.

- [x] **T3 (2026-09-14). Code Cell C, `utility_split_report`: the tilt/width split printed in Appendix
  C (user: new §8, Blocks 1-3, Block 1 at Λ = 8 only; §0).** Closed for the code: one function and one
  call appended to Code Cell C, called with `part_d_priors()` and Code Cell 4's `sweep_grids` α and Λ
  lists, so the plane is Code Cell 4's. Prints Blocks 1-3 as recorded in §0, under C7 names; the two
  single-part fields are labelled as counterfactual, not network states (agent, pending user
  confirmation: a construction of the report, not a control of the model). Acceptance
  (`agent/audits/2026-09-14-utility-split/acceptance.py`, run before insertion): every number of
  `mode_mechanism_output.txt` and `halving_check_output.txt` for Part D's four diffuse rows, every plane
  count, the 21-cell and ten-cell tables: PASS. Executed: main 0 errors, 8 figures, 14/14, 266 s; the
  only output change is Code Cell C's 91 added lines, equal to the pre-insertion test; appendix_E 0
  errors, 5 figures, E2 18/18, E3 PASS (203 and 234 lines identical), 673 s. Code Cell C is not mirrored
  in appendix_E, so T4 does not apply. The §8 prose (and §9 renumbering, ToC, anchor) is drafted in §5
  for review. Commit 27a4122. Originally:

- **T3. The tilt/width decomposition (R15). Placement is the user's call.**
  - The preliminary result, F4 below, comes from `mode_mechanism.py`. Decide whether it is printed,
    and where:
    - (i) Code Cell 2, for Part D's rows;
    - (ii) Code Cell 4's summary, for the plane counts;
    - (iii) both;
    - (iv) not printed, if the paper does not quote it.
  - [x] Prerequisite (2026-09-13): the Eq. (24) halving is checked across the plane and on Part D's
    rows (F5, `halving_check.py`). The placement decision above is still open.
  - Acceptance: equal to `mode_mechanism_output.txt` for whatever is printed.

- [x] **T4 (2026-09-14). Mirror into Appendix E** — closed for T1: the block patched into E2 with the
  same replacement; no new printing call, so E3's replay list is unchanged. Originally:
  - Lift T1's changes and any T3 addition to Code Cell 2 verbatim into E2.
  - If a new printing call is added, add it to E3's replay list, with what it needs passed in.
  - Keep the `# === Code Cell 2` prefix.

- [x] **T5 (2026-09-14). Execute main, then appendix_E** — closed for T1: `RUNNER OK main.ipynb: error
  outputs 0, figures 8, runtime 248 s`, 14/14; `RUNNER OK appendix_E.ipynb: error outputs 0, figures 5,
  runtime 706 s`, E2 18/18, E3 PASS (202 and 233 lines identical), E4 unchanged. Output diffs against
  7854b8f: the T1 block inserted, and the C7 renames. Record: `agent/audits/2026-09-14-no-position/`. T2, T3
  and T6 remain open. Originally:
  - Baseline: main 0 errors, 6 figures, 14/14; appendix_E 0 errors, 3 figures, E2 18/18, E3 PASS.
  - Diff the stored outputs against the T0 hash: only insertions, plus `cost:` lines.

- [x] **T6 (2026-09-15). Notebook prose, approved by the user and applied.** Closed: the six edits of
  §6 (E1–E6) into Text cells 4, 4b and 6, commit af971c4. E1 Part C, the pairs do not always agree
  (121 position, 35 shift); E2 Part D, the two criteria as unnumbered displays on $k^\ast$ and $k_0$,
  the grid-steps column and the 0.12 spacing, and the Λ = 8 result (3, 6, 3, 5 steps; met under none
  and all four); E3 the R15 correction, made explicit at the user's instruction (which shift, which
  movement); E4 Text cell 4b, the eight rows and the steps at Λ = 512, with the flat row as plane cell
  (1, 512); E5 Text cell 6, the plane under the delta read-out and the V under both read-outs; E6 (the
  user, 2026-09-15) the word "delta" is the delta distribution, in the read-out's name and in the
  delta-like prior, and is unrelated to $\Delta_y$. Applied by `agent/audits/2026-09-14-mode-plane/apply_t6.py`.
  Checks: every number in the new prose is printed by Code Cell 2, 2b, 4 or C; 74 anchors, 73 ToC
  links, none unresolved; no new "condition" or "verdict"; markdown spacing kept. Markdown only, so
  the notebooks were not re-executed. Originally:

- **T6. Notebook prose. Wording needs the user's review before it lands.**
  - Text cell 4 Part D's reading guide defines (a) and (b) as reported statistics, class (b) of
    agent/agent.md §3.3, as unnumbered displays so Eqs. (1)–(41) do not shift (agent/agent.md §2 item 5). It
    also announces the new lines.
  - Text cell 6, *Where both of Part C's conditions hold*: the delta criteria's counts, and the V
    under both read-outs, reported as a result (R14).
  - Text cell 4 Part C: one sentence that the conditions have a delta counterpart (B8) and that the
    two do not coincide.
  - Every quoted number is checked against the executed output.

- [x] **T7 (2026-09-15). Records, approved by the user and applied; commit 5acb6b5.** §7 holds the
  six changes: `agent/decisions.md` B8's dated finding, the new C8 (control names a manipulation of the
  model; an algebraic one is a counterfactual manipulation), I12 (the argmax tie rule, confirmed by
  the user), E14 (the classing of everything T1–T3 added); `thesis_outline/revisions.md` §8's three
  rows, its dated note, and the two stale "not printed by any cell" lines; `agent/agent.md` §3.3's class (c)
  row, which cited decision E4 where the entry is B4, now also carrying C8's distinction; and C8's
  naming in Code Cell C's comment and printed legend and in Appendix C §8. Verified: main 0 errors, 8
  figures, 14/14, the only output change being Code Cell C's legend; Code Cells 2 and 2b unchanged, so
  appendix_E was not re-executed. Still stale, left for the user: `revisions.md` line 816 says R15's
  investigation "is an open task in `agent/history.md` §6", which T3 closed.
  Originally:

- **T7. Records.**
  - `agent/decisions.md`: B8's implementational reason; an E-register entry for each new printed
    quantity; an I-entry for the mode tie rule if T1 makes one.
  - `thesis_outline/revisions.md` §8: point the numbers of Q2 and Q6 at their cells.

- [x] **T8 (2026-09-15). Commit** (agent/agent.md §4.3), with the hash on each closed task: T1 2718404,
  T2 5ee04a6, T3 27a4122 with its prose 5a7bc8e, T6 af971c4, T7 5acb6b5, plus the record commits
  9937734, 92cf465, 4cb1d1a and 28c838a. Nothing is pushed; the user asks for pushes.

*Full original:* `git show 1558f83:procedure_records/delta_criteria_printing.md`

---

<a id="r7" name="r7"></a>

## 7. Part D at a strong Λ, and the new cell after Code Cell 2

*Was* `procedure_records/evaluation_partD_atStrongLambda.md`

**Opened** 2026-09-14 13:51 · **Closed** 2026-09-14 20:05 · 5 commits

**Settled** B3, B8, B9, I11

**Opened by**

> Can you probe what the part D evaluations would look like if Lambda is fixed at 512 for all
> priors-cases and utterances?
> write your finding to a new evaluation_partD_atStrongLambda.md. We want to insert a new text+code
> cell right after the current code cell 2 to report this observation; the existing report on the
> delta-like base-prior will also be moved to this new cell since it uses Lambda=512. The md file
> will be used as a guide to this change.
> You recommendation is approved for S-1 to S-5. Regarding S-6, yes we will need to rewrite the
> argument; and we will do that after the codes are finished. Regarding S-7, yes, we want figures
> for all five priors as well as the "no" "some" "all" figures under gaussian prior.

##### 1.3b Findings during implementation (2026-09-14, from `test_sources.py`, outside the notebooks)

- **F10. The integrated run holds for the two new rows.** Flat: one update of Eq. (20) reaches
  θ_u = 7.8161 (λ_max(H) = 63.1); the integrated fixed point gives shift −0.0119 and q_H = 0.0384,
  both met, 13,589 Euler steps, agreeing with Eqs. (15)–(16) to 1e−9. Skewed high: θ_u = 7.9926
  (65.9), shift −0.0925, q_H = 0.0442, both met, 14,199 steps. Their roundoff floors, 2.8–3.0e−11
  and 3.0–4.5e−11, sit below `infer`'s 1e−9 tolerance, as the delta row's does.
- **F11. A printed number in Code Cell 2 changes with the move.** The ℓ₀-invariance of the φ_S
  contrasts at a shared θ_u = 1, over Part D's rows, is 5.3e−15 over the four priors against 3.6e−14
  over five. Text cell 4 Part D quotes 3.6e−14 (prose pass). At Λ = 512 over five priors: 1.1e−13 at
  θ_u = 1, and **0.0001** at each prior's own θ_u\* (0.0575 at Λ = 8), since the θ_u\* nearly coincide.
- **F12. The peaks against the cell of *all*, at Λ = 512 and θ_u\*:** Gaussian 6 nodes below the
  cell (inside against outside −3.256), flat 5 (−1.964), Beta(1,3) 7 (−3.216), Beta(3,1) 5 (−1.841),
  delta-like 1 (−0.081). Only the delta row sits at the boundary.
- **F13. The spike block at Λ = 512.** Under flat and Beta(3,1) the full network's mode moves to
  s = 0.92 with density 0.0000 at the top node; q_lit is unchanged. The block's wording ("the
  right-edge spike") describes Λ = 8; prose pass.
- **F14. A printed sentence Code Cell 2b now contradicts on its own page (S-6).** The moved
  Gaussian control still prints "Raising Lambda alone moves the shift AWAY from the criterion, so
  the delta row's result is the prior's doing and not its Lambda's", a few lines below a table in
  which raising Λ alone moves flat and Beta(3,1) into the criterion. It was moved verbatim, as
  S-2 required; its wording belongs to the prose pass.
- Timing: Code Cell 2 224 s (was about 245 s), Code Cell 2b 22 s.


##### S-1. What the new cell reports, and what Part D keeps

- **(a)** Part D keeps the four diffuse priors at Λ = 8. The new cell reports all five priors at
  Λ = 512, and the delta row appears only there. *Recommended*: the new cell is then one
  configuration family at one Λ, and the Λ = 8 table stops mixing two Λ.
- (b) Part D keeps all five rows as now, and the new cell adds the Λ = 512 sweep plus the moved
  delta-row blocks. The delta row would be printed twice.
- Consequence of (a): Part D's Λ = 8 counts become "first condition 0 of 4, conjunction 0 of 4".
  The delta row's numbers do not change.


##### S-2. Which parts of the "report on the delta-like base prior" move

Inventory of Code Cell 2 that uses Λ = 512 or the delta row. Line numbers are of Code Cell 2's
source as of HEAD 9de5319.

**Move clearly (delta row only, or Λ = 512 only):**

| Block | Lines |
|---|---|
| comment block and `DELTA_ALL_ALPHA` / `DELTA_ALL_LAMBDA` | ≈740–757 |
| `base_prior_sweep`: the Gaussian-at-Λ = 512 control | 949–961 |
| `base_prior_sweep`: THE DELTA-LIKE ROW (headroom) | 976–1006 |
| `base_prior_sweep`: THE MECHANISM (Eqs. 23–24 on this row; also prints the Gaussian's Eq. (23) gap) | 1008–1051 |
| third figure (delta-like prior, log axis) | 1513–1557 |

**Shared (loop over `part_d_priors()`, which includes the delta row). Each must be split or
duplicated:**

| Block | Lines |
|---|---|
| `part_d_priors` itself; also read by `realizability_report` and by appendix E's E4 | 760–770 |
| `base_prior_sweep`'s main table, tempering split, and condition counts | 859–914 |
| ℓ₀-invariance across the five priors, at the network's Λ = 8; **the delta prior is taken at Λ = 8 there** | 917–947 |
| `realizability_report`'s table and "threshold exists under N of M" | 1208–1237 |
| `delta_readout_report`'s rows and the ℓ₀-peak table | 1349–1400 |

**Dependent (the delta row is the only case that triggers them):**

| Block | Lines |
|---|---|
| `realizability_report`'s RUN, NOTHING IN CLOSED FORM (picks the cheapest runnable both-conditions row, today only the delta row) | 1239–1305 |
| THE ROUNDOFF FLOOR, run on that row; the floor justifies `infer`'s 1e−9 tolerance (I3) | 1307–1320 |
| `delta_readout_report`'s realizable rows | 1356–1360 |
| AT THE BOUNDARY and the finer grids (triggered by a peak moving out of the cell) | 1402–1420 |

**Stays:**

- the integration-cost table (Gaussian only), 1193–1206;
- the spike block (flat, skewed high at Λ = 8);
- the second figure. Under S-1(a) its Λ filter becomes a no-op.

Question for the user: does "the existing report on the delta-like base prior" cover the dependent
blocks too? This matters because of the roundoff floor. Under S-1(a), with the delta row gone from
Code Cell 2, no Λ = 8 prior has a both-conditions threshold (§1.2 of the stored output). Code
Cell 2 would then print neither the integrated run nor the floor that supports I3.
*Recommendation:* move them. At Λ = 512 the run gains two more candidates (flat, skewed high; F6).


##### S-3. Naming the new cells

- (a) No renumbering: e.g. "Text cell 4b" and "Code Cell 2b", with anchors `tc4b` and `code2b`.
  *Recommended.* Existing references to Code Cells 3 and 4 and Text cells 5 and 6 stay true: Text
  cell 5 (9 mentions), Appendix C/D and Code Cell D comments, Code Cell 4, agent/decisions.md,
  revisions.md, agent/agent.md, the records.
- (b) Renumber everything after it. That touches every site above, and every record that cites them
  by number.
- The header prefix of the new code cell must not begin `# === Code Cell 2` followed by a colon-free
  continuation that E3's `startswith("# === Code Cell 2")` would also match. **"Code Cell 2b"
  matches that prefix.** E3 would pick whichever comes first, which is Code Cell 2 by position.
  It still works today, but fragilely: either tighten E3's match to `# === Code Cell 2:` or choose a
  name that does not share the prefix.


##### S-4. Appendix E

- E3 diffs E2's replayed output against main's Code Cell 2 output alone. After the move, blocks now
  checked by E3 would sit in the new cell and fall outside that check, unless:
  - **(a)** appendix E gains a mirror of the new cell (E2b), and E3 extends to diff it against the
    new cell's stored output. *Recommended*: keeps E3's coverage, including the integrated run and
    the delta read-out, where the relay's path differs.
  - (b) E3 covers Code Cell 2 only, and appendix E states it.
- E4's `relay_bound_report` iterates `part_d_priors()`. If S-1(a) removes the delta row from that
  function, E.1's delta-like bound (1.26e−7) disappears. Either pass the delta row to E4 explicitly
  or keep a function that returns all five.
- I10's implementational reason ("E3's replay needs no new calls") no longer holds. I10 needs an
  amendment, the user's to confirm.


##### S-5. Order against `delta_criteria_printing.md`

That record's T1 adds criteria (a) and (b) to `delta_readout_report` in Code Cell 2, with
acceptance against the five-row Part D output. Options:

- (a) Do this move first, then T1 prints the criteria in both cells, at Λ = 8 and at Λ = 512.
  *Recommended*: F7 is exactly a disagreement those criteria would show.
- (b) T1 first, then move.


##### S-6. Interpretive claims the new cell contradicts (agent/agent.md §5.4: stop and ask)

These sentences are true of the Λ = 8 table and become Λ-conditional once the new cell prints §1.
Rewriting them is the user's call.

- **Text cell 4 Part C:**
  - "Across Part D's five priors the conjunction holds under exactly one" (≈ line 124);
  - "produces it nowhere else among Part D's five … and not under the four diffuse priors"
    (≈ 192–199);
  - commitment 1, "it is the prior doing that rather than the raised Λ" (≈ 140–147). Still true
    for the Gaussian control. But raising Λ alone brings flat and Beta(3,1) into the conjunction, so
    for those priors Λ does matter.
- **Text cell 4 Part D:**
  - "The conjunction holds under the delta-like prior, and under it alone" (≈ 298);
  - "negative in every one of them" and "Only when the prior is already concentrated there does the
    utility level move much mass at all" (≈ 312–316). Skewed low turns positive at Λ = 512 (F5);
    flat and skewed high move 0.10–0.19.
  - "So the sign of the shift is a fact about the prior … and not about the entry" (≈ 317–319). At
    Λ = 512 the entry's strength changes the sign under two priors.
- **Text cell 6:** "Four of Part D's rows sit outside that band and the delta-like row sits inside
  it" (≈ 273–278). Still true of Λ = 8; at Λ = 512 flat is the (1, 512) cell inside the band.


##### S-7. Figures

- Does the new cell add a figure of *some* under the five priors at Λ = 512? The four diffuse
  priors are now comparable with the delta row on one Λ, so a shared log axis could hold all five.
- Figure count changes 6 → 7 if yes. The baseline in agent/agent.md §5.1 must follow.

---


##### 6.4 Findings

- **F15.** Part D quoted q_lit masses 0.0504 and 0.1368 and tempered masses 0.0066, 0.1357 and 0.2356
  that no cell printed at four decimals (C6). Resolved by printing the three masses beside the split
  (Code Cell 2, E2, and so Code Cell 2b).

- **F1. The conjunction holds under 3 of 5 priors, against 1 of 5 at the stored settings.** Flat
  and skewed high join the delta-like row. The Gaussian and skewed-low priors still fail the first
  condition, and by more than at Λ = 8 (+0.0071 against +0.0008; +0.0089 against +0.0004). The delta
  row is the same row as before, since it already carried Λ = 512.


- **F2. The entries hold under every prior; at Λ = 8 they did not.**
  - At Λ = 8 the diffuse priors override the entries for *no* and *all*: max leak 0.63 (Gaussian),
    0.91 (skewed low and high).
  - At Λ = 512 every leak is below 1e−174.
  - So at Λ = 8, Part D's *no* and *all* columns partly measure the override. That is the situation
    Part D's own delta-row paragraph says a probe must avoid.


- **F3. The shifts for *no* and *all* go to zero under every prior. That is saturation (B6).**
  q_lit under *all* holds 1.0000 of the all-region under all five priors, and under *no* about 0.
  Neither has room to move. At Λ = 8 the *all* shifts were −0.4557, −0.0160, −0.1849 and −0.0087.


- **F4. The prior barely matters any more.** The lexical field outweighs ℓ₀.

  | prior | E[s] *no* | E[s] *some* | E[s] *all* |
  |---|---|---|---|
  | gaussian | 0.002 | 0.899 | 0.998 |
  | flat | 0.002 | 0.912 | 0.998 |
  | skewed low | 0.002 | 0.898 | 0.998 |
  | skewed high | 0.002 | 0.914 | 0.998 |
  | delta (all) | 0.003 | 0.946 | 0.998 |

  - θ_u\* lies between +1407 and +1590 under all five priors, all positive. At Λ = 8 the values
    were −28.4, +5950.6, −14.5, +55.0 and +1407.8.
  - φ_u\* and c_y = BᵀW(ℓ₀ − φ_L) nearly coincide across the four diffuse priors. For example, c_some
    ranges over +571.6 to +595.6 in tilt and −374.1 to −387.7 in width.


- **F5. The tempering does not change; the utility level's contribution does.**

  | prior | q_lit | tempered | tempering | utility at Λ = 8 | utility at Λ = 512 |
  |---|---|---|---|---|---|
  | gaussian | 0.0016 | 0.0191 | +0.0175 | −0.0167 | −0.0104 |
  | flat | 0.0504 | 0.1361 | +0.0857 | −0.0559 | −0.1003 |
  | skewed low | 0.0001 | 0.0067 | +0.0065 | −0.0061 | **+0.0024** |
  | skewed high | 0.1368 | 0.2356 | +0.0989 | −0.0568 | −0.1943 |
  | delta (all) | 0.9568 | 0.8982 | −0.0586 | −0.4631 | −0.4631 |

  - The tempering is unchanged because χ_some excludes only the bottom of the scale, so Λ does not
    reach the all-region's literal mass.
  - Flat and skewed high turn negative because the utility level's contribution grows past the
    tempering.
  - Under the Gaussian it shrinks. Under skewed low it changes sign, which makes Part D's current
    sentence "negative in every one of them" false at Λ = 512.


- **F6. Cost.** The threshold is small and passed in one update wherever the conjunction holds.

  | prior | λ_max(H) at θ_u\* | θ_crit | λ_max(H) at θ_crit | updates | holds to θ_u\* |
  |---|---|---|---|---|---|
  | gaussian | 2.50e6 | none | | | |
  | flat | 2.31e6 | 3.078 | 11.5 | 1 | yes |
  | skewed low | 2.53e6 | none | | | |
  | skewed high | 2.25e6 | 1.021 | 3.0 | 1 | yes |
  | delta (all) | 1.98e6 | 2.126 | 6.5 | 1 | yes |

  So an end-to-end integrated run like the delta row's (realizability block) is affordable for flat
  and skewed high as well. Not run by the probe; run in Code Cell 2b, see F10.


- **F7. The delta read-out's criteria (B8) now part from q's conditions on two rows.**

  | prior | ℓ₀ peak (s) | φ_S\*("some") peak (s) | (a) | (b) | q conjunction |
  |---|---|---|---|---|---|
  | gaussian | 0.5000 | 0.9072 | not met | met | not met |
  | flat | 0.5000 | 0.9168 | not met | met | **met** |
  | skewed low | 0.2535 | 0.8966 | not met | met | not met |
  | skewed high | 0.7465 | 0.9168 | not met | met | **met** |
  | delta (all) | 0.9852 | 0.9468 | met | met | met |

  - On the four diffuse priors the peak moves up the scale, to 0.90–0.92, and stays outside the cell
    of *all* (s ≥ 0.95).
  - Under flat and skewed high the q conjunction holds and criterion (a) does not.
  - At the stored settings the two agree row by row (`delta_criteria_printing.md` F1). This is the
    first Part D configuration where they disagree.
  - It fits `delta_criteria_printing.md` F4: the tilt moves a peak up wherever the literal mode sits
    below s ≈ 0.94, while the width lowers the tail.
  - **Not yet measured:** how many grid nodes below θ_L these peaks sit. The boundary check
    prints that only for the delta row.


- **F8. Consistent with the plane Code Cell 4 already prints.**
  - The flat prior is `beta_world_prior(1, 1)` (Code Cell 1, `uniform_world_prior`), which is the
    α = 1 column of Text cell 6's plane.
  - Code Cell 4 prints "both conditions in 33, from (1, 512)" and a first-condition floor of
    Λ = 512 at α = 1. So the flat row at Λ = 512 is already a both-conditions cell of the plane.
  - `delta_criteria_printing.md` F2 finds no delta conjunction at α ≤ 8, which fits (a) failing
    for flat here.
  - Gaussian, Beta(1,3) and Beta(3,1) are not on the plane.


- **F9. Couplings found while scoping the move** (see §3 and §4).
  - Appendix E's **Code Cell E4** (`relay_bound_report`) iterates `part_d_priors()`. E.1 quotes its
    delta-like number (1.26e−7).
  - **Code Cell 4** reads none of Code Cell 2's delta-row names. Its comment at source line 67
    points at "Code Cell 2's realizability block".
  - **I10** records that additions to Code Cell 2 go inside existing functions, so that E3's replay
    needs no new calls. A new cell departs from that implementational reason.

- [x] **T0 (2026-09-14). Checkpoint.** This record and `agent/audits/2026-09-14-strong-lambda/` committed
  as a202cdb; the build and apply scripts read both notebooks at that commit.

- [x] **T1 (2026-09-14). S-1 to S-5 and S-7 settled by the user; S-6 deferred to the prose pass.**
  `agent/decisions.md`: B9 (new), dated findings under B3 and B8, I10 marked amended, I11 (new: naming,
  E2b, E3's two prefixes, E4's explicit delta row). Commit pending with T9.
  - **Implementation choices made by the agent, confirmed by the user 2026-09-14:**
    - the integrated RUN and THE ROUNDOFF FLOOR run for **every** both-conditions row whose arrival
      θ_u is integrable, not only the cheapest; a row that is not integrable is named. The delta
      row's lines are unchanged by this;
    - three printed sentences in Code Cell 2 print only when true: the "not a property of the model
      alone" lines (only if the rows split), and the realizability narrative (only if some row has
      a threshold);
    - `scalar_implicature_probe`'s pointer "its sign is prior-dependent (Part D)" now reads
      "(Code Cell 2b)", since Part D's four rows at Λ = 8 share one sign;
    - the spike block stays in `base_prior_sweep`, so Code Cell 2b also prints it at Λ = 512;
    - all three Code Cell 2b figures use a log vertical axis, like the moved delta-like figure;
    - Code Cell 2b's comments correct E9's stale "Code Cell 3" to "Code Cell 4".
  - Scripts (scratch, to be filed under `agent/audits/2026-09-14-strong-lambda/` at T9):
    `build_sources.py`, `cell2b_template.py`, `test_sources.py`, `apply_to_notebooks.py`, `new_e3.py`.

- [x] **T2 (2026-09-14). New code cell after Code Cell 2** — closed: Code Cell 2b at main cell 9,
  built by `build_sources.py` + `cell2b_template.py`. Acceptance: its numbers equal the probe; every
  moved line prints byte-identically (`test_report.txt`); the flat row at Λ = 512 is a
  both-conditions cell, as Code Cell 4 prints for (1, 512) (Code Cell 4 prints floors, not per-cell
  values, so the match is of verdict, not of digits). Originally: (cell index 8 today), under S-1, S-2, S-3, S-7. Prints:
  - the Λ = 512 table of §1.2;
  - the E[s] and tempering/utility tables of F4–F5;
  - headroom for every row (F3: saturation now applies to *no* and *all* under all five);
  - thresholds and arrivals of F6;
  - the delta read-out peaks against ℓ₀ and the cell, with **node margins for every row that ends
    outside the cell**, not only the delta row (F7);
  - a Λ = 8 against Λ = 512 comparison line per prior for the *some* shift and q_H;
  - the blocks moved under S-2.

  Every θ_u is θ_u\* of its own configuration. Every fixed-θ line is labelled a control (B4). Every
  wall-clock line is behind `cost:`.

  **Acceptance:**
  - the new numbers equal `probe_lambda512_output.txt`;
  - every moved line is byte-identical to the line Code Cell 2 printed at T0, apart from any header
    rename;
  - the flat row equals Code Cell 4's (α, Λ) = (1, 512) cell.

- [x] **T3 (2026-09-14). Code Cell 2 residue** — closed: 1418 lines (was 1566). Acceptance: the only
  changed printed lines are the counts (0 of 4), the pointer to Code Cell 2b, "four priors", and
  the ℓ₀-invariance value (F11). Originally:
  - Remove the moved blocks and adjust `part_d_priors` and the shared loops per S-1/S-2.
  - Update comments that point at the delta row, the third figure, or "Code Cell 3".
  - **Acceptance:** the lines Code Cell 2 still prints equal their T0 versions, except the counts
    S-1(a) changes ("of 5" → "of 4") and anything S-2 splits.

- [x] **T4 (2026-09-14). Code Cell 4** — closed, no edit: its comment points at functions that stay
  in Code Cell 2. Originally: Update the comment at source line 67 if the realizability block moved.
  Nothing else there reads Code Cell 2's names.

- [x] **T5 (2026-09-14). Appendix E** — closed by `apply_to_notebooks.py` and `new_e3.py`: E2
  re-mirrored (exactly the header and the 98 relay-check lines differ from main), E2b added, E3 checks
  both cells, E4 takes the delta-like row explicitly. Originally, under S-4:
  - re-mirror E2 by lifting main's Code Cell 2 verbatim (the scratchpad `remirror.py` pattern of
    the reach record);
  - mirror the new cell if S-4(a);
  - update E3's replay list and its baseline match (S-3's prefix issue);
  - make E4's delta-like row explicit.

- [x] **T6 (2026-09-14). Execute main, then appendix_E** — closed. `RUNNER OK main.ipynb: error
  outputs 0, figures 8, runtime 249 s`, 14/14; `RUNNER OK appendix_E.ipynb: error outputs 0, figures
  5, runtime 671 s`, E2 18/18, E3 PASS on Code Cell 2 (190 identical, 1 changed, 4 inserted) and on
  Code Cell 2b (215 identical, 0 changed). Stored outputs of Code Cells 2 and 2b equal the
  outside-notebook test; Code Cells 1, 3, 4, A–D, E1 and E4 print exactly what they printed at
  a202cdb (`verify_executed.py`). Originally:
  - Baseline: main 0 errors, 6 figures (7 under S-7 yes), 14/14. appendix_E 0 errors, 3 figures,
    E2 18/18, E3 PASS.
  - Diff the stored outputs against T0: Code Cell 2's lost lines must reappear in the new cell.
    `cost:` lines excepted.

- [x] **T7 (2026-09-14). Structure** — closed for code: Text cell 4b (heading, anchor `tc4b`, a scope
  paragraph, anchor `code2b`); ToC regenerated (72 links, all resolve; indices checked); agent/agent.md §1
  cell maps, §2 couplings 1, 2, 7 and §5.1 baseline updated. agent/decisions.md cites cells by name, not
  index, so needs no change. Text cell 4b's argument is the prose pass (S-6). Originally:
  - New markdown cell before the new code cell, with its anchor inside the heading. The code anchor
    goes at the end of that markdown cell (agent/agent.md §2 item 6).
  - Regenerate the ToC (cell 0).
  - Update agent/agent.md §1's cell map: 21 → 23 cells; Text cell 5 onward shift by 2, so Code Cells A–D
    move to 15, 17, 19, 21 and References to 22.
  - Update agent/decisions.md entries that cite cell indices.
  - New displays are unnumbered unless the user approves renumbering (agent/agent.md §2 item 5).

- [x] **T8 (2026-09-14). Records** — closed: agent/decisions.md B9, I11, findings under B3 and B8, I10
  amended, quantity trace entry for Code Cell 2b; `delta_criteria_printing.md` order note. Originally:
  - `agent/decisions.md`: E-register entries for each new printed quantity; B3/B7/B8/I10 updates per T1.
  - `delta_criteria_printing.md`: note the order chosen under S-5, and that its T1 acceptance now
    spans two cells.

- [x] **T9 (2026-09-14). Commit** — closed: T0 is a202cdb; T1–T8 are 3cbb721. Not pushed.

---

- [x] **T10 (2026-09-14).** Drafted, executed and verified: `RUNNER OK main.ipynb: error outputs 0,
  figures 8, runtime 249 s`, 14/14; `RUNNER OK appendix_E.ipynb: error outputs 0, figures 5, runtime
  693 s`, E2 18/18, E3 PASS on Code Cell 2 (191 identical) and Code Cell 2b (217 identical). The only
  changed output lines are the mass columns (F15) and Code Cell 2b's control conclusion (F14). Every
  decimal on a changed markdown line is found in the executed outputs (`verify_prose_pass.py`).
  Committed for review; §6.2 is not settled until the user confirms.

Checkpoint: 8aaf9ff (clean tree). Script: `prose_pass.py` (every replacement asserted against the
current text). All sites of §5 were written against the executed outputs of 3cbb721; the new text is
checked number by number against the re-executed outputs (`verify_prose_pass.py`).

*Full original:* `git show 98c2df8:procedure_records/evaluation_partD_atStrongLambda.md`

---

<a id="r8" name="r8"></a>

## 8. B10: reporting the conditions without taking a position

*Was* `procedure_records/b10_no_position.md`

**Opened** 2026-09-14 20:05 · **Closed** 2026-09-14 20:05 · 1 commit

**Settled** B10, C7

**Opened by**

> your decisions are confirmed. Just remember that we do not take a position that both conditions
> need to be met to count as scalar strengthening. We are just reporting them so that the reader can
> make their own judgment. (Any positions we take would be left to the paper, not the notebook. )
> Execute next step.
> (2026-09-14, second instruction) criterion is kay. Calling it a criterion does not mean we commit to
> this criterion. Also, for clarity, call the first criterion/(a) "the shift criterion" and the second
> criterion/(b) "the position criterion".  When you need to specify which read-out the criterion is in
> terms of, say "the q/mode shift/position criterion Do not use the word "condition" or verdict"
> because we want to keep word choice consistent and avoid confusion.
> For old sentences like "we take", we can substitute with "the reader, in accordance with their own
> …

#### 1. Decisions

- **B10** (user, 2026-09-14): the notebooks report Part C's two conditions (B2) and the delta
  read-out's two criteria (B8), each and together, as measurements, and take no position on what
  counts as scalar strengthening.
- B2 is superseded in part by B10; its definitions of the two conditions stand.

#### 2. Sites that take the position, or read the conditions as a verdict

Found by searching both notebooks for criterion, verdict, scalar implicature, sufficient,
strengthen, stipulat, "we take / adopt", "counts as". Line wording is quoted in short.

##### Text cell 4 Part C (the core)
- The opening: "**C** asks whether the network produces a scalar implicature. The question needs an
  operational form, and we adopt one."
- **The criterion** paragraph: "We take scalar strengthening to be the conjunction of two
  conditions", "Neither is sufficient alone", with the argument for each; "every verdict below is
  relative to it".
- "**The criterion is not met under the default Gaussian prior.**", "toward the criterion without
  reaching it", "the verdict can be shown in the dynamics".
- "commitments anyone reading that outcome as scalar implicature thereby takes on" and the two
  commitments' framing; "A reader who wants scalar strengthening to follow …".
- The closing section: "the conjunction is reached … without an alternatives space" reads the
  conjunction as the target. The user's sentence on alternative competition is the user's own and is
  not a site.

##### Text cell 4, other parts
- *Integration cost*: "how much of it the criterion actually needs", "How much of θ_u\* the
  criterion needs", "the θ_u its verdict needs", "So Part C's verdict is demonstrated in the
  dynamics", "the verdict *at θ_u\**", "how much machinery a scalar implicature should need".
- Text cell 4b: "moves … away from the criterion"; "the prior overriding the entry as well as the
  criterion".

##### Text cell 3
- "the θ_u\* the evaluation's criterion turns out to need"; "the criterion it is judged by is one";
  "the criterion Text cell 4 adopts is met at a …".

##### Text cell 5
- "The criterion adopted in Text cell 4 Part C is not a contrast between …"; "an implicature under
  that criterion".

##### Text cell 6
- "not a second criterion, since the criterion is stipulated on the raw …"; "both verdicts are …";
  "The cells where the criterion is met"; "the θ_u the criterion itself needs"; "the criterion it
  serves is a stipulation of …"; "the θ_u its verdict needs".

##### Appendix B
- "the baseline the criterion is measured against"; "the criterion it is judged by is met at a …".
  (The literature summary on strengthening, Gazdar, Levinson, Sauerland, is description, not a site.)

##### Appendix C
- §1 title "Two readings of the criterion"; "This is Part A's criterion" (Appendix C's own sense,
  to check); "This model's verdict is that the gap …" (Horn's gap; a different sense, to check).

##### Printed lines, Code Cell 2 (mirrored in E2)
- `SCALAR IMPLICATURE PROBE` header.
- "Under the criterion of Text cell 4 Part C, the conjunction, the criterion is met / NOT met";
  "Whether the criterion is met is a measurement; what meeting it commits …"; "the same criterion is
  met by other utterances too".
- "(a scalar implicature for \"some\" requires a NEGATIVE shift)".
- "Whether it is met is therefore NOT a property of the model alone … criterion as much as about the
  model".
- "Ascending F~ moves the shift DOWN, toward the first condition …", "the criterion: raising
  |theta_u| amplifies …".
- "Part C's verdict does not wait for it."
- Function name `updates_to_criterion` (a name, not printed; decide whether it matters).

##### Printed lines, Code Cell 2b (mirrored in E2b)
- "This is the case the criterion is under the most pressure in"; "AWAY from the criterion".

##### Not sites
- "sufficient" in Text cell 3 (μ_u ≠ 0 necessary, not sufficient), Reporting statistics ("the
  nonlinearity is sufficient"), Text cell 5 and Appendix C (m = 2 sufficiency): unrelated senses.
- "stipulation" in Appendix A (Eq. 8 a consequence, not a stipulation): unrelated.
- References.

#### 3. What a revision would do (proposal of 2026-09-14, SUPERSEDED by C7 and §4)

- Replace "criterion" by "the two conditions" (and "the delta read-out's two criteria" stays B8's
  name only if the user wants "criteria" kept for those), and "met/verdict" by "holds / does not hold".
- Part C's criterion paragraph becomes a definition of two reported conditions with what each
  measures, without "we take scalar strengthening to be" or "neither is sufficient alone"; the
  arguments for requiring both move to the paper.
- The commitments paragraph keeps its measurements (prior and strength dependence, the mechanism) and
  drops the framing that they are commitments of an implicature reading.
- Printed lines follow the same wording; E2/E2b mirror; both notebooks re-executed.

#### 4. The wording pass (T1, 2026-09-14, under C7)

Checkpoint 7854b8f. Script `c7_rename.py` (every replacement asserted exactly once; main cells and
their appendix E mirrors patched together), filed with its run output in `agent/audits/2026-09-14-no-position/`.
Executed together with `delta_criteria_printing.md` T1: main 0 errors, 8 figures, 14/14; appendix_E 0
errors, 5 figures, E2 18/18, E3 PASS (202 and 233 lines identical), E4 unchanged; ToC 72 links resolve.
Every changed output line is a C7 rename, the T1 block, or Code Cell 3's "requirement".

- [x] **Applied.**
  - **Names.** Every criterion-sense "condition" became the q shift / q position criterion (Part C,
    Part D, Text cell 4b, Text cell 6, *Integration cost*, Text cells 3 and 5, Appendix B), or
    "criteria"/"both q criteria" for the pair. Table headers "first | second" became "q shift | q
    position". Printed lines in Code Cells 2, 2b and 4 (and E2, E2b) follow.
  - **Stance.** Part C's "We take scalar strengthening to be the conjunction … Neither is sufficient
    alone" is replaced by definitions of the shift and position criteria, the facts about what each
    can be met by, and the user's sentence verbatim ("nether" read as "neither"). "we adopt one" became
    "Part C states two criteria"; "adopts" / "judged by" became "reports"; "every verdict below is
    relative to it" became "everything reported below is relative to them".
  - **Printed position line removed.** "(a scalar implicature for "some" requires a NEGATIVE shift)"
    now reads "(the q shift criterion for "some" is a NEGATIVE shift)"; the probe's "what meeting it
    commits the model to is argued in Text cell 4 Part C" now reads "this notebook takes no position on
    how they should be interpreted".
  - **The delta read-out's criteria defined in Part D** (new paragraph after the peak paragraph): the
    mode shift and mode position criteria, not assumed to agree with the q criteria, no position.
    T1's printed block uses the four names.
  - **"verdict"** removed everywhere: prose ("result", "what Part C reports", "the conjunction"),
    Appendix C ("This model's answer"), and the identifiers in Code Cell A (`outcome`) and E3
    (`passed`, `strong_passed`), none of which printed the word.
  - **Unrelated senses of "condition" renamed** where a reader could confuse them with the criteria:
    "standing condition" → "standing requirement" (Text cell 3 §9.1 heading and ToC, Appendix B,
    E.3); "stationarity condition" → "stationarity equation" (Code Cells 1, 2, E1, E2, Text cell 5,
    Appendix B); "fixed-point condition" → "fixed-point equation" (Appendix A); "the exact condition",
    "a condition on direction", "Appendix B's condition", "the full condition" → "requirement" (Text
    cells 3 and 5, Code Cells 1 and 3, E1); "three conditions" of §8's proofs → "three assumptions";
    "Two conditions can be asked of B" → "Two requirements" (Appendix C); "the flat condition" → "the
    flat prior" (Part D, Text cell 6, Code Cell 2); the pseudocode's "conditions how much" → "sets how
    much"; Code Cell 4's `floor(condition, …)` parameter → `holds`.
- **Kept, as fixed technical compounds** (agent, pending user confirmation): "condition number" (Text
  cells 3 and 4, Code Cell A), "boundary condition" (Code Cell 1, E1), "truth-conditional" (Text cell
  3), "a conditional" (Text cell 3 §8.6), "conditioning" (literal conditioning; the *Integration cost
  and conditioning* heading and its references), "precondition" (Code Cell 2b and E2b comments).

*Full original:* `git show 98c2df8:procedure_records/b10_no_position.md`

---

<a id="r9" name="r9"></a>

## 9. Side quests: the mirrored inventory, and the number of atoms

*Was* `procedure_records/side_quests_mirror_and_granularity.md`

**Opened** 2026-09-15 21:53 · **Closed** 2026-09-22 13:35 · 4 commits

**Settled** O9 (settled), O10 (settled), O1

**Opened by**

> Now there are two side quests we want to ask:
>
> 1. we have that the O corner {1} is non-representational. Another question we want to follow: is
>    {1} as representational as {0}? That is, if we have an inventory of three {no, notall, all},
>    will it behave exactly like a mirrored version of the current {no, some, all}?
> 2. if our predicates have three atoms instead of ten, with corresponding K and theta_L, would some
>    essential results be different? What is there is exactly two atom, will the model become
>    degenerate?
>
> ---
> …

#### 3. Findings

- **F0 (a bug in the first pass, and what caught it).** The first `mirror_equivariance.py` wrote
  `torch.eye(m) + sigma_u * theta**2 / S`, which adds the scalar to *every* entry, where
  `closed_form_fixed_point` writes `torch.eye(m) + sigma_u * theta**2 * gram / S`. The off-diagonal
  entries do not commute with P below, so the mirror appeared broken by 3.7e+03 while θ_u\* matched
  to 4e-14. Fixed by carrying the Gram matrix, and a validation against
  `closed_form_fixed_point` (now 0.00e+00) was added so the same class of error cannot recur.
  Lesson for later probes: **validate any reimplementation against the cell it reimplements before
  reading anything off it.**

##### Side quest 1

- **F1 (the architecture is exactly mirror-symmetric).** Write R for ζ → −ζ on the grid and
  P = diag(−1, +1) on the (tilt, width) coordinates. Then Rb₁ = −b₁ and Rb₂ = +b₂ (to 4e-17), so
  RB = BP, and since W is symmetric under R, BᵀWR = P BᵀW. The reflection pairs the inventories
  utterance by utterance, Rχ_no = χ_all and Rχ_some = χ_not all, **exactly** (0.00e+00). It follows
  that the model built on (inventory, ℓ₀, μ_u) and the model built on
  (mirrored inventory, Rℓ₀, Pμ_u) are reflections: same θ_u\*, and φ_S\* and φ_u\* related by R and
  P. Measured worst discrepancy **7.11e-15** under N(0,1), **7.11e-15** under Beta(3,1) ↔ Beta(1,3),
  **1.14e-13** under Beta(64,1) ↔ Beta(1,64).
- **F2 (so the answer to "is {1} as representational as {0}" is yes, exactly).** Nothing in the
  representation prefers {0}. Appendix C §4's rectangle is the finite statement of it; F1 is the
  statement for the whole model.
- **F3 (but the model is not mirror-symmetric, and μ_u is the only reason).** Of the ingredients,
  the grid, W, b₁, b₂ and the default ℓ₀ = N(0,1) are all R-invariant or of definite parity.
  **μ_u = 1 = (1, 1) is not**: Pμ_u = (−1, +1) ≠ μ_u. So running the mirrored inventory at the
  stipulated μ_u is *not* the mirror. θ_u\* is −28.4375 on {no, some, all} against −19.7219 on
  {no, not all, all}; under Beta(3,1) ↔ Beta(1,3) it **changes sign**, +55.0081 against −17.0332.
  A5 records μ_u = 1 as a stipulation with no target to be derived from, so this asymmetry is
  stipulated rather than motivated.
- **F4 (the fields barely notice, and Appendix C §8 says why).** At the stipulated μ_u the settled
  fields differ by only 4.98e-02 (Gaussian) and 5.67e-02 (Beta(3,1)), despite θ_u\* differing by
  8.7 and by a sign. Eq. (24)'s limit k → c/2 is independent of θ_u, sign included, and every
  configuration here is deep in that regime. So the mirror breaks in the **learned parameter**, and
  the settled field is nearly insensitive to the break.
- **F5 (the criteria read the same on each side).** Reading each inventory's scalar member against
  its own region — *some* against the all-region, *not all* against the no-region — gives shift
  +0.0008 against +0.0009 and position 0.0025 against 0.0025, so both give the same verdict on both
  q criteria. (The q shift criterion is not met under the default Gaussian; that is the prior, not
  the mirror, and matches what Part C already reports.)

##### Side quest 2

- **F6 (n enters in exactly one place).** `theta_L = log(2 * num_atoms - 1)` is the only use of n in
  code cell 1, and `num_atoms` is then recovered *from* θ_L, so θ_L is the real quantity and n its
  denotation (Eq. A5). **K does not track n**: Text cell 3 §1 and I6 make K an accuracy parameter
  for the quadrature, not a state space, so "three atoms with corresponding K" overstates what has
  to move. θ_L < grid half-width caps n at 201.
- **F7 (nothing structural moves).** At n ∈ {2, 3, 4, 10, 50, 100} the three χ_y have rank 3 and
  rank 2 modulo the constant, so by Eq. (C2) there are still two thresholds and **m = 2 stays
  exactly right**. θ_u\* moves smoothly and keeps its sign: −32.5731 at n = 2 to −19.1884 at
  n = 100.
- **F7 qualified, 2026-09-22 (T14).** The smoothness clause is a property of **N(0,1)**, not of the
  model. Sweeping all four `BASE_WORLD_PRIORS`, θ_u\* under the **flat** prior at Λ = 8 runs
  −1082.011 at n = 2, +2510.809 at n = 3, +5950.626 at n = 10, −3322.896 at n = 11: it is not
  monotone and **not bounded**. Eq. (B2)'s two roots have the constant product −S/σ_u, so θ_u\*
  diverges exactly where ⟨μ_u, Σ_y c_y⟩ vanishes, and that coupling changes sign twice along the
  ladder. This is **Appendix B's degenerate ray, reached by varying n alone**. The rank and m = 2
  results of F7 are untouched. Code Cell A now prints the coupling beside θ_u\*.
- **F7's qualification corrected the same day, 2026-09-22.** As first written it added "and
  `theta_u_stationary_points` guards only exact zero, so nothing flagged it". **That was wrong on
  both halves.** Appendix B states the requirement exactly — "what Eq. (B2) actually needs is
  ⟨μ_u, Σ_y c_y⟩ ≠ 0, which is strictly stronger" — and the large θ_u\* values were already
  printed by Code Cell 2 and Code Cell 4 and quoted in the appendix (−557.67 to +12228.42;
  +5950.63 under flat at Λ = 8), so there was no C6 violation and no undocumented hazard. The
  agent overstated a documented feature as an oversight. **What actually stood**, and is now in
  Appendix B and A5: the appendix's −40.9119 is the *default* configuration's margin quoted as a
  general reassurance, the ray is reachable by varying **n** with μ_u fixed (its framing is about
  μ_u's orientation), and the large values are **poles** rather than points in a continuum. **And
  the ray is harmless**, for a reason the appendix did not state: φ_S\* converges to one limit as
  |θ_u| → ∞ from both signs (2.290e-06 apart at 1e6, gap ∝ 1/|θ_u|), so the readings cross it
  continuously — measured at n = 8…15 under flat at Λ = 8, both q readings monotone and neither
  criterion changing status. Printed by `degenerate_ray_report`, Code Cell B.
- **F8 (n = 2 is not degenerate; n = 1 is).** At n = 2, θ_L = 1.0986, the cell of s = 0 is
  s ≤ 0.25 and the cell of s = 1 is s ≥ 0.75, χ_some ≠ χ_all, and 19 grid nodes lie strictly
  between the thresholds. The two thresholds stay distinct, so the span is unchanged. Degeneracy is
  at n = 1, where θ_L = 0 and the entries for *some* and *all* coincide; the constructor already
  rejects it.
- **F9 (but the reported criteria do move with n, and they cross).** This is the substantive answer
  to "would some essential results be different", and it is yes. For *some*:
  - under N(0,1), the **q shift** criterion is not met at n = 2…20 and **is met at n = 50**;
  - under Beta(3,1), the **q position** and **mode position** criteria are not met at n = 2, 3 and
    **are met at n ≥ 4**, and the **q shift** criterion is not met at n ≤ 10 and **met at n ≥ 20**.

  So n = 10 is not a neutral choice of units: it sits on one side of two crossings under a prior
  the notebook runs. This makes **O1 consequential** rather than cosmetic.
- **F9 extended and qualified, 2026-09-22 (T14, Code Cell A).** The sweep now covers all four
  `BASE_WORLD_PRIORS` at Λ = 8 **and** Λ = 512 — 80 rows — and every row prints all four criteria.
  F9's own readings all survive. Three things it did not say, and the prose must:
  1. **Magnitude.** F9 wrote "crosses at n = 50" under N(0,1) without the size of what crosses. The
     q shift there falls **+1.017e-01** at n = 2 → **+2.966e-06** at n = 20 → **−7.593e-07** at
     n = 50: the change of status is the **sign flip of a quantity decayed five orders of
     magnitude**, not a substantive change in what the model reports. Contrast *skewed high* at
     Λ = 512, where the same criterion changes status at **−9.546e-02**. These are not findings of
     equal weight and F9 presented them as one kind.
  2. **A ladder brackets, it does not locate.** "Crosses at n = 50" means *not met at 20, met at
     50*; the change lies somewhere in (20, 50]. No rung measures where it happens.
  3. **The crossings do move with Λ**, which §4 listed as unchecked. The q shift criterion changes
     at n = 50 under three priors at Λ = 8 and by n = 15 or n = 10 under all four at Λ = 512; the
     q position criterion, met at every rung under N(0,1) at Λ = 8, fails at n ≤ 5 at Λ = 512.
     **Granularity and lexical strength are not separable** in what the evaluation reports.

  Two further facts the wider sweep produced. The **mode shift** criterion is met in **one row of
  the eighty** (*skewed low*, Λ = 8, n = 201): the peak of φ_S\* otherwise sits above ℓ_0's peak
  whatever the q criteria say. And **q position and mode position agree in 79 of 80 rows**,
  disagreeing only at *flat*, Λ = 8, n = 2.
- **A measurement limit found at T14.** χ_y is a threshold on the grid, so two n whose
  θ_L = log(2n − 1) fall between the same two grid nodes give the **same network but for θ_L**:
  n = 12 and n = 13 return byte-identical rows. n is resolved only as finely as the grid resolves
  θ_L. No rung of the published ladder collides, so nothing printed is affected.
- **F10 (separation is best near n = 15).** The minimum κ separation over the three utterances rises
  from 0.70917 at n = 2 to a maximum **1.49027 at n = 15**, and falls to 0.05999 at n = 201. The
  implementation's n = 10 gives 1.44196, near the peak.
- **F11 (a latent divergence between code and Eq. (A1), noticed, not changed).** Eq. (A1) writes
  E_some ↦ {ζ ≤ −θ_L}, non-strict. `exclusion_indicator` computes `margin = -(zeta + theta_L)` and
  excludes where `margin > 0`, i.e. ζ < −θ_L, **strict**; its own docstring states the non-strict
  form, so the code disagrees with both the docstring and Eq. (A1). At a node lying exactly on
  −θ_L, χ_no and χ_some would both be 0 and χ_no + χ_some = 1 would fail there, which Appendix C §2
  and Eq. (C1) rely on. Prose defines and code implements (`agent/agent.md` §3), so the code is the side
  that is wrong. **Left for the user** (§5.4): it is a code cell, and outside the scope of these two
  questions.
- **F11 corrected, 2026-09-16.** F11 as first written said the divergence was "invisible today: no
  integer n in [2, 201] puts a grid node on a threshold". **That was wrong**, and the error was in
  the scan, not the arithmetic: it swept only θ_L = log(2n − 1) for integer n and the K ladder, and
  never covered the *explicit* θ_L values the notebooks pass. Code Cell 4's
  `override_threshold(boundaries=(1.0, 2.0, 3.0))` puts **θ_L = 3.0 exactly on node 25** of the
  K = 101 grid. The divergence was therefore live in a table the notebook prints, and fixing it
  (decision I13) moved that row's θ_u\* from 14946.06 to 14937.23 and Text cell 6's quoted range
  from "13378 to 14946" to "13378 to 14937". Lesson, beside F0: **a static scan for literals is not
  a reachability test.** The authoritative check is a full printed-output diff of both notebooks
  before and after, which is exhaustive over everything they actually compute.

*Full original:* `git show ab4840d:procedure_records/side_quests_mirror_and_granularity.md`

---

<a id="r10" name="r10"></a>

## 10. exclusion_indicator: χ_some as the complement of χ_no

*Was* `procedure_records/exclusion_complement_fix.md`

**Opened** 2026-09-16 08:23 · **Closed** 2026-09-17 11:43 · 3 commits

**Settled** I13

**Opened by**

> let's look into 2. Why is it that the code defines < instead of <=?
> good. go with the complement fix

#### 1. The divergence

Eq. (A1) writes E_some ↦ {ζ ≤ −θ_L}, non-strict. `exclusion_indicator` computed
`margin = -(zeta + theta_L)` and excluded where `margin > 0`, i.e. the strict ζ < −θ_L. Its own
docstring stated the non-strict form, so the code disagreed with both the docstring and Eq. (A1).

**Why it read that way.** The function computes a signed margin and applies one shared
`margin > 0` to all three entries. That factorization exists for the `sharpness` branch, which
feeds the margin to a logistic and never compares it. Two of three entries are strict in Eq. (A1),
so the shared test gets them right; *some* is the only non-strict one, and it was the one built as
the **negation** of another entry's margin. Negating a margin and re-applying a strict test gives
`<`, never `≤`. The strictness was inherited from the factorization, not chosen.

Present since the initial snapshot 499918c and never edited; the docstring carried the correct `≤`
from that same commit.

#### 2. Why the complement form, and not `margin >= 0`

Both match Eq. (A1). The complement form was chosen because it keeps one shared comparison and one
shared smooth map, and makes χ_no + χ_some = 1 exact **by construction** — the identity Appendix C
§2 and Eq. (C1) rest on — rather than as something that happens to hold away from the boundary.
Its only cost is that 1 − σ(x) and σ(−x) differ in the last ulp: worst 2.22e-16, inside the 1e-12
zero band (I5) and invisible at four printed decimals.

A uniform *test* is not achievable anyway: Eq. (A1) mixes one closed region with two open ones, and
one comparison cannot express that. The old uniformity was bought by getting one entry wrong.

#### 3. Tasks

- [x] T0 (2026-09-16): checkpoint be47516. The tree carried one uncommitted line in `main.ipynb`
  cell 18, the user's; folded into this change's commit at their direction.
- [x] T1: `agent/audits/2026-09-16-exclusion-complement/acceptance.py`, run **before** applying.
  ACCEPTANCE PASS.
- [x] T2: `apply.py --apply` patched `main.ipynb` cell 5 and `appendix_E.ipynb` cell 2, one site
  each. Writer round-trip verified byte-identical first, so nothing outside the hunk moved. The two
  copies remain IDENTICAL.
- [x] T3: both notebooks re-executed, main first (E3 reads its stored outputs).
- [x] T4: Text cell 6's quoted θ_u\* range corrected, 14946 → 14937 (C6).
- [x] T5: decision I13; F11 corrected in the side-quest record; this record.

#### 4. Verification

- Acceptance, before applying: step branch identical to the old function over 3000 shipped
  configurations (K ladder × n ∈ [2, 201] × three utterances); smooth branch within 2.22e-16;
  *no* and *all* bit-identical. At a grid with a node on the threshold: old χ_some = 0 where
  Eq. (A1) requires 1, new χ_some = 1; χ_no + χ_some = 1 exact; Eq. (C1) residual 3.0e-02 → 3.3e-16.
- Acceptance against the **patched** notebooks: same results, and the default network still learns
  θ_u\* = −28.437487, matching the settled value.
- `main.ipynb` 0 errors, 8 figures, 14/14, 249 s. `appendix_E.ipynb` 0 errors, 5 figures, E2 18/18,
  E3 PASS, 672 s. Both within the §5.1 baseline.
- Printed-output diff against be47516: `appendix_E` 0 differing lines; `main` 2, being the one
  θ_u\* value in Code Cell 4's override-threshold table. All 13 figures byte-identical.

#### 5. Findings

- **F1 (the fix was not output-neutral, contrary to what was first reported).** The agent told the
  user the change would alter nothing printed, on the strength of a scan that swept θ_L = log(2n − 1)
  for integer n and the K ladder. That scan never covered the explicit θ_L values the notebooks
  pass. `override_threshold(boundaries=(1.0, 2.0, 3.0))` puts **θ_L = 3.0 exactly on node 25** of
  the K = 101 grid — the only such coincidence in either notebook. That row's θ_u\* moved
  14946.06 → 14937.23, stable across the six preceding commits, so the move is the fix and not
  run-to-run noise. **The new value is correct**; the old was computed with χ_some = 0 where
  Eq. (A1) requires 1.
- **F2 (the general lesson).** A static scan for literals is not a reachability test — it gave a
  false all-clear three times here. The authoritative test is a full printed-output diff of both
  notebooks before and after.
- **F3 (noticed, not changed).** The notebooks carry two conventions at the top of the scale:
  `zeta > theta_L` for Eq. (27)'s all-region q-mass, and `zeta >= theta_L` for "the cell of *all*"
  (the mode-position criterion, Code Cell C's *not all*). After I13, 1 − χ_all = {ζ ≥ θ_L} agrees
  with the second. The residual tension is that Eq. (27)'s all-region is strict while its own gloss
  reads "where *all* is true", which is the closed cell. Same class of latent issue, in prose, and
  out of scope here. Recorded as open decision O11 on 2026-09-17, with both options and the measured
  cost of each. **Settled by the user the same day** in favour of the closed form: Eq. (27)'s
  all-region is now R = {ζ ≥ θ_L}. See `all_region_closed.md`; no printed number moved.
- **F4 (a coupling `agent/agent.md` §2 did not list).** Code cell 1 and Code Cell E1 both define
  `exclusion_indicator`, byte-identically, and §2's list covered Code Cell 2 ↔ E2 but not this pair.
  **Added as coupling 9 on 2026-09-17**; F6 gives the true width of the duplication.
- **F5 (the fragility, quantified 2026-09-17).** θ_u\* at the override threshold is a **staircase**
  in θ_L: flat between grid-node crossings and stepping about 1.3% at each. At Λ = 4413.6 under
  Beta(1024, 1), the crossings at 2.88, 3.00 and 3.12 give 15125.82, 14937.20, 14745.80 and
  14551.38. θ_L = 3.0 sits exactly on a crossing, which is why a boundary convention decided it.
  Pre-fix it returned 14946.04 — matching **neither** neighbouring plateau, because node 25 was
  owned by neither entry; post-fix it returns 14937.20, the plateau below, owned by exactly one,
  Eq. (A1)'s `≤` making the staircase left-continuous. The printed value is therefore exact for the
  stated θ_L and grid, but it moves about 1.3% per grid node, so it reflects the grid's resolution
  as much as the threshold's. Whether to nudge the boundaries off the node, or to quote fewer
  figures, is the user's call.

- **F6 (the duplication is far wider than one function).** Checking F4 properly: appendix_E's Code
  Cell E1 shares **878 of code cell 1's 912 lines**, and every `def` in main appears verbatim in E1,
  which adds only `relay`, `relay_loop_abscissa` and `theta_u_gradient_columns`. Nothing in the
  project diffs the two. Added to `agent/agent.md` §2 as coupling 9 on 2026-09-17.

*Full original:* `git show ace8204:procedure_records/exclusion_complement_fix.md`

---

<a id="r11" name="r11"></a>

## 11. Eq. (27)'s all-region becomes closed

*Was* `procedure_records/all_region_closed.md`

**Opened** 2026-09-17 11:43 · **Closed** 2026-09-17 11:56 · 2 commits

**Settled** O11 (settled), O12 (opened)

**Opened by**

> For 3, the formula needs to be changed. Can you inspect the scope of that change before
> implementing?
> for 1, we will fix this redundancy later, record and don't do anything about it yet. For 2, leave
> it. Now go ahead and implement the changes.

#### 1. The disagreement, and which side was wrong

Text cell 4 defined P(all-region) over the **open** R = {ζ > θ_L} while glossing it "where *all* is
true". *all* excludes E_all = {ζ < θ_L} (Eq. A1), so it is true on the **closed** {ζ ≥ θ_L}. The
formula and its own gloss disagreed at the single node ζ = θ_L. Everything else in the notebook
already took the closed form: the cell of *all*, Code Cell C's χ_not all, P(no-region). The user
ruled that the formula was the wrong side.

#### 2. Scope, as inspected before implementing

| What | Count | Where |
|---|---|---|
| mask sites | **23** | main cells 7 (7), 9 (2), 11 (1), 13 (2), 19 (2); appendix_E cells 3 (7), 4 (2) |
| printed labels | **3** | main c7 and E c3 column header; main c19 legend |
| prose | **2** | Text cell 4: the Eq. (27) definition, and "the region ζ ≥ θ_L is s ≥ 0.95" |
| must not change | **11** | the cell-of-*all* masks, already `>=`; plus `lower_region`, already `<=` |

Mirror pairs moved together: main cell 7 ↔ E2, main cell 9 ↔ E2b (I11). Cells 11, 13 and 19 are not
mirrored.

#### 3. Tasks

- [x] T0 (2026-09-17): checkpoint e10f002, tree clean.
- [x] T1: `agent/audits/2026-09-17-all-region-closed/acceptance.py`, run **before** applying. PASS: the
  site counts match the scope, and the open and closed masks agree on all 55 (θ_L, K) combinations
  the notebooks use — while differing, as expected, at θ_L = 3.0 on K = 101.
- [x] T2: `apply.py --apply`, every edit count-asserted, writer round-trip checked byte-identical
  first. 14 + 9 masks, 2 + 1 labels, 2 prose.
- [x] T3: both notebooks re-executed, main first.
- [x] T4: O11 settled; B2 given a dated finding; O12 recorded; this record.
- [x] T5 (2026-09-17): O12 resolved, on the user's instruction. Prose: Text cell 4 Part C states the
  identity once; Part D refers to Part C instead of re-deriving the cell. Code: both `upper_region`
  and `inside` kept, with a comment at the canonical declaration of `upper_region` (Code Cell 2's
  `demonstrate`, mirrored in E2). Acceptance: every code cell compiles; the only source changes are
  markdown in cell 6 (+7 −5) and three comment lines in each notebook; stored outputs byte-identical.
  **Notebooks not re-executed** — the sole code change is a comment, which cannot move any output
  (the precedent is T1 of `o5_o6_resolution.md`).

#### 4. Verification

- Source diff against e10f002: **18 changed lines in main** (14 masks, 2 labels, 2 prose) and
  **10 in appendix_E** (9 masks, 1 label). Nothing else moved; `lower_region` and the Code Cell 2b
  comment are untouched.
- `main.ipynb` 0 errors, 8 figures, 14/14, 240 s. `appendix_E.ipynb` 0 errors, 5 figures, E2 18/18,
  E3 PASS, 703 s. Both within the §5.1 baseline.
- Printed-output diff against e10f002: **no numeric change anywhere**. The only differing lines are
  the 5 printed occurrences of the two relabelled headers (main cells 7, 9, 19; appendix_E cells 3,
  4). All 13 figures byte-identical.

#### 5. Findings

- **F1 (the change is inert, and why).** No grid node lands on +θ_L for any θ_L the notebooks use —
  log 19, the explicit 2.9444, and log(2n − 1) across n — at any K in the ladder. The one
  node-on-threshold configuration, `override_threshold`'s θ_L = 3.0, takes its leak from χ_no and
  never computes an all-region mass. So the q position criterion reads identically in every
  configuration actually run; only its *definition at the boundary* changed.
- **F2 (a prediction corrected).** The scope said 3 printed label lines would change; 5 did. The
  column header is defined once, in Code Cell 2, but `delta_readout_report` is called from both
  Code Cell 2 and Code Cell 2b, so one source line prints in two cells. Source sites and printed
  occurrences are not the same count.
- **F3 (a third checker written with assumed expectations).** The post-apply check counted every
  `X.zeta >= X.theta_L` and compared against the number of *new* sites, so the cell-of-*all* masks
  that were already `>=` read as a MISMATCH. The edit was correct; the checker was not. This is the
  same failure as F0 of `exclusion_complement_fix.md` and the inverted acceptance expectations
  there. **The form that works is to count the pre-change state and assert new = old + delta**, which
  is what reconciled it. Prefer that to asserting an absolute number.
- **F4 (a gating bug in the runner).** The verification block and the two notebook runs were
  sequenced with `;`, so execution proceeded despite the checker reporting FAIL. Harmless here only
  because the edit was right. Use `&&` so a failed check stops the run.
- **F5 (the redundancy this creates).** The all-region and the cell of *all* are now the same set
  with two names and two implementations. Recorded as **O12** at the user's direction, then settled
  by them the same day: resolved in prose, retained in code behind a comment. See T5.
- **F6 (a fifth checker caught a real ambiguity, for once).** The comment insertion first anchored on
  the pair `proportion = logistic(net.zeta)` + `upper_region = ...`, which occurs **twice** in Code
  Cell 2 — in `demonstrate` and in `base_prior_sweep`. The assertion refused to patch rather than
  guessing, and the anchor was moved to the enclosing `def demonstrate(`. Unlike F3 and F4, this is
  the failure mode working as intended: assert the site count, never patch on a non-unique anchor.

*Full original:* `git show 7da49c1:procedure_records/all_region_closed.md`

---

<a id="r12" name="r12"></a>

## 12. The scale-class hypothesis, against Xiang et al. (2022)

*Was* `procedure_records/scale_classes_hypothesis.md`

**Opened** 2026-09-17 13:06 · **Closed** 2026-09-22 16:16 · 16 commits

**Settled** A20, E16, O13, O14; revisions.md T0-T13

**Opened by**

> we have updated the notebook again since we last changed the outlines and revision plans. Can you
> reexamine this matter given the updated data? My hypothesis is that, 1. scalar expressions with
> unstable atomicity are associated with weaker lexical strength; 2. open-scale adjectives behave
> similar to "some"; complete scale adjectives behave similar to endpoint(s)+some. Check
> implications of this hypothesis and see if our prediction under this hypothesis matches Xiang's
> data.

#### 5. Findings

**F1. The empirical profiles, recomputed from the authors' data** (Experiment 3, mean proportion of
choices, positions 1..5):

| class | condition | 1 | 2 | 3 | 4 | 5 | peak | mean position |
|---|---|---|---|---|---|---|---|---|
| maximum | shape | .002 | .007 | .018 | .013 | .960 | 5 | 4.61 |
| maximum | artifact | .018 | .011 | .016 | .026 | .929 | 5 | 4.83 |
| minimum | shape | .019 | .133 | .328 | .276 | .244 | 3 | 3.29 |
| minimum | artifact | .015 | .038 | .111 | .182 | .653 | 5 | 4.42 |
| relative | shape | .007 | .018 | .049 | .174 | .752 | 5 | 4.65 |
| relative | artifact | .052 | .026 | .054 | .186 | .681 | 5 | 4.42 |

**F1 is internally inconsistent, and F3–F5 were scored against absent data. Both corrected
2026-09-22 at T1/T2; `agent/decisions.md` E16 carries the record.**

Two faults, one in the table above and one in the audit that produced it.

1. **F1's two `shape` rows were renormalized and their mean positions were not.** One image set,
   `curved_greenline`, drew **no** Experiment 3 response at all, for both of its adjectives — so the
   maximum class's shape row averages over 15 items of 16 and the minimum class's over 11 of 12, and
   both fall short of summing to 1 (0.9375 and 0.9167). Whoever wrote F1 divided the five cells by
   that sum but left `mean position` alone. The cell values above are therefore right *as
   normalized profiles*; the two mean positions are not. Corrected: maximum/shape is **4.92**, not
   4.61, and minimum/shape is **3.59**, not 3.29. The other four rows were never affected.
2. **The audit scored the model against those 10 rows as measured zeros**, which is a comparison
   against nothing. Dropping them changes the headline numbers materially:

   | | audit (F3–F5) | corrected, printed by Code Cell F |
   |---|---|---|
   | maximum class R² | 0.953 | **0.993** |
   | minimum class R² | 0.401 | **0.434** |
   | q_lit, maximum | 0.952 | **0.992** |
   | q_lit, minimum | 0.092 | **0.103** |
   | minimum class image-type difference, measured | −1.13 | **−0.83** |

   The maximum class crosses from below the published ST (.98) and QF (.97) values to above them, so
   this is not a rounding matter. **Every number F3–F5, F8–F10 record is superseded** by Code Cell F's
   output; what the findings *say* survives, since each contrast keeps its direction.

Note also that the fitted Λ of the minimum class moves from 32 to **48** once the absent rows go —
but the ladder only brackets it between 32 and 48, and Code Cell F prints the bracket rather than
the argmax alone.

**F2. H2's class-to-entry map is the one the data show.** Each class's profile is the profile of the
entry H2 assigns it: the maximum class is concentrated in the top cell; the minimum class is spread
over every cell but the bottom one, which is exactly what {ζ ≤ −θ_L} excludes; the relative class
sits above the midpoint. The paper states the same thing in words (9:27): "for maximum adjectives,
participants consistently chose the maximum degree; for minimum adjectives, the choices distributed
among all the non-minimal degrees; and for relative adjectives, the choices were clustered mainly on
degrees above the mid-point."

**F3. The model reaches the same overall fit as the models in the paper.** On their 96 items, with
their priors, at one Λ for every class, the model's posterior-degree R² is **0.81** (Λ = 16 to 24,
relative cut between positions 3 and 4), against **LG 0.78** and **QF 0.82** (their Table 5).

**F4. By class, the model is level with them on two and behind on one.**

| | max | min | rel |
|---|---|---|---|
| this model (Λ 8 / 32 / 16) | **0.953** | **0.401** | **0.800** |
| LG | 0.94 | 0.55 | 0.69 |
| QF | 0.97 | 0.58 | 0.78 |
| semantic threshold (ST) | 0.98 | 0.19 | 0.58 |
| hybrid | 0.97 | 0.32 | 0.80 |

The minimum class is the residual of every model in the paper, this one included. The authors say so
themselves: "all of the models we have looked at seem to perform weaker on minimum adjectives, there
may be independent sources of difficulties yet to be discovered" (9:45).

**F5. The utility level is what earns the fit on the two non-endpoint classes.** The literal
listener ℓ₀ − φ_L, on the same items and the same Λ, gives **max 0.952, min 0.092, rel 0.200**. The
maximum class needs no utility level at all; the other two gain 0.31 and 0.60 of R² from it.

**F6. Λ per class, which is H1's test.** Each class's R² depends only on its own Λ.
- **max**: rises to 0.953 at Λ = 8 and is then **flat to Λ = 2048**. The data put no upper bound on
  its lexical strength; they are consistent with the hard entry of the Λ → ∞ limit.
- **min**: peaks at **Λ ≈ 32** (0.401) and falls away on both sides, to 0.325 by Λ = 512.
- **rel**: peaks at **Λ ≈ 16** (0.800) with the cut between positions 3 and 4, and falls to 0.756.

So a **finite** Λ is required by the minimum and relative classes and not by the maximum class,
which is H1's content: the class whose threshold is the scale's own endpoint behaves as a hard
constraint, and the two classes whose thresholds depend on something unstable do not. The ordering
of the two finite optima is min (32) above rel (16).

**F7. The relative cut.** Best at the boundary between positions 3 and 4, s = 0.625 — just above the
midpoint, which is where the paper puts the class ("clustered mainly on degrees above the
mid-point"). At s = 0.375 the optimum is Λ = 24 (0.799) and at s = 0.875 it is Λ = 6 (0.781), so the
cut and Λ trade off and neither is identified alone.

**F8. The image-type effect: right class, right sign, far too small.** The authors find one credible
image-type effect, and it is the minimum class's, in both experiments. Shape minus artifact, in mean
scale position:

| | max | min | rel |
|---|---|---|---|
| their elicited prior | +0.84 | −1.12 | −0.00 |
| their Experiment 3 | −0.22 | **−1.13** | +0.23 |
| this model, fitted Λ | +0.03 | **−0.16** | +0.01 |

The model puts the effect in the minimum class and nowhere else, which is the empirical pattern, but
at one seventh of its size.

**F9. Why, and what would fix it.** At the fitted Λ the entry has already overridden the prior, so
the prior's own −1.12 cannot reach the belief. The model reproduces the −1.13 only at **Λ ≲ 2**,
where the minimum class's R² collapses (0.19 shape, 0.005 artifact). Split by condition, the two
halves want different lexical strengths: by mean position, **shapes want Λ ≈ 6 and artifacts Λ ≈ 24**;
by R², the artifact half reaches 0.86 at Λ = 24 to 64 while the shape half reaches only 0.24, at
Λ ≈ 0.5 to 1. **No single Λ fits both halves of the minimum class.**

That is H1 in a sharper, within-class form: the same adjectives carry a weaker lexical strength when
predicated of novel shapes than of familiar artifacts — which is what "unstable atomicity" would
say, since what counts as one bump or one stripe is fixed by familiarity with the object. Nothing
else in the model produces the effect: m = 3 and m = 4 leave it at −0.17 and −0.04 (and m = 4 costs
the minimum class two thirds of its R²), and the utility level's amplification of the span-B
component of ℓ₀ − φ_L (Eq. 24) is what flattens the prior's contribution at any m the basis allows.

**F10. What the minimum class actually does, and the model does not.** Both conditions move the
belief up from the prior by about the same amount — 1.19 → 3.29 and 2.31 → 4.42, +2.10 and +2.11
positions — while the model moves it to a place fixed by the entry and Λ rather than by a
displacement. Reproducing a constant displacement is not something Λ can do at fixed θ\*.

**F11. The between-class interaction §5.2 claims is there, attenuated.** The gap between the maximum
and minimum classes is larger in the shape condition than the artifact condition, in the data
(1.32 against 0.41) and in the model (0.61 against 0.42).

**F12. §5.2's and background §1.7's description of the prior manipulation is backwards.** Both call
shapes the impoverished-prior condition and artifacts the rich-prior one. What the authors report
about the elicited priors is the opposite: "artifacts tend to have a less categorical distribution
than shapes, in particular for the dimensions corresponding to absolute adjectives" (9:19), and
their own data bear it out — the shape priors are the peaked ones: the minimum class's elicited
prior has mean position 1.19 for shapes against 2.31 for artifacts, and the maximum class's 4.36
against 3.52. The shape condition is
impoverished in world knowledge and **sharper**, not flatter, in elicited prior. Whatever §5.2 says
about prior sharpness has to be stated on the elicited priors, not on the labels.

**F13. What no longer stands in §5.2's own terms.** The prediction as written is a monotone trend in
the cut's position under a flat prior, reversing under a sharp one. The comparison the data make is
not that: the three classes differ in **which cut** they carry and in **Λ**, and the prior
manipulation is not a sharpening of one prior but two elicited sets. The 2026-09-14 findings stand
(the numbers were θ_u = 1 controls or a carried θ\*; "monotonically" fails; the tilt carries the
contribution). The parity result about κ is untouched.

**F14 (2026-09-17, for S-2). A relative adjective's cut is not identified by the data.** Best R² for
the relative class, each candidate cut with its own Λ scan: midpoint 0.793 (Λ 16), the item's own
prior median 0.795 (Λ 24), its prior upper quartile 0.797 (Λ 16), cell boundary s = 0.375 0.799
(Λ 24), s = 0.625 0.800 (Λ 16), s = 0.875 0.781 (Λ 6). A spread of 0.019 across every plausible
choice, so **t need not be fitted**: stipulating the midpoint costs 0.007 against the best cut.

**F15 (2026-09-17, for S-7). The parity of the three classes' loadings at n = 4**, κ = BᵀWχ:

| entry | cut (s) | tilt | width | \|width/tilt\| |
|---|---:|---:|---:|---:|
| MAX = *all* | 0.875 | −1.33667 | −0.56936 | 0.426 |
| MIN = *some* | 0.125 | −1.33667 | **+0.56936** | 0.426 |
| REL, cut at the midpoint | 0.500 | −1.49985 | **+0.00000** | 0 |
| REL, cut at s = 0.625 | 0.625 | −1.48785 | −0.17284 | 0.116 |

**The maximum and minimum entries share their tilt exactly and differ only in the sign of their
width**, and a midpoint cut is the one entry with no even component at all (the node on the cut
half-weighted, as the 2026-09-14 numerical note says). An antonym's κ is exactly the negative of the
entry's, to 2.2e-16, since B is orthogonal to the constant.

**F16 (2026-09-17, for S-2). None of H2's inventories forces m = 2.** Every one of them is a
complementary pair, so by Appendix C §5 its span modulo the constant is 1, measured as 1 for all
four tested. The model carries m = 2 as a property of the architecture, not because these
inventories demand it. This is not the collapse Eq. (C3) reports for an odd m = 1 basis: the pair's
two loadings are opposite, not equal, so the utility level is not common-mode on them.

**F17 (2026-09-17, the section as S-2 finally scopes it).** The two absolute classes only, 56 of the
96 items, no cut *t* anywhere. R² of our own predictions against their Experiment 3:

| | max | min | both classes |
|---|---:|---:|---:|
| the model at θ\* | 0.953 | 0.401 | **0.804** |
| the tempered control | 0.951 | 0.208 | 0.789 |
| the literal listener | 0.952 | 0.092 | 0.728 |

So the utility level's whole contribution sits in the minimum class, and the maximum class is
indifferent to it (0.952 against 0.953). Λ scanned per class: max reaches 0.953 at Λ = 8 and is flat
to Λ = 2048; min peaks at 0.401 at Λ = 32 and falls to 0.325. Shape minus artifact in mean scale
position: prior +0.84 / −1.12, data −0.22 / −1.13, model +0.03 / −0.16. The gap between the two
classes: data +1.32 (shape) against +0.41 (artifact), model +0.61 against +0.42.

**F18 (2026-09-17, for O14). The parity of the two entries holds only while one θ fixes both ends.**
κ for *some* at n = 4 is (tilt −1.33667, width +0.56936), fixed by the 0 boundary. Moving the 1
boundary alone, with the 0 boundary held:

| θ_A | cut in s | tilt | width | tilt − tilt(*some*) | width + width(*some*) |
|---:|---:|---:|---:|---:|---:|
| 0.50 θ_L | 0.7257 | −1.45665 | −0.31963 | −0.11999 | +0.24973 |
| 0.80 θ_L | 0.8259 | −1.40626 | −0.45378 | −0.06959 | +0.11557 |
| **θ_L** | 0.8750 | −1.33667 | −0.56936 | **+0.00000** | **+0.00000** |
| 1.25 θ_L | 0.9193 | −1.24788 | −0.66040 | +0.08879 | −0.09105 |
| 2.00 θ_L | 0.9800 | −0.86631 | −0.72692 | +0.47035 | −0.15757 |

The identical tilts and cancelling widths are a consequence of θ_A = θ_L, not of anything else, so
the parity paragraph S-7 keeps is exactly the statement O14's instinct doubts. **This measures what
the symmetry rests on; it does not test the instinct, and nothing here says the symmetry accounts
for the mismatch (R16).**

**F19 (2026-09-17, for O14 and O10). The n = 1 degeneracy is a property of the single θ, not of n.**
Building Eq. (A1) with the 0 boundary at −θ_L and the 1 boundary at θ_A, and taking the Gram rank of
the three χ_y as O10 and Eq. (C2) do:

| θ_L | θ_A | n | rank | rank mod **1** | max \|χ_some − χ_all\| | |
|---:|---:|---:|---:|---:|---:|---|
| log 7 | log 7 | 4 | 3 | 2 | 1.0000 | the model |
| 0 | 0 | 1 | **2** | **1** | **0.0000** | O10's degeneracy: the entries coincide |
| 0 | log 7 | 1 | 3 | 2 | 1.0000 | 0 boundary at n = 1, 1 boundary kept |
| 0 | 0.5 | 1 | 3 | 2 | 1.0000 | both moved, still distinct |
| log 7 | 0 | 4 | 3 | 2 | 1.0000 | the 1 boundary at the midpoint |

So **representationally** the user's instinct holds: separate the two boundaries and n = 1 no longer
collapses *some* into *all*, and the inventory keeps the two thresholds Eq. (C2) counts. The last row
is the configuration in which a relative adjective's cut would be θ_A at the midpoint, with the 0
boundary left where n puts it.

**What this does not settle**, and what keeps it an instinct rather than a result:
- Nothing here is dynamical. The user's instinct is that an architecture with an alternatives level
  has different dynamics; no dynamics were run, and none can be until such an architecture exists.
- **Eq. (A2)'s gain.** θ_L is the gain of g_y as well as a cut, so θ_L = 0 zeroes the word-form
  prediction whatever θ_A does. Whether that survives the separation depends on which θ gains which
  row of A, which is undetermined. It is the one obstacle the rank test does not touch.

**F20 (2026-09-21, for O8). The paradigm detail, read off the paper itself.** Checked against
Xiang, Kennedy, Xu & Leffel (2022), *Semantics and Pragmatics* 15(9), Secs. 2.1.1, 2.2.1 and 2.3.1
(PDF from semprag.org; not copied into the repository).

- **Experiment 2 (truth value).** 48 image sets, each paired separately with each member of an
  antonym pair = 96 items. Artifact and shape items were run on **two separate groups**. The items
  "were distributed in a latin-square fashion such that the same participant did not see both
  adjectives that were paired to the same image set", and "each participant, therefore, only saw 24
  trials total".
- **Experiment 3 (posterior degrees).** "The image sets and adjectives used for this experiment, as
  well as the procedure to pair together the images and adjectives and to distribute them among
  participants, were identical to Experiment 2." Separate groups again (67 shape, 68 artifact).
- **So no participant heard both members of a pair about the same images.** Whether a participant
  met both members across *different* image sets is not stated: each pair was used for two image
  sets, and the paper constrains only the same-image-set case.
- **Experiment 1 (priors) used no adjective at all** — "Which of these is the most likely?", one
  choice per image set, no adjective mentioned. The by-item prior is therefore **adjective-free**,
  which is how the audit uses it; the by-adjective figure averages items for visualization only.
  Scale position 1 is the least and 5 the most of the property, which is the authors' own coding and
  is what "in the adjective's own orientation" means.
- **A lexical detail that does not disturb the ensemble.** A few adjectives sit in more than one
  pair (*short* with *long* and with *tall*; *straight* with *bent* and with *curved*), so the
  partner is not a function of the adjective alone. In this phase's representation it makes no
  difference: any minimum-standard partner of a maximum-standard entry is its complement whatever
  the word is, because the ensemble is fixed by class and one θ, not by lexical identity.

**What F20 settles, and what it does not.** It removes one justification and leaves the conclusion
standing, for the reason the user gave on 2026-09-21: *presence in the inventory follows from
exposure in the experiment, but not the converse* — a participant not shown *plain* in the
experiment has still met it elsewhere. So {χ, 1 − χ} **cannot be argued from experimental exposure**,
since the latin square denies it; it is argued, if at all, from the **inventory a speaker of English
has**, which the experiment neither creates nor limits. §5.2 must say it that way.


- **Q7** in `revisions.md`: three of its four choices are now answerable from measurement, and the
  fourth (the empirical-fit paragraph) needs F12 either way.

- **S-1 — settled, option (ii) in effect but bounded.** "the point of H1 is about a fitted Lambda;
  for H1 and only for H1 this is allowed since it is part of the hypothesis's commitment." So Λ is a
  fitted quantity **here and nowhere else**, because H1 is a claim about Λ, and it is labelled as
  fitted where it is printed. Nothing else in §5.2 or Appendix F may be fitted — which is what makes
  S-2 a live question rather than a matter of fitting *t* too.

- **S-3 — settled.** The data live in the repository.

- **S-4 — settled.** n = 4.

- **S-5 — settled, the opposite of the agent's reading.** "do not print published number; any
  published number should appear in the paper with proper citation; the code is only to print our
  own predictions." So Code Cell F prints the model's own quantities only; their LG/QF/ST/hybrid R²
  values are cited in §5.2's prose, and the by-item R² of **our** predictions against their data is
  ours to print.

- **S-6 — settled.** The word budget rises as needed.

- **S-7 — settled, the agent's recommendation.** The parity paragraph stays in §5.2, restated for
  n = 4, with its numbers printed by Code Cell F. Under the scope S-2 sets, what it states is that
  **the maximum and minimum entries differ in the even (width) coordinate alone**: their tilts are
  identical to 0.0e+00 and their widths sum to 0.0e+00 (F15, F17e). The general parity statement —
  that a cut at the midpoint of the log-odds scale would carry no even component at all, measured
  1.2e-17 with the node on the cut half-weighted — is kept as a statement, not as a modelled class.
  The old ratios 0.219 / 0.633 / 1.07 go with the old prediction; they were n = 10 cuts.

- **S-2 — settled: the relative class is not modelled.** The user's reasoning, verbatim
  (2026-09-17):

  > even though we currently model the two endpoint as symmetric to each other, I do not think it is
  > actually the case. Recall our motivation for an alternatives level; under this proposed
  > architecture, the 0 and the 1 would no longer be defined by the same theta, but instead theta_L
  > and theta_A. I think our current model's symmetricity is the culprit of mismatch that we have
  > with Xiang's data. My instinct is that n can be properly represented by the architecture
  > (particularly as one of theta_L or theta_A) once the two thetas are separated from each other.
  > However, we want to avoid making too many promises in the paper over things we haven't
  > implemented yet, so my take is that we point to this intinct and leave it as an instinct. Thus,
  > we do not try to model the relative class with our current implementation.

  And the clarification that followed, verbatim:

  > I need to clarify that theta_L is the lexical level's property, and only theta_A is meant to be
  > the alternative level's property. The lexical level infers the boundary of 0, and the
  > alternative level infers the boundary of 1.

  And the correction that followed, which is what the instinct is actually about:

  > I'm sorry for mispeaking earlier, but I meant the midpoint t of the relative class can be
  > properly represented by one of theta_L or theta_A. As for n, we my instinct is that it is still
  > dependent on theta_L. However, since an architecture with an alternatives level has different
  > dynamics, it is well possible that n=1 no longer causes degeneracy.

  So the quantity the separation would represent is **t**, the relative class's midpoint, not n; n
  stays with θ_L. S-2's decision is unchanged: the relative class is not modelled here.

  Recorded as `agent/decisions.md` **O14**. What follows for this change:
  - **No cut *t* enters the model.** Appendix A's identification argument and its "θ_L enters twice"
    paragraph are untouched, and the objection that motivated S-2 does not arise.
  - **§5.2 still states H2 in full** (the user's first instruction) and says plainly that its
    open-scale half is not tested here, pointing to the instinct. It must not report the relative
    class's 0.80, since that number comes from a configuration the model does not have.
  - **The instinct is stated as an instinct**, once, with no promise attached and no claim that it
    accounts for the mismatch. Placement: the agent recommends the close of §5.2, pointing back to
    §5.1 where an alternatives level is proposed, since θ_A is the quantity that would need a level
    to carry it. Confirm the placement at T10. §5.1 itself gains nothing: naming θ_A among what the
    level "would have to supply" would turn the instinct into a promise.
  - **The parity paragraph is where the symmetry the instinct doubts is actually stated**, which is
    why S-7 keeping it matters more under this scope than it did before.


- **S-1. Is Λ fitted, and if so what class of quantity is a fitted Λ?** The section's Λ numbers come
  from choosing, per class, the Λ that best matches their data. Nothing in this project is fitted;
  the four classes of `agent/agent.md` §3.3 have no room for a fitted parameter, so a quoted best-fit Λ is
  class (e) as things stand. Options: **(i)** quote the whole Λ scan and no single value, which
  keeps §5.2's standing "no fit is offered" sentence true and still carries F6's result (a finite Λ
  is required by two classes and not by the third); **(ii)** declare a fitted quantity as a fifth
  class in `agent/agent.md` §3.3 and record each fitted Λ under it; **(iii)** fix Λ = 8 for every class,
  which loses F6 and most of F4. The agent's reading is that (i) is the only option that leaves the
  rest of the paper's standards intact, but the choice is the user's.

- **S-2. Does the relative class enter at all?** A relative adjective's cut *t* is neither an
  endpoint nor 1/2n, so it is a quantity of the entry that Text cell 3 §2's inventory does not have,
  and Appendix A's identification argument is written for a θ_L that is both the gain of Eq. (A2)
  and the cut of Eq. (A1). Options: declare *t* (which opens A5 and Appendix A's "θ_L enters
  twice"); or restrict §5.2 and Appendix F to the two absolute classes, losing H2's open-scale half
  and the .80 that is the model's best class after the maximum one.

- **S-3. May their data live in the repository?** R² is a statistic of the model **against their
  data**, so Code Cell F cannot print it unless the data are present. Options: **(i)** commit the
  34 KB derived aggregate (96 items × 5 positions: elicited prior, Experiment 3 posterior,
  Experiment 2 judgment, class) with a README giving provenance, licence (CC-BY) and sha256, and
  have Code Cell F read it; **(ii)** embed the 480 numbers in the cell; **(iii)** quote no R² and
  restrict §5.2 to profile comparisons, which are still model-versus-data but need only the six
  class profiles. The agent's reading is (i).

- **S-4. n = 4.** Appendix F respawns the network at n = 4 so that Eq. (A5)'s cells are their five
  scale positions. This is a setting of an existing quantity (class (a)) and needs a agent/decisions.md
  entry saying why 4 and that the default n = 10 is untouched. Confirm.

- **S-5. May a cell print a published number?** The comparison quotes their LG/QF/ST/hybrid R²
  values. Printing a literature value inside a cell is new; the alternative is to cite them in the
  markdown and print only ours. Confirm which.

- **S-6. The word budget.** §5.2 is allocated 200 words (revisions.md §3). Stating H1 and H2,
  the instantiation, the matches and the mismatches will not fit. Estimate 340–380. Either §5
  absorbs it (from §5.1's 350, the only section with slack), or the 3,000 total rises. The user's
  call.

- **S-7. Does §5.2 keep its parity paragraph?** The κ parity result survives (2026-09-14 finding 6)
  but belongs to the old prediction, not to H1/H2. Keep, move to Appendix C, or drop.

**Raised 2026-09-21, SETTLED 2026-09-22 — S-8.** The user asked that **how the evaluation varies with
n** be reported in the notebook and in the paper, the finding currently sitting in
`agent/history.md` §9 (F6–F10, decision **O10**). Two things are
the user's to settle:
1. **Where it goes in the paper.** (a) §4, as a property of the evaluation, since it says which side
   of a crossing the reported verdicts sit on; (b) §5.2, next to H1, since n is what atomicity
   fixes and H1 is about exactly that instability; (c) §5.5 Limits, one sentence. **Recommendation:
   (a) with one clause in §5.2**, because F9 is a fact about the criterion's readings, which §4
   reports, while H1's claim concerns Λ, not n. It costs about 60 words in §4 and 15 in §5.2.
2. **Which cell prints it, and how wide the sweep is.** The side quest measured n at Λ = 8 under two
   priors only. Options: the existing Code Cell A (Appendix A owns θ_L and n); a block in Code
   Cell F, which is being written anyway; or a new cell. **Recommendation: Code Cell A**, since
   Eq. (A5) is where n gets its denotation, and a sweep of n against the two priors already reported,
   at Λ = 8 and at Λ = 512, so the paper can say whether the crossings move with Λ (the side quest
   did not check, and §4.4 now reports at Λ = 512).

**Both recommendations taken, 2026-09-22, with one widening.** (a) §4.2 carries it, as a second
guard beside the softmax-nonlinearity guard, with a clause in §5.2's *Calibrate the claim* bullet;
(b) Code Cell A prints it. The widening: the sweep runs **all four `BASE_WORLD_PRIORS`**, not the
two the side quest used, because the two were `gaussian` and `skewed high` under ad-hoc names and
the inconsistency was itself a `agent/agent.md` §5.5 violation. It cost nothing — the block runs in
under 0.1 s — and it is what exposed the degenerate-ray crossing under `flat` (F7 qualified).

**The budget moved.** S-8 estimated 60 words in §4 and 15 in §5.2. §4.2 took about **90**, because
the finding grew two qualifications the estimate did not anticipate (bracketing, and magnitude), and
a third result (non-separability from Λ) that the side quest had listed as unchecked. §4.2 goes
170 → 260 and the §§3–6 total 3,520 → 3,610, recorded as **R25** in `revisions.md`.

**One instruction overrode part of T14 as written.** The user, 2026-09-22: *"We want q-shift,
q-position, mode shift, and mode position status to be explicitly printed for every (n, Lambda,
ell_0) combination. Whether there is a flip or not is to be clarified in text, not the printed
report."* T14's acceptance clause "the crossings of F9 are **printed** rather than described" is
therefore **superseded**: the report prints per-row *statuses*, and the crossings are described in
Appendix A's prose and in §4.2. The first draft of the block violated this (it carried crossing
language in its header and docstring) and was rewritten.

**Settled 2026-09-21 — S-9. One fitted Λ per class, not per (class, image type).** The user's
reason: a constrained model should carry as few fitted quantities as possible. Fitting per image
type would entail that lexical strength depends on class **and** image type, a stipulation the user
does **not** call implausible; the paper opts out of the extra fit rather than arguing against the
dependence. Consequences for the tasks: **T2 block 4** keeps its per-class scan; **T2 block 5** keeps
the image-type difference as a measured difference, and may print the two best-fitting Λ of the
minimum class (F9: shapes ≈ 6, artifacts ≈ 24) **labelled as a property of the fit, not as a fitted
parameter**; **T10's prose** may never write that Λ is independent of image type — only that no
second Λ was fitted, and why. `agent/decisions.md` **O8**.

- [x] **T0. Checkpoint.** — done 2026-09-22 at `ae2f414`; tree clean but for three untracked backups.
      (The list was written at `acabb7e`; the U0–U14 change and T14–T16 landed in between.)
      **As specified:** **T0. Checkpoint.** `git status` clean, record `git rev-parse --short HEAD`. The tree is clean
      at `acabb7e` as this list is written.

- [x] **T1. The data file** — done 2026-09-22. `data/xiang_2022/` holds `xiang_items.csv` (sha256
      `c23d930d…`, 480 rows, 96 items), `README.md` with the OSF node, the four source files, the
      smoothing rule, CC-BY and the hash, and `check_data.py`, which verifies the hash and reprints
      the six empirical class profiles. **The derivation script does not exist and could not be
      written:** the four OSF files were never vendored and the 2026-09-17 derivation kept only its
      result. The user settled this the same day — ship the aggregate with its provenance — so the
      README says plainly that the hash pins the file and certifies nothing about the derivation
      (`agent/decisions.md` A20). Running the check exposed a defect in the record: **F1's table below is
      internally inconsistent**, its two `shape` rows renormalized while their mean positions were
      not. See the correction under §5.
      **As specified:** **T1. The data file** (S-3 settled: yes). Add the derived aggregate under a new `data/xiang_2022/`
      with `README.md` giving the OSF node, the four source files, the derivation, the licence and a
      sha256 per file; add the derivation script beside it. Acceptance: the README's hashes match,
      and a fresh read of the file reproduces the six class profiles in §5 F1 above.

- [x] **T2. Code Cell F** — done 2026-09-22, cell 23 of `main.ipynb`, 8 blocks, 130 lines of output,
      0.3 s. All eight blocks as specified, with three departures forced by what was found:
      **(i)** the relative class carries no prediction anywhere (S-2/O14), so block 6's
      "between-class gaps" is maximum against minimum and block 3's "overall" pools the two absolute
      classes; **(ii)** the fitted Λ of the minimum class is **48**, not the audit's 32, once the
      absent item is dropped, and the cell prints the **bracket** (32 to 48) rather than presenting
      the argmax as located — R25's lesson applied again; **(iii)** every helper takes *fields*
      rather than utterance names, because `ker χ_all` is a field no utterance names, and block 1
      checks both against `closed_form_fixed_point` and `theta_u_stationary_points` (0.0e+00 on
      each). `code cell 1` untouched, coupling 9 quiet, no figure, no `cost:` line needed.
      **As specified:** **T2. Code Cell F** (S-1 to S-7 settled). A new code cell printing every number §5.2 will quote,
      and nothing else. Its blocks:
      1. **Configuration and self-checks.** n = 4, θ_L = log 7, the five cells and their boundaries;
         the three entries of Eq. (A1) in the adjective's own orientation and the complement that
         each item's antonym supplies; that the audit's closed form equals `closed_form_fixed_point`
         (expect 0.0); that the closed-form θ\* equals a scan (expect ~6e-06) and returns −28.4375
         for the default n = 10 inventory; that a uniform five-cell prior pushes forward to
         [0.193, 0.200, 0.214, 0.200, 0.193]; that the five cells partition the grid to 1e-10.
      2. **The class profiles**, prior / q_lit / model / data, for the two absolute classes by image
         type, with the peak and the mean scale position.
      3. **R²** by class and overall, for the model and for q_lit — **ours only** (S-5). Their
         published values are cited in §5.2's prose and printed nowhere.
      4. **The Λ scan per class**, wide enough to show that the maximum class is flat to Λ = 2048
         and that the minimum class turns over at Λ = 32. Λ is labelled as fitted, and as fitted for
         H1 alone (S-1).
      5. **The image-type difference** per class, in prior, data and model.
      6. **The between-class gaps** by image condition.
      7. **The mismatch quantities**: the minimum class's R², the −0.16 against −1.13, and the
         displacement from prior to posterior in both conditions. Reported, not explained (R16).
      8. **The parity of the two entries' loadings** (S-7): κ for *all* and for *some* at n = 4,
         their identical tilt, their opposite width, and the midpoint statement.
      Constraints: every helper stays local to this cell, so `code cell 1` is untouched and coupling
      9 does not fire; no figure, so the figure baseline is unchanged; any wall-clock line goes
      behind `cost:` (coupling 3). Acceptance: the cell prints every number the drafted §5.2 quotes,
      and no number in §5.2 is absent from it.

- [x] **T3. Appendix F markdown cell.** — done 2026-09-22, cell 22, anchors `appf`, `appf-1`…`appf-6`
      and `codef` at its end; Eqs. (F1)–(F2). Six sections: the two hypotheses, what is instantiated
      and what is not, what is measured, what matches, what does not, and the parity at n = 4. No
      sentence says what any mismatch is due to.
      **As specified:** **T3. Appendix F markdown cell.** Heading with anchor `appf`, the `codef` anchor at its end.
      Content: H1 and H2 as stated by the user; the instantiation (five positions = five Voronoi
      cells at n = 4, the three entries, the complement ensemble); what is measured and how R² is
      computed; then match and mismatch, reported and not explained. Displays, if any, numbered F1,
      F2 … (appendix letters restart, so the body's (1)–(41) is untouched and no renumbering
      question arises). No sentence about what the mismatch is due to.

- [x] **T4. Structure.** — done 2026-09-22. Inserted after Code Cell D at 22 and 23; References moved
      to 24; 23 → 25 cells. ToC regenerated with the eight new rows.
      **As specified:** **T4. Structure.** Insert the two cells after Code Cell D (index 21), before References, which
      becomes index 24; cell count 23 → 25. Regenerate the ToC (cell 0) with rows for 22 and 23 and
      the moved References row. Acceptance: every ToC link resolves and every index in it is right.

- [x] **T5. References.** — done 2026-09-22. Kennedy (2007) and Xiang et al. (2022) added to the
      notebook's References in alphabetical position. **The pending Leffel-versus-Xiang check is
      decided: the manuscript is dropped.** The published 2022 article reports the shapes/artifacts
      contrast itself, so it is cited alone, in `background_sections.md` §1.7 and its reference
      list, and in `sections_3-6.md` §5.2 and its sources.
      **As specified:** **T5. References.** Add Xiang, Kennedy, Xu & Leffel (2022), and Kennedy (2007) if §5.2 names
      the open-scale class it does not model, APA 7th, in alphabetical position. The pending
      Leffel-versus-Xiang check (`background_sections.md` line 612) is decided here. Their LG/QF/ST
      and hybrid R² values are cited in the prose and printed by no cell (S-5).

- [x] **T6. Couplings.** — done 2026-09-22. None of the nine fires: Code Cells 2 and 2b untouched
      (1, 7), the new cell's prefix is `# === Code Cell F:` and not E3's two (2), no wall-clock line
      (3), main executed before appendix_E (4), the dangling-reference check returns `[]` on both
      notebooks with F1 and F2 defined (5), anchors added and ToC regenerated (6), no stdout tee (8),
      `code cell 1` untouched (9). **One new coupling was needed and is recorded as coupling 10:**
      Code Cell F is the only cell in either notebook that reads a file, by a path relative to the
      project folder. E.3 gains Appendix F in its *Unaffected* list.
      **As specified:** **T6. Couplings.** Confirm none fires: E3 diffs Code Cells 2 and 2b only; `code cell 1` is
      unchanged so coupling 9 is quiet; no new printing call in Code Cell 2 or 2b, so coupling 7 is
      quiet. Check whether `appendix_E.ipynb` §E.3 ("claims in main restated") needs a line.

- [x] **T7. Execute** — done 2026-09-22, `6e3326e`. main **0 errors, 8 figures, 14/14, 855 s**;
      appendix_E **0 errors, 5 figures, E2 18/18, E3 PASS on both cells, 1,860 s**. Execution counts
      run 1–10 and 1–5 with no gaps (the §5.1 interrupted-run check). **Diffed against T0's
      `ae2f414`: every difference in either notebook is a `cost:` line, which E3 drops by design,
      and the only new cell is Code Cell F.** Two departures from the recorded baseline, both
      bookkeeping rather than defects, and both fixed in `agent/agent.md` §5.1: main's runtime was "about
      250 s" from 2026-09-14 and is 855 s with every count unchanged, the cells added since
      accounting for it; and E3's line counts are 220 and 261 where the baseline said 203 and 234,
      because Code Cells 2 and 2b have gained printed lines. **What E3 asserts is the shape** — 0
      deleted, 1 changed (the pass count), 4 inserted — and that has never moved.
      **As specified:** **T7. Execute** main, then appendix_E, by `agent/agent.md` §5.1. Acceptance: main 0 errors,
      8 figures, 14/14; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS on both cells. Record the
      new runtime. Diff every other cell's stored output against T0: only the two new cells may
      differ.

- [x] **T8. agent/agent.md.** — done 2026-09-22. §1's cell map 23 → 25 with rows for 22, 23 and References
      at 24; §2 gains coupling 10 (the data-file path) and a loud dependency (Code Cell F reads
      `evaluation_network` from Code Cell 2); §5.1's baseline updated.
      **As specified:** **T8. agent/agent.md.** §1's `main.ipynb` cell map (23 → 25 cells, the new rows, References at 24)
      and §5.1's baseline. §2 needs no new coupling if T6 holds; if Code Cell F reads the data file,
      add a coupling for that path.

- [x] **T9. agent/decisions.md.** — done 2026-09-22. New **A20** (n = 4, the fitted Λ and its scope, the
      data file and what its hash does and does not certify, the relative class's exclusion, the
      bracket). New register-E entry **E16**, classing every quantity Code Cell F prints and
      recording the absent-item defect. **O13 rewritten**: its audit numbers are marked superseded
      and the printed values take their place. **O8** gains the pointer to what Code Cell F builds.
      **As specified:** **T9. agent/decisions.md.** New entries or amendments for whatever S-1 to S-5 settle: the n = 4
      configuration; the treatment of Λ; *t*, if it enters; the data file and its provenance;
      O13's status. Quantity-trace (register E) entries for every quantity Code Cell F prints, each
      assigned a class under §3.3. O8 gains the pointer.

- [x] **T10. §5.2 prose** — done 2026-09-22, written against the executed output. 400 → **550 words**
      (§§3–6 total → 3,760), retitled *Scale structure: two hypotheses, and where the model matches*.
      The old prediction (the monotone trend in the cut's position, reversing under a sharp prior) is
      withdrawn per F13; the parity paragraph is kept and restated at n = 4. X7's wording constraint
      honoured. **The instinct sits at the close of §5.2, pointing back to §5.1** — the user's choice
      of site, 2026-09-22. Scope-tier row and word table updated; both add up.
      **As specified:** **T10. §5.2 prose**, written against the executed output, not before.
      **Wording constraint from X7 (`exposure_stipulation.md`, applied 2026-09-22).** §5.2 states
      the ensemble as **the inventory's, not the experiment's**. F20 records that Xiang et al.'s
      latin square denies the exposure reading — no participant saw both adjectives of an image set
      — and the user's principle is that presence in the inventory follows from exposure somewhere
      but **not** conversely, so what a participant was shown constrains nothing about membership.
      §5.2 may also say that for these absolute classes, in this phase, $\mathrm{ant}$ coincides
      with $\ker$; it may **not** advance a thesis about antonymy, which is a lexical accident of
      two words sharing a scale and is not an involution (A18). §5.2 goes to about 400 words and the §§3–6 total to 3,200 (S-6). Confirm the instinct sentence's placement with the user. Also
      the §5.2 row of the word table in `sections_3-6.md` lines 81–103 and its scope-tier row at
      line 60.

- [x] **T11. Background §1.7.** — done 2026-09-22. F12's backwards bullet replaced: the manipulation
      is stated as novel versus familiar objects, with the elicited priors' actual direction given
      (artifacts are the **less** categorical). Q3b softened from "§5.2 answers it" to "§5.2 takes it
      up", with the reason.
      **As specified:** **T11. Background §1.7.** The prior-manipulation bullet (F12), and the Q3b sentence softened
      per the 2026-09-14 entry. `background_sections.md` line numbers are one lower than
      revisions.md cites, after R8.

- [x] **T12. revisions.md.** — done 2026-09-22. The §5.2 entry and **Q7 both marked CLOSED**, each
      keeping its old assessment beneath as the record; §8's source row now points at Code Cell F and
      says which audit numbers stay class (e) and reach no prose; §3's budget → 3,760; **R26** added.
      **As specified:** **T12. revisions.md.** Mark the §5.2 entry and Q7 closed by this change; update §8's source
      table so the numbers point at Code Cell F rather than at the audit; clear the audit from the
      class (e) list.

- [x] **T13. Commit** — done 2026-09-22, five commits, one logical change each:
      `c170067` T1 (the data file and what its hash does not certify) · `fc53a3e` T10–T12 (§5.2
      rewritten, the old prediction withdrawn from §5.2, §5.6 and §6 item 4) · `282f5ac` T8–T9 (the
      records, and the absent-data defect) · `ee03438` (E3's drifted baseline counts) · `6e3326e`
      T2–T7 (the two cells, executed and verified). The notebooks went in one commit because E3's
      verification spans both and `agent/agent.md` §4.3 forbids committing half a coupling.
      Checkpoint `ae2f414`; the list was written at `acabb7e`, with U0–U14 and T14–T16 in between.

**Added 2026-09-21 at the user's request (decision O10). Blocked on S-8.**


- [x] **T14. Print how the evaluation varies with n.** — done 2026-09-22, `2068268`. The cell S-8 settles prints, for the priors
      and lexical strengths S-8 fixes: θ_L = log(2n − 1) at each n, θ_u\*, the two q criteria and the
      two mode criteria for *some*, and the κ separation of F10. Acceptance: the numbers of F7–F10
      that the prose will quote are reproduced by the cell (they are class (e) until then), the
      crossings of F9 are printed rather than described, and no figure is added unless S-8 asks for
      one. n = 1 stays rejected by the constructor (F8).
      **As executed:** 80 rows (n × Λ × all four base priors), each printing θ_L,
      ⟨μ_u, Σc⟩, θ_u\*, the q shift, P(all∣*some*), the mode step and the **status of all four
      criteria**; then the κ ladder (F10) and the n = 1 refusal (F8). Two defects in the pre-existing
      block were fixed on the way: the mode shift was measured against the **tempered** fixed point
      rather than **ℓ_0**, disagreeing with Code Cells 2 and 4 (`agent/agent.md` §5.5); and the q shift was
      printed to four decimals, so a status change appeared between two numbers both shown as
      0.0000. F7 is qualified and F9 extended in the side-quest record.

- [x] **T15. The prose** — done 2026-09-22. As specified: at the site S-8 settles; n = 10 is a stipulation (O1), not a neutral choice
      of units; the criteria's readings cross with n; m = 2 and the rank results do not move (F7);
      n = 2 is not degenerate and n = 1 is (F8). Written against T14's output. Whether this entails
      anything about O1 is **not** claimed here.
      **As executed:** §4.2's second guard (about 90 words) and a clause in §5.2. The phrase "the
      criteria's readings **cross** with n" is **not** used: per the user's 2026-09-22 instruction
      and F9-extended, the prose says which criteria *change status* where, that a sweep brackets
      rather than locates the change, and that one such change is a sign flip at −7.593e-07. The
      O1 non-claim is honoured and stated in both `agent/decisions.md` O1 and R25.

- [x] **T16. Records.** — done 2026-09-22. `agent/decisions.md`: O10 gains the pointer to the printed source and its numbers
      leave class (e); O1 gains a line that the reporting exists, since F9 is what makes it
      consequential. `agent/history.md` §9 §4 loses "neither
      question has any prose site" for side quest 2. `thesis_outline/revisions.md`: a site entry and
      a §8 source row.

*Full original:* `git show 200677a:procedure_records/scale_classes_hypothesis.md`

---

<a id="r13" name="r13"></a>

## 13. Λ against ℓ₀: the counterforce, and where ℓ₀ enters

*Was* `procedure_records/ell0_placement_and_counterforce.md`

**Opened** 2026-09-17 20:19 · **Closed** 2026-09-21 13:13 · 29 commits

**Settled** A3, E9, E15; revisions.md U0-U14

**Opened by**

> Before we do T0-T13, we need to clear something else first. Recall that we have made new changes
> to the evaluation since we last edited sections 3 and 4. The new important take-away is this:
> under a strong Lambda, the shift criterion is more robustly met for different priors; this is
> thanks to the mechanism that Lambda and ell_0 are so to speak couterforces to each other. This is
> a commitment that the model makes. We would want to inform the reader more about what this
> commitment concerns:
>
> 1. does this commitment have any parallel in RSA architecures?
> 2. logically speaking, is g_L the only place where ell_0 could enter the model? Of course not! We
> could have placed ell_0 at g_s instead. That would not have allowed ell_0 and Lambda to counteract
> …

#### 4. Findings

- **G1. The placement changes exactly one quantity: the utility level's drive.**
  c_y = BᵀW(ℓ₀ − φ_L) under A, and −BᵀW(ℓ₀ + φ_L) under B. Measured as identities over the three
  entries: `c^A − c^B − 2BᵀWℓ₀` is at most 2.8e-14 and `c^A + c^B + 2BᵀWφ_L` at most 1.1e-14. So
  **the entry enters both placements the same way and the whole difference is the sign the prior
  carries against it**, and that difference is 2BᵀWℓ₀ = (−0.0, −37.1992) at the default settings,
  independent of the utterance.

- **G2. It is not a difference in the belief formula.** At σ_L = σ_S the two give the same φ_S given
  φ_u, to 1.8e-15. What differs is φ_u\* itself (by 12.3997 at θ_u = 1), and through it φ_S\* (by
  3.9996). The user's "not as directly" is the accurate phrasing: ℓ₀ and Λχ_y still oppose each
  other inside φ_S\* under B.

- **G3. Reason (a), made exact.** Under A the opposition is one error unit's activity:
  ε_L = φ_L − ℓ₀ + φ_S computes the difference at a node. Under B, ε_L computes φ_L + φ_S and ε_S
  computes φ_S − ℓ₀ − θ_u Bφ_u; ℓ₀ − φ_L is never any unit's activity and exists only as a
  combination of two residuals. The counterforce is a fact about a node under A and a fact about the
  algebra under B.

- **G4. A third reason, not on record anywhere and stronger than either of the user's.** Under A the
  literal listener is a fixed point of the network: φ_S\* → ℓ₀ − φ_L as σ_S → ∞ (agreement 2.7e-5
  at σ_S = 1e6). **Under B no σ produces it.** σ_S → ∞ gives −φ_L (the entry, prior discarded);
  σ_L → ∞ gives ℓ₀ + θ_u Bφ_u (the prior, entry discarded); ℓ₀ − φ_L is unreachable. §4.1's
  sentence — that q_lit "is a fixed point of this network rather than an external construction",
  which "removes the obvious objection that the baseline was built to be beaten" — is available
  only under A, and the outline states it without knowing it depends on A3.

- **G5. Reason (b) has empirical content.** The two placements are distinguishable as soon as
  σ_L ≠ σ_S: the φ_S difference at a shared φ_u is exactly (σ_L − σ_S)ℓ₀/S. At σ_L = 2, σ_S = 1 the
  measured max is 6.3063 against a predicted 6.3063. Under A the prior travels with the lexical
  channel's precision, under B with the utility channel's, so a later precision-bearing phase
  (Text cell 3 §5: the log σ terms are "carried only to mark where a later precision-bearing version
  would reintroduce them") tests the placement instead of inheriting it.

- **G6. The take-away is placement-dependent.** Shift for *some*, both variants scored against the
  same literal listener ℓ₀ − φ_L, which B cannot itself produce (G4):

  | prior | Λ=8, A | Λ=8, B | Λ=512, A | Λ=512, B |
  |---|---:|---:|---:|---:|
  | Gaussian | +0.0008 | +0.3815 | +0.0071 | +0.0587 |
  | flat | +0.0295 | +0.3159 | **−0.0146** | +0.0071 |
  | Beta(1,3) | +0.0004 | +0.3405 | +0.0089 | +0.0546 |
  | Beta(3,1) | +0.0421 | +0.2016 | **−0.0955** | **−0.0820** |
  | delta-like | +0.0030 | **−0.5067** | **−0.5217** | **−0.9494** |

  At Λ = 512 the conjunction holds under **3 of 5** priors under A (flat, Beta(3,1), delta-like) and
  **2 of 5** under B. The sharper contrast is at Λ = 8, where the anti-exhaustive shift is two to
  three orders of magnitude larger under B (+0.3405 against +0.0004 on Beta(1,3)): the direction
  §4.4 names, and background §1.3 Beat 3 ties to Cremers et al. (2023), is one the model's placement
  suppresses before Λ is raised at all. The A columns reproduce Text cell 4b and Part D in every
  printed digit.

- **G7. How Λ reaches the utility level.** |c_y| under the Gaussian prior for *some*: at Λ → 0 the
  two couplings are exact negatives, (0, −18.5996) and (0, +18.5996); as Λ grows both approach
  −Λ BᵀWχ_y, and |c^A| − |c^B| saturates at +19.88. So the placements agree in the entry's leading
  term and differ in the prior's sign against it, at every Λ.

- **G8. The answer to question 1, in four parts.**
  1. **Λ → ∞ *is* RSA's literal listener.** log L₀ = log P(s) + log⟦u⟧(s), and a hard semantics puts
     log⟦u⟧ ∈ {0, −∞}. φ_S = ℓ₀ − Λχ_y is that with −∞ replaced by −Λ. Text cell 3 §3 item 6 already
     says Λ → ∞ recovers a hard truth-conditional constraint; what is not said is that the object at
     that limit is RSA's L₀. This is the tightest parallel and costs one clause.
  2. **The parallel to c_y is S₁'s utility, not any RSA parameter.** S₁ reads log L₀(s|u), the log
     of the literal posterior; the utility level reads BᵀW(ℓ₀ − φ_L), a linear projection of the
     same log quantity. Under B the level above would read ℓ₀ + φ_L, which corresponds to no RSA
     quantity. **But see P-5:** background line 373 explicitly forbids equating the mapping with
     RSA's social recursion, so this part is not free to state.
  3. **Finite Λ has no single RSA counterpart.** RSA lets prior and semantics trade off with a
     latent variable rather than a strength: lexical uncertainty marginalizes over hard lexica
     (Potts et al., 2016, in the background bibliography); threshold uncertainty infers the cut
     jointly with the state (Lassiter & Goodman — hence Xiang et al.'s LG model, so this touches
     §5.2); wonky worlds (Degen, Tessler & Goodman, 2015) makes *the prior* defeasible instead,
     which is the inversion §1.3 Beat 2 already states. The nearest strength parameter is α, which
     sharpens informativity, not the lexicon. **Nothing in RSA plays the role of Eq. (41)'s
     Λ_crit ≈ α log 2n**, the quantified exchange rate — that is the part of the commitment with no
     parallel at all.
  4. **The placement question itself has a contrastive parallel.** RSA also has a "where does the
     prior enter" degree of freedom and resolves it the other way: P(s) appears in L₀ *and again* in
     L₁ ∝ S₁(u|s)P(s). In this chain ℓ₀ enters once, and the commitment is which map it enters. One
     sentence, stated as a contrast.

- **G9. Nothing here contradicts a settled decision.** A3 is confirmed, not challenged: every
  finding above is a reason for it. Under `agent/agent.md` §3.1 the reasons and the evidence are added to
  A3 as a dated amendment, and A3 is not reopened.

---


##### G10. The warning has an exact form, and it is measured

$B$ is orthogonal to the constant: $B^{\mathsf T}W\mathbf 1 = 9.4\times10^{-17}$ (m = 2, the
constant column dropped in Part A). So the utility level's drive is **invariant to an additive
constant** on the field it reads: adding $3.7\cdot\mathbf 1$ to $\ell_0-\varphi_L$ leaves
$c_{\textit{some}} = (9.119088, -24.367443)$ unchanged to $1.4\times10^{-14}$.

- **The statement.** $S_1$ reads $\log L_0(s\mid u)$, normalizer included. The utility level reads
  $B^{\mathsf T}W(\ell_0-\varphi_L)$: **rank 2, and blind to exactly the direction the normalizer
  lives in.** Two of the scale's coordinates — the tilt and the width of Appendix C — and nothing
  else. That is the warning in its exact form, and it is stronger than a caution: the projection
  discards the one component that makes $\log L_0$ a normalized quantity.
- **The nuance that must not be got wrong.** The invariance is a property of $c_y$, not of the
  model. $\varphi_S^\ast$ is *not* defined up to a constant — Text cell 3 §9.1 establishes there is
  no flat direction, and Appendix D §3's third reading turns on it — because the
  $\sigma_S(\ell_0-\varphi_L)$ term of Eq. (15) carries the constant directly. Say the invariance of
  the *coupling*; never write that the model is constant-invariant.


##### G11. The trade-off survives, but as a property of the plane, not of the five priors

The floors table (Code Cell 4, already printed) gives the least Λ from which each criterion holds at
every larger Λ, by α on Beta(α,1):

| α | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| q shift | 512 | 256 | 128 | 64 | 32 | 32 | 16 | 2 | 2 | 2 | 2048 |
| q position | 2 | 2 | 2 | 2 | 64 | 256 | 512 | 1024 | — | — | — |

The two floors run in opposite directions and cross at α = 16. **§4.5's opposing-floors result is
untouched**, and so is the argument that a drain keyed to the alternative would not consume the
headroom the position criterion needs. What is false is the Part D framing: at Λ = 512 the
conjunction holds for α = 1 to 64 (7 of the 11 rows), because 512 lies above both floors over most
of the range, and among Part D's five priors the position criterion holds under **all five**. So
"prior concentration buys the first and spends the second" is a statement about the **floors**, and
it can no longer be carried by "under every prior tested".


##### G12. The Λ = 512 picture, for the rework

From Text cell 4b, already printed: the q position criterion holds under **five of five**; the q
shift criterion under **three** (flat, Beta(3,1), delta-like); **no prior meets the shift criterion
alone**. So the two conditions no longer separate the rows — the shift criterion is strictly the
harder one, and the three that meet it are the three with the most prior mass on the all-region
(0.0479, 0.1367, 0.9568), the shift deepening with that mass. The anti-exhaustive direction holds
under **two of five** at Λ = 512 (Gaussian +0.0071, Beta(1,3) +0.0089), against four of five at
Λ = 8.

---


- **P-1. Does the paper report the alternative placement with numbers, or state the commitment
  without them?**
  - (i) *Assert only.* §3.2 gains a bullet; no number is quoted; no cell changes. Cheapest; the
    commitment is then unfalsifiable in the text.
  - (ii) **(recommended)** *The structural facts, printed.* The identity c^A − c^B = 2BᵀWℓ₀, the
    node-level statement (G3) and the σ-limit fact (G4) are stated and printed by **Code Cell D**,
    with the prose in a new Appendix D section. The body quotes at most one number.
  - (iii) *The full counterfactual.* Part D under both placements (G6) as well. This is a second
    evaluation of a model the paper does not hold, and it needs its own appendix.
  Recommendation (ii): Appendix D is already the home of the question "which map carries the
  entry into a field", the placement is its sibling question, and (ii) satisfies C6 without
  spending body words.

- **P-2. Where the commitment sits in the body: §3.2 or §3.3?** §3.2 holds the Λ material ("the
  price of a soft lexicon"), §3.3 holds the chain and g_S. Recommendation: **§3.2**, one bullet,
  because the commitment is about Λ against ℓ₀; §3.3's g_S bullet gets a clause pointing to it.

- **P-3. Word budget.** §3 is at 920 and §4 at 950 after R1/S-6, and background §1.3 at 340. The
  commitment needs roughly 90 words in §3.2, 20 in §3.3, 30 in §4.1, and 50 in background §1.3.
  Raise the budget, or trim, and by how much? The §3 word table in `revisions.md` §3 is **not**
  edited until this is answered.

- **P-4. Which of G8's four parts the paper states.** Parts 1, 3 and 4 are safe. Part 2 is P-5.

- **P-5. Is the c_y ↔ log L₀ parallel (G8.2) stated at all?** It is the sharpest parallel and it
  invites exactly the reading `background_sections.md` line 373 tells the writer to block ("do not
  equate this mapping with RSA's social recursion"). Options: state it with that qualification
  attached; state it only in Appendix D, away from the background's framing; or drop it.
  **This one is genuinely the user's call.**

- **P-6. The Λ = 512 headline.** Rebuilding §§4.4–4.5 moves the verdict from "the conjunction holds
  under none" (outline) / "under one" (`revisions.md` §2) to **"under three of five"**. Under
  `agent/agent.md` §5.4 a headline result changing is a stop-and-ask. §5.1, §6 and the background's
  forward pointers lean on the old count. Confirm the new headline sentence before any prose moves.

- **P-7. How A3 is updated.** Recommendation: a dated amendment in place — the user's reasons (a)
  and (b), the third reason G4, the evidence pointer, and an expanded "Depends on it" naming Eq.
  (16)'s c_y, §4.1's baseline sentence and the Λ = 512 result. Not a new entry, and not a reopening
  (G9). Agent decision, pending the user.

---

- [x] **U0. Checkpoint** (2026-09-17). Clean at `b548e0a` when the list was written; clean again at
      `90a9352` before U2.

- [x] **U1. Settle the blocking decisions** (2026-09-17). P-4 and P-5 in §8, P-1, P-2, P-3, P-7,
      P-8, P-9, P-10 in §11, each verbatim. Commit `1c473d8`, `90a9352`.

- [x] **U2. `agent/decisions.md`** (2026-09-17, P-7 = amend). **A3 amended:** the two user reasons dated 2026-09-17, the third
      reason (G4), the evidence line pointing at `agent/audits/2026-09-17-ell0-placement/`, and the
      widened "Depends on it". Add a dated finding under **B1/B2** if P-6 changes the criterion's
      reported scope. Register-E entries for every quantity a cell newly prints (U3), each classed
      under `agent/agent.md` §3.3 — note that variant B's fields are a **counterfactual manipulation
      (C8)**, not a control, since no setting of the model produces them, and C8's wording must be
      used in both the cell's labels and the prose.

- [x] **U3. Code Cell D** (2026-09-17, P-1 = printed by Code Cell D). Appended
      `UtilityPlacementNetwork`, three helpers and `ell0_placement_report`, printing five blocks
      under the heading *Sec. 5: where ell_0 enters*, plus self-checks. Commit `23bdf23`.
      - **Built from 𝓕, not asserted.** The alternative is a subclass overriding `predict_lexical`
        and `predict_state` only, exactly as `TruthSetNetwork` already does in this cell, and it is
        solved by the cell's own `settle_by_newton` on Eq. (13). Its closed form agrees with Newton
        to **3.6e-15**, and its θ\* is **+22.57787** both in closed form and by the cell's
        `learned_by_bisection` on Eq. (20).
      - **Eq. (B2) over given couplings.** `theta_u_stationary_points` builds c_y inline, so a
        local `theta_star_over_couplings` takes c_y as an argument. Fed the model's own couplings it
        returns **−28.43749**, the parent's value, and that check prints before it is used.
      - **What it prints.** (1) the two couplings per entry and the identities c(g_L) − c(g_S) =
        2BᵀWℓ₀ to 2.8e-14 and c(g_L) + c(g_S) = −2BᵀWφ_L to 1.1e-14; (2) **R19's warning** —
        BᵀW1 = (+9.4e-17, −2.6e-17), the constant component ⟨1, ℓ₀ − φ_L⟩_W per entry
        (−154.5617, −107.5217, −154.5617, so it is **not the same for every entry**), and c_y
        unchanged to 1.4e-14 by adding 3.7·1; (3) the σ-limit table; (4) the same-φ_u agreement and
        the (σ_L − σ_S)ℓ₀/S difference; (5) Part D's five priors under both placements at Λ = 8 and
        Λ = 512, scored by the cell's own `criterion_for_some`.
      - **Constraints met.** Every helper is local to Code Cell D; `code cell 1` is untouched, so
        coupling 9 is quiet; no figure, so the 8-figure baseline holds; no wall-clock is printed, so
        coupling 3 does not arise. Every label says *counterfactual manipulation*, never *control*,
        and the two θ_u = 1 rows say "a control" as B4 requires.
      - **A dependency to record in U6/U8:** the block reads `part_d_priors` (Code Cell 2) and
        `STRONG_LAMBDA`, `DELTA_ALL_ALPHA` (Code Cell 2b). Renaming any of them raises `NameError`
        in Code Cell D — loud, not silent, so it is not a coupling of the §2 kind, but it is a new
        cross-cell dependency and belongs in the record.
      - **Verification.** `main.ipynb` re-executed: **0 errors, 8 figures, 14/14, 246 s**. Against
        the checkpoint only two cells differ — Code Cell D (source and output) and Code Cell 2b,
        whose only changed lines are `cost:` wall-clock. Appendix D §§1 and 3 reproduce every stored
        number exactly (θ_u\* −28.43749 under both conventions, Eq. (D3)'s +4.000000, the field
        norms, Eq. (D4)). `appendix_E.ipynb` is **not** re-executed here; that is U7.

- [x] **U4. Appendix D prose** (2026-09-17). New **Sec. 5, "Where ℓ₀ enters"**, with displays
      **(D5)–(D7)**; the body's (1)–(41) is untouched and coupling 5 does not fire. Commit `ccaccd4`.
      - **Content, kept to what the notebook can say and the paper cannot.** The logical space in
        three clauses (a bias belonging to no g is not a prediction and so has no error unit; μ_u is
        in ℝ^m; g_y is out while φ_L is clamped); Eq. (D5)'s Bogacz status, which is Eq. (9)'s, so
        one register entry covers both; Eq. (D6), the alternative's stationary point; Eq. (D7), the
        two coupling identities; then four short paragraphs — the one quantity that differs, what
        Eq. (9) makes available, what the coupling does not carry, and Part D under both. **The
        commitment framing and the reasons are not argued here; they are §3.2's.** Part D's rows are
        noted with our position reserved (composition guide Entry 3b), as Text cell 4b does.
      - **Sec. 4 rewritten** to close Secs. 1–3 and point forward to Sec. 5, instead of reading as
        the appendix's own close. Its "assymetry" typo is corrected in the same sentence.
      - **Appendix retitled**, "why emission is exclusion" → "why emission is exclusion, and where
        ℓ₀ enters", since the appendix now answers two questions about the same map. **Agent
        decision, named to the user, and confirmed by the user 2026-09-21.** Text cell 3's two references to Appendix D stay accurate (one
        already says it derives "ℓ₀'s place here"); cell 0's ToC row still reads "(D1)–(D4)" and
        carries the old title, which **U5** fixes.
      - **One number was quoted before it was printed**, and Code Cell D was corrected rather than
        the prose: block (4) printed the same-φ_u agreement as `0.0000`, so it now prints four
        significant figures (`1.776e-15`, and `6.306` against a predicted `6.306`). Every number
        Sec. 5 quotes is now in Code Cell D's output — checked one by one.
      - **Verification.** `main.ipynb` re-executed: **0 errors, 8 figures, 14/14, 250 s**. Against
        U3's commit, cells 20 (markdown) and 21 differ, and Code Cell 2b's output differs in 12
        lines, every one of them a `cost:` line.

- [x] **U5. Anchors and ToC** (2026-09-18). Commit `4b0eb71`. The `appd-5` anchor was already inline
      in the heading from U4 (coupling 6). Cell 0's Appendix D rows were **derived from cell 20's own
      headings and `\tag{}`s** rather than typed, so the titles and equation ranges cannot drift from
      the appendix: the header row now carries the new title and **(D1)–(D7)**, row 4 the rewritten
      heading, and a new row 5 `(D5)–(D7)`. Only those three lines of cell 0 change. **All 74 ToC
      links resolve** to an inline anchor. `appendix_E.ipynb` names Appendix D once, in a list of
      appendices, unaffected by the title. Markdown only: no execution needed, and the stored outputs
      are those U4 verified.

- [x] **U6. Couplings** (2026-09-18). **None fires.** Commit `84e45e8`. Against the checkpoint
      `b548e0a`, only cells 0, 20 and 21 of `main.ipynb` differ in source; the cell count is 23.
      - **1, 2, 7.** Code Cells 2 and 2b are source-identical to the checkpoint, and their headers
        still carry the exact prefixes `# === Code Cell 2:` and `# === Code Cell 2b:`, which are
        the only things E3 locates main's cells by. E3 never reads Code Cell D.
      - **3.** Code Cell D prints no run-dependent line. **5.** The body's tags are still exactly
        (1)–(41); Appendix D's run (D1)–(D7). **6.** Closed in U5. **8.** Code Cell D does not touch
        `sys.stdout`. **9.** `code cell 1` is source-identical to the checkpoint, so E1 needs no
        mirror. Figures 8 → 8.
      - **E.3 needs no line, and that is now measured rather than assumed.** E.3 lists Appendix D
        as *Unaffected* by the relay, a line written before Sec. 5 existed. Running Code Cell D's
        Sec. 5 report on E1's architecture — E1 for `code cell 1`, E2 and E2b's definitions for
        Code Cells 2 and 2b, Eq. (D5) written at the relay as g_S = ℓ₀ + θ_u r — reproduces **all
        61 lines** of main's stored Sec. 5 output, self-checks included. Script and output:
        `agent/audits/2026-09-17-ell0-placement/relay_check.py`, `relay_check_output.txt`.
      - **Two loud dependencies, for U8 to record.** Neither is a coupling of `agent/agent.md` §2's kind,
        because each fails with an exception rather than silently.
        1. *Names.* Code Cell D now reads `part_d_priors` and `criterion_for_some` (Code Cell 2)
           and `STRONG_LAMBDA`, `DELTA_ALL_ALPHA` (Code Cell 2b). Renaming any raises `NameError`.
        2. *A signature.* `UtilityPlacementNetwork.predict_state` overrides main's
           `predict_state(phi_u, theta_u=None)`. E1's version takes a third argument, `relay`, so
           the override **cannot run on E1 as written** — the relay check above had to restate it
           with E1's signature. If `code cell 1` ever gains that argument, Code Cell D raises
           `TypeError`. `TruthSetNetwork` is not exposed the same way: it overrides only
           `predict_lexical`, whose signature the two notebooks share.

- [x] **U7. Execute** (2026-09-18), main then appendix_E, by `agent/agent.md` §5.1. Commit `bf746b1`.
      **Both at baseline, exactly.**
      - `main.ipynb`: **0 errors, 8 figures, 14/14, 249 s.** Every code cell source-identical to U6's
        commit; against its stored outputs the only differing lines are 12 `cost:` lines in Code
        Cell 2b.
      - `appendix_E.ipynb`: **0 errors, 5 figures, E2 18/18, E3 PASS on both cells, 679 s.** Code
        Cell 2: 203 lines identical, 0 deleted, 1 changed (the pass count), 4 inserted (the relay's
        checks). Code Cell 2b: 234 identical, none changed. Against the committed appendix_E, the
        only differing lines are 12 `cost:` lines in E2b.
      - Over the whole change (checkpoint `b548e0a` to here), the only stored output that differs
        in anything but wall-clock is Code Cell D's, which is the one U3 and U4 set out to change.

- [x] **U8. `agent/agent.md`** (2026-09-18). Commit `1320fa1`.
      - **§1 cell map.** The Appendices A–D row now names "where ℓ₀ enters (Sec. 5, Eqs. (D5)–(D7),
        decision A3)". The cell count stays 23 and the Code Cells A–D row stays accurate.
      - **§2, the two loud dependencies from U6**, recorded under a new *Loud dependencies* paragraph
        after coupling 9, explicitly marked as not couplings of §2's kind.
      - **§2 coupling 9 corrected — a pre-existing inaccuracy found while writing the second
        dependency.** It said every `def` in `code cell 1` appears verbatim in E1. Measured: 24 of 30
        do; `__init__`, `predict_state`, `residuals`, `free_energy`, `infer` and `theta_u_gradient`
        carry the relay in E1. The "878 of 912 lines" figure beside it is right (re-measured). The
        correction matters because coupling 9 also instructs mirroring **by lifting the source
        verbatim**, which inside those six would delete E1's relay; the item now says so.
      - **§5.1 unchanged.** 249 s and 679 s against the stated "about 250 s" and "about 710 s", with
        every count identical.

- [x] **U9. §3 prose** (2026-09-18, commit `d667600`). `sections_3-6.md` §§3.2–3.3 only; headings raised to P-3's 270
      and 255. No number is quoted in either section, so C6 does not arise.
      - **§3.2, "The price of a soft lexicon"** now names the Λ → ∞ object as RSA's L₀ (G8.1), and
        defines ℓ₀ in place, since §3.2 is its first use in the outline.
      - **§3.2, a new bullet: the commitment (R18).** The contest between Λ and ℓ₀ is staged at one
        error unit because ℓ₀ sits in g_L; Eq. (D5) is as local and has the same Bogacz status, so
        locality does not decide it (A3). The three reasons, one clause each: (a) cleaner, in G3's
        exact form; (b) the counteraction hypothesis, with G5's empirical content; the agent's
        fixed-point reason (G4), tied to §4.1. It closes on Eq. (D7) and points to §4.4, and calls
        the Eq. (D5) rows a counterfactual manipulation (C8).
      - **§3.3, the g_S bullet** says g_S carries nothing else and ℓ₀ enters at g_L. **A
        pre-existing Entry 5 slip fixed in passing:** the bullet used c_y (Appendix B's condition)
        before anything defined it; it now glosses c_y in place.
      - **§3.3, a new bullet: the projection and its warning (R19)**, in G10's exact form, with the
        coupling/model nuance. Two calibrations under composition-guide Entry 2: the utility level's
        drive is described as each utility unit's own afferent sum (Eq. 19), so the reading is
        local; and ℓ₀ − φ_L is log L₀ only with −∞ softened to −Λ, so the parallel says so.
      - **One agent addition, flagged in the bullet:** the sentence that RSA's informativity runs on
        the normalizer (for two utterances true at one state, S₁'s preference comes from their
        normalizers alone, cost aside). It follows from §1.2's three equations, so it quotes no
        number, and it makes concrete why forgetting the difference is dangerous. The bullet names it
        as the first to cut.
      - **Not done here, by the plan:** G8.3 (no RSA counterpart to a finite Λ; nothing plays
        Λ_crit) and G8.4 (P(s) in both L₀ and L₁) go to the background (U11). The outline's own
        word table and §3 heading still carry pre-R1 figures; replacing them is `revisions.md` §4's
        "Word allocation table" entry, which no U task owns.

- [x] **U10. §4.4 and §4.5, rebuilt on Λ = 512** (2026-09-18, commit `bab65cc`). `sections_3-6.md` §§4.1, 4.4, 4.5;
      headings to P-3's 140, 285, 255. No new code: every number is in the stored output of Code
      Cells 2, 2b or 4, checked by script against the outputs, not against the text cells.
      - **§4.1.** The A3 clause (G4): q_lit is a fixed point **because** ℓ₀ enters at g_L. The
        renamings (literal listener, tempered control) come in with it, because §4.4 now uses them
        and Entry 5 needs them defined first; DEC5's sentence goes in with a writer's note that it
        does not contradict U9's §3.2 (L₀ only as Λ → ∞, a limit and not a setting).
      - **§4.4 "The five priors".** Text cell 4b's table with tempering and utility columns; the
        conjunction under three of five, position under five, nested among these rows and not on
        the plane; the Λ = 8 contrast in one bullet (P-10), placing the change in the utility
        level's contribution, the one quantity the placement changes (Eq. D7), and the prior
        mattering less (contrasts agree to 0.0001 against 0.0575); P-9's two counts; the Cremers
        guards; the Eq. (23)–(24) mechanism.
      - **§4.5.** 33 cells, band (1,512)–(128,2048); the floors as the source of the trade-off
        claim (P-8); the V under both read-outs (R14); Eq. (41) as the exchange rate of §3.2's
        contest; spread D and the least-|θ_u| sentence at the printed values.
      - **Three things the plan had wrong, found against the printed rows** (details in
        `revisions.md` §4's §4.4 entry): (1) the utility level's contribution is **positive under
        Beta(1,3) at Λ = 512** (+0.0024), so "negative under all five" and item 1's Cremers guard hold
        at Λ = 8 only; (2) "four of five at Λ = 8" is really **all four priors with a Λ = 8 row**, the
        delta-like prior having none; (3) raising Λ **removes** the anti-exhaustive direction under
        flat and Beta(3,1) but **enlarges** it under Gaussian and Beta(1,3), so §10's gloss on P-9
        ("something raising Λ removes") was half true. P-9's decision itself, both counts in one
        sentence, stands and is applied. Also corrected: the floors cross between α = 8 and 16; the
        Eq. (41) match is 4.1%, not 4%.
      - **Deliberately not carried:** Text cell 4b's claim that every θ\* at Λ = 512 sits in
        Eq. (24)'s saturation (no cell prints it for the four diffuse rows); item 1's delta read-out
        results (they need §3.6 first).

- [x] **U11. Background §1.3** (2026-09-18, commit `4510beb`). `background_sections.md` only.
      - **Beat 2** gains G8.1 (the hard limit is L₀, a forward pointer), G8.4 (P(s) in L₀ and again in
        L₁; the prior enters this model once, and the commitment is which map), G8.3 (latent variables,
        not a strength: lexical uncertainty, threshold uncertainty, wonkiness; nothing plays the
        override law), and R19's foreshadowing with the warning in the same sentence and the
        coupling/model guard. All in Beat 2, not §1.2, because §1.3 carries P-3's added budget.
      - **Beat 3 (V11, taken here because it is the same subsection)**: pointer to §4.4, both counts
        as U10 corrected them, the tempering named, "corroboration" and the drain dropped (R7).
      - **Headings and totals** moved by P-3's +75: §1.3 415, Part I 2,110, target 3,670.
      - **Reference added:** Lassiter & Goodman (2017), *Synthese*, marked [verify], including
        whether Xiang et al.'s LG model builds on it or on the 2013 SALT paper.
      - **Found: α names two quantities** — RSA's speaker optimality (§1.2) and the Beta concentration
        of Eq. (41). The background states the override law in words; the clash is `revisions.md`
        **Q8**, open, for the user.
      - **Found for U12:** Beat 1's "redeployment" bullet says human robustness to prior concentration
        is "precisely the profile a drain scaling with prior mass on the all-region cannot produce" and
        flags it forward to §5.1. That is the trade-off claim in another form, and after P-8 it must
        point at §4.5's floors or go.

- [x] **U12. The verdict sites** (2026-09-18, commit `7f03135`). Against §9's table:
      - **V1**, central claim: the verdict on Λ = 512 and the plane, then R2's list with P-8's floors
        argument as its last item, marked argued and not measured; "shape of its absence" withdrawn.
      - **V2**, Tier A criterion row: reworded as planned.
      - **V7, V8**, §5.1: the two bullets become one (P-8 (i)), stated on §4.5's floors.
      - **V9, V10**, §6: item 1 flags the placement as a commitment; item 3 rewritten. Heading 165.
      - **Background Beat 1** (found in U11): the "drain scaling with prior mass" line now states the
        rising floor (§4.5) and points to §5.1's argument.
      - **Already done or elsewhere:** V4–V6 (U10), V11–V12 (U11); V3 and V14 are not R20's; V13 is
        U13's. A grep for the old headline's phrases ("every prior tested", "four of five", "under
        none", "exactly one condition", "shape of its absence", "only one of the two") finds only
        the sentences in §4.5 and §5.1 that bar the phrase; the outline's word table still titles
        §4.4 "One condition, every time", which U13 replaces.

- [x] **U13. `revisions.md`, the outline's table, and the stale pointers** (2026-09-21, commit `1bdeeea`).
      - **`revisions.md`.** R18–R20 and §3's table were already in place from U1. Now: the
        2026-09-15 note in §2 is **closed** and its table re-scoped as the 2026-09-13 record rather
        than the paper's evidence (site **V13**); §8's ℓ₀-placement row names **Code Cell D's Sec. 5**
        as the source and drops class (e), keeping the audit as the derivation; the scope-line and
        word-table entries in §4 are marked applied.
      - **`sections_3-6.md`.** The scope line reads 3,450 and names Code Cells A–D. The word table is
        replaced by §3's, with a "was" column and a note saying which sections have bodies written to
        the new budget. Headings brought into line: §3 1,085, §3.4 230, §4 1,020, §4.3 70, §5 1,180,
        §5.1 350, §5.2 400. **The renumbering is applied**: Limits → §5.5, Predictions → §5.6, with
        the three references in the scope tiers and one in `background_sections.md` (commitment 3)
        following. §§3.6, 4.6, 5.3 and 5.4 appear in the table with no bodies yet, and the note says
        so; the central claim's pointer to the new §5.3 now works.
      - **`agent/decisions.md` A3.** The Evidence line no longer says the numbers are "to be printed" or
        class (e): Code Cell D prints them (U3, `23bdf23`), and the audit is named as the derivation.
      - **Not done, and not U13's:** the outline bodies whose budgets moved under R1–R17 but whose
        text U9–U12 did not touch (§3.4, §4.3, §5.1, §5.2, §5.5, §5.6). The table's note flags them.

- [x] **U14. Close the change** (2026-09-21, commit `a580599`). One logical change per commit throughout; every task
      line above carries its hash. The closing checklist of `agent/agent.md` §6, item by item:
      - **Bogacz.** One new operation in the change, Eq. (D5), and it has Eq. (9)'s status, an
        instance under restriction (A3, D3). No divergence entry is needed.
      - **Quantities.** **A gap found and closed here:** U2 required Register-E entries for
        everything Code Cell D newly prints, and U3 closed without writing them. `agent/decisions.md`
        now carries **E15**, classing the couplings and identities (a), BᵀW1 and the constant
        component (a), the σ-limit and same-φ_u blocks (a) with their two σ controls and the θ_u = 1
        control labelled, Part D under both placements (b), and Eq. (D5) itself as a counterfactual
        manipulation (C8). **Nothing in the change is class (e).**
      - **Decisions.** A3 amended (U2) and its Evidence line corrected (U13); R18–R21 in
        `revisions.md` §1; the agent decisions named to the user as they were made (Appendix D's
        retitle in U4, the §4.1 renamings in U10, the normalizer sentence in U9). **Q8 settled by
        the user 2026-09-21: RSA's parameter is α_rsa** → R21, applied in `background_sections.md`
        §§1.2 and 1.3. The notebooks never write RSA's α, so neither changed.
      - **Mirror.** `main.ipynb` is 23 cells; Code Cells 2 and 2b keep the exact `# === Code Cell 2:`
        and `# === Code Cell 2b:` prefixes E3 locates them by; `code cell 1` untouched since the
        checkpoint, so coupling 9 stays quiet.
      - **Execution.** Neither notebook has changed since **U7** (`bf746b1`), which ran both at
        baseline: main 0 errors, 8 figures, 14/14, 249 s; appendix_E 0 errors, 5 figures, E2 18/18,
        E3 PASS, 679 s. U8–U14 touched no notebook, so nothing needed re-running.
      - **Numbers.** Re-checked by script at close: the 68 decimal figures in everything U9–U13
        wrote (the central claim, §§3.2–3.3, 4.1, 4.4, 4.5, §5.1's new bullet, §6, background Beat 2
        and Beat 3) all appear in the stored output of a code cell. C6 holds.
      - **Anchors and numbering.** All 74 ToC links resolve; the body's tags run (1)–(41) complete;
        Appendix D's run (D1)–(D7).
      - **One deviation, reported rather than repaired.** The ten commits from U9 to U13 carry the
        subject line and the attribution but not `agent/agent.md` §4.3's `Why:` and `Verified:` lines;
        U0–U8's commits do. The history is not rewritten for it (that needs the user under §4.5);
        this entry is the record that the tasks were prose-only and that no notebook was executed
        for them.

      **The change is closed.** U4's retitle of Appendix D was **confirmed by the user on
      2026-09-21**, so nothing from this change is left hanging. What it does not touch is the
      standing list of open decisions in `agent/decisions.md`, which the user worked through on
      2026-09-21: O4 deleted, O9 settled, O10, O13 and O14 addressed, leaving **O1, O2 and O8**
      (and O3, still open by the user's own earlier choice). `revisions.md` §7's Q1–Q8 are all
      resolved. Next is **T0–T13** of `agent/history.md` §12.

---

- **P-8. What replaces the trade-off claim, and where it is sourced.** The claim "prior
  concentration buys the first condition and spends the second" motivates the drain keyed to the
  alternative, and it appears at V7 and V9. By G11 it is true of the **floors** and false of the
  five priors. Options: (i) restate it on the floors — §4.5's own result, unchanged — and drop
  "under every prior tested" wherever it appears; (ii) withdraw it entirely and let R2's complexity
  argument carry §5.1 alone; (iii) keep it only inside §4.5 and let §5.1 and §6 point there.
  **Recommendation (i)**, because the result it rests on is untouched and printed, and because
  removing it would leave §6 item 3 with nothing to say about what a level would change. This
  rewrites an interpretive argument, so under `agent/agent.md` §5.4 it is the user's.

- **P-9. Which Λ the anti-exhaustive count is stated at** (V5, V8, V11). Four of five at Λ = 8, two
  of five at Λ = 512. Stating it at Λ = 512 is consistent with the rest of §4.4 and makes the
  direction **something raising Λ removes**, which is R18's counterforce doing visible work — but it
  weakens the Cremers tie, which background §1.3 Beat 3 offers as "a second, independent reason".
  Options: Λ = 512 only; Λ = 8 only, labelled; or both, as the contrast. **Recommendation: both**,
  in one sentence — it costs about 15 words and it is the cleanest demonstration of the commitment.

- **P-10. Whether §4.4 reports one Λ or two.** The notebook keeps both (Part D at Λ = 8, Text cell
  4b at Λ = 512). Reporting only Λ = 512 is cheaper and is where the verdict now lives; reporting
  both is what makes the counterforce visible in the evaluation rather than only asserted in §3.2.
  **Recommendation: the Λ = 512 table, with Λ = 8 as a one-line contrast**, which resolves P-9 the
  same way and joins P-6 to R18.

**Tasks these change.** U9 gains the P-5 statement in §3.3 and the exact warning of G10; U11 gains
the background foreshadowing and the same warning; U12 is no longer a sweep for stragglers but the
worked list V1–V13 above; U10 absorbs V4–V6.

*Full original:* `git show 066f042:procedure_records/ell0_placement_and_counterforce.md`

---

<a id="r14" name="r14"></a>

## 14. One name for the scale's resolution, and what fixes it

*Was* `procedure_records/resolution_naming.md`

**Opened** 2026-09-21 13:25 · **Closed** 2026-09-22 14:36 · 5 commits

**Settled** O1

**Opened by**

> We currently don't have an answer for what fixes delta since we don't include predicates with
> unstable atoms as one of the modeled cases in this phase; in addition, for subsequent phases, I
> don't think we will fix delta at all, it should be a read-out that is derived from a learned
> theta_L. Also, unless the name comes from Xiang's papers, I don't think we should give it a
> separate name from n, since they are essentially the same quantity.

- [x] **N0. Checkpoint** — clean tree at `bc97d29`.
      *(orig:)* **N0. Checkpoint** (`agent/agent.md` §4.2). Record `git rev-parse --short HEAD`.

- [x] **N1. Appendix A (S1)** — done. Eq. (A6) and every δ removed; the gradable case folded under Eq. (A5) as *the same formula, a different source for n*; the open part replaced by O1's decision — this phase stipulates n and models no unstable-atom predicate, the two candidate readings are stated with the position reserved, and a later phase reads n off a learned θ_L rather than fixing it.
      *(orig:)* **N1. Appendix A (S1), markdown.** Under Q-N1(i): Eq. (A6) is removed and its content folded
      into Eq. (A5)'s discussion — the two-part gloss of n, the non-integer reading, the grid cap
      stated once as n < 202.21, and the observation that a counting predicate and a gradable one
      differ in where n comes from and not in the formula. **The open-part paragraph is replaced by
      O1's decision**: this phase stipulates n and says so; the two candidate readings (constant in
      s, constant in ζ) are kept as the statement of what a resolution could mean, with our position
      reserved (Entry 3b); and the position for the next phase is stated — n is not a parameter to
      fix but a **read-out of a learned θ_L** by Eq. (A5), which Eq. (A4) says this phase cannot
      learn while φ_L is clamped. No verdict on which reading is right.

- [x] **N2. Code Cell A (S2)** — done; heading now *(Eq. A5)* and the δ cap line dropped.
      *(orig:)* **N2. Code Cell A (S2).** The δ line goes; the n cap stays. The block heading becomes
      *Eqs. (A5)* rather than *(A5-A6)*. No number that any prose quotes is removed except 0.004945,
      which N1 removes from the prose in the same change.

- [x] **N3. `code cell 1` (S3) and E1 (S4)** — done, mirrored; coupling 9 verified by AST.
      *(orig:)* **N3. `code cell 1` (S3) and E1 (S4).** One comment, mirrored. **Coupling 9 fires**: the two
      cells stay source-identical in this comment, and E1's relay arguments are untouched.

- [x] **N4. ToC (S5)** — (A1)–(A5); all 74 links resolve.
      *(orig:)* **N4. ToC (S5).** Appendix A's row → (A1)–(A5), derived from the cell's own tags, not typed.
      Re-check that all 74 links resolve.

- [x] **N5. Couplings** — verified: tags 61 → 60, exactly {A6} removed, the remaining sequence identical so nothing renumbered; no anchor changed; E3's prefixes untouched.
      *(orig:)* **N5. Couplings.** 5 (equation numbers: (A6) removed, nothing renumbered, no body tag moves),
      6 (anchors), 9 (N3), and E3's prefixes untouched.

  **N5 WAS INCOMPLETE — found 2026-09-22 by an audit the user asked for, and fixed the same day.**
  The check recorded above verified the **supply** side only: that the A6 tag was gone and nothing
  renumbered. It never asked the other question, whether anything still **cites** (A6). Four live
  citations survived the change:
  | Site | Text |
  |---|---|
  | `main.ipynb` cell 5, `code cell 1` docstring | "denotation (Eqs. A5-A6)" |
  | `appendix_E.ipynb` cell 2, E1 | the same, mirrored |
  | `thesis_outline/sections_3-6.md` scope-tier table | "Eqs. (A5)–(A6)" |
  | `thesis_outline/sections_3-6.md` §5.2 setup bullet | "(Eq. A6)" |

  The first two are a **second** A6 reference inside the same docstring N3 edited: S3 recorded one
  comment ("1/delta for a JND delta (Eq. A6, Appendix A)") as the site, that one was removed, and
  this one was not surveyed. N3's own verification, "coupling 9 by AST", compares the two notebooks
  **to each other**, so a defect identical in both copies passes. The last two were never in the
  S1–S8 table at all, which recorded §3.3 (S6) as the outline's only δ site — the same survey gap
  that produced the six missed δ sites N7 had to clean up.

  Fixed: all four now read Eq. (A5), and §5.2's sentence is rewritten to N's own position — the
  gradable case is *the same* Eq. (A5) read with a real n, not a different equation.
  `agent/agent.md` coupling 5 now requires the `cited` ⊆ `defined` direction and carries a check that
  spans both notebooks. **Lesson:** a mirror check cannot catch a defect that is mirrored, and a
  removal check cannot catch what still points at what was removed.


- [x] **N6. Executed** (shared with HA10d): main 0 errors, 8 figures, 14/14, 837 s; appendix_E 0 errors, 5 figures, 18/18, E3 PASS both, 1872 s. Only the expected lines moved.
      *(orig:)* **N6. Execute** main then appendix_E (`agent/agent.md` §5.1). Acceptance: main 0 errors, 8 figures,
      14/14; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS. The only stored-output change should
      be Code Cell A's two lines and `cost:` lines.

- [x] **N7. Prose and records** — done, plus the six missed sites above. `agent/agent.md` §5.5 gains a general rule rather than a one-off: *one quantity, one name* — the resolution is n and never δ, "delta" being reserved for the delta read-out and the delta-like prior.
      *(orig:)* **N7. Prose and records.** `sections_3-6.md` §3.3 (S6) drops the δ clause and states the
      two-part gloss of n in one sentence; `scale_classes_hypothesis.md` §2 (S7) reads n for δ, which
      also makes H1's wording match S-4's n = 4; `agent/decisions.md` O1's 2026-09-15 finding (S8) reads n;
      `agent/agent.md` §5.5's naming list gains the one-name rule if it is the kind of clash that list
      records.

- [x] **N8. Commit** — done.
      *(orig:)* **N8. Commit**, one logical change per commit, hashes recorded above.

**Sequencing note (2026-09-21).** `agent/history.md` §15 (X0–X5, decision O2)
is approved and waiting too. It touches cells 16 and 4 where this list touches 14, 15, 5, 0 and E1,
so the two do not collide, and N6's execution would cover both. Running them in one pass saves an
`appendix_E.ipynb` run of about 11 minutes.

---

*Full original:* `git show 2caaa84:procedure_records/resolution_naming.md`

---

<a id="r15" name="r15"></a>

## 15. The exposure ensemble, stated as a stipulation: its weights and its membership

*Was* `procedure_records/exposure_stipulation.md`

**Opened** 2026-09-21 13:38 · **Closed** 2026-09-22 11:26 · 4 commits

**Settled** O2 (settled), A18, O8's ensemble half

**Opened by**

> go with (a). Again, I think this is essentially the same philosophy as fixing all sigma at 1.


Working record for the change the user approved on 2026-09-21, settling `agent/decisions.md` **O2** (the
ensemble's **weights**) and, from the same day, **A18** and **O8**'s ensemble half (its
**membership**). Pattern: `agent/agent.md` §5.3.

**Task IDs here are `X0`–`X8`.** `N0`–`N8` (`resolution_naming.md`) and `T0`–`T16`
(`scale_classes_hypothesis.md`) are live at the same time; the prefixes keep them apart.

**Status, 2026-09-22: APPLIED.** All nine tasks closed; commit recorded at X5 below. Markdown
only, so no coupling fired and neither notebook was re-executed — verified rather than assumed
(X4). One correction to this record's own site table: Y2's pointer said "Text cell 3 §3, item 3",
but the σ sentence and the "exposure ensemble" clause are in Text cell 3's **preamble** items 3 and
6, not in §3, whose item 3 is the utility basis $B$.

---

#### 1. The decision, in the user's words (2026-09-21)

> go with (a). Again, I think this is essentially the same philosophy as fixing all sigma at 1.

Option (a) of the four put to them: **stipulate uniform p(y) and label it**, rather than argue it
from a principle, fit it to corpus frequencies, or add a sensitivity sweep. Recorded as
`agent/decisions.md` **O2**, settled.

---

#### 2. Why the σ parallel is the right frame, checked

Text cell 3 §3 item 3: "At this phase, the model does not implement any precision inference. Hence,
every variance (σ) is fixed at 1. The value is the multiplicative identity because σ weights a
synaptic connection, so fixing every σ at 1 assigns equal weight to every connection." Text cell 3
§6 keeps the log σ terms "only to mark where a later precision-bearing version would reintroduce
them".

The parallel is exact on three counts, and the prose should use it rather than invent a new frame:

1. **The reason is the same.** A quantity the phase does not model (precision; exposure statistics)
   is fixed at the value that treats every channel, or every utterance, alike.
2. **The stipulated value is the one that makes the quantity vanish from the formula.** σ = 1 gives
   ε_y = r_y and constant log σ terms; uniform p(y) turns 3·E_{p(y)}[c_y] into the bare sum Σ_y c_y
   that Eq. (B3) already writes.
3. **Both are marked for a later phase**, not hidden: precision-bearing for σ, frequency-bearing for
   p(y).

**The one asymmetry, to be stated and not smoothed over.** σ is a variable in the code with a
default of 1, so a precision-bearing phase changes defaults (D11 covers σ ≠ 1). p(y) is not a
variable at all — it is implicit in the batched sum — so a frequency-bearing phase adds a weight
vector. Appendix B's per-presentation check (the batched and per-presentation flows agree to
3e-4) is where that would be felt, since it is exactly the place the ensemble is visited one
utterance at a time.

---

#### 3. Sites

| # | Site | What changes |
|---|---|---|
| Y1 | `main.ipynb` cell 16, Appendix B, the "prior over utterances" sentence | It states the fact and stops. It gains the stipulation, the σ parallel in one clause, and what a later phase would add (a weight vector, not a default) |
| Y2 | `main.ipynb` cell 4, Text cell 3 §3 | Item 3 fixes σ; the exposure stipulation belongs beside it, one sentence, so the two stipulations of the phase are read together. Item 6 already lists "the exposure ensemble" among what fixes θ_u\*, and gains "uniform at this phase" |
| Y3 | `thesis_outline/sections_3-6.md` §5.6 | The exposure prediction reads as a prediction **about departures from a stipulated uniform**, which is what makes it a prediction at all |
| Y4 | `thesis_outline/sections_3-6.md` §5.5 Limits | One clause: results are reported at uniform exposure; a frequency-bearing version is not built |
| Y5 | `thesis_outline/revisions.md` | A site entry for Y3 and Y4, so the outline pass picks them up |
| Y6 | `agent/decisions.md` | O2 settled (done 2026-09-21); A14's "see O2" pointer still reads correctly |

**No code changes and no numbers move**, because uniform is what the code already computes. Nothing
here is printed, so C6 does not arise and neither notebook is re-executed for this change alone.

---

#### 4. Tasks, in order

- [x] **X0. Checkpoint** — clean tree at `f64d32e` (2026-09-22).
      *(original:)* **X0. Checkpoint** (`agent/agent.md` §4.2). Record `git rev-parse --short HEAD`.
- [x] **X1. Appendix B (Y1)** — done. The stipulation and the σ parallel sit with the prior-over-utterances sentence; the asymmetry went to the per-presentation passage instead, since that is the place it would be felt. No claim about how far a non-uniform p(y) moves θ\*.
      *(original:)* **X1. Appendix B (Y1).** The stipulation, the σ parallel, the later-phase note, and the
      asymmetry of §2 in one short passage. It does **not** claim how far a non-uniform p(y) would
      move θ_u\*; that was option (d) and was not adopted. Position reserved (composition guide
      Entry 3b).
- [x] **X2. Text cell 3, preamble items 3 and 6 (Y2)** — done; see the site correction above.
      *(original:)* **X2. Text cell 3 §3 (Y2).** One sentence beside item 3, in item 3's own register, and the
      "uniform at this phase" clause in item 6. No new equation and no new notation: p(y) is already
      named in Appendix B, and if the sentence needs it here it is defined at first use.
- [x] **X3. The outline (Y3, Y4) and `revisions.md` (Y5)** — done: §5.6's exposure prediction now reads as one about departures from a stipulated uniform, §5.5 Limits carries both stipulations, and **R24** records the change.
      *(original:)* **X3. The outline (Y3, Y4) and `revisions.md` (Y5).** Written after X1 and X2, so the paper's
      wording follows the notebook's.
- [x] **X4. Couplings** — confirmed, not assumed: three markdown cells changed and no code cell; equation tags 61 → 61 with none added or removed; no anchor added or removed; stored outputs 41 → 41. So couplings 5, 6 and 9 are quiet, E3 cannot fire, the ToC is unaffected and **no execution is needed**.
      *(original:)* **X4. Couplings.** None is expected to fire: markdown only, no tag added, no anchor added,
      `code cell 1` untouched, E3 unaffected. Confirm rather than assume, and confirm the ToC needs
      no change (no heading and no equation range moves).
- [x] **X5. Commit** — done.
      *(original:)* **X5. Commit.** One logical change per commit, hashes recorded above. **No execution**, so the
      message says `Verified: not run`, with the reason.

**Sequencing note.** If this list runs in the same pass as `resolution_naming.md` N0–N8, X1 and X2
touch cells 16 and 4 while N touches 14, 15, 5, 0 and E1, so nothing collides; N6's execution then
covers both, and X5 folds into N8. Run alone, this change needs no execution at all.

---

#### 5. The membership half (A18, added 2026-09-21)

**The decision.** The ensemble holds at least {χ, ker χ} (Appendix D Eq. (D2)); an antonym is never
needed to define an entry; antonymy is a lexical accident of two words sharing a scale, is not
invertible where ker is, and has no word at all where ker E_all = {1}, the O corner. In this phase
ant(x) may **coincide** with ker(x), which is a prediction of the single θ and is not transported
(O9's pattern). That the inventory holds the pair at all is this phase's stipulation, labelled as
one; under §5.1's proposed level, with at most two entries per level, it becomes a consequence
instead — and that is compatible with O14, since complementarity is **within** a level and O14's
asymmetry is **across** levels.

- [x] **X6. Appendix B and Appendix D** — done. Appendix D §2 takes the membership stipulation, beside Eq. (D2) where ker is defined and where ker E_all = {1} makes the point; Appendix B states membership beside weighting.
      *(original:)* **X6. Appendix B and Appendix D.** Appendix B's ensemble passage says what the ensemble
      contains, beside X1's sentence on how it is weighted, so membership and weights are stated
      together and both are labelled as this phase's stipulations. Appendix D §2, which already
      defines ker and tabulates where it escapes the family, gains the one sentence that the
      inventory holds {χ, ker χ} for any entry — it is the notation's home, and the E_all row is the
      case that makes the point.
- [x] **X7. §5.1 and §5.2** — done. §5.1's cascade is connected to A18 in one clause. §5.2's half went **into T10's task line** rather than into §5.2's prose, because T10 rewrites that section wholesale and prose written now would be overwritten; the constraint is therefore where the writer will read it.
      *(original:)* **X7. §5.1 and §5.2.** §5.1's cascade is already written ⟨E_some, ker E_some⟩ and
      ⟨E_all, ker E_all⟩; one clause connects it to A18 so the design and the commitment read as one
      claim. §5.2 states the ensemble as the inventory's, **not** as the experiment's: F20 shows the
      latin square denies the exposure reading, and the user's principle is that inventory follows
      from exposure but not conversely. It also says that ant coincides with ker for these absolute
      classes in this phase, with no thesis about antonymy.
- [x] **X8. Records** — done: R24 in `revisions.md`, the wording constraint on `scale_classes_hypothesis.md` T10, and this block.
      *(original:)* **X8. Records.** `agent/decisions.md` A18 and O8 are written (2026-09-21); `revisions.md` gains the
      site entries for X6 and X7; `scale_classes_hypothesis.md` T2's block 1 and T10's prose carry
      the wording constraint of X7.

---

#### 6. What this change does not do

- It does not measure the sensitivity of θ_u\* or of the criteria to p(y). Option (d) was declined.
- It does not touch Code Cell B's *ALTERNATIVE SPACES* block, which varies ensemble **membership**
  and is a different probe.
- It does not derive the inventory. A18 fixes what the ensemble contains; why a lexicon contains
  those entries is not this phase's question.
- It does not measure a no-antonym configuration. A18 says the ensemble is {χ, ker χ} whether or not
  a word lexicalizes ker χ, so nothing needs re-running; the audit's ensemble probes stand.

*Full original:* `git show bc97d29:procedure_records/exposure_stipulation.md`

---

<a id="r16" name="r16"></a>

## 16. Halting by tolerance: can the realizable maximizer be defined that way?

*Was* `procedure_records/tolerance_halting.md`

**Opened** 2026-09-21 15:45 · **Closed** 2026-09-22 12:18 · 25 commits

**Settled** A19 (demoted to a direction), D12, I3

**Opened by**

> halting is achieved by tolerance. Currently we have tolerance at 1e-9 (I think), which is an
> arbitrary small number. The need for tolerance for a computer program is because numbers cannot
> be represented exactly. The need for tolerance in a living organism might share the same reason or
> it might not, over which we will not make a claim. But we can make a plausible argument that the
> representative tolerance is almost certainly greater than 1e-9, thus giving an earlier halt. It is
> not within the scope of this study to stipulate the appropriate tolerance that is representative
> of the human brain, and tolerance might not even be uniform across different inference tasks. The
> stipulation that we will commit to in the paper is that tolerance is the mechanism of halt. I
> understand that our current implementation of the realizable maximizer is not defined in terms of
> tolerance, so before adopting my take, the first thing you should inspect is that if the notebook
> …

#### 4. Findings

- **H1. It can be defined that way, and the definition is self-contained.** The rule needs only
  |Δθ_u|, which the flow produces anyway. Unlike both current rules it never mentions θ\*, so R10's
  objection — that every realizable θ_u is located using a closed form the simulated system has no
  access to — **does not apply to it**.

- **H2. No verdict moves, at either Λ.** Part D's rows at Λ = 512, over tolerances from 1e-9 to 1:
  the flat, Beta(3,1) and delta-like priors meet both criteria at every tolerance, the Gaussian and
  Beta(1,3) priors meet neither, exactly as at θ\*. At Λ = 8 no row meets the conjunction at any
  tolerance, as at θ\*.

- **H3. The plane is unchanged, cell by cell.** Both q criteria hold in **33 of 121** cells at every
  tolerance tested, and the halted verdict agrees with the θ\* verdict in **121 of 121** cells.

- **H4. The cost falls by two to three orders of magnitude.** The separation 4λ_max(H) that
  commitment 7 demands, at Λ = 512:

  | | θ\* | tol = 1e-2 | tol = 1e-1 | tol = 1 |
  |---|---:|---:|---:|---:|
  | flat | 9.26e6 | 6.72e4 | 1.50e4 | 1.19e4 |
  | Beta(3,1) | 8.99e6 | 6.75e4 | 1.51e4 | 1.09e4 |
  | delta-like | 7.93e6 | 8.98e4 | 2.02e4 | 4.82e3 |

  θ_halt/θ\* is 0.03 to 0.11 across those rows, and the reported quantities move in the third or
  fourth decimal: the delta-like row's shift is −0.5217 at θ\* and −0.5208 at tol = 1, with
  P(all | *some*) 0.4351 against 0.4361.

- **H5. The rule halts at a slow *start*, not only near the asymptote. Since 2026-09-21 this is a
  prediction of the commitment, not a hazard of it** (the user ruled out any guard; see §6). Under the
  flat prior at Λ = 8, where θ\* = 5950.63, the first update is tiny because ⟨μ_u, Σ_y c_y⟩ is small
  there, so any tolerance ≥ 1e-2 halts after **one update, at θ_u = 0.0005** — the tempered control
  in all but name. The verdict is unchanged (the conjunction fails at θ\* too), but the reported
  shift would be +0.0854 rather than +0.0295 — the tempering alone. The guards once considered here
  (a relative tolerance |Δθ| < tol·|θ|; halting only after the flow has left its start; a minimum
  number of updates) are **rejected**: each requires the system to know something about the shape of
  its own trajectory beyond its local input, which is the commitment's own premise. What the
  commitment predicts instead: **where the flow starts slowly, the system halts at once and the
  belief stays at the tempered control.** Under Λ = 8 that is the flat prior at every coarse
  tolerance tested.

- **H6. A fine tolerance never fires in any plausible number of exposures.** At 1e-9 and 1e-6 at
  Λ = 512 the flow is still at θ_u ≈ 600 after **2,000,000 updates**, against θ\* ≈ 1500. This is
  F15 again, and it is the measured form of the user's argument: a tolerance anywhere near 1e-9 does
  not halt the flow at all, so the halting regime is the coarse one, where 3 to 3,700 updates
  suffice.

- **H7. The fast loop's tolerance is not where the cost lives.** Coarsening `infer`'s tolerance from
  1e-9 to 1e-2 at Λ = 8 leaves every verdict unchanged, moves φ_S by at most 5.2e-3, and saves only
  513 → 152 Euler steps. So "tolerance halts the fast loop" is already true and costs nothing to
  say; the claim that does work is the one about the **slow** flow.

- **H8. WITHDRAWN 2026-09-21 by H9 — the cost columns below are wrong; do not quote them.** They
  price a row by scaling the *settling* step count and never price the *flow*, which is where the
  cost actually is once halting makes the flow long. The θ_halt and update columns are correct and
  are superseded in the more careful form of H10. Kept for the record of what was claimed.
  *(Original text:)* What a committed tolerance costs, measured 2026-09-21 (block 4 of the audit,
  added after the user chose to define `learn_theta_u` by the tolerance itself). Steps are scaled
  from Code Cell 2b's integrated delta-like row (39,035 steps at λ = 180.9), since dt = τ_state/(8λ):

  | tolerance | Λ = 512: θ_halt | updates | an integrated row | Λ = 8: θ_halt |
  |---|---|---|---|---|
  | 1 | 34.7 to 61.4 | 3 to 7 | **12 to 37 s** | −0.34, 0.0005, −0.42, 0.18 — one update everywhere |
  | 1e-1 | 61.1 to 71.1 | 3 to 173 | **27 to 50 s** | −5.29, 0.0005, −4.32, 5.51 |
  | 1e-2 | 129.2 to 149.9 | 3,023 to 3,657 | **166 to 223 s** | −10.59, 0.0005, −8.07, 11.46 |

  The notebook's whole baseline is about 250 s and Code Cell 2b integrates three such rows, so
  **1e-2 is not affordable** (about nine minutes for the three) while 1 and 1e-1 are (about 80 to
  110 s added). At Λ = 512 the halted θ_u of 35 to 71 sits far above the θ_crit of 1.0 to 3.1 at
  which the conjunction is first met, which is the measured form of "the conjunction is reached
  early": it is a fact about the shape of the update, not about where the flow stops.

- **H9. There is an INTEGRABILITY BOUNDARY just above λ = 1206, and H8's cost table is wrong**
  (measured 2026-09-21 at HA4b; `integrability_boundary.py`, `integrability_spectrum.py`,
  `integrability_output.txt`). One `infer` at Λ = 512:

  | θ_u | λ_max | steps | steps/λ | seconds |
  |---:|---:|---:|---:|---:|
  | 13.37 | 180.8 | 39,007 | 215.8 | 1.73 |
  | 34.70 | 1,206.1 | 264,724 | 219.5 | 11.64 |
  | 52.07 | 2,713.3 | 21,706,280 | **8000.0** | 945.50 |
  | 54.43 | 2,964.6 | 23,717,000 | **8000.0** | 1025.57 |
  | 61.27 | 3,756.0 | 30,048,104 | **8000.0** | 1305.24 |
  | 71.09 | 5,055.8 | 40,446,305 | **8000.0** | 1751.29 |

  `infer` sets `max_steps = ceil(max_time / dt)` with `max_time = 1000.0` and
  `dt = tau_state/(8λ)`, so the cap **is** 8000·λ. The four large rows hit it exactly and
  returned **`converged = False`**: they are failures, not expensive successes. Cost is *linear*
  in λ — 219·λ steps at a flat 45 µs/step — up to the boundary, and the integration simply stops
  converging within its time horizon above it. **It is not a condition-number effect**:
  λ_min = 1.00000 at every θ_u tested, so cond = λ_max, and the 219 → 8000 jump is not in the
  spectrum. Why 27 simulated time units suffice below the boundary and 1000 do not above it is
  **not diagnosed**; nothing may be written about the cause until it is.

  **Two corrections this forces.**
  1. **H8's table is withdrawn.** It priced a row by scaling Code Cell 2b's *settling* step count
     and never priced the *flow*, which under halting is 61–173 updates × 3 inferences climbing
     into the non-converging region. Its "12 to 37 s" and "27 to 50 s" are not what a halted row
     costs. H4's 4λ figures stand (they are closed-form) and H2/H3's verdicts stand.
  2. **`FEASIBLE_STIFFNESS` is not the pure machine budget the agent described to the user.** It
     sits just under the convergence boundary — 1206 converges, 2713 does not — so raising it past
     about 1.2e3 admits rows that fail, and the block's
     `RuntimeError("the arrival theta_u was expected to be integrable")` fires. The user's approval
     to raise it was given on the agent's wrong description and **was not acted on**; the point was
     put back to them.

- **H10. What survives at Λ = 512, measured.** The conjunction holds at **every** halted θ_u at
  both tolerances, and the criteria barely move: flat's shift −0.0119 at today's arrival against
  −0.0145 halted; delta-like −0.5182 against −0.5213, with θ\*'s −0.5217. So halting costs no
  verdict (H2 confirmed against the real implementation). Of the three rows, only
  **delta (all) at tol = 1** (θ_u = 34.70, λ = 1206, 11.6 s) is inside the integrability boundary;
  flat (54.43) and skewed high (52.07) at tol = 1 are outside, as are all three at tol = 1e-1.

---


#### 8. HA4b: the open question (2026-09-21)

**Blocking the conversion of call sites 3 and 4.** H9 and H10 are measured; what to do about them
is the user's.

- **The integrability boundary is real and sits between λ = 1206 and λ = 2713.** Above it `infer`
  exhausts `max_time` and returns `converged = False`. Nothing in the model changes; what changes
  is which θ_u the notebook can *exhibit* by integration.
- **At tol = 1, one of the three Λ = 512 rows survives it** (delta (all), θ_u = 34.70, λ = 1206,
  11.6 s). The other two would print the existing "is not run end to end" line with the reason,
  which is an honest report and costs nothing.
- **At tol = 1e-1 none survives it**, so the end-to-end block would report nothing at Λ = 512.
- **The user's proposal (2026-09-21): tolerance is a function of the case's Λ**, with 1e-1 at
  Λ = 8 and 1 at Λ = 512 as ad hoc demonstration values, the hypothesis to be stated in the
  outline. **The premise the user was given for it — that cost is super-linear in λ — was the
  agent's error and is withdrawn (H9).** The hypothesis keeps independent, measured support: a
  *fixed* absolute tolerance buys very different amounts of flow at different Λ (15 updates at
  Λ = 8 against 61–173 at Λ = 512 for the same 1e-1), because the gradient's scale grows with Λ.
  If the hypothesis is stated, it must rest on that and **not** on the withdrawn cost claim.
- **Note for whoever writes it:** a tolerance keyed to Λ is *not* the relative tolerance
  |Δθ| < tol·|θ| that H5 rejects as a guard. Λ is a standing property of the configuration, fixed
  before the flow starts; |θ| is where the trajectory currently is. The first is a stipulation
  about the case, the second is the system reading its own trajectory, which is what the user
  ruled out. The outline should draw that line explicitly, or the two will be confused.
- **Not diagnosed:** why the settling time crosses from ~27 to >1000 simulated time units. No
  claim about the cause goes anywhere until it is.

- **H11. The printed cost extrapolation to θ\* is unsupported above the boundary** (2026-09-21).
  Code Cell 2b prints, for each end-to-end row, *"the same inference at theta_u\* = 1521.5 would be
  4.99e+08 steps, about 6.3 h"* (and 4.85e8 / 6.1 h, 4.28e8 / 5.5 h). That number is
  `steps_per_rate * star_rate`, i.e. the **linear** 219·λ model, extrapolated from λ ≈ 1.8e2 to
  λ ≈ 2.3e6 — four orders of magnitude, across the boundary H9 measures at λ ≈ 2e3, above which the
  integration does not converge at all. At θ\* the step cap alone is 8000·λ ≈ 1.85e10 steps, about
  230 h, and the run would end at the cap rather than at a fixed point.
  **The direction of the claim is unharmed and in fact strengthened** — θ\* is further out of reach
  than the notebook says, not nearer — so §4.6's argument and the outline's line (`revisions.md`
  line 449: "4.28e8 steps, hours, at a separation of 7.9e6") survive in substance. But the *number*
  is a linear extrapolation through a regime change and may not be printed as a measurement. Either
  it is replaced by the cap (a lower bound on the steps, with non-convergence stated) or the claim
  is made qualitatively. **Not yet changed**; it is part of HA4b.

- **H12. The convergence boundary is DIAGNOSED: a roundoff floor that grows as θ_u², against a
  fixed stopping tolerance** (2026-09-21, `why_it_stops_converging.py`,
  `why_it_stops_converging_output.txt`). It is **neither** of the two candidates named when H9 was
  recorded — not a slow mode of the dynamics, and not an instability of explicit Euler.

  **The dynamics settle just as fast on both sides of it.** max|derivative| decays exponentially at
  rate ≈ 1 per simulated time unit (the rate λ_min = 1 predicts) and reaches its floor by t ≈ 37 at
  either θ_u, then sits there unchanged to t = 166:

  | | θ_u = 34.70 (λ = 1206) | θ_u = 52.07 (λ = 2713) |
  |---|---|---|
  | t ≈ 10 | 1.668e-2 | 5.277e-2 |
  | t ≈ 20 | 5.254e-7 | 5.276e-2 → 5.254e-6 at t = 18 |
  | t ≈ 37–41 | **5.484e-10** | **1.234e-9** |
  | t ≈ 74–166 | 5.484e-10 (unchanged) | 1.234e-9 (unchanged) |

  **What differs is only the floor's height**, and the floor is a clean square law in θ_u:

  | θ_u | 13.37 | 20.00 | 34.70 | 42.00 | 46.90 | 52.07 | 61.27 |
  |---|---|---|---|---|---|---|---|
  | floor | 8.220e-11 | 1.828e-10 | 5.484e-10 | 8.031e-10 | 1.001e-9 | 1.234e-9 | 1.708e-9 |
  | /θ_u² | 4.598e-13 | 4.570e-13 | 4.555e-13 | 4.553e-13 | 4.551e-13 | 4.551e-13 | 4.550e-13 |
  | converges | yes | yes | yes | yes | **no** | no | no |

  **floor = 4.55e-13 · θ_u²**, constant to three figures over a 4.6-fold range, crossing the 1e-9
  tolerance at **θ_u = 46.6, λ = 2177** — with 42.00 the last success measured and 46.90 the first
  failure. Above the crossing the derivative can never fall below the tolerance, so the test cannot
  fire however long the run, and it ends at the cap.

  **Why quadratic:** θ_u enters the roundoff twice — the residuals carry it, and `phi_u_dot`
  multiplies the state error by it again (`-eps_utility + theta * project(eps_state)`).
  max|φ_S| ≈ 856 at *both* θ_u, so this is **not** the state growing.

  **What it means.** The boundary is a property of **the stopping tolerance**, not of the model, the
  integrator, or the machine's speed. I3 set 1e-9 above the roundoff floor measured at the θ_u of
  the time (F34: 8e-11 to 1.6e-10 — consistent with this law at θ_u ≈ 13–19). **The principle was
  right; the constant does not travel.** Applying I3's own principle consistently — a tolerance that
  sits above the floor at the θ_u actually being integrated — would restore convergence at every
  θ_u the halting flow reaches, and would let all three Λ = 512 rows run end to end instead of one.
  **That is a change to I3 and is the user's**; see §9.

---


#### 10. HA9: the flow is integrated twice per row (2026-09-21, user approved)

**The finding.** After HA6, `realizability_report` integrates Eq. (20)'s flow to its halt for each
end-to-end row (printed: **80.61 s**, **75.19 s**, **145.24 s** at Λ = 512), and then
`delta_readout_report` integrates *the same flow again*, from the same start with the same
arguments, purely to arrive at the same θ_u for its "realizable" row. At one update — what the
criterion-stop used to give — this cost nothing and nobody noticed. At 3 to 7 updates climbing to
θ_u ≈ 54 it is about **300 s**, roughly a quarter of the run's whole increase.

**Why it is safe to remove, and what it is not.** What the delta read-out *demonstrates* is the
**settling** at that θ_u — Eqs. (18)–(19) integrated, which is what its `"integrated"` tag marks —
not the flow that reached it. The flow has already been integrated, in the block above, and
`realizability_report` records where it landed in `row["run"]["theta_u"]`. Taking that value is
therefore not a substitution of closed form for dynamics: it is **the value the integrated flow
actually reached**, reused instead of recomputed. (`halt_by_tolerance`'s closed-form value agrees
with it to better than 1e-13, but `row["run"]["theta_u"]` is preferred precisely because it is the
integrated one.)

**Prediction: no printed number moves.** `learn_theta_u` is deterministic and both calls start from
the same respawned network with the same arguments, so the second run reproduces the first exactly.
The only expected difference is runtime. **If any number does move, that is a finding about
determinism and is reported, not absorbed.**

- [x] **HA9a** done 2026-09-21. Three lines in `delta_readout_report`, mirrored into E2.
- [x] **HA9b** done. **The prediction held: no printed number moved.** All 69 lines of the
      function's own output matched the stored copy exactly. The two lines the first comparison
      flagged were an artifact of it running past the end of the function into Code Cell 2b's own
      printing — checked by confirming that header appears nowhere in Code Cell 2's source, rather
      than assumed. Measured: `delta_readout_report` **184.0 s** against about 485 s before, with
      `realizability_report` unchanged at 527.8 s.
- [x] **HA9c** done. **main: 0 errors, 8 figures, 14/14, 839 s** (from 1154 s, −315 s).
      **appendix_E: 0 errors, 5 figures, 18/18, E3 PASS both cells, 1961 s** (from 2516 s, −555 s).
      E3's counts unchanged at 221 and 261 identical lines with the same pattern.
      **Verified that nothing but runtime moved**, by diffing every stored output line against
      `bc3a261`: Code Cell 2b's output is **300 lines before and after**, and the only differences
      are the wall-clock seconds and µs/step inside `cost:` lines (26.06 → 25.38 s, 45 → 44 µs/step
      and so on). **Every step count is byte-identical** — 574,120, 527,295, 242,163 — as are all
      reported quantities. Those `cost:` lines are what `agent/agent.md` §5.2 calls machine quantities and
      what E3 skips for that reason.

- **H19. R23's first evidence was cherry-picked across priors; corrected 2026-09-22**
  (`lambda_and_tolerance.py`, `lambda_and_tolerance_output.txt`). The footnote's draft said *"the
  same 1e-1 halts the Λ = 8 flow after 15 updates and the Λ = 512 flow only after 61 to 173"*. The
  15 is the **gaussian** prior at Λ = 8; the 61–173 are **flat, skewed high and delta** at Λ = 512.
  Matched by prior at 1e-1 the counts are 15 → 13, 1 → 61, 13 → 3, 16 → 77, 3 → 173: **two of five
  fall**, because prior-specific slow starts (H5) dominate at that tolerance. The agent wrote the
  draft; the error is its own, not the user's.

  **What the matched data does support, and it is stronger:**
  - at **tol = 1, every one of the five priors takes three times as many updates at Λ = 512** than
    at Λ = 8 (1 → 3, and 3 → 7 for the delta-like row) — uniform, no selection possible;
  - at **tol = 1e-2** the rows that are not slow-started go up **11 to 17 fold** (245 → 3042,
    173 → 3023, 280 → 3111);
  - and the sharper observation, which the user chose for the footnote: **at Λ = 512 the flow halts
    at 3.5% to 5% of θ\* under every prior and across a tenfold change of tolerance** (0.0347 to
    0.0505), while at Λ = 8 the same tolerances land anywhere from **0% to 30%**. At large Λ the
    tolerance barely moves where the flow lands.

  **The user's decision (2026-09-22):** state the claim qualitatively in the footnote and cite the
  audit for the numbers, adding the 3.5–5% observation. No notebook change and no re-execution: a
  matched comparison is not printed anywhere, precisely because `DEMONSTRATION_TOLERANCE` is keyed
  to Λ, and printing one would have cost a ~50 minute re-run for a single footnote.


---


#### 11. HA10: the notebook sites the demotion touches (batched, 2026-09-22)

**Batched deliberately**: each needs a re-execution of both notebooks (~50 minutes), so they wait
for a pass that has another reason to run. None of them affects a computed value.

- [x] **HA10a** — done 2026-09-22.
      *(orig:)* **HA10a.** `learn_theta_u`'s docstring, both notebooks: *"This study commits to halting BY a
      tolerance, not to any particular tolerance"* → offers it as a direction, with a pointer to
      D12's unsettled violation. Comment only; no behaviour.
- [x] **HA10b** — done.
      *(orig:)* **HA10b.** The `DEMONSTRATION_TOLERANCE` comment block, both notebooks: same phrase, same
      fix.
- [x] **HA10c** — done. The printed lines now state two facts and no position: the flow stopped at this tolerance, which is ad hoc; θ\* above is Eq. (B2)'s closed form, computed without one.
      *(orig:)* **HA10c.** `theta_u_learning_probe`'s **printed** line, *"That value is AD HOC. The
      commitment is that halting is BY a tolerance, not that it takes any particular value, so what
      is PREDICTED is theta_u\* above."* **This one is a defect independent of the demotion**: it
      is a position stated in the notebook's own output, which **B10/C7 forbids** — the notebooks
      report measurements and take no position. The agent introduced it at HA4a and should not
      have. It becomes a description of what the code does (the flow halts at this tolerance; θ\*
      is what the closed form reports) with the interpretation left to the paper.
- [x] **HA10d** — done, in one pass shared with N6. main 14/14 in 837 s, appendix_E 18/18 and E3 PASS in 1872 s. Diffed against `bc97d29`: the ONLY non-timing output changes are HA10c's three lines becoming two, N2's heading and δ line, and E3's counts following mechanically (222 → 221 recorded, 221 → 220 identical). No verdict and no reported quantity moved.
      *(orig:)* **HA10d.** Re-execute both, confirm 14/14, 18/18, E3 PASS, and that only these lines move.

- [x] **HA0. Checkpoint** (`agent/agent.md` §4.2), before any code cell is touched. **Clean tree,
      `f07db5d`** (2026-09-21). No uncommitted work of the user's was present, so §4.2 step 2
      applies and the current commit is the checkpoint; no `backups/` folder is needed, since every
      file this change touches is tracked.

- [x] **HA1. `code cell 1`, `learn_theta_u`** under Q-HA1 — done 2026-09-21, commit recorded below.
      The rule: `step = (tau_state/tau_theta)*gradient`, applied, then `abs(step) < tolerance`
      halts. `tolerance` is **keyword-only with no default**, so no run can inherit an ad hoc value
      silently (A19 point 2) and every call site must name the value it is demonstrating at.
      `num_updates` becomes a cap that **raises `RuntimeError`** when reached — the user's
      instruction of 2026-09-21: *"when it is hit it should raise a runtime error. If any of our
      cases ended up incurring a runtime error, then we need to report it as such."* Two guards
      added (`tolerance <= 0`, `num_updates < 1`), both `ValueError`, neither about the
      trajectory's shape. The docstring gains three paragraphs: the rule and that it reads only the
      unit's own last step, the ad hoc status of the value with θ\* as the tolerance-free
      prediction, and the cap's meaning.
      **Coupling 9 holds**: the two definitions were already byte-identical here (the relay lives
      in `theta_u_gradient`, not in this def), so the same four replacements were applied to E1's
      own copy, and the two are verified source-identical after the edit.
      **Verified** against block 5 by integrating the real flow (not the audit's rebuild) through
      the edited cell: at Λ = 8, flat halts after 1 update at θ_u = **+0.000495** at both 1e-1 and
      1, gaussian after 1 update at **−0.340933** at 1 — the audit's 0.0005 and −0.3409. The cap
      raises with the last step's size, the tolerance and θ_u in the message; omitting `tolerance`
      is a `TypeError`.
      **Consequence carried to HA4:** the eight call sites (four per notebook) now fail with a
      `TypeError` until they name a tolerance, so **neither notebook executes between HA1 and
      HA4.** This is deliberate — a default would have hidden exactly the quantity A19 refuses to
      commit to — and it is why HA1's commit says `Verified: not run`.

- [x] **HA2. `infer`'s docstring and I3** — done 2026-09-21. **The task as written is void**: it
      said the 1e-9 "keeps its value" and "no behaviour changes", which H12 refuted. What was done:
      `infer`'s docstring in both notebooks carries the floor law and the keyed tolerance;
      `agent/decisions.md` **I3 is rewritten** as `DERIVATIVE_TOLERANCE_PER_RATE x lambda_max(H)`, keeping
      its 2026-09-13 reasoning as the *reason for* the revision rather than against it, and noting
      that its old claim of "two orders inside the checks' 1e-8" was one order even then;
      `agent/decisions.md` **A19 point 5 is revised** — the fast loop's tolerance is *not* inconsequential,
      H7 having been measured at Λ = 8 where the question does not arise; **F34 is annotated** in
      `theta_u_learned_reach.md` to say its 8.2e-11–1.6e-10 band is the floor *at that θ_u* and the
      law is 4.547e-13·λ_max(H), so F34's conclusion generalizes while the single fixed tolerance it
      licensed does not; and **`agent/agent.md` §5.2's rule** now states that the floor scales, so the
      tolerance does, and that any threshold bounding a tolerance-linked quantity is expressed in
      multiples of the tolerance rather than as a constant.

- [x] **HA3. Text cell 3 §8.5** — done 2026-09-21. Three paragraphs replace the old one, whose
      stated reason for not reaching θ\* was "a run of the length the evaluation can afford" — the
      pre-A19 framing, in which a fixed update count was the stopping rule. Now: **how the flow
      stops** (|Δθ_u| < tol, the only rule, reading the unit's own last step and nothing about the
      trajectory; the fast subsystem stopping the same way at its own timescale, with a tolerance
      scaling as λ_max(H)); **the value is ad hoc and what is reported does not use it** (θ\* as the
      asymptote carrying no tolerance, a flow-derived θ_u labelled realizable and carrying its
      tolerance on its face); and **two consequences stated as consequences** — a plausible
      tolerance halts well short of θ\*, and a slow start halts at once at the tempered control.
      Per B10/C7 the cell takes no position on whether a living system needs a tolerance for the
      reason a floating-point computation does; it says only that this study does not fix one.

- [x] **HA4. Appendix B and Text cell 4's realizability block** — closed 2026-09-21 by HA4a, HA4b
      and HA4c below; the recomputation Q-HA2 settles.
      Every realizable θ_u is the tolerance-halted one, reported at the demonstration tolerance and
      labelled with it; the fact that the conjunction is met well before the halt moves into prose,
      on H8's numbers. C6 applies — each quoted number is printed by the cell that reports it.
  - [x] **HA4a. Call sites 1 and 2**, done 2026-09-21, commit recorded below. Code Cell 2 gains two
        named constants beside `FEASIBLE_STIFFNESS`: `DEMONSTRATION_TOLERANCE = 1.0e-1`, commented
        as ad hoc and named once so every row halted by it prints it, and `HALTING_CAP = 100_000`,
        commented as a cap and not a stopping rule. **Site 1**, `check_specification`'s
        "Eq. (20) ascends toward it from theta_u = 0": was 25 fixed updates, now halts at the
        demonstration tolerance after **15 updates at θ_u = −5.285227** (default Λ = 8,
        θ\* = −28.4375), F~ monotone, |grad| 6.82 → 2.00. **Site 2**,
        `theta_u_learning_probe`: `num_updates=60` is replaced by `tolerance`, defaulting to the
        named constant **which the block now prints**, so the ad hoc value is never invisible; the
        SLOW PARAMETER line becomes "0.0000 → −5.285227, halted after 15 update(s)" in place of
        "over 60 updates", and the settled/still-ascending clause becomes the halting relation (the
        final gradient −1.997 gives a step of 0.0999, just under 0.1).
        **Both sites got cheaper**, 15 updates against 25 and 60.
        **One dependence to keep visible:** site 1's clause that |grad| shrinks needs two updates,
        so a tolerance coarse enough to halt after one (≥ 1 at Λ = 8, block 5) makes that check
        **fail** rather than pass vacuously. That is deliberate and is commented in the cell — a
        silent weakening would have been the patchwork the user ruled out.
  - [x] **HA4b. Call sites 3 and 4**, done 2026-09-21, commit `d8c93ef`. New helper
        `halt_by_tolerance` applies `learn_theta_u`'s rule at the closed-form equilibrium, so the
        survey stays affordable; the end-to-end run integrates the flow and lands on it to better
        than **1e-13**. The realizability block is now **two tables** — where the flow halts (the
        realizable θ_u) and where the conjunction is first met, the second labelled in the OUTPUT
        as a fact about the shape of the update and not a halting rule. `DEMONSTRATION_TOLERANCE`
        is keyed to Λ, `{8.0: 1e-1, 512.0: 1}`, strict (an unlisted Λ raises).
        `FEASIBLE_STIFFNESS` 1.0e3 → **1.3e3**, just above 1206. The H11 cost line is replaced by
        `infer`'s own cap as a lower bound. The roundoff-floor block's leftover `arrival` reference
        (a `NameError`) is fixed to the halted θ_u.
        **Measured:** Λ = 8 block 0.0 s; Λ = 512 block **377.5 s**, of which the 7 integrated
        updates of the flow are 149 s and the settle 11.7 s — so **the flow, not the settling, is
        where the time goes**, which is exactly the assumption H8 got backwards. At Λ = 512 only
        `delta (all)` is inside the gate; `flat` and `skewed high` print the not-run-end-to-end
        line with their λ and the reason.
  - [x] **HA4c. The prose half**, done 2026-09-21. Written AFTER execution, not before: the
        passages carry ~25 numbers that the tolerance change moves, and C6 makes a number class (e)
        until a cell prints it, so writing them from the audit first would have been two passes and
        four C6 violations. **Appendix B**: the 60-update run to θ_u = −7.567 and "an integration of
        affordable length does not arrive" are replaced by the halt (15 updates, θ_u = −5.285227,
        gradient −1.997) and the division of labour — θ\* the tolerance-free asymptote, a
        flow-derived θ_u *realizable* and carrying its tolerance. **Text cell 4**: the tolerance
        paragraphs ("made badly at first" → "got wrong twice, in the same way"); the gate as a
        wall-clock budget at 3e3, with every Λ = 512 row integrated at its halt though none at θ\*;
        and the end-to-end rows as halts (54.429, 52.065, 34.695 after 3, 3, 7 updates) with the
        conjunction's early arrival moved into its own sentence as a fact about the shape of the
        update. 4λ now quoted at three scales: 12–46 at the thresholds, 4.8e3–1.5e4 at the halts,
        7.9e6–9.3e6 at θ\*.
        **A C6 violation in the agent's own first draft, caught and fixed:** it quoted the floor
        coefficient, the old tolerance's margins, the 31-step drift and the crossing λ, all from the
        audit. Rather than trim the argument, the floor block now **prints** the coefficient
        (4.547e-13, 4.547e-13, 4.548e-13 at three λ) and the counterfactual — what a fixed 1e-9
        would have bought there (0.74, 0.81, 1.82 floors, the first two **below** the floor) and the
        λ at which it equals the floor (2199). The notebook now justifies its own tolerance rule.

- [x] **HA5. Couplings and numbering** — done 2026-09-21. Coupling 5 quiet (no equation tag added
      or moved); 6 quiet (no anchor added; Text cell 3's `tc3-8-5` anchors verified intact);
      **coupling 9 verified by AST**: `learn_theta_u`, `halt_by_tolerance` and
      `demonstration_tolerance` are source-identical across main and E1/E2, and all five new
      constants are present in both. `infer` differs, **correctly** — E1's carries the relay — and a
      line-by-line diff confirms the difference is the relay, the spectral guard and pre-existing
      formatting, while the three tolerance lines are identical. **E3 PASS on both cells.** ToC
      untouched: no heading moved.

- [x] **HA6. Executed** 2026-09-21 (`agent/agent.md` §5.1), main twice (the second time to print the
      floor coefficient the prose needed). **main: 0 errors, 8 figures, 14/14, 1154 s.
      appendix_E: 0 errors, 5 figures, 18/18, E3 PASS on both cells, 2516 s.**
      **Departures from the recorded baseline, reported not explained away.** Runtime: 250 s → 1154 s
      and 710 s → 2516 s, because three Λ = 512 rows are integrated end to end where one was, and
      the flow itself is now integrated to its halt (the flat row: 80.6 s of flow against 26.4 s of
      settling). E3's counts move because the cells print more lines — Code Cell 2 goes 203 → **221**
      identical and Code Cell 2b 234 → **261**, while the *pattern* the baseline records is
      unchanged: 1 changed (the pass count) and 4 inserted (the checks the relay adds) in Code Cell
      2, nothing at all in 2b. Step counts fall everywhere the tolerance coarsens: an inference at
      θ_u\* takes **138,390–138,398** steps against 148,081–148,104, about 6.5% fewer.
      **C6 swept over every markdown cell of both notebooks.** Three numbers were stale *because of
      this change* — φ_u\* at the realizable θ_u ([+71.1166,−39.1606] → **[+27.6730,−15.2423]**),
      φ_S\*'s extremes there (139.18/−852.64 → **140.50/−856.51**), and the θ_u\* step count — all
      three fixed. **Eight pre-existing C6 violations were found and are NOT this change's**: cell
      10's 0.2122 and cell 12's 0.0095, 0.0445, 0.1512, 0.5477, 4096, 0.0002 and 13378, identical
      before and after. Reported to the user; not touched here.

- [x] **HA7. The outline** — done 2026-09-21/22.
      **`revisions.md` Item 2 (§5.3's plan) revised in six places**, because A19 falsified the
      premise the section was built on. It was written around the *absence* of a halting mechanism;
      one now exists. Changed: the fast loop's tolerance is no longer "a numerical surrogate... not
      the halting in question" but the same mechanism at the other timescale (I3 revised); a new
      bullet states what halts the flow, that no guard is attached and why, the ad hoc status of the
      value, and the two implications; the cost figure 724 at θ_u = 13.37 becomes **4,823 at the
      halted θ_u = 34.695**; the "consequence without the alternatives level" bullet is marked as
      **answered in part** — the mechanism was supplied, the locality and Bogacz-divergence argument
      it asks for is still owed and unwritten.
      **R10's bullet keeps its conclusion and reverses its reason.** θ\* stays the commitment not
      because no mechanism exists but because **the tolerance is ad hoc**. The two old stopping
      rules are recorded as retained and relabelled — they measure where the conjunction is first
      met, a fact about the shape of the update — not deleted.
      **Two stale numbers fixed** (H11): the evidence block's "4.28e8 steps, hours" → **3.98e8,
      about 5.0 hours**, and the realizable run's 39,035 steps at θ_u = 13.3749 → **242,163 at
      34.695**, with Δ_some −0.5182 → **−0.5208** and q_H 0.4386 → **0.4361**. §8's source-trace
      table follows, and gains two rows for the roundoff-floor quantities and Part A's ratios.
      **R22 corrected**: it claimed the halted verdicts come "at 1e-4 of the cost". Measured, both
      the separation (9.3e6 → 1.19e4) and the step count (4.48e8 → 5.74e5) are near **1/780**, so it
      is about **1e-3** — the row overstated it by an order of magnitude.
      **`sections_3-6.md` §5.5 Limits** gains a halting bullet. **§3.4 needs nothing**: HA3
      introduced no notation, only prose.
      **Flagged to the user, not decided:** (i) §5.5's bullet list now runs about 199 words against
      a drafted-section budget of 80, and it carried six topics before this seventh; (ii) R23's
      footnote quotes "61 to 173 updates at Λ = 512 under 1e-1", which is an audit figure — the
      notebook demonstrates Λ = 512 at tolerance 1, so the paper will need either a source line or a
      different illustration.

- [x] **HA8. Commit** — done throughout, one logical change per commit, hashes on each task line.
      The A19 change closed at `a582bb8` (2026-09-22); **HA10 remains batched**.

**What stays untouched, by the user's scope line:** A9, R10, the θ\* tables, the plane, and
§§4.1–4.5. The audit's H2–H4 are evidence for the discussion, not new results to print, and they
stay class (e) unless a cell is later asked to print them.

**Corrected at HA0:** this paragraph used to begin "every reported number", which Q-HA2's answer
makes false. The realizable rows move, because they are now defined by the tolerance. What the scope
line protects is everything the paper reports **as a prediction** — and those are at θ\*.

---

*Full original:* `git show 7754cb5:procedure_records/tolerance_halting.md`

---

<a id="r17" name="r17"></a>

## 17. The node count K: printing what was found, and what it implies

*Was* `agent/node_count_2026-09-24.md` (folded under `agent/agent.md` §5.3 on 2026-09-24)

**Opened** 2026-09-24 12:25 · **Closed** 2026-09-24 · 4 commits

**Settled** I6 (the K half printed, and corrected), I10 (NK1's placement), E19; revisions.md §15

**Opened by**

> Now can you check if we have every tried accuracies other than K = 10?

> I see. The trend towards finer K is worth reporting. However, I am more interested in the trend
> towards coarser K, since that informs us the minimum complexity required before things become
> unpredictive.

> No need. Print what we have found so far in an appropriate place the notebook. In the outline,
> discuss the implications and direction of future investigation regarding this issue. Now plan
> your tasks regarding this.

"No need" declined the aligned-grid audit (θ_L held on a Voronoi boundary at every K); it entered
the outline as a direction instead.

**NK-D1, the user's ruling**

> No to the 4.2 guard. we don't know the lower bound of K yet, so we don't want to add that to the
> guard as if we know it. What we need in the outline is a warning to the reader on a suspected
> lower bound of K and pointer to the relevant section that discusses what we know about it.

So the lower bound is **suspected, not established**, everywhere it is written, and §4.2's guard
stays with n and Z. **Confirmed by the user at close (2026-09-24, "All confirmed")**: NK1's
placement in Code Cell A, and the reading that the outline's headline counts carry no per-site K
qualifier, their spread across K being reported once, in §5.5.

#### Tasks

- [x] **NK0** (2026-09-24): checkpoint, `git status` clean at `5e755a1`.
- [x] **NK1**: Code Cell A's `node_count_report`, after `peak_locality_report`: the floor (K = 401
  against 801); the finer end (Part D's nine rows at K = 101 to 1601 with P(all), the plane's six
  counts and reversals at K = 101 to 801, and the cells that move); the coarse end (odd K from 101
  to 5: spacing, nodes in the region, first node and lower edge against θ_L, the two conjunctions,
  agreement with K = 801, Part D of 36); the smooth-mask control at sharpness 0.1. Reproduces all
  four audit outputs digit for digit; about a second. `09ea547`.
- [x] **NK2**: both notebooks executed; acceptance met (NK-F5). `09ea547`.
- [x] **NK3**: Appendix A, "A third axis: the node count", after the neighbour-comparison paragraph
  (which the block follows); it suggests a lower bound without establishing one. `09ea547`.
- [x] **NK4**: Text cell 3 §1 — refining K converges the settled fields and the expectations read
  from them; a criterion's status can still change at a boundary cell. `09ea547`.
- [x] **NK5**: "at K = 101" at the first quote of each count per text cell (NK-F8). `09ea547`.
- [x] **NK6–NK8**: `sections_3-6.md` §4.3 warning and §5.5 bullet with four directions; §4.3
  105 → 145, §5.5 465 → 645, Total 6,210; `revisions.md` §15. `01955cd`.
- [x] **NK9**: I6 finding (printed; seven cells; the lower edge), I10 finding, E19. `a32d059`.
- [x] **NK10**: C6 sweep (NK-F7), references checked (NK-F9), this fold.

#### Findings

- **NK-F1 (NK1): seven plane cells move at the finer end, not five.** The audit's
  `plane_flips.py` checked q shift, q position and the two conjunctions only; the printed list adds
  (α 16, Λ 32) in mode position and (α 32, Λ 8) in mode shift. The record's own summary and I6's first
  finding said five; the outline quotes seven.
- **NK-F2 (NK1): the column that sorts the coarse rungs is the lower edge, not the first node.**
  The plan asked for the distance from θ_L to the first node inside the cell. That column is
  +0.056 on K = 101, 81 and 61 as well, which track the fine grid, so it does not separate
  anything. Under the trapezoidal weights the first node inside carries the interval down to the
  midpoint with the node below; that midpoint minus θ_L does sort the rungs (negative: q
  conjunction 33, 32, 29, 24, 9, 0 as it grows; +0.056: 32 to 39). Both columns are printed, and
  I6's "node at ζ = 3.0" account is corrected in a new finding there.
- **NK-F3 (NK1): at a fixed lower-edge offset, agreement still falls with the spacing** (q shift
  116 of 121 at K = 51, 76 at K = 7, all at +0.056). So placement does not account for all of the
  coarse end, and the ladder already separates the two in part. It still does not establish a
  bound: the offset is held only at one value, never at zero.
- **NK-F4 (NK6): the outline's §4.3 and §5.5 were drafted while NK2 ran**, from the prototype's
  output, whose code is identical to the cell's; every number is checked against the executed
  cell before commit.
- **NK-F5 (NK2): acceptance met.** main 0 errors, 8 figures; appendix_E 0 errors, 5 figures; 15/15;
  E3 PASS (223 identical / 1 changed / 4 inserted; 263). Against NK0 only Code Cell A's output
  changed, apart from Code Cell 2b's and E2b's machine-timing `cost:` lines. main was run a second
  time after NK-F6's fix; the diff between the two runs is the header lines alone.
- **NK-F6: the block's header and Appendix A cited Eq. (2) for the trapezoidal weights.** Eq. (2) is
  the quadrature inner product, and Text cell 3 §1 says only "fixed positive quadrature weights";
  the trapezoidal rule lives in Code Cell 1's `build_grid`. Both now cite `build_grid`.
- **NK-F7 (C6 sweep): two derived numbers replaced by printed ones.** "Within four cells of the
  floor" became the printed ranges (119–121 at the floor, 117–120 at K = 81), and "three statuses
  change at K = 61" became "only 33 of 36 agree". Every numeral in Appendix A's new paragraph is
  found in Code Cell A's output.
- **NK-F8 (NK5): the K = 101 clause went to the first quote of each count per text cell**, three
  sites (Text cell 4's band of 33; Text cell 6's 33 and 13), not all six, so as not to repeat it.
  The agent's scoping, named to the user.
- **NK-F9 (§4.3): the warning was placed after the refinement/half-width pair, and E3's sentence
  before it**, so that "the companion to that one" keeps its antecedent and E3's "every one of these
  numbers" does not appear to cover Code Cell A, which E3 does not replay.

---

*Full original:* `git show a32d059:agent/node_count_2026-09-24.md`

---

<a id="r18" name="r18"></a>

## 18. The outline's organization, and what belongs in the notebook

*Was* `agent/review_2026-09-24_outline_organization.md` (folded under `agent/agent.md` §5.3 on 2026-09-24)

**Opened** 2026-09-24 14:19 · **Closed** 2026-09-24 · 5 commits to the record; the change itself is
`5fb809a`, `83aa693`, `b777247`, `f08ad77`

**Settled** OR-D1 (the line between result and technicality), OR9 (§4 split into §4.1 and §4.2);
revisions.md §16. **Confirmed by the user** ("Your decisions are confirmed"; "I agree with your
organization"; "approved. Start."), and folded at the user's instruction.

#### 1. The user's instruction

> Now review the entire outline and inspect the organization of content. Determine:
>
> 1. if any organization should be improved
> 2. if any content should be in the notebook instead following the rule that rationale and
>    discussions belong to the dissertation while technicality belongs to the notebook.
> 3. if any content in the outline already overlap with content in the notwbook. These should be
>    replaced by a pointer to the notebook.

**Scope read as**: `thesis_outline/sections_3-6.md` and `thesis_outline/background_sections.md`.
`thesis_outline/revisions.md` is the revision log, not the outline, and is where bookkeeping moved
out of the two files would go.

#### 2. The line between "result" and "technicality" (OR-D1, confirmed by the user 2026-09-24)

A dissertation's §4 must report results, and a pointer cannot replace a number the discussion argues
from. The agent's line, **confirmed by the user**:

- **Stays in the outline:** every rationale and discussion; every number a claim in §§4–6 argues
  from (§4.4's table; the 33 and 13; the 15 and 9; one ladder figure per guard); the drafting
  guards a writer needs ("never write …").
- **Becomes a pointer:** derivations; verification and precision figures (1.8e-15, 3.6e-15,
  7.4e-13, slope ratios); enumerations the argument does not use item by item (floor lists, the V's
  list, peak lists); and notes about how a count was computed.
- **Moves out to `revisions.md`:** provenance and history (raise chains, supersession notes, closed
  open items, ticked checklists).

Every finding in §§3–4 below is classed on this line. If the user draws it elsewhere, §4's list
shrinks or grows but its entries stay valid.

#### 3. Findings: organization (question 1)

- **OR1. The header is stale.** `sections_3-6.md` line 4 says "approximately **5,600 words**"
  (the table sums to 6,310) and lists Appendices A–D, omitting F, which §5.2 is written against.
- **OR2. Bookkeeping sits inside both outlines.** In `sections_3-6.md`: the word-allocation raise
  chain and its "does not reconcile" note (lines ~139–157), "What this table does not do" (~186),
  "Open items" (all four closed, ~1538), and "Sources for §5.2" (a note on where §5.1's citations
  went, misnamed). In `background_sections.md`: the header's revision history, the raise history
  in "Target length", the thirteen-item drafting checklist (all ticked, with audit evidence), and
  the reference list's verification log. **Proposal:** move all of it to `revisions.md`; keep the
  table, the targets and the reference entries.
- **OR3. Provenance runs through the prose instructions.** Tags like "(R2)", "(PP10)", "since
  2026-09-23", "supersedes the 2026-09-23 ruling", "the agent's addition to R19" appear mid-bullet
  throughout. **Proposal:** keep a decision ID only where a writer must honour a ruling; move
  histories to `revisions.md`; set writer's notes in one consistent form (*(Writer's note: …)*),
  which the file already half-uses.
- **OR4. §5.1 contradicts its own ordering instruction.** Its frame says **the complexity saving
  leads** and the conjecture is second, but the body puts the P-8 floors bullet, the five-move
  conjecture and its four-move weighting **before** "The design: resolution as a negative search".
  **Proposal:** frame → the design and its savings (the specification, first motivation) → what the
  criteria add (floors, conjecture, its weight) → what is not derived → the gain and the standing
  qualification. Optionally split the criteria reading into its own subsection. Word count
  unchanged.
- **OR5. §5.5 is overloaded and unsorted** (745 words, thirteen bullets mixing four kinds of
  limit). **Proposal:** group it under four run-in heads — *the numerical substrate* (Z, K, the
  (K, Z)(n) proposal); *the architecture* (linear-Gaussian, the relay, m = 2, not learned);
  *stipulations* (uniform exposure, the inventory, Tier B); *open* (the read-out's locality). Two
  bullets duplicate other sections and shrink to a line each (OR7).
- **OR6. The scope decision's Tier C no longer describes the outline.** Tier C says grid refinement
  and the μ_u/ℓ₀ common-mode invariance are "left in the notebook and cited", but §4.2 quotes the
  invariance's measured instance and §§4.3, 5.5 carry grid refinement at length. Resolved either by
  the pointers of OR-P7, OR-P9 and OR-P15, or by moving those items to Tier A. The agent recommends
  the pointers.
- **OR7. The same content is stated in several sections of the outline.**
  1. The constructive claim's numbers appear three times (Central claim, §§4.4–4.5, §6 item 3), and
     the Central claim also carries the Z-ladder figures (32, 15, 0, 0, 0 / 22, 9, 0, 0, 0). Keep
     the numbers in §4.5 and the claim in words, with "(§4.5)", in the other two.
  2. How Z reaches the verdict (B orthonormalized under the grid's measure; the peak moves; the
     mode position criterion moves by definition) is explained in both §4.2 and §5.5. Keep the
     guard in §4.2 and the mechanism in §5.5.
  3. Halting by tolerance is argued in §5.3 and again in a §5.5 bullet. §5.5 keeps one line and a
     pointer.
  4. §4.6's numbers (2.126, 26, 4,823, 7.9e6) reappear in §5.3. §5.3 cites §4.6.
  5. Commitment 7 and the relay's ordering τ_r ≤ τ_ε (F26) are stated in §3.4, §5.5, and
     background §§2.1, 2.4, 2.6 and 2.7. State the ordering once in background §2.6 and once in
     §3.4; the rest point.
  6. The override law appears in background §1.3, §4.5 and §5.6, and the Cremers parallel's counts
     in background §1.3 and §4.4 (see OR8).
- **OR8. The background quotes measured counts, against its own rule.** Background §1.3 Beat 3
  gives the anti-exhaustive direction's counts ("under all four priors that have a row at the
  weaker lexical strength, and under two of five at the stronger …"), while §2.2 closes on
  "nothing measured enters the background (BG7)". **Proposal:** the forward pointer names the
  parallel and sends the counts to §4.4.

- **OR9. The Xiang comparison is evaluation, not discussion (the user, 2026-09-24).**
  > I think the evaluation against Xiang data are essentially evaluations rather than discussions
  > […] The content that are already in section 4 is evaluation on scalar implicature
  > specifically. So any existing 4.* should be 4.1.* instead; then any evaluation against Xiang
  > should be 4.2.*

  **The new §4**, with a two-line opening naming the two evaluations and their different
  configurations:
  - **4.1 Scalar implicature** — the present §§4.1–4.6 become §§4.1.1–4.1.6, content unchanged by
    this task (4.1.1 What is compared; 4.1.2 The criterion; 4.1.3 The specification holds; 4.1.4
    The five priors; 4.1.5 The plane; 4.1.6 What the verdict needs, against what θ\* costs).
  - **4.2 Scale classes against Xiang et al. (2022)** — §5.2's measurements move here:
    4.2.1 *What is tested, and at what configuration* (n = 4, a fitted Λ, H1 and H2 stated as what
    is tested, the open-scale half untested, the ensemble is the inventory's); 4.2.2 *Where the
    model matches* (the fits, the half-width control, the utility level's gain, the image-type
    sign); 4.2.3 *Where it does not* (the residuals); 4.2.4 *How far the utility level reaches*
    (Eq. F3's sign result and the Eq. 24 limit as measured facts; the parity loadings as a pointer
    to Appendix F).
  - **§5.2 stays numbered §5.2** and keeps the discussion: why no position is taken on H1, the one
    causal statement, what the comparison is worth against Xiang et al.'s conclusion, the
    calibration, and the θ_A instinct. About 500 of its 860 words move to §4.2; the total stays.
  - **Consequences the move exposes.** (i) §4.1.1's "all internal to the model; no quantitative
    comparison offered" is scoped to §4.1 by the numbering, and §4.2.1 states its own comparison;
    Xiang et al.'s own models' R² stay cited as *their reported fits*, not as a comparison this
    dissertation runs. (ii) §4.2.1 says §4.1.2's criterion does not apply there. (iii) Pointers to
    §5.2 for the comparison are re-aimed: Central claim, the scope table's Tier A row, §5.6's
    fourth prediction, §6 item 4, background §1.7.
  - **Cross-references.** "§4.x" → "§4.1.x" in the live files: `sections_3-6.md` (94),
    `background_sections.md` (13), `agent/decisions.md` (26), and one comment in Code Cell A
    ("Sec. 4.5"; a comment, so no re-execution). `revisions.md` (100) and `agent/history.md` are
    logs: a mapping note at the head of `revisions.md` §16, and the binding lists of §§14–15
    updated, rather than rewriting history.

#### 4. Findings: content (questions 2 and 3)

Checked against the notebooks' markdown on 2026-09-24. "In the notebook" means the passage or its
numbers are already stated there. "Not in the notebook" means the technical content lives only in
the outline.

##### Technical content not yet in a notebook (question 2)

- **OR-N1. §5.1's cascade derivation.** Substituting χ_D for **1** in Eq. (C1), so that a
  complementary pair within a domain costs no dimension at any cascade depth, is a derivation,
  and no notebook carries it (no "χ_D" or "cascade" in any markdown cell). **Proposal:** a short
  section of Appendix C states and proves it; §5.1 keeps the claim ("a binary cascade needs m = 1
  at every level, so it is local without the relay") and points there.
- **OR-N2. §5.5's claim that the Z dependence sits below the criterion.** "A projection taken in
  L²([−Z, Z]) … only a projection under a fixed reference measure would [remove it], and that
  breaks the BᵀWB = I that Eq. (B2) assumes" is a technical claim that no notebook states
  (Text cell 3 §1 has the L² fact, not the consequence). **Proposal:** a sentence in Appendix A's
  half-width paragraph or in Text cell 3 §1; §5.5 keeps "reformulating the criterion cannot remove
  it" and points.
- Nothing else found. The rest of §5.1's design argument (log-odds absorbing the normalization,
  the anchoring proviso) is rationale, and its technical conditions already point to Text cell 3
  §8.6.

##### Content already in a notebook, to become a pointer (question 3)

| ID | Outline site | Already in | Keep in the outline |
|---|---|---|---|
| OR-P1 | §3.2, the grid's two parameters | Text cell 3 §1 | one sentence: K discretizes, Z bounds |
| OR-P2 | §3.2, R18 reason 2's formula (σ_L − σ_S)ℓ₀/S; Eq. D7's 2BᵀWℓ₀ | Appendix D §5 | the three reasons in words |
| OR-P3 | §3.3, the projection warning's exact form (BᵀW**1** = 0; Eq. 15 carries the constant) | Appendix D §5 | the parallel and the warning in words |
| OR-P4 | §3.4, the four convergence results; the stiffness ratio 404.8 and the 810.69 writer's note | Text cell 3 §8.2; Text cell 4, *Integration cost and conditioning* | "four results kept apart"; "conditioning decides what is reachable" |
| OR-P5 | §3.4, the relay's mechanics (Eqs. E1, E4, E4a, E6; F26; O6) | `appendix_E.ipynb` E.1 | the sum relocated, not removed; the cost is an ordering |
| OR-P6 | §3.5, the parity derivation's steps | Appendix C §5 | the rationale for m = 2 and the scoped necessity |
| OR-P7 | §4.2, the invariance instance (3.6e-15 over sixty settings; a fifth of Δ) | Text cell 5 | the guard in words |
| OR-P8 | §4.2, the Z ladder's peak list and the two cautions (brackets; decayed sign flips) | Appendix A (half-width paragraphs) | the guard and one figure |
| OR-P9 | §4.3, the check-by-check figures | Code Cell 2's check table | "reported as a table"; the K/Z pair; the K warning |
| OR-P10 | §4.4, the diffuse priors' peak lists; the 8-rows/5-priors note; "exact to 1.8e-15" | Text cells 4 and 4b | the table, the conjunction counts, the delta-like row |
| OR-P11 | §4.5, the floor enumerations, the V's list, the override slopes and ratios, the spread D, the least-θ_u ranges | Text cell 6 | the floors' directions and crossing, the band, 33 / 13 / 15 / 9, the Z caveat |
| OR-P12 | §4.6, the integration numbers | Text cells 4 and 4b | the three facts §5.3 uses, once (OR7.4) |
| OR-P13 | §5.1, θ_u\* by inventory (−11.28, −44.18, −65.70, −28.44) | Appendix B | "depends substantially on the inventory" |
| OR-P14 | §5.2, the Eq. (F3) derivation and both "(Note for the notebook …)" asides (medians; the midpoint node's 0.0194) | Appendix F | the sign result in words; **delete the two notes**, since the notebook already has them |
| OR-P15 | §5.5, the K bullet's finer- and coarse-end numbers | Appendix A, *A third axis* | the suspected bound, what the evidence allows, the directions, the (K, Z)(n) proposal |
| OR-P16 | §5.5, the read-out bullet's "Sourced (C6)" counts | Appendix A, *Finding the peak* | the nuances and the candidate stipulation |
| OR-P17 | §5.6, θ_u\* set by 3𝔼_{p(y)}[c_y] | Appendix B | the prediction |

The background (`background_sections.md`) has no technical overlap beyond OR7.5 and OR8. Its
content is rationale and literature, as the rule wants.

#### 5. Proposed tasks (not started; wait for the user)

- [x] **OR0.** Checkpoint: clean at `574aa23`.
- [x] **OR-D1.** Confirmed by the user 2026-09-24 ("Your decisions are confirmed"), with the proposals of §§3–4.
- [x] **OR-A. Housekeeping** (`5fb809a`; OR3's history notes in `f08ad77`) (OR1, OR2, OR3): header, bookkeeping moved to `revisions.md`, one
  form for writer's notes. No content change.
- [x] **OR-S. The new §4** (`83aa693`) (OR9), before any pointer pass, so that pointers are written against
  the new layout: renumber, move §5.2's measurements to §4.2, add §4's opening, re-aim references,
  re-sum the word table.
- [x] **OR-B. Notebook first** (`b777247`) (OR-N1, OR-N2): Appendix C and Appendix A (or Text cell 3 §1) gain
  the two technical passages; no code changes, so no re-execution is needed. Code before prose does
  not bind here, since neither passage quotes a number, but each is checked against the equations it
  cites.
- [x] **OR-C. Pointers** (`f08ad77`) (OR-P1 to P17), section by section, keeping what the table's right column
  names.
- [x] **OR-D. Restructure** (`f08ad77`) (OR4 §5.1 order; OR5 §5.5 grouping; OR6 Tier C; OR7 de-duplication;
  OR8 background §1.3).
- [x] **OR-E. Word budget.** No budget line changed: the detail moved out was the outline's, not the dissertation's; the table was rebuilt at OR-S (Total 6,350). Pointers shorten the outline, not the dissertation's budget, unless a
  budget line was paying for the moved detail; re-sum where it was.
- [ ] **OR-F. Close**: dangling references, C6 sweep, `revisions.md` §16, fold.

#### 6. Findings log

- **OR-F1 (OR-A): §5.1 never carried the citations "Sources for §5.2" said had been redeployed
  into it.** No Rooth, Kratzer & Shimoyama, Katzir or Fox & Spector appeared in §5.1. They are now
  placed in the design's "inventory at any one level is binary" bullet (background §1.6 introduces
  all four).
- **OR-F2 (OR-S): the §4.1 heading was first written as 1,430 words**; its subsections sum to 1,930.
  Corrected before commit.
- **OR-F3 (OR-C): two pointers first named the wrong home.** The utterance-contrast spreads across
  priors (0.0575, 0.0001) and the Z ladder's peak list (0.8516 …) are printed by code cells, not
  stated in markdown; the pointers now name Code Cells 2 and 2b, and Code Cell A.
- **OR-F4 (OR3): decision IDs were kept, revision-plan IDs mostly kept.** Only dated history
  ("since 2026-09-23", "supersedes the ruling", "settled on …", "New.", raise notes) was removed.
  A bare ID like (R14) or (R16) often names a ruling the writer must honour, so a blanket strip
  would have lost rulings. The background's "the previous draft …" instructions were kept: they
  direct a revision of existing prose.
- **OR-F5 (OR7.1): the conclusion's item 3 now states the result in words with pointers**, as the
  confirmed proposal said, so the four headline counts appear in §§4.1.4–4.1.5 only.
- **OR-F6 (OR-B): the orthonormality claim was checked before it entered Appendix A.** Eliminating
  x gives Eq. (B1)'s scalar ratio only when BᵀWB = I; otherwise the denominator is a matrix.

---

*Full original:* `git show 0f3bb42:agent/review_2026-09-24_outline_organization.md`

---
