Background sections outline · MD
# Outline for the dissertation background
 
**Rewritten 2026-09-11** under the three-question frame, per
`claude/background_revision_plan.md` (Revision 4). The previous version motivated a model that
learns confidence in the prior; this architecture performs no precision inference, and the question
it answers is a different one. Nothing from the precision/wonkiness arc survives except as contrast.
 
---
 
## Scale and argumentative shape
 
- **Target length: approximately 3,595 words.**
- **Opening (about 220 words).** The explanandum; the three questions the dissertation answers; and
  Marr's levels, fixed by contrast with RSA.
- **Part I — What scalar resolution is asked to explain, and why the existing division does not
  settle it (about 2,035 words).** Establishes two things §§3–6 need and one they dissolve: that
  every existing account computes strengthening over a *represented alternative set*; that the
  accounts deriving it *from the prior* carry a documented liability; and that the debates over
  which level a pattern belongs to share a presupposition about staging.
- **Part II — Predictive coding, its commitments, and the constraint that generates the answers
  (about 1,440 words).** Only the parts the model uses, organized around the framework's three
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
 
# Opening: three questions, and the level they are asked at (about 220 words)
 
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
     peculiarity **when the computational goal does not entail it**.
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
 
# Part I. What scalar resolution is asked to explain, and why the existing division does not settle it (about 2,035 words)
 
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
  - **New, and load-bearing for §4.2 of the proposal:** this dissertation's explanandum is
    **graded** — movement of belief mass off the *all* reading — rather than a truth-value judgment.
    Say so here, because §4.2's two-condition criterion is otherwise a stipulation arriving without
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
  - Pragmatic speaker: \(S_1(u\mid s)\propto \exp\{\alpha[\log L_0(s\mid u)-C(u)]\}\).
  - Pragmatic listener: \(L_1(s\mid u)\propto S_1(u\mid s)P(s)\).
  - \(\alpha\) controls soft-maximal speaker choice; \(C(u)\) penalizes costly forms. The
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
## 1.3 Strengthening derived from the prior, and its two liabilities (about 340 words)
 
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
- **The redeployment.** Human strengthening is **robust against prior concentration** — which is
  precisely the profile a drain scaling with prior mass on the all-region cannot produce. Flag
  forward to §5.1.
- *Counterargument:* numerical and slider judgments are noisy. The convergence of expected-number
  judgments, all-state judgments, and separate normality judgments is nevertheless stronger than
  reliance on one dependent measure.
**Beat 2 — wRSA as the response, and the inverted parallel (about 100 words).**
 
- A latent wonkiness variable \(w\); under the usual setting \(P(s\mid w)\) is the elicited world
  prior, under the wonky setting a uniform back-off. The pragmatic listener becomes
  \(L_1(s,w\mid u)\propto S_1(u\mid s,w)P(s\mid w)P(w)\). Improved fit, and the qualitative U-shaped
  normality judgments for *some*.
- **Its function here is contrast, not target.** wRSA keeps Bayesian reasoning by making **the
  prior** defeasible against the utterance. This dissertation's architecture makes **the lexical
  entry** defeasible against the prior — finite lexical strength \(\Lambda\), §3.2 — and §4.5
  quantifies where that override bites. Two sentences, no verdict, forward pointer only.
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
- **Forward pointer, stated without embarrassment:** §5.1 reports that *this model exhibits the same
  anti-exhaustive direction on four of five priors*, and treats the fact as corroboration — both
  models derive strengthening from the prior, so both inherit the liability, and what avoids it is a
  drain keyed to the alternative.
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
> supplies an architecture in which it does not hold, and §5.1 returns to what follows.
 
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
 
*New. Supplies §5.2's entire literature, motivates a continuous state space in §3.2, and earns the
project's "scalar vagueness resolution" keyword.*
 
- **Main claim to establish:** Where a predicate's threshold sits on its scale is a matter of
  semantic convention, and the conventions differ systematically by scale structure.
- **Material to include:**
  - Degree semantics: a gradable predicate relates a degree to a threshold.
  - **Maximum-standard absolute adjectives have closed scales and conventional endpoint standards;
    relative adjectives have open scales and context-dependent thresholds** (Kennedy, 2007).
  - The empirical profile: absolute adjectives elicit categorical responses concentrated near the
    scalar maximum, relative adjectives a roughly constant increase across scale positions, and the
    difference is most dramatic in the impoverished-prior (geometric shapes) condition rather than
    the rich-prior (familiar artifacts) one (Leffel, Xiang & Kennedy, 2017; Xiang, Kennedy, Xu &
    Leffel, 2022).
  - Xiang et al.'s own conclusion: Bayesian pragmatics models what is *communicated* well
    (\(R^2=.78\)–\(.82\)) but threshold judgments poorly (\(R^2=.36\)–\(.63\)), especially for
    absolute adjectives, so Bayesian reasoning must be combined with the semantic conventions
    governing thresholds.
- **State Q3b as the open question this leaves:** *what mechanism produces endpoint orientation?*
  **Do not answer it here.** §5.2 answers it from the parity structure of the utility basis, and the
  background's job is to make the question askable.
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
 
# Part II. Predictive coding, its commitments, and the constraint that generates the answers (about 1,440 words)
 
## 2.1 FEP, generative models, and Bayesian model inversion (about 210 words)
 
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
- **Counterargument/qualification:** do not equate this mapping with RSA's social recursion.
  Bidirectional generative/inference flow is not nested reasoning about a speaker reasoning about a
  listener. The proposal borrows RSA's likelihood structure while using predictive-coding dynamics
  for listener-side inference.
- **Scope caveat:** FEP is a broad principle, not a language-specific theory. It constrains the form
  of inference and learning; it does not supply scalar alternatives or lexical semantics
  (Colombo & Wright, 2021).
## 2.2 Three commitments of the canonical framework (about 230 words)
 
*New, and the backbone of Part II: §§2.3–2.5 develop one commitment each, and §2.7's caveats attach
to them rather than floating free.*
 
- **Main claim to establish:** The canonical form of predictive coding under the free-energy
  principle makes three commitments. Each is adopted for good reasons and established by none.
| Commitment | What it asserts | What it buys | What this dissertation does with it |
|---|---|---|---|
| **1. A unified objective** | One functional — variational free energy — is minimized by perception, learning and action alike (Friston, 2008, 2010) | State inference and parameter learning fall out of one quantity, and the same objective yields both sets of dynamics | Taken. It is what makes the strict concavity of §3.4 and the closed forms meaningful rather than incidental, and §4.3 tests them |
| **2. Local computation and local plasticity** | A unit updates from its own afferents; a synapse updates from the activities it connects (Bogacz, 2017) | That the algorithm could be carried by neurons at all | Taken as a **design constraint on the build**, and treated as generative. **This is the dissertation's answer to the first question** |
| **3. Gaussian machinery** | Densities are Gaussian, or Laplace-approximated as such (Friston et al., 2007; Bogacz, 2017) | Free energy reduces to precision-weighted squared prediction errors; updates become subtraction and multiplication | Inherited. It is what makes the model linear-Gaussian while the lexical field is clamped, and hence what §5.3 records as a limit |
 
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
## 2.3 Variational free energy: the objective actually minimized (about 190 words)
 
*Commitment 1 in detail. Shortened from the previous draft's 300 words, since §2.2 now introduces
the unified objective.*
 
- **Present both decompositions:**
  - \(\mathcal F(q)=D_{KL}[q(s)\|p(s)]-\mathbb E_q[\log p(u\mid s)]\) — complexity minus accuracy.
  - \(\mathcal F(q)=D_{KL}[q(s)\|p(s\mid u)]-\log p(u)\); since KL divergence is non-negative,
    \(\mathcal F\ge -\log p(u)\), so free energy upper-bounds surprisal.
- **Clarify three terms the slides risk conflating:** *prediction error* is a mismatch between an
  observation and a model prediction; *surprisal* is \(-\log p(u)\); *variational free energy* is an
  optimizable bound on surprisal, not the raw difference between prediction and input.
- **Replace the mapping paragraph entirely.** The previous draft mapped the objective onto
  \(q(s)=\mathrm{softmax}(z)\) over a discrete state set. **The state is continuous:** the
  approximating belief is over \(\zeta=\operatorname{logit}(s)\), evaluated on a fixed quadrature
  grid, and the grid discretizes the integral rather than the state.
- **One sentence on "utility":** in this architecture it names the terminating level of the
  prediction chain, not an RSA speaker's informativity-minus-cost. **Cut** the previous draft's
  KL-versus-communicative-utility discussion and the presupposition-accommodation material; §§3–6
  contain no such argument.
- **Counterargument/qualification:** in small discrete state spaces the posterior could be computed
  exactly, so the variational formulation is justified here not by computational necessity but
  because it defines dynamics that can be compared with predictive-coding-style iterative inference.
  State this candidly.
## 2.4 Predictive coding as local, error-driven message passing (about 330 words)
 
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
  **generative**: §3.5 derives the utility basis dimension from it, §5.1 derives binary branching
  from it, and Appendix E pays a fourth timescale to keep it at \(m>1\). Say here that the
  dissertation treats an implementation constraint as a *source of structure*, and that Part I's
  three questions will be answered from it.
- **Potential neural support, kept proportionate:** canonical-microcircuit proposals associate
  feedforward and feedback pathways with error and prediction signals (Bastos et al., 2012);
  language-focused work has proposed related beta/gamma dynamics during sentence comprehension
  (Lewis & Bastiaansen, 2015). **Label these as circuit-level claims the dissertation does not itself
  make**, per §2.1's three-way vocabulary.
## 2.5 What this architecture does not use (about 60 words)
 
*Replaces the previous draft's 300-word precision subsection. Kept as its own heading so a reader
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
## 2.6 Timescales, bidirectional flow, and joint settlement (about 220 words)
 
*This is the dissertation's answer to the second question. Note the warrant: the claim is about
**staging**, not about message direction.*
 
- **Timescale separation.** \(\tau_\varepsilon \ll \tau_\varphi \ll \tau_\theta\): error units relax
  toward their residuals, state units ascend the objective, and the slow parameter follows Bogacz's
  own gradient. Bogacz (2017) distinguishes rapidly changing neural activities representing inferred
  states and errors from synaptic parameters encoding learned regularities.
  - **There is no learning rate and none is required:** the constant of proportionality is a time
    constant of the kind the error and state units already carry. Worth one sentence, because it is
    where the model differs from a fitted network.
  - Appendix E adds a fourth timescale; mention, do not develop.
- **Bidirectional flow.** Predictions descend the chain and errors ascend it, and every intermediate
  level is both predicted and predicting.
- **The consequence for staging, which is the point of the subsection.** Because the lexical field
  and the world prior enter the **same log-density** and the objective is jointly concave with a
  unique maximum, the settled interpretation is **co-determined**: there is no point in the
  computation at which a purely semantic value exists prior to pragmatic influence, and the result
  cannot be factored into a semantic stage followed by a pragmatic one.
  - **Be careful here.** Bidirectional message flow alone does not deny staging — a feedforward
    pipeline with error feedback is still stageable. What denies it is the joint settlement. State
    the joint settlement as the claim and bidirectional flow as the mechanism by which it is reached.
  - This is the architectural fact §1.5's demarcation problem is answered from.
- **Counterargument/qualification:** updating the slow parameter once per utterance is closer to
  empirical-Bayes parameter learning than to a fully derived canonical predictive-coding circuit.
  The methods section specifies the schedule.
## 2.7 Limits, and the level of the claim (about 200 words)
 
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
     millimetre of mouse cortex; none exists for any circuit plausibly responsible for scalar
     implicature or vagueness resolution, in any organism.
- **Close on claim level, not on apology.** The model is a predictive coding model at the
  **algorithmic** level and makes no general circuit-level claim — **with one exception that should
  be named rather than swallowed: Appendix E's relay is a circuit-level proposal**, modest but
  genuinely implementational, and it carries a testable consequence in the required speed of the
  relay. The model is linear-Gaussian while the lexical field is clamped, which is what makes the
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
 
Aitchison, L., & Lengyel, M. (2017). With or without you: Predictive coding and Bayesian inference in the brain. *Current Opinion in Neurobiology, 46*, 219-227. https://doi.org/10.1016/j.conb.2017.08.010
 
Bastos, A. M., Usrey, W. M., Adams, R. A., Mangun, G. R., Fries, P., & Friston, K. J. (2012). Canonical microcircuits for predictive coding. *Neuron, 76*(4), 695-711. https://doi.org/10.1016/j.neuron.2012.10.038
 
Bogacz, R. (2017). A tutorial on the free-energy framework for modelling perception and learning. *Journal of Mathematical Psychology, 76*, 198-211. https://doi.org/10.1016/j.jmp.2015.11.003
 
Chemla, E., & Spector, B. (2011). Experimental evidence for embedded scalar implicatures. *Journal of Semantics, 28*(3), 359-400. https://doi.org/10.1093/jos/ffq023
 
Chierchia, G. (2017). Scalar implicatures and their interface with grammar. *Annual Review of Linguistics, 3*, 245-264. https://doi.org/10.1146/annurev-linguistics-011516-033846
 
Chierchia, G., Fox, D., & Spector, B. (2012). Scalar implicature as a grammatical phenomenon. In C. Maienborn, K. von Heusinger, & P. Portner (Eds.), *Semantics: An international handbook of natural language meaning* (Vol. 3, pp. 2297-2331). De Gruyter Mouton.
 
Clifton, C., Jr., & Dube, C. (2010). Embedded implicatures observed: A comment on Geurts and Pouscoulous (2009). *Semantics and Pragmatics, 3*, Article 7, 1-13. https://doi.org/10.3765/sp.3.7
 
Colombo, M., & Wright, C. (2021). First principles in the life sciences: The free-energy principle, organicism, and mechanism. *Synthese, 198*(Suppl. 14), S3463-S3488. https://doi.org/10.1007/s11229-018-01932-w
 
Cremers, A., Wilcox, E., & Spector, B. (2023). Exhaustivity and anti-exhaustivity in the RSA framework: Testing the effect of prior beliefs. *Cognitive Science, 47*(3), e13286. **[Verify volume, issue, article number.]**
 
Degen, J., Tessler, M. H., & Goodman, N. D. (2015). Wonky worlds: Listeners revise world knowledge when utterances are odd. In D. C. Noelle et al. (Eds.), *Proceedings of the 37th Annual Meeting of the Cognitive Science Society* (pp. 548-553). Cognitive Science Society.
 
Feldman, H., & Friston, K. J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience, 4*, Article 215. https://doi.org/10.3389/fnhum.2010.00215
 
Fox, D., & Spector, B. (2018). Economy and embedded exhaustification. *Natural Language Semantics, 26*(1), 1-50. https://doi.org/10.1007/s11050-017-9139-6
 
Frank, M. C., & Goodman, N. D. (2012). Predicting pragmatic reasoning in language games. *Science, 336*(6084), 998. https://doi.org/10.1126/science.1218633
 
Franke, M. (2011). Quantity implicatures, exhaustive interpretation, and rational conversation. *Semantics and Pragmatics, 4*, Article 1, 1-82. https://doi.org/10.3765/sp.4.1
 
Friston, K. J. (2008). Hierarchical models in the brain. *PLOS Computational Biology, 4*(11), e1000211. https://doi.org/10.1371/journal.pcbi.1000211
 
Friston, K. J. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience, 11*(2), 127-138. https://doi.org/10.1038/nrn2787
 
Friston, K., Mattout, J., Trujillo-Barreto, N., Ashburner, J., & Penny, W. (2007). Variational free energy and the Laplace approximation. *NeuroImage, 34*(1), 220-234. https://doi.org/10.1016/j.neuroimage.2006.08.035
 
Furutachi, S., & Hofer, S. B. (2026). **[Verify exact title and venue — literature-landscape treatment of predictive coding and the free-energy principle among competing accounts of cortical computation.]**
 
Geurts, B., & Pouscoulous, N. (2009). Embedded implicatures?!? *Semantics and Pragmatics, 2*, Article 4, 1-34. https://doi.org/10.3765/sp.2.4
 
Goodman, N. D., & Frank, M. C. (2016). Pragmatic language interpretation as probabilistic inference. *Trends in Cognitive Sciences, 20*(11), 818-829. https://doi.org/10.1016/j.tics.2016.08.005
 
Goodman, N. D., & Stuhlmüller, A. (2013). Knowledge and implicature: Modeling language understanding as social cognition. *Topics in Cognitive Science, 5*(1), 173-184. https://doi.org/10.1111/tops.12007
 
Grice, H. P. (1975). Logic and conversation. In P. Cole & J. L. Morgan (Eds.), *Syntax and semantics: Speech acts* (Vol. 3, pp. 41-58). Academic Press.
 
Gutzmann, D. (2021). Semantics vs. pragmatics. In D. Gutzmann, L. Matthewson, C. Meier, H. Rullmann, & T. E. Zimmermann (Eds.), *The Wiley Blackwell companion to semantics*. Wiley. **[Verify page or article number.]**
 
Ippolito, M. (2010). Embedded implicatures? Remarks on the debate between globalist and localist theories. *Semantics and Pragmatics, 3*, Article 5, 1-15. https://doi.org/10.3765/sp.3.5
 
Jaszczolt, K. M. (2012). Semantics/pragmatics boundary disputes. In C. Maienborn, K. von Heusinger, & P. Portner (Eds.), *Semantics: An international handbook of natural language meaning* (Vol. 3, pp. 2333-2360). De Gruyter Mouton.
 
Katzir, R. (2007). Structurally-defined alternatives. *Linguistics and Philosophy, 30*(6), 669-690. https://doi.org/10.1007/s10988-008-9029-y
 
Keller, G. B., & Mrsic-Flogel, T. D. (2018). Predictive processing: A canonical cortical computation. *Neuron, 100*(2), 424-435. https://doi.org/10.1016/j.neuron.2018.10.003
 
Kennedy, C. (2007). Vagueness and grammar: The semantics of relative and absolute gradable adjectives. *Linguistics and Philosophy, 30*(1), 1-45. https://doi.org/10.1007/s10988-006-9008-0
 
Kogo, N., & Trengove, C. (2015). Is predictive coding theory articulated enough to be testable? *Frontiers in Computational Neuroscience, 9*, Article 111. https://doi.org/10.3389/fncom.2015.00111
 
Kratzer, A., & Shimoyama, J. (2002). Indeterminate pronouns: The view from Japanese. In Y. Otsu (Ed.), *Proceedings of the 3rd Tokyo Conference on Psycholinguistics* (pp. 1-25). Hituzi Syobo.
 
Leffel, T., Xiang, M., & Kennedy, C. (2017). *Interpreting gradable adjectives in context: Domain distribution vs. scalar representation* [Manuscript]. **[Check whether Xiang et al. (2022) reports the shapes/artifacts contrast in the same terms; if so, cite the article and drop the manuscript.]**
 
Levinson, S. C. (2000). *Presumptive meanings: The theory of generalized conversational implicature*. MIT Press.
 
Lewis, A. G., & Bastiaansen, M. (2015). A predictive coding framework for rapid neural dynamics during sentence-level language comprehension. *Cortex, 68*, 155-168. https://doi.org/10.1016/j.cortex.2015.02.014
 
Magri, G. (2011). Another argument for embedded scalar implicatures based on oddness in downward-entailing environments. *Semantics and Pragmatics, 4*, Article 6, 1-51. https://doi.org/10.3765/sp.4.6
 
Marr, D. (1982). *Vision: A computational investigation into the human representation and processing of visual information*. W. H. Freeman.
 
Millidge, B., Seth, A., & Buckley, C. L. (2021). Predictive coding: A theoretical and experimental review. *arXiv:2107.12979*.
 
Potts, C., Lassiter, D., Levy, R., & Frank, M. C. (2016). Embedded implicatures as pragmatic inferences under compositional lexical uncertainty. *Journal of Semantics, 33*(4), 755-802. https://doi.org/10.1093/jos/ffv012
 
Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience, 2*(1), 79-87. https://doi.org/10.1038/4580
 
Ronai, E., & Xiang, M. (2024). What could have been said? Alternatives and variability in pragmatic inferences. *Journal of Memory and Language, 136*, 104507. https://doi.org/10.1016/j.jml.2024.104507
 
Rooth, M. (1985). *Association with focus* [Doctoral dissertation, University of Massachusetts Amherst].
 
Rooth, M. (1992). A theory of focus interpretation. *Natural Language Semantics, 1*(1), 75-116. https://doi.org/10.1007/BF02342617
 
Sauerland, U. (2012). The computation of scalar implicatures: Pragmatic, lexical or grammatical? *Language and Linguistics Compass, 6*. https://doi.org/10.1002/lnc3.321 **[Verify issue and page range.]**
 
Schlegel, P., et al. (2024). **[Verify exact title and venue — the FlyWire whole-brain connectome proofreading/cell-typing paper; ~139,000 neurons, ~15.1 million synapses.]**
 
Spratling, M. W. (2013). **[Verify exact title and venue — Marr-levels framing of predictive-coding claims.]**
 
Walsh, K. S., McGovern, D. P., Clark, A., & O'Connell, R. G. (2020). Evaluating the neurophysiological evidence for predictive processing as a model of perception. *Annals of the New York Academy of Sciences, 1464*(1), 242-268. https://doi.org/10.1111/nyas.14321
 
Whittington, J. C. R., & Bogacz, R. (2017). An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity. *Neural Computation, 29*(5), 1229-1262. https://doi.org/10.1162/NECO_a_00949
 
Xiang, M., Kennedy, C., Xu, W., & Leffel, T. (2022). Pragmatic reasoning and semantic convention: A case study on gradable adjectives. *Semantics and Pragmatics, 15*(9). https://doi.org/10.3765/sp.15.9
 
**Dropped with this revision:** Cover & Thomas (2006), which supported the KL-versus-communicative-utility discussion cut from §2.3.
 
## Project materials consulted
 
Gu, S. (2026a). *Another way to wonky worlds? Generative models and prior precision in scalar inference via the Free Energy Principle* [Unpublished presentation slides]. University College London.
 
Gu, S. (2026b). *Scalar implicature as predictive coding (discrete state space)* [Unpublished Jupyter notebook].
 
---
 
# Drafting checklist
 
**Tier 1 — the background is wrong without these.**
 
- [ ] §2.5 cut to the scope statement (the previous 300-word precision subsection describes a
      mechanism this architecture does not have)
- [ ] Opening rewritten with the three questions and the RSA level contrast
- [ ] Closing bridge rewritten — the old question asked whether the muted prior effect emerges when
      confidence in the prior is learnable
- [ ] §2.3's mapping paragraph corrected (the state is continuous, not a discrete softmax)
- [ ] The old "testable payoff" bullet cut — it promised a quantitative wRSA comparison that §4.1
      explicitly disclaims, on a quantity (prior entropy) the model does not have
- [ ] §1.4's trailing two-utility line deleted
**Tier 2 — a question goes unsupported without these.**
 
- [ ] §1.5 pasted and edited (drafted above)
- [ ] §1.7 written — without it Q3b has no background and §5.2's literature is uncited
- [ ] §1.6 written — without it §5.1's conventionalized/computed distinction lands cold
**Tier 3 — improvements.**
 
- [ ] §2.2 three commitments
- [ ] §2.4 expanded to carry locality as a thesis
- [ ] §2.6 rewritten to the staging warrant
- [ ] §1.3 merge; §1.4 trim; §1.8 rewritten; §2.7's claim-level close
**Verification, before the prose cites them:** Furutachi & Hofer (2026), Schlegel et al. (2024),
Spratling (2013) exact title and venue; the MICrONS primary consortium paper rather than press
coverage; Gutzmann (2021) page or article number; Sauerland (2012) issue and pages; Cremers, Wilcox
& Spector (2023) volume and article number; Leffel et al. (2017) against Xiang et al. (2022).