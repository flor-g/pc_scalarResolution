Sections 3 6 outline · MD
# Outline for the proposal, evaluation, and discussion sections
 
Scope: §§3–6, approximately 3,520 words (`revisions.md` §3: R1, S-6, P-3, and the 2026-09-22 raise of §5.5 for A19). Written against
`main.ipynb` (Text cells 1–6, Code Cells 1–4, Appendices A–D with Code Cells A–D, Eqs. (1)–(41))
and `appendix_E.ipynb` (Eqs. (E1)–(E6)).
 
---
 
## Central claim
 
The dissertation argues a positive thesis and, from the shape of what its architecture does not
yet contain, a second constructive one.
 
**Thesis.** A predictive-coding network organized under the free-energy principle, in which the
observed utterance's lexical entry is the only lexical quantity represented and no alternative is
consulted at any point in an inference pass, reproduces part of the profile of scalar
strengthening. Movement of belief mass away from the *all* reading therefore does not, by itself,
require a within-trial computation over alternatives. What produces the movement is measured
rather than assumed: the utility level amplifies the observed entry's own low-rank projection of
the prior–lexicon net (Eqs. 23–24), under a gain $\theta_u$ whose value is fixed by cross-trial
exposure rather than by anything about the current trial.
 
**Constructive claim.** The architecture meets the two-condition criterion of §4.2. At a lexical
strength that holds every entry against each of the five priors ($\Lambda=512$), both conditions hold
under three of the five priors, the three with the most prior mass on the all-region, and the
second holds under all five, so among these priors the two conditions are nested (§4.4). Across
the plane of lexical strength against prior concentration both hold in 33 of 121 cells, in a band
whose shape two opposed floors set: as the prior sharpens, the first condition's floor in $\Lambda$
falls and the second's rises (§4.5). The case for a level representing within-trial competition
among alternatives therefore does not rest on the criterion failing (R2). It rests on what such a
level would save:
- branching logarithmic in the predicate's granularity;
- one dimension per level, so plasticity is local without the relay;
- an affine generative map that keeps the convergence proof;
- a read-out that needs no normalization across the scale (§5.1);
- an end to learning short of a maximizer the slow flow never reaches, which the present
  architecture lacks (§5.3; argued, not derived);
- and, on the plane, a drain keyed to the alternative rather than to prior mass on the all-region,
  which would not carry the second condition's floor up as the first's falls (§4.5's floors; argued
  in §5.1, not measured).

**Such a level is compatible with this architecture; it is specified here and not
built.** What the dissertation contributes in its place is that specification: the construction the
model works under states exactly what any additional level must supply — a state space, a position
in the chain, generative maps in both directions, and a convergence argument — and §5.1 discharges
as much of it as the present results determine, naming precisely what is left.
 
**Standing qualification, carried into §5.** Neither claim says that human scalar strengthening
lacks a within-trial alternatives computation, and nothing in this implementation could show it:
the model has no alternatives space to begin with. The claims are about what the *effect*
requires, not about what human processing contains.
 
---
 
## Scope decision: what the architecture implies, and what the paper carries
 
The recommended policy follows Composition Guide Entry 3: what the argument needs is kept and
used; what neither argument nor reader needs is cut; what the argument does not need but the
reader should weigh is recorded as a fact with our position reserved.
 
**Tier A — carried in the main argument.**
 
| Result | Where | Why it is load-bearing |
|---|---|---|
| Amplification mechanism, Eqs. (23)–(24) | §3.5, §4.4 | It is what produces the effect, and it is measured |
| The two-condition criterion and its results | §4.2–§4.5 | The verdict, and the evidence that the conjunction is reachable |
| Conventionalization of $\theta_u^\ast$ by exposure (App. B) | §3.4, §5.1 | The position the architecture commits to |
| The four construction obligations (Text cell 3; §8; App. B) | §5.1 | Turns the gap into a specification |
| Binary branching per level, and $m=1$ (App. C §§2, 5) | §5.1 | Makes the alternatives level tractable and local |
| Non-locality of normalization across word forms (App. A) | §5.1 | The obstacle binarity removes |
| The relay, Eqs. (E1)–(E6) | §3.4, §5.5 | Locality at $m>1$, and the cost it carries |
| $\theta_L$ as predicate granularity, Eqs. (A5)–(A6) | §3.3, §5.1–§5.2 | Sets the search's resolution; the closed/open prediction |
| $m$ = threshold count and the parity argument (App. C) | §3.5, §5.1–§5.2 | Fixes dimension; the mechanism behind §5.2 |
| Closed vs open scale, extreme-favouring (new, §5.2) | §5.2 | Second empirical anchor; connects to Xiang et al. |
| Strict concavity, unique fixed point, closed forms | §3.4, §4.3 | Makes the dynamics a testable implementation claim |
 
**Tier B — recorded as a fact, position reserved.** One or two sentences each, no verdict, in §5.5
or a footnote.
 
- *Exact zero is unrepresentable* (App. A): a predicate over $n$ atoms cannot distinguish "none"
  from "fewer than half an atom", so *no* means *below the resolution limit*. The notebook already
  reserves its position; the paper should do the same rather than argue it.
- *The O corner costs nothing* (App. C §4): *not all* introduces no threshold and so no dimension.
  The model's verdict is that Horn's (1972) lexicalization gap is not representational. (It also
  bears on §5.1: enlarging the alternative set need not enlarge the space.)
  **What the implementation predicts, and how far (O9, settled 2026-09-21).** The reflection
  $\zeta\mapsto-\zeta$ carries the inventory onto its mirror exactly, so **this implementation
  predicts that the O corner is just as representational**. State the limit in the same breath: the
  prediction is about the architecture as it stands, and it is **not** carried into the phase §5.1
  proposes, where the two endpoints stop being fixed by the same threshold and become asymmetric
  (§5.2's instinct sentence; `decisions.md` O14). Position reserved on $\mu_u$, the one quantity
  that breaks the mirror. Quote no number here unless a cell prints it first (C6): the equivariance
  is measured in an audit, not in a notebook.
- *Exclusion over truth sets* (App. D): stated in §3 in two sentences as a forced design choice,
  not as a finding — though §5.1 now gives it a second, independent motivation.
**Tier C — left in the notebook and cited.** Conditioning and stiffness (Eq. 28); the
$\mu_u$/$\ell_0$ common-mode invariance and its polar sweep (Eqs. 32–35); the flat-direction
resolution (§9.1); grid refinement; the multidimensional ceiling (§9.3), except for one sentence
in §5.5; the weight-transport accounting of § E.2.
 
---
 
## Word allocation

Kept in step with `revisions.md` §3, which is the authority: 2,400 → 3,000 (R1) → 3,200 (S-6) →
**3,520** (P-3, then §5.5 raised 80 → 150 on 2026-09-22 for A19's halting bullet). The "was" column is the 2,400 allocation this outline was written to.

| Section | Was | Words | Function |
|---|---:|---:|---|
| **3. The proposed architecture** | 800 | **1,085** | |
| 3.1 What the model must do | 90 | 90 | Four design requirements |
| 3.2 A continuous world state and a soft lexicon | 160 | **270** | Eq. (1); $\varphi_L=\Lambda\chi_y$; defeasibility as the price; the Λ–ℓ₀ commitment and Λ → ∞ as RSA's L₀ (R18) |
| 3.3 The chain, and the semantics of its threshold | 200 | **255** | Eq. (7); $\theta_L$ from granularity; $\mu_u\ne0$; the projection parallel and its warning (R19) |
| 3.4 State units, error units, and what is local | 210 | **230** | Concavity, closed forms, the relay; commitment 7; $\theta_u$ learned |
| 3.5 Two choices the scale forces | 140 | 140 | $m=2$ from threshold parity; the amplification axis |
| 3.6 Two read-outs (new) | — | **100** | `revisions.md` §5, item 1 |
| **4. Evaluation** | 745 | **1,020** | |
| 4.1 What is compared | 100 | **140** | Three beliefs; RSA/wRSA as analytic baselines only; q_lit's status depends on A3 |
| 4.2 The criterion, and how to read the statistics | 170 | 170 | The conjunction; the softmax-nonlinearity guard |
| 4.3 The specification holds | 90 | **70** | Closed forms, Hessian, grid (trimmed to fund §4.5, R14) |
| 4.4 The five priors | 220 | **285** | The Λ = 512 table, the Λ = 8 contrast, the Cremers parallel, the mechanism |
| 4.5 The plane, and where both conditions hold | 165 | **255** | The band; the opposing floors, where the trade-off claim is sourced; the V; Eq. (41) |
| 4.6 What the verdict needs, against what θ\* costs (new) | — | **100** | `revisions.md` §4's §4.6 entry |
| **5. Discussion** | 705 | **1,180** | |
| 5.1 What an alternatives level would have to supply | 390 | **350** | The specification, and what is left undone |
| 5.2 Scale structure: a second prediction | 200 | **400** | H1 and H2 against Xiang et al. (R16, R17) |
| 5.3 Realizability, halting, and the plausibility commitment (new) | — | **170** | `revisions.md` §5, item 2 |
| 5.4 What an algorithmic account makes posable (new) | — | **120** | `revisions.md` §5, item 3 |
| 5.5 Limits (was 5.3) | 65 | **150** | Convergence status, linear-Gaussian caveat, the relay's cost, **halting by tolerance** (raised from 80 on 2026-09-22: the section carried six topics at 80 and A19 adds a seventh) |
| 5.6 Predictions (was 5.4) | 50 | **60** | Exposure; granularity; the midpoint cut; the timescale separation |
| **6. Conclusion** | 150 | **165** | |
| **Total** | **2,400** | **3,520** | |

**What this table does not do.** §§3.6, 4.6, 5.3 and 5.4 are new sections whose content is planned
in `revisions.md` §5 and whose bodies are not written in this outline yet; Limits and Predictions
keep their text under their new numbers, §5.5 and §5.6. Only the headings of §§3.2, 3.3, 4.1, 4.4,
4.5 and 6 have bodies rewritten to their new budgets (tasks U9–U12); the rest carry the new figure
against text still written to the old one.

# 3. The proposed architecture (about 1,085 words)
 
## 3.1 What the model must do (about 90 words)
 
Four requirements, each traceable to a commitment the implementation actually makes rather than to
a desideratum imposed from outside:
 
1. The world state is a proportion on a dense scale, so its representation must be a field rather
   than a finite set of categories.
2. World knowledge must constrain interpretation while remaining defeasible, which is what a finite
   lexical strength buys and what a hard semantic mask forecloses.
3. Every message must be local in Bogacz's (2017) sense — computation from a unit's own afferents,
   plasticity from the activities a synapse connects.
4. The objective's stationary point must be available in closed form, so that the recurrent
   dynamics can be assessed as a claim about implementation rather than assumed to converge.
Requirement 4 is what distinguishes this model from a fit, and §4.3 reports the test.
 
## 3.2 A continuous world state and a soft lexicon (about 270 words)
 
- The world state is a proportion $s\in(0,1)$ carried in logit coordinates,
  $\zeta=\operatorname{logit}(s)$ (Eq. 1). Because $\operatorname{logit}$ is a bijection
  $(0,1)\to\mathbb R$, this is a change of coordinates and not a modelling assumption. Integrals
  over $\zeta$ are evaluated on a fixed quadrature grid (Eq. 2), and the grid discretizes the
  integral rather than the state: no quantity in the model is defined in terms of a node. State the
  point explicitly, because a reader will otherwise take $K$ for a state-space size. **Flag for
  §5.1 that $\zeta$ is a log-odds coordinate**; that fact does work twice later.
- Each utterance carries an **exclusion set** $E_y$, the states its entry rules out (Eq. 5), and the
  lexical field is that set's indicator scaled by lexical strength, $\varphi_L=\Lambda\chi_y$
  (Eq. 6). Two sentences on why exclusion rather than the truth set: under exclusion, "this entry
  carries no lexical information" and "this entry contributes no lexical field" are one statement,
  since the tautology maps to $\varphi_L=0$.
- **The price of a soft lexicon.** $\Lambda\to\infty$ recovers a hard truth-conditional constraint,
  and the object at that limit is RSA's literal listener. Introduce the base world prior here, where
  it first does work: $\ell_0=\log p_0$ at the grid nodes, a log-density over $\zeta$. The field
  $\ell_0-\Lambda\chi_y$, the prior restricted by the entry, is then §1.2's
  $\log L_0(s\mid u)=\log P(s)+\log\llbracket u\rrbracket(s)$ up to $L_0$'s normalizer, in
  $\zeta$'s coordinates: $\ell_0$ plays $\log P(s)$, and $-\Lambda\chi_y$ plays
  $\log\llbracket u\rrbracket\in\{0,-\infty\}$ with $-\infty$ replaced by $-\Lambda$. One clause in
  the paper, about 20 words; §3.3 returns to the normalizer. Finite $\Lambda$ buys differentiability
  and makes the lexicon *defeasible*. A sufficiently confident prior therefore overrides the entry
  outright, so that the model, told *no*, comes to believe $s\approx1$. §4.5 measures where it
  bites (Eq. 41).
- **Where the prior meets the entry is a commitment, and the paper says so (R18).** The override is
  a contest between $\Lambda$ and $\ell_0$. The model stages that contest at one node because
  $\ell_0$ enters through the map predicting the lexical field from the situation belief,
  $g_L(\varphi_S)=\ell_0-\varphi_S$ (Eq. 9): the entry and the prior then meet as a single
  difference in the lexical level's residual, $\varphi_L-g_L(\varphi_S)=\varphi_L-\ell_0+\varphi_S$,
  which one error unit carries (Eq. 11; Bogacz, 2017), and raising $\Lambda$ pushes against $\ell_0$
  there. **Nothing in the construction forces $\ell_0$ into $g_L$** (`decisions.md` A3). It could
  have entered one map up, in the map from the utility state: $g_L(\varphi_S)=-\varphi_S$ with
  $g_S(\varphi_u)=\ell_0+\theta_uB\varphi_u$ (Eq. D5). That placement is as local as Eq. (9) and
  has the same Bogacz status (Appendix D Sec. 5), so locality does not decide between them. Give the
  three reasons for the choice, one clause each:
  1. *The architecture is cleaner.* Under Eq. (9) the contest is one unit's activity. Under
     Eq. (D5), $\ell_0-\varphi_L$ is no unit's activity and exists only as a combination of two
     residuals.
  2. *It builds in a hypothesis about the dynamics:* that the world prior and lexical strength
     counteract. Under Eq. (9) the two enter Eq. (15) as one term with one weight. Under Eq. (D5)
     they still oppose each other in $\varphi_S^\ast$, but less directly, since the prior is then
     weighted with the utility level's prediction and the entry apart from it. The hypothesis has
     empirical content: the two placements return the same situation field from the same utility
     state only while the lexical and situation levels' variances are equal, $\sigma_L=\sigma_S$,
     and otherwise differ in it by $(\sigma_L-\sigma_S)\ell_0/S$ with $S=\sigma_L+\sigma_S$, so a
     later precision-bearing phase tests the placement instead of inheriting it.
  3. *The literal listener is a state the network reaches.* Under Eq. (9) the field
     $\ell_0-\varphi_L$ is what Eq. (15) returns as $\sigma_S\to\infty$, when the utility level's
     prediction carries no weight. Under Eq. (D5) no setting of the variances returns it. §4.1's
     baseline rests on this reason.

  Close on what the choice changes. The two placements differ in one quantity, the utility level's
  drive $c_y$ (§3.3), and there only by the sign the prior carries against the entry: the couplings
  differ by $2B^{\mathsf T}W\ell_0$, the same vector whatever was uttered (Eq. D7). §4.4 reports what
  raising $\Lambda$ does under Eq. (9). The rows under Eq. (D5) are a **counterfactual
  manipulation**, not a control, and stay in Appendix D and Code Cell D. About 90 words in the
  paper, and no number quoted here.
## 3.3 The chain, and the semantics of its threshold (about 255 words)
 
- The chain of prediction runs $y\leftarrow\varphi_L\leftarrow\varphi_S\leftarrow\varphi_u\leftarrow1$
  (Eq. 7). $\varphi_L$ is clamped by the observed entry, so $\varepsilon_y\equiv0$ (Eq. 8) — **as a
  consequence of the clamp, not as a stipulation**. Appendix A makes the difference matter: the
  gradient of the utterance-level weight $\theta_L$ vanishes identically while $\varepsilon_y\equiv0$
  (Eq. A4), so unclamping $\varphi_L$ sets it running by the same route that would let a
  word-recognition model stack beneath. The architecture is written to be extended, and §5.1 takes
  up what extending it would cost.
- **$\theta_L$ is semantic, and this is where the architecture earns a linguistic commitment.**
  Because $\operatorname{logit}$ is asymptotic at the endpoints, realizing $E_y$ on the scale
  requires a threshold $\theta_L>0$ (Eq. A1). Declaring $\varsigma(-\theta_L)=1/2n$ gives it a
  denotation: **$n$ is the number of atoms the predicate resolves** (Eq. A5), the threshold sits at
  half a Voronoi cell, and the entries exclude precisely the states outside the cell each anchors.
  Where no atom count exists the declaration is unchanged and so is the name: $n$ is then the
  number of distinguishable steps the scale affords, the reciprocal of a just-noticeable
  difference, and need not be an integer. The two cases differ in where $n$ comes from, not in the
  formula (O1). $n$ is the size of the space §5.1's search runs
  over, and §5.2 turns the same quantity into a prediction.
- **The chain terminates in utility.** $g_S$ carries the utility state into the situation field
  through a fixed profile matrix $B$ (Eq. 10; Eq. E2 at the relay), and carries nothing else:
  $\ell_0$, which could have entered here as a tonic offset, enters at $g_L$ (§3.2). $\mu_u\ne0$ is
  a standing requirement: at $\mu_u=0$ the terminating contribution vanishes for every $\theta_u$,
  the chain stops rather than terminates, and $\theta_u$ becomes unidentifiable along the degeneracy
  $(\theta_u,\varphi_u)\mapsto(c\theta_u,\varphi_u/c)$. This is Bogacz's own unstated premise
  ($v_p\neq0$) stated; Appendix B sharpens it to $\langle\mu_u,\sum_y c_y\rangle\neq0$, a condition
  on direction, where $c_y$ is the drive the field below exerts on the utility level under entry
  $y$ (Eq. 16, next bullet).
- **What the utility level reads: a projection, and not an equivalence (R19).** At the stationary
  point, the afferent sum each utility unit forms through its own profile,
  $\theta_u\langle\varepsilon_S,b_i\rangle$ (Eq. 19), takes in the field below through one
  quantity, $c_y=B^{\mathsf T}W(\ell_0-\varphi_L)$ (Eq. 16), one pairing per column of $B$. By
  §3.2, $\ell_0-\varphi_L$ is $\log L_0$ up to its normalizer, with $-\infty$ softened to $-\Lambda$,
  so **the utility level reads a linear projection of the same log quantity RSA's $S_1$ reads**
  (§1.2), softened as the lexicon is. State that, and warn in the same
  breath that a projection does not imply an equivalence and that forgetting the difference is
  dangerous. Give the warning its exact form: $B^{\mathsf T}W\mathbf 1=0$, so $c_y$ is blind to the
  constant direction, which is exactly where $\log L_0$'s normalizer lives, and keeps only the
  field's coordinates along the columns of $B$ — at $m=2$, the tilt and the width of §3.5. The
  normalizer is what RSA's informativity runs on: for two utterances true at the same state, their
  unnormalized $\log L_0$ agree there, and $S_1$'s preference between them, cost aside, comes from
  their normalizers alone. Then the nuance that must not be got wrong: the invariance belongs to the
  coupling, and the model does not share it. Eq. (15) carries the constant into $\varphi_S^\ast$,
  and Eq. (21)'s strict concavity leaves no flat direction for it to vanish along; never write that
  the model is constant-invariant. Code Cell D prints both facts (Appendix D Sec. 5). About 45 words
  in the paper; the normalizer sentence is the agent's addition to R19 and the first to cut if the
  bullet overruns.
## 3.4 State units, error units, and what is local (about 230 words)
 
- Error units relax toward their residuals and state units ascend $\mathcal F$ (Eqs. 18–19), both
  instances of Bogacz's Eqs. (53)–(54). The slow parameter follows his own gradient under
  $\tau_\varepsilon\ll\tau_\varphi\ll\tau_\theta$. There is no learning rate and none is required:
  the constant of proportionality is a time constant of the kind the error and state units already
  carry.
- **Why the dynamics are a claim and not an assumption.** $\mathcal F$ is strictly concave in
  $(\varphi_S,\varphi_u)$ for *every* $\theta_u$ and *every* $\Lambda$ (Eq. 21), and Eq. (22) lifts
  this to arbitrary $B$ and arbitrary $m$. So there is a unique global maximum and the closed forms
  Eqs. (15)–(16) are *the* solution. Note §8.1(iii): $\varphi_L$ does not enter the Hessian at all,
  so every convergence result is independent of the shape of the lexical field — which is what §5.2
  will need. The honest qualification belongs here: because the model is linear-Gaussian while
  $\varphi_L$ is clamped, the recurrent dynamics are a claim about **neural implementation**, the
  status they have in Bogacz's own linear examples, and the closed forms are what make that claim
  testable.
- **Locality, and the relay that secures it.** The ranking inverts against expectation: Bogacz's
  free matrix $\Theta$ is local without comment, and our scalar restriction $\theta_u B$ is what
  needs defending, because tying $K\times m$ entries to one scalar is weight sharing. At $m=1$ the
  defence is that $b$ is the fixed spatial profile of one projection, so $\langle\varepsilon_S,b\rangle$
  is a single signal at a single synapse. At $m>1$ that defence gives out (Eq. B4), and the
  implementation runs at $m=2$. Appendix E closes the gap by inserting a relay: the columns of $B$
  become the terminal fields of the $\varphi_u$ axons, so $r=B\varphi_u$ (Eq. E1) is formed in one
  node's dendrite, and the rule becomes $\tau_\theta\dot\theta_u=\langle\varepsilon_S,r\rangle$
  (Eq. E4) — pre times post, at any $m$. **The sum is relocated, not removed**: out of the
  plasticity rule, where a synapse would have had to read other neurons, and into a dendrite, where
  summing one's own afferents is what local computation permits. Eq. (E4a) shows the two forms are
  the same number, so no prediction moves. The cost is a fourth timescale, $\tau_r\ll\tau_\varepsilon$
  with $\tau_r\lesssim\theta_u^{-2}$ (Eqs. E5–E6): a third lag in the loop can oscillate where two
  cannot, and the stronger the learned gain, the faster the relay must be. State that as a
  commitment with empirical content, not as bookkeeping.
## 3.5 Two choices the scale forces (about 140 words)
 
Neither of the following is chosen. Both are consequences of the lexicon's threshold structure.
 
- **$m=2$, because the scale has two ends.** With $t$ distinct cut points the scale divides into
  $t+1$ intervals, so the entries span at most $t$ dimensions modulo the constant (Eq. C2). Here
  $t=2$, one threshold per endpoint, and $m=2$ is exactly right rather than merely sufficient: the
  only direction it misses is the constant, which the read-out misses too. The parity form:
  $\chi_{\textit{all}}-\chi_{\textit{some}}$ is even and $\chi_{\textit{no}}-\chi_{\textit{all}}$ is
  odd, so any single basis function of definite parity annihilates one of them, and $m\ge2$ is
  forced exactly when an inventory contains two pairs whose differences have opposite parity —
  **which, with symmetric thresholds, requires three utterances at one level**. §5.1 turns that
  clause into a design.
- **The two directions do different work.** The odd column is a monotone ramp that slides
  log-density from one end of the scale to the other — **tilt**. The even column raises both tails
  and lowers the centre — **width**, and therefore the axis along which mass moves between the
  centre and the extremes. Every result in §4.4 and §5.2 turns on which of the two an entry loads.
---
 
# 4. Evaluation (about 1,020 words)
 
## 4.1 What is compared (about 140 words)
 
Three beliefs, all internal to the model:
 
- $q_{\mathrm{lit}}$, the **untempered literal listener**, $\varphi_S=\ell_0-\varphi_L$: the prior
  restricted by the entry and nothing else. At this first mention, one sentence saying that what
  "literal" denotes here is distinct from what it denotes in RSA and the Gricean literature, and no
  further explanation (DEC5 of `procedure_records/d9_delta_readout.md`). Writer's note, not for the
  paper: the sentence does not contradict §3.2, whose identification with RSA's $L_0$ holds only as
  $\Lambda\to\infty$, a limit and not a setting, so the sentence is true of every configuration
  evaluated. $q_{\mathrm{lit}}$ is a fixed point of this network rather than an external
  construction, being what Eq. (15) returns as $\sigma_S\to\infty$, **and it is one because
  $\ell_0$ enters at $g_L$**: under the placement §3.2 sets aside, no setting of the variances
  returns it (§3.2, reason 3; `decisions.md` A3). Say both; the first removes the obvious objection
  that the baseline was built to be beaten, and the clause names what that answer rests on.
- The **tempered control**, $(\ell_0-\varphi_L)/2$, at $\theta_u=0$: the literal listener tempered
  by one half, the halving surviving into the belief because the read-out is exponential. It is a
  third quantity and not the baseline, and it holds the temperature fixed so that the utility level's
  own contribution can be read off. It is also where learning starts: Eq. (20) runs from
  $\theta_u(0)=0$.
- $q_H$, the settled belief.
State once, plainly, that RSA and wRSA are **analytic baselines and are not implemented**, so no
quantitative comparison is offered or implied.
 
## 4.2 The criterion, and how to read the statistics (about 170 words)
 
- Scalar strengthening is taken to be the conjunction of two conditions on the all-region mass under
  *some*: $q_H<q_{\mathrm{lit}}$, the network lowering the mass the entry and prior already assign;
  and $q_H<\tfrac12$, the strengthened reading being the majority outcome rather than merely the
  suppressed alternative. Writing $\Delta_{\textit{some}}$ for the shift (Eq. 37), the first is
  $\Delta_{\textit{some}}<0$.
- Neither is sufficient alone: the second can hold under literal conditioning by itself, since the
  non-all states stand together against the single all state; the first can hold while *all* remains
  the most probable single outcome. Reading implicature strength off the literal–pragmatic gap
  follows the probabilistic accounts (Frank & Goodman, 2012; Goodman & Stuhlmüller, 2013;
  Goodman & Frank, 2016). The criterion is a stipulation about how such an effect would have to show
  up *in this model*, and every verdict is relative to it.
- **A guard the reader needs before the first table.** These statistics are $q$-masses taken after
  the read-out's exponential, so they are nonlinear in $\varphi_S$ and do not inherit invariances
  the $\varphi_S$ contrasts have. Measured instance: $\mu_u$ and $\ell_0$ move no $\varphi_S$
  contrast at fixed $\theta_u$ — bit-identical to $3.6\times10^{-15}$ across a sixty-setting sweep —
  while $\Delta_{\textit{some}}$ varies by more than a fifth of its own size across six $\mu_u$
  settings. Any claim about a contrast between utterances must be checked against $\varphi_S$
  directly.
## 4.3 The specification holds (about 70 words)
 
Brief, and reported as a table rather than argued. The closed forms are exact to
$6.0\times10^{-11}$ against the integrated dynamics; the fixed-point identities of Eq. (17) hold;
the Hessian is negative definite across $\theta_u$; the relaxation rate is independent of
$\varphi_L$; the analytic messages agree with finite differences. Grid refinement is tested on the
**tail** of the sequence rather than on two coarse grids, because the rate is set by the entry being
a step: $1.6\times10^{-3}$ under the hard mask against $1.8\times10^{-6}$ under a smooth one, with
the smooth mask serving as the control that identifies which of the two is model and which is
quadrature. Code Cell E3 checks that the relay reproduces every one of these numbers.
 
## 4.4 The five priors (about 285 words)
 
**This is the section the argument turns on.** It reports Text cell 4b's rows: all five priors at
$\Lambda=512$, each at its own learned $\theta_u^\ast$, with $\Lambda=8$ entering as a one-line
contrast (R20, P-10).
 
| prior | $\theta_u^\ast$ | $P_0$(all-region) | $q_{\mathrm{lit}}$ | $q_H$ | $\Delta_{\textit{some}}$ | tempering | utility | first | second |
|---|---|---|---|---|---|---|---|---|---|
| Gaussian | $+1580.81$ | 0.0016 | 0.0016 | 0.0088 | $+0.0071$ | $+0.0175$ | $-0.0104$ | not met | met |
| flat | $+1521.48$ | 0.0479 | 0.0504 | 0.0357 | $-0.0146$ | $+0.0857$ | $-0.1003$ | met | met |
| $\mathrm{Beta}(1,3)$ | $+1589.49$ | 0.0001 | 0.0001 | 0.0091 | $+0.0089$ | $+0.0065$ | $+0.0024$ | not met | met |
| $\mathrm{Beta}(3,1)$ | $+1499.37$ | 0.1367 | 0.1368 | 0.0413 | $-0.0955$ | $+0.0989$ | $-0.1943$ | met | met |
| delta-like | $+1407.77$ | 0.9568 | 0.9568 | 0.4351 | $-0.5217$ | $-0.0586$ | $-0.4631$ | met | met |
 
- **Why $\Lambda=512$, in one sentence.** At Part D's $\Lambda=8$ the diffuse priors override the
  entries for *no* and *all* (largest leak $0.63$ under the Gaussian prior, $0.91$ under both skewed
  priors), so those rows measure the override as well as the criterion; at $\Lambda=512$ every
  entry holds under every prior (largest leak $1.1\times10^{-74}$). Read *some* only: under *no*
  and *all* the literal listener already holds none and all of the all-region, so their zero shifts
  are saturation.
- **The conjunction holds under three of the five**, the flat, $\mathrm{Beta}(3,1)$ and delta-like
  priors, and the second condition under all five, so no prior meets the first condition alone.
  State it as an observation before interpreting it. Among these five rows the two conditions are
  nested, the first the harder; on the plane they are not (§4.5: the first holds in 74 cells, the
  second in 59). The three are the priors with the most prior mass on the all-region, and across
  them the shift deepens with that mass.
- **The contrast with $\Lambda=8$, and where §3.2's commitment shows.** At $\Lambda=8$ the four
  diffuse priors meet the second condition only, with shifts $+0.0008$, $+0.0295$, $+0.0004$ and
  $+0.0421$. Raising $\Lambda$ to 512 carries the flat and $\mathrm{Beta}(3,1)$ priors across zero
  and moves the Gaussian and $\mathrm{Beta}(1,3)$ priors further from it. The tempering barely moves
  with $\Lambda$; what moves is the utility level's own contribution, whose drive $c_y$ is the one
  quantity the placement of $\ell_0$ changes (§3.2, Eq. D7). The prior also matters less at this
  $\Lambda$: the $\varphi_S$ contrasts between utterances agree across the five priors to $0.0001$
  at each prior's own $\theta_u^\ast$, against $0.0575$ across Part D's four at $\Lambda=8$.
- **Decompose the shift before interpreting it.** $\Delta_y$ contains the tempering and the utility
  level, and they come apart at the tempered control. Where the conjunction holds, the utility
  level's contribution outweighs the tempering. It is negative under four priors and positive under
  $\mathrm{Beta}(1,3)$. Whether the first condition is met therefore depends on the prior the entry
  is read against.
- **The anti-exhaustive direction, and the Cremers parallel (R7, P-9; about 40 words).** Give both
  counts in one sentence. The shift is positive under all four priors that have a row at
  $\Lambda=8$ (the delta-like prior has none there, since it needs the stronger lexicon), and under
  two of five at $\Lambda=512$, the Gaussian and $\mathrm{Beta}(1,3)$. Raising $\Lambda$ removes the
  direction under the flat and $\mathrm{Beta}(3,1)$ priors, the two of those four with the most
  prior mass on the all-region, and enlarges it under the other two ($+0.0008\to+0.0071$,
  $+0.0004\to+0.0089$). Name it: the settled belief holds *more* all-region mass than the literal
  listener, the direction Cremers, Wilcox and Spector (2023) identify as a liability of baseline
  RSA. Guards:
  - The parallel is in direction, not in conditions, and the mechanisms differ: the $\tfrac12$
    temperature of a finite $\sigma_S$ here, the prior acting through the speaker model there. Say
    "parallel", not "shared liability".
  - Under $q$ the tempering carries the direction. At $\Lambda=8$ the utility level's contribution
    runs against it under all four priors; at $\Lambda=512$ it runs against it under the Gaussian
    prior and **with** it under $\mathrm{Beta}(1,3)$, $+0.0024$ of the $+0.0089$.
  - §5.1 does not use the parallel as evidence for the alternatives level (R2).
- **Where the first condition is met, the mechanism is amplification, not competition.** Differencing
  Eq. (16) against the tempered control gives
  $\varphi_S^\ast(\theta_u)-\varphi_S^\ast(0)=\tfrac{\theta_u}{2}B\varphi_u^\ast$ (Eq. 23, exact to
  $1.8\times10^{-15}$ at the Gaussian prior's $\theta_u^\ast$), and growing $|\theta_u|$ drives
  $\varphi_S^\ast\to\tfrac12(I+BB^{\mathsf T}W)(\ell_0-\varphi_L)$ (Eq. 24) — the control field with
  its component in $\operatorname{span}B$ **doubled**. Under the delta-like prior the two entries'
  couplings share their tilt coordinate and differ only in width, and doubling a negative width
  coordinate lowers both tails, the all-region among them. Eq. (24)'s limit gives that row's
  $-0.5217$, and so does its own $\theta_u^\ast$.
- **One sentence pointing to §4.6:** the conjunction is shown in the integrated dynamics, not only
  in closed form, for all three rows that meet it (Code Cell 2b).
## 4.5 The plane, and where both conditions hold (about 255 words)
 
- **The conjunction is not confined to Part D's rows.** Sweeping lexical strength against prior
  concentration on the limit family $\mathrm{Beta}(\alpha,1)$, both conditions hold together in
  **33 of 121 cells**, in a band running from $(\alpha,\Lambda)=(1,512)$ to $(128,2048)$. Text
  cell 4b's flat row is the band's corner cell $(1,512)$, and its delta-like row is the cell
  $(64,512)$, at the band's lower edge in $\Lambda$. The Gaussian and $\mathrm{Beta}(1,3)$ priors
  are not members of the family, and $\mathrm{Beta}(3,1)$ falls between $\alpha=2$ and $\alpha=4$.
- **The floors, and where the trade-off claim now lives (P-8).** Each condition holds above a floor
  in $\Lambda$, and the two floors run in opposite directions in $\alpha$. The first condition's
  floor **falls** as the prior sharpens, from $\Lambda\ge512$ at $\alpha=1$ to $\Lambda\ge16$ at
  $\alpha=64$ and $\Lambda\ge2$ from $\alpha=128$ to $512$ (the $\alpha=1024$ row reads 2048 and is
  saturated): the more prior mass sits on the all-region, the less lexical strength the utility
  level needs to take some away. The second condition's floor **rises**, from $\Lambda\ge2$ up to
  $\alpha=8$ to $64$, $256$, $512$ and $1024$ at $\alpha=16$, $32$, $64$ and $128$, and past
  $\alpha=256$ it is unreachable on this grid. The floors cross between $\alpha=8$ and $\alpha=16$.
  **This is the claim that prior concentration buys the first condition and spends the second, and
  it is sourced here, on the floors.** It is a property of the plane and not of Part D's rows: at
  $\Lambda=512$ both floors lie at or below 512 from $\alpha=1$ to $64$, which is why those rows do
  not show the tension (§4.4). "Under every prior tested" is not written anywhere; §5.1 and §6
  point here.
- **The V, under both read-outs (R13, R14).** The least $\Lambda$ at which both conditions hold
  runs $512$, $256$, $128$, $64$, $64$, $256$, $512$, $1024$ over $\alpha=1$ to $128$, a V with its
  minimum at $\alpha=8$ and $16$. Under the delta read-out's two criteria (§3.6; R12) the right arm
  is shared from $\alpha=32$, at $\Lambda=8\alpha$; the left arm exists only under $q$, since the
  mode shift criterion is never met at $\alpha\le8$; and the two conjunctions part in 20 cells, all
  of them met under $q$ alone. Report the V as a result, and derive no evidence for a missing level
  from it.
- **The override law, the exchange rate of §3.2's contest.** $\Lambda_{\mathrm{crit}}\approx\alpha\log2n$
  (Eq. 41), linear in prior concentration with a slope fixed by the predicate's granularity alone:
  the rate at which lexical strength must grow to hold the entry against a sharper $\ell_0$.
  Measured slopes match it to within $4.1\%$ at the tempered control (ratios $1.041$, $1.014$,
  $0.998$ at $\alpha=1024$). With $\theta_u^\ast$ re-learned
  they are $1.9890$, $2.9334$ and $4.3102$, $36$–$45\%$ above it: the utility level reinforces the
  prior against the entry. That nothing in RSA plays this role is background §1.3's point (U11), not
  this section's.
- **Two honesty notes.** The band is reached by raising $\Lambda$, a parameter of the lexicon rather
  than an elicited quantity — but Eq. (41) means its required value is predicted rather than
  arbitrary. And what fails first as $\alpha$ grows is the model's ability to tell the utterances
  apart, the spread $D$ falling $0.0057\to0.0012\to0.0003$ over $\alpha=64,256,1024$ at
  $\Lambda=8$.
- **What the conjunction needs, measured apart from what $\theta_u^\ast$ costs.** Across the 33
  cells the least $|\theta_u|$ meeting the conjunction runs from $0.100$ to $4.250$, with
  $\lambda_{\max}(H)$ between $2.0$ and $20.1$ there, so every cell is integrable at the $\theta_u$
  the conjunction needs; at their own $\theta_u^\ast$ the same cells have $\lambda_{\max}(H)$
  between $3.5\times10^{4}$ and $3.6\times10^{7}$. §4.6 takes it up.
---
 
# 5. Discussion (about 1,180 words)
 
## 5.1 What an alternatives level would have to supply (about 350 words)
 
**Frame the section as a specification, not a concession.** The claim is not that this architecture
excludes within-trial competition. It is that adding a level is a construction with four stated
obligations, that the present results discharge part of each, and that the architecture's own
results point at which design is the tractable one.
 
- **What the criterion adds to the case, and where it is sourced (P-8).** The case for the level is
  the complexity it saves (R2; the design below). The criterion adds one thing the level would
  change, and it is stated on §4.5's floors, not on Part D's rows. As the prior sharpens, the first
  condition's floor in $\Lambda$ falls and the second's rises, so on the plane prior concentration
  buys the first condition and spends the second. A drain keyed to the *alternative* would not
  scale with prior mass on the all-region, and so would lower the first floor without raising the
  second. Say that this is argued from the floors and not measured, since no such drain is built.
  Do not write "under every prior tested": at $\Lambda=512$ both floors lie at or below it from
  $\alpha=1$ to $64$, and Part D's rows show no tension (§4.4). The earlier bullet reading the
  pattern as pointing at an absent level is withdrawn (R14), and the anti-exhaustive parallel now
  lives in §4.4 as a parallel, not as corroboration (R7).
**The design: resolution as a negative search.** State the position, because it is what makes the
remaining obligations answerable rather than open.
 
- Scalar resolution is treated as a **search over the scale**, and the architecture already
  represents each entry by what it *rules out* rather than by what it admits (Eq. 5). Appendix D
  justified that convention locally, from a property of the representation map; the search framing
  says why the property is the right one to want. **The system first determines what the state is
  not, and infers what it is on the remainder.** Semantic content does the excluding; pragmatic
  strengthening excludes again on the domain the first step leaves.
- **What is searched, and what branches.** Keep the two apart, since conflating them makes the
  complexity claim look weaker than it is. The space searched is the **scale**: a predicate
  resolving $n$ atoms (Eq. A5) presents $n+1$ distinguishable states, $n=10$ by default and capped
  at $202$ by the grid. The **inventory at a level is the branching factor**, not the domain. The
  thesis that no inventory exceeds two members is therefore the thesis that resolution branches
  binarily, and the comparison it invites is $O(n)$ against $O(\log n)$ in the granularity — which
  at $n=10$, let alone $202$, is not a distinction without a difference.
- **The inventory at any one level is binary.** In place of a flat $\{$*no*, *some*, *all*$\}$, the
  same three-way partition is reached by a cascade of two complementary oppositions — which is the
  design reading of the commitment Appendix D §2 states, that the inventory holds at least
  $\{\chi,\ker\chi\}$ for any entry $\chi$: at the
  utterance level $\langle E_{\textit{some}},\ \ker E_{\textit{some}}\rangle$, and then, on the
  domain that leaves, $\langle E_{\textit{all}},\ \ker E_{\textit{all}}\rangle$ with the kernel
  taken relative to that domain. Appendix D's Eq. (D2) already supplies the kernel relation.
- **Where the present inventory does and does not exhibit the saving.** State this rather than let
  a reader find it. Each of the cascade's two cuts peels off a *single endpoint cell* — $s=0$, then
  $s=1$ — leaving the interior $\{1/n,\dots,(n{-}1)/n\}$ undifferentiated: two levels, three
  regions, binary in branching but linear in depth. That is the right behaviour for these
  quantifiers, since *some but not all* is genuinely unspecific and the scale offers nothing
  further to resolve; but it means ⟨*no*, *some*, *all*⟩ does not itself demonstrate the
  logarithmic claim. **The inventory that would is one with an interior cut, and *most* is the
  clean case:** true where $s>\tfrac12$, hence a cut at $\zeta=0$, the exact midpoint of the
  log-odds coordinate and the first step of a balanced search. Present ⟨*some*, *most*, *all*⟩ as
  the prediction rather than the three-word scale as the demonstration.
- **The dimension and locality payoff, which is an argument and not a measurement.** Appendix C
  Eq. (C2) fixes the dimension by the threshold count, and Appendix C §5 shows $m\ge2$ is forced
  exactly when one inventory carries two pairs of opposite parity — which with symmetric thresholds
  takes three utterances at one level. A cascade puts one cut per level, so **each level is a
  complementary pair and $m=1$ suffices at each**. Eq. (C1) already proves that a complementary pair
  costs no dimension, its $\kappa_{y'}=-\kappa_y$ resting on $\langle\mathbf 1,b_j\rangle=0$.
  Complementary *within a domain* $D$ means $\chi_{y'}=\chi_D-\chi_y$, so the identical derivation
  returns $\kappa_{y'}=-\kappa_y$ once the level's basis is taken orthogonal to $\chi_D$ in place of
  $\mathbf 1$ — a substitution into a proved result rather than a new computation, and one that
  therefore holds at **any cascade depth** whose levels are complementary pairs, ⟨*some*, *most*,
  *all*⟩ included. The consequence is exact: $m=1$ is where Appendix B's locality defence is clean,
  so a binary cascade is local at every level **without the relay**, and Appendix C's degeneracy
  result does not bite because *some* and *all* never occupy one level.
- **And binarity removes the obstacle at the generative map.** Appendix A observes that a
  normalization across word-form units would not be local, and an RSA speaker term is exactly such
  a normalization — a softmax over the alternative set, which is also non-affine and so would cost
  §8.1's concavity. **With two alternatives neither problem arises.** Represent the opposition by
  its log-odds, which is the coordinate the model already lives in (Eq. 1), and normalization is not
  an operation at all — it is absorbed into the representation, and complement becomes an
  order-reversing affine involution, $x\mapsto c-x$, the form $g_L$ already has (Eq. 9). Affine
  preserves §8.6's first condition, so the global convergence proof extends by Eq. (22)'s own
  argument. **This is the good branch of the trade**: an affine alternatives level keeps the proof,
  and binarity is what lets it perform the comparison anyway.
**What this dissertation does not derive, stated plainly.** The design above places the
order-reversing involution at a new alternatives-level map $g_a$ rather than at $g_L$ — **lowercase
because the level's state $\varphi_a$ has the same type as $\chi$**, an indicator selecting a
subdomain of the scale rather than a graded field, so that $\varphi_a=\chi_D$ for the domain $D$ a
level passes down — and **the algebra of that migration is not worked out here.** Four things
remain, and naming them is the point of saying so:
 
  1. **The reference point of $g_a$'s involution on the restricted domain** — the analogue of
     $\ell_0$ in Eq. (9), not derived. The type constraint narrows it: an indicator-valued
     $\varphi_a$ takes an indicator reference point rather than a log-density, and $\chi_D$ is the
     natural candidate, being the same object obligation 3 turns on. Whether that is correct is the
     algebra.
  2. **What $g_L$ becomes** once it no longer carries the involution, and the sign of its Jacobian,
     since $g_L'=-I$ is currently what makes $\varepsilon_L$ reach $\varphi_S$ inhibitorily.
  3. **Whether Appendix D §3's argument for the exclusion convention re-anchors at $g_a$.** That
     argument turns on the involution having a fixed point the model settles on, $\ell_0/2$; on a
     restricted domain the relevant constant is the domain's indicator rather than $\mathbf 1$, so
     the argument needs re-running there rather than transferring.
  4. **The new level's error unit and variance**, and confirmation that the composed maps stay
     affine in the state so §8.6's first condition holds and Eq. (22) extends as claimed.
  Until these are settled, the design of this section is a **specification with a proposed
  solution, not a result**. Everything reported in §4 stands independently of it: no number in this
  dissertation depends on the alternatives level existing.
 
- **Close with the position on the current gain.** At learning, $\theta_u^\ast$ depends on
  $\sum_y c_y$ and so on the inventory, substantially: exposure to *no* alone gives $-11.28$, to
  *some* alone $-44.18$, to *all* alone $-65.70$, to all three $-28.44$. But this is a cross-trial
  average, one shared weight, consulted identically whatever is heard, so any implicature reaching
  the belief by this route is **conventionalized rather than computed** — and § E.2 confirms the
  relay does not change this. Levinson's (2000) default GCIs are the nearest neighbour and still
  differ: a default is keyed to an alternatives set at the utterance and is defeasible within the
  trial. Ronai and Xiang (2024) are the relevant empirical constraint: alternative *accessibility*
  behaves like an exposure-indexed quantity, but contextual *relevance* governs inference rates, and
  relevance is a within-trial quantity only the level specified above could carry.
- **Then the standing qualification**, in its own sentence: three facts settle the *absence* of an
  alternatives computation in the present model — $\varphi_L$ is a function of the observed
  utterance alone, $g_S$ reaches the belief only through $\varphi_u$, and no term in Eq. (13)
  involves any unobserved utterance — and they settle nothing about human processing.
## 5.2 Scale structure: a second prediction (about 400 words)
 
- **The setup.** §3.3 fixes $\theta_L$ by the predicate's own resolution: at a scale endpoint the
  threshold is supplied by the scale itself (Eq. A5), while a predicate with no endpoint to anchor
  to must take its threshold from elsewhere (Eq. A6), and Appendix A leaves open what fixes it. In
  the terms of the gradable-adjective literature, maximum-standard absolute adjectives have closed
  scales and conventional endpoint standards, while relative adjectives have open scales and
  context-dependent thresholds (Kennedy, 2007; Xiang, Kennedy, Xu & Leffel, 2022).
- **The mechanism, which rests on parity before it rests on measurement.** By §3.5 the even/width
  column is the axis along which mass moves between centre and extremes. **An entry whose threshold
  sits at the midpoint of the log-odds scale has no even component at all**: $\chi=\mathbb
  1[\zeta<0]$ is the constant plus a purely odd function, and the basis is orthogonal to the
  constant by construction (App. C §2), so its width loading is exactly zero. Moving the cut
  off-centre is what gives it one. That much is a parity argument in the family of Appendix C's,
  not a fitted trend. The measured ratios of width loading to tilt loading then quantify the
  growth: $0.219$ at $s=0.73$, $0.633$ at $s=0.95$, $1.07$ at $s=0.99$. **A mid-scale threshold is
  invisible to the extreme-favouring axis; an endpoint-anchored one loads it heavily.**
  *(Numerical note for the notebook, not the prose: on the grid the midpoint ratio reads $0.013$
  rather than $0$, and the sign flips with the strict-versus-inclusive inequality — the cut sits on
  a node. Half-weighting that node returns $0$ to machine precision. Report the parity result, not
  the artifact.)*
- **The prediction, in two parts.** Under a flat prior, the utility level's own contribution to
  posterior degree rises monotonically as the threshold approaches the endpoint, from $+0.034$ at
  $s=0.50$ to $+0.070$ at $s=0.98$ (and from $+0.047$ to $+0.099$ at $\theta_u^\ast$). And the
  contribution decays as prior knowledge sharpens, reversing sign for mid-scale thresholds while
  remaining positive for endpoint-anchored ones: under a Gaussian prior of precision 2 it is
  $-0.005$ at $s=0.50$ against $+0.020$ at $s=0.98$. So the model predicts **endpoint-oriented
  interpretation for closed-scale predicates, proportional prior-tracking for open-scale ones, and
  an interaction in which the endpoint orientation is sharpest where prior knowledge is weakest.**
- **The empirical fit.** This is the reported profile. Maximum-standard absolute adjectives elicit
  categorical responses concentrated near the scalar maximum, relative adjectives a roughly constant
  increase across scale positions, and the difference is most dramatic in the impoverished-prior
  (geometric shapes) condition rather than the rich-prior (familiar artifacts) one
  (Leffel, Xiang & Kennedy, 2017; Xiang et al., 2022). Xiang et al. further find that Bayesian
  pragmatics models what is *communicated* well ($R^2=0.78$–$0.82$) but threshold judgments poorly
  ($R^2=0.36$–$0.63$), especially for absolute adjectives, and conclude that Bayesian reasoning must
  be combined with the semantic conventions governing thresholds. **That is the architecture this
  model already has**: $\theta_L$ is a semantic convention, fixed by the predicate rather than
  inferred, sitting inside a free-energy inference.
- **Calibrate the claim.** The model was not fitted to these data and no fit is offered; what is
  offered is that a qualitative interaction the model derives from scale structure alone matches one
  the literature reports. Say that, and no more.
## 5.5 Limits (about 80 words, was §5.3)
 
- Convergence status: **global** for $(\varphi_S,\varphi_u)$; for $\theta_u$, convergence of the
  reduced objective plus convergence to a stationary point guaranteed only **locally**, since that
  objective is not concave. The same division as in Bogacz.
- **Halting by tolerance is offered as a direction, not a commitment, and the reason is a
  violation we have not settled.** The flow of Eq. (20) stops when its own update falls below a
  tolerance; the value is ad hoc, so results are reported at $\theta_u^\ast$, the asymptote, which
  carries none, and a realizable $\theta_u$ is quoted with the tolerance it halted at. What keeps
  this a direction rather than a claim is that the **fast** loop's tolerance is keyed to
  $\lambda_{\max}(H)$, a global quantity — a locality problem of the same kind as the timescale
  bound's, and not licensed by it (D12). The **slow** rule carries no such debt. Two implications
  are owned rather than hedged: a plausible tolerance halts far short of $\theta_u^\ast$, and a
  slow start halts at once at the tempered control (§5.3).
- The model is linear-Gaussian while $\varphi_L$ is clamped, so the recurrent dynamics are an
  implementation claim rather than a computational necessity.
- The relay secures locality at the cost of a fourth timescale scaling as $\theta_u^{-2}$ (Eq. E6).
- $m=2$ is necessary at a flat inventory; **sufficiency is open**.
- Multidimensional semantics with sharp lexical boundaries is a declared non-compatibility.
- Not learned: $\Lambda$, $\theta_L$, $B$, $\mu_u$, the inventory.
- **Two stipulations of this phase, labelled as such and not built otherwise.** Results are
  reported at **uniform exposure** — $p(y)$ is not a variable of the implementation but is implicit
  in the batched sum, and no frequency-bearing version is built. And the inventory is taken to hold
  at least $\{\chi,\ker\chi\}$ for any entry; membership follows from exposure somewhere, not
  from exposure in a given experiment.
- Tier B facts recorded here, position reserved.
## 5.6 Predictions (about 60 words, was §5.4)
 
- **Exposure frequency should shift strengthening.** $\theta_u^\ast$ is set by
  $3\,\mathbb E_{p(y)}[c_y]$, so non-uniform exposure to the inventory moves it. **This is a
  prediction about departures from a stipulated uniform**, which is what makes it a prediction at
  all: uniform $p(y)$ is this phase's stipulation (Appendix B), not a result, and the model is not
  run at any other exposure. No analogue in RSA.
- **Granularity should shift the override threshold**, $\Lambda_{\mathrm{crit}}\approx\alpha\log2n$.
- **Scales providing interior cuts should partition the log-odds coordinate near-uniformly**, with
  *most* at $\zeta=0$ the confirming instance; ⟨*some*, *most*, *all*⟩ is where the search thesis of
  §5.1 is testable, and §5.1's dimension argument already covers that cascade, its three levels
  being complementary pairs on their own domains.
- **The scale-structure interaction of §5.2**, tested on degree estimates rather than truth-value
  judgments.
---
 
# 6. Conclusion (about 165 words)
 
1. A field-valued world state on a dense scale, with a soft lexical entry competing additively
   against the world prior in the same log-density — a placement of the prior the architecture
   commits to, not one its construction forces (§3.2) — admits a closed-form stationary point and a
   recurrent network that provably reaches it, with plasticity local at every $m$.
2. That network moves belief mass away from the *all* reading without representing any alternative,
   by amplifying the observed entry's own projection under a gain fixed by exposure. The effect
   therefore does not by itself diagnose a within-trial alternatives computation.
3. The network also meets both conditions the criterion imposes: under three of five priors at a
   lexical strength that holds every entry, across a band of the plane, and within two updates of
   learning. What a level representing competition among alternatives would change is what the
   network pays for that. On the plane the first condition's floor falls as the prior sharpens and
   the second's rises (§4.5), and a drain keyed to the alternative would not raise the second; and
   learning has no end short of a maximizer the slow flow never reaches. This dissertation specifies that level and
   proposes a design for it — resolution as a negative search branching binarily at each level,
   which keeps the dimension at one, the plasticity local, and the generative map affine enough to
   inherit the convergence proof — but does not derive its algebra, and says so in §5.1.
4. Independently, the same threshold semantics predicts an endpoint-orientation asymmetry between
   closed- and open-scale predicates, sharpest where prior knowledge is weakest.
---
 
## Sources for §5.2
 
- Xiang, M., Kennedy, C., Xu, W., & Leffel, T. (2022). Pragmatic reasoning and semantic convention:
  A case study on gradable adjectives. *Semantics and Pragmatics, 15*(9).
  https://doi.org/10.3765/sp.15.9
- Leffel, T., Xiang, M., & Kennedy, C. (2017). *Interpreting gradable adjectives in context: Domain
  distribution vs. scalar representation* [Manuscript]. **Check whether the published 2022 article
  reports the shapes/artifacts contrast in the same terms before citing the manuscript.**
- Ronai, E., & Xiang, M. (2024). What could have been said? Alternatives and variability in
  pragmatic inferences. *Journal of Memory and Language, 136*, 104507.
- Kennedy, C. (2007). Vagueness and grammar: The semantics of relative and absolute gradable
  adjectives. *Linguistics and Philosophy, 30*, 1–45.
Citations redeployed into §5.1: Rooth (1985, 1992) and Kratzer & Shimoyama (2002) make the
alternative set depend on context rather than on the uttered expression; Katzir (2007) and
Fox & Spector (2018) treat competition as resolved by, rather than generative of, what is produced.
Both constrain where such a level would sit, and Katzir and Fox & Spector are also the right
citations for a structurally bounded alternative set.
 
## Open items
 
1. **The §5.2 magnitudes are not yet in the notebook.** The *mechanism* no longer depends on them:
   the midpoint's zero width loading is a parity result (App. C §2), and §5.2 now leads with it. But
   the off-centre loading ratios, the utility contributions to posterior degree, and the sign
   reversal under a sharp prior are genuine measurements, computed from the closed forms
   (Eqs. 15–16) and validated by reproducing every published quantity — the Appendix B $c_y$ table,
   the Eq. (30) offset, the basis shapes, and all five rows of the Part D table with its
   tempering/utility decomposition. A probe cell has been drafted; run it before the prose quotes
   them. If time runs out, §5.2 survives on the parity argument plus a qualitative statement of the
   interaction.
2. **The background is being rewritten** under the three-question frame (Q1 locality; Q2 not one
   pass; Q3 algorithmic-level peculiarities). The plan is `claude/background_revision_plan.md`
   (Revision 4) and the rewritten outline is `background_sections_outline.md`. Two consequences for
   this document, both already applied above: §5.1's sub-bullet on alternative-sensitive versus
   world-sensitive utility is deleted rather than redirected, since the model has one utility level;
   and the background now introduces Levinson (2000), Rooth, Kratzer & Shimoyama, Katzir,
   Fox & Spector, Kennedy (2007) and Xiang et al. (2022) before §5.1 and §5.2 use them.
3. ~~The $g_a$ algebra.~~ **Resolved by decision: not derived, and admitted as such in §5.1** under
   "What this dissertation does not derive", with the four remaining obligations named. Do not
   attempt the derivation. Note that the admission is written as a scope statement; any account of
   *why* it was out of scope belongs in an introductory scope note or the acknowledgements, not in
   §5.1, where it would add nothing about the model. **Notation settled 2026-09-11: the subscript is
   lowercase, because $\varphi_a$ has the same type as $\chi$ — an indicator selecting a subdomain,
   not a graded field.**
4. ~~The *most* case, and the cascade check.~~ **Resolved: both are arguments, not measurements.**
   §5.1's $m=1$ result now runs through Eq. (C1) with $\chi_D$ substituted for $\mathbf 1$, which is
   a proved result applied to a restricted domain and therefore holds at any cascade depth whose
   levels are complementary pairs. ⟨*some*, *most*, *all*⟩ is such a cascade — split off $s=0$,
   split the remainder at $s=\tfrac12$, split the upper part at $s=1$ — so it needs no separate
   check, and the $8\times10^{-16}$ figure is no longer cited.