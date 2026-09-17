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

- **Atomicity** is *n* (Eq. A5) or the resolution δ = 1/n (Eq. A6). Appendix A leaves open what
  fixes δ for a predicate with no atoms, and says so.
- **Lexical strength** is Λ, and the model already carries that name for it: Text cell 3 §2's
  inventory reads "Λ | lexical strength, a scalar of g_y(φ_L)", and §3 item 6 says Λ → ∞ recovers a
  hard truth-conditional constraint while finite Λ makes it soft.
- So **H1 makes Λ a function of how stably the predicate fixes δ**, coupling two quantities the
  model currently fixes independently (A5's θ_L and Λ). That is a new dependency, hence O13.
- **H2** says the classes are these entries of Eq. (A1), in each adjective's own orientation:
  maximum-standard absolute = *all*, minimum-standard absolute = *some*, relative = a cut at a
  context threshold *t* anchored by neither endpoint nor δ.

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

## 6. What is open

- **O13** (new): whether H1 and H2 are adopted, and if so what fixes Λ. Nothing was changed.
- **O8**: F1 and the antonym structure answer the ensemble question for this paradigm ({χ, 1 − χ});
  the Λ question is now sharper, not settled — F9 says the data want Λ to vary within a class.
- **Q7** in `revisions.md`: three of its four choices are now answerable from measurement, and the
  fourth (the empirical-fit paragraph) needs F12 either way.
- Every number here is class (e) under `agent.md` §3.3 until a cell prints it (C6). Whether any of
  it should reach a cell is the user's call, and it would need a decision about a five-position
  configuration the notebooks do not currently contain.
