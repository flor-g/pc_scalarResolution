Background sections outline · MD
# Outline for the dissertation background
 
The live plan for this document is `thesis_outline/revisions.md`; its history is in §16 there.
The precision/wonkiness arc of earlier drafts survives only as contrast.

---
 
## Scale and argumentative shape
 
- **Target length: approximately 4,160 words.** The budget follows what the sections have to carry
  (raise history: `revisions.md` §16).
- **Opening (about 245 words).** The explanandum; the three questions the dissertation answers; and
  Marr's levels, fixed by contrast with RSA.
- **Part I — What scalar resolution is asked to explain, and why the existing division does not
  settle it (about 2,115 words).** Establishes two things §§3–6 need and one they dissolve: that
  every existing account computes strengthening over a *represented alternative set*; that the
  accounts deriving it *from the prior* carry a documented liability; and that the debates over
  which level a pattern belongs to share a presupposition about staging.
- **Part II — Predictive coding, its commitments, and the constraint that generates the answers
  (about 1,680 words).** Only the parts the model uses, organized around the framework's three
  commitments, with locality carrying the most weight because it is Q1's answer.
- **Closing bridge (about 120 words).** The three questions restated, and the standing qualification.
### Terminological corrections carried through the dissertation
 
- Spell the author's name **Judith Degen**, not *Degan*.
- A slide reference attributing *Predicting pragmatic reasoning in language games* to "Franke and
  Goodman (2012)" duplicates/misattributes Frank and Goodman (2012). For recursive/game-theoretic
  Quantity reasoning use **Franke (2011)**; for the canonical Bayesian RSA architecture use
  **Frank and Goodman (2012)**, **Goodman and Stuhlmüller (2013)**, and **Goodman and Frank (2016)**.
- The alternatives-level map introduced in §5.1 is **$g_a$**, lowercase, because $\varphi_a$ has the
  same type as $\chi$. The background does not use the notation; it is recorded here so the two
  documents agree.
---
 
# Opening: three questions, and the level they are asked at (about 245 words)
 
- **Main claim to establish:** Scalar interpretation is a test case for theories of inference
  because the listener must integrate lexical meaning, alternatives, assumptions about the speaker,
  and prior world knowledge — and because the field disagrees not only about the answer but about
  what kind of answer is wanted.
- **Material to include, in three moves.**
  1. *The explanandum.* Introduce *some* as semantically compatible with *all* but often interpreted
     as *some but not all*.
  2. *The three questions*, stated as questions and in this order, so the reader knows from the
     first page that one architecture answers all three:
     - **What computational constraint(s) might scalar resolution obey?**
     - **Is scalar resolution one pass?**
     - **Can patterns observed in scalar resolution be understood as peculiarities arising at the
       algorithmic rather than the computational level?** — with the three sub-questions named:
       whether alternative competition is necessary to produce strengthening and whether it is a
       separate module from world-prior inference; what mechanism underlies extreme-favouring
       resolution for complete-scale inference; and how the semantic/pragmatic division is drawn to
       begin with.
  3. *The level distinction, fixed by contrast rather than by definition.* **A computational-level
     theory states a goal and is silent on compute-resource constraints.** RSA is the example, and
     Part I introduces it anyway: it specifies *what* is recovered — a posterior over states, by
     inversion of a speaker model — and says nothing about what resources the recovery may use, how
     the quantities are represented, or what any one unit may see. **An algorithmic-level theory
     specifies representations and a process running under those constraints**: message passing,
     state and error units, locality, a basis of fixed dimension. A pattern is an algorithmic-level
     peculiarity **when the computational goal does not entail it**. §5.4 extends that definition
     by one step, and the clause belongs here rather than there: a question can fail to be
     **posable** at the computational level at all — not answered wrongly, but unaskable, because a
     theory that fixes only the goal supplies nothing for the question to be about. Name the
     extension in a clause and leave its instances to §5.4. **Never write that the computational
     level is wrong, or that such a question refutes RSA**; neither follows, and both are the
     natural misreading.
- **Evidence and citations:** Marr (1982) for the levels; Spratling (2013) and Aitchison and Lengyel
  (2017) for the observation that predictive-coding and Bayesian claims are routinely pitched a
  level above their evidence. The classical derivation begins with Gricean Quantity reasoning
  (Grice, 1975); contemporary probabilistic and grammatical implementations differ over where and
  how enrichment occurs (Goodman & Frank, 2016; Chierchia et al., 2012).
- **Guard against overclaiming:** Do not announce that either literature proves neural predictive
  coding. Do not promise that the dissertation settles the semantic/pragmatic assignment question —
  it argues the question's *form* is the problem.
- **Drafting note.** Resist making this an abstract exposition of Marr. The RSA contrast does the
  work in two sentences; a reader who knows RSA knows what a computational-level theory is as soon
  as it is named as one.
---
 
# Part I. What scalar resolution is asked to explain, and why the existing division does not settle it (about 2,115 words)
 
## 1.1 Scalar implicature and the target explanandum (about 200 words)
 
- **Main claim to establish:** The inference from *some (p)* to *not all (p)* is defeasible but
  systematic, and therefore cannot simply be written into the truth-conditional meaning of *some*
  without losing its context sensitivity.
- **Material to include:**
  - A minimal scale \(\langle\textit{some},\textit{all}\rangle\).
  - The literal/prejacent meaning \(\exists x\,P(x)\) against the strengthened interpretation
    \(\exists x\,P(x)\wedge\neg\forall x\,P(x)\).
  - The Gricean reconstruction: a better-informed speaker who could truthfully have uttered the
    stronger alternative *all* but chose *some* licenses the inference that *all* is not assertable
    (Grice, 1975).
  - The ignorance inference ("the speaker does not know that all") distinguished from the scalar
    inference proper ("the speaker believes that not all"), since grammatical accounts treat the
    latter as exhaustification rather than as ordinary mind-reading (Chierchia, 2017).
  - **New, and load-bearing for §4.1.2 of the proposal:** this dissertation's explanandum is
    **graded** — movement of belief mass off the *all* reading — rather than a truth-value judgment.
    Say so here, because §4.1.2's two-condition criterion is otherwise a stipulation arriving without
    motivation.
  - **New, one sentence:** flag *defeasibility* as one of the criteria by which patterns are sorted
    into semantics or pragmatics, so the reader meets it once before §1.5 questions it.
- **Counterargument to anticipate:** A default lexical meaning *some but not all* is simpler.
  Answer that cancellation and embedded readings require a mechanism that preserves the weak meaning
  and determines where strengthening applies (Chierchia et al., 2012).
- **Transition:** RSA makes the Gricean reasoning explicit as probabilistic Bayesian inference.
## 1.2 RSA: a computational-level theory of pragmatic interpretation (about 300 words)
 
- **Main claim to establish:** RSA formalizes pragmatic interpretation as Bayesian inversion of a
  speaker model, making the listener's posterior jointly sensitive to semantics, **alternatives**,
  utterance cost, speaker optimality, and the world prior (Frank & Goodman, 2012;
  Goodman & Frank, 2016).
- **Core equations, with notation fixed for the rest of the dissertation:**
  - Literal listener: \(L_0(s\mid u)\propto \llbracket u\rrbracket(s)P(s)\).
  - Pragmatic speaker: \(S_1(u\mid s)\propto \exp\{\alpha_{\mathrm{rsa}}[\log L_0(s\mid u)-C(u)]\}\).
  - Pragmatic listener: \(L_1(s\mid u)\propto S_1(u\mid s)P(s)\).
  - \(\alpha_{\mathrm{rsa}}\) controls soft-maximal speaker choice; \(C(u)\) penalizes costly
    forms. **The subscript is not decoration** (Q8, settled by the user 2026-09-21): §§4.1.5 and 5.2
    use a bare \(\alpha\) for the concentration of the prior \(\mathrm{Beta}(\alpha,1)\), and the
    two quantities meet in §1.3's override-law sentence. Every RSA \(\alpha\) in the dissertation
    carries the subscript; the Beta concentration keeps the bare symbol, as the notebooks write it. The
    "informativeness" term is the log probability that the literal listener recovers the intended
    state, not an unanalyzed general-purpose utility (Frank & Goodman, 2012; Goodman & Frank, 2016).
- **The point to make visible, which the previous draft left implicit.** The alternative set enters
  through the **normalization of \(S_1\)**: the sum runs over utterances the speaker did not
  produce, so the listener's posterior at any state depends on expressions that were never uttered.
  **That dependency is the quantity §§3–6 remove**, and §5.1's standing qualification is its
  negation — no term in the model's objective involves any unobserved utterance. Unless this is
  stated plainly here, the proposal's central negative result reads as a curiosity rather than as a
  departure from a shared commitment.
- **This subsection does double duty.** It is also the opening's worked example of a
  computational-level theory: RSA specifies the goal and the quantities, and is silent about what
  computes them or what a unit may see. Say so in one sentence and do not labour it.
- **How scalar implicature arises:** In a state where *all* is true, a cooperative speaker has a more
  informative alternative than *some*; hearing *some* therefore reduces the posterior probability of
  the all-state (Goodman & Stuhlmüller, 2013).
- **Evidence/reasoning:** RSA has quantitatively captured pragmatic effects in reference games and
  knowledge-sensitive implicature tasks, which is why it is a serious baseline rather than a straw
  theory (Frank & Goodman, 2012; Goodman & Stuhlmüller, 2013).
- **Counterargument to keep, trimmed:** *"The prior can simply be fitted."* An independently elicited
  prior yields a substantive empirical prediction; replacing it post hoc with a flatter one would
  describe the data without explaining when or why flattening occurs. This is what makes §1.3's
  design a real test.
- **Counterargument to cut:** the "RSA is already recursive, so why add another iterative mechanism?"
  exchange. It defended the superseded precision thesis and serves nothing now.
- **Transition:** The dependency on \(P(s)\) creates a specific and documented failure.
## 1.3 Strengthening derived from the prior, and its two liabilities (about 440 words)
 
*Merges the previous draft's §1.3 and §1.4 and promotes the Cremers material out of §1.5. The
section's function has changed: it is no longer the setup for a wonkiness mechanism, but the first
of the two empirical anchors §5.1 uses.*
 
- **Main claim to establish:** Deriving scalar strengthening from the listener's prior carries two
  liabilities, one from the size of the predicted prior effect and one from its direction.
**Beat 1 — prior-insensitivity (Degen, Tessler & Goodman, 2015), about 150 words.**
 
- If nearly all marbles normally sink, prior mass on the all-state approaches one. Because the weak
  semantics of *some* removes only the zero-state and competition with *all* targets only the
  all-state, a sufficiently extreme prior can dominate \(L_1\). Two sentences; do not re-derive at
  length.
- Degen et al. independently elicited priors over how many objects undergo events such as sinking.
  After participants heard quantified utterances the prior still had a detectable effect, but far
  smaller than standard RSA predicts: even high-prior items retained low posterior probability for
  the all-state after *some*.
- Filler conditions tracked prior knowledge, arguing against the explanation that participants simply
  ignored world knowledge.
- **The redeployment.** Human strengthening is **robust against prior concentration**. In this
  model the strengthened reading stays a majority under a concentrated prior only above a floor in
  lexical strength, and that floor rises with the concentration (§4.1.5). Flag forward to §4.1.5 for the
  floor and to §5.1, which argues that a drain keyed to the alternative would not carry it up.
- *Counterargument:* numerical and slider judgments are noisy. The convergence of expected-number
  judgments, all-state judgments, and separate normality judgments is nevertheless stronger than
  reliance on one dependent measure.
**Beat 2 — wRSA as the response, the inverted parallel, and what RSA has of the commitment (about 175 words).**
 
- A latent wonkiness variable \(w\); under the usual setting \(P(s\mid w)\) is the elicited world
  prior, under the wonky setting a uniform back-off. The pragmatic listener becomes
  \(L_1(s,w\mid u)\propto S_1(u\mid s,w)P(s\mid w)P(w)\). Improved fit, and the qualitative U-shaped
  normality judgments for *some*.
- **Its function here is contrast, not target.** wRSA keeps Bayesian reasoning by making **the
  prior** defeasible against the utterance. This dissertation's architecture makes **the lexical
  entry** defeasible against the prior — finite lexical strength \(\Lambda\), §3.2 — and §4.1.5
  quantifies where that override bites. Two sentences, no verdict, forward pointer only.
- **What RSA has of the commitment, and what it lacks (R18; about 50 words).** §3.2 states as a
  commitment that the prior and the lexical entry meet as counterforces at one node. Foreshadow it
  against §1.2's three equations:
  - *RSA has the hard limit.* As \(\Lambda\to\infty\) the model's field for the prior restricted by the
    entry is \(\log L_0\) up to its normalizer (§3.2). One clause, a forward pointer.
  - *RSA has a choice of where the prior enters, and makes it the other way.* \(P(s)\) enters \(L_0\)
    and enters again in \(L_1\propto S_1(u\mid s)P(s)\). In this architecture the prior enters once,
    and the commitment is which map carries it (§3.2). One sentence, stated as a contrast.
  - *RSA has no single counterpart to a finite \(\Lambda\).* Its ways of letting prior and semantics
    trade off use a **latent variable** rather than a strength: lexical uncertainty (Potts et al.,
    2016), threshold uncertainty, where the listener infers the cut jointly with the state
    (Lassiter & Goodman, 2017; the basis of Xiang et al.'s (2022) LG model, §1.7), and wonkiness,
    above. **Nothing in RSA plays the role of the override law** (§4.1.5, Eq. 41): the lexical
    strength needed to hold the entry against the prior grows linearly in the prior's concentration,
    at a rate set by the logarithm of the predicate's granularity. That is the part of the commitment
    with no parallel, and the one worth the words. **State the law in words here, not in symbols:**
    §4.1.5 writes it \(\Lambda_{\mathrm{crit}}\approx\alpha\log2n\), whose \(\alpha\) is the Beta
    concentration and not §1.2's \(\alpha_{\mathrm{rsa}}\) (Q8), and the background has defined
    neither the family nor \(n\).
- **The projection parallel, foreshadowed and warned against in one breath (R19; about 25 words).**
  The model's utility level reads a fixed linear projection of the same log quantity \(S_1\) reads,
  \(\log L_0\) (§3.3). Say so here, and warn in the same sentence that a projection does not imply an
  equivalence and that forgetting the difference is dangerous: the projection discards the constant
  component, which is exactly where \(L_0\)'s normalizer lives (§3.3 gives the exact form). Two guards
  for the writer:
  - Say that the **projection** discards the component, never that the model does. The model is
    not blind to it (§3.3).
  - This is how §2.1's instruction not to equate the mapping with RSA's social recursion is
    honoured here: by making the disanalogy precise, not by leaving the parallel out.
- **Cut entirely** (Entry 3a): the internal-limitations list (what exactly is revised; uniform
  back-off as one option among many; \(P(w)=.5\) as a fitted choice), and the binary-versus-graded
  counterargument. All of it existed to motivate a continuous precision parameter this architecture
  does not have.
**Beat 3 — anti-exhaustivity (Cremers, Wilcox & Spector, 2023), about 90 words.**
 
- Deriving strengthening from the prior implies that under a sufficiently skewed prior, baseline RSA
  can make the pragmatic listener **more** confident in the excluded state than the literal listener
  is. Human participants do not show this.
- State that it does not by itself establish a covert grammatical operator, and that it is a second,
  independent reason to ask whether the computation of strengthening should reference the listener's
  current prior at all.
- **Forward pointer, stated without embarrassment (R7, P-9).** §4.1.4 reports the same direction in
  this model, as a property of its read-out \(q\) against its literal listener. Give both counts: it
  appears under all four priors that have a row at the weaker lexical strength, and under two of
  five at the stronger, where raising the strength removes it under two priors and enlarges it under
  the other two. Name what carries it: the tempering, the halving of the settled log-density that §4.1.1's tempered
  control isolates (§4.1.4). Call it a parallel in direction, not a
  shared liability, since the mechanisms differ. Do not treat it as corroboration, and do not say
  what would avoid it: §5.1 no longer uses it (R2).
- **Transition:** The grammatical tradition computes strengthening over alternatives without
  consulting the prior at all.
## 1.4 The Chierchia line: local exhaustification and comparison among strengthened parses (about 360 words)
 
- **Main claim to establish:** On the grammatical approach, scalar alternatives are compositionally
  represented and a covert exhaustivity operator \(\mathsf{Exh}\) (or \(O\)) can be inserted at
  different syntactic/semantic locations. Scalar resolution therefore involves selecting among
  multiple candidate logical forms (Chierchia et al., 2012; Chierchia, 2017).
- **Mechanism to explain:**
  - For a prejacent \(p\) and alternatives \(Alt(p)\), \(\mathsf{Exh}(p)\) asserts \(p\) and negates
    the relevant excludable alternatives. For *some*, negating *all* yields the strengthened truth
    conditions.
  - Because \(\mathsf{Exh}\) is an LF operator it may apply globally or inside an embedded
    constituent, and different insertion sites may produce different truth conditions.
  - Chierchia's parsing condition favours uses of \(O\) that add information rather than weaken the
    whole sentence, unless a locally weakened parse is required to avoid contradiction
    (Chierchia, 2017). Fox and Spector (2018) develop economy constraints on embedded
    exhaustification formally.
- **One worked locality contrast:** in a conditional, exhaustifying a scalar expression in the
  consequent can strengthen the whole conditional, whereas exhaustifying the antecedent may weaken
  it because entailment reverses in a downward-entailing position. A continuation can nevertheless
  force the otherwise disfavoured local reading by making the unexhaustified interpretation
  contradictory (Chierchia, 2017).
- **The property that matters for the dissertation, named separately from locality.** \(\mathsf{Exh}\)
  applies at logical form, so **its output does not depend on the listener's current probabilistic
  beliefs about the world.** That is a different property from the locality facts above, and it is
  the one §1.3's two liabilities bear on.
- **The experimental record — kept at weight, not summarized away.** This is Q3c's evidence base and
  the previous draft's instinct to compress it was wrong.
  - Hurford-type disjunctions and contextually supported conditionals motivate subsentential
    exhaustification (Chierchia et al., 2012).
  - Geurts and Pouscoulous (2009) found little evidence for freely available embedded implicatures
    and warned that some tasks inflate strengthening; Clifton and Dube (2010) found embedded
    strengthening with a more sensitive multiple-choice task; Chemla and Spector (2011) reported
    broader experimental evidence for embedded readings; Ippolito (2010) argues the
    Geurts–Pouscoulous findings resist localist treatment even when supplemented with a formal
    account of when an embedded implicature is preferred.
  - Oddness effects in downward-entailing environments have been argued to follow from embedded,
    grammatically mandated exhaustification (Magri, 2011).
  - **Say what this record shows, plainly:** two decades of task-sensitive results that have not
    converged on an assignment. Our position on who is right is reserved (Entry 3b); the fact that
    the dispute has not settled is what §1.5 uses.
- **Counterarguments and balanced response:**
  - Local readings do not uniquely prove a covert grammatical operator: compositional
    lexical-uncertainty RSA derives embedded implicatures pragmatically by allowing uncertainty about
    lexical meanings (Potts et al., 2016).
  - Experimental incidence varies with task and context, so avoid saying local strengthening is
    automatic or cost-free.
- **Wording correction to carry:** rather than saying the parser "chooses the path with the strongest
  consequences", say **candidate exhaustification sites are compared, and all else equal,
  interpretations that add information are preferred; weakening is licensed when required for
  coherence** (Chierchia, 2017).
- **Delete:** the trailing sub-bullet directing a connection to "section 3's move to distinctly
  represent alternative-sensitive utility and world-sensitive utility". The architecture has one
  utility level.
- **Transition:** The dispute has a shape worth examining before its content.
## 1.5 The demarcation problem, and what it presupposes (about 285 words) — DRAFTED
 
*Prose, not an outline. Edit directly.*
 
> The debates of §1.4 assume that a pattern of interpretation belongs either to the semantics or to
> the pragmatics, and that evidence can settle which. Both halves of that assumption bear
> examination.
>
> Three criteria are in use, and they are usually run together: **truth-conditionality** (semantic
> content bears on the sentence's truth conditions), **conventionality** (semantic content is fixed
> by linguistic convention rather than by conversational reasoning), and **constancy** (semantic
> content does not vary with context). They cross-cut. Of the meaning types the three jointly
> classify, only literal content and conversational implicature receive uniform verdicts; every
> intermediate type — indexicals, pragmatic enrichment, expressive content — is sorted one way by
> one criterion and the other way by another (Gutzmann, 2021). Approaching the boundary from the
> theoretical side, Jaszczolt (2012) likewise finds no clear-cut line, but rather frameworks drawing
> different lines according to prior commitments about compositionality and psychological reality.
>
> Scalar strengthening sits in the contested region. It is cancellable and conversationally derived,
> which conventionality counts as pragmatic; it has been argued to be truth-conditionally active
> under embedding (§1.4), which truth-conditionality would count as semantic. Sauerland (2012)
> accordingly presents pragmatic, lexical and grammatical treatments as three live options for one
> phenomenon.
>
> This dissertation reserves its position on which treatment is correct. What it takes from the
> dispute is the **form the dispute shares**: to assign a pattern to one of two levels is to
> presuppose that the levels are stages — a semantic value computed, then a pragmatic one computed
> on it. Every criterion above inherits that presupposition rather than arguing for it. Part II
> supplies an architecture in which the interpretation is not staged that way, and §5.1 returns to
> what follows.
 
- **Drafting notes.** "Has been argued to be truth-conditionally active" rather than "is", because
  §1.4's evidence is contested and Entry 2a forbids borrowing the stronger reading. The closing
  paragraph states the presupposition and stops: the dissolution belongs to §5.1 and §6, and stating
  it here spends the result before the model that earns it has been introduced.
- **Position reserved** on Gutzmann's own resolution (abandon constancy; prefer conventionality).
  The dissertation needs the cross-cutting, not the remedy.
## 1.6 Alternatives: where they come from, and what bounds them (about 180 words)
 
*New. Every work below is used in §5.1 and none was introduced in the previous draft; composition
guide Entry 5b requires a sourced name to be cited before first use.*
 
- **Main claim to establish:** An alternative set is not read off the uttered expression, and it is
  not free either. Both facts constrain where a level representing competition could sit.
- **Four moves, one or two sentences each:**
  1. **Context-dependence.** Alternative sets depend on context rather than on the uttered
     expression alone (Rooth, 1985, 1992; Kratzer & Shimoyama, 2002).
  2. **Structural bounding.** Competition is resolved by, rather than generative of, what is
     produced, and the candidate set is structurally bounded rather than arbitrary (Katzir, 2007;
     Fox & Spector, 2018). This is also what makes a *finite inventory at a level* a coherent object
     for §5.1's cascade to branch over.
  3. **Accessibility versus relevance.** Alternative *accessibility* behaves like an exposure-indexed
     quantity, while contextual *relevance* governs inference rates (Ronai & Xiang, 2024). **This is
     the distinction §5.1 needs**: the architecture can carry an exposure-indexed quantity in a
     cross-trial weight, and cannot carry a within-trial one at all.
  4. **The nearest existing proposal to an uncomputed inference.** Levinson's (2000) default
     generalized conversational implicatures, differing in that a default is still keyed to an
     alternatives set at the utterance and is defeasible within the trial.
- **Guard:** do not present move 4 as the dissertation's position. §5.1 argues that its own gain is
  *conventionalized rather than computed*, which is a stronger claim than a default, and the
  difference is the point.
## 1.7 Scale structure, thresholds, and extreme-favouring interpretation (about 190 words)
 
*New. Supplies the entire literature of §4.2 and §5.2, motivates a continuous state space in §3.2, and earns the
project's "scalar vagueness resolution" keyword.*
 
- **Main claim to establish:** Where a predicate's threshold sits on its scale is a matter of
  semantic convention, and the conventions differ systematically by scale structure.
- **Material to include:**
  - Degree semantics: a gradable predicate relates a degree to a threshold.
  - **Maximum-standard absolute adjectives have closed scales and conventional endpoint standards;
    relative adjectives have open scales and context-dependent thresholds** (Kennedy, 2007).
  - The empirical profile: maximum-standard absolute adjectives elicit categorical responses
    concentrated near the scalar maximum, minimum-standard ones responses spread over every
    non-minimal position, and relative adjectives a roughly constant increase across scale positions
    (Xiang, Kennedy, Xu & Leffel, 2022).
  - **The contrast is between novel and familiar objects, and it is not a contrast in prior
    sharpness.** The between-class difference is larger for the geometric shapes than for the
    familiar artifacts. But the shape condition is impoverished in *world knowledge*, not in prior
    **concentration**: Xiang et al. report that the elicited priors for artifacts are the **less**
    categorical ones (9:19), and their own elicited priors bear it out. State the manipulation as
    novel versus familiar, and say which way the elicited priors actually go — an earlier draft of
    this bullet and of the comparison had it backwards.
  - Xiang et al.'s own conclusion: Bayesian pragmatics models what is *communicated* well
    (\(R^2=.78\)–\(.82\)) but threshold judgments poorly (\(R^2=.36\)–\(.63\)), especially for
    absolute adjectives, so Bayesian reasoning must be combined with the semantic conventions
    governing thresholds.
- **State Q3b as the open question this leaves:** *what mechanism produces endpoint orientation?*
  **Do not answer it here**, and do not promise an answer later: §§4.2 and 5.2 **take it up**. Parity fixes
  an entry's width loading, but the contribution that is actually measured is carried by the tilt,
  and under learning the prior's width enters too — so "the comparison answers it from the parity structure of
  the utility basis" claims more than §§4.2 and 5.2 can carry. The background's job is to make the question
  askable.
- **Connection to make explicit:** quantifiers and gradable adjectives share a scale structure, which
  is what licenses §3.2's treatment of the world state as a proportion on a dense scale rather than
  a finite set of categories.
## 1.8 Part I synthesis: three questions, and an impasse (about 160 words)
 
- **Main claim to establish:** The traditions converge on a computational requirement, disagree about
  representational details, and share an assumption none of them defends.
- **Synthesis to state:**
  > Every account surveyed computes strengthening over a represented alternative set, and differs
  > over where the computation sits and what it is sensitive to. The accounts deriving it from the
  > listener's prior inherit a liability the grammatical line avoids; the grammatical line's own
  > assignment evidence has not converged. What none of them tests is whether the alternative set is
  > required for the *effect*, what fixes the scale's structure, or whether the two-level sorting the
  > debates perform is well posed.
- **Counterargument to anticipate:** Neither a recursive formal definition nor multiple LFs shows
  that the human processor literally cycles through discrete stages in real time. Keep the
  conclusion at the level of what the theories assume, not what processing does.
- **Bridge to Part II:** predictive coding is introduced not as a mechanism for revising confidence,
  but as the framework in which an inference architecture can be **built under an explicit
  implementation constraint** — and in which a prior and a lexical entry can be made to compete in a
  single density rather than in sequence.
---
 
# Part II. Predictive coding, its commitments, and the constraint that generates the answers (about 1,680 words)
 
## 2.1 FEP, generative models, and Bayesian model inversion (about 235 words)
 
- **Main claim to establish:** The free-energy principle provides a variational formulation of how an
  adaptive system can maintain a generative model and infer hidden causes of observations;
  predictive coding is one proposed process implementation of that inference (Friston, 2008, 2010;
  Bogacz, 2017).
- **Concepts to define:** observation \(u\), hidden cause \(s\), prior \(p(s)\), generative mapping
  \(p(u\mid s)\), posterior \(p(s\mid u)\). "Generative" means specifying how latent causes
  probabilistically produce observations; perception inverts that mapping.
- **Relevance to the proposal:** world state latent, utterance observed; \(p(u\mid s)\) the top-down
  direction and \(p(s\mid u)\) model inversion.
- **Recap the levels in one sentence** and state which the dissertation's claims sit at: a
  **free-energy-normative** claim (an objective the system can be read as approximating); a
  **predictive-coding-style algorithmic** claim (an error-driven, locally-plastic update scheme that
  could implement it); and a **neurally-implemented circuit** claim (a mapping onto cell types,
  layers, connectivity). The dissertation makes claims at the first two and declines the third,
  **with one named exception** — §2.7 gives the reason and the exception.
- **One sentence on what the algorithmic claim costs, because it is not free.** That claim carries
  the architecture's **commitment 7** (§3.4) — one of the model's *own* commitments, numbered in
  its own list, and **not** one of §2.2's three canonical ones; say which list once, here, because
  the two are otherwise a numbering trap. The error units are held to
  \(\tau_\varepsilon\le\tau_\varphi/(4\lambda_{\max}(H))\), a separation that tightens as
  \(\theta_u^2\), and what it secures, with the error units' silent start, is the *monotone* rise of
  \(\mathcal F\) rather than convergence. It is **measured**, not assumed, and §5.3 prices it as a liability of the
  plausibility claim rather than as a detail of the schedule. One sentence and a forward pointer:
  the background defines neither \(H\) nor \(\theta_u\), and §2.6 is where the ordering it
  sharpens is stated.
- **Counterargument/qualification:** do not equate this mapping with RSA's social recursion.
  Bidirectional generative/inference flow is not nested reasoning about a speaker reasoning about a
  listener. The proposal borrows RSA's likelihood structure while using predictive-coding dynamics
  for listener-side inference.
- **Scope caveat:** FEP is a broad principle, not a language-specific theory. It constrains the form
  of inference and learning; it does not supply scalar alternatives or lexical semantics
  (Colombo & Wright, 2021).
## 2.2 Three commitments of the canonical framework (about 285 words)
 
*New, and the backbone of Part II: §§2.3–2.5 develop one commitment each, and §2.7's caveats attach
to them rather than floating free.*
 
- **Main claim to establish:** The canonical form of predictive coding under the free-energy
  principle makes three commitments. Each is adopted for good reasons and established by none.
| Commitment | What it asserts | What it buys | What this dissertation does with it |
|---|---|---|---|
| **1. A unified objective** | One functional — variational free energy — is minimized by perception, learning and action alike (Friston, 2008, 2010) | State inference and parameter learning fall out of one quantity, and the same objective yields both sets of dynamics | Taken. It is what makes the strict concavity of §3.4 and the closed forms meaningful rather than incidental, and §4.1.3 tests them |
| **2. Local computation and local plasticity** | A unit updates from its own afferents; a synapse updates from the activities it connects (Bogacz, 2017) | That the algorithm could be carried by neurons at all | Taken as a **design constraint on the build**, and treated as generative. **This is the dissertation's answer to the first question** |
| **3. Gaussian machinery** | Densities are Gaussian, or Laplace-approximated as such (Friston et al., 2007; Bogacz, 2017) | Free energy reduces to precision-weighted squared prediction errors; updates become subtraction and multiplication | Inherited. It is what makes the model linear-Gaussian while the lexical field is clamped, and hence what §5.5 records as a limit. It does **not** make the posterior a delta: Bogacz's delta is a further approximation adopted beside it, and §3.6 offers that delta as a read-out and prefers it, on the bullet below |
 
- **The scoping sentence.** No measurement shows that cortex minimizes one objective rather than
  several; locality is a desideratum imported from what neurons plausibly can do rather than a
  measured constraint on cortical inference, and the field treats it as optional — Rao and Ballard
  (1999) do not impose it, Whittington and Bogacz (2017) show it can be met, Millidge, Seth and
  Buckley (2021) survey how much of the framework survives when it is enforced; and nothing
  independently establishes that cortical densities are Gaussian.
- **One further sentence on commitment 3, because it is more load-bearing than it looks.** The error
  unit — the object the architecture is built around — is a *subtraction* only because the densities
  are Gaussian. A non-Gaussian generative model would not yield subtractive error units at all.
  **Cross-refer forward to §2.7's negative-firing-rate problem**, which is the same issue seen at the
  circuit level.
- **And the further approximation §3.6 turns into a choice of read-out.** Bogacz (2017) goes one
  step past commitment 3: rather than the whole posterior, the system infers the most likely value
  of the hidden state (his §2.2), and his §3 recovers this as a free energy whose approximating
  density is a **delta** at that value (his Eq. 34). The delta is a commitment of its own and not a
  consequence of Gaussianity, since a Laplace approximation keeps a mode *and* a covariance (Friston
  et al., 2007). What it shares with commitment 3 is the motivation, a reduction in what inference
  has to carry: commitment 3 reduces the objective to precision-weighted squared errors, and the
  delta reduces the belief to the point the dynamics settle to. Bogacz's ground for the second is
  representational: it is reasonable to assume that the brain represents at a given moment only the
  most likely values of features (his §2.2, with binocular rivalry as the example). One sentence
  here, with the forward pointer, because **§3.6's position on the two read-outs rests on Bogacz's
  §2.2** — on its normalization argument (§2.4 below), not on the most-likely-values ground, since
  §3 lifts the hidden state to a field over the scale and so does carry many values
  (`agent/decisions.md` A21). The argument belongs to §3.6, and nothing measured enters the
  background (BG7).
## 2.3 Variational free energy: the objective actually minimized (about 190 words)
 
*Commitment 1 in detail. Shortened from the previous draft's 300 words, since §2.2 now introduces
the unified objective.*
 
- **Present both decompositions**, in Bogacz's \(v\) for the hidden state, since \(s\) is the
  scale's proportion throughout this dissertation:
  - \(\mathcal F(q)=D_{KL}[q(v)\|p(v)]-\mathbb E_q[\log p(u\mid v)]\) — complexity minus accuracy.
  - \(\mathcal F(q)=D_{KL}[q(v)\|p(v\mid u)]-\log p(u)\); since KL divergence is non-negative,
    \(\mathcal F\ge -\log p(u)\), so free energy upper-bounds surprisal.
- **Bridge the sign convention in one sentence.** The free energy of this section is minimized.
  Bogacz works with its negative, which he also writes \(F\) and maximizes (his Eq. 34), and §3 and
  both notebooks follow him: their \(\mathcal F\) is the negative free energy and is maximized.
- **Clarify three terms the slides risk conflating:** *prediction error* is a mismatch between an
  observation and a model prediction; *surprisal* is \(-\log p(u)\); *variational free energy* is an
  optimizable bound on surprisal, not the raw difference between prediction and input.
- **Replace the mapping paragraph entirely.** The previous draft mapped the objective onto
  \(q(s)=\mathrm{softmax}(z)\) over a discrete state set. **The hidden state is a pair of fields**,
  \(x=(\varphi_S,\varphi_u)\), with \(\varphi_S\) sampled on a fixed quadrature grid over
  \(\zeta=\operatorname{logit}(s)\). Three objects follow, and they must not be run together:
  - the model's **posterior over field configurations** \(x\), at fixed \(\theta_u\);
  - Bogacz's **delta** \(\delta(x-x^\ast)\), the approximation to it the construction adopts (§2.2),
    also over \(x\);
  - the **read-out** \(q(\zeta)\propto e^{\varphi_S^\ast(\zeta)}\), a distribution over the world
    coordinate, formed from the settled field for comparison with RSA (§3.6).
  The grid discretizes the integral over \(\zeta\) that \(q\) needs; it does not discretize
  \(x\), which is a vector of \(K+m\) numbers throughout.
- **One sentence on "utility":** in this architecture it names the terminating level of the
  prediction chain, not an RSA speaker's informativity-minus-cost. **Cut** the previous draft's
  KL-versus-communicative-utility discussion and the presupposition-accommodation material; §§3–6
  contain no such argument.
- **Counterargument/qualification:** in small discrete state spaces the posterior could be computed
  exactly, so the variational formulation is justified here not by computational necessity but
  because it defines dynamics that can be compared with predictive-coding-style iterative inference.
  State this candidly.
## 2.4 Predictive coding as local, error-driven message passing (about 400 words)
 
*Commitment 2, and the answer to the first of the three questions. This is the weightiest subsection
in Part II; the previous draft's 250 words were thinner than the load it bears.*
 
- **Main claim to establish:** Predictive coding turns variational inference into local dynamics
  between state units and error units — and **locality is not a side condition but the constraint
  that generates the architecture's structure**.
- **Mechanism to explain:**
  - Higher levels send predictions downward through a generative mapping \(g(\mu)\).
  - Lower levels compute prediction errors from the difference between received input and prediction.
  - Precision-weighted errors travel upward and update latent-state estimates by gradient ascent on
    the relevant objective (Bogacz, 2017).
  - In a hierarchy each intermediate level is predicted by the level above while predicting the level
    below (Friston, 2008).
- **State the locality constraint explicitly, in Bogacz's two senses:** computation from a unit's own
  afferents, plasticity from the activities a synapse connects. Name it as a **design constraint on
  the build**, not as after-the-fact commentary — the dissertation's §3.1 lists it as one of four
  requirements, and Appendix E exists to preserve it.
- **Where the project sits, and why that placement is earned.** Whittington and Bogacz (2017) show a
  predictive-coding network with strictly local Hebbian plasticity approximates backpropagation —
  the standard this project holds itself to. Millidge, Seth and Buckley (2021) survey how much of
  the framework survives when locality is enforced rather than assumed. Rao and Ballard (1999), the
  architecture's ancestor, do not impose it — which is itself evidence that the field treats locality
  as optional.
- **The move that makes the first question a thesis rather than a methodological note.** Locality is
  **generative**, though not of the utility basis's dimension: §3.5 chooses \(m=2\) for tilt and
  width, and locality is what that choice puts under strain, since at \(m>1\) the update of
  \(\theta_u\) stops being local. Appendix E buys it back with a relay, at the cost of a fourth
  timescale — which under commitment 7 is an **ordering**, \(\tau_r\le\tau_\varepsilon\), and
  not a stability requirement the relay carries of its own (F26). And §5.1 argues for binary
  branching from it: a cascade of complementary pairs needs only \(m=1\) at each level, where the
  update is local without the relay. Say here that the
  dissertation treats an implementation constraint as a *source of structure*, and that Part I's
  three questions will be answered from it.
- **Where the constraint is stated, and what Bogacz does with a read-out.** Bogacz (2017, §1)
  states both constraints as conditions any computational model must meet to be biologically
  plausible, and his model has **no read-out stage**: what it delivers is the activity of its state
  units, which is what he takes to be represented (§2.2). The same section gives two reasons not to
  compute the posterior itself. Representing it takes infinitely many values rather than a few
  summary statistics; and its normalization, for a continuous distribution an integral, would be
  challenging for a simple biological system. He adds that circuits in the basal ganglia have been
  proposed to compute the normalization for **discrete** distributions (Bogacz & Gurney, 2007).
  State both and draw nothing from them here: the tutorial does not say whether a read-out falls
  under the locality constraint, and §3.6 is where the dissertation takes that up. Worth the
  sentence on discreteness, since the quadrature grid of §3 makes \(q\)'s normalizer a sum over a
  discrete set.
- **Potential neural support, kept proportionate:** canonical-microcircuit proposals associate
  feedforward and feedback pathways with error and prediction signals (Bastos et al., 2012);
  language-focused work has proposed related beta/gamma dynamics during sentence comprehension
  (Lewis & Bastiaansen, 2015). **Label these as circuit-level claims the dissertation does not itself
  make**, per §2.1's three-way vocabulary.
## 2.5 What this architecture does not use (about 110 words)
 
*Raised 60 → 110 at BG7: the 60 was a minimum budget handed a second move, which repeats §5.6's
failure. Replaces the previous draft's 300-word precision subsection. Kept as its own heading so a reader
arriving from the FEP literature finds the absence stated rather than having to infer it.*
 
- Precision weighting is the standard mechanism by which a predictive-coding model modulates the
  influence of a prior or an error (Friston, 2008; Feldman & Friston, 2010; Bogacz, 2017), and
  **this architecture uses none of it** — every variance is fixed at unity, which removes precision
  learning and Bogacz's interneuron construction with it.
- One sentence, **position reserved** (Entry 3b): predictive coding's precision machinery, combined
  with freedom to posit error- and expectation-coding subpopulations where data require, has been
  argued to make the framework flexible enough to accommodate findings after the fact (Walsh et al.,
  2020, citing Kogo & Trengove, 2015). Dropping precision inference **sidesteps that concern for the
  model built here rather than resolving it**, and is a scope narrowing, not a rebuttal.
## 2.6 Timescales, bidirectional flow, and joint settlement (about 250 words)
 
*This is the dissertation's answer to the second question. Note the warrant: the claim is about
**staging**, not about message direction.*
 
- **Timescale separation, and it is a commitment rather than an ordering.**
  \(\tau_\varepsilon\le\tau_\varphi/(4\lambda_{\max}(H))\ll\tau_\varphi\ll\tau_\theta\):
  error units relax toward their residuals, state units ascend the objective, and the slow parameter
  follows Bogacz's own gradient. Bogacz (2017) distinguishes rapidly changing neural activities
  representing inferred states and errors from synaptic parameters encoding learned regularities,
  and the bound on \(\tau_\varepsilon\) is **ours and not his** (§2.1, commitment 7): it is
  critical damping of the stiffest mode, it tightens as \(\theta_u^2\), and what it secures, with
  the error units' silent start, is the monotone rise of \(\mathcal F\), not convergence — which §5.5 records and §5.3 prices.
  - **The learning rate is a ratio of time constants,** \(\tau_\varphi/\tau_\theta\): the constant
    of proportionality is a time constant of the kind the error and state units already carry, so
    the model has no step size set apart from its ordering of timescales. One sentence, and no
    stronger: the ratio still does a learning rate's work (Text cell 3 §7).
  - **The slow parameter is learned, and its flow starts at \(\theta_u(0)=0\)** — one start
    shared by every configuration, and there the network is the **tempered control** rather than
    the literal listener (§4.1.1 names both). Worth one sentence: it is why §4's readings are
    displacements from a control the model passes through, and not from a baseline stipulated
    beside it.
  - Appendix E adds a fourth timescale, ordered \(\tau_r\le\tau_\varepsilon\) as in §2.4;
    mention, do not develop.
- **Bidirectional flow.** Predictions descend the chain and errors ascend it, and every intermediate
  level is both predicted and predicting.
- **The consequence for staging, which is the point of the subsection, at its true scope.** The
  lexical input is not co-determined: \(\varphi_L=\Lambda\chi_y\) is supplied by the utterance and
  clamped before recurrence begins, so a semantic value, the entry itself, does exist before any
  pragmatic influence. What is joint is everything downstream of it. Given the clamped
  \(\varphi_L\), the world belief and the utility state are inferred together, as the one maximizer
  of an objective strictly concave in both, and neither settles first. So the claim is that **the
  interpretation is co-determined**: no literal interpretation is settled on the entry alone and
  then revised by pragmatic influence.
  - **Be careful here, twice.** Bidirectional message flow alone does not deny staging — a
    feedforward pipeline with error feedback is still stageable; the claim rests on the joint
    settlement, and bidirectional flow is the mechanism by which it is reached. And concavity gives
    a *unique* solution, not an *impossibility* of staging: a staged computation could reach the
    same maximizer. The claim is about how this architecture computes the interpretation, not about
    how no architecture could.
  - This is the architectural fact §1.5's demarcation problem is answered from.
- **Counterargument/qualification:** updating the slow parameter once per utterance is closer to
  empirical-Bayes parameter learning than to a fully derived canonical predictive-coding circuit.
  The methods section specifies the schedule.
## 2.7 Limits, and the level of the claim (about 210 words)
 
- **Main claim to establish:** The framework's standing is contested in ways that bear on any model
  built in it, and the dissertation's own claims are scoped by level rather than hedged by label.
- **Three beats:**
  1. **The field has no settled framework.** Predictive coding and the free-energy principle are
     prominent, actively developed proposals rather than consensus (Furutachi & Hofer, 2026), and
     the free-energy principle is a principle rather than a mechanism (Colombo & Wright, 2021).
  2. **The evidence is mixed rather than confirmatory** (Walsh et al., 2020). Give the
     **negative-firing-rate problem** as the concrete instance of the algorithm/circuit gap:
     subtraction-based error units imply signed signals, a spiking neuron cannot represent a negative
     rate, and the proposed fixes — signed subpopulations, or divisive rather than subtractive
     normalization — compete rather than settle (Walsh et al., 2020; Keller & Mrsic-Flogel, 2018).
     **Cross-refer back to commitment 3**: signed errors follow from Gaussian densities, so this is
     that commitment seen at the circuit level.
  3. **The connectome-scale gap** is why no general circuit-level claim is made. A complete,
     synapse-resolved connectome exists for the fly (Schlegel et al., 2024) and for a cubic
     millimetre of mouse visual cortex (MICrONS Consortium, 2025); none exists for any circuit
     plausibly responsible for scalar implicature or vagueness resolution, in any organism.
- **Close on claim level, not on apology.** The model is a predictive coding model at the
  **algorithmic** level and makes no general circuit-level claim — **with one exception that should
  be named rather than swallowed: Appendix E's relay is a circuit-level proposal**, modest but
  genuinely implementational. **Its content is not the relay's speed.** Under commitment 7 the
  relay's requirement collapses into the ordering \(\tau_r\le\tau_\varepsilon\) and binds
  nothing further (F26), and what a slower relay breaks is the monotone rise of \(\mathcal F\) —
  a transient, not a failure to converge. The implementational commitment carrying empirical content
  is **commitment 7's separation itself**, which grows as \(\theta_u^2\) and which §5.3 prices.
  The model is linear-Gaussian while the lexical field is clamped, which is what makes the
  closed forms exact and the implementation claim testable.
- **Do not hedge the generative model.** The continuous log-odds state, the exclusion-set lexical
  representation, utility as the terminating level, unit variances, and the two-dimensional utility
  basis are **commitments this architecture makes**, stated as such in §3 and parallel in form to
  §2.2's three. Hedging one's own theoretical content is not caution.
- **Final scope note:** the free-energy principle does not choose the alternative set, the semantic
  representation, or the communicative goal; those remain linguistic commitments.
---
 
# Closing bridge (about 120 words)
 
- State the three questions once more, and that one architecture answers them together because the
  constraint generates the rest:
  > The architecture is built under locality; it settles a lexical entry and a world prior jointly in
  > one density rather than in sequence; and it produces movement of belief mass off the *all*
  > reading while representing no alternative at any point.
- **Then the standing qualification, in its own sentence**, because §5.1 leans on it: **the model has
  no alternatives space, so nothing in it could show that human processing lacks one.** The claims
  are about what the *effect* requires, not about what human processing contains.
- **Do not** introduce implementation details, hyperparameter values, or results here.
---
 
# Reference list

**Scope: the whole dissertation.** This is the only reference list either outline keeps —
`sections_3-6.md` has none of its own — and it covers the background, §§3–6, **and the appendices
as `main.ipynb` and `appendix_E.ipynb` carry them**. A work cited anywhere in the dissertation has
an entry here. Each notebook keeps its own References cell for its own text — `main.ipynb` cell 24,
`appendix_E.ipynb` cell 9 (`agent/agent.md` §1, coupling 11). **BG10** reconciled the three on
2026-09-22, 50 entries to 64: eight works that lived only in main's cell and six only in
appendix_E's were folded in here. *Two divergences left standing, both wanting one pass across all
three: Friston is "Friston, K." for 2005 and "Friston, K. J." for 2007-2010, and the notebooks set
page ranges with en dashes where this list uses hyphens.*
 
Aitchison, L., & Lengyel, M. (2017). With or without you: Predictive coding and Bayesian inference in the brain. *Current Opinion in Neurobiology, 46*, 219-227. https://doi.org/10.1016/j.conb.2017.08.010
 
Åström, K. J., & Murray, R. M. (2008). *Feedback systems: An introduction for scientists and engineers*. Princeton University Press.
 
Bastos, A. M., Usrey, W. M., Adams, R. A., Mangun, G. R., Fries, P., & Friston, K. J. (2012). Canonical microcircuits for predictive coding. *Neuron, 76*(4), 695-711. https://doi.org/10.1016/j.neuron.2012.10.038
 
Bogacz, R. (2017). A tutorial on the free-energy framework for modelling perception and learning. *Journal of Mathematical Psychology, 76*, 198-211. https://doi.org/10.1016/j.jmp.2015.11.003
 
Bogacz, R., & Gurney, K. (2007). The basal ganglia and cortex implement optimal decision making between alternative actions. *Neural Computation, 19*(2), 442-477. https://doi.org/10.1162/neco.2007.19.2.442
 
Chemla, E., & Spector, B. (2011). Experimental evidence for embedded scalar implicatures. *Journal of Semantics, 28*(3), 359-400. https://doi.org/10.1093/jos/ffq023
 
Chierchia, G. (2004). Scalar implicatures, polarity phenomena, and the syntax/pragmatics interface. In A. Belletti (Ed.), *Structures and beyond: The cartography of syntactic structures* (Vol. 3, pp. 39-103). Oxford University Press.
 
Chierchia, G. (2017). Scalar implicatures and their interface with grammar. *Annual Review of Linguistics, 3*, 245-264. https://doi.org/10.1146/annurev-linguistics-011516-033846
 
Chierchia, G., Fox, D., & Spector, B. (2012). Scalar implicature as a grammatical phenomenon. In C. Maienborn, K. von Heusinger, & P. Portner (Eds.), *Semantics: An international handbook of natural language meaning* (Vol. 3, pp. 2297-2331). De Gruyter Mouton.
 
Clifton, C., Jr., & Dube, C. (2010). Embedded implicatures observed: A comment on Geurts and Pouscoulous (2009). *Semantics and Pragmatics, 3*, Article 7, 1-13. https://doi.org/10.3765/sp.3.7
 
Colombo, M., & Wright, C. (2021). First principles in the life sciences: The free-energy principle, organicism, and mechanism. *Synthese, 198*(Suppl. 14), S3463-S3488. https://doi.org/10.1007/s11229-018-01932-w
 
Cremers, A., Wilcox, E. G., & Spector, B. (2023). Exhaustivity and anti-exhaustivity in the RSA framework: Testing the effect of prior beliefs. *Cognitive Science, 47*(5), e13286. https://doi.org/10.1111/cogs.13286
 
Danskin, J. M. (1967). *The theory of max-min and its application to weapons allocation problems*. Springer. https://doi.org/10.1007/978-3-642-46092-0
 
Davey, B. A., & Priestley, H. A. (2002). *Introduction to lattices and order* (2nd ed.). Cambridge University Press. https://doi.org/10.1017/CBO9780511809088
 
Degen, J., Tessler, M. H., & Goodman, N. D. (2015). Wonky worlds: Listeners revise world knowledge when utterances are odd. In D. C. Noelle et al. (Eds.), *Proceedings of the 37th Annual Meeting of the Cognitive Science Society* (pp. 548-553). Cognitive Science Society.
 
Feldman, H., & Friston, K. J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience, 4*, Article 215. https://doi.org/10.3389/fnhum.2010.00215
 
Ferguson, K. A., & Cardin, J. A. (2020). Mechanisms underlying gain modulation in the cortex. *Nature Reviews Neuroscience, 21*(2), 80-92. https://doi.org/10.1038/s41583-019-0253-y
 
Fox, D., & Spector, B. (2018). Economy and embedded exhaustification. *Natural Language Semantics, 26*(1), 1-50. https://doi.org/10.1007/s11050-017-9139-6
 
Frank, M. C., & Goodman, N. D. (2012). Predicting pragmatic reasoning in language games. *Science, 336*(6084), 998. https://doi.org/10.1126/science.1218633
 
Franke, M. (2011). Quantity implicatures, exhaustive interpretation, and rational conversation. *Semantics and Pragmatics, 4*, Article 1, 1-82. https://doi.org/10.3765/sp.4.1
 
Friston, K. (2005). A theory of cortical responses. *Philosophical Transactions of the Royal Society B: Biological Sciences, 360*(1456), 815-836. https://doi.org/10.1098/rstb.2005.1622
 
Friston, K. J. (2008). Hierarchical models in the brain. *PLOS Computational Biology, 4*(11), e1000211. https://doi.org/10.1371/journal.pcbi.1000211
 
Friston, K. J. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience, 11*(2), 127-138. https://doi.org/10.1038/nrn2787
 
Friston, K., Mattout, J., Trujillo-Barreto, N., Ashburner, J., & Penny, W. (2007). Variational free energy and the Laplace approximation. *NeuroImage, 34*(1), 220-234. https://doi.org/10.1016/j.neuroimage.2006.08.035
 
Furutachi, S., & Hofer, S. B. (2026). Rethinking predictive processing. *Annual Review of Neuroscience, 49*, 471-494. https://doi.org/10.1146/annurev-neuro-102124-031410
 
Gazdar, G. (1979). *Pragmatics: Implicature, presupposition, and logical form*. Academic Press.
 
Geurts, B. (2010). *Quantity implicatures*. Cambridge University Press.
 
Geurts, B., & Pouscoulous, N. (2009). Embedded implicatures?!? *Semantics and Pragmatics, 2*, Article 4, 1-34. https://doi.org/10.3765/sp.2.4
 
Goodman, N. D., & Frank, M. C. (2016). Pragmatic language interpretation as probabilistic inference. *Trends in Cognitive Sciences, 20*(11), 818-829. https://doi.org/10.1016/j.tics.2016.08.005
 
Goodman, N. D., & Stuhlmüller, A. (2013). Knowledge and implicature: Modeling language understanding as social cognition. *Topics in Cognitive Science, 5*(1), 173-184. https://doi.org/10.1111/tops.12007
 
Grice, H. P. (1975). Logic and conversation. In P. Cole & J. L. Morgan (Eds.), *Syntax and semantics: Speech acts* (Vol. 3, pp. 41-58). Academic Press.
 
Griffiths, T. L., Lieder, F., & Goodman, N. D. (2015). Rational use of cognitive resources: Levels of analysis between the computational and the algorithmic. *Topics in Cognitive Science, 7*(2), 217-229. https://doi.org/10.1111/tops.12142
 
Grossberg, S. (1987). Competitive learning: From interactive activation to adaptive resonance. *Cognitive Science, 11*(1), 23-63.
 
Gutzmann, D. (2021). Semantics vs. pragmatics. In D. Gutzmann, L. Matthewson, C. Meier, H. Rullmann, & T. E. Zimmermann (Eds.), *The Wiley Blackwell companion to semantics* (pp. 1-31). Wiley. https://doi.org/10.1002/9781118788516.sem049 **[Year unresolved: Crossref records the chapter and the volume as 2020 (online); the print volume is dated 2021. Pick one and use it for every Companion chapter cited.]**
 
Horn, L. R. (1972). *On the semantic properties of logical operators in English* [Unpublished doctoral dissertation]. University of California, Los Angeles.
 
Ippolito, M. (2010). Embedded implicatures? Remarks on the debate between globalist and localist theories. *Semantics and Pragmatics, 3*, Article 5, 1-15. https://doi.org/10.3765/sp.3.5
 
Jaszczolt, K. M. (2012). Semantics/pragmatics boundary disputes. In C. Maienborn, K. von Heusinger, & P. Portner (Eds.), *Semantics: An international handbook of natural language meaning* (Vol. 3, pp. 2333-2360). De Gruyter Mouton.
 
Katzir, R. (2007). Structurally-defined alternatives. *Linguistics and Philosophy, 30*(6), 669-690. https://doi.org/10.1007/s10988-008-9029-y
 
Keller, G. B., & Mrsic-Flogel, T. D. (2018). Predictive processing: A canonical cortical computation. *Neuron, 100*(2), 424-435. https://doi.org/10.1016/j.neuron.2018.10.003
 
Kennedy, C. (2007). Vagueness and grammar: The semantics of relative and absolute gradable adjectives. *Linguistics and Philosophy, 30*(1), 1-45. https://doi.org/10.1007/s10988-006-9008-0
 
Kogo, N., & Trengove, C. (2015). Is predictive coding theory articulated enough to be testable? *Frontiers in Computational Neuroscience, 9*, Article 111. https://doi.org/10.3389/fncom.2015.00111
 
Kratzer, A., & Shimoyama, J. (2002). Indeterminate pronouns: The view from Japanese. In Y. Otsu (Ed.), *Proceedings of the 3rd Tokyo Conference on Psycholinguistics* (pp. 1-25). Hituzi Syobo.
 
Lassiter, D., & Goodman, N. D. (2017). Adjectival vagueness in a Bayesian model of interpretation. *Synthese, 194*(10), 3801-3836. https://doi.org/10.1007/s11229-015-0786-1 **[Volume, issue, pages and DOI verified 2026-09-22 against Crossref. Still open: whether Xiang et al. (2022) build their LG model on this paper or on Lassiter & Goodman (2013, SALT 23) — that is a question about their paper, not about this entry.]**
 

 
Levinson, S. C. (2000). *Presumptive meanings: The theory of generalized conversational implicature*. MIT Press.
 
Lewis, A. G., & Bastiaansen, M. (2015). A predictive coding framework for rapid neural dynamics during sentence-level language comprehension. *Cortex, 68*, 155-168. https://doi.org/10.1016/j.cortex.2015.02.014
 
Lieder, F., & Griffiths, T. L. (2020). Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources. *Behavioral and Brain Sciences, 43*, Article e1. https://doi.org/10.1017/S0140525X1900061X
 
Lillicrap, T. P., Cownden, D., Tweed, D. B., & Akerman, C. J. (2016). Random synaptic feedback weights support error backpropagation for deep learning. *Nature Communications, 7*, Article 13276. https://doi.org/10.1038/ncomms13276
 
MacKay, D. J. C. (1998). Choice of basis for Laplace approximation. *Machine Learning, 33*(1), 77-86. https://doi.org/10.1023/A:1007558615313
 
Magri, G. (2011). Another argument for embedded scalar implicatures based on oddness in downward-entailing environments. *Semantics and Pragmatics, 4*, Article 6, 1-51. https://doi.org/10.3765/sp.4.6
 
Marr, D. (1982). *Vision: A computational investigation into the human representation and processing of visual information*. W. H. Freeman.
 
MICrONS Consortium. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. *Nature, 640*, 435-447. https://doi.org/10.1038/s41586-025-08790-w
 
Millidge, B., Seth, A., & Buckley, C. L. (2021). *Predictive coding: A theoretical and experimental review*. arXiv. https://doi.org/10.48550/arXiv.2107.12979
 
Potts, C., Lassiter, D., Levy, R., & Frank, M. C. (2016). Embedded implicatures as pragmatic inferences under compositional lexical uncertainty. *Journal of Semantics, 33*(4), 755-802. https://doi.org/10.1093/jos/ffv012
 
Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience, 2*(1), 79-87. https://doi.org/10.1038/4580
 
Ronai, E., & Xiang, M. (2024). What could have been said? Alternatives and variability in pragmatic inferences. *Journal of Memory and Language, 136*, 104507. https://doi.org/10.1016/j.jml.2024.104507
 
Rooth, M. (1985). *Association with focus* [Doctoral dissertation, University of Massachusetts Amherst].
 
Rooth, M. (1992). A theory of focus interpretation. *Natural Language Semantics, 1*(1), 75-116. https://doi.org/10.1007/BF02342617
 
Sauerland, U. (2004). Scalar implicatures in complex sentences. *Linguistics and Philosophy, 27*(3), 367-391. https://doi.org/10.1023/B:LING.0000023378.71748.db
 
Sauerland, U. (2012). The computation of scalar implicatures: Pragmatic, lexical or grammatical? *Language and Linguistics Compass, 6*(1), 36-49. https://doi.org/10.1002/lnc3.321
 
Schlegel, P., Yin, Y., Bates, A. S., Dorkenwald, S., Eichler, K., Brooks, P., Han, D. S., Gkantia, M., Dos Santos, M., Munnelly, E. J., Badalamente, G., Serrano Capdevila, L., Sane, V. A., Pleijzier, M. W., Tamimi, I. F. M., Dunne, C. R., Salgarella, I., Javier, A., Fang, S., … Jefferis, G. S. X. E. (2024). Whole-brain annotation and multi-connectome cell typing of *Drosophila*. *Nature, 634*, 139-152. https://doi.org/10.1038/s41586-024-07686-5
 
Sherman, S. M., & Guillery, R. W. (1998). On the actions that one nerve cell can have on another: Distinguishing "drivers" from "modulators". *Proceedings of the National Academy of Sciences, 95*(12), 7121-7126. https://doi.org/10.1073/pnas.95.12.7121
 
Spratling, M. W. (2013). Distinguishing theory from implementation in predictive coding accounts of brain function. *Behavioral and Brain Sciences, 36*(3), 231-232. https://doi.org/10.1017/S0140525X12002178
 
Strogatz, S. H. (1994). *Nonlinear dynamics and chaos: With applications to physics, biology, chemistry, and engineering*. Addison-Wesley.
 
Walsh, K. S., McGovern, D. P., Clark, A., & O'Connell, R. G. (2020). Evaluating the neurophysiological evidence for predictive processing as a model of perception. *Annals of the New York Academy of Sciences, 1464*(1), 242-268. https://doi.org/10.1111/nyas.14321
 
Whittington, J. C. R., & Bogacz, R. (2017). An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity. *Neural Computation, 29*(5), 1229-1262. https://doi.org/10.1162/NECO_a_00949
 
Xiang, M., Kennedy, C., Xu, W., & Leffel, T. (2022). Pragmatic reasoning and semantic convention: A case study on gradable adjectives. *Semantics and Pragmatics, 15*(9). https://doi.org/10.3765/sp.15.9
 
**Dropped with this revision:** Cover & Thomas (2006), which supported the KL-versus-communicative-utility discussion cut from §2.3.
 
## Project materials consulted
 
Gu, S. (2026a). *Another way to wonky worlds? Generative models and prior precision in scalar inference via the Free Energy Principle* [Unpublished presentation slides]. University College London.
 
Gu, S. (2026b). *Scalar implicature as predictive coding (discrete state space)* [Unpublished Jupyter notebook].
 
---
 
