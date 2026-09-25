# Central claim reframed by the three questions (opened 2026-09-24)

Working record under `agent/agent.md` §5.3. Fold into `agent/history.md` when it closes.

## 1. The user's instruction

> I think the thesis is broader than the one you specified. I think the thesis is better described
> by the three questions that opens the background section. We have particularly used scalar
> implicature and the current implementation as the main demonstration.

and, on the agent's three consequences (a question is not a thesis, so the thesis is the answers,
and the "is" of the second question is answered at the architecture's scope; the outline's central
claim disagrees with the background; the alternatives level becomes a proposal the first answer
motivates):

> correct. Those three things do follow. Go ahead.

## 2. Constraints the draft keeps

- **B12** (user, settled): "the constructive claim" names the position result, led by the cells
  whose baseline fails, the unconditioned counts after. §§4.1.4–4.1.5 cite it by that name, so the
  name stays, attached to the demonstration.
- **R2** and **B11**: the complexity saving leads the case for the level; the shift conjecture is
  second. **RVQ3**: the saving is a conditional design argument.
- The background's answers, cited and not restated: §2.2 (locality, the first answer), §2.6 (joint
  settlement at its true scope, the second), §1.5 (the demarcation problem), the opening's
  sub-questions (the third).

## 3. The draft (replaces `thesis_outline/sections_3-6.md`, lines 10–78)

**Approved by the user and applied 2026-09-24**, verbatim.

---

## Central claim

The dissertation's thesis is its answer to the three questions the background opens with, and one
architecture answers all three together, because the constraint it is built under generates the
rest (background, *Opening* and *Closing bridge*). **Scalar implicature, run through the present
implementation, is the main demonstration**; §4.2's scale classes against Xiang et al. (2022) are a
second and smaller one. The demonstration is what §§3–4 build and measure, and §5 says how far it
carries each answer.

**The thesis: three answers.**

1. **What computational constraint might scalar resolution obey?** Locality, in Bogacz's (2017) two
   senses, taken as a design constraint on the build and treated as **generative** rather than as a
   check applied afterwards (background §2.2). It is what the utility basis puts under strain at
   $m>1$, what Appendix E's relay buys back at the cost of a fourth timescale, and what motivates
   the binary branching of the level §5.1 proposes.
2. **Is scalar resolution one pass?** In this architecture the interpretation is **co-determined**:
   given the lexical entry, which the utterance clamps, the world belief and the utility state
   settle together as the one maximizer of an objective strictly concave in both, and no literal
   interpretation is settled on the entry alone and then revised (background §2.6). **State the
   scope with the answer, because the question asks more than one architecture can.** The entry
   itself exists before any pragmatic influence; and the answer is about how this architecture
   computes the interpretation, not about how no architecture could, nor about what human
   processing does. The question asks *is*; a demonstration answers *can be*.
3. **Can patterns observed in scalar resolution be understood as algorithmic-level
   peculiarities?** Yes, for the three the background names, each shown or argued in this
   implementation:
   - *whether strengthening needs a within-trial competition among alternatives* — it does not
     need one to occur (the demonstration below);
   - *what underlies extreme-favouring resolution on complete scales* — argued from parity: the
     extreme-favouring axis is the even coordinate of the utility basis (Appendix C §5), and at
     $n=4$ the two absolute entries differ in that coordinate alone (§4.2.4);
   - *how the semantic/pragmatic division is drawn* — the division's form is the problem: the
     threshold $\theta_L$ is a semantic convention fixed by the predicate, sitting inside one
     free-energy inference, and the joint settlement of the second answer is the fact §1.5's
     demarcation problem is answered from.

   §5.5 extends the third answer by one step: some questions are ones the computational level
   leaves unspecified and an algorithmic account settles.

**The main demonstration: scalar implicature.** A predictive-coding network organized under the
free-energy principle, in which the observed utterance's lexical entry is the only lexical quantity
represented and no alternative is consulted at any point in an inference pass, reproduces part of
the profile of scalar strengthening. Movement of belief mass away from the *all* reading therefore
does not, by itself, require a within-trial computation over alternatives. What produces the
movement is measured rather than assumed: the utility level amplifies the observed entry's own
low-rank projection of the prior–lexicon net (Eqs. 23–24), under a gain $\theta_u$ whose value is
fixed by cross-trial exposure rather than by anything about the current trial.

**What the demonstration shows, the constructive claim.** Say what the network carries before
saying how often, because a count is only worth something once the baseline is out of it. **Where
the prior leaves the all-region in the majority, the network takes it out; where the prior puts
the settled field's peak inside the cell of *all*, the network carries it outside.** Both are
§4.1.2's position criterion, read through the two read-outs of §3.6. Part D's delta-like prior is
the case in a single row (§4.1.4), and across the plane the network does it in a minority of the
cells whose baseline fails a position criterion, under $q$ and, in a subset of those, under the
delta read-out (§4.1.5). **In every one of those cells the shift criterion is met as well**, which
the cell counts rather than the prose asserts: where the network changes the position verdict it
meets both criteria, under either read-out. **The conditioned counts are figures at the stipulated
half-width**, and they cannot outlast the shift criterion as the grid widens (§4.1.5). §4.1.2's
guard governs this claim as it governs the counts below it.

The unconditioned counts belong in the claim too, and only with what they include. Both conditions
hold under three of the five priors at $\Lambda=512$, the three with the most prior mass on the
all-region (§4.1.4), and across the plane in a band whose shape two opposed floors set (§4.1.5).
Under the delta read-out the same two counts shrink to the delta-like prior alone and a smaller band,
since **what survives the change of read-out is the position criterion and what does not is the
shift** (§3.6's position). **Each of these is a count in which the baseline is doing part of the
work**, which is why they stand after the paragraph above and not in place of it.

**What the first answer motivates: a proposed alternatives level.** It is a proposal the thesis
motivates, not a second thesis, and its case does not rest on the criterion failing (R2). It rests
on what such a level would save:
- branching logarithmic in the predicate's granularity, if its cuts stay balanced at every depth
  (§5.1: a conditional design argument, not a derived bound);
- one dimension per level, so plasticity is local without the relay;
- an affine generative map that keeps the convergence proof;
- a read-out that needs no normalization across the scale (§5.1);
- an end to learning short of a maximizer the slow flow never reaches, which the present
  architecture lacks (§5.3; argued, not derived);
- and, on the plane, a drain keyed to the alternative rather than to prior mass on the all-region,
  which would not carry the second condition's floor up as the first's falls (§4.1.5's floors;
  argued in §5.1, not measured).

**How the two criteria are read.** §5.1 states the reading, as a conjecture and not a measurement:
**the position criterion is what this architecture comes closest to supplying — one operation on
the settled field, locating its peak (§5.6) — and consistent shift is what the absent level would
supply** — with neither standing as the criterion of strengthening on its own, which is why §4.1.2
takes the conjunction. It is argued from §4.1.5's opposed floors and §4.1.4's rows, under the guard
§4.1.2 sets on $n$ and $Z$, and nothing here measures a level that is not built. **It is the second
motivation and not the first.** The case for the level is the complexity it would save (R2), a
conditional design argument from the construction that needs no datum; the conjecture is about
what *this* architecture cannot deliver, and whether strengthening must be a shift at all rests on
a baseline that is a construct in every account that has one (§5.1). Do not let the order slip.

**Such a level is compatible with this architecture; it is specified here and not built.** What
the dissertation contributes in its place is that specification: the construction the model works
under states exactly what any additional level must supply — a state space, a position in the
chain, generative maps in both directions, and a convergence argument — and §5.1 discharges as much
of it as the present results determine, naming precisely what is left.

**Standing qualification, carried into §5.** Neither the three answers nor the demonstration say
that human scalar strengthening lacks a within-trial alternatives computation, and nothing in this
implementation could show it: the model has no alternatives space to begin with. The claims are
about what the *effect* requires, and about what one architecture shows can be the case, not about
what human processing contains.

---

## 4. What else would follow, not in the draft

- **§6 Conclusion** is organized by result (architecture; effect; position; scale classes), not by
  the three answers. Under this framing it should close on them. Not drafted.
- **Tier A** ("Why it is load-bearing") has no row for the three answers or for joint settlement;
  the background carries them.
- **`agent/decisions.md`**: a new entry recording the framing (the user's), and a finding under
  B12 that its object is now the demonstration's result.

## 5. Tasks

- [x] CC1 (2026-09-24): draft written (§3 above) and set out to the user.
- [x] CC2 (2026-09-24): approved; applied verbatim to `sections_3-6.md`, replacing the old central
      claim through the rule before *Scope decision*; read back.
- [x] CC3 (2026-09-24): records — decision C10, B12's finding, `revisions.md` §20.
- [x] CC5 (2026-09-24): the standing qualification restated positively at its three sites
      (central claim, §5.1's closing bullet, background closing bridge), at the user's
      agreement; §6 will not repeat it (user).
- [ ] CC4: §6 Conclusion — the plan goes to the user before any drafting (user's instruction:
      "Before you draft the conclusion, tell me what you plan to say first").

## 6. §6 draft (pending the user's review; not applied)

Plan agreed with the user: organized by the three answers; about 350 words (user approved the
length); the Xiang comparison under extreme-favouring (user); no standing qualification (user: made
elsewhere); the second answer **named joint settlement** (user), with the clamped-entry scope clause
kept and the staging and human-processing clauses left to the central claim and §5.1.

One architecture, built under the locality constraint, answers the background's three questions
together, and scalar implicature is where it is shown.

1. **The constraint.** Under locality, a field-valued world state with a soft lexical entry
   competing additively against the world prior in one log-density (a placement the architecture
   commits to, §3.2) admits a closed-form stationary point and a recurrent network that provably
   reaches it. Plasticity is local at $m=1$, and at every $m$ with Appendix E's relay, whose added
   timescale the proof does not cover. The same constraint points the next level toward binary
   branching.
2. **Joint settlement.** Given the entry the utterance clamps, the world belief and the utility
   state settle together as the one maximizer of a single objective; no literal interpretation is
   settled first and then revised. The entry itself precedes pragmatic influence; what settles
   jointly is everything downstream of it.
3. **Three patterns, as algorithmic-level peculiarities.**
   - *Strengthening without alternatives.* The network moves belief mass off the *all* reading while
     representing no alternative, by amplifying the observed entry's own projection under a gain
     fixed by exposure; any implicature it carries is conventionalized. Where the prior peaks inside
     the cell of *all*, it carries the peak outside — in one row of §4.1.4 and a band of the plane
     (§4.1.5), at the stipulated half-width — and meets the shift criterion there too. The position
     criterion survives the change of read-out; the shift does not.
   - *Extreme-favouring on complete scales*, argued from parity: the utility basis's even
     coordinate. On Xiang et al.'s (2022) items, the class fixed at its scale's own endpoint puts no
     upper bound on $\Lambda$ and the other requires a finite one, the direction the atomicity
     hypothesis predicts; the dissertation takes no position on it, and the residual is reported,
     not explained.
   - *The semantic/pragmatic division.* $\theta_L$ is a semantic convention inside one free-energy
     inference, and §5.5's questions are ones the computational level leaves unspecified.
4. **The proposal.** A level representing competition among alternatives is specified, not built:
   first for what it would save — logarithmic branching if its cuts stay balanced, one dimension per
   level, locality without the relay, an affine map that keeps the convergence proof — and second for the reading that
   consistent shift is what it would supply. Its algebra is not derived (§5.1).
