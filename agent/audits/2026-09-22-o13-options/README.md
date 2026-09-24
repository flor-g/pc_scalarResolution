# O13: what the Appendix F data can and cannot say about H1

Two probes, run 2026-09-22 after T0–T13 closed. **Nothing in the notebooks was changed by them.**
Every number here is class (e) under `agent/agent.md` §3.3 until a cell prints it (C6), and none reaches
prose. They are evidence for the user's standing decision on **O13**, which remains open.

| file | what it does |
|---|---|
| `o13_options.py` / `output.txt` | R² over (Λ, cut) per class; the cost of one shared Λ; the per-image-type Λ |
| `o13_levels.py` / `levels_output.txt` | q_lit, tempered and model per (class, image type), with the learned θ_u\* |

The cut scan is a **counterfactual manipulation (C8)**, not a control: Eq. (A5) fixes the cut at
θ_L, and freeing it breaks the identification Appendix A calls "θ_L enters twice". The five Voronoi
cells that carry the five scale positions stay at n = 4 throughout; only the entry's cut moves.
Both probes reproduce `exclusion_indicator` exactly at the model's own cut (0.0e+00).

## What they found

**1. H1's independent variable does not vary across the comparison.** Both classes run at n = 4, so
θ_L = log 7 enters χ_all and χ_some at the same magnitude. What separates the classes in Appendix F
is **which entry they carry**; reading that as a difference in atomicity is an interpretation of the
result, not the result.

**2. A shared Λ costs 0.001 — but that is an identifiability statement, not evidence against H1.**
Per-class best is (max 8, min 48) at R² 0.993 / 0.434; a single Λ = 48 gives 0.992 / 0.434. The
classes do **not** want the same Λ: the maximum class's admissible band is Λ 6 → 2048 (no upper
bound) and the minimum class's is 32 → 48 (interior). A shared value works because the first band
**contains** the second's optimum. The ordering — endpoint-fixed entry tolerating an unbounded Λ,
the other requiring a finite one — runs in H1's direction.

**3. The maximum class identifies almost nothing.** Its R² stays between 0.989 and 0.993 for every
cut from ζ = −1.0 to +4.0, and its q_lit, tempered and settled beliefs agree to three decimals
(0.995 shapes, 0.990 artifacts; mean position 5.00 under all three). It establishes a lower bound on
Λ and nothing above it, and it does not establish that its threshold is endpoint-anchored. **§5.2's
sentence was softened accordingly (R27).**

**4. The minimum class splits by image type into two opposite regimes, and no Λ repairs it.**
At Λ = 48:

| | q_lit R² | tempered R² | model R² | mean θ_u\* |
|---|---|---|---|---|
| min / shape | **0.271** | 0.222 | 0.058 | **−871** |
| min / artifact | 0.044 | 0.305 | **0.880** | **+1605** |

Artifacts want the utility level; shapes are hurt by it. Scanning the whole Λ ladder, the best the
model reaches on min/shape is 0.231, still below q_lit's 0.271 — so a per-image-type Λ, declined at
S-9 on parsimony, **would not have worked either**. The learned θ_u\* has opposite signs in the two
conditions.

**This is where a mechanism claim would start, and it stops here.** R16 bars §5.2 from characterizing
the mismatch, and item 4 bears on exposure (O2, Appendix B) rather than on lexical strength. Nothing
above is offered as an account of the residual.

## What they do not license

An earlier reading of probe 2 treated "a shared Λ costs 0.001" as grounds to answer O13(a) "no". The
user rejected that, 2026-09-22, and the rejection is the part worth carrying:

> H1 is posed simply because it sheds light on how we want to develop the model in subsequent
> phases. … it is a bit rash to commit to a position that rejects H1 completely at this phase. At
> the end of the day, we don't even know if the match or mismatch at this current phase will persist
> for a implemention of future phase.

A fit statistic on one experiment at one resolution does not settle a claim about the lexicon. And
the minimum class's misfit sits exactly where **O14** expects the architecture to change — its entry
is the one whose threshold is a resolution step inside the *other* endpoint, the boundary the
instinct assigns to θ_A once the two thresholds separate. **O13 stays open in both halves.**
