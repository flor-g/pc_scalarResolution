# Cost, attribution and scope review (opened 2026-09-24)

Working record under `agent/agent.md` §5.3. Fold into `agent/history.md` when it closes.

**IDs.** Tasks are RV0–RV8, the review's points RP1–RP6, questions to the user RVQ1–RVQ4, findings
RVF1–RVF12. The prefix keeps them apart from `thesis_outline/revisions.md`'s rulings R1–R28 and from
the 2026-09-23 record's PS/PSF/PSQ.

## 1. The user's instruction

> Here are another agent's review. Let's address them:

The review, as a list of its points (the full text is in the session of 2026-09-24). It changes no
file and reports eight reproduced cells matching their saved output.

- **RP1.** §5.4 step 1: a trajectory functional of a deterministic system is fixed before
  execution, so "no state before the halt fixes" the cost is false; what holds is that this network
  has no mechanism supplying the cost during the inference. Step 2's anticipated/actual distinction
  does not show an anticipation cannot be exact. "Converges if the map is a contraction, and
  oscillates or diverges otherwise" is false: contraction is sufficient, not necessary.
- **RP2.** §4.2.2 and Appendix F call the gain over q_lit a "utility gain", but the comparison
  changes tempering and utility together. Minimum class at Λ = 48: q_lit 0.1034, tempered control
  0.2265, model 0.4339. Include the control; narrow the attribution in §§4.2–5.2 and the
  displacement §5.2's hedged causal statement rests on.
- **RP3.** §5.1: one midpoint cut is not a recursively balanced partition; O(log n) needs a search
  task, balanced cuts at every depth and a bound per level, and an O(n) baseline Appendix G does not
  set. The alternatives state is called both one real-valued log-odds unit and the indicator χ_D.
- **RP4.** §5.1 move 3 ("a mode is what commitment 3 says the system carries") and §5.5 ("one
  posterior", "the ½ tempering has no counterpart") predate the posterior/read-out repair.
  Distinguish questions the computational level leaves unspecified from ones it cannot pose.
- **RP5.** main.ipynb: Eqs. (21)–(22) pair an ordinary vᵀ∇²F v with a metric Hessian (the ordinary
  symmetric part of H has eigenvalue ≈ −0.711 at the defaults); Appendix G's step analysis should use
  `infer`'s update order (errors first); "n enters cost only through θ_u\*" is too strong (5,296,
  5,314, 5,103 steps at n = 2, 10, 100 with θ_u = 5, K = 101, κ = 27).
- **RP6.** Background §§2.2, 2.4 say Rao and Ballard (1999) did not impose locality; Bogacz (tutorial
  line 37) says their model fully satisfied it. "A non-Gaussian model would not yield subtractive
  errors" is too broad (Poisson log-link score y − e^η). CF2 and CF3 remain. The conclusion's
  "provably reaches it, with plasticity local at every m" needs a scope check.

## 2. Verification (agent, 2026-09-24; checkpoint e62349d, clean tree)

Scripts in the session scratchpad, run against `code cell 1` and Code Cell F's own helpers.

- **RVF1 (RP1).** Confirmed. The §5.4 footnote itself says the dynamics are predictable from
  outside to within constants (Eq. G2), which is the review's point. `C_{k+1} = C_k/(1+C_k)`
  converges to 0 from C₀ > 0 without being a strict contraction on [0, 1].
- **RVF2 (RP2).** Reproduced exactly: absolute_min 0.1034 / 0.2265 / 0.4339. **New:** absolute_max
  0.9922 / 0.9929 / 0.9928, and **pooled 0.7676 / 0.8297 / 0.8189 — the tempered control fits better
  than the model over both classes.** Displacement in mean scale position, measured from the
  tempered control: model +0.92 (shapes) and +1.17 (artifacts), data −0.04 and +0.84; the tempered
  control itself sits +0.20 and +0.22 above q_lit.
- **RVF3 (RP3).** Confirmed at `sections_3-6.md` §5.1 (lines 909–936, "the comparison it invites is
  O(n) against O(log n)") and the central claim ("derived from the construction"); φ_a is "one
  log-odds unit" at the R4 bullet and "φ_a = χ_D, an indicator" in *What this dissertation does not
  derive*.
- **RVF4 (RP4).** Confirmed at §5.1 move 3 and §5.5's four instances.
- **RVF5 (RP5, metric).** Confirmed: at θ_u\* = −28.4375 the ordinary symmetric part of H has least
  eigenvalue −0.7109, while H's own least eigenvalue is 1.0000 and the coordinate Hessian
  −∂²F/∂x² = GH is symmetric (asymmetry 1.8e-14) and positive definite. Eqs. (21)–(22) are the
  coordinate Hessian's quadratic form with W-norms, equal to the G-pairing ⟨v, ∇²F v⟩_G; the text
  writes neither.
- **RVF6 (RP5, recurrence).** Confirmed: `infer` updates the error units first and the states from
  the updated errors. Per mode of H with eigenvalue λ, with dt = τ_ε/2 and τ_ε = τ_φ/(4λ_max), the
  implemented step is the 2 × 2 map u' = u/2 + λy/2, y' = y − u'/(8λ_max), of **determinant ½ and
  trace 3/2 − λ/(16λ_max)**: both roots real and in (0, 1) for every 0 < λ ≤ λ_max, the slow one
  μ = 1 − λ/(8λ_max) − (λ/(8λ_max))² + O((λ/λ_max)³); for λ = 1, 8κ(−log μ) = 1 + 3/(16κ) + O(κ⁻²). That gives
  **1.0333 at κ = 6** against Code Cell G's measured **1.0334**, and 1.0005 at κ = 402: the exact
  recurrence explains the printed decay, which the leading-order argument (→ 1) did not. The
  code comment in `infer` ("explicit Euler is stable … dt|s| ≤ 1") argues from forward Euler too.
- **RVF7 (RP5, n).** Reproduced exactly: 5,296 / 5,314 / 5,103 steps, λ_max = 27 at all three. n
  moves φ_L and so the start's derivative a in Eq. (G2)'s log factor. (Corrected by RVF11: a does
  not move; a₁ does.)
- **RVF8 (RP6).** Confirmed at background lines 450–456 and 530–532, and a third site the review
  did not name: `appendix_E.ipynb` cell 7 ("Rao and Ballard (1999) … does not impose it"). The same
  tutorial line says Friston (2005) did **not** fully satisfy the constraints. CF2 (Text cell 3
  §8.3) and CF3 (Appendix B) are still in main. Appendix E's relay convergence is a subsystem
  spectrum (Eq. E5) plus measurement, so "provably reaches it" and "local at every m" hold of two
  different networks.

## 3. The user's rulings (2026-09-24, in chat)

- **RVQ1 (RP1): architectural claim.** Step 1: the cost is fixed in advance, but only from
  outside; nothing in this network computes or reads it during the inference. Step 2 keeps the
  anticipated/actual distinction and says whether an anticipation could be exact is not argued.
- **RVQ2 (RP2): three-way split.** Code Cell F prints the tempered control beside q_lit and the
  model; the prose attributes tempering and utility separately, reports the pooled reversal, and
  measures §5.2's displacement from the tempered control.
- **RVQ3 (RP3): conditional, order kept.** The saving is a conditional design argument (logarithmic
  if cuts stay balanced at every depth, for a stated search task); it still leads because it needs
  no datum, and is no longer called derived. φ_a is one log-odds unit; χ_D is the domain its sign
  selects.
- **RVQ4 (RP4): "leaves unspecified".** §5.5 claims only questions the computational level leaves
  unspecified; the tempering instance goes, the delta instance is restated over the right
  variables; §5.1 move 3 says the construction infers a field configuration and locating its peak
  is a further operation.

The agent's own calls, pending user confirmation, are marked (agent) where they are made below.

## 4. Tasks

- [x] RV0 (2026-09-24): checkpoint — clean tree at e62349d.
- [x] RV1 (2026-09-24): Code Cell F — tempered control in F.2, F.3 (tempering and utility columns
      replace "utility gain") and F.9(d) (displacement from the tempered control). Scratch run
      reproduces RVF2 exactly.
- [x] RV2 (2026-09-24): Code Cell G — 'recurrence' column beside the measured decay (agree to
      ≤ 0.0002 in every row), every mode's factors checked real, block 2b the n ladder with a₁.
      `infer`'s stability comment rewritten from the recurrence in `code cell 1`; E1's own shorter
      comment edited in place (it is one of coupling 9's six relay-carrying defs).
- [x] RV3 (2026-09-24): main re-executed — RUNNER OK, 0 errors, 8 figures, 897 s. Every code
      cell's stream output identical to the pre-run copy except Code Cells F and G (the new
      columns and block 2b) and Code Cell 2b's `cost:` lines (wall clock, which E3 drops).
      appendix_E not re-executed: its changes are one code comment and one prose sentence.
- [x] RV4 (2026-09-24): main prose, 14 edits validated on a scratch copy first, then applied to
      the executed notebook and read back — Text cell 3 §8 (metric pairing, Eqs. 21–22, CF2),
      Appendix B (CF3), Appendix F §§3, 4, 5, 6, Appendix G (opening; §3's recurrence and n ladder).
      C6 sweep clean on both notebooks; no dangling equation reference.
- [x] RV5 (2026-09-24): `sections_3-6.md` — 25 edits, validated before writing and read back:
      central claim (three), word table (three rows), §§4.2.2, 4.2.3, 4.2.4, 5.1 (frame, search
      bullet, *most* bullet, φ_a/χ_D, underived item 1, move 3 twice), 5.2, 5.4 (steps 1–2, proxy),
      5.5 (heading, claim, counterargument, guard), 5.6, 5.7, §6 item 1.
- [x] RV6 (2026-09-24): `background_sections.md` — Rao and Ballard at §§2.2 and 2.4 (Friston 2005
      as the model that does not fully satisfy locality, already in the reference list), the
      subtractive-error sentence narrowed, the opening's "posable" clause (RVQ4).
      `appendix_E.ipynb` E.2's Rao sentence (no new citation: "by Bogacz's account").
- [x] RV7 (2026-09-24): `agent/decisions.md` — findings under A22, I14, A17, B11, E1; CF2/CF3
      resolved; E21. `thesis_outline/revisions.md` §19.
- [ ] RV8: commit.

## 5. Findings log

(RVF1–RVF8 above.)

- **RVF9 (RV1).** Pooled over both classes the tempered control beats the model, 0.830 against
  0.819; on the maximum class the utility step is −0.000 (0.9928 against 0.9929). Raised with the
  user before any edit (RVQ2) and reported in §4.2.3 and Appendix F §5 without explanation.
- **RVF10 (RV1).** Eq. (24)'s limit ½(I + BBᵀW)(ℓ₀ − φ_L) doubles the span-B component of the
  tempered control, not of q_lit's field: the tempered control is the base the "doubling" was
  always relative to, which is why RVQ2 measures the displacement from it.
- **RVF11 (RV2).** The start's largest derivative a is the same at n = 2, 10, 100 (2661.58): n moves
  N through a₁ alone. The review's "forcing and modal amplitudes" is right about the second.
- **RVF12 (RV4).** The prose script's Appendix G pattern failed its pre-write validation on a line
  wrapped at "appears / in no count"; nothing was written, the pattern was fixed and the script
  re-validated on a scratch copy before it touched main.
