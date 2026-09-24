# Proof scope and read-out review (opened 2026-09-23)

Working record under `agent/agent.md` §5.3. Fold into `agent/history.md` when it closes.

## 1. The user's instruction

> Here is another agent's feedback that we should address:

The feedback, as a list of its points (the full text is in the session of 2026-09-23). It treats
the Z-dependence and the exposure ensemble as closed and changes no file.

- **P1.** Background §§2.2-2.3 and outline §3.6 conflate three objects: the conditional posterior
  over field configurations x at fixed θ_u, Bogacz's point approximation δ(x − x\*) over x, and the
  read-out q(ζ) ∝ e^{φ_S\*(ζ)} over the world coordinate. Gaussianity does not make the posterior a
  delta; the delta is a further commitment (Laplace keeps a mode and a covariance). The background's
  minimized free energy needs a bridge to the notebook's maximized F.
- **P2.** The "two numbers against a whole field" argument (background §2.2, outline §3.6 reason 3)
  does not apply: the inferred mean is the whole vector (φ_S\*, φ_u\*), 103 numbers at K = 101,
  m = 2, and the delta does not compress it.
- **P3.** Outline §3.5 says m = 2 is forced. One mixed-parity column separates all three entries;
  Appendix C uses "spanning" for two properties. Separate: separating the inventory; retaining every
  direction of its span; representing tilt and width as independent coordinates.
- **P4.** Text cell 3 §§8.1-8.4: the concavity proof is sound; Ḟ = ‖∇F‖²/τ_φ holds for
  instantaneous errors only; the metric convention (W) is implicit; monotonicity needs the silent
  error initialization. State four results separately.
- **P5.** Appendix E: "F does not see it" holds only at r = Bφ_u; Eq. (E5) freezes φ_S, so it is a
  subsystem; the Hessian proof does not cover an extra dynamical variable. Outline §5.1's affine
  alternatives level keeps the proof only if no new direction is left unanchored.
- **P6.** The mode criteria need a read-out beyond the delta (an argmax), whose locality does not
  follow from the absence of a normalizer; the shared mode of §3.6 is coordinate-dependent.
- **P7.** Appendix B: μ_u = 0 does leave a stationary point (θ_u = 0); the orthogonal case needs a
  case split; "no learning rate" overstates, the step factor being τ_φ/τ_θ.
- **P8.** Background §2.6: joint settlement does not prove the absence of a semantic stage, since
  φ_L = Λχ_y is clamped before recurrence.

## 2. Verification (agent, 2026-09-23; checkpoint 955aaf3, clean tree)

Every point was checked against the files and, where numerical, recomputed with `code cell 1`
(scripts in the session scratchpad, not in the repository; no number below is quoted in prose).

- **F1 (P1).** Confirmed. `agent/Bogacz_2017_Free_Energy_Tutorial.md` line 297 adopts the delta
  "for simplicity" as a shape simpler than the Gaussian, not as a consequence of it; line 331 calls F
  the *negative* free energy. Background §2.2's table row ("what makes the delta … a posterior")
  and §2.3's "the approximating belief is over ζ" are the two sites.
- **F2 (P2).** Confirmed: x has K + m = 103 components. **This contradicts the third reason of A16's
  2026-09-23 finding, which is the user's ruling.** Not edited. Bogacz line 103 supplies a
  different motivation for a point estimate ("the brain represents at a given moment of time only
  most likely values of features"), which would carry the preference without the cost comparison.
- **F3 (P3).** Confirmed. With b = (b₁ + b₂)/√2 the projections of φ_L at Λ = 8 are +2.3697,
  −2.3697, −10.5266 for *no*, *some*, *all*. Least-squares reconstruction of each χ_y (mod 1) from
  span B leaves a relative residual of 0.449. Text cell 5 already says a mixed-parity profile
  separates and that m = 2 is chosen for tilt/width; outline §3.5 ("Neither of the following is
  chosen") and A7 overstate it.
- **F4 (P4).** Confirmed. The metric half is already on record as register entries E1 and E2 (open
  since 2026-09-13). `infer` starts every error unit at zero, which is the initialization the
  monotonicity claim silently uses.
- **F5 (P5).** Confirmed. `relay_loop_abscissa` builds the 4×4 matrix of Eq. (E5) with φ_S held.
  The full linear network (φ_S, φ_u, ε_L, ε_S, ε_u, r; 410 variables) at θ_u = −20, θ\*, −40, −80
  and τ_r/τ_ε ∈ {1, 2, 10} is stable, largest real part ≈ −1.000 (the τ_φ mode E5 lacks). No cell
  prints this.
- **F6 (P6).** Confirmed. Delta-like row (Beta(64,1), Λ = 512, θ\* = 1407.77), under *some*: the
  peak of φ_S\* on the ζ grid maps to s = 0.94685, outside the cell of *all* (s ≥ 0.95); the peak
  of the same distribution as a density over s, φ_S\* − log s(1−s), is at s = 0.95257, inside it.
  **The mode position criterion on that row therefore depends on the coordinate** — a stop-and-ask
  under agent.md §5.4. No cell prints the second number.
- **F7 (P7).** Confirmed. From Eq. (B1) summed over utterances, stationarity is
  p σ_u θ² + (3S‖μ_u‖² − σ_u Σ‖c_y‖²) θ − pS = 0 with p = ⟨μ_u, Σc_y⟩. At p = 0 the one finite root
  is θ = 0, a maximum if 3S‖μ_u‖² > σ_u Σ‖c_y‖², a minimum if reversed, F̃ constant at equality; the
  other root diverges (the ray). At μ_u = 0, θ = 0 is a minimum and the flow from θ(0) = 0 stays.
- **F8 (P8).** Confirmed: background §2.6, "The consequence for staging".

## 3. Tasks

- [x] **R1** (2026-09-23): Appendix B, μ_u = 0 paragraph (no maximizer; θ = 0 a minimum; the flow
  from zero stays) and the orthogonal case (three-way split; one root to 0, one to the ray);
  "no interior maximizer" on the ray → "no maximizer away from θ_u = 0".
- [x] **R2** (2026-09-23): "no learning rate" → the learning rate is τ_φ/τ_θ, in Text cell 3 §7,
  background §2.6 and outline §3.4.
- [x] **R3** (2026-09-23): Appendix C §1 defines "spanning" as injectivity of B^T W on
  span{χ_y}/⟨1⟩, and says B's columns do not span the χ_y. The word is kept (P3 asks to separate
  the senses, not to rename; renaming is open to the user).
- [x] **R4** (2026-09-23): Appendix E. E.1 states Eq. (E5) is a subsystem and what it omits; the
  "What is unchanged" rows for Eq. (13) and Eqs. (21)-(22) say "at r = Bφ_u"; E.2's "F does not see
  it" restricted to the equilibrated relay; E.3's §8.4 row says the extra variable is not covered.
- [ ] **R5**, waits on the user (Q1-Q2): background §§2.2-2.3 and outline §3.6 carry the three
  objects, the sign bridge, and whatever replaces or restricts A16's third reason.
- [ ] **R6**, waits on the user (Q3): outline §3.5, §5.1 and A7 recast m = 2 as a design rationale
  (tilt and width as independent coordinates), with necessity only within a definite-parity basis;
  §5.1's affine-level convergence made conditional on every new direction being anchored.
- [ ] **R7**, waits on the user (Q4): Text cell 3 §§8.2-8.3 split into four results (unique optimum;
  ascent with instantaneous errors, in the W metric; coupled stability from the characteristic
  equation; monotonicity from the silent start), which also closes E1/E2; outline §3.4 follows.
- [ ] **R8**, waits on the user (Q5): the mode criteria named as statistics of φ_S\* in ζ, the
  argmax named as a further operation, §3.6's "the mode is shared" given its coordinate; whether a
  cell prints the s-density mode.
- [ ] **R9**, waits on the user (Q6): background §2.6's staging claim restated as joint inference of
  the downstream fields given the clamped lexical input.
- [ ] **R10**, optional, waits on the user: a full-network spectrum with the relay in Code Cell E4
  (code change; re-execution of appendix_E), so E.1 can quote F5.

## 4. Questions for the user

- **Q1** (A16, user-ruled): the two-number reason is not true of this implementation. Replace it
  with Bogacz's own motivation (line 103) plus the extra operations q needs, restrict it, or drop it?
- **Q2**: confirm that the delta is stated as Bogacz's further simplification over x, not a
  consequence of Gaussianity, at background §2.2 and outline §3.6.
- **Q3** (A7): may §3.5 stop saying m = 2 is forced?
- **Q4** (E1/E2, open since 2026-09-13): may Text cell 3 §8 be restructured and D6's metric stated?
- **Q5** (B7/B8): how to treat the coordinate dependence of the delta-like row's mode position.
- **Q6**: may background §2.6's no-semantic-stage claim be narrowed?
