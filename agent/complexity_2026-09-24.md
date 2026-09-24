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
  4. Appendix G §2's table row and its "choices of this instantiation" sentence, Eq. (G3)'s K³
     term, and the outline §5.5 bullet's total all change with it.
  Acceptance: both notebooks re-run, no printed line changes outside `cost:` lines and Appendix G's
  own, and λ_max agrees with the decomposition to roundoff at every configuration Code Cell G lists.
- [ ] **CX7. OPEN (user, 2026-09-24): can the cost take part in the dynamics?** Not settled, and
  not yet written into any notebook, outline or `agent/decisions.md` entry; the user will examine it
  further. The question as posed: RSA writes utility as informativeness minus cost; this model has
  no cost in its dynamics; would adding **Appendix G's** cost (this instantiation's complexity, read
  as a representation of the process's cost) to μ_u break locality or the construction?
  **The user's argument, as it stands:**
  1. The true cost is not available to the system at any time t: it is a property of the whole
     trajectory, halting step included, so no state before the halt fixes it.
  2. Adding it to the dynamics makes the system self-referential (φ at t depends on the cost, which
     depends on φ after t), and does so **even with locality set aside**.
  3. So any stipulated participation of cost in the dynamics is not the true cost. Once a term takes
     part, the true cost is the cost of the modified system; the two agree only at a fixed point
     C = cost(dynamics given C), which the evaluator can solve for and the system never computes.
  4. RSA's own treatment of cost is set aside by the user as not obviously right; nothing here rests
     on it.
  **Corrected on the way (the user's):** committing this instantiation's cost to the algorithm is
  not a confusion of levels. It makes this instantiation the algorithm, which is one more commitment
  and no defect in itself. The agent's argument from non-uniqueness had cause and effect reversed and
  is withdrawn; the objection that remains is the self-reference of 1–3.
  **Qualifications the agent raised, not yet discussed:**
  - (a) Of N ≈ 8κ(H) log(a/tol) (Eq. G2), the factor κ(H) = θ_u² + 2 is a function of the current
    θ_u, fixed within an inference, and so is determined before the inference starts; only the log
    factor and the halting step depend on the trajectory. Coupling κ(H) into μ_u would still close a
    loop, μ_u → θ_u\* (Appendix B) → κ(H) → μ_u, but a loop in what determines what rather than in
    time. So "not available at any t" holds of the full cost, not of its dominant factor.
  - (b) θ_u changes between inferences (τ_θ ≫ τ_φ), so the realized cost of a *completed*
    inference could reach the slow timescale as ordinary feedback without self-reference. It would be
    the cost of past inferences, never of the current one; and it needs a halting signal this phase
    does not commit to (A19 is a direction; the λ_max-keyed tolerance is D12's open locality problem).
  - (c) On the locality side, for any per-utterance or per-trial μ_u: Bogacz encodes v_p in synaptic
    strength, maintained over the lifetime, so a μ_u that changes with the input stops being a
    parameter and becomes an input activity at the top of the chain; and a y-dependent prior on φ_u
    makes the directed generative model cyclic unless the utterance's form is split off as a root
    observation. Both were raised under the agent's first, mistaken reading (utterance complexity in
    RSA's sense) and may or may not bear on the reading above.
  **The user's ruling on (a) and (b), 2026-09-24:** agreed, both. They are the **forms in which a
  proxy of the cost can take part in the dynamics**: (a) a configuration-level proxy, κ(H), available
  before an inference starts, whose coupling closes a loop in determination and not in time; (b) a
  cross-trial proxy, the realized cost of completed inferences fed to the slow timescale, conditional
  on a halting signal. Neither is the true cost of the inference in progress, which steps 1–3 keep.
  **Next (the user's):** before steps 1–3 are settled, clear what "self-referential" commits the
  argument to, against the literature on self-reference (Hofstadter's GEB; Open questions about time
  and self-reference in living systems, in the user's reading list).
  **The literature review (agent, 2026-09-24) and the user's rulings on it.** Read: Abramsky,
  Banzhaf, Caves, Levin, Machado, Ofria, Stepney & White (2026), *Open questions about time and
  self-reference in living systems*, R. Soc. Open Sci. 13: 261059 (the user's reading list); searched
  and verified: Wolpert (2008, Physica D 237: 1257–1281); Kauffman (2005, EigenForm, Kybernetes 34:
  129–150) and von Foerster on eigenbehaviour; Russell & Wefald (1991, AI 49: 361–395); Russell &
  Subramanian (1995, JAIR); Mar & Grim (1991, Noûs 25: 659–693); Niv, Daw, Joel & Dayan (2007,
  Psychopharmacology 191: 507–520). From memory, unverified: Hofstadter (1979, 2007); Rosen (1985,
  *Anticipatory systems*); Shenhav, Botvinick & Cohen (2013, Neuron). Already in the dissertation's
  list: Griffiths, Lieder & Goodman (2015); Lieder & Griffiths (2020); Friston (2010).
  What bears on the argument: the paper's §4.2 (self-reference is paradoxical only in a timeless
  projection; in natural time a reference to oneself is resolved by a future self, and, after Rosen,
  a system can be driven by an anticipated future state, not an actual one) diagnoses steps 1–2 and
  names (a) as anticipation and (b) as the spiral; its §2.2 (whole-to-whole self-reference is not
  necessarily paradoxical); its footnote 8 (a fixed update rule admits closed forms, a self-modifying
  one in general does not); its §6.1.2 (eigenforms: a self-referential equation's solution realized
  by unwinding it in time); Bennett's criterion for representational time as the paper reports it
  (met by θ_u, not by the fast subsystem). Bounded optimality and resource-rational analysis place
  the true cost outside or across runs, not inside the running algorithm: the established position
  closest to the user's. Niv et al.'s tonic average reward rate is a biological instance of (b).
  The free-energy principle's complexity term is a state function and takes part without
  self-reference, which fixes the scope of step 1.
  **Amendments, approved by the user 2026-09-24:**
  - Step 1 names its object: the true cost is a **functional of the trajectory** (steps, settling
    time, dissipation). Costs that are functions of the current state are out of its scope and can
    take part without self-reference.
  - Step 2 says **self-referential, not paradoxical**. The obstacle within an inference is causal:
    the present state would have to be driven by the completed trajectory, a future self; only an
    anticipated cost can do that (Rosen).
  - Step 3 is restricted to **the inference in progress**. Across inferences, (b) iterated,
    C_{k+1} = cost(dynamics given C_k), reaches the fixed point as an eigenform if the map is a
    contraction, and oscillates or diverges otherwise.
  - The argument is kept **free of Gödel, Turing and Wolpert**: the dynamics here are predictable
    from outside to within constants (Eq. G2), and the argument rests on the temporal premise alone.
  **The user's further instructions, 2026-09-24:**
  > Nevertheless, I think this line of literature is worth a footnote.
  > Besides that we want to lead the argument with one background sentence of why we brought it up:
  > both neo-Gricean literature and Relevance Theory involves cost in their dynamics. We want to
  > discuss what cost-in-dynamics means to a system like what is instantiated in this dissertation.
  - **A footnote** on the classical limits of self-reference (Gödel, Turing, Wolpert 2008): why the
    argument does not rest on them, with pointers to the tradition that treats self-reference as
    unfolding in time (Hofstadter; Abramsky et al. 2026).
  - **A lead sentence**: neo-Gricean pragmatics and Relevance Theory both put cost into
    interpretation; the question is what cost in the dynamics means for a system of the kind
    instantiated here. **Accuracy point raised with the user (agent.md §5.4), awaiting a ruling:** the
    two put different costs there. Neo-Gricean cost (Horn's 1984 R-principle; Levinson's 2000
    M-principle) is mainly the *speaker's* economy of expression, which the hearer reasons *from*: a
    represented quantity, a function of the utterance's form, which steps 1–3 do not exclude. Relevance
    Theory's effort is the *hearer's own* processing effort, part of what relevance is and of when
    comprehension stops (Sperber & Wilson 1995; Wilson & Sperber 2004): squarely in scope, and its
    stopping rule parallels A19's halting question. Neither work is yet in the dissertation's
    reference list (only Horn 1972 and Levinson 2000 are).
  **To settle:** whether 1–3, amended, is the position the dissertation takes; the lead sentence's
  wording, after the accuracy point; and where the argument is written, and at what length
  (candidates: an `agent/decisions.md` entry; §5.3, which interprets the cost;
  §5.5; Appendix G).

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
