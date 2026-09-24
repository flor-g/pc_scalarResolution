# Proof scope and read-out review (opened 2026-09-23)

Working record under `agent/agent.md` §5.3. Fold into `agent/history.md` when it closes.

**IDs.** Tasks are PS1–PS11, questions to the user PSQ1–PSQ6, findings PSF1–PSF18, the review's
points P1–P8. The prefix keeps them apart from `thesis_outline/revisions.md`'s rulings R1–R21 and
questions Q1–Q8, and from `agent/history.md`'s findings. The outline-side view of these tasks is
`thesis_outline/revisions.md` §14.

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

- **PSF1 (P1).** Confirmed. `agent/Bogacz_2017_Free_Energy_Tutorial.md` line 297 adopts the delta
  "for simplicity" as a shape simpler than the Gaussian, not as a consequence of it; line 331 calls F
  the *negative* free energy. Background §2.2's table row ("what makes the delta … a posterior")
  and §2.3's "the approximating belief is over ζ" are the two sites.
- **PSF2 (P2).** Confirmed: x has K + m = 103 components. **This contradicts the third reason of A16's
  2026-09-23 finding, which is the user's ruling.** Not edited. Bogacz line 103 supplies a
  different motivation for a point estimate ("the brain represents at a given moment of time only
  most likely values of features"), which would carry the preference without the cost comparison.
- **PSF3 (P3).** Confirmed. With b = (b₁ + b₂)/√2 the projections of φ_L at Λ = 8 are +2.3697,
  −2.3697, −10.5266 for *no*, *some*, *all*. Least-squares reconstruction of each χ_y (mod 1) from
  span B leaves a relative residual of 0.449. Text cell 5 already says a mixed-parity profile
  separates and that m = 2 is chosen for tilt/width; outline §3.5 ("Neither of the following is
  chosen") and A7 overstate it.
- **PSF4 (P4).** Confirmed. The metric half is already on record as register entries E1 and E2 (open
  since 2026-09-13). `infer` starts every error unit at zero, which is the initialization the
  monotonicity claim silently uses.
- **PSF5 (P5).** Confirmed. `relay_loop_abscissa` builds the 4×4 matrix of Eq. (E5) with φ_S held.
  The full linear network (φ_S, φ_u, ε_L, ε_S, ε_u, r; 410 variables) at θ_u = −20, θ\*, −40, −80
  and τ_r/τ_ε ∈ {1, 2, 10} is stable, largest real part ≈ −1.000 (the τ_φ mode E5 lacks). No cell
  prints this.
- **PSF6 (P6).** Confirmed. Delta-like row (Beta(64,1), Λ = 512, θ\* = 1407.77), under *some*: the
  peak of φ_S\* on the ζ grid maps to s = 0.94685, outside the cell of *all* (s ≥ 0.95); the peak
  of the same distribution as a density over s, φ_S\* − log s(1−s), is at s = 0.95257, inside it.
  **The mode position criterion on that row therefore depends on the coordinate** — a stop-and-ask
  under agent.md §5.4. No cell prints the second number.
- **PSF7 (P7).** Confirmed. From Eq. (B1) summed over utterances, stationarity is
  p σ_u θ² + (3S‖μ_u‖² − σ_u Σ‖c_y‖²) θ − pS = 0 with p = ⟨μ_u, Σc_y⟩. At p = 0 the one finite root
  is θ = 0, a maximum if 3S‖μ_u‖² > σ_u Σ‖c_y‖², a minimum if reversed, F̃ constant at equality; the
  other root diverges (the ray). At μ_u = 0, θ = 0 is a minimum and the flow from θ(0) = 0 stays.
- **PSF8 (P8).** Confirmed: background §2.6, "The consequence for staging".

## 3. Tasks

- [x] **PS1** (2026-09-23): Appendix B, μ_u = 0 paragraph (no maximizer; θ = 0 a minimum; the flow
  from zero stays) and the orthogonal case (three-way split; one root to 0, one to the ray);
  "no interior maximizer" on the ray → "no maximizer away from θ_u = 0".
- [x] **PS2** (2026-09-23): "no learning rate" → the learning rate is τ_φ/τ_θ, in Text cell 3 §7,
  background §2.6 and outline §3.4.
- [x] **PS3** (2026-09-23): Appendix C §1 defines "spanning" as injectivity of B^T W on
  span{χ_y}/⟨1⟩, and says B's columns do not span the χ_y. The word is kept (P3 asks to separate
  the senses, not to rename; renaming is open to the user).
- [x] **PS4** (2026-09-23): Appendix E. E.1 states Eq. (E5) is a subsystem and what it omits; the
  "What is unchanged" rows for Eq. (13) and Eqs. (21)-(22) say "at r = Bφ_u"; E.2's "F does not see
  it" restricted to the equilibrated relay; E.3's §8.4 row says the extra variable is not covered.
- [x] **PS5** (2026-09-23, PSQ1-PSQ2 answered): background §2.2's table row and read-out bullet, §2.3's
  three objects, Bogacz's v in the decompositions and the sign bridge; outline §3.6's delta bullet
  and reason 3 now cite Bogacz §2.2's ground in place; A16 finding; revisions.md note.
- [x] **PS6** (2026-09-23, PSQ3 approved; §3.5 retitled "Two choices the scale motivates", 140 → 180
  words, §3 and Total re-summed; Appendix C opening and §5; Text cell 5; §5.5's limit line): outline §3.5, §5.1 and A7 recast m = 2 as a design rationale
  (tilt and width as independent coordinates), with necessity only within a definite-parity basis;
  §5.1's affine-level convergence made conditional on every new direction being anchored.
- [x] **PS7** (2026-09-23, PSQ4 approved; monotonicity kept in §8.2 as (iii) so Part A's printed
  label "Sec. 8.2 F non-decreasing" stays true and no code changes; outline §3.4 290 → 320 words;
  background §§2.1, 2.6 name the silent start; E1, E2 resolved; A11 finding): Text cell 3 §§8.2-8.3 split into four results (unique optimum;
  ascent with instantaneous errors, in the W metric; coupled stability from the characteristic
  equation; monotonicity from the silent start), which also closes E1/E2; outline §3.4 follows.
- [x] **PS8** (2026-09-23, PSQ5 answered across four exchanges): the mode is read over ζ and Text
  cell 4 says why (B13, MacKay 1998); §3.6's shared mode names its coordinate; background §2.4
  states Bogacz's lack of a read-out stage and the basal-ganglia note; §3.6's reason 3 rests on the
  normalization (A21); whether the read-out is bound by locality is posed as **open** in outline
  §5.5, with the user's unimodal stipulation assessed there (PSF16-PSF18). No cell prints the
  s-density mode, by the user's decision; the counts §5.5 needs are PS11.
- [x] **PS9** (2026-09-23, PSQ6 approved; also narrows the drafted §1.5's closing line, "in which it
  does not hold" → "in which the interpretation is not staged that way", flagged to the user): background §2.6's staging claim restated as joint inference of
  the downstream fields given the clamped lexical input.
- [x] **PS11** (2026-09-23, applied on the user's word "start applying"; checkpoint e403106):
  Code Cell A gains `peak_locality_report`, Appendix A a closing paragraph, Text cell 4 a pointer.
  767 configurations under *some* (Part D's nine rows on the Z ladder, the n ladder and K = 101,
  201, 401; the plane at every Z): one peak of φ_S\* and of ℓ₀ in all, both neighbour rules equal to
  the argmax in all; the Beta(1, β) control reproduces PSF18. The count is tie-aware (E18: symmetric
  priors on even-K grids have two equal central nodes). Placement in Code Cell A recorded under I10,
  pending the user. main 0 errors, 8 figures, 15/15, 846 s; appendix_E 0 errors, 5 figures, E3 PASS
  (223 identical / 1 changed / 4 inserted; 263 identical); only Code Cell A's output changed.
  Was: TODO, not to be applied until the user says (user, 2026-09-23): print PSF17's and PSF18's
  counts from a code cell so that `thesis_outline/sections_3-6.md` 5.5 may quote them (C6) — the
  265 configurations in which φ_S\* and ℓ₀ are unimodal under *some* and the neighbour rule agrees
  with the argmax, and the Beta(1, 64) / Beta(1, 256) at Λ = 8 counterexamples. Source:
  `agent/audits/2026-09-23-mode-coordinate/local_rule.py` and `counterexample_output.txt`. A code
  change: needs a checkpoint, the E2/E3 couplings checked if the cell is Code Cell 2 or 2b, and both
  notebooks re-executed.
- [ ] **PS10**, optional, waits on the user: a full-network spectrum with the relay in Code Cell E4
  (code change; re-execution of appendix_E), so E.1 can quote PSF5.

## 4. Questions for the user

- **PSQ1** (A16, user-ruled): the two-number reason is not true of this implementation. Replace it
  with Bogacz's own motivation (line 103) plus the extra operations q needs, restrict it, or drop it?
- **PSQ2**: confirm that the delta is stated as Bogacz's further simplification over x, not a
  consequence of Gaussianity, at background §2.2 and outline §3.6.
- **PSQ3** (A7): may §3.5 stop saying m = 2 is forced?
- **PSQ4** (E1/E2, open since 2026-09-13): may Text cell 3 §8 be restructured and D6's metric stated?
- **PSQ5** (B7/B8): how to treat the coordinate dependence of the delta-like row's mode position.
  **User, 2026-09-23: "we need to think more about this one. As pointed out, the choice carries
  theoretical content and needs to be justified explicitly."** PS8 stays open.

## 5. PSQ5 evidence (agent, 2026-09-23; `agent/audits/2026-09-23-mode-coordinate/`)

Both mode criteria under *some*, read in ζ (the node where φ_S\* is largest, B7/B8) and as a density
over s (the node where φ_S\* − log s(1−s) is largest):

- **PSF9. The dependence is not confined to the delta-like row.** Plane, 121 cells: mode shift 67 (ζ)
  against **121** (s); mode position 59 against 39, differing in 20 cells; conjunction 13 against
  39, differing in 32. Part D: 5 of 9 rows change at least one criterion (flat and Beta(3,1) at both
  Λ, and the delta-like row).
- **PSF10. In s the baselines sit on the grid's edge.** Every Beta(α, 1) with α ≥ 1 has its s-density
  mode at s = 1, Beta(1, 3) at s = 0, and the flat prior has none; on the grid these become the edge
  nodes, s = 0.99753 or 0.00247, which move with the half-width Z. That is why the s-read mode shift
  criterion holds in all 121 cells: it compares against an endpoint the open scale excludes
  (Eq. A1). In ζ, every Beta(α, β) has an interior mode, at log(α/β).
- **PSF11. What fixes ζ in the model.** φ_S is a log-density against the quadrature measure in ζ
  (Eq. 2; I6; the default prior is Gaussian in ζ, A15), so the most active situation unit *is* the
  ζ mode. The s mode needs a fixed per-unit bias, −log s(1−s), which no part of the model supplies.
  Outside source worth checking before citing: MacKay (1998), "Choice of basis for Laplace
  approximation", on mode-based approximations being basis-dependent and the logit/softmax basis
  being the better one for probabilities. **Checked 2026-09-23, see PSF14.**
- **PSF12. The argmax is an operation across nodes.** Selecting the most active unit compares every
  node, as q's normalizer sums over every node: a max where q has a sum. §3.6 reason 1 ("it needs
  no sum across nodes") is true of the delta, which is the settled vector, but not of the mode
  criteria read from it. This is P6's second half, and it bears on the position of A16.

- **PSQ6**: may background §2.6's no-semantic-stage claim be narrowed?

**User, 2026-09-23:** elaborate point 1 (PSF10); check MacKay (PSF11); on point 4, "it is yet unclear to
me whether we want to think of the read-out as part of the system constrained by locality" — look
for any discussion in Bogacz.

- **PSF13 (point 1, `z_dependence_output.txt`).** The s-read baselines are the grid's edge nodes
  exactly: s = 0.99753 / 0.00247 at Z = 6 and 0.99966 / 0.00034 at Z = 8, for the flat, Beta(1,3),
  Beta(3,1) and Beta(64,1) priors. Only the Gaussian prior, whose ζ tails fall faster than the
  Jacobian 1/s(1−s) ≈ e^{|ζ|} rises, keeps an interior s mode (0.5 at both Z). The rule: a
  Beta(α, β) has an interior s mode only if α > 1 and β > 1; its ζ mode is interior for every
  α, β > 0, at log(α/β). The s-read model modes move with Z more than the ζ-read ones (flat 0.947 →
  0.989 against 0.673 → 0.690; Beta(1,3) 0.192 → 0.083 against 0.327 → 0.277). Note also that the
  ζ-read delta-like row moves from 0.94685 to 0.98879 between Z = 6 and 8: that is E17's Z
  dependence, not this question.
- **PSF14 (point 3, MacKay).** MacKay, D. J. C. (1998). Choice of basis for Laplace approximation.
  *Machine Learning, 33*(1), 77–86, https://doi.org/10.1023/A:1007558615313. **Abstract read
  (mlanthology.org):** MAP optimization and the Laplace approximation are both basis-dependent, and
  for models parameterized by probabilities the softmax basis improves on the probability simplex.
  **Full text not read** (Springer requires a login; MacKay's own page returned 403). The detail
  is read from a secondary source, Hennig, Stern, Herbrich & Graepel, *Kernel Topic Models*
  (arXiv:1110.4713, AISTATS 2012), §3.3: MacKay showed that since the softmax's Jacobian is
  proportional to ∏π_k, a Dirichlet in the softmax basis has exponents α_k rather than α_k − 1, does
  not diverge at the boundary for α_k < 1, and is unimodal with its mode at α/‖α‖, which is also its
  mean. For two outcomes the softmax basis is ζ = logit s, and that mode is PSF10's log(α/β). Cite
  MacKay for the basis dependence; read the paper itself before citing the Dirichlet details to him.
- **PSF15 (point 4, Bogacz).** The tutorial has **no read-out stage and no discussion of one.** The
  locality constraints (§1) are stated as conditions on "any computational model" to be
  biologically plausible — a neuron computes from its inputs, a synapse changes from its pre- and
  post-synaptic activity — and the model's output is the activity of the φ nodes itself (§2.2: the
  brain represents only most likely values). Two passages bear on the question:
  - §2.2 (line 97) gives **two** reasons against computing the posterior. (1) Representing it takes
    infinitely many values "rather than a few summary statistics like mean and variance" — the
    source of the user's original "two numbers" wording, stated for a scalar v; (2) **the
    normalization term**: for continuous distributions it is an integral that "would be challenging
    for a simple biological system". Reason (2) is q's cost, in Bogacz's own words.
  - The same passage notes that circuits in the basal ganglia have been proposed to compute the
    normalization term **for discrete distributions** (Bogacz & Gurney, 2007). Our grid is discrete,
    so the tutorial itself names a candidate mechanism, outside the inference network, for a
    normalization over a discrete set.
  Nothing in the tutorial addresses selecting a maximum across nodes (PSF12).

**User, 2026-09-23 (PSQ5 answered in part):** reading over s fails and the notebook reports in ζ, so
add a clarification to the notebook on why s is not used (done: Text cell 4, decision B13; MacKay
(1998) added to main's cell 24 and the dissertation list). The locality question belongs to the
dissertation: background discusses Bogacz's position on the read-out and his basal-ganglia note
(done: background §2.4, +70 words, target 4,160; Bogacz & Gurney (2007) added to the list). The
user asked: doesn't φ_S\* already encode the largest unit, and why must it be searched over the grid?

- **PSF16 (`local_maxima_output.txt`).** Under *some*, φ_S\* has exactly **one** strict local maximum in
  all 9 Part D rows and all 121 plane cells, so the peak unit is the only unit that exceeds both its
  neighbours. Under *no* and *all* it has two to four in most cells (plane: *no* 92 of 121 cells with
  more than one, *all* 35), edge nodes and the lexical step's edges among them. A sketch of why *some*
  is unimodal, not a proof: ℓ₀ is concave in ζ for every prior used, the width part of the utility
  field is negative (`agent/history.md` §4 F4) and so concave, the tilt is linear, and the lexical step under *some* lowers
  the left tail, which only removes candidates to the left of a rising field. Measured, not proved.
- **MacKay (1998), full text read** (the user supplied the PDF): PSF14's secondary-source reading is
  confirmed in the primary (§1; §2, Eq. 10 and Eq. 14; §3, Fig. 1 for the binary case p(a) =
  1/(1 + e^{−2a}), so a = ζ/2).

PS8 status: notebook clarification and §3.6's coordinate done. Open: §3.6's reason 1 ("needs no sum
across nodes") and whether a read-out falls under locality — the user's call, with PSF12 and PSF16 as
the evidence. Flagged, not edited: background §2.4 says "§3.5 derives the utility basis dimension
from [locality]", which PS6's recast of §3.5 no longer supports.

**User, 2026-09-23:** record the field-valued situation level in decisions.md (done: **A21**, with
**D13** in the divergence register); narrow §3.6's reason 3 to the normalization (done; A16 finding;
background §2.2's pointer); pose the read-out's locality as an open question in §5.5 with the
unimodal/neighbour nuance, and verify whether the user's proposed stipulation — the read-out assumes
a unimodal posterior and compares neighbours only — resolves it (done: §5.5 bullet, +120 words;
§3.6 +30; Total 5,820).

- **PSF17 (`local_rule_output.txt`).** Under *some*, over Part D's nine rows at every Z ∈ {6, 8},
  K ∈ {101, 201}, n ∈ {2, 4, 10, 20} (144 configurations) and the 121-cell plane: φ_S\* and ℓ₀ each
  have exactly one local maximum in all 265, and the neighbour rule — the peak is the unit exceeding
  both neighbours; the shift criterion is the sign of ℓ₀'s slope at that unit — agrees with the
  argmax on both mode criteria in all 265.
- **PSF18 (`counterexample_output.txt`), predicted before it was run.** Unimodality under *some* fails
  where prior plus utility peak inside *some*'s excluded region, s < 1/2n: Beta(1, 64) and
  Beta(1, 256) at Λ = 8 give two local maxima (for Beta(1, 256) the global one, s = 0.021, is inside
  the excluded region). At Λ = 512 both are unimodal. Beta(1, 3) and Beta(1, 16) are unimodal at
  both Λ. Why *some* is the favourable case: its excluded region is the far tail from where a
  concave ℓ₀ plus a tilt and a negative width peak, so the step removes no candidate; *no* and
  *all* exclude the region that holds that peak.
- **Assessment of the stipulation**, as written into §5.5: it resolves the question for every
  reported mode criterion; it is consonant with the delta and with Bogacz's binocular-rivalry
  remark; it costs a stipulation, a connection among state units Bogacz does not have (his
  within-level Σ of §5.2 connects error nodes and interneurons), the global peak under *no*/*all*,
  and a proof. It does nothing for q.
- C6: PSF17's and PSF18's counts are printed by audit scripts only; a cell must print them before the
  paper quotes them.

**User, 2026-09-23:** the notebook change is a TODO task, not applied (PS11). Fix background §2.4's
misalignment (done: locality is no longer said to derive the utility basis's dimension; §3.5 chooses
m = 2 for tilt and width, locality is what that choice strains, Appendix E buys it back, and §5.1
argues binary branching from it).

**User, 2026-09-24:** clarify in the notebook why the single-node alternative of A21 is not taken.

- [x] **PS12** (2026-09-24): Text cell 3 §1 closes on "Why the situation level carries a field over
  ζ" — the alternative (a single ζ node with a nonlinear generative map, as in Bogacz §2's
  g(v) = v²), three reasons against it, and the price. Markdown only, no number quoted; A21 finding.

**User, 2026-09-24:** a note in the outline on the general design strategy relative to Bogacz's
construction; four points reviewed (linear-Gaussian; the field; θ\*; determinacy and its cost), then
"Draft it in that form".

- [x] **PS13** (2026-09-24): `thesis_outline/sections_3-6.md` §3 opens on "The design strategy"
  (about 100 words; §3 1,460, Total 5,920); decision C9 records the framing and its wording rules.
