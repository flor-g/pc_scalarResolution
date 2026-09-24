# The computational complexity of the simulation (opened 2026-09-24)

Working record under `agent/agent.md` §5.3. Fold into `agent/history.md` when it closes. IDs carry
the prefix **CX** so they do not collide with `thesis_outline/revisions.md`'s R and Q, or with the
NK, OR and PS records.

## 1. The user's instructions

> now let's do this: we want a complexity analysis on the current implementation. Can you suggest
> how we go about it and where do we put the analysis?

> Is it big O or or big Theta?

> Approved. The total complexity uses big O, but how its arrived at should also be broken down. You
> should use big Theta wherever a tight bound is known and use big O only if not. Be clear that this
> is the complexity of the simulation in particular, not that of the architecture (correct?).

"Approved" covers the agent's proposal of the same session: three parts (network size, the cost of
one inference by closed form and by integration, the cost of learning θ_u), derived and then printed
(C6), step counts and not seconds, the evaluation harness's own runtime left out; a new Appendix G
with a Code Cell G in `main.ipynb`; the outline gets rationale and pointers, no new section; the
name "computational complexity", since "realizability" is O7's and "tractable" was rejected there;
§5.1's O(n) against O(log n) left out, being a claim about an architecture not built.

**The "(correct?)" was answered in chat before work began (agent.md §5.4, the user's phrasing):**
mostly correct, with one qualification. Time is the simulation's: a serial machine's Θ(Km) per
step, the Euler step count set by dt, and the closed form, which the network never takes. **Size
is the architecture's**: Θ(K + m) units and Θ(Km) synapses; the simulation's memory is that size
stored. **Settling time in units of τ_φ is also the architecture's**, and O7/§5.3 already carry it.
So the appendix is framed as the simulation's complexity, and names every line that is also a fact
about the architecture.

## 2. Decisions this rests on

- **I14** (new, below): the framing, the notation rule, the placement. User's, 2026-09-24, except
  where I14 marks a part as the agent's.
- **B4**: the step-count ladder holds θ_u fixed, so it is a stated control, labelled in the output
  and justified in the prose.
- **C6**: every number Appendix G quotes is printed by Code Cell G.
- **C7**: no "condition" or "verdict" in the notebook. "Condition number" is used, with Text cell 3
  §2's precedent ("condition number 21.0"); the Θ requirement is written "requirement", not
  "condition".
- **§3.4 of the outline and BG13**: the *stiffness ratio* is not a condition number. Appendix G
  introduces the condition number κ(H) = λ_max/λ_min as a different quantity and prints both.

## 3. Tasks, in order

- [x] **CX0. Checkpoint.** `git status` clean at `22c5b35` (2026-09-24).
- [x] **CX1 (2026-09-24). Code Cell G and Appendix G** in `main.ipynb`, cells 24 and 25; References
  moves to 26. ToC rows added (all links resolve); anchors `appg`, `appg-1`…`appg-4`, `codeg`;
  Eqs. (G1)–(G3), dangling-reference check clean. `agent/agent.md` §1 cell map (27 cells), §2
  item 5's regex (`[A-F]` → `[A-G]`), and the loud-dependency list. Main run twice (the first
  exposed CX-F5): **RUNNER OK, 0 errors, 8 figures, 943 s**. Acceptance PASS: spectrum gap 2.1e-15;
  all fourteen runs converged; decay × 8κ 1.0005–1.0334; every other cell's printed output
  identical to `22c5b35` apart from Code Cell 2b's `cost:` lines; C6 sweep of Appendix G clean. `0475a21`
- [x] **CX2 (2026-09-24). appendix_E re-run** after main's second run: **RUNNER OK, 0 errors,
  5 figures, 1985 s**; E2 19/19; E3 PASS on both cells, Code Cell 2 223 lines identical with the
  usual shape (1 changed, 4 inserted), Code Cell 2b 263 identical and nothing else. `0475a21`
- [x] **CX3 (2026-09-24). Outline**: §5.5's numerical-substrate group gets one bullet (82 words)
  on the simulation's cost, pointing to Appendix G and naming how n reaches the cost, the (K, Z)(n)
  proposal included; Tier C gains Appendix G. §5.5 745 → 830, §5 2,085 → 2,170, total 6,350 →
  6,435, headings in step. `revisions.md` §17 records it. `ec2eb0d`
- [x] **CX4 (2026-09-24). Records**: I14 and E20 in `agent/decisions.md`; findings CX-F1 to
  CX-F6 below. `0475a21`

## 4. Findings

- **CX-F1. The spectrum of H is closed-form (Eq. G1).** At σ = 1 and BᵀWB = I:
  {1 (m times), 2 (K − m times), θ_u² + 2 (m times)}, so κ(H) = θ_u² + 2, independent of K and m.
  Checked to 2.1e-15 relative over 45 configurations (scratch probe, 2026-09-24; Code Cell G
  prints it). λ_min(H) = 1 is the "rate is 1" `infer`'s docstring already names.
- **CX-F2. `infer` pays Θ(K³) per call for a number Eq. (G1) gives in closed form.**
  `stiffest_state_rate` runs a dense eigendecomposition of the (K + m)-square H, and `infer` calls it
  twice (the tolerance and τ_ε). At K = 101 it is negligible against the steps; at K = 3201 it is
  3.2 s per call on this machine, against 0.06 s of stepping at θ_u = 2. **Not changed**: it is
  `code cell 1` and E1 (coupling 9), and outside this task. Named to the user.
- **CX-F3. The step count is Θ(κ log) in every printed run.** The largest derivative's decay per
  step over the second half of the run, × 8κ(H), is 1.0334 at κ = 6 falling to 1.0005 at κ = 402:
  the slowest mode is excited, which is the requirement the lower bound needs. N/κ is 176–204 and
  does not move with K (1223, 1224, 1223 at κ = 6) or with m (182.3, 187.0, 187.5 at κ = 102).
- **CX-F4. The architecture's settling time does not carry θ_u².** N dt/τ_φ falls from 25.5 at
  κ = 6 to 22.0 at κ = 402. The growth of N with θ_u² is the separation 8λ_max(H) = τ_φ/dt counted
  in steps. The fall itself is the tolerance: it is keyed to λ_max(H) (I3), so log(a/tol) shrinks
  as θ_u grows.
- **CX-F5. At the sizes run, the wall clock does not show the per-step Θ(Km).** At θ_u = 2 the
  per-step time was 45–53 µs from K = 101 to 3201, and the K = 3201 figure came out negative in the
  first full run (−119.3 µs): 1224 steps are too few against two 3.3 s eigendecompositions. The block
  now times at θ_u = 20 (70,865 steps): 45.7, 48.9, 57.2, 67.0 µs at K = 101, 401, 1601, 3201 in a
  scratch run, so K × 32 costs × 1.5. A fixed per-operation overhead dominates the arithmetic. The
  eigendecomposition does show its growth. The appendix says so, qualitatively, and quotes no
  second.
- **CX-F6. n is not free of cost after all.** n appears in no per-step or construction count, but it
  sets θ_L, so c_y, so θ_u\*, so κ(H). The proposal's "n costs nothing at fixed K" was wrong as
  worded; the appendix says n enters only through θ_u\* (and through K under §5.5's proposal).
