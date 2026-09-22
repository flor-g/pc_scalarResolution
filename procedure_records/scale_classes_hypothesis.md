# The scale-class hypothesis, against Xiang et al. (2022)

Working record for the investigation opened by the user on 2026-09-17. **Nothing in the notebooks or
the outlines was changed by it.** Its results are evidence, and the decisions they bear on are the
user's: `decisions.md` O8 and O13, and `thesis_outline/revisions.md` Q7.

## 1. The user's instruction, verbatim (2026-09-17)

> we have updated the notebook again since we last changed the outlines and revision plans. Can you
> reexamine this matter given the updated data? My hypothesis is that, 1. scalar expressions with
> unstable atomicity are associated with weaker lexical strength; 2. open-scale adjectives behave
> similar to "some"; complete scale adjectives behave similar to endpoint(s)+some. Check
> implications of this hypothesis and see if our prediction under this hypothesis matches Xiang's
> data.

"This matter" is §5.2 of `thesis_outline/sections_3-6.md`, re-examined on 2026-09-14 (revisions.md
§4, the §5.2 entry) and left with Q7 and O8 open.

## 2. What the hypothesis says in the model's own quantities

- **Atomicity** is *n* (Eq. A5) — a count where the predicate has atoms, and otherwise the number
  of distinguishable steps the scale affords, which need not be an integer. One name and one
  formula since N1 (O1); the separate δ form of Eq. (A6) is gone. Appendix A leaves open what fixes
  *n* for a predicate with no atoms, and says so.
- **Lexical strength** is Λ, and the model already carries that name for it: Text cell 3 §2's
  inventory reads "Λ | lexical strength, a scalar of g_y(φ_L)", and §3 item 6 says Λ → ∞ recovers a
  hard truth-conditional constraint while finite Λ makes it soft.
- So **H1 makes Λ a function of how stably the predicate fixes *n***, coupling two quantities the
  model currently fixes independently (A5's θ_L and Λ). That is a new dependency, hence O13.
- **H2** says the classes are these entries of Eq. (A1), in each adjective's own orientation:
  maximum-standard absolute = *all*, minimum-standard absolute = *some*, relative = a cut at a
  context threshold *t* anchored by neither endpoint nor *n*.

## 3. The instantiation

Xiang et al. use five scale positions. A predicate resolving **n = 4** atoms has exactly five
Voronoi cells (Appendix A: the counts k = 0..n at s_k = k/n), so **the five scale positions are the
five cells**, at θ_L = log 7 = 1.9459. Nothing else about the architecture is changed: σ = 1,
μ_u = [1, 1], m = 2, the 101-node grid of half-width 6, θ_u\* learned per configuration (A9).

The 96 items pair each image set with an antonym. In the uttered adjective's own orientation the
partner is the entry's **complement**: for a minimum adjective ("striped") the partner ("plain") is
{ζ > −θ_L} = 1 − χ_some, and for a maximum adjective ("plain") the partner ("striped") is
{ζ ≥ θ_L} = 1 − χ_all, which is Appendix C §4's O corner. So the exposure ensemble is {χ, 1 − χ}
for every item, and O8's first question needs no further choice **in this paradigm**.

## 4. What was run

`audits/2026-09-17-scale-classes/`:

- `scale_classes.py` → `output.txt`. The three classes under illustrative Beta priors, scanned in Λ;
  the decomposition into prior, q_lit, the tempered control and the model; the override Λ at which
  each class's entry stops holding against its own prior; the three entries under one common prior;
  and θ\* for the ensembles each scale carries.
- `xiang_items.py` → `xiang_items_output.txt`. The model on the authors' own 96 items with their own
  elicited priors, against their own Experiment 3 data.
- `xiang_items.csv`. The item-level aggregate used by the second script, derived from the authors'
  public OSF repository (https://osf.io/nr6a4/, CC-BY): the elicited prior, the Experiment 3
  posterior and the Experiment 2 truth-value judgment for each of the 96 items at each of the five
  positions, with their class label. The derivation is in the script's docstring. The raw files
  themselves are not copied into this repository.

Self-checks: the audit's closed form agrees with Code Cell 1 to 0.0; its closed-form θ\* agrees with
its own dense scan to 6.4e-06 and returns −28.4375 for the default n = 10 inventory, which is what
Code Cell 2 prints; a uniform five-cell prior pushes forward to [0.193, 0.200, 0.214, 0.200, 0.193]
on the grid, the O(h) spread of I6's quadrature.

**R² is the squared Pearson correlation over item × position rows**, which is how the authors compute
theirs (`LG&QF.model.predictions.R` lines 184-190).

## 5. Findings

**F1. The empirical profiles, recomputed from the authors' data** (Experiment 3, mean proportion of
choices, positions 1..5):

| class | condition | 1 | 2 | 3 | 4 | 5 | peak | mean position |
|---|---|---|---|---|---|---|---|---|
| maximum | shape | .002 | .007 | .018 | .013 | .960 | 5 | 4.61 |
| maximum | artifact | .018 | .011 | .016 | .026 | .929 | 5 | 4.83 |
| minimum | shape | .019 | .133 | .328 | .276 | .244 | 3 | 3.29 |
| minimum | artifact | .015 | .038 | .111 | .182 | .653 | 5 | 4.42 |
| relative | shape | .007 | .018 | .049 | .174 | .752 | 5 | 4.65 |
| relative | artifact | .052 | .026 | .054 | .186 | .681 | 5 | 4.42 |

**F1 is internally inconsistent, and F3–F5 were scored against absent data. Both corrected
2026-09-22 at T1/T2; `decisions.md` E16 carries the record.**

Two faults, one in the table above and one in the audit that produced it.

1. **F1's two `shape` rows were renormalized and their mean positions were not.** One image set,
   `curved_greenline`, drew **no** Experiment 3 response at all, for both of its adjectives — so the
   maximum class's shape row averages over 15 items of 16 and the minimum class's over 11 of 12, and
   both fall short of summing to 1 (0.9375 and 0.9167). Whoever wrote F1 divided the five cells by
   that sum but left `mean position` alone. The cell values above are therefore right *as
   normalized profiles*; the two mean positions are not. Corrected: maximum/shape is **4.92**, not
   4.61, and minimum/shape is **3.59**, not 3.29. The other four rows were never affected.
2. **The audit scored the model against those 10 rows as measured zeros**, which is a comparison
   against nothing. Dropping them changes the headline numbers materially:

   | | audit (F3–F5) | corrected, printed by Code Cell F |
   |---|---|---|
   | maximum class R² | 0.953 | **0.993** |
   | minimum class R² | 0.401 | **0.434** |
   | q_lit, maximum | 0.952 | **0.992** |
   | q_lit, minimum | 0.092 | **0.103** |
   | minimum class image-type difference, measured | −1.13 | **−0.83** |

   The maximum class crosses from below the published ST (.98) and QF (.97) values to above them, so
   this is not a rounding matter. **Every number F3–F5, F8–F10 record is superseded** by Code Cell F's
   output; what the findings *say* survives, since each contrast keeps its direction.

Note also that the fitted Λ of the minimum class moves from 32 to **48** once the absent rows go —
but the ladder only brackets it between 32 and 48, and Code Cell F prints the bracket rather than
the argmax alone.

**F2. H2's class-to-entry map is the one the data show.** Each class's profile is the profile of the
entry H2 assigns it: the maximum class is concentrated in the top cell; the minimum class is spread
over every cell but the bottom one, which is exactly what {ζ ≤ −θ_L} excludes; the relative class
sits above the midpoint. The paper states the same thing in words (9:27): "for maximum adjectives,
participants consistently chose the maximum degree; for minimum adjectives, the choices distributed
among all the non-minimal degrees; and for relative adjectives, the choices were clustered mainly on
degrees above the mid-point."

**F3. The model reaches the same overall fit as the models in the paper.** On their 96 items, with
their priors, at one Λ for every class, the model's posterior-degree R² is **0.81** (Λ = 16 to 24,
relative cut between positions 3 and 4), against **LG 0.78** and **QF 0.82** (their Table 5).

**F4. By class, the model is level with them on two and behind on one.**

| | max | min | rel |
|---|---|---|---|
| this model (Λ 8 / 32 / 16) | **0.953** | **0.401** | **0.800** |
| LG | 0.94 | 0.55 | 0.69 |
| QF | 0.97 | 0.58 | 0.78 |
| semantic threshold (ST) | 0.98 | 0.19 | 0.58 |
| hybrid | 0.97 | 0.32 | 0.80 |

The minimum class is the residual of every model in the paper, this one included. The authors say so
themselves: "all of the models we have looked at seem to perform weaker on minimum adjectives, there
may be independent sources of difficulties yet to be discovered" (9:45).

**F5. The utility level is what earns the fit on the two non-endpoint classes.** The literal
listener ℓ₀ − φ_L, on the same items and the same Λ, gives **max 0.952, min 0.092, rel 0.200**. The
maximum class needs no utility level at all; the other two gain 0.31 and 0.60 of R² from it.

**F6. Λ per class, which is H1's test.** Each class's R² depends only on its own Λ.
- **max**: rises to 0.953 at Λ = 8 and is then **flat to Λ = 2048**. The data put no upper bound on
  its lexical strength; they are consistent with the hard entry of the Λ → ∞ limit.
- **min**: peaks at **Λ ≈ 32** (0.401) and falls away on both sides, to 0.325 by Λ = 512.
- **rel**: peaks at **Λ ≈ 16** (0.800) with the cut between positions 3 and 4, and falls to 0.756.

So a **finite** Λ is required by the minimum and relative classes and not by the maximum class,
which is H1's content: the class whose threshold is the scale's own endpoint behaves as a hard
constraint, and the two classes whose thresholds depend on something unstable do not. The ordering
of the two finite optima is min (32) above rel (16).

**F7. The relative cut.** Best at the boundary between positions 3 and 4, s = 0.625 — just above the
midpoint, which is where the paper puts the class ("clustered mainly on degrees above the
mid-point"). At s = 0.375 the optimum is Λ = 24 (0.799) and at s = 0.875 it is Λ = 6 (0.781), so the
cut and Λ trade off and neither is identified alone.

**F8. The image-type effect: right class, right sign, far too small.** The authors find one credible
image-type effect, and it is the minimum class's, in both experiments. Shape minus artifact, in mean
scale position:

| | max | min | rel |
|---|---|---|---|
| their elicited prior | +0.84 | −1.12 | −0.00 |
| their Experiment 3 | −0.22 | **−1.13** | +0.23 |
| this model, fitted Λ | +0.03 | **−0.16** | +0.01 |

The model puts the effect in the minimum class and nowhere else, which is the empirical pattern, but
at one seventh of its size.

**F9. Why, and what would fix it.** At the fitted Λ the entry has already overridden the prior, so
the prior's own −1.12 cannot reach the belief. The model reproduces the −1.13 only at **Λ ≲ 2**,
where the minimum class's R² collapses (0.19 shape, 0.005 artifact). Split by condition, the two
halves want different lexical strengths: by mean position, **shapes want Λ ≈ 6 and artifacts Λ ≈ 24**;
by R², the artifact half reaches 0.86 at Λ = 24 to 64 while the shape half reaches only 0.24, at
Λ ≈ 0.5 to 1. **No single Λ fits both halves of the minimum class.**

That is H1 in a sharper, within-class form: the same adjectives carry a weaker lexical strength when
predicated of novel shapes than of familiar artifacts — which is what "unstable atomicity" would
say, since what counts as one bump or one stripe is fixed by familiarity with the object. Nothing
else in the model produces the effect: m = 3 and m = 4 leave it at −0.17 and −0.04 (and m = 4 costs
the minimum class two thirds of its R²), and the utility level's amplification of the span-B
component of ℓ₀ − φ_L (Eq. 24) is what flattens the prior's contribution at any m the basis allows.

**F10. What the minimum class actually does, and the model does not.** Both conditions move the
belief up from the prior by about the same amount — 1.19 → 3.29 and 2.31 → 4.42, +2.10 and +2.11
positions — while the model moves it to a place fixed by the entry and Λ rather than by a
displacement. Reproducing a constant displacement is not something Λ can do at fixed θ\*.

**F11. The between-class interaction §5.2 claims is there, attenuated.** The gap between the maximum
and minimum classes is larger in the shape condition than the artifact condition, in the data
(1.32 against 0.41) and in the model (0.61 against 0.42).

**F12. §5.2's and background §1.7's description of the prior manipulation is backwards.** Both call
shapes the impoverished-prior condition and artifacts the rich-prior one. What the authors report
about the elicited priors is the opposite: "artifacts tend to have a less categorical distribution
than shapes, in particular for the dimensions corresponding to absolute adjectives" (9:19), and
their own data bear it out — the shape priors are the peaked ones: the minimum class's elicited
prior has mean position 1.19 for shapes against 2.31 for artifacts, and the maximum class's 4.36
against 3.52. The shape condition is
impoverished in world knowledge and **sharper**, not flatter, in elicited prior. Whatever §5.2 says
about prior sharpness has to be stated on the elicited priors, not on the labels.

**F13. What no longer stands in §5.2's own terms.** The prediction as written is a monotone trend in
the cut's position under a flat prior, reversing under a sharp one. The comparison the data make is
not that: the three classes differ in **which cut** they carry and in **Λ**, and the prior
manipulation is not a sharpening of one prior but two elicited sets. The 2026-09-14 findings stand
(the numbers were θ_u = 1 controls or a carried θ\*; "monotonically" fails; the tilt carries the
contribution). The parity result about κ is untouched.

**F14 (2026-09-17, for S-2). A relative adjective's cut is not identified by the data.** Best R² for
the relative class, each candidate cut with its own Λ scan: midpoint 0.793 (Λ 16), the item's own
prior median 0.795 (Λ 24), its prior upper quartile 0.797 (Λ 16), cell boundary s = 0.375 0.799
(Λ 24), s = 0.625 0.800 (Λ 16), s = 0.875 0.781 (Λ 6). A spread of 0.019 across every plausible
choice, so **t need not be fitted**: stipulating the midpoint costs 0.007 against the best cut.

**F15 (2026-09-17, for S-7). The parity of the three classes' loadings at n = 4**, κ = BᵀWχ:

| entry | cut (s) | tilt | width | \|width/tilt\| |
|---|---:|---:|---:|---:|
| MAX = *all* | 0.875 | −1.33667 | −0.56936 | 0.426 |
| MIN = *some* | 0.125 | −1.33667 | **+0.56936** | 0.426 |
| REL, cut at the midpoint | 0.500 | −1.49985 | **+0.00000** | 0 |
| REL, cut at s = 0.625 | 0.625 | −1.48785 | −0.17284 | 0.116 |

**The maximum and minimum entries share their tilt exactly and differ only in the sign of their
width**, and a midpoint cut is the one entry with no even component at all (the node on the cut
half-weighted, as the 2026-09-14 numerical note says). An antonym's κ is exactly the negative of the
entry's, to 2.2e-16, since B is orthogonal to the constant.

**F16 (2026-09-17, for S-2). None of H2's inventories forces m = 2.** Every one of them is a
complementary pair, so by Appendix C §5 its span modulo the constant is 1, measured as 1 for all
four tested. The model carries m = 2 as a property of the architecture, not because these
inventories demand it. This is not the collapse Eq. (C3) reports for an odd m = 1 basis: the pair's
two loadings are opposite, not equal, so the utility level is not common-mode on them.

**F17 (2026-09-17, the section as S-2 finally scopes it).** The two absolute classes only, 56 of the
96 items, no cut *t* anywhere. R² of our own predictions against their Experiment 3:

| | max | min | both classes |
|---|---:|---:|---:|
| the model at θ\* | 0.953 | 0.401 | **0.804** |
| the tempered control | 0.951 | 0.208 | 0.789 |
| the literal listener | 0.952 | 0.092 | 0.728 |

So the utility level's whole contribution sits in the minimum class, and the maximum class is
indifferent to it (0.952 against 0.953). Λ scanned per class: max reaches 0.953 at Λ = 8 and is flat
to Λ = 2048; min peaks at 0.401 at Λ = 32 and falls to 0.325. Shape minus artifact in mean scale
position: prior +0.84 / −1.12, data −0.22 / −1.13, model +0.03 / −0.16. The gap between the two
classes: data +1.32 (shape) against +0.41 (artifact), model +0.61 against +0.42.

**F18 (2026-09-17, for O14). The parity of the two entries holds only while one θ fixes both ends.**
κ for *some* at n = 4 is (tilt −1.33667, width +0.56936), fixed by the 0 boundary. Moving the 1
boundary alone, with the 0 boundary held:

| θ_A | cut in s | tilt | width | tilt − tilt(*some*) | width + width(*some*) |
|---:|---:|---:|---:|---:|---:|
| 0.50 θ_L | 0.7257 | −1.45665 | −0.31963 | −0.11999 | +0.24973 |
| 0.80 θ_L | 0.8259 | −1.40626 | −0.45378 | −0.06959 | +0.11557 |
| **θ_L** | 0.8750 | −1.33667 | −0.56936 | **+0.00000** | **+0.00000** |
| 1.25 θ_L | 0.9193 | −1.24788 | −0.66040 | +0.08879 | −0.09105 |
| 2.00 θ_L | 0.9800 | −0.86631 | −0.72692 | +0.47035 | −0.15757 |

The identical tilts and cancelling widths are a consequence of θ_A = θ_L, not of anything else, so
the parity paragraph S-7 keeps is exactly the statement O14's instinct doubts. **This measures what
the symmetry rests on; it does not test the instinct, and nothing here says the symmetry accounts
for the mismatch (R16).**

**F19 (2026-09-17, for O14 and O10). The n = 1 degeneracy is a property of the single θ, not of n.**
Building Eq. (A1) with the 0 boundary at −θ_L and the 1 boundary at θ_A, and taking the Gram rank of
the three χ_y as O10 and Eq. (C2) do:

| θ_L | θ_A | n | rank | rank mod **1** | max \|χ_some − χ_all\| | |
|---:|---:|---:|---:|---:|---:|---|
| log 7 | log 7 | 4 | 3 | 2 | 1.0000 | the model |
| 0 | 0 | 1 | **2** | **1** | **0.0000** | O10's degeneracy: the entries coincide |
| 0 | log 7 | 1 | 3 | 2 | 1.0000 | 0 boundary at n = 1, 1 boundary kept |
| 0 | 0.5 | 1 | 3 | 2 | 1.0000 | both moved, still distinct |
| log 7 | 0 | 4 | 3 | 2 | 1.0000 | the 1 boundary at the midpoint |

So **representationally** the user's instinct holds: separate the two boundaries and n = 1 no longer
collapses *some* into *all*, and the inventory keeps the two thresholds Eq. (C2) counts. The last row
is the configuration in which a relative adjective's cut would be θ_A at the midpoint, with the 0
boundary left where n puts it.

**What this does not settle**, and what keeps it an instinct rather than a result:
- Nothing here is dynamical. The user's instinct is that an architecture with an alternatives level
  has different dynamics; no dynamics were run, and none can be until such an architecture exists.
- **Eq. (A2)'s gain.** θ_L is the gain of g_y as well as a cut, so θ_L = 0 zeroes the word-form
  prediction whatever θ_A does. Whether that survives the separation depends on which θ gains which
  row of A, which is undetermined. It is the one obstacle the rank test does not touch.

**F20 (2026-09-21, for O8). The paradigm detail, read off the paper itself.** Checked against
Xiang, Kennedy, Xu & Leffel (2022), *Semantics and Pragmatics* 15(9), Secs. 2.1.1, 2.2.1 and 2.3.1
(PDF from semprag.org; not copied into the repository).

- **Experiment 2 (truth value).** 48 image sets, each paired separately with each member of an
  antonym pair = 96 items. Artifact and shape items were run on **two separate groups**. The items
  "were distributed in a latin-square fashion such that the same participant did not see both
  adjectives that were paired to the same image set", and "each participant, therefore, only saw 24
  trials total".
- **Experiment 3 (posterior degrees).** "The image sets and adjectives used for this experiment, as
  well as the procedure to pair together the images and adjectives and to distribute them among
  participants, were identical to Experiment 2." Separate groups again (67 shape, 68 artifact).
- **So no participant heard both members of a pair about the same images.** Whether a participant
  met both members across *different* image sets is not stated: each pair was used for two image
  sets, and the paper constrains only the same-image-set case.
- **Experiment 1 (priors) used no adjective at all** — "Which of these is the most likely?", one
  choice per image set, no adjective mentioned. The by-item prior is therefore **adjective-free**,
  which is how the audit uses it; the by-adjective figure averages items for visualization only.
  Scale position 1 is the least and 5 the most of the property, which is the authors' own coding and
  is what "in the adjective's own orientation" means.
- **A lexical detail that does not disturb the ensemble.** A few adjectives sit in more than one
  pair (*short* with *long* and with *tall*; *straight* with *bent* and with *curved*), so the
  partner is not a function of the adjective alone. In this phase's representation it makes no
  difference: any minimum-standard partner of a maximum-standard entry is its complement whatever
  the word is, because the ensemble is fixed by class and one θ, not by lexical identity.

**What F20 settles, and what it does not.** It removes one justification and leaves the conclusion
standing, for the reason the user gave on 2026-09-21: *presence in the inventory follows from
exposure in the experiment, but not the converse* — a participant not shown *plain* in the
experiment has still met it elsewhere. So {χ, 1 − χ} **cannot be argued from experimental exposure**,
since the latin square denies it; it is argued, if at all, from the **inventory a speaker of English
has**, which the experiment neither creates nor limits. §5.2 must say it that way.

## 6. What is open

- **O13** (new): whether H1 and H2 are adopted, and if so what fixes Λ. Nothing was changed.
- **O8**: F1 and the antonym structure answer the ensemble question for this paradigm ({χ, 1 − χ});
  the Λ question is now sharper, not settled — F9 says the data want Λ to vary within a class.
  **2026-09-21: O8 is settled in both halves.** The Λ half by S-9 above; the ensemble half by the
  user's decision **A18** — the ensemble is architectural, {χ, ker χ}, and an antonym is never needed
  to define an entry. For these absolute classes ant(x) **coincides** with ker(x) in this phase, a
  prediction of the single θ, not a definition. **Wording constraint on T2's block 1 and T10's
  prose:** state the ensemble as the **inventory's**, never as the experiment's — F20 shows the latin
  square denies the exposure reading — and make no claim about antonymy.
- **Q7** in `revisions.md`: three of its four choices are now answerable from measurement, and the
  fourth (the empirical-fit paragraph) needs F12 either way.
- Every number here is class (e) under `agent.md` §3.3 until a cell prints it (C6). Whether any of
  it should reach a cell is the user's call, and it would need a decision about a five-position
  configuration the notebooks do not currently contain.

---

# The change this record now covers: §5.2 rewritten, and Appendix F

## 7. The user's instruction, verbatim (2026-09-17, second message)

> Here's my take: for this section, state both H1 and H2, then report where the model's prediction
> match Xiang's data as well as where it doesn't. Refrain from making any claims on the nature of
> this mismatch. Every data quoted in this section must be reproducible. Add a new appendix F to
> main.ipynb printing the model results quoted in this section. Now update revisions.md and
> work-process documentations listing all the tasks that need to be done for this change. Do not
> start the edits and implementations yet.

Read with `agent.md` §3.1 and C6: the section states the two hypotheses, reports match and mismatch,
and stops there; **no sentence characterizes what the mismatch is due to**, which rules out the
mechanism sentences §5.2 now has and also rules out F9's and F10's readings, which stay in this
record. "Every data quoted must be reproducible" is C6 made specific to this section: a number in
§5.2 exists only if Code Cell F prints it.

**Why F and not E.** `appendix_E.ipynb` holds Appendix E. The next free letter in `main.ipynb` is F,
and the user named it.

## 8. What must be settled before any code (blocking)

None of these is the agent's to decide (`agent.md` §3.1, §5.4). Each is listed with what it changes.

**Answered by the user, 2026-09-17 (second message of the day):**
- **S-1 — settled, option (ii) in effect but bounded.** "the point of H1 is about a fitted Lambda;
  for H1 and only for H1 this is allowed since it is part of the hypothesis's commitment." So Λ is a
  fitted quantity **here and nowhere else**, because H1 is a claim about Λ, and it is labelled as
  fitted where it is printed. Nothing else in §5.2 or Appendix F may be fitted — which is what makes
  S-2 a live question rather than a matter of fitting *t* too.
- **S-3 — settled.** The data live in the repository.
- **S-4 — settled.** n = 4.
- **S-5 — settled, the opposite of the agent's reading.** "do not print published number; any
  published number should appear in the paper with proper citation; the code is only to print our
  own predictions." So Code Cell F prints the model's own quantities only; their LG/QF/ST/hybrid R²
  values are cited in §5.2's prose, and the by-item R² of **our** predictions against their data is
  ours to print.
- **S-6 — settled.** The word budget rises as needed.
- **S-7 — settled, the agent's recommendation.** The parity paragraph stays in §5.2, restated for
  n = 4, with its numbers printed by Code Cell F. Under the scope S-2 sets, what it states is that
  **the maximum and minimum entries differ in the even (width) coordinate alone**: their tilts are
  identical to 0.0e+00 and their widths sum to 0.0e+00 (F15, F17e). The general parity statement —
  that a cut at the midpoint of the log-odds scale would carry no even component at all, measured
  1.2e-17 with the node on the cut half-weighted — is kept as a statement, not as a modelled class.
  The old ratios 0.219 / 0.633 / 1.07 go with the old prediction; they were n = 10 cuts.
- **S-2 — settled: the relative class is not modelled.** The user's reasoning, verbatim
  (2026-09-17):

  > even though we currently model the two endpoint as symmetric to each other, I do not think it is
  > actually the case. Recall our motivation for an alternatives level; under this proposed
  > architecture, the 0 and the 1 would no longer be defined by the same theta, but instead theta_L
  > and theta_A. I think our current model's symmetricity is the culprit of mismatch that we have
  > with Xiang's data. My instinct is that n can be properly represented by the architecture
  > (particularly as one of theta_L or theta_A) once the two thetas are separated from each other.
  > However, we want to avoid making too many promises in the paper over things we haven't
  > implemented yet, so my take is that we point to this intinct and leave it as an instinct. Thus,
  > we do not try to model the relative class with our current implementation.

  And the clarification that followed, verbatim:

  > I need to clarify that theta_L is the lexical level's property, and only theta_A is meant to be
  > the alternative level's property. The lexical level infers the boundary of 0, and the
  > alternative level infers the boundary of 1.

  And the correction that followed, which is what the instinct is actually about:

  > I'm sorry for mispeaking earlier, but I meant the midpoint t of the relative class can be
  > properly represented by one of theta_L or theta_A. As for n, we my instinct is that it is still
  > dependent on theta_L. However, since an architecture with an alternatives level has different
  > dynamics, it is well possible that n=1 no longer causes degeneracy.

  So the quantity the separation would represent is **t**, the relative class's midpoint, not n; n
  stays with θ_L. S-2's decision is unchanged: the relative class is not modelled here.

  Recorded as `decisions.md` **O14**. What follows for this change:
  - **No cut *t* enters the model.** Appendix A's identification argument and its "θ_L enters twice"
    paragraph are untouched, and the objection that motivated S-2 does not arise.
  - **§5.2 still states H2 in full** (the user's first instruction) and says plainly that its
    open-scale half is not tested here, pointing to the instinct. It must not report the relative
    class's 0.80, since that number comes from a configuration the model does not have.
  - **The instinct is stated as an instinct**, once, with no promise attached and no claim that it
    accounts for the mismatch. Placement: the agent recommends the close of §5.2, pointing back to
    §5.1 where an alternatives level is proposed, since θ_A is the quantity that would need a level
    to carry it. Confirm the placement at T10. §5.1 itself gains nothing: naming θ_A among what the
    level "would have to supply" would turn the instinct into a promise.
  - **The parity paragraph is where the symmetry the instinct doubts is actually stated**, which is
    why S-7 keeping it matters more under this scope than it did before.

- **S-1. Is Λ fitted, and if so what class of quantity is a fitted Λ?** The section's Λ numbers come
  from choosing, per class, the Λ that best matches their data. Nothing in this project is fitted;
  the four classes of `agent.md` §3.3 have no room for a fitted parameter, so a quoted best-fit Λ is
  class (e) as things stand. Options: **(i)** quote the whole Λ scan and no single value, which
  keeps §5.2's standing "no fit is offered" sentence true and still carries F6's result (a finite Λ
  is required by two classes and not by the third); **(ii)** declare a fitted quantity as a fifth
  class in `agent.md` §3.3 and record each fitted Λ under it; **(iii)** fix Λ = 8 for every class,
  which loses F6 and most of F4. The agent's reading is that (i) is the only option that leaves the
  rest of the paper's standards intact, but the choice is the user's.
- **S-2. Does the relative class enter at all?** A relative adjective's cut *t* is neither an
  endpoint nor 1/2n, so it is a quantity of the entry that Text cell 3 §2's inventory does not have,
  and Appendix A's identification argument is written for a θ_L that is both the gain of Eq. (A2)
  and the cut of Eq. (A1). Options: declare *t* (which opens A5 and Appendix A's "θ_L enters
  twice"); or restrict §5.2 and Appendix F to the two absolute classes, losing H2's open-scale half
  and the .80 that is the model's best class after the maximum one.
- **S-3. May their data live in the repository?** R² is a statistic of the model **against their
  data**, so Code Cell F cannot print it unless the data are present. Options: **(i)** commit the
  34 KB derived aggregate (96 items × 5 positions: elicited prior, Experiment 3 posterior,
  Experiment 2 judgment, class) with a README giving provenance, licence (CC-BY) and sha256, and
  have Code Cell F read it; **(ii)** embed the 480 numbers in the cell; **(iii)** quote no R² and
  restrict §5.2 to profile comparisons, which are still model-versus-data but need only the six
  class profiles. The agent's reading is (i).
- **S-4. n = 4.** Appendix F respawns the network at n = 4 so that Eq. (A5)'s cells are their five
  scale positions. This is a setting of an existing quantity (class (a)) and needs a decisions.md
  entry saying why 4 and that the default n = 10 is untouched. Confirm.
- **S-5. May a cell print a published number?** The comparison quotes their LG/QF/ST/hybrid R²
  values. Printing a literature value inside a cell is new; the alternative is to cite them in the
  markdown and print only ours. Confirm which.
- **S-6. The word budget.** §5.2 is allocated 200 words (revisions.md §3). Stating H1 and H2,
  the instantiation, the matches and the mismatches will not fit. Estimate 340–380. Either §5
  absorbs it (from §5.1's 350, the only section with slack), or the 3,000 total rises. The user's
  call.
- **S-7. Does §5.2 keep its parity paragraph?** The κ parity result survives (2026-09-14 finding 6)
  but belongs to the old prediction, not to H1/H2. Keep, move to Appendix C, or drop.

**Raised 2026-09-21, SETTLED 2026-09-22 — S-8.** The user asked that **how the evaluation varies with
n** be reported in the notebook and in the paper, the finding currently sitting in
`procedure_records/side_quests_mirror_and_granularity.md` (F6–F10, decision **O10**). Two things are
the user's to settle:
1. **Where it goes in the paper.** (a) §4, as a property of the evaluation, since it says which side
   of a crossing the reported verdicts sit on; (b) §5.2, next to H1, since n is what atomicity
   fixes and H1 is about exactly that instability; (c) §5.5 Limits, one sentence. **Recommendation:
   (a) with one clause in §5.2**, because F9 is a fact about the criterion's readings, which §4
   reports, while H1's claim concerns Λ, not n. It costs about 60 words in §4 and 15 in §5.2.
2. **Which cell prints it, and how wide the sweep is.** The side quest measured n at Λ = 8 under two
   priors only. Options: the existing Code Cell A (Appendix A owns θ_L and n); a block in Code
   Cell F, which is being written anyway; or a new cell. **Recommendation: Code Cell A**, since
   Eq. (A5) is where n gets its denotation, and a sweep of n against the two priors already reported,
   at Λ = 8 and at Λ = 512, so the paper can say whether the crossings move with Λ (the side quest
   did not check, and §4.4 now reports at Λ = 512).

**Both recommendations taken, 2026-09-22, with one widening.** (a) §4.2 carries it, as a second
guard beside the softmax-nonlinearity guard, with a clause in §5.2's *Calibrate the claim* bullet;
(b) Code Cell A prints it. The widening: the sweep runs **all four `BASE_WORLD_PRIORS`**, not the
two the side quest used, because the two were `gaussian` and `skewed high` under ad-hoc names and
the inconsistency was itself a `agent.md` §5.5 violation. It cost nothing — the block runs in
under 0.1 s — and it is what exposed the degenerate-ray crossing under `flat` (F7 qualified).

**The budget moved.** S-8 estimated 60 words in §4 and 15 in §5.2. §4.2 took about **90**, because
the finding grew two qualifications the estimate did not anticipate (bracketing, and magnitude), and
a third result (non-separability from Λ) that the side quest had listed as unchecked. §4.2 goes
170 → 260 and the §§3–6 total 3,520 → 3,610, recorded as **R25** in `revisions.md`.

**One instruction overrode part of T14 as written.** The user, 2026-09-22: *"We want q-shift,
q-position, mode shift, and mode position status to be explicitly printed for every (n, Lambda,
ell_0) combination. Whether there is a flip or not is to be clarified in text, not the printed
report."* T14's acceptance clause "the crossings of F9 are **printed** rather than described" is
therefore **superseded**: the report prints per-row *statuses*, and the crossings are described in
Appendix A's prose and in §4.2. The first draft of the block violated this (it carried crossing
language in its header and docstring) and was rewritten.

**Settled 2026-09-21 — S-9. One fitted Λ per class, not per (class, image type).** The user's
reason: a constrained model should carry as few fitted quantities as possible. Fitting per image
type would entail that lexical strength depends on class **and** image type, a stipulation the user
does **not** call implausible; the paper opts out of the extra fit rather than arguing against the
dependence. Consequences for the tasks: **T2 block 4** keeps its per-class scan; **T2 block 5** keeps
the image-type difference as a measured difference, and may print the two best-fitting Λ of the
minimum class (F9: shapes ≈ 6, artifacts ≈ 24) **labelled as a property of the fit, not as a fitted
parameter**; **T10's prose** may never write that Λ is independent of image type — only that no
second Λ was fitted, and why. `decisions.md` **O8**.

## 9. Tasks, in order

Code before prose (`agent.md` §5.3). Nothing below starts until S-1 to S-7 are answered.

**Ordering, 2026-09-17.** The user has put another change ahead of this list: the Λ–ℓ₀
counterforce and where ℓ₀ enters, `procedure_records/ell0_placement_and_counterforce.md`, tasks
U0–U14. T0–T13 follow it. The two lists touch no common cell — that change works on Appendix D,
Code Cell D and §§3–4, this one adds Appendix F and rewrites §5.2 — but both renumber nothing and
both regenerate the ToC, so whichever runs second re-checks cell indices before T4/U5.

- [x] **T0. Checkpoint.** — done 2026-09-22 at `ae2f414`; tree clean but for three untracked backups.
      (The list was written at `acabb7e`; the U0–U14 change and T14–T16 landed in between.)
      **As specified:** **T0. Checkpoint.** `git status` clean, record `git rev-parse --short HEAD`. The tree is clean
      at `acabb7e` as this list is written.
- [x] **T1. The data file** — done 2026-09-22. `data/xiang_2022/` holds `xiang_items.csv` (sha256
      `c23d930d…`, 480 rows, 96 items), `README.md` with the OSF node, the four source files, the
      smoothing rule, CC-BY and the hash, and `check_data.py`, which verifies the hash and reprints
      the six empirical class profiles. **The derivation script does not exist and could not be
      written:** the four OSF files were never vendored and the 2026-09-17 derivation kept only its
      result. The user settled this the same day — ship the aggregate with its provenance — so the
      README says plainly that the hash pins the file and certifies nothing about the derivation
      (`decisions.md` A20). Running the check exposed a defect in the record: **F1's table below is
      internally inconsistent**, its two `shape` rows renormalized while their mean positions were
      not. See the correction under §5.
      **As specified:** **T1. The data file** (S-3 settled: yes). Add the derived aggregate under a new `data/xiang_2022/`
      with `README.md` giving the OSF node, the four source files, the derivation, the licence and a
      sha256 per file; add the derivation script beside it. Acceptance: the README's hashes match,
      and a fresh read of the file reproduces the six class profiles in §5 F1 above.
- [x] **T2. Code Cell F** — done 2026-09-22, cell 23 of `main.ipynb`, 8 blocks, 130 lines of output,
      0.3 s. All eight blocks as specified, with three departures forced by what was found:
      **(i)** the relative class carries no prediction anywhere (S-2/O14), so block 6's
      "between-class gaps" is maximum against minimum and block 3's "overall" pools the two absolute
      classes; **(ii)** the fitted Λ of the minimum class is **48**, not the audit's 32, once the
      absent item is dropped, and the cell prints the **bracket** (32 to 48) rather than presenting
      the argmax as located — R25's lesson applied again; **(iii)** every helper takes *fields*
      rather than utterance names, because `ker χ_all` is a field no utterance names, and block 1
      checks both against `closed_form_fixed_point` and `theta_u_stationary_points` (0.0e+00 on
      each). `code cell 1` untouched, coupling 9 quiet, no figure, no `cost:` line needed.
      **As specified:** **T2. Code Cell F** (S-1 to S-7 settled). A new code cell printing every number §5.2 will quote,
      and nothing else. Its blocks:
      1. **Configuration and self-checks.** n = 4, θ_L = log 7, the five cells and their boundaries;
         the three entries of Eq. (A1) in the adjective's own orientation and the complement that
         each item's antonym supplies; that the audit's closed form equals `closed_form_fixed_point`
         (expect 0.0); that the closed-form θ\* equals a scan (expect ~6e-06) and returns −28.4375
         for the default n = 10 inventory; that a uniform five-cell prior pushes forward to
         [0.193, 0.200, 0.214, 0.200, 0.193]; that the five cells partition the grid to 1e-10.
      2. **The class profiles**, prior / q_lit / model / data, for the two absolute classes by image
         type, with the peak and the mean scale position.
      3. **R²** by class and overall, for the model and for q_lit — **ours only** (S-5). Their
         published values are cited in §5.2's prose and printed nowhere.
      4. **The Λ scan per class**, wide enough to show that the maximum class is flat to Λ = 2048
         and that the minimum class turns over at Λ = 32. Λ is labelled as fitted, and as fitted for
         H1 alone (S-1).
      5. **The image-type difference** per class, in prior, data and model.
      6. **The between-class gaps** by image condition.
      7. **The mismatch quantities**: the minimum class's R², the −0.16 against −1.13, and the
         displacement from prior to posterior in both conditions. Reported, not explained (R16).
      8. **The parity of the two entries' loadings** (S-7): κ for *all* and for *some* at n = 4,
         their identical tilt, their opposite width, and the midpoint statement.
      Constraints: every helper stays local to this cell, so `code cell 1` is untouched and coupling
      9 does not fire; no figure, so the figure baseline is unchanged; any wall-clock line goes
      behind `cost:` (coupling 3). Acceptance: the cell prints every number the drafted §5.2 quotes,
      and no number in §5.2 is absent from it.
- [x] **T3. Appendix F markdown cell.** — done 2026-09-22, cell 22, anchors `appf`, `appf-1`…`appf-6`
      and `codef` at its end; Eqs. (F1)–(F2). Six sections: the two hypotheses, what is instantiated
      and what is not, what is measured, what matches, what does not, and the parity at n = 4. No
      sentence says what any mismatch is due to.
      **As specified:** **T3. Appendix F markdown cell.** Heading with anchor `appf`, the `codef` anchor at its end.
      Content: H1 and H2 as stated by the user; the instantiation (five positions = five Voronoi
      cells at n = 4, the three entries, the complement ensemble); what is measured and how R² is
      computed; then match and mismatch, reported and not explained. Displays, if any, numbered F1,
      F2 … (appendix letters restart, so the body's (1)–(41) is untouched and no renumbering
      question arises). No sentence about what the mismatch is due to.
- [x] **T4. Structure.** — done 2026-09-22. Inserted after Code Cell D at 22 and 23; References moved
      to 24; 23 → 25 cells. ToC regenerated with the eight new rows.
      **As specified:** **T4. Structure.** Insert the two cells after Code Cell D (index 21), before References, which
      becomes index 24; cell count 23 → 25. Regenerate the ToC (cell 0) with rows for 22 and 23 and
      the moved References row. Acceptance: every ToC link resolves and every index in it is right.
- [x] **T5. References.** — done 2026-09-22. Kennedy (2007) and Xiang et al. (2022) added to the
      notebook's References in alphabetical position. **The pending Leffel-versus-Xiang check is
      decided: the manuscript is dropped.** The published 2022 article reports the shapes/artifacts
      contrast itself, so it is cited alone, in `background_sections.md` §1.7 and its reference
      list, and in `sections_3-6.md` §5.2 and its sources.
      **As specified:** **T5. References.** Add Xiang, Kennedy, Xu & Leffel (2022), and Kennedy (2007) if §5.2 names
      the open-scale class it does not model, APA 7th, in alphabetical position. The pending
      Leffel-versus-Xiang check (`background_sections.md` line 612) is decided here. Their LG/QF/ST
      and hybrid R² values are cited in the prose and printed by no cell (S-5).
- [x] **T6. Couplings.** — done 2026-09-22. None of the nine fires: Code Cells 2 and 2b untouched
      (1, 7), the new cell's prefix is `# === Code Cell F:` and not E3's two (2), no wall-clock line
      (3), main executed before appendix_E (4), the dangling-reference check returns `[]` on both
      notebooks with F1 and F2 defined (5), anchors added and ToC regenerated (6), no stdout tee (8),
      `code cell 1` untouched (9). **One new coupling was needed and is recorded as coupling 10:**
      Code Cell F is the only cell in either notebook that reads a file, by a path relative to the
      project folder. E.3 gains Appendix F in its *Unaffected* list.
      **As specified:** **T6. Couplings.** Confirm none fires: E3 diffs Code Cells 2 and 2b only; `code cell 1` is
      unchanged so coupling 9 is quiet; no new printing call in Code Cell 2 or 2b, so coupling 7 is
      quiet. Check whether `appendix_E.ipynb` §E.3 ("claims in main restated") needs a line.
- [ ] **T7. Execute** main, then appendix_E, by `agent.md` §5.1. Acceptance: main 0 errors,
      8 figures, 14/14; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS on both cells. Record the
      new runtime. Diff every other cell's stored output against T0: only the two new cells may
      differ.
- [x] **T8. agent.md.** — done 2026-09-22. §1's cell map 23 → 25 with rows for 22, 23 and References
      at 24; §2 gains coupling 10 (the data-file path) and a loud dependency (Code Cell F reads
      `evaluation_network` from Code Cell 2); §5.1's baseline updated.
      **As specified:** **T8. agent.md.** §1's `main.ipynb` cell map (23 → 25 cells, the new rows, References at 24)
      and §5.1's baseline. §2 needs no new coupling if T6 holds; if Code Cell F reads the data file,
      add a coupling for that path.
- [x] **T9. decisions.md.** — done 2026-09-22. New **A20** (n = 4, the fitted Λ and its scope, the
      data file and what its hash does and does not certify, the relative class's exclusion, the
      bracket). New register-E entry **E16**, classing every quantity Code Cell F prints and
      recording the absent-item defect. **O13 rewritten**: its audit numbers are marked superseded
      and the printed values take their place. **O8** gains the pointer to what Code Cell F builds.
      **As specified:** **T9. decisions.md.** New entries or amendments for whatever S-1 to S-5 settle: the n = 4
      configuration; the treatment of Λ; *t*, if it enters; the data file and its provenance;
      O13's status. Quantity-trace (register E) entries for every quantity Code Cell F prints, each
      assigned a class under §3.3. O8 gains the pointer.
- [x] **T10. §5.2 prose** — done 2026-09-22, written against the executed output. 400 → **550 words**
      (§§3–6 total → 3,760), retitled *Scale structure: two hypotheses, and where the model matches*.
      The old prediction (the monotone trend in the cut's position, reversing under a sharp prior) is
      withdrawn per F13; the parity paragraph is kept and restated at n = 4. X7's wording constraint
      honoured. **The instinct sits at the close of §5.2, pointing back to §5.1** — the user's choice
      of site, 2026-09-22. Scope-tier row and word table updated; both add up.
      **As specified:** **T10. §5.2 prose**, written against the executed output, not before.
      **Wording constraint from X7 (`exposure_stipulation.md`, applied 2026-09-22).** §5.2 states
      the ensemble as **the inventory's, not the experiment's**. F20 records that Xiang et al.'s
      latin square denies the exposure reading — no participant saw both adjectives of an image set
      — and the user's principle is that presence in the inventory follows from exposure somewhere
      but **not** conversely, so what a participant was shown constrains nothing about membership.
      §5.2 may also say that for these absolute classes, in this phase, $\mathrm{ant}$ coincides
      with $\ker$; it may **not** advance a thesis about antonymy, which is a lexical accident of
      two words sharing a scale and is not an involution (A18). §5.2 goes to about 400 words and the §§3–6 total to 3,200 (S-6). Confirm the instinct sentence's placement with the user. Also
      the §5.2 row of the word table in `sections_3-6.md` lines 81–103 and its scope-tier row at
      line 60.
- [x] **T11. Background §1.7.** — done 2026-09-22. F12's backwards bullet replaced: the manipulation
      is stated as novel versus familiar objects, with the elicited priors' actual direction given
      (artifacts are the **less** categorical). Q3b softened from "§5.2 answers it" to "§5.2 takes it
      up", with the reason.
      **As specified:** **T11. Background §1.7.** The prior-manipulation bullet (F12), and the Q3b sentence softened
      per the 2026-09-14 entry. `background_sections.md` line numbers are one lower than
      revisions.md cites, after R8.
- [x] **T12. revisions.md.** — done 2026-09-22. The §5.2 entry and **Q7 both marked CLOSED**, each
      keeping its old assessment beneath as the record; §8's source row now points at Code Cell F and
      says which audit numbers stay class (e) and reach no prose; §3's budget → 3,760; **R26** added.
      **As specified:** **T12. revisions.md.** Mark the §5.2 entry and Q7 closed by this change; update §8's source
      table so the numbers point at Code Cell F rather than at the audit; clear the audit from the
      class (e) list.
- [ ] **T13. Commit**, one logical change per commit, hashes recorded on each task line above.

**Added 2026-09-21 at the user's request (decision O10). Blocked on S-8.**

- [x] **T14. Print how the evaluation varies with n.** — done 2026-09-22, `2068268`. The cell S-8 settles prints, for the priors
      and lexical strengths S-8 fixes: θ_L = log(2n − 1) at each n, θ_u\*, the two q criteria and the
      two mode criteria for *some*, and the κ separation of F10. Acceptance: the numbers of F7–F10
      that the prose will quote are reproduced by the cell (they are class (e) until then), the
      crossings of F9 are printed rather than described, and no figure is added unless S-8 asks for
      one. n = 1 stays rejected by the constructor (F8).
      **As executed:** 80 rows (n × Λ × all four base priors), each printing θ_L,
      ⟨μ_u, Σc⟩, θ_u\*, the q shift, P(all∣*some*), the mode step and the **status of all four
      criteria**; then the κ ladder (F10) and the n = 1 refusal (F8). Two defects in the pre-existing
      block were fixed on the way: the mode shift was measured against the **tempered** fixed point
      rather than **ℓ_0**, disagreeing with Code Cells 2 and 4 (`agent.md` §5.5); and the q shift was
      printed to four decimals, so a status change appeared between two numbers both shown as
      0.0000. F7 is qualified and F9 extended in the side-quest record.
- [x] **T15. The prose** — done 2026-09-22. As specified: at the site S-8 settles; n = 10 is a stipulation (O1), not a neutral choice
      of units; the criteria's readings cross with n; m = 2 and the rank results do not move (F7);
      n = 2 is not degenerate and n = 1 is (F8). Written against T14's output. Whether this entails
      anything about O1 is **not** claimed here.
      **As executed:** §4.2's second guard (about 90 words) and a clause in §5.2. The phrase "the
      criteria's readings **cross** with n" is **not** used: per the user's 2026-09-22 instruction
      and F9-extended, the prose says which criteria *change status* where, that a sweep brackets
      rather than locates the change, and that one such change is a sign flip at −7.593e-07. The
      O1 non-claim is honoured and stated in both `decisions.md` O1 and R25.
- [x] **T16. Records.** — done 2026-09-22. `decisions.md`: O10 gains the pointer to the printed source and its numbers
      leave class (e); O1 gains a line that the reporting exists, since F9 is what makes it
      consequential. `procedure_records/side_quests_mirror_and_granularity.md` §4 loses "neither
      question has any prose site" for side quest 2. `thesis_outline/revisions.md`: a site entry and
      a §8 source row.

## 10. Prose sites, to be written only after T2 and T7

- `sections_3-6.md` §5.2 (lines 436–477): the rewrite.
- `sections_3-6.md` line 60 (scope tier) and the word table (lines 81–103).
- `background_sections.md` §1.7.
- Anything in §5.4, §5.6 or §6 item 4 that leans on the old §5.2 prediction (revisions.md lists
  them under the 2026-09-14 entry).
