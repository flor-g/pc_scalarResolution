# Part D at a strong Λ, and the new cell after Code Cell 2

Working record, on the pattern of `theta_u_learned_reach.md` (agent.md §5.3). It is the guide for
the change. **Status 2026-09-14: code tasks T0–T8 closed, T9 (commit) in progress; the prose pass
(S-6, §5) is open.** §1.1–1.3 were measured by the probe before the change; Code Cell 2b now prints
every number there (C6). The scripts are in `audits/2026-09-14-strong-lambda/`.

## 0. Instructions (the user's, verbatim, 2026-09-14)

> Can you probe what the part D evaluations would look like if Lambda is fixed at 512 for all
> priors-cases and utterances?

> write your finding to a new evaluation_partD_atStrongLambda.md. We want to insert a new text+code
> cell right after the current code cell 2 to report this observation; the existing report on the
> delta-like base-prior will also be moved to this new cell since it uses Lambda=512. The md file
> will be used as a guide to this change.

> You recommendation is approved for S-1 to S-5. Regarding S-6, yes we will need to rewrite the
> argument; and we will do that after the codes are finished. Regarding S-7, yes, we want figures
> for all five priors as well as the "no" "some" "all" figures under gaussian prior.

**Reading of S-7 (agent, pending user confirmation).** The new code cell draws three figures, all at
Λ = 512: *no*/*some*/*all* under the Gaussian prior (the counterpart of Code Cell 2's first figure);
*some* under all five priors (the counterpart of its second); and the delta-like *no*/*some*/*all*
figure moved from Code Cell 2 (S-2). main.ipynb's figures go from 6 to 8: Code Cell 2 keeps two,
Code Cell 2b has three, Code Cell 4 keeps its three.

---

## 1. The finding

### 1.1 How it was measured

- **Script:** `audits/2026-09-14-strong-lambda/probe_lambda512.py`. Output:
  `probe_lambda512_output.txt` beside it. Run from the project folder with `.venv/bin/python`.
- **Source of the code.** It execs Code Cell 1 and Code Cell 2's definitions verbatim from
  `main.ipynb`. Code Cell 2's RUN block is not executed. No project code was changed.
- **The configurations.** Λ = 512 for each of Part D's five priors, all three utterances. Each
  configuration re-learns its own θ_u\* by `respawn` (A9, D2).
- **Closed form throughout** (Eqs. 15–16). At Λ = 512, λ_max(H) at θ_u\* is 2.0e6 to 2.5e6 under
  every prior, so no row can be integrated at θ_u\* (I-entry for `FEASIBLE_STIFFNESS`).
- **Reproduction check.** A first pass at the stored settings (Λ = 8, delta row at 512) matches
  Code Cell 2's stored Part D output in every printed digit:
  - the table, and the tempering/utility split;
  - the realizability thresholds;
  - the delta read-out peaks.

  The Gaussian at Λ = 512 (θ_u\* = 1580.81, shift +0.0071) also equals the control line Code Cell 2
  already prints.

### 1.2 The Part D table at Λ = 512

"1st" is the first condition of B2, shift for *some* < 0. "2nd" is the second, P(all | *some*) < ½.

| prior | θ_u\* | P₀(all) | shift *no* | shift *some* | shift *all* | max leak | P(all\|some) | 1st | 2nd |
|---|---|---|---|---|---|---|---|---|---|
| gaussian | +1580.8143 | 0.0016 | −0.0000 | +0.0071 | +0.0000 | 1.7e−177 | 0.0088 | not met | met |
| flat | +1521.4822 | 0.0479 | −0.0000 | −0.0146 | −0.0000 | 6.2e−177 | 0.0357 | met | met |
| skewed low | +1589.4935 | 0.0001 | −0.0000 | +0.0089 | −0.0000 | 7.1e−175 | 0.0091 | not met | met |
| skewed high | +1499.3704 | 0.1367 | −0.0000 | −0.0955 | −0.0000 | 1.8e−179 | 0.0413 | met | met |
| delta (all) | +1407.7691 | 0.9568 | +0.0000 | −0.5217 | +0.0000 | 1.1e−74 | 0.4351 | met | met |

At the stored settings (Λ = 8 for the first four), the shifts for *some* are +0.0008, +0.0295,
+0.0004 and +0.0421. The max leaks are 6.3e−1, 2.3e−2, 9.1e−1 and 9.1e−1.

### 1.3 What changes

- **F1. The conjunction holds under 3 of 5 priors, against 1 of 5 at the stored settings.** Flat
  and skewed high join the delta-like row. The Gaussian and skewed-low priors still fail the first
  condition, and by more than at Λ = 8 (+0.0071 against +0.0008; +0.0089 against +0.0004). The delta
  row is the same row as before, since it already carried Λ = 512.

- **F2. The entries hold under every prior; at Λ = 8 they did not.**
  - At Λ = 8 the diffuse priors override the entries for *no* and *all*: max leak 0.63 (Gaussian),
    0.91 (skewed low and high).
  - At Λ = 512 every leak is below 1e−174.
  - So at Λ = 8, Part D's *no* and *all* columns partly measure the override. That is the situation
    Part D's own delta-row paragraph says a probe must avoid.

- **F3. The shifts for *no* and *all* go to zero under every prior. That is saturation (B6).**
  q_lit under *all* holds 1.0000 of the all-region under all five priors, and under *no* about 0.
  Neither has room to move. At Λ = 8 the *all* shifts were −0.4557, −0.0160, −0.1849 and −0.0087.

- **F4. The prior barely matters any more.** The lexical field outweighs ℓ₀.

  | prior | E[s] *no* | E[s] *some* | E[s] *all* |
  |---|---|---|---|
  | gaussian | 0.002 | 0.899 | 0.998 |
  | flat | 0.002 | 0.912 | 0.998 |
  | skewed low | 0.002 | 0.898 | 0.998 |
  | skewed high | 0.002 | 0.914 | 0.998 |
  | delta (all) | 0.003 | 0.946 | 0.998 |

  - θ_u\* lies between +1407 and +1590 under all five priors, all positive. At Λ = 8 the values
    were −28.4, +5950.6, −14.5, +55.0 and +1407.8.
  - φ_u\* and c_y = BᵀW(ℓ₀ − φ_L) nearly coincide across the four diffuse priors. For example, c_some
    ranges over +571.6 to +595.6 in tilt and −374.1 to −387.7 in width.

- **F5. The tempering does not change; the utility level's contribution does.**

  | prior | q_lit | tempered | tempering | utility at Λ = 8 | utility at Λ = 512 |
  |---|---|---|---|---|---|
  | gaussian | 0.0016 | 0.0191 | +0.0175 | −0.0167 | −0.0104 |
  | flat | 0.0504 | 0.1361 | +0.0857 | −0.0559 | −0.1003 |
  | skewed low | 0.0001 | 0.0067 | +0.0065 | −0.0061 | **+0.0024** |
  | skewed high | 0.1368 | 0.2356 | +0.0989 | −0.0568 | −0.1943 |
  | delta (all) | 0.9568 | 0.8982 | −0.0586 | −0.4631 | −0.4631 |

  - The tempering is unchanged because χ_some excludes only the bottom of the scale, so Λ does not
    reach the all-region's literal mass.
  - Flat and skewed high turn negative because the utility level's contribution grows past the
    tempering.
  - Under the Gaussian it shrinks. Under skewed low it changes sign, which makes Part D's current
    sentence "negative in every one of them" false at Λ = 512.

- **F6. Cost.** The threshold is small and passed in one update wherever the conjunction holds.

  | prior | λ_max(H) at θ_u\* | θ_crit | λ_max(H) at θ_crit | updates | holds to θ_u\* |
  |---|---|---|---|---|---|
  | gaussian | 2.50e6 | none | | | |
  | flat | 2.31e6 | 3.078 | 11.5 | 1 | yes |
  | skewed low | 2.53e6 | none | | | |
  | skewed high | 2.25e6 | 1.021 | 3.0 | 1 | yes |
  | delta (all) | 1.98e6 | 2.126 | 6.5 | 1 | yes |

  So an end-to-end integrated run like the delta row's (realizability block) is affordable for flat
  and skewed high as well. Not run by the probe; run in Code Cell 2b, see F10.

- **F7. The delta read-out's criteria (B8) now part from q's conditions on two rows.**

  | prior | ℓ₀ peak (s) | φ_S\*("some") peak (s) | (a) | (b) | q conjunction |
  |---|---|---|---|---|---|
  | gaussian | 0.5000 | 0.9072 | not met | met | not met |
  | flat | 0.5000 | 0.9168 | not met | met | **met** |
  | skewed low | 0.2535 | 0.8966 | not met | met | not met |
  | skewed high | 0.7465 | 0.9168 | not met | met | **met** |
  | delta (all) | 0.9852 | 0.9468 | met | met | met |

  - On the four diffuse priors the peak moves up the scale, to 0.90–0.92, and stays outside the cell
    of *all* (s ≥ 0.95).
  - Under flat and skewed high the q conjunction holds and criterion (a) does not.
  - At the stored settings the two agree row by row (`delta_criteria_printing.md` F1). This is the
    first Part D configuration where they disagree.
  - It fits `delta_criteria_printing.md` F4: the tilt moves a peak up wherever the literal mode sits
    below s ≈ 0.94, while the width lowers the tail.
  - **Not yet measured:** how many grid nodes below θ_L these peaks sit. The boundary check
    prints that only for the delta row.

- **F8. Consistent with the plane Code Cell 4 already prints.**
  - The flat prior is `beta_world_prior(1, 1)` (Code Cell 1, `uniform_world_prior`), which is the
    α = 1 column of Text cell 6's plane.
  - Code Cell 4 prints "both conditions in 33, from (1, 512)" and a first-condition floor of
    Λ = 512 at α = 1. So the flat row at Λ = 512 is already a both-conditions cell of the plane.
  - `delta_criteria_printing.md` F2 finds no delta conjunction at α ≤ 8, which fits (a) failing
    for flat here.
  - Gaussian, Beta(1,3) and Beta(3,1) are not on the plane.

- **F9. Couplings found while scoping the move** (see §3 and §4).
  - Appendix E's **Code Cell E4** (`relay_bound_report`) iterates `part_d_priors()`. E.1 quotes its
    delta-like number (1.26e−7).
  - **Code Cell 4** reads none of Code Cell 2's delta-row names. Its comment at source line 67
    points at "Code Cell 2's realizability block".
  - **I10** records that additions to Code Cell 2 go inside existing functions, so that E3's replay
    needs no new calls. A new cell departs from that implementational reason.

### 1.3b Findings during implementation (2026-09-14, from `test_sources.py`, outside the notebooks)

- **F10. The integrated run holds for the two new rows.** Flat: one update of Eq. (20) reaches
  θ_u = 7.8161 (λ_max(H) = 63.1); the integrated fixed point gives shift −0.0119 and q_H = 0.0384,
  both met, 13,589 Euler steps, agreeing with Eqs. (15)–(16) to 1e−9. Skewed high: θ_u = 7.9926
  (65.9), shift −0.0925, q_H = 0.0442, both met, 14,199 steps. Their roundoff floors, 2.8–3.0e−11
  and 3.0–4.5e−11, sit below `infer`'s 1e−9 tolerance, as the delta row's does.
- **F11. A printed number in Code Cell 2 changes with the move.** The ℓ₀-invariance of the φ_S
  contrasts at a shared θ_u = 1, over Part D's rows, is 5.3e−15 over the four priors against 3.6e−14
  over five. Text cell 4 Part D quotes 3.6e−14 (prose pass). At Λ = 512 over five priors: 1.1e−13 at
  θ_u = 1, and **0.0001** at each prior's own θ_u\* (0.0575 at Λ = 8), since the θ_u\* nearly coincide.
- **F12. The peaks against the cell of *all*, at Λ = 512 and θ_u\*:** Gaussian 6 nodes below the
  cell (inside against outside −3.256), flat 5 (−1.964), Beta(1,3) 7 (−3.216), Beta(3,1) 5 (−1.841),
  delta-like 1 (−0.081). Only the delta row sits at the boundary.
- **F13. The spike block at Λ = 512.** Under flat and Beta(3,1) the full network's mode moves to
  s = 0.92 with density 0.0000 at the top node; q_lit is unchanged. The block's wording ("the
  right-edge spike") describes Λ = 8; prose pass.
- **F14. A printed sentence Code Cell 2b now contradicts on its own page (S-6).** The moved
  Gaussian control still prints "Raising Lambda alone moves the shift AWAY from the criterion, so
  the delta row's result is the prior's doing and not its Lambda's", a few lines below a table in
  which raising Λ alone moves flat and Beta(3,1) into the criterion. It was moved verbatim, as
  S-2 required; its wording belongs to the prose pass.
- Timing: Code Cell 2 224 s (was about 245 s), Code Cell 2b 22 s.

### 1.4 Caveats

- Closed form only at θ_u\*. The agreement of Eqs. (15)–(16) with the integrated dynamics is
  established elsewhere (Code Cell 2's integrated rows, 1e−9), not at Λ = 512 for the diffuse
  priors.
- Peaks are grid nodes (B7).
- The probe reports the Λ = 512 rows only. It does not repeat the headroom, mechanism, spike,
  ℓ₀-invariance or figure blocks at Λ = 512.

---

## 2. Decisions this rests on or touches

- **B2** (the conjunction), **B6** (read the headroom), **B7** and **B8** (the delta read-out and
  its criteria).
- **B3** (Beta(64, 1) with Λ = 8α = 512 for the delta row alone). The move puts that row in the new
  cell; B3's derivation (Λ_crit ≈ α log 2n) stays with it.
- **A9, D2** (θ_u\* re-learned per configuration). Every Λ = 512 row carries its own.
- **C3** (the three objects: q_lit, the tempered control, the model), **C5** (reader-facing text),
  **C6** (every quoted number printed by a cell).
- **I7** and agent.md §2 items 1, 2, 3, 7 (E2 mirrors Code Cell 2; E3's prefix `# === Code Cell 2`;
  `cost:` lines; E3's replay list).
- **I10** (where numbers are printed). See S-4.
- **O8** (Λ per configuration for §5.2). Related, not the same question: O8 asks how Λ is set for a
  single-predicate probe. This change holds Λ at 512 by the user's instruction.
- agent.md §2 item 5 (equation numbering) and item 6 (anchors and ToC).

---

## 3. Decisions needed before any code task (the user's)

None of these is settled. Each lists the options and the agent's recommendation.

### S-1. What the new cell reports, and what Part D keeps

- **(a)** Part D keeps the four diffuse priors at Λ = 8. The new cell reports all five priors at
  Λ = 512, and the delta row appears only there. *Recommended*: the new cell is then one
  configuration family at one Λ, and the Λ = 8 table stops mixing two Λ.
- (b) Part D keeps all five rows as now, and the new cell adds the Λ = 512 sweep plus the moved
  delta-row blocks. The delta row would be printed twice.
- Consequence of (a): Part D's Λ = 8 counts become "first condition 0 of 4, conjunction 0 of 4".
  The delta row's numbers do not change.

### S-2. Which parts of the "report on the delta-like base prior" move

Inventory of Code Cell 2 that uses Λ = 512 or the delta row. Line numbers are of Code Cell 2's
source as of HEAD 9de5319.

**Move clearly (delta row only, or Λ = 512 only):**

| Block | Lines |
|---|---|
| comment block and `DELTA_ALL_ALPHA` / `DELTA_ALL_LAMBDA` | ≈740–757 |
| `base_prior_sweep`: the Gaussian-at-Λ = 512 control | 949–961 |
| `base_prior_sweep`: THE DELTA-LIKE ROW (headroom) | 976–1006 |
| `base_prior_sweep`: THE MECHANISM (Eqs. 23–24 on this row; also prints the Gaussian's Eq. (23) gap) | 1008–1051 |
| third figure (delta-like prior, log axis) | 1513–1557 |

**Shared (loop over `part_d_priors()`, which includes the delta row). Each must be split or
duplicated:**

| Block | Lines |
|---|---|
| `part_d_priors` itself; also read by `realizability_report` and by appendix E's E4 | 760–770 |
| `base_prior_sweep`'s main table, tempering split, and condition counts | 859–914 |
| ℓ₀-invariance across the five priors, at the network's Λ = 8; **the delta prior is taken at Λ = 8 there** | 917–947 |
| `realizability_report`'s table and "threshold exists under N of M" | 1208–1237 |
| `delta_readout_report`'s rows and the ℓ₀-peak table | 1349–1400 |

**Dependent (the delta row is the only case that triggers them):**

| Block | Lines |
|---|---|
| `realizability_report`'s RUN, NOTHING IN CLOSED FORM (picks the cheapest runnable both-conditions row, today only the delta row) | 1239–1305 |
| THE ROUNDOFF FLOOR, run on that row; the floor justifies `infer`'s 1e−9 tolerance (I3) | 1307–1320 |
| `delta_readout_report`'s realizable rows | 1356–1360 |
| AT THE BOUNDARY and the finer grids (triggered by a peak moving out of the cell) | 1402–1420 |

**Stays:**

- the integration-cost table (Gaussian only), 1193–1206;
- the spike block (flat, skewed high at Λ = 8);
- the second figure. Under S-1(a) its Λ filter becomes a no-op.

Question for the user: does "the existing report on the delta-like base prior" cover the dependent
blocks too? This matters because of the roundoff floor. Under S-1(a), with the delta row gone from
Code Cell 2, no Λ = 8 prior has a both-conditions threshold (§1.2 of the stored output). Code
Cell 2 would then print neither the integrated run nor the floor that supports I3.
*Recommendation:* move them. At Λ = 512 the run gains two more candidates (flat, skewed high; F6).

### S-3. Naming the new cells

- (a) No renumbering: e.g. "Text cell 4b" and "Code Cell 2b", with anchors `tc4b` and `code2b`.
  *Recommended.* Existing references to Code Cells 3 and 4 and Text cells 5 and 6 stay true: Text
  cell 5 (9 mentions), Appendix C/D and Code Cell D comments, Code Cell 4, decisions.md,
  revisions.md, agent.md, the records.
- (b) Renumber everything after it. That touches every site above, and every record that cites them
  by number.
- The header prefix of the new code cell must not begin `# === Code Cell 2` followed by a colon-free
  continuation that E3's `startswith("# === Code Cell 2")` would also match. **"Code Cell 2b"
  matches that prefix.** E3 would pick whichever comes first, which is Code Cell 2 by position.
  It still works today, but fragilely: either tighten E3's match to `# === Code Cell 2:` or choose a
  name that does not share the prefix.

### S-4. Appendix E

- E3 diffs E2's replayed output against main's Code Cell 2 output alone. After the move, blocks now
  checked by E3 would sit in the new cell and fall outside that check, unless:
  - **(a)** appendix E gains a mirror of the new cell (E2b), and E3 extends to diff it against the
    new cell's stored output. *Recommended*: keeps E3's coverage, including the integrated run and
    the delta read-out, where the relay's path differs.
  - (b) E3 covers Code Cell 2 only, and appendix E states it.
- E4's `relay_bound_report` iterates `part_d_priors()`. If S-1(a) removes the delta row from that
  function, E.1's delta-like bound (1.26e−7) disappears. Either pass the delta row to E4 explicitly
  or keep a function that returns all five.
- I10's implementational reason ("E3's replay needs no new calls") no longer holds. I10 needs an
  amendment, the user's to confirm.

### S-5. Order against `delta_criteria_printing.md`

That record's T1 adds criteria (a) and (b) to `delta_readout_report` in Code Cell 2, with
acceptance against the five-row Part D output. Options:

- (a) Do this move first, then T1 prints the criteria in both cells, at Λ = 8 and at Λ = 512.
  *Recommended*: F7 is exactly a disagreement those criteria would show.
- (b) T1 first, then move.

### S-6. Interpretive claims the new cell contradicts (agent.md §5.4: stop and ask)

These sentences are true of the Λ = 8 table and become Λ-conditional once the new cell prints §1.
Rewriting them is the user's call.

- **Text cell 4 Part C:**
  - "Across Part D's five priors the conjunction holds under exactly one" (≈ line 124);
  - "produces it nowhere else among Part D's five … and not under the four diffuse priors"
    (≈ 192–199);
  - commitment 1, "it is the prior doing that rather than the raised Λ" (≈ 140–147). Still true
    for the Gaussian control. But raising Λ alone brings flat and Beta(3,1) into the conjunction, so
    for those priors Λ does matter.
- **Text cell 4 Part D:**
  - "The conjunction holds under the delta-like prior, and under it alone" (≈ 298);
  - "negative in every one of them" and "Only when the prior is already concentrated there does the
    utility level move much mass at all" (≈ 312–316). Skewed low turns positive at Λ = 512 (F5);
    flat and skewed high move 0.10–0.19.
  - "So the sign of the shift is a fact about the prior … and not about the entry" (≈ 317–319). At
    Λ = 512 the entry's strength changes the sign under two priors.
- **Text cell 6:** "Four of Part D's rows sit outside that band and the delta-like row sits inside
  it" (≈ 273–278). Still true of Λ = 8; at Λ = 512 flat is the (1, 512) cell inside the band.

### S-7. Figures

- Does the new cell add a figure of *some* under the five priors at Λ = 512? The four diffuse
  priors are now comparable with the delta row on one Λ, so a shared log axis could hold all five.
- Figure count changes 6 → 7 if yes. The baseline in agent.md §5.1 must follow.

---

## 4. Tasks, in order (all open)

Record format when closing: `[x] Tn (date): what changed; acceptance result; commit`.

- [x] **T0 (2026-09-14). Checkpoint.** This record and `audits/2026-09-14-strong-lambda/` committed
  as a202cdb; the build and apply scripts read both notebooks at that commit.
- [x] **T1 (2026-09-14). S-1 to S-5 and S-7 settled by the user; S-6 deferred to the prose pass.**
  `decisions.md`: B9 (new), dated findings under B3 and B8, I10 marked amended, I11 (new: naming,
  E2b, E3's two prefixes, E4's explicit delta row). Commit pending with T9.
  - **Implementation choices made by the agent, pending user confirmation:**
    - the integrated RUN and THE ROUNDOFF FLOOR run for **every** both-conditions row whose arrival
      θ_u is integrable, not only the cheapest; a row that is not integrable is named. The delta
      row's lines are unchanged by this;
    - three printed sentences in Code Cell 2 print only when true: the "not a property of the model
      alone" lines (only if the rows split), and the realizability narrative (only if some row has
      a threshold);
    - `scalar_implicature_probe`'s pointer "its sign is prior-dependent (Part D)" now reads
      "(Code Cell 2b)", since Part D's four rows at Λ = 8 share one sign;
    - the spike block stays in `base_prior_sweep`, so Code Cell 2b also prints it at Λ = 512;
    - all three Code Cell 2b figures use a log vertical axis, like the moved delta-like figure;
    - Code Cell 2b's comments correct E9's stale "Code Cell 3" to "Code Cell 4".
  - Scripts (scratch, to be filed under `audits/2026-09-14-strong-lambda/` at T9):
    `build_sources.py`, `cell2b_template.py`, `test_sources.py`, `apply_to_notebooks.py`, `new_e3.py`.
- [x] **T2 (2026-09-14). New code cell after Code Cell 2** — closed: Code Cell 2b at main cell 9,
  built by `build_sources.py` + `cell2b_template.py`. Acceptance: its numbers equal the probe; every
  moved line prints byte-identically (`test_report.txt`); the flat row at Λ = 512 is a
  both-conditions cell, as Code Cell 4 prints for (1, 512) (Code Cell 4 prints floors, not per-cell
  values, so the match is of verdict, not of digits). Originally: (cell index 8 today), under S-1, S-2, S-3, S-7. Prints:
  - the Λ = 512 table of §1.2;
  - the E[s] and tempering/utility tables of F4–F5;
  - headroom for every row (F3: saturation now applies to *no* and *all* under all five);
  - thresholds and arrivals of F6;
  - the delta read-out peaks against ℓ₀ and the cell, with **node margins for every row that ends
    outside the cell**, not only the delta row (F7);
  - a Λ = 8 against Λ = 512 comparison line per prior for the *some* shift and q_H;
  - the blocks moved under S-2.

  Every θ_u is θ_u\* of its own configuration. Every fixed-θ line is labelled a control (B4). Every
  wall-clock line is behind `cost:`.

  **Acceptance:**
  - the new numbers equal `probe_lambda512_output.txt`;
  - every moved line is byte-identical to the line Code Cell 2 printed at T0, apart from any header
    rename;
  - the flat row equals Code Cell 4's (α, Λ) = (1, 512) cell.
- [x] **T3 (2026-09-14). Code Cell 2 residue** — closed: 1418 lines (was 1566). Acceptance: the only
  changed printed lines are the counts (0 of 4), the pointer to Code Cell 2b, "four priors", and
  the ℓ₀-invariance value (F11). Originally:
  - Remove the moved blocks and adjust `part_d_priors` and the shared loops per S-1/S-2.
  - Update comments that point at the delta row, the third figure, or "Code Cell 3".
  - **Acceptance:** the lines Code Cell 2 still prints equal their T0 versions, except the counts
    S-1(a) changes ("of 5" → "of 4") and anything S-2 splits.
- [x] **T4 (2026-09-14). Code Cell 4** — closed, no edit: its comment points at functions that stay
  in Code Cell 2. Originally: Update the comment at source line 67 if the realizability block moved.
  Nothing else there reads Code Cell 2's names.
- [x] **T5 (2026-09-14). Appendix E** — closed by `apply_to_notebooks.py` and `new_e3.py`: E2
  re-mirrored (exactly the header and the 98 relay-check lines differ from main), E2b added, E3 checks
  both cells, E4 takes the delta-like row explicitly. Originally, under S-4:
  - re-mirror E2 by lifting main's Code Cell 2 verbatim (the scratchpad `remirror.py` pattern of
    the reach record);
  - mirror the new cell if S-4(a);
  - update E3's replay list and its baseline match (S-3's prefix issue);
  - make E4's delta-like row explicit.
- [x] **T6 (2026-09-14). Execute main, then appendix_E** — closed. `RUNNER OK main.ipynb: error
  outputs 0, figures 8, runtime 249 s`, 14/14; `RUNNER OK appendix_E.ipynb: error outputs 0, figures
  5, runtime 671 s`, E2 18/18, E3 PASS on Code Cell 2 (190 identical, 1 changed, 4 inserted) and on
  Code Cell 2b (215 identical, 0 changed). Stored outputs of Code Cells 2 and 2b equal the
  outside-notebook test; Code Cells 1, 3, 4, A–D, E1 and E4 print exactly what they printed at
  a202cdb (`verify_executed.py`). Originally:
  - Baseline: main 0 errors, 6 figures (7 under S-7 yes), 14/14. appendix_E 0 errors, 3 figures,
    E2 18/18, E3 PASS.
  - Diff the stored outputs against T0: Code Cell 2's lost lines must reappear in the new cell.
    `cost:` lines excepted.
- [x] **T7 (2026-09-14). Structure** — closed for code: Text cell 4b (heading, anchor `tc4b`, a scope
  paragraph, anchor `code2b`); ToC regenerated (72 links, all resolve; indices checked); agent.md §1
  cell maps, §2 couplings 1, 2, 7 and §5.1 baseline updated. decisions.md cites cells by name, not
  index, so needs no change. Text cell 4b's argument is the prose pass (S-6). Originally:
  - New markdown cell before the new code cell, with its anchor inside the heading. The code anchor
    goes at the end of that markdown cell (agent.md §2 item 6).
  - Regenerate the ToC (cell 0).
  - Update agent.md §1's cell map: 21 → 23 cells; Text cell 5 onward shift by 2, so Code Cells A–D
    move to 15, 17, 19, 21 and References to 22.
  - Update decisions.md entries that cite cell indices.
  - New displays are unnumbered unless the user approves renumbering (agent.md §2 item 5).
- [x] **T8 (2026-09-14). Records** — closed: decisions.md B9, I11, findings under B3 and B8, I10
  amended, quantity trace entry for Code Cell 2b; `delta_criteria_printing.md` order note. Originally:
  - `decisions.md`: E-register entries for each new printed quantity; B3/B7/B8/I10 updates per T1.
  - `delta_criteria_printing.md`: note the order chosen under S-5, and that its T1 acceptance now
    spans two cells.
- [x] **T9 (2026-09-14). Commit** — closed: T0 is a202cdb; T1–T8 are 3cbb721. Not pushed.

---

## 5. Prose sites (after T2–T6, written against the executed outputs)

Draft wording goes to the user before it lands. Interpretive sites are under S-6.

- **The new text cell.** What a strong Λ is for:
  - B3's derivation moves here from Part D (≈ lines 230–244): Λ_crit ≈ α log 2n = 192, Λ = 8α.
  - Why every prior now carries it: at Λ = 8 the diffuse priors override *no* and *all*, F2.
  - How to read the table, headroom first (B6, F3).
  - The four findings F1, F4, F5, F7.
  - The integration cost (F6).
  - The delta read-out's disagreement with q (F7). It reports; it does not interpret.
- **Text cell 4 Part C.** The sentences under S-6. The mechanism paragraph (≈ 156–173) cites the
  delta row's c_y and Eq. (24) limit, which now print in the new cell: repoint "Code Cell 2".
- **Text cell 4 Part D.**
  - Intro (≈ 206–212): five priors → four, or as S-1 decides.
  - The delta-like paragraph (≈ 230–244) moves.
  - The baseline/control separation (≈ 266–272) and the prior-relativity list (≈ 274–277) drop or
    keep the delta row per S-1.
  - The table (≈ 290–296) and its reading (≈ 298–319).
  - The delta read-out guide (≈ 343–376): the realizable row and the boundary check move.
- **Found during implementation (§1.3b):**
  - Text cell 4 Part D's ℓ₀-invariance "agree to 3.6 × 10⁻¹⁴" becomes 5.3 × 10⁻¹⁵ over the four
    priors (F11); "differ by up to 0.058" at θ_u\* is over four priors too and must be re-read from
    the output.
  - Code Cell 2b's printed sentences that read Λ = 8 facts: the moved Gaussian-control conclusion
    (F14) and the spike block's wording at Λ = 512 (F13). Printed text is prose for this pass.
  - Code Cell 2's `scalar_implicature_probe` now points to Code Cell 2b for the sign's
    prior-dependence; Text cell 4 Part C's pointers to "Part D" for the same claim follow it.
- **Text cell 4, *Integration cost and conditioning*** (≈ 492–515): the delta-like threshold 2.126,
  the realizable run, and the separation 7.9e6 now print in the new cell. Add flat and skewed high if
  the run's candidates grow (F6).
- **Text cell 6** (≈ lines 98, 226, 231, 273–278): Part D's delta-like configuration as a plane
  cell; add that flat at Λ = 512 is the cell (1, 512) (F8).
- **Appendix E, E.1** (≈ line 100): the delta-like relay bound's source, per S-4.
- **ToC, agent.md, decisions.md** cell references (T7).
