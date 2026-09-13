# E4 and E7: the default base prior, and every quoted number printed

Working record for two findings of `decisions.md` register E, on the pattern of
`theta_u_learned_reach.md`.

## 0. Instructions (the user's, verbatim, 2026-09-13)

> E4: the Gaussian base-world-prior is one of the several base-world-priors we tested our model on.
> It is indeed not elicited from any experiments. ell_0 can be supplied by an elicited distribution
> but it doesn't have to be. When an elicited distribution is not supplied, the default is N(0,1).
> It may be helpful to clarify the the reason that we chose N(0,1) as default : the pc framework as
> in Bogacz operates on the fundamental assumption that a system represents states with gaussian;
> now although ell_0 is not a state unit and does not have to be gaussian by construction, it makes
> more sense that it is defaulted to gaussian given the framework's assumption.
>
> E7: all unsourced numbers must be computed by an explicit script and printed in some code cell.

## 1. Decisions

- **DEC1 (user).** The Gaussian N(0,1) in ζ is the *default* base world prior, one of several the
  model is tested on, and not elicited. ℓ₀ may be supplied by an elicited distribution. Reason for a
  Gaussian default: the framework (Bogacz) represents states with Gaussians; ℓ₀ is not a state unit
  and need not be Gaussian, but a Gaussian default is the choice consistent with that assumption.
  The reason for the parameter values (mean 0, precision 1) is not recorded.
- **DEC2 (user).** Every number the prose quotes is computed by an explicit script and printed in a
  code cell. This replaces the earlier allowance for a script recorded only in a change record
  (I8).
- **DEC3 (agent, pending user confirmation).** Placement: numbers quoted in Text cells 4 and 5 are
  printed by Code Cells 2 and 3; each of Appendices A–D gets its own code cell directly after it
  (Code Cells A–D); numbers quoted in Appendix E.1 are printed by a new Code Cell E4.

## 2. Tasks

Record format: `[x] Tn (date): what changed; acceptance result; commit`.

- [x] T0 (2026-09-13): checkpoint. Tree clean at e02e95d (local, one commit ahead of origin).
- [x] T1 (2026-09-13): every E7 number recomputed in scratch from code cell 1 (and Code Cell E1
  for the relay). Most reproduce exactly; departures logged as F1–F9 below.
- [x] T2 (2026-09-13): code, applied by a script that required every edit to land exactly once.
  Code cell 1 and E1: `gaussian_world_prior` docstring (E4). Code Cell 2 and E2, identical edits: the
  "elicited" print line; a mechanism block in the delta-like row (c_y, Eq. 23 gap, Eq. 24 limit, the
  shift across θ_u); an integration-cost table before the realizability table; a roundoff-floor
  measurement after the integrated run, at the closed-form arrival θ_u so that E2 prints the same
  line. Code Cell 3: B^TWℓ₀, the control shifts and tilt per unit, the μ_u ray. New Code Cells A–D
  after Appendices A–D, with anchors `codea`–`coded` and table-of-contents rows (cells renumbered
  12–20). New Code Cell E4 after E3. Smoke test: every code cell compiles; Code Cells A–D and E4's
  fast part run standalone and print the T1 values; E4's loop matches `infer` (1003 steps each, F
  trace identical).
- [x] T3 (2026-09-13): executed with nbclient, `main.ipynb` first. main: RUNNER OK, 0 errors,
  6 figures, 237 s, 14/14. appendix_E: RUNNER OK, 0 errors, 3 figures, 680 s, E2 18/18, E3 PASS
  (221 lines identical, 0 deleted). Re-executed after F10's fix: main 0 errors, 6 figures, 242 s,
  14/14; appendix_E 0 errors, 3 figures, 652 s, E2 18/18, E3 PASS (221 identical); both print the
  floor as 8.2e-11 to 2.4e-10.
- [x] T4 (2026-09-13): prose, applied by a script that first required every value it quotes to
  appear in the stored outputs (it refused once, which exposed F10) and every anchor to land once.
  All §4 sites changed. E4: the inventory row, Text cell 3 §3.4 with DEC1's reason, Part A, Part C
  twice, Appendix B. Pointers to the printing cell were added only where that cell is not directly
  below (Text cell 3 to Code Cells A and 2; E.1 to E4). Left as written, pending the user: the
  +22.578 sentence (F2), and what F8 implies for Eq. (E6). Checks: 70 ToC links resolve, no duplicate
  anchors, "elicited" no longer describes the Gaussian.
- [x] T5 (2026-09-13): `audit_numbers.py` re-run on the edited notebooks, after changing it to skip
  the table of contents and reference lists by content rather than by cell index (the renumbering
  had made it skip Appendix C and read the References). 365 quoted numbers: 356 match a stored
  output, 9 do not, and all 9 are section numbers or coordinate pairs. Output in
  `audits/2026-09-13/after_e7/`. `decisions.md`: A15, C6, I10 added, I8 superseded, E4 and E7
  resolved, O5 (F2) and O6 (F8) opened. `agent.md`: §3.3's rule, the cell map, the baseline.

## 3. Findings

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

## 4. Prose sites

Written against the executed outputs (T3). Every E7 site gains a pointer to the printing cell
unless that cell is the one directly below.

**E4.**
- Text cell 3, inventory row ℓ₀: "fixed (elicited)".
- Text cell 3 §3.4: say that ℓ₀ may be supplied by an elicited distribution; otherwise the default
  is N(0, 1) in ζ; give DEC1's reason; note that Part D tests five priors.
- Text cell 4 Part A: "under the elicited prior is −28.4375".
- Text cell 4 Part C, three sites: "the elicited prior".
- Appendix B: "which is the elicited configuration among many others".

**E7.**
- Text cell 3 §2: 2.4e-15 → 3.3e-15 (Code Cell A).
- Text cell 3 §8.3: 809.69 and 810.69 (Code Cell 2, integration cost).
- Text cell 4 Part C: c_some and c_all (Code Cell 2, delta-like row); "at most −0.0664 as θ_u → 0"
  and "saturating at the limit from both directions" per F1.
- Text cell 4 Part D: log α = 4.16 (Code Cell 2).
- Text cell 4, integration cost: the table (Code Cell 2); the floor, 8e-11 to 1.6e-10 → per F7.
- Text cell 5: Eq. (30)'s [0, −18.5996]; the μ_u ray; the control shifts; +0.0075 (Code Cell 3).
- Appendix A: every number (Code Cell A).
- Appendix B: 5.5e-16 → 3.3e-16; 2.2e-16 → exact at double precision; batching per F3; the rest as
  printed (Code Cell B). The +22.578 sentence is left as written (F2, the user's).
- Appendix C: §3 table and §7 per F4; §5 1.44190 → 1.44196 (Code Cell C).
- Appendix D: 5.3e-15 and 4.4e-16 → as printed (Code Cell D).
- Appendix E.1: 1.78e-14 → 1.90e-15 (E2, stale); the four bounds labelled by prior (F9); the
  slow-relay counts per utterance (F8, the sentence's bearing on Eq. E6 is the user's) (Code Cell E4).
