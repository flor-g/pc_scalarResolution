# Xiang, Kennedy, Xu & Leffel (2022) — derived item aggregate

The one data file in this repository. It exists so that Code Cell F (Appendix F of `main.ipynb`)
can print the model's fit **against** these data, which C6 requires it to print rather than quote:
an R² is a statistic of the model against the data, so the data have to be present.

## Contents

| file | bytes | sha256 |
|---|---|---|
| `xiang_items.csv` | 34803 | `c23d930d48357455b797a953651459e97b4371ef53de00b745cafbeb792004a0` |

480 rows = 96 items × 5 scale positions. One header row. Columns:

| column | meaning |
|---|---|
| `adj` | the adjective, in its own orientation (21 distinct) |
| `img_set` | the image set the item names (96 distinct, one per item) |
| `img_type` | `shape` or `artifact` |
| `cls` | `absolute_max`, `absolute_min` or `relative` |
| `pos` | scale position 1…5 |
| `prior` | elicited degree prior for that item and position (Experiment 1), smoothed and renormalized |
| `posterior` | mean proportion of posterior-degree choices (Experiment 3) |
| `n_post` | participants contributing to `posterior` |
| `tvj` | mean truth-value judgment (Experiment 2) |
| `n_tvj` | participants contributing to `tvj` |

Item counts by class and image type: maximum 16 + 16, minimum 12 + 12, relative 20 + 20.

## Provenance

Derived from the authors' public OSF repository, **https://osf.io/nr6a4/**, licensed **CC-BY**.
Cite the article, not this file:

> Xiang, M., Kennedy, C., Xu, W., & Leffel, T. (2022). Pragmatic reasoning and semantic convention:
> A case study on gradable adjectives. *Semantics and Pragmatics, 15*(9).
> https://doi.org/10.3765/sp.15.9

Four source files were read:

- `Expt1.priors/expt1.priors.adjsplitted.byitem.csv` — the elicited degree prior for each of the 96
  items, in that adjective's own orientation. → `prior`
- `Expt3.posterior_degrees/adj.posterior.judgment.results.csv` — averaged per item and scale
  position over participants, keyed by the authors' `scale_updated`. → `posterior`, `n_post`
- `Expt2.Truth_value_judgment/Expt2.adjTVJ.csv` — likewise. → `tvj`, `n_tvj`
- `Expt1.priors/adj_info.csv` — the class of each adjective. → `cls`

Two transformations were applied, both following the authors' own treatment:

1. **Prior smoothing.** Zero prior cells are smoothed as the authors smooth them: `+1e-5`, taken off
   the largest cell, and the five cells renormalized.
2. **Missing Experiment 3 responses.** Ten of the 480 item × position cells drew no response and are
   read as `0`. They are stored as the empty string, not as `0`, so that a reader can tell a
   measured zero from an absent one; `n_post` is never zero.

## What is *not* here, and why

**The step from those four files to this CSV is documented above but not re-runnable in this
repository.** The derivation was performed once, in the 2026-09-17 audit, and only its result was
kept; the source files are not vendored and the script that read them was not saved. Settled by the
user 2026-09-22: ship the aggregate with its provenance rather than re-derive it. So the sha256
above pins *this* file against later drift — it does not certify the derivation. Anyone needing that
guarantee should go to the OSF node.

The file is the authors' measurements only. **No published statistic of theirs is stored here or
printed by any cell** (S-5): their LG/QF/ST/hybrid R² values are cited in §5.2's prose. What Code
Cell F prints is the model's own predictions and our own statistics of those predictions against
these columns.

## Scope

All 96 items are stored, including the 40 **relative** ones. The relative class is **not modelled**
(`decisions.md` O14, S-2): a relative adjective's cut is a context threshold that neither endpoint
supplies, and this phase has one θ_L for both endpoints. The items stay in the file because the file
is the data; what is modelled is a property of Code Cell F, not of the aggregate.

## Checking

```
.venv/bin/python data/xiang_2022/check_data.py
```

Reads the CSV and reprints the six empirical class profiles (F1 of
`history.md` §12). It is a data-integrity check and **not** a source
for any number the paper quotes — under C6 that source is Code Cell F.
