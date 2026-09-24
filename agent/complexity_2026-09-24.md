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

Later in the session, after the agent had twice misread the scope:

> I might not have explained myself clearly. We have three concepts at hand: the process, the
> architecture, the simulation. The architecture is essentially an algorithm which we claim to
> represent the true process. The simulation is an instantiation of the algorithm, and therefore a
> representation of the architecture. Therefore the simulation is to be understood as a
> representation of the true process. --- That being said, the simulation is not the only possible
> instantiation of the architecture, nor is the architecture the only possible representation of
> the true process. Hence when Appendix G's complexity is specifically the complexity of the
> simulation and should not be conflated with the unique complexity of the architecture.

> Good. Now Correct whatever you got wrong in Appendix G and such. Don't touch the
> cost-part-of-algorithm argument yet.

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
- [x] **CX6 (2026-09-24). Correct the framing to the user's three levels** (CX-F7). Appendix G's opening and §3's
  closing paragraph, Code Cell G's header comment, the §5.5 bullet, `revisions.md` §17, agent.md's
  cell map, I14's finding. No printed line changes; notebooks not re-executed (markdown and one
  comment). `cf2a25f`
- [ ] **CX5. OPEN (user, 2026-09-24): remove the avoidable Θ(K³) from `infer`** (CX-F2).
  `stiffest_state_rate` finds λ_max(H) by a dense eigendecomposition of the (K + m)-square H, and
  `infer` calls it twice per inference (the tolerance and τ_ε); Eq. (G1) gives λ_max(H) = θ_u² + 2
  in closed form at σ = 1 and BᵀWB = I. **What the fix has to respect:**
  1. `code cell 1` and E1 both carry `stiffest_state_rate` verbatim (coupling 9): change both in
     one pass, lifted, not retyped.
  2. The closed form holds only at σ = 1 and G = I. The code carries σ symbolically and supports a
     non-orthonormal B, so either keep the decomposition as the general path with the closed form
     where its premises hold, or state the restriction; do not silently narrow the method.
  3. λ_max(H) keys the stopping tolerance (I3) and τ_ε (I4), so any change must reproduce it to
     roundoff: every step count in both notebooks must be unchanged, E3 included.
  4. Appendix G §2's table row and its "costs of this implementation" sentence, Eq. (G3)'s K³
     term, and the outline §5.5 bullet's total all change with it.
  Acceptance: both notebooks re-run, no printed line changes outside `cost:` lines and Appendix G's
  own, and λ_max agrees with the decomposition to roundoff at every configuration Code Cell G lists.

## 4. Findings

- **CX-F1. The spectrum of H is closed-form (Eq. G1).** At σ = 1 and BᵀWB = I:
  {1 (m times), 2 (K − m times), θ_u² + 2 (m times)}, so κ(H) = θ_u² + 2, independent of K and m.
  Checked to 2.1e-15 relative over 45 configurations (scratch probe, 2026-09-24; Code Cell G
  prints it). λ_min(H) = 1 is the "rate is 1" `infer`'s docstring already names.
- **CX-F2. `infer` pays Θ(K³) per call for a number Eq. (G1) gives in closed form.**
  `stiffest_state_rate` runs a dense eigendecomposition of the (K + m)-square H, and `infer` calls it
  twice (the tolerance and τ_ε). At K = 101 it is negligible against the steps; at K = 3201 it is
  3.2 s per call on this machine, against 0.06 s of stepping at θ_u = 2. **Not changed**: it is
  `code cell 1` and E1 (coupling 9), and outside this task. Named to the user, who made it an
  open task to fix: **CX5**.
- **CX-F3. The step count is Θ(κ log) in every printed run.** The largest derivative's decay per
  step over the second half of the run, × 8κ(H), is 1.0334 at κ = 6 falling to 1.0005 at κ = 402:
  the slowest mode is excited, which is the requirement the lower bound needs. N/κ is 176–204 and
  does not move with K (1223, 1224, 1223 at κ = 6) or with m (182.3, 187.0, 187.5 at κ = 102).
- **CX-F4. The architecture's settling time does not carry θ_u².** *(Its framing is superseded by
  CX-F7: the settling time is a quantity of the shared equations, not "the architecture's" cost.)* N dt/τ_φ falls from 25.5 at
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
- **CX-F7. The first framing was wrong (the user's correction, 2026-09-24).** The agent's answer to
  "(correct?)" in §1 split time from size and gave the size and the settling time to "the
  architecture", on the grounds that a parallel instantiation updates every unit at once. That took
  one instantiation to be the architecture, and denied that the simulation's cost represents the
  process's. The user's three levels (§1): the simulation represents the process through the
  architecture, and its complexity is this instantiation's, not the architecture's unique one.
  Appendix G, the §5.5 bullet and I14 were written on the first framing; CX6 corrects them. The
  argument about cost taking part in the dynamics is held back by the user and not recorded yet.
