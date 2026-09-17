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

## 6. What is open

- **O13** (new): whether H1 and H2 are adopted, and if so what fixes Λ. Nothing was changed.
- **O8**: F1 and the antonym structure answer the ensemble question for this paradigm ({χ, 1 − χ});
  the Λ question is now sharper, not settled — F9 says the data want Λ to vary within a class.
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
- **S-2 and S-7 — still open**, and the subject of the measurements F14 to F16 above.

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
  endpoint nor δ/2, so it is a quantity of the entry that Text cell 3 §2's inventory does not have,
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

## 9. Tasks, in order

Code before prose (`agent.md` §5.3). Nothing below starts until S-1 to S-7 are answered.

- [ ] **T0. Checkpoint.** `git status` clean, record `git rev-parse --short HEAD`. The tree is clean
      at `acabb7e` as this list is written.
- [ ] **T1. The data file** (S-3 settled: yes). Add the derived aggregate under a new `data/xiang_2022/`
      with `README.md` giving the OSF node, the four source files, the derivation, the licence and a
      sha256 per file; add the derivation script beside it. Acceptance: the README's hashes match,
      and a fresh read of the file reproduces the six class profiles in §5 F1 above.
- [ ] **T2. Code Cell F** (S-1, S-3, S-4, S-5 settled; needs S-2). A new code cell printing every number §5.2 will quote,
      and nothing else. Its blocks:
      1. **Configuration and self-checks.** n = 4, θ_L = log 7, the five cells and their boundaries;
         the three entries of Eq. (A1) in the adjective's own orientation and the complement that
         each item's antonym supplies; that the audit's closed form equals `closed_form_fixed_point`
         (expect 0.0); that the closed-form θ\* equals a scan (expect ~6e-06) and returns −28.4375
         for the default n = 10 inventory; that a uniform five-cell prior pushes forward to
         [0.193, 0.200, 0.214, 0.200, 0.193]; that the five cells partition the grid to 1e-10.
      2. **The class profiles**, prior / q_lit / model / data, by class and image type, with the peak
         and the mean scale position.
      3. **R²** by class and overall, for the model and for q_lit — **ours only** (S-5). Their
         published values are cited in §5.2's prose and printed nowhere.
      4. **The Λ scan per class**, wide enough to show that the maximum class is flat to Λ = 2048
         and that the other two turn over.
      5. **The image-type difference** per class, in prior, data and model.
      6. **The between-class gaps** by image condition.
      7. **The mismatch quantities**: the minimum class's R², the −0.16 against −1.13, the two
         one-sided Λ optima, and the displacement from prior to posterior in both conditions.
      Constraints: every helper stays local to this cell, so `code cell 1` is untouched and coupling
      9 does not fire; no figure, so the figure baseline is unchanged; any wall-clock line goes
      behind `cost:` (coupling 3). Acceptance: the cell prints every number the drafted §5.2 quotes,
      and no number in §5.2 is absent from it.
- [ ] **T3. Appendix F markdown cell.** Heading with anchor `appf`, the `codef` anchor at its end.
      Content: H1 and H2 as stated by the user; the instantiation (five positions = five Voronoi
      cells at n = 4, the three entries, the complement ensemble); what is measured and how R² is
      computed; then match and mismatch, reported and not explained. Displays, if any, numbered F1,
      F2 … (appendix letters restart, so the body's (1)–(41) is untouched and no renumbering
      question arises). No sentence about what the mismatch is due to.
- [ ] **T4. Structure.** Insert the two cells after Code Cell D (index 21), before References, which
      becomes index 24; cell count 23 → 25. Regenerate the ToC (cell 0) with rows for 22 and 23 and
      the moved References row. Acceptance: every ToC link resolves and every index in it is right.
- [ ] **T5. References.** Add Xiang, Kennedy, Xu & Leffel (2022) and whichever of Kennedy (2007) and
      Leffel, Xiang & Kennedy (2017) the drafted text cites, APA 7th, in alphabetical position. The
      pending Leffel-versus-Xiang check (`background_sections.md` line 612) is decided here.
- [ ] **T6. Couplings.** Confirm none fires: E3 diffs Code Cells 2 and 2b only; `code cell 1` is
      unchanged so coupling 9 is quiet; no new printing call in Code Cell 2 or 2b, so coupling 7 is
      quiet. Check whether `appendix_E.ipynb` §E.3 ("claims in main restated") needs a line.
- [ ] **T7. Execute** main, then appendix_E, by `agent.md` §5.1. Acceptance: main 0 errors,
      8 figures, 14/14; appendix_E 0 errors, 5 figures, E2 18/18, E3 PASS on both cells. Record the
      new runtime. Diff every other cell's stored output against T0: only the two new cells may
      differ.
- [ ] **T8. agent.md.** §1's `main.ipynb` cell map (23 → 25 cells, the new rows, References at 24)
      and §5.1's baseline. §2 needs no new coupling if T6 holds; if Code Cell F reads the data file,
      add a coupling for that path.
- [ ] **T9. decisions.md.** New entries or amendments for whatever S-1 to S-5 settle: the n = 4
      configuration; the treatment of Λ; *t*, if it enters; the data file and its provenance;
      O13's status. Quantity-trace (register E) entries for every quantity Code Cell F prints, each
      assigned a class under §3.3. O8 gains the pointer.
- [ ] **T10. §5.2 prose**, written against the executed output, not before (S-6 settled: the budget rises; needs S-7). Also
      the §5.2 row of the word table in `sections_3-6.md` lines 81–103 and its scope-tier row at
      line 60.
- [ ] **T11. Background §1.7.** The prior-manipulation bullet (F12), and the Q3b sentence softened
      per the 2026-09-14 entry. `background_sections.md` line numbers are one lower than
      revisions.md cites, after R8.
- [ ] **T12. revisions.md.** Mark the §5.2 entry and Q7 closed by this change; update §8's source
      table so the numbers point at Code Cell F rather than at the audit; clear the audit from the
      class (e) list.
- [ ] **T13. Commit**, one logical change per commit, hashes recorded on each task line above.

## 10. Prose sites, to be written only after T2 and T7

- `sections_3-6.md` §5.2 (lines 436–477): the rewrite.
- `sections_3-6.md` line 60 (scope tier) and the word table (lines 81–103).
- `background_sections.md` §1.7.
- Anything in §5.4, §5.6 or §6 item 4 that leans on the old §5.2 prediction (revisions.md lists
  them under the 2026-09-14 entry).
