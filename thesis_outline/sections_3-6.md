Sections 3 6 outline · MD
# Outline for the proposal, evaluation, and discussion sections
 
Scope: §§3–6, approximately **5,600 words**, which is what this file's own word table sums to and
the figure to trust (`revisions.md` §3 is the historical plan; the raises are listed above the table). Written against
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
 
**Constructive claim.** Say what the network carries before saying how often, because a count is
only worth something once the baseline is out of it. **Where the prior leaves the all-region in the
majority, the network takes it out; where the prior puts the settled field's peak inside the cell
of *all*, the network carries it outside.** Both are §4.2's position criterion, read through the
two read-outs of §3.6, and Part D's delta-like prior is the case in a single row:
$q_{\mathrm{lit}}=0.9568$ against $q_H=0.4351$, and a peak at $s=0.9852$ inside the cell against
$0.9468$ outside it (§4.4). Across the plane, $q_{\mathrm{lit}}$ holds at least half the all-region
in 77 of the 121 cells and the settled belief holds less than half in **15** of those;
$\ell_0$ peaks inside the cell in 66 cells and $\varphi_S^\ast$ peaks outside it in **9** of those,
the 9 a subset of the 15 (§4.5). **In every one of those cells the shift criterion is met as well**,
which the cell counts rather than the prose asserts: where the network changes the position
verdict it meets both criteria, and it does so under either read-out. **The 15 and the 9 are
figures at the stipulated half-width**, and Appendix A's ladder counts them $32, 15, 0, 0, 0$ and
$22, 9, 0, 0, 0$ over $Z\in\{5,6,7,8,10\}$: a count conditioned on the baseline failing entails a
shift and so cannot outlast the shift criterion, which is empty by $Z=7$. §4.2's guard governs this
claim as it governs the counts below it, and §4.5 states it there in full.

The unconditioned counts belong in the claim too, and only with what they include. Both conditions
hold under three of the five priors at $\Lambda=512$, the three with the most prior mass on the
all-region, and the second under all five, so among those priors they are nested (§4.4); across the
plane both hold in 33 of 121 cells, in a band whose shape two opposed floors set, the first
condition's falling in $\Lambda$ as the prior sharpens and the second's rising (§4.5). Under the
delta read-out the same two counts are the delta-like prior alone and 13 cells, since **what
survives the change of read-out is the position criterion and what does not is the shift** (§3.6's
position). **Each of these is a count in which the baseline is doing part of the work**, which is
why they stand after the paragraph above and not in place of it.

The case for a level representing within-trial competition among alternatives therefore does not
rest on the criterion failing (R2). It rests on what such a
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

**How the two criteria are read.** §5.1 states the reading, as a conjecture and not a measurement:
**the position criterion is what this architecture supplies natively, and consistent shift is what
the absent level would supply** — with neither standing as the criterion of strengthening on its
own, which is why §4.2 takes the conjunction. It is argued from §4.5's opposed floors and §4.4's
rows, under the guard §4.2 sets on $n$ and $Z$, and nothing here measures a level that is not built.
**It is the second motivation and not the first.** The case for the level is the complexity it
saves (R2), which is derived from the construction and needs no datum; the conjecture is about what
*this* architecture cannot deliver, and whether strengthening must be a shift at all rests on a
baseline that is a construct in every account that has one (§5.1). Do not let the order slip.

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
| The two-condition criterion and its results | §4.2–§4.5 | The verdict. **Carried as the position criterion with the baseline's own cells left out** (§4.4's one row; §4.5's 15 and 9), with the unconditioned counts reported beside them |
| The cell of *all* has two stipulated ends, $n$ and $Z$ | §3.2, §4.2, §4.5, §5.5 | The guard every count in §§4.4–4.5 is relative to. **Printed at both ends since 2026-09-23** (Appendix A's two ladders; Code Cell 2's $K$-against-$Z$ check; F.10's control), so it is carried rather than reserved |
| Conventionalization of $\theta_u^\ast$ by exposure (App. B) | §3.4, §5.1 | The position the architecture commits to |
| The four construction obligations (Text cell 3; §8; App. B) | §5.1 | Turns the gap into a specification |
| Binary branching per level, and $m=1$ (App. C §§2, 5) | §5.1 | Makes the alternatives level tractable and local |
| Non-locality of normalization across word forms (App. A) | §5.1 | The obstacle binarity removes |
| The relay, Eqs. (E1)–(E6) | §3.4, §5.5 | Locality at $m>1$, and the cost it carries |
| $\theta_L$ as predicate granularity, Eq. (A5) | §3.3, §5.1–§5.2 | Sets the search's resolution; the closed/open prediction |
| $m$ = threshold count and the parity argument (App. C) | §3.5, §5.1–§5.2 | Fixes dimension; the mechanism behind §5.2 |
| Scale class against Xiang et al.: H1 and H2, match and mismatch (§5.2, App. F) | §5.2 | Second empirical anchor. **Reported; neither adopted nor rejected**, because the comparison runs at one resolution and under commitments a later phase may drop (O13). The open-scale half of H2 is stated and left untested (O14) |
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
  (§5.2's instinct sentence; `agent/decisions.md` O14). Position reserved on $\mu_u$, the one quantity
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

**This table is the authority.** `revisions.md` §3 is the historical plan it grew out of, and that
file's own closing note says so: its Total and its §5 subtotal have not been re-summed since 2026-09-22.
2,400 → 3,000 (R1) → 3,200 (S-6) →
**3,520** (P-3, then §5.5 raised 80 → 150 on 2026-09-22 for A19's halting bullet) → **3,610**
(§4.2 raised 170 → 260 on 2026-09-22 for S-8/T15's $n$ guard) → **3,760** (§5.2 raised 400 → 550 on
2026-09-22 at T10, under S-6's standing permission for this section) → **3,880** (§5.2 550 → 650 and
§6 165 → 185 the same day, for R27's reservation on H1) → **4,030** (§5.2 650 → 800 the same day,
for R28's mechanism and its one hedged causal statement) → **4,210** (§5.6 60 → 130 the same day:
it carries four predictions and R27 had added the H1 reservation to the fourth without raising it)
→ **4,270** (§3.4 230 → 290 the same day, at **BG13**: commitment 7 in its exact form, conditioning,
and $\theta_u(0)=0$ — three items of `revisions.md` §4 that had never been applied) → **5,060**
(2026-09-23, the two positions of §11 of `revisions.md`: §3.6 100 → 190, §4.2 480 → 525, §4.4 355 → 415,
§4.5 345 → 370, §5.1 390 → 460, §6 185 → 225) → **5,160** (the same day, §5.1 460 → 560 at PP10) → **5,290** (the same day, the constructive claim's rewrite at §12 of `revisions.md`: §4.4 415 → 470, §4.5 370 → 420, §6 225 → 250) → **5,600** (the same day, the half-width printed, §13's Z8: §3.2 270 → 295, §4.2 525 → 545, §4.3 70 → 105, §4.5 420 → 530, §5.2 800 → 860, §5.5 300 → 345, §6 250 → 265). The "was" column is the 2,400 allocation this outline was written to.

**The running chain above does not reconcile with the rows, and the rows are what to trust.** Before
this entry the chain read 4,270 while the rows summed to 4,730: four raises were applied to rows
without being appended here (§4.2, §4.4, §4.5 and §5.5), and which raise accounts for which part of
the 460 cannot be recovered from this file. **The subtotals and the Total are re-summed from the
rows and agree with them**; the chain is a record of raises with gaps in it. Treat it as history.

| Section | Was | Words | Function |
|---|---:|---:|---|
| **3. The proposed architecture** | 800 | **1,260** | |
| 3.1 What the model must do | 90 | 90 | Four design requirements |
| 3.2 A continuous world state and a soft lexicon | 160 | **295** | Eq. (1); $\varphi_L=\Lambda\chi_y$; defeasibility as the price; the Λ–ℓ₀ commitment and Λ → ∞ as RSA's L₀ (R18) |
| 3.3 The chain, and the semantics of its threshold | 200 | **255** | Eq. (7); $\theta_L$ from granularity; $\mu_u\ne0$; the projection parallel and its warning (R19) |
| 3.4 State units, error units, and what is local | 210 | **290** | Concavity, closed forms, the relay; commitment 7 **in its exact form**; conditioning; $\theta_u$ learned, starting at the tempered control (raised from 230 on 2026-09-22 at **BG13**, for the three items of `revisions.md` §4 that had never been applied) |
| 3.5 Two choices the scale forces | 140 | 140 | $m=2$ from threshold parity; the amplification axis |
| 3.6 Two read-outs (new) | — | **190** | `revisions.md` §5, item 1; **+90 on 2026-09-23 for the position that the delta read-out is the one the construction motivates, and the four things it does not license** (§11 of `revisions.md`, PP1) |
| **4. Evaluation** | 745 | **1,890** | |
| 4.1 What is compared | 100 | **140** | Three beliefs; RSA/wRSA as analytic baselines only; q_lit's status depends on A3 |
| 4.2 The criterion, and how to read the statistics | 170 | **545** | The conjunction; the softmax-nonlinearity guard; **the all-cell width guard** — the $n$ end (raised from 170 on 2026-09-22, S-8/T15) and the $Z$ end (raised from 260 on 2026-09-23, E17); **+45 the same day for which read-out the criterion is written in** (PP2) |
| 4.3 The specification holds | 90 | **105** | Closed forms, Hessian, grid (trimmed to fund §4.5, R14); **+35 on 2026-09-23 for the fifteenth check, $Z$ against $K$** (Z8) |
| 4.4 The five priors | 220 | **470** | The Λ = 512 table, the Λ = 8 contrast, the Cremers parallel, the mechanism; **+70 on 2026-09-22 for item 1's delta read-out results**, unblocked by §3.6; **+60 on 2026-09-23 for the five priors' delta criteria at Λ = 512, and for which rows the baseline already meets** (PP3) |
| 4.5 The plane, and where both conditions hold | 165 | **530** | The band; the opposing floors, where the trade-off claim is sourced; the V; Eq. (41); **+25 on 2026-09-23 for the delta conjunction's own count** (PP4) |
| 4.6 What the verdict needs, against what θ\* costs (new) | — | **100** | `revisions.md` §4's §4.6 entry |
| **5. Discussion** | 705 | **2,185** | |
| 5.1 What an alternatives level would have to supply | 390 | **560** | The specification, and what is left undone; **+40 on 2026-09-22 for item 1's §3.6 link (R4)** — the second condition is a sign on one opposition, and the four qualifications on that; **+70 on 2026-09-23 for the reading of the two criteria** (PP5); **+100 the same day for the order of the two motivations, and why the conjecture stays second** (PP10) |
| 5.2 Scale structure: two hypotheses, and what the comparison shows | 200 | **860** | H1 and H2 against Xiang et al. (R16, R17); 400 → 550 at T10, → 650 for **R27** (why no position is taken on H1), → 800 for **R28**: Eq. (F3)'s sign result, the Eq. (24) reach, and the one hedged causal statement; **+60 on 2026-09-23 for F.10's half-width control** (Z5) |
| 5.3 Realizability, halting, and the plausibility commitment (new) | — | **170** | `revisions.md` §5, item 2 |
| 5.4 What an algorithmic account makes posable (new) | — | **120** | `revisions.md` §5, item 3 |
| 5.5 Limits (was 5.3) | 65 | **345** | Convergence status, linear-Gaussian caveat, the relay's cost, **halting by tolerance** (raised from 80 on 2026-09-22: the section carried six topics at 80 and A19 adds a seventh), **the truncated state space** (raised from 150 on 2026-09-23, E17; **+45 the same day, the peak's climb now printed**, Z5) |
| 5.6 Predictions (was 5.4) | 50 | **130** | Exposure; granularity; the midpoint cut; **the lexical strength of a class (R27)**. Raised from 60 on 2026-09-22: it carries four predictions, and R27 gave the fourth the H1 reservation, at 15 words each |
| **6. Conclusion** | 150 | **265** | **+40 on 2026-09-23: what the change of read-out leaves standing** (PP6) |
| **Total** | **2,400** | **5,600** | |

**What this table does not do.** **§§3.6, 4.6, 5.3 and 5.4 are all written** (2026-09-22;
`revisions.md` §5 items 1–3 and §4's §4.6 entry). *This note said §§4.6, 5.3 and 5.4 were unwritten
until BG13 corrected it — it had gone stale within the same day they were written.* Every
subsection of §§3–6 now has a body. Limits and Predictions keep
their text under their new numbers, §5.5 and §5.6. Bodies rewritten to their new budgets: §§3.2,
3.3, 4.1, 4.4, 4.5 and 6 (tasks U9–U12), plus §5.2 (T10, R27, R28) and §3.6; the rest carry the new
figure against text still written to the old one. **Every section heading's figure was checked
against this table on 2026-09-22 and three were stale** (§4 1,020, §5 1,250, §6 165); they now
agree, and the check is worth repeating whenever a budget moves.

# 3. The proposed architecture (about 1,260 words)
 
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
 
## 3.2 A continuous world state and a soft lexicon (about 295 words)
 
- The world state is a proportion $s\in(0,1)$ carried in logit coordinates,
  $\zeta=\operatorname{logit}(s)$ (Eq. 1). Because $\operatorname{logit}$ is a bijection
  $(0,1)\to\mathbb R$, this is a change of coordinates and not a modelling assumption. Integrals
  over $\zeta$ are evaluated on a fixed quadrature grid (Eq. 2). **Say what the grid's two
  parameters do, and do not let the familiar half of it stand for both.** The node count $K$
  discretizes the integral rather than the state, and no quantity in the model is defined in terms
  of a node, so a reader must not take $K$ for a state-space size; Code Cell 2's specification
  check reports $\mathbb E[s]$ converging in $K$. **The half-width $Z$ is the other kind.** Eq. (1)
  carries $\zeta$ onto the whole of $\mathbb R$, so cutting it at $\pm Z$ **bounds the state
  space**, there is nothing for it to converge to, and the same check reports that it does not
  settle. §4.2's guard and §5.5 are where that is paid for; here it is one clause, so that the
  sentence about $K$ is not read as covering the grid entire. **Flag for §5.1 that $\zeta$ is a
  log-odds coordinate**; that fact does work twice later.
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
  there. **Nothing in the construction forces $\ell_0$ into $g_L$** (`agent/decisions.md` A3). It could
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
## 3.4 State units, error units, and what is local (about 290 words)
 
- Error units relax toward their residuals and state units ascend $\mathcal F$ (Eqs. 18–19), both
  instances of Bogacz's Eqs. (53)–(54). The slow parameter follows his own gradient under
  $\tau_\varepsilon\le\tau_\varphi/(4\lambda_{\max}(H))\ll\tau_\varphi\ll\tau_\theta$ —
  **a commitment and not merely an ordering** (Text cell 3, commitment 7; A11). The bound is
  critical damping of the stiffest mode; it is **ours rather than Bogacz's**, which is what makes it
  something to answer for in §5.3; and since $\lambda_{\max}(H)$ grows as $\theta_u^2$ it tightens
  as $\theta_u^{-2}$. What it secures is the **monotone** rise of $\mathcal F$, not convergence —
  the next bullet gets convergence from concavity instead, and the two should not be run together.
  There is no learning rate and none is required: the constant of proportionality is a time constant
  of the kind the error and state units already carry.
- **Why the dynamics are a claim and not an assumption.** $\mathcal F$ is strictly concave in
  $(\varphi_S,\varphi_u)$ for *every* $\theta_u$ and *every* $\Lambda$ (Eq. 21), and Eq. (22) lifts
  this to arbitrary $B$ and arbitrary $m$. So there is a unique global maximum and the closed forms
  Eqs. (15)–(16) are *the* solution. Note §8.1(iii): $\varphi_L$ does not enter the Hessian at all,
  so every convergence result is independent of the shape of the lexical field — which is what §5.2
  will need. The honest qualification belongs here: because the model is linear-Gaussian while
  $\varphi_L$ is clamped, the recurrent dynamics are a claim about **neural implementation**, the
  status they have in Bogacz's own linear examples, and the closed forms are what make that claim
  testable.
- **$\theta_u$ is learned, and where its flow starts is worth one sentence.** It belongs to the
  configuration, so every respawned network re-learns it, and the flow of Eq. (20) starts at
  $\theta_u(0)=0$ — one start shared by every configuration (A10, C3). **There the network is the
  tempered control, not the literal listener** (§4.1 names both), which is why §4's readings are
  displacements from a baseline the model passes *through* rather than one stipulated beside it.
- **Concavity is not the whole story; conditioning decides what is reachable.** Strict concavity
  secures convergence of the fast subsystem at *every* $\theta_u$ the slow flow passes through and
  says nothing about the cost of arriving. The **stiffness ratio** — Eq. (28)'s $\varphi_u$ rate
  over the constant $\varphi_S$ rate — is $(1+\theta_u^2)/2$, which is $404.8$ at the Gaussian
  prior's $\theta_u^\ast$. Slow-parameter learning and fast-subsystem conditioning are therefore
  coupled, and this is the sentence §4.6 and §5.3 are built on.
  *(Writer's note: the printed name is **stiffness ratio**. `revisions.md` §4's §3.4 entry called it
  a condition number and it is not one — at that $\theta_u^\ast$, $\lambda_{\max}(H)=810.69$
  against Eq. (28)'s rate of $809.69$, so the ratio is not $\lambda_{\max}/\lambda_{\min}$. Use
  the notebook's name; Text cell 4's *Integration cost and conditioning* prints the table.)*
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
  the same number, so no prediction moves. The cost is a fourth timescale — and **under commitment 7
  it is an ordering rather than a requirement the relay carries of its own**:
  $\tau_r\le\tau_\varepsilon$ (Eq. E6, which keeps the weak inequality), for **monotone
  $\mathcal F$ and not against oscillation** (F26). A relay no slower than the error units inherits
  their $\theta_u^{-2}$ scaling without a separate one; the scaling has moved, not disappeared.
  State the exception rather than smoothing it: at equality $\mathcal F$ is monotone under *some*
  only (O6). **The empirical content sits in commitment 7's separation, not in the relay's speed**
  — background §2.7 closes on the same correction.
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
 
## 3.6 Two read-outs (about 190 words)

The settled state is a pair of fields. Turning it into a statement about belief takes a read-out,
and the model admits two. Which one is in force decides what a result means, so the choice is stated
here rather than assumed.

- **The delta at the settled state** (Bogacz §3; `agent/decisions.md` A16). *Assumes* the posterior is a
  point mass at $(\varphi_S^\ast,\varphi_u^\ast)$ — the Laplace commitment the construction
  inherits, background §2.2 commitment 3. *Supplies* the settled vector itself, with **no
  normalization**, so the read-out is local. *Does not supply* masses or expectations: neither
  condition of §4.2's criterion has a direct analogue under it, and the nearest is the Voronoi cell
  that the peak of $\varphi_S^\ast$ falls in (App. A).
- **$q$** (Eq. 12; A13, A16). *Assumes* $\varphi_S$ codes unnormalized log-weights over the scale.
  *Supplies* a normalized density, and with it every mass statistic and the RSA comparison — which
  is why **both conditions of the criterion are stated on $q$**. *Costs* three things, and they
  should be named together: the normalizer $\sum_j w_j e^{\varphi_{S,j}}$ sums across every node,
  so no unit could form it from its own afferents; it sits outside the dynamics and takes no part in
  Eq. (20); and nothing in the architecture dictates it.
- **What they share, and where they part.** The **mode is shared**: the exponential and the
  normalizer are monotone, so the peak of $\varphi_S^\ast$ is also $q$'s mode. What differs is
  what needs the normalizer — and, with it, tempering. Halving $\varphi_S$ does not move its peak,
  so **the tempering/utility confound in $\Delta$ is a property of $q$**, not of the settled state.
  §4.4 reports where the two read-outs agree in direction and where they do not.
- **The position, and it is taken rather than reserved.** Both read-outs are reported, and the
  dissertation holds that **the delta read-out is the better defined of the two and the one this
  construction motivates**. Three reasons, in ascending order of weight.
  1. *It is congruous with the construction.* Every cost the bullet above charges $q$ is a cost the
     delta does not carry. It needs no sum across nodes; it is what the dynamics settle to rather
     than an operation laid on top of them; and the architecture dictates it where it dictates
     nothing about $q$ (`agent/decisions.md` A16).
  2. *The practical reasons are already on the page.* Halving does not move a peak, so the delta
     does not see the tempering at all and carries none of the tempering/utility confound that
     $\Delta$ has under $q$. What it registers is the utility level's own doing.
  3. **The representational reason, which is the one to lead with.** Background §2.2's commitment 3
     is not a convenience of the algebra. It is the claim that a system of this kind does not carry
     a posterior as a distribution over states but as a **small number of parameters, a mode and a
     variance**, and on a dense scale the two are nowhere near each other in cost: a value at every
     node against two numbers. A read-out that needs the whole field normalized across every node
     therefore asks the system for exactly the object the commitment says it cannot afford. That is
     why $q$ is a convention of the literature compared with rather than a statement the model makes
     about itself, and it is the reason to give first.
- **Four things the position does not license.** State them in the same place, or the position
  reads as licensing all four.
  1. **The criterion stays on $q$** (§4.2). Strengthening is stated as a mass in the accounts this
     dissertation answers to, the delta supplies no mass, and comparability is the whole reason $q$
     is kept (A16). A preference about which read-out the *architecture* motivates is not a
     preference about which read-out the *criterion* is written in.
  2. **Nothing is derived from the two agreeing** (R14, and §4.4's closing instruction). A
     preference is not a tie-breaker: where they part, the delta result is not the corrected version
     of the $q$ one, because the two answer different questions.
  3. **The position narrows what is reported, and the narrowing is stated where the figures are.**
     Under the delta read-out's own two criteria the conjunction holds under the **delta-like prior
     alone** rather than under three of the five (§4.4), and in **13** of the 121 cells rather than
     33 (§4.5). Taking the delta read-out as the better motivated one is not free, and §§4.4 and
     4.5 say so in their own voice rather than leaving it to be inferred here.
  4. **It buys no escape from §4.2's guard.** The mode is shared between the read-outs, so the
     position criterion moves with $Z$ and with $n$ whichever read-out states it.
- **The link forward.** $q$'s normalizer is a normalization across a represented set — the operation
  App. A shows would not be local, and the one §5.1 argues binarity absorbs.
---
 
# 4. Evaluation (about 1,890 words)
 
## 4.1 What is compared (about 140 words)
 
Three beliefs, all internal to the model:
 
- $q_{\mathrm{lit}}$, the **untempered literal listener**, $\varphi_S=\ell_0-\varphi_L$: the prior
  restricted by the entry and nothing else. At this first mention, one sentence saying that what
  "literal" denotes here is distinct from what it denotes in RSA and the Gricean literature, and no
  further explanation (DEC5 of `agent/history.md` §4). Writer's note, not for the
  paper: the sentence does not contradict §3.2, whose identification with RSA's $L_0$ holds only as
  $\Lambda\to\infty$, a limit and not a setting, so the sentence is true of every configuration
  evaluated. $q_{\mathrm{lit}}$ is a fixed point of this network rather than an external
  construction, being what Eq. (15) returns as $\sigma_S\to\infty$, **and it is one because
  $\ell_0$ enters at $g_L$**: under the placement §3.2 sets aside, no setting of the variances
  returns it (§3.2, reason 3; `agent/decisions.md` A3). Say both; the first removes the obvious objection
  that the baseline was built to be beaten, and the clause names what that answer rests on.
- The **tempered control**, $(\ell_0-\varphi_L)/2$, at $\theta_u=0$: the literal listener tempered
  by one half, the halving surviving into the belief because the read-out is exponential. It is a
  third quantity and not the baseline, and it holds the temperature fixed so that the utility level's
  own contribution can be read off. It is also where learning starts: Eq. (20) runs from
  $\theta_u(0)=0$.
- $q_H$, **the settled belief read through $q$** — §3.6 gives the read-out and what it costs.
State once, plainly, that RSA and wRSA are **analytic baselines and are not implemented**, so no
quantitative comparison is offered or implied.
 
## 4.2 The criterion, and how to read the statistics (about 545 words)
 
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
- **Which read-out the criterion is written in, and why that is not the read-out the dissertation
  prefers.** Both conditions are stated on $q$, because a mass above a cut is what the probabilistic
  accounts state strengthening in and the delta read-out supplies no mass (§3.6). **§3.6
  nonetheless holds the delta read-out to be the better motivated one**, and the two sit together
  without strain: $q$ is the read-out this criterion is *comparable* in, the delta is the read-out
  the construction *commits* to, and §§4.4 and 4.5 report the criteria of both. What the preference
  costs in reported results is stated there, not here, and §5.1 is where the two criteria are
  interpreted. This section reports them.
- **A guard the reader needs before the first table.** These statistics are $q$-masses taken after
  the read-out's exponential, so they are nonlinear in $\varphi_S$ and do not inherit invariances
  the $\varphi_S$ contrasts have. Measured instance: $\mu_u$ and $\ell_0$ move no $\varphi_S$
  contrast at fixed $\theta_u$ — bit-identical to $3.6\times10^{-15}$ across a sixty-setting sweep —
  while $\Delta_{\textit{some}}$ varies by more than a fifth of its own size across six $\mu_u$
  settings. Any claim about a contrast between utterances must be checked against $\varphi_S$
  directly.
- **A second guard: the verdicts are relative to the *all*-cell's width, not to $n$ alone.** Both
  q criteria are stated on the mass of an interval. $\theta_L=\log(2n-1)$ fixes that interval's
  lower end and the grid's half-width $Z$ cuts off its upper, so what the criteria are stated over
  has length $Z-\theta_L$ — and **both ends are stipulated, neither measured**: $n=10$ by
  Appendix A, $Z=6$ by `agent/decisions.md` I6, which fixes only $\theta_L<Z$ and nothing more.
  - *The $n$ end, which a cell prints.* Across both lexical strengths and all four base priors the
    q shift criterion changes status somewhere on a sweep of $n$, and *where* it changes depends on
    $\Lambda$ — granularity and lexical strength are not separable in what the tables below report.
    Appendix A prints that sweep.
  - *The $Z$ end, which a cell now prints too.* Appendix A's half-width ladder runs the same four
    criteria over $Z\in\{5,6,7,8,10\}$ at fixed node spacing, beside its ladder in $n$, and
    Code Cell 4's plane is recounted at each. **The guard is symmetric and both halves are
    sourced.** The figure to give is the one that makes the point in a line: under the flat prior
    at $\Lambda=512$ both q criteria are met at $Z=5$ and $6$ and neither from $Z=7$, while the
    peak of $\varphi_S^\ast$ climbs $0.8516$, $0.9168$, $0.9597$, $0.9862$, $0.9981$ in $s$ and
    crosses the cell's start at $0.9500$ between $Z=6$ and $7$. *(Writer's note: this supersedes
    the 2026-09-23 ruling that the $Z$ end takes no printed evidence, which the user reopened the
    same day. `agent/decisions.md` E17 records the supersession, and the audit stays class (e) for
    anything the cell does not print.)*
  - *How $Z$ reaches the verdict, and the one thing not to say.* Not by clipping a tail:
    $\varphi_S^\ast$ stays normalizable and nothing piles at the cut. $B$ is orthonormalized under
    the grid's own measure, so **the peak of $\varphi_S^\ast$ moves with $Z$** — the same peak
    Text cell 4 reports, which Eq. (12) makes $q$'s mode as well, so this is a fact about the
    settled field and not about a choice of read-out. That peak is $\zeta_{k^\ast}$, so what moves
    is the left-hand side of **§3.6's mode position criterion, $\zeta_{k^\ast}<\theta_L$** — name
    it, because "the peak relative to $\theta_L$" *is* that criterion and not a new quantity.
    Where it **fails**, the peak sitting at or above $\theta_L$, the conjunction cannot hold
    either. **State the implication in that direction only.** The mode position criterion being
    *met* does **not** deliver the conjunction: the first condition fails on its own in most
    configurations, and it is the more fragile of the two. So the conjunction is **not** a claim
    about where the peak sits, and the delta read-out is no substitute for it, both moving
    together. *(Writer's note: Text cell 4 reports that peak in $s$ and $\theta_L$ is a threshold
    in $\zeta$; convert once, or the two look like different quantities.)* §5.2's comparison is
    untouched, $R^2$ over profiles reading agreement of shape across items.
  Two further cautions attach. A sweep **brackets** a change rather than locating it; and a change
  of status may be the sign flip of a quantity already decayed to $10^{-7}$, which is not the
  finding that a flip at $10^{-1}$ is.
## 4.3 The specification holds (about 105 words)
 
Brief, and reported as a table rather than argued. The closed forms agree with the integrated
dynamics to $4.45\times10^{-9}$ — **quoted as $1.00$ times the stopping tolerance, not as an
absolute**, because I3 keys that tolerance to $\lambda_{\max}(H)$, so the figure is a property of
what is being integrated and moves between rows. The fixed-point identities of Eq. (17) hold; the
Hessian is negative definite across $\theta_u$; the relaxation rate is independent of
$\varphi_L$; the analytic messages agree with finite differences. Grid refinement is tested on the
**tail** of the sequence rather than on two coarse grids, because the rate is set by the entry being
a step: $|401-801|$ in $\mathbb E[s]$ is $1.7\times10^{-3}$ under the hard mask against
$3.3\times10^{-6}$ under a smooth one, with the smooth mask serving as the control that identifies
which of the two is model and which is quadrature. (The coarse $51$–$401$ spread, $1.1\times10^{-2}$,
is the $O(h)$ step artefact, which is why the tail is what is tested.) **The table's fifteenth
line is the companion to that one and belongs beside it in the prose**: widening the half-width at
fixed node spacing does not settle, $\mathbb E[s]$ spreading $1.5\times10^{-1}$ over $Z\in[5,10]$
against the $1.7\times10^{-3}$ tail in $K$, which is §3.2's two-parameter point measured rather
than asserted. Report the pair in one sentence and send the consequences to §4.2's guard.
Code Cell E3 checks that the relay reproduces every one of these numbers.
 
## 4.4 The five priors (about 470 words)
 
**This is the section the argument turns on, and since 2026-09-23 it turns on one row of it.**
It reports Text cell 4b's rows: all five priors at $\Lambda=512$, each at its own learned
$\theta_u^\ast$, with $\Lambda=8$ entering as a one-line contrast (R20, P-10). **The delta-like row
is the one the constructive claim rests on**, for the reason the baseline bullet below gives, and
the other four are reported rather than relied on. Write the table first and that sentence after
it, so the reader sees the rows before being told which one carries weight.
 
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
- **Under the other read-out (§3.6), the same rows say something different — and the configuration
  has to be named each time, because the two read-outs are reported at different $\Lambda$.**
  - *Part D's four diffuse priors, at $\Lambda=8$ and each at its own $\theta_u^\ast$* (Code
    Cell 2). The peak of $\varphi_S^\ast$ under *some* sits **up** the scale of $\ell_0$'s peak
    under every one of them — $0.5000\to0.5890$, $0.5000\to0.6726$, $0.2535\to0.3274$,
    $0.7465\to0.8429$ — while the utility level's contribution to all-region $q$-mass is negative
    under each. **The two read-outs disagree in direction**, and §3.6 says why that is possible:
    halving does not move a peak, so what the mode registers is the utility level's own doing.
  - *The same five priors at $\Lambda=512$*, which Code Cell 2b prints beside the q criteria and
    beside this section's own table, so the two read-outs can be read at one lexical strength for
    once. The cell prints **the mode position criterion met in all 8 of its rows and the mode shift
    criterion in 2**, those two being the delta-like prior at $\theta_u^\ast$ and at its realizable
    $\theta_u$. The four diffuse priors' peaks move *up*, to $0.9072$, $0.9168$, $0.8966$ and
    $0.9168$ from $0.5000$, $0.5000$, $0.2535$ and $0.7465$. So **under the read-out §3.6 prefers
    the conjunction holds under the delta-like prior alone, where under $q$ it holds under three of
    the five.** Say it in the same breath as the q count and never on its own. *(Writer's note: the **8 rows
    are 5 priors and 3 repeats** at a realizable $\theta_u$, so a count over rows is not a count
    over priors. Since 2026-09-23 the cell prints **both**: over the five distinct priors, one row
    each at its own $\theta_u^\ast$, **the mode shift criterion under 1, the mode position criterion
    under 5, both under 1, against the q criteria's 3, 5 and 3** — the same form the q blocks above
    use, so either count may be quoted (C6). It also prints that each repeat carries the same four
    verdicts as its own $\theta_u^\ast$ row. Naming the prior is still the better sentence, because
    it says *which*.)*
  - *The mode position criterion is already met by $\ell_0$ alone* on those four: the cell of
    *all* starts at $s=0.9500$, and every one of the four priors peaks outside it before the model
    is run. Nothing is shown by a criterion its own baseline meets. **The same holds at
    $\Lambda=512$**, where Code Cell 2b prints the same four $\ell_0$ modes, so **the delta-like
    prior is the only row in either cell whose baseline starts inside the cell of *all***, and the
    only row where meeting the mode position criterion is the model's doing rather than the prior's.
    §5.1's reading of the two criteria rests on this bullet as much as on the counts.
  - *The delta-like prior, at $\Lambda=512$* (Code Cell 2b), is the one row where the model moves
    the peak out: $0.9852$ **inside** the cell to $0.9468$ **outside** it, one node below
    $\theta_L$. It stays outside on grids of $201$, $401$ and $801$ nodes, so it is not a
    discretization artefact.
  - **Report both read-outs and derive nothing from their agreement.** Where they agree the reading
    is not doubled, and where they disagree neither is the corrected version of the other; they
    answer different questions, §3.6 says which.
- **The row the constructive claim rests on, stated once and plainly.** Under the delta-like prior
  the baseline starts with *all* in the majority and with its own peak inside the cell, and the
  network moves both: $q_{\mathrm{lit}}=0.9568$ to $q_H=0.4351$, and a peak at $s=0.9852$ inside the
  cell to $0.9468$ outside it, one node below $\theta_L$. **Under the other four priors neither
  quantity had anywhere to move**: $q_{\mathrm{lit}}$ is already below $\tfrac12$ and $\ell_0$
  already peaks outside the cell, so those rows report what the model does to a belief that already
  meets both position criteria. That is the whole of the asymmetry, and it is why "three of five"
  and "five of five" are reported counts rather than the result. §4.5 gives the same measurement on
  the plane, where it is a count and not a single row.
- **One sentence pointing to §4.6:** the conjunction is shown in the integrated dynamics, not only
  in closed form, for all three rows that meet it (Code Cell 2b).
## 4.5 The plane, and where both conditions hold (about 530 words)
 
- **What the network carries, with the cells its baseline already holds left out (Code Cell 4).**
  Lead with this, because it is the plane's version of §4.4's one row and it is what the
  constructive claim quotes. Of the 121 cells, $q_{\mathrm{lit}}$ holds at least half the
  all-region in **77**, and in **15** of those the settled belief holds less than half. $\ell_0$
  peaks inside the cell of *all* in **66**, and in **9** of those $\varphi_S^\ast$ peaks outside it.
  The 9 are a subset of the 15, which is the same containment §3.6's two read-outs show everywhere
  else. **The shift criterion is met in all 15 and in all 9**, and the cell prints that rather than
  the prose deducing it. Both counts sit at $\alpha$ from 16 to 128 under $q$ and 32 to 128 under
  the mode, between the region where the prior meets the criterion unaided and the region past
  $\alpha=256$ where the criterion is unreachable at any $\Lambda$ on this grid — so **the band in
  which this architecture does the work itself is bounded on both sides, and by different things**.
  *(Writer's note: these are the counts that survive §4.4's rule that nothing is shown by a
  criterion its own baseline meets. Do not restate the rule here; §4.4 states it and §5.1 uses it.)*
- **And say in the same breath that 15 and 9 are $Z=6$ figures**, because they are the claim's own
  numbers and §4.2's guard bears on them hardest. Appendix A's ladder counts them **32, 15, 0, 0, 0**
  and **22, 9, 0, 0, 0** over $Z\in\{5,6,7,8,10\}$. **They are no more robust to the half-width than
  the conjunction is**, and they cannot be: carrying a criterion the baseline fails entails a shift,
  so each is bounded above by the shift count, which is already $0$ by $Z=7$. State that as the
  reason rather than leaving the pattern to look like a coincidence. What survives a wider grid is
  the **bare** position count, $76, 59, 48, 25, 12$ against the shift's $113, 74, 24, 0, 0$, and
  that is a count the baseline is doing the work in — which is exactly what §4.4's rule bars from
  carrying a claim. **The honest summary: conditioning on the baseline buys the argument and costs
  the robustness, and both halves are reported here.**
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
  it is sourced here, on the floors.** **And with the position criterion carrying the constructive
  claim, the second floor is the binding one**: it is what closes the band at $\alpha=256$ and so
  what bounds the 15 and the 9 above. Say so, and say what follows in §5.1: a drain keyed to the
  alternative lowers the *first* floor, so it would not extend the region this architecture's own
  result lives in. The level is not what the constructive claim needs, which is R2's point reached
  from the other end. It is a property of the plane and not of Part D's rows: at
  $\Lambda=512$ both floors lie at or below 512 from $\alpha=1$ to $64$, which is why those rows do
  not show the tension (§4.4). "Under every prior tested" is not written anywhere; §5.1 and §6
  point here.
- **The V, under both read-outs (R13, R14).** The least $\Lambda$ at which both conditions hold
  runs $512$, $256$, $128$, $64$, $64$, $256$, $512$, $1024$ over $\alpha=1$ to $128$, a V with its
  minimum at $\alpha=8$ and $16$. Under the delta read-out's two criteria (§3.6; R12) the right arm
  is shared from $\alpha=32$, at $\Lambda=8\alpha$; the left arm exists only under $q$, since the
  mode shift criterion is never met at $\alpha\le8$; and the two conjunctions part in 20 cells, all
  of them met under $q$ alone. **Give the delta conjunction its own count and not only the
  difference**: it holds in **13** of the 121 cells against $q$'s 33, and §3.6's position makes 13
  the figure this dissertation's preferred read-out returns. Report both, and do not let the
  preference quietly promote one of the two numbers. Report the V as a result, and derive no evidence for a missing level
  from it. **Say which half of that is $Z$-conditional** (§4.2's guard). **Robust, and now printed:** Appendix A's ladder counts the two
  conjunctions at each half-width and counts the cells where the mode conjunction holds and the q
  conjunction does not, and **that column is zero at every rung**. So the delta conjunction is a
  strict subset at every half-width swept, the two read-outs part only in $q$'s favour, and the
  instruction just given stands on the subset relation and not on the count. **Not robust:** the
  figures **13** and **20** are $Z=6$ figures. The ladder gives the delta conjunction as
  $37, 13, 0, 0, 0$ and the q conjunction as $68, 33, 0, 0, 0$, so the gap runs $31, 20, 0, 0, 0$.
  *(Writer's note: a zero gap at the wide rungs is **both** conjunctions empty, not the read-outs
  agreeing, and the zero reversal column is what distinguishes the two. Never report a zero gap as
  agreement. What is still **class (e)** is the boundary $\alpha\le8$: the least $\alpha$ at which
  the mode shift criterion is met runs $8, 16, 32, 32, 128$ in the audit and no cell prints it, so
  write the boundary as a $Z=6$ figure without quoting its ladder.)*
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
 
## 4.6 What the verdict needs, against what $\theta_u^\ast$ costs (about 100 words)

**Evidence for §5.3, reported without interpretation.** Every row is the delta-like prior at
$\Lambda=512$ (Code Cell 2b), the case the criterion is under most pressure in.

- **The conjunction arrives early.** It first holds at $|\theta_u|=2.126$, where
  $\lambda_{\max}(H)=6.5$ and commitment 7 demands a separation $4\lambda=26$. Eq. (20) from
  $\theta_u=0$ passes that value **in one update**. Whatever makes this row expensive, it is not
  the conjunction.
- **What the flow actually reaches is where it halts** — its own update having fallen below the
  tolerance, the only stopping rule the model has, and an **ad hoc** value (A19). That is
  $\theta_u=34.695$, after $7$ updates. The integrated run there ($242{,}163$ Euler steps) gives
  $\Delta_{\textit{some}}=-0.5208$ and $q_H=0.4361$: **both criteria met, in the dynamics and not
  only in closed form.** There $\lambda_{\max}(H)=1205.8$, a demanded separation of $4{,}823$.
- **What $\theta_u^\ast$ would cost.** The same inference at $\theta_u^\ast=1407.77$ would take
  $3.98\times10^{8}$ steps at a separation of $7.9\times10^{6}$ — hours on the machine that ran it.
  Quote the step count and the separation, not the wall clock: the hours sit on a `cost:` line and
  move with the machine (`agent/agent.md` §5.2).
- **And $\theta_u^\ast$ is not what the flow reaches.** Code Cell 2b says so in its own output:
  $\theta_u^\ast$ lies orders of magnitude beyond both the conjunction's threshold and the halt,
  and **this integrator does not reach it at all**. That $\theta_u^\ast$ *is* the maximizer rests
  on the closed form and the monotone rise, not on an integration.
  *(Writer's note, not for the paper: the sharper statement — not within $0.1\%$ of
  $\theta_u^\ast$ after $5{,}000$ updates, F15 of `agent/history.md` §3 —
  is **class (e)**. No cell prints it, and I8, which once licensed recorded scripts as sources, is
  superseded by C6 and I10. Do not reinstate those figures unless a cell prints them.)*
- **Report, and stop.** §5.3 is where the cost is interpreted, and §5.5 is where the tolerance's own
  locality debt (D12) is admitted. This section states neither.
---
 
# 5. Discussion (about 2,185 words)
 
## 5.1 What an alternatives level would have to supply (about 560 words)
 
**Frame the section as a specification, not a concession.** The claim is not that this architecture
excludes within-trial competition. It is that adding a level is a construction with four stated
obligations, that the present results discharge part of each, and that the architecture's own
results point at which design is the tractable one.

**And state the order of the motivations in the frame, because the section carries two and they are
not of equal weight.** **The complexity saving leads**, and it leads for an epistemic reason rather
than a rhetorical one: it is derived from the construction and needs no datum to be true, so it
survives a change of data. R2 rests the level on it and **R2 stands**. The conjecture about
consistent shift is the **second** motivation, and the bullet below says what keeps it second.
 
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
- **The two criteria are keyed to different parts of the construction, and this is the
  dissertation's reading of them.** State it as a conjecture, argued and not measured, and under
  §4.2's guard: both criteria are stated over the cell of *all*, and that cell is stipulated at both
  ends. Five moves, in this order.
  1. **Consistent shift is what an alternatives level would supply.** The shift criterion is met
     here only where the prior already puts mass on the all-region. It is the fragile one of the two
     under the five priors (§4.4); it is where the read-outs part, in 35 of the 121 cells and in
     half of Code Cell 2b's 8 rows, that cell printing the shift criteria agreeing in 4 of 8 and the
     position criteria in 8, against **no** cell of the plane where the position criteria part;
     and its floor falls with prior concentration where the other's rises (§4.5). A drain keyed to
     the *alternative* rather than to prior mass is what would detach it from the prior, which is
     the argument the floors already carry. **The conjecture is that this architecture cannot
     deliver consistent shift because it lacks that level, not because the effect is absent.**
     Nothing here measures what such a level would do, and the sentence says so.
  2. **Shift does not stand as the criterion of scalar strengthening on its own**, and this is not a
     retreat from 1. A shift that leaves *all* the most probable single outcome is movement without
     resolution (§4.2), so the dissertation does not fall back on the shift alone when the position
     criterion is the one its architecture supplies, and does not treat the shift's fragility as
     the finding.
  3. **Position is mostly what this architecture instantiates.** Two reasons, of different kinds.
     *It is stated on the object the construction represents*: a mode is what commitment 3 says the
     system carries (§3.6), so "where the settled field peaks, relative to the cell of *all*" is a
     question this architecture answers natively, in either read-out — which is why the two position
     criteria agree in every cell of the plane and in every row of Code Cells 2 and 2b, with the
     single exception move 5 names. *The shift criterion is not like that*: it is a difference
     between two normalized masses taken against a baseline, and the fourth qualification in the
     list below already says binarity does not remove that and no level carries it as one unit. So the criterion this architecture supplies natively is position, and the criterion that
     needs machinery beyond it is shift.
  4. **The guard, in the same breath, because 3 overstates without it.** Where the baseline already
     meets the position criterion nothing is shown by the model meeting it (§4.4), and that is
     every prior but the delta-like one, at both lexical strengths; the delta-like row is the one
     where the model carries the peak out. At the sharp end of the plane the criterion is not met at all, its floor
     rising past reach beyond $\alpha=256$ (§4.5). **So the claim is that position is where this
     architecture does its work, not that meeting it is common or cheap.**
  5. **And the agreement of the two position criteria is measured, not proved.** Appendix A's sweep
     holds one printed row where they part: the flat prior at $\Lambda=8$ and $n=2$, where the mode
     sits outside the cell of *all* while $0.5615$ of the mass sits inside it. That row is §4.2's
     guard on $n$ made concrete, and it is why 3 is written as a reading of the measurements rather
     than as a property of the criteria.
- **What weight that conjecture carries, and why it does not outrank the complexity argument.**
  Put this immediately after the conjecture, or a reader who has just read it will take it for the
  case. Four moves.
  1. **The conjecture is about this architecture, and the prose should say so.** What §§4.4 and 4.5
     show is that the shift criterion is inconsistent **in this model**, which has no within-trial
     competition. The step from there to *inconsistent without within-trial competition* is the
     conjecture, not the measurement: one architecture is one architecture. Write the model-relative
     version. Nothing in this section needs the stronger one.
  2. **A shift would be welcome, not required.** Say the hope plainly: a level carrying the
     alternative would be expected to deliver the shift too, and that would be a result worth
     having. It is not a condition on the design, and no obligation below is contingent on it.
  3. **Why it cannot be promoted, and the obstacle is not instrument precision.** The shift is a
     **comparison of two distributions over the scale**, the settled belief against the literal
     listener, with the prior held fixed across both. Two of those three quantities can be asked
     for and the third cannot.
     - *The settled belief can.* Xiang et al. (2022) elicit graded judgments over a five-point
       scale, which is the measurement §5.2 already runs against, and Chemla and Spector (2011)
       establish graded interpretation judgments as a method.
     - *The prior can*, and Degen, Tessler and Goodman (2015) and Cremers, Wilcox and Spector
       (2023) elicit it precisely to drive a prediction. Note the complication in the same breath:
       *Wonky worlds* shows the prior is **revised by the utterance**, so "held fixed across both"
       is not an innocent premise even where the prior is measured.
     - *The literal listener cannot.* It is defined by holding the prior and the truth conditions
       fixed while removing the pragmatic computation, and **no behavioural condition instantiates
       that**. Where the literature supplies a "literal" condition it manipulates the speaker's
       epistemic state, which changes the inference rather than suspending it, and what it returns
       is a **rate**, not a distribution over the scale. Geurts and Pouscoulous (2009) show how far
       the measured rate moves with the task the judgment is collected in. In the probabilistic
       accounts the literal listener is **computed**, from an elicited prior and a stipulated
       semantics, which is exactly what it is here: §4.1 says $q_{\mathrm{lit}}$ is a fixed point of
       this network rather than an external construction, and that is a virtue **inside** the model
       and the reason it has no counterpart outside one.
     **State the conclusion as a claim about what the quantity is, not about what instruments
     reach.** The position criterion is one distribution against a threshold, both of which a person
     can be asked for. The shift criterion is stated against a baseline that is a construct in every
     account that has one, so any empirical claim of the form *strengthening is a shift* is relative
     to a stipulated semantics and an elicited prior. Written that way the point does not expire;
     written as a limit of current methods it invites "wait for better methods".
  4. **And say where the wanting comes from, in one sentence and without contempt for it.** That
     strengthening should be a shift and not only a position is, in the first instance, something we
     introspect: hearing *some*, one takes oneself to have moved **away from** *all*, not merely to
     have landed below it. That is a real datum about the explanandum and it is the source of the
     framing the background sets out. It is also not the kind of thing that outranks a motivation
     needing no datum at all, which is move 1 of the frame and the whole of R2.
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
- **And the criterion's second condition is binary already (§3.6, R4).** This is where the previous
  bullet stops being about the generative map and starts being about what §4 actually reports.
  §3.6's cost of $q$ is its normalizer, which sums across every node. But
  $q_H(\textit{all}\mid\textit{some})<\tfrac12$ says only that the **log-odds of the all-region
  against its complement is negative** — a sign on a single opposition, and precisely the opposition
  $\langle E_{\textit{all}},\ \ker E_{\textit{all}}\rangle$ that one level of the cascade above
  carries. **A level carrying that opposition as one log-odds unit would report the second condition
  as that unit's sign, with no normalization across the scale at all.**
- **The qualification, in the same place, on the pattern of A17.** Say all four; the claim is worth
  less without them.
  1. A log-odds of two cell masses cancels the *global* normalizer but **still sums within each
     cell**, so the saving is partial, not total.
  2. It is complete only if the level's state **is** that log-odds unit, rather than something a
     read-out computes from a field.
  3. Whether $\varphi_a$'s value equals $q$'s cell log-odds is part of the $g_a$ algebra this
     section already declares underived — it is **not a fifth obligation**, but a consequence the
     four below would settle.
  4. **The first condition has no such binary form.** It is a difference against
     $q_{\mathrm{lit}}$, which is two normalized quantities compared, and nothing in binarity
     removes that. So the saving reaches one of the two conditions, and the section says which.

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
## 5.2 Scale structure: two hypotheses, and what the comparison shows (about 860 words)

Written against Code Cell F's executed output (Appendix F). Every number below is printed there;
every number attributed to Xiang et al. is cited and printed by no cell (S-5). **No sentence in this
section says what any mismatch is due to** (R16).

- **The setup.** §3.3 fixes $\theta_L$ by the predicate's own resolution, $\theta_L=\log(2n-1)$: at
  a scale endpoint the threshold is supplied by the scale itself, while a predicate with no endpoint
  to anchor to must take its resolution from elsewhere, and Appendix A leaves open what fixes it.
  In the terms of the gradable-adjective literature, maximum- and minimum-standard absolute
  adjectives have closed scales and conventional endpoint standards, while relative adjectives have
  open scales and context-dependent thresholds (Kennedy, 2007; Xiang, Kennedy, Xu & Leffel, 2022).
- **The two hypotheses, stated as hypotheses.** **H1:** scalar expressions whose atomicity is
  unstable carry weaker lexical strength — in this model's quantities, $\Lambda$ as a function of
  how stably the predicate fixes $n$, which couples two quantities §3.3 fixes independently.
  **H2:** open-scale adjectives behave like *some*, complete-scale adjectives like
  endpoint(s) + *some* — a map from scale class onto an entry of Eq. (A1), read in the adjective's
  own orientation. **Neither is adopted, and neither is rejected.** The section states them, reports
  the comparison, and stops.
- **Why no position is taken, stated rather than left to inference.** A hypothesis about the lexicon
  is not settled by a fit statistic on one experiment at one resolution, and **what is measured here
  is bound to this phase**. The comparison runs at a single $n$, so the quantity H1 is *about* — how
  stably a predicate fixes its resolution — does not vary across the classes compared; what
  distinguishes them here is which entry of Eq. (A1) they carry, and reading that as a difference in
  atomicity is an interpretation of the result, not the result. And the architecture this phase
  commits to is one the dissertation itself expects to change: §5.1 proposes a level this model does
  not have, and the instinct below doubts the single $\theta_L$ that fixes both endpoints. **A match
  or a mismatch obtained under commitments a later phase may drop is evidence about this phase.**
  H1 is posed because of what it would mean for how the model develops, and it is left open on
  purpose.
- **What is instantiated, and the half that is not.** Five scale positions are the five Voronoi
  cells of $n=4$, so $\theta_L=\log 7$; the default $n=10$ of §4 is untouched. **H2's open-scale
  half is not tested.** A relative adjective's cut is a context threshold that neither endpoint
  supplies, and this phase fixes both endpoints with the one $\theta_L$, so the relative class is
  not modelled and its items carry no prediction. $\Lambda$ is **fitted**, per class, here and
  nowhere else in the dissertation — H1 is a claim about $\Lambda$, so a comparison holding it fixed
  could not bear on H1 at all. One $\Lambda$ per class and not one per image type: the second fit is
  declined, and nothing here says $\Lambda$ is independent of image type.
- **The ensemble is the inventory's, not the experiment's.** Each entry is paired with its own
  kernel, $\{\chi,\ker\chi\}$, which for these two classes coincides with the antonym the
  experiment used. That coincidence follows from one $\theta_L$ fixing both endpoints; it is not a
  thesis about antonymy, and membership in the inventory follows from having met an entry somewhere,
  not from having met it in this experiment — the authors' latin square in fact shows no participant
  both adjectives of an image set.
- **Where the model matches.** H2's class-to-entry map is the one the data show: the maximum class's
  measured mass sits in the top cell ($0.960$ under shapes, $0.929$ under artifacts) and the minimum
  class's spreads over every cell but the bottom one, which is what $\{\zeta\le-\theta_L\}$ excludes.
  The maximum class is fitted at $R^2=0.993$, and **puts no upper bound on $\Lambda$** — every value
  from $6$ to the ladder's top at $2048$ is within $0.005$ of the best, consistent with the hard
  entry of the $\Lambda\to\infty$ limit. The minimum class **requires a finite $\Lambda$**: its fit
  rises to $0.434$ and falls away on both sides, to $0.351$ by $\Lambda=2048$, with the optimum
  bracketed between $32$ and $48$. **Two sentences on the half-width, now that Code Cell F prints
  the control (F.10).** The maximum class's $R^2$ reads $0.993$ at every half-width on the ladder;
  the minimum class's moves between $0.397$ and $0.434$ and the pooled figure between $0.762$ and
  $0.827$. So **H1's content survives the half-width and the minimum class's bracket is a
  default-grid figure**, which is the contrast §4.2's guard predicts: a statistic scoring agreement
  of shape across items moves by hundredths where a mass above a fixed cut changes status
  outright. **That contrast runs in H1's direction, and it is weaker evidence
  than it looks.** The maximum class's *threshold* is not identified by these data at all: its fit
  stays between $0.989$ and $0.993$ for every cut from $\zeta=-1.0$ to $+4.0$, and its literal,
  tempered and settled beliefs agree to three decimals. What that class establishes is a lower bound
  on $\Lambda$ and nothing above it — not that its threshold is endpoint-anchored, which is read in
  from the scale structure rather than measured. The utility level is what earns
  the minimum class's fit — the literal listener reaches $0.103$ against the model's $0.434$, a gain
  of $0.331$, while on the maximum class it reaches $0.992$ against $0.993$, so that class is fitted
  by its entry alone. And the image-type difference has the right sign and the right home: $-0.18$
  against a measured $-0.83$ in the minimum class, $+0.03$ against $+0.09$ in the maximum.
- **Where it does not.** The minimum class is the residual: $R^2=0.434$ against $0.993$, and its
  measured profile peaks at position 3 under shapes where the model's peaks at position 5. The
  image-type difference is about a fifth of the measured size. The between-class gap is $+1.33$ and
  $+0.41$ measured against $+0.44$ and $+0.22$ modelled. And the model displaces belief further from
  the elicited prior than the data do in both conditions ($+3.37$ against $+2.40$ under shapes,
  $+2.43$ against $+2.11$ under artifacts). **Reported, and not explained.**
- **How far the utility level reaches, and what fixes $\theta_u^\ast$'s sign (App. F §6, F.9).**
  Two facts, both printed. First, the ensemble is $\{\chi,\ker\chi\}$, so
  $\sum_y\varphi_{L,y}=\Lambda\mathbf 1$ and the $\Lambda$ term cancels against
  $B^{\mathsf T}W\mathbf 1=0$, leaving $\sum_y c_y=2B^{\mathsf T}W\ell_0$ (Eq. F3, exact to
  $7.4\times10^{-13}$). Since Eq. (B2) gives $\theta_u^\ast$ the sign of
  $\langle\mu_u,\sum_y c_y\rangle$, **that sign is fixed by the prior alone — independent of
  $\Lambda$ and of which entry was uttered.** Second, it does not follow that the sign reaches the
  belief: in the minimum class the settled field is within $4.9\times10^{-3}$ of Eq. (24)'s limit,
  which is **the same from either sign**, and scoring that limit instead changes no $R^2$ in the
  third decimal. *(Note for the notebook: $|\theta_u^\ast|$ diverges near Appendix B's degenerate
  ray, so a mean over items is not a usable statistic — 11 of 12 artifact items in the minimum class
  have $\theta_u^\ast<0$, median $-769.8$, while the mean is $+1604.7$ on one item's $+29123.3$.
  Quote medians.)*
- **What the amplification does, and what we think it is the cause of.** Eq. (24) doubles the
  $\operatorname{span}B$ component of $\ell_0-\varphi_L$, displacing the read-out up the scale.
  Measured from the literal listener, that displacement is $+1.12$ under shapes and $+1.39$ under
  artifacts — **near-constant** — while the data are displaced $+0.16$ and $+1.06$. In the maximum
  class both are within $0.02$ of zero. **We think this near-constant displacement is the cause of
  the minimum class's misfit**: the amplification the utility level supplies is close to insensitive
  to the manipulation the experiment actually ran, so it overshoots by $+0.97$ where the data barely
  move and by $+0.32$ where they move nearly as far.
  **Say it as a belief about this phase, and not more.** It is the one causal statement §5.2 makes,
  and it is made under the reservation above: the class it concerns is the one whose threshold sits
  a resolution step inside the *other* endpoint — the boundary §5.2's own instinct would reassign to
  $\theta_A$ — so whether the account survives an architecture with two thresholds is not something
  this phase can show. It is offered as what we currently think, not as a result.
- **What the comparison is worth.** Xiang et al. find that Bayesian pragmatics models what is
  *communicated* well but threshold judgments poorly, especially for absolute adjectives, and
  conclude that Bayesian reasoning must be combined with the semantic conventions governing
  thresholds. **That is the architecture this model already has**: $\theta_L$ is a semantic
  convention, fixed by the predicate rather than inferred, sitting inside a free-energy inference.
  Their own models' $R^2$ are cited for comparison and printed by no cell; note that every model in
  their paper is weakest on the minimum class, this one included, as they say themselves.
- **The parity result, restated at this resolution (S-7).** By §3.5 the even/width column is the
  axis along which mass moves between centre and extremes. **An entry whose threshold sits at the
  midpoint of the log-odds scale has no even component at all**: $\chi=\mathbb 1[\zeta<0]$ is a
  constant plus a purely odd function, and the basis is orthogonal to the constant by construction
  (App. C §2), so its width loading is $1.2\times10^{-17}$. Moving the cut off-centre is what gives
  it one. At $n=4$: **the two absolute entries' tilts are identical, differing by
  $0.0\times10^{0}$, and their widths sum to $0.0\times10^{0}$ — they differ in the even coordinate
  alone.** A parity argument in the family of Appendix C's, not a fitted trend.
  *(Numerical note for the notebook, not the prose: the midpoint cut sits on a node, half-weighted;
  left unweighted the grid reads $0.0194$, the node's own mass. Report the parity, not the artifact.)*
- **Calibrate the claim, in both directions.** $\Lambda$ is fitted and labelled as fitted; nothing
  else here is, and a ladder **brackets** an optimum rather than locating it. The section must not
  credit H1 with more than the ordering it shows, and must not treat the residual as telling against
  it either. The one causal statement above is hedged on purpose and stays hedged: it is what we
  think, about this phase, and nothing in §5.1, §5.6 or §6 may restate it as established. §4.2's second guard applies here too: the
  denotation $n$ that fixes $\theta_L$ is stipulated, and §4's readings move with it — this section
  runs at $n=4$ because the authors' scale has five positions, a choice about their paradigm and not
  a discovery about the predicates.
- **The instinct, stated once, as an instinct.** The symmetry the parity paragraph states — both
  endpoints fixed by the one $\theta_L$ — is a commitment of this phase, and it may be the wrong
  one. The instinct is that separating the lexical level's threshold from an alternatives level's,
  $\theta_L$ inferring the boundary of $0$ and $\theta_A$ the boundary of $1$, would give the
  relative class's midpoint $t$ something to be a property of. **No promise is attached**: the
  algebra is not derived, the phase is not built, and nothing above is claimed to follow from it.
  §5.1 is where an alternatives level is specified; $\theta_A$ is named here and not there, because
  naming it among what that level "would have to supply" would turn an instinct into an obligation.
## 5.3 Realizability, halting, and the plausibility commitment (about 170 words)

The cost sense keeps the name **realizability** (O7). §4.6 supplies the evidence; this section says
what it costs and what is still owed.

- **What halts, and on which timescale.** The claim is about the **slow** flow of Eq. (20), which
  ascends $\tilde{\mathcal F}$ toward $\theta_u^\ast$. Since $\theta_u$ is an exposure statistic
  across trials, halting here is **the end of plasticity across exposures, not the end of one
  inference** — within an inference the fast subsystem settles at whatever $\theta_u$ the slow flow
  currently carries. Say that once; the two are otherwise easy to conflate.
- **Why the maximizer does not stop it.** A flow halts where its gradient vanishes, at
  $\theta_u^\ast$. $\tilde{\mathcal F}$ flattens toward its asymptote, so the flow **approaches
  without arriving**, and nothing *in* $\tilde{\mathcal F}$ stops it earlier. That is the point:
  what stops it is not in $\tilde{\mathcal F}$.
- **What does halt it.** The flow stops when **its own update falls below a tolerance**. The rule is
  self-contained in the way the old stopping rules were not: it reads the size of the step the unit
  has just taken and nothing else — no closed form, and nothing about the shape of a trajectory the
  unit has no access to. No guard is attached, because a guard would need exactly the knowledge of
  its own trajectory that this denies the system. **The value is ad hoc**, so what is offered is
  halting *by* a tolerance, not any particular tolerance; the dissertation declines both to claim an
  organism needs one for a computer's reason and to stipulate a value representative of a brain.
  Two implications, owned rather than hedged: a plausible tolerance halts **far short of**
  $\theta_u^\ast$, and where the flow starts slowly the same rule halts it **at once**, leaving the
  belief at the tempered control.
- **A direction, not a commitment — and the reason is a violation we have not settled (D12).** The
  **fast** loop's tolerance is keyed to $\lambda_{\max}(H)$, a global spectral quantity, because
  the roundoff floor it must clear is not a constant. The defence that the timescale bound already
  requires that quantity is weaker than it looks: **that bound is itself ours and not Bogacz's**, so
  the keying inherits an unpaid licence of the same kind rather than a settled one. The **slow**
  rule $|\Delta\theta_u|<\mathrm{tol}$ carries no such debt, and §5.3 says which of the two is
  clean rather than demoting both alike.
- **Where Bogacz stands, since it cuts against the obvious reading.** He has **no halting rule and
  no halting problem**: his parameters never converge, being updated after each observation with
  successive observations differing, and he offers the value at which the *expected* change vanishes
  in place of convergence. The problem is ours because this phase batches a uniform ensemble, making
  every update identical in fact as well as in expectation, which turns his random walk into a
  monotone approach. **State the cause; do not treat it as a dissolution.** Halting is a problem for
  the organism as much as for the simulation, and a divergence with an identified cause is still a
  divergence.
- **Cost rises while the verdict stands still.** Commitment 7 ties the error units' speed to
  $\lambda_{\max}(H)$, which grows as $\theta_u^2$. Under the delta-like prior the conjunction
  holds from the first update, at a demanded separation of $26$; every later update leaves the
  verdict as it is and makes each later inference costlier — $4{,}823$ where the flow halts, rising
  toward $7.9\times10^{6}$ at $\theta_u^\ast$. Across the plane's 33 both-condition cells the
  separation needed where the conjunction first holds is at most about $80$, against
  $4\times(3.5\times10^{4}$ to $3.6\times10^{7})$ at $\theta_u^\ast$.
- **Why $\theta_u^\ast$ stays the commitment, the conclusion unchanged and the reason reversed.**
  It is the **asymptote**, and it carries no tolerance. It used to stand because no self-contained
  halting mechanism was known. It now stands because the tolerance is **ad hoc**: a result reported
  at a halted $\theta_u$ would carry a number this study declines to fix, so predictions are given
  in closed form at the asymptote. The two old stopping rules are **retained and relabelled**, not
  deleted — $\theta_{\mathrm{crit}}=2.126$ and the one-update arrival still measure *where the
  conjunction is first met*, a fact about the shape of the update and explicitly not a halting rule.
- **With the level, and what is not derived.** What the alternatives level would have to claim
  concerns the slow flow, not how one inference ends: either its slow objective has a maximizer its
  flow reaches, or its verdict does not depend on growing a gain whose cost grows with it.
  **Neither is derived.** §5.1's one-dimension-per-level result is where an argument would start.
- **Neural plausibility, which is what this all answers to.** Commitment 7's separation, and tens of
  thousands of Euler steps per inference even where the conjunction first holds, are the cost the
  plausibility commitment has to answer for. This section is the argument `main.ipynb`'s *Integration
  cost and conditioning* defers to the outline, and the target O3's bare pointers were waiting on.
  *(Writer's note: F15's sharper figure — not within $0.1\%$ of $\theta_u^\ast$ after $5{,}000$
  updates — is **class (e)**, as at §4.6; no cell prints it. The approach-without-arrival is stated
  from $\tilde{\mathcal F}$'s flattening, which is an argument, not a measurement.)*
---
 
## 5.4 What an algorithmic account makes posable (about 120 words)

- **The claim.** Every question the three sections above turn on is **not posable at the
  computational level**. A computational theory states a goal and is silent on resources and
  representation, so the questions do not have wrong answers there — they have no answers, because
  they cannot be asked. Four instances, each naming where it arose:
  - **There is one posterior**, so there is **no choice between a delta and a normalized read-out**,
    and none of §3.6's costs is incurred by anything.
  - **$\theta_u^\ast$ is the answer however long the flow takes toward it**, so the gap §5.3 makes
    its subject — between where the verdict is reached and where learning would stop — does not open.
  - **There is no computation whose end could be asked about**, so halting is not a question about a
    theory of that kind, and a tolerance is not a candidate answer to it.
  - **The $\tfrac12$ tempering has no counterpart.** It comes from representing the utility level
    at finite $\sigma_S$, and §4.4 has to decompose $\Delta$ around it; a theory that fixes only
    the posterior has nothing there to decompose.
- **What that licenses, stated as an extension and not a new thesis.** The background's opening
  defines an algorithmic-level peculiarity as **a pattern the computational goal does not entail**.
  These four extend it by one step: **a question the computational level cannot pose**. Say that the
  definition extends; do not restate it as a second claim.
- **The counterargument, which should be raised here rather than left to a reader.**
  Resource-rational analysis brings costs into a computational-level analysis (Griffiths, Lieder &
  Goodman, 2015; Lieder & Griffiths, 2020), which looks like a direct denial. It is not: **it prices
  a process, and so still needs one specified.** The questions are posable there **because an
  algorithm has been supplied** — which is this section's point, arrived at from the other side.
- **Guard, and it is the whole risk of the section.** Do not say the computational level is
  **wrong**, and do not say these questions **refute RSA**. Neither follows, and both are the
  natural misreading: the claim is about what a level can be asked, not about what is true.
---
 
## 5.5 Limits (about 345 words, was §5.3)
 
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
- **The state space is truncated, and the truncation reshapes $\varphi_S^\ast$ itself.** $\zeta$
  ranges over $\mathbb R$; the grid carries $[-Z,Z]$, and $Z$ is stipulated with only a lower bound
  from the semantics, $\theta_L<Z$ (Text cell 3 §1, which separates it from $K$: refining $K$
  converges, $Z$ has nothing to converge to). **The mechanism is not a clipped tail.** $B$ is
  orthonormalized under the grid's own measure, so the **peak of $\varphi_S^\ast$** moves with $Z$.
  That peak is $\zeta_{k^\ast}$, so **§3.6's mode position criterion, $\zeta_{k^\ast}<\theta_L$,
  moves with $Z$ by definition**, and where it fails the conjunction fails too — sufficient, not
  equivalent, the first condition failing on its own in most configurations. Appendix A's ladder
  prints it: under the flat prior at $\Lambda=512$ the peak climbs $0.8516$ to $0.9981$ in $s$ over
  $Z\in\{5,10\}$ and crosses the cell's start between $Z=6$ and $7$, which is where both q criteria
  stop being met. The same peak is $q$'s
  mode (Eq. 12), so neither read-out escapes it. §4.5's band moves with $Z$; §5.2's $R^2$ does not, reading
  agreement of shape across items. **The general form: a mass above a fixed cut, and the peak's own
  location, both move with the half-width; a statistic comparing shapes across items does not.**
  And the
  dependence sits **below** the criterion: Eq. (24)'s limit doubles the field's component in
  $\operatorname{span}\{\zeta,\zeta^2\}$, a projection taken in $L^2([-Z,Z])$, so
  **reformulating the criterion cannot remove it** — only a projection under a fixed reference
  measure would, and that breaks the $B^{\mathsf T}WB=I$ that Eq. (B2) assumes. Owned rather than
  hedged, under §4.2's guard.
- The model is linear-Gaussian while $\varphi_L$ is clamped, so the recurrent dynamics are an
  implementation claim rather than a computational necessity.
- The relay secures locality at the cost of a fourth timescale, $\tau_r\le\tau_\varepsilon$
  (Eq. E6), which **inherits** $\theta_u^{-2}$ from the error units rather than imposing its own
  (F26); at equality $\mathcal F$ is monotone under *some* only (O6).
- $m=2$ is necessary at a flat inventory; **sufficiency is open**.
- Multidimensional semantics with sharp lexical boundaries is a declared non-compatibility.
- Not learned: $\Lambda$, $\theta_L$, $B$, $\mu_u$, the inventory.
- **Two stipulations of this phase, labelled as such and not built otherwise.** Results are
  reported at **uniform exposure** — $p(y)$ is not a variable of the implementation but is implicit
  in the batched sum, and no frequency-bearing version is built. And the inventory is taken to hold
  at least $\{\chi,\ker\chi\}$ for any entry; membership follows from exposure somewhere, not
  from exposure in a given experiment.
- Tier B facts recorded here, position reserved.
## 5.6 Predictions (about 130 words, was §5.4)
 
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
- **The lexical strength of a class, from its scale structure (§5.2).** A predicate anchored at its
  scale's own endpoint should behave as a hard entry — its fit putting no upper bound on $\Lambda$ —
  while one whose threshold depends on something the scale does not supply should require a finite
  one. That is the ordering the measurement of §5.2 shows, and it is testable on any class with an
  elicited prior and a degree estimate. **Stated as a prediction of H1, on which the dissertation
  takes no position** — it neither adopts nor rejects it, for the reason §5.2 gives: the comparison
  runs at one resolution and under commitments a later phase may drop. What is *not* predicted here is the old §5.2 trend — the monotone
  rise in the utility level's contribution as the cut approaches the endpoint, and its reversal under
  a sharp prior — which is withdrawn.
---
 
# 6. Conclusion (about 265 words)
 
1. A field-valued world state on a dense scale, with a soft lexical entry competing additively
   against the world prior in the same log-density — a placement of the prior the architecture
   commits to, not one its construction forces (§3.2) — admits a closed-form stationary point and a
   recurrent network that provably reaches it, with plasticity local at every $m$.
2. That network moves belief mass away from the *all* reading without representing any alternative,
   by amplifying the observed entry's own projection under a gain fixed by exposure. The effect
   therefore does not by itself diagnose a within-trial alternatives computation.
3. Where the prior leaves the all-region in the majority the network takes it out, and where the
   prior peaks inside the cell of *all* the network carries the peak outside it: in a single row of
   §4.4, and in 15 and 9 of the 121 cells of §4.5, under the two read-outs respectively, at the
   stipulated half-width and not at wider ones (§4.2's guard, sourced at both ends). In every
   one of those the shift criterion is met as well. The unconditioned counts are three of five
   priors and 33 cells under $q$, and the delta-like prior and 13 cells under the delta read-out
   §3.6 argues for — counts in which the prior is doing part of the work, which is why the
   conditioned ones lead. **What survives the change of read-out is the position criterion and not
   the shift**, and §5.1 reads that division as keyed to the level this architecture lacks.
   What a level representing competition among alternatives would change is what the
   network pays for that. On the plane the first condition's floor falls as the prior sharpens and
   the second's rises (§4.5), and a drain keyed to the alternative would not raise the second; and
   learning has no end short of a maximizer the slow flow never reaches. This dissertation specifies that level and
   proposes a design for it — resolution as a negative search branching binarily at each level,
   which keeps the dimension at one, the plasticity local, and the generative map affine enough to
   inherit the convergence proof — but does not derive its algebra, and says so in §5.1.
4. Independently, the same threshold semantics distinguishes scale classes by the entry each
   carries. Run on Xiang et al.'s (2022) own items, the class whose entry is fixed at the scale's own
   endpoint is fitted almost exactly and puts no upper bound on $\Lambda$, while the class whose
   threshold sits a resolution step inside the other endpoint requires a finite one and is where this
   model, like every model in their paper, is weakest. **That ordering runs in the direction the
   atomicity hypothesis of §5.2 predicts, and the dissertation takes no position on that hypothesis**
   — the comparison runs at a single resolution, and under architectural commitments §5.1 and §5.2
   themselves put in doubt, so what it establishes is a fact about this phase. The residual is
   reported and not explained.
---
 
## Sources for §5.2
 
**The entries live in `background_sections.md`'s reference list, which is the dissertation's only
one** (BG10, 2026-09-22): Xiang, Kennedy, Xu and Leffel (2022), Ronai and Xiang (2024), and
Kennedy (2007). They were duplicated here, and the duplicate had drifted — Kennedy's issue number
was missing from it. **This file keeps no entries of its own**; what follows is the note about
where the §5.1 citations went, which is a drafting instruction and not a list.

Citations redeployed into §5.1: Rooth (1985, 1992) and Kratzer & Shimoyama (2002) make the
alternative set depend on context rather than on the uttered expression; Katzir (2007) and
Fox & Spector (2018) treat competition as resolved by, rather than generative of, what is produced.
Both constrain where such a level would sit, and Katzir and Fox & Spector are also the right
citations for a structurally bounded alternative set.
 
## Open items
 
1. ~~The §5.2 magnitudes are not yet in the notebook.~~ **CLOSED 2026-09-22 (T2, T7).** Every number
   §5.2 quotes is printed by **Code Cell F** (Appendix F, cells 22–23 of `main.ipynb`), and a C6
   sweep over the rewritten section returns none without a printed source. The magnitudes are not
   the ones this item meant: the off-centre loading ratios, the utility contributions to posterior
   degree and the sign reversal under a sharp prior belonged to the prediction that F13 withdrew.
   What survives is the parity result, now restated at $n=4$ against printed $\kappa$, and what
   replaces the rest is the class comparison against Xiang et al.'s own items. The "drafted probe"
   was never found in the project or on the Desktop and is not needed.

2. ~~The background is being rewritten.~~ **DONE, and the pointers here were dangling
   (2026-09-22).** The rewrite under the three-question frame (Q1 locality; Q2 not one pass; Q3
   algorithmic-level peculiarities) is complete: the outline is `thesis_outline/background_sections.md`,
   whose 13-item drafting checklist is fully ticked. The two files this item used to name —
   `claude/background_revision_plan.md` and `background_sections_outline.md` — **do not exist**;
   the second is one of the superseded Desktop drafts `agent/agent.md` §1 lists as not maintained. Two
   consequences for this document, both applied long since: §5.1's sub-bullet on alternative-sensitive versus
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