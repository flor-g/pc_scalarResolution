# agent.md

Working standard for any agent editing the paper or the code in this repository. Read it in full
before the first edit of a session. It covers where things are, the couplings that break silently,
and the procedures that protect the integrity of the architecture. The standard for prose is a
separate file, `agent/composition guide.md`, and this file does not repeat it.

**Paths are written from the repository root**, in this file and in every other project file, so
`agent/decisions.md` names that file wherever it is cited from and whatever folder you are in. The
standards, the records and the audits moved under `agent/` on 2026-09-23; the notebooks, the
outline and the data stayed at the root, and **the notebooks must be executed with the root as the
working directory**, since Code Cell F opens `data/xiang_2022/xiang_items.csv` by a relative path
(§5.1).

**Precedence.** The user's instructions in chat come first. After that, the settled entries of
`agent/decisions.md`, then this file, then `agent/composition guide.md` for prose. When two of these conflict,
stop and ask; do not pick one.

**Other agents' memory is invisible to you, and yours to them.** Anything a later agent needs goes
into a project file (`agent/decisions.md`, the change record, this file), never only into private memory.

---

## 1. Where to look

### The tree

Two levels. The root holds what the dissertation **is** and what it reads; `agent/` holds what an
agent works **from**.

| Path | What it is | Read it when |
|---|---|---|
| `main.ipynb` | The primary text: prose, architecture code, evaluation code. | Always. |
| `appendix_E.ipynb` | Bonus notebook: the same model made fully local with a relay node. Read after `main.ipynb`. | Any change to main's code or to Eq. (20). |
| `thesis_outline/` | The dissertation outline: `sections_3-6.md` (proposal, evaluation, discussion, conclusion), `background_sections.md` (background), and `revisions.md` (the revision plan and its task blocks, which also record what each change did). The composition guide covers the outlines. | Before any claim about the paper's argument, and before editing either outline: read `revisions.md` first. |
| `data/xiang_2022/` | The one data file in the repository, the derived item aggregate of Xiang, Kennedy, Xu & Leffel (2022), with its README and `check_data.py`. Code Cell F opens it **relative to the root**, so the working directory matters. | Before touching Appendix F or anything it prints. |
| `runnb.py` | The executor: `.venv/bin/python runnb.py NOTEBOOK`, in place, one line of verification per run (§5.1). | Every execution. |
| `backups/` | Folder and file snapshots from before, and during, the life of the repository. Historical: never modify (§4.7). Read a folder's README before trusting its name. | Only to recover something a commit does not hold. |
| `.gitignore`, `.gitattributes` | Git configuration: what is excluded (`.venv/`, `.DS_Store`, notebook checkpoints, caches), and the nbdime diff and merge drivers for notebooks. | Before changing what git tracks (§4.5). |
| **`agent/`** | **Everything below sits in this folder.** | |
| `agent/agent.md` | This file. | First, every session. |
| `agent/decisions.md` | Every architectural and implementation decision, who made it, why, and every open decision. Also the Bogacz divergence register and the quantity trace register. | Before any change that touches the architecture, an evaluation, or a quantity. |
| `agent/history.md` | The sixteen closed working records in one file, oldest first, each with when it was opened and closed, what it settled, and its numbered findings, which `agent/decisions.md` cites as evidence. It replaced `procedure_records/` on 2026-09-23; the full originals stay in git and each section gives the command. §3 is the record of the change that made θ_u learned everywhere: tasks T0-T11, findings F1-F34, and the table of retained fixed-θ controls. | As the model for a change record (§5.3), for the evidence behind decisions A9-A11 and I1-I5, and to find when a change happened. |
| `agent/composition guide.md` | The five-entry prose standard, applied in its stated order. | Before drafting or editing any prose or code comment. |
| `agent/audits/` | One folder per audit run, holding its scripts and their output, which the registers of `agent/decisions.md` cite. Some carry a README; the rest are read from their `output.txt`. | To reproduce or rerun an audit. |
| `agent/Bogacz_2017_Free_Energy_Tutorial.md` | The tutorial the architecture is built against. The reference for §3.2 below. | Any claim about, or check against, Bogacz. Cite from this file, never from memory. |

**Repository.** The root is a git repository on branch `main`, with the user's private GitHub
repository as remote `origin` (`https://github.com/flor-g/pc_scalarResolution.git`). The first
commit is 499918c (2026-09-13). Procedures are in §4.

### `main.ipynb`, by cell index (25 cells)

| Index | Cell | Holds |
|---|---|---|
| 0 | Table of contents | Generated from the notebook. Regenerate it; do not hand-edit it. |
| 1-3 | Text cells 1-2, pseudocode | Background. The five quoted Bogacz equations here are unnumbered, by the user's choice. |
| 4 | **Text cell 3** | **The architecture's specification, and the authority for §3.3.** §2 inventory of quantities, §3 fixed quantities, §4 generative model Eqs. (7)-(12), §5 free energy Eq. (13), §6 targets Eqs. (14)-(17), §7 dynamics Eqs. (18)-(20), §8 convergence, §9 extensions. |
| 5 | Code cell 1 | Architecture: `LexicalPredictiveCodingNetwork` and the grid and prior builders. Header `# === code cell 1` (lowercase). |
| 6 | Text cell 4 | Evaluation, Parts A-D, reporting statistics Eqs. (25)-(27), integration cost. |
| 7 | Code Cell 2 | Evaluation. **Mirrored in appendix_E's Code Cell E2** (§2). |
| 8 | Text cell 4b | Part D's priors, the delta-like one included, all at Λ = 512 (decision B9). |
| 9 | Code Cell 2b | Part D at Λ = 512. **Mirrored in appendix_E's Code Cell E2b** (§2). |
| 10 | Text cell 5 | Notes after the evaluation: Part A (m), Part B (μ_u). |
| 11 | Code Cell 3 | Probes reported in Text cell 5. |
| 12 | Text cell 6 | The Λ×α sweep. |
| 13 | Code Cell 4 | The sweep. |
| 14, 16, 18, 20 | Appendices A-D | θ_L and g_y; θ\*, locality, alternatives; how many utility directions; why emission is exclusion, and where ℓ₀ enters (Sec. 5, Eqs. (D5)–(D7), decision A3). |
| 15, 17, 19, 21 | Code Cells A-D | Each prints the numbers the appendix above it quotes; Code Cell A also prints Text cell 3 §2's (decision I10). |
| 22 | **Appendix F** | H1 and H2 against Xiang et al. (2022), Eqs. (F1)–(F3). The only cell that reads a data file, and the only place Λ is fitted (S-1). States the two hypotheses, reports match and mismatch, and says nothing about what a mismatch is due to. |
| 23 | Code Cell F | The numbers Appendix F quotes, in eight blocks. Runs at n = 4 in its own respawned network; the default n = 10 everywhere else is untouched. |
| 24 | References | APA 7th, alphabetical. Add a work here whenever a new citation enters the text. |

### `appendix_E.ipynb` (10 cells)

Intro, E.1 equations (E1-E6), **Code Cell E1** (architecture with the relay), **Code Cell E2** (main's
Code Cell 2 plus four checks), **Code Cell E2b** (main's Code Cell 2b, verbatim), **Code Cell E3**
(diffs E2's and E2b's output against main's stored output),
**Code Cell E4** (the numbers E.1 quotes that E2 does not print), E.2 commitments, E.3 claims in
main restated, references.

### Outside the repository

- **Not maintained, do not edit or treat as current:** `~/Desktop/sections_3-5_outline.md`,
  `~/Desktop/background_sections_outline.md` and their `_copy` versions (drafts of 2026-09-01,
  superseded by `thesis_outline/`), `~/Desktop/revision*.ipynb`,
  `revision2 copy.ipynb`, `scalar_implicature_PC_annotated-7*`, `cell7_rebuilt_spec.md`,
  `mu_u_probe_report.md`.

---

## 2. Couplings that break silently

Each of these has broken at least once.

1. **Code Cell E2 is a copy of main's Code Cell 2.** E3 diffs their printed output line by line.
   Any edit to main's Code Cell 2, a comment included if it is printed, must be mirrored into E2 in
   the same pass. Mirror by lifting the source verbatim out of main, never by retyping. The same
   holds for main's Code Cell 2b and E2b, which E3 requires to match with no difference (I11).
2. **E3 finds its baselines by the exact prefixes `# === Code Cell 2:` and `# === Code Cell 2b:`**
   (the colon matters: without it the first also matches 2b). Renaming main's code cells breaks it
   with `LookupError` (I11).
3. **E3 drops lines that begin with `cost:`.** Anything run-dependent (wall-clock seconds) must be
   printed behind that prefix, or E3 fails on noise.
4. **E3 reads main's stored outputs**, so main must be executed before appendix_E, and main's
   outputs must be current when appendix_E runs.
5. **Equation numbers.** Body (Text cells 3-6) is one run, (1)-(41), no letter suffixes. Appendices
   restart with their letter (A1..., B1..., C1..., D1..., E1...). Bogacz is cited by his own numbers,
   which interleave with ours (6, 7, 11 collide). Inserting a numbered display into the body shifts
   every later number: ask the user first. Unnumbered displays are the established alternative.
   **Check BOTH directions.** Removing a tag is the easy half; the half that gets missed is whether
   anything still *cites* it. Verify `cited` ⊆ `defined`, not only that the tag list is what it
   should be — a deleted equation leaves dangling references that no renumbering check sees, and a
   mirror check (coupling 9) cannot see them either, because the two notebooks carry the same stale
   text. Bogacz's numbers are cited by his own scheme, so a citation only counts as ours when it is
   not preceded by "Bogacz". (Added 2026-09-22: decision N deleted Eq. (A6) on 2026-09-21 and the
   coupling was recorded as verified — "tags 61 → 60, exactly {A6} removed, nothing renumbered" —
   while four live citations survived, two of them in `code cell 1` and its E1 mirror.)

   The defined set is the **union over both notebooks**: `appendix_E.ipynb` defines only E-tags and
   cites main's (A1), (B2), (C1) and the body's by design, so checking it alone reports every one of
   those as dangling and the check gets ignored.

   ```python
   # dangling-reference check: run after any tag is added or removed
   import json, re
   def read(p):
       src = "\n".join("".join(c["source"]) for c in json.load(open(p))["cells"])
       return src, set(re.findall(r"\\tag\{([A-F]?\d+)\}", src))
   pairs = [read("main.ipynb"), read("appendix_E.ipynb")]
   defined = pairs[0][1] | pairs[1][1]
   for src, _ in pairs:
       cited = set()
       for m in re.finditer(r"(?<!Bogacz )Eqs?\.?\s*\(?([A-F]?\d+)\)?"
                            r"(?:\s*[-–]\s*\(?([A-F]?\d+)\)?)?", src):
           cited |= {g for g in m.groups() if g}
       print(sorted(x for x in cited - defined if not x.isdigit()))   # must be []
   ```

   A bare integer left over is Bogacz's (he is cited as "Bogacz Eq. 54", and 42, 50-61 and 71 are
   his); a leftover carrying a letter is ours and is a real dangling reference. The same check over
   `thesis_outline/*.md` is worth running by eye when an appendix equation is deleted, since the
   outline cites them too — that is where two of the four A6 citations were.
6. **Anchors and the table of contents.** Every link target is an explicit inline anchor inside the
   heading (`### <a id="..." name="..."></a>Title`). Code cells cannot hold anchors, so `code1`..
   `code4` sit at the end of the markdown cell above. When a heading moves or is added, add its
   anchor and regenerate cell 0.
7. **E3 replays Code Cell 2's and Code Cell 2b's printing calls by name.** A new printing call in
   either must be added to E3's replay list, with what it needs passed in, or E3 reports its lines as deleted.
8. **Never replace `sys.stdout` with a tee under ipykernel.** It silently kills stream capture for
   the rest of the session. `contextlib.redirect_stdout` is safe.
9. **`code cell 1` is copied almost whole into appendix_E's Code Cell E1.** 878 of its 912 lines are
   identical. Every `def` in main appears in E1, which adds only `relay`, `relay_loop_abscissa` and
   `theta_u_gradient_columns`; 24 of main's 30 are verbatim. The other six — `__init__`,
   `predict_state`, `residuals`, `free_energy`, `infer`, `theta_u_gradient` — carry the relay in E1
   (`predict_state`, `residuals` and `free_energy` take an extra `relay=None`). **Nothing diffs the
   two.** E3 compares printed output, not source, and the architecture cells print nothing of their
   own, so a change made to one and not the other is invisible to every check in the project. Any
   edit to `code cell 1` must be mirrored into E1 in the same pass, by lifting the source verbatim,
   never by retyping (decision I13 was applied this way) — **except inside those six**, where lifting
   main's version would delete the relay: apply the same change to E1's version and keep its relay
   argument. (Corrected 2026-09-18: this item said every `def` was verbatim.)

10. **Code Cell F reads `data/xiang_2022/xiang_items.csv` by a path relative to the project
   folder.** It is the only cell in either notebook that reads a file. The runner of §5.1 already
   passes `resources={"metadata": {"path": "."}}`, so this holds as long as the notebook is executed
   **from the project folder**; run from anywhere else, Code Cell F raises `FileNotFoundError` and
   nothing else in the notebook does. Moving, renaming or re-deriving that file changes every number
   in Appendix F and in §5.2. `data/xiang_2022/README.md` pins it by sha256 and
   `check_data.py` verifies the pin; run that check after any change to the file, before re-running
   the notebook.

11. **Three reference lists, with a declared division of labour.** `main.ipynb` cell 24 and
   `appendix_E.ipynb` cell 9 are each a **notebook's** list, for that notebook's own text.
   `thesis_outline/background_sections.md`'s is the **dissertation's**, and it is the only one
   either outline keeps — `sections_3-6.md` has none — so it covers the background, §§3–6 *and*
   the appendices as both notebooks carry them. A new citation in a notebook therefore needs an
   entry in **two** lists, that notebook's and the dissertation's; a new citation in either outline
   needs one in the dissertation's alone. None of the three errors when it falls behind: a missing
   entry is silent until someone reads for it. Reconciled at **BG10**, 2026-09-22 — 50 entries to
   **64**, folding in eight works that lived only in main's cell 24 and six only in appendix_E's,
   and giving Millidge et al. appendix_E's DOI form. Two divergences left standing, both wanting
   one pass across all three: Friston is "Friston, K." for 2005 and "Friston, K. J." for 2007-2010,
   and the notebooks set page ranges with en dashes where the outline uses hyphens.

**Loud dependencies.** Not couplings of the kind above, since each fails with an exception rather
than silently, but an agent renaming or re-signing these should know what breaks:

- **Code Cell D reads names from Code Cells 2 and 2b**: `part_d_priors` and `criterion_for_some`
  (Code Cell 2), `STRONG_LAMBDA` and `DELTA_ALL_ALPHA` (Code Cell 2b). Renaming any of them raises
  `NameError` in Code Cell D.
- **Code Cell A reads names from Code Cells 2 and 2b**: `evaluation_network` (Code Cell 2),
  `STRONG_LAMBDA` and `delta_like_row` (Code Cell 2b), in `peak_locality_report` (added
  2026-09-23, PS11) and `node_count_report` (added 2026-09-24, NK1), so that their Part D rows
  are the ones Text cell 4b reports. Renaming any of
  them raises `NameError` in Code Cell A.
- **Code Cell F reads `evaluation_network` from Code Cell 2** and respawns it at `num_atoms=4`.
  It defines every other name it uses, so `code cell 1` is untouched and coupling 9 stays quiet.
- **Code Cell D overrides `predict_state` against main's signature**, `(phi_u, theta_u=None)`, in
  `UtilityPlacementNetwork` (Appendix D Sec. 5). If `code cell 1`'s `predict_state` gains an
  argument — as E1's has, `relay` — Code Cell D raises `TypeError`. `TruthSetNetwork` overrides only
  `predict_lexical`, whose signature the two notebooks share, and is not exposed.

---

## 3. Integrity of the architecture

The direction of authority is **prose defines, code implements**. Text cell 3 specifies the model;
the code cells are an implementation of it. When the two disagree, do not repair whichever is more
convenient. Record the disagreement (§3.3) and ask the user which side is wrong.

### 3.1 Recording decisions in `agent/decisions.md`

**What counts as a decision.** Any choice that a different, defensible choice could have replaced
and that a result, an equation, or a sentence of the argument depends on. That includes:

- the form of a generative map, error, update rule, or free-energy term;
- what is fixed, what is variational, what is plastic, and each fixed value;
- a baseline, control, criterion, prior, or statistic of the evaluation;
- a numerical surrogate for the dynamics (closed forms, stopping rules, feasibility thresholds,
  zero bands, step sizes);
- a naming or framing convention that constrains what the prose may claim.

Choices of pure presentation (layout, variable spelling in a loop) are not decisions.

**Entry format** (the template is at the top of `agent/decisions.md`). Every entry carries:

- **Status:** Settled, Open, or Superseded by another entry. Never delete a superseded entry.
- **Decided by:** exactly one of `user (date)`; `agent, confirmed by user (date)`;
  `agent, pending user confirmation`; `not recorded`. Do not write `user` unless the user made or
  explicitly confirmed the choice in chat. "Adopted of necessity" is an agent decision.
- **Theoretical reason** and **implementational reason**, kept separate. Write "none" if one is
  absent, which is itself informative.
- **Bogacz status:** the equation it instantiates, or a pointer to its divergence entry (§3.2).
- **Depends on it:** the equations, cells, and results that would move if it changed.
- **Evidence:** the measurement or derivation, with where it is printed or recorded.

**Rules.**

- An agent may record a decision it had to make, as `agent, pending user confirmation`, and must
  name it to the user in the same turn. It may not mark its own decision settled.
- An agent may never close an Open decision. It may add evidence under it.
- **Do not re-litigate settled decisions.** When new evidence bears on one, add it under the entry as
  a dated finding and raise it with the user. Do not change the model to match the new evidence.
- When a decision cannot be made yet, record it as Open with the options, what each would change,
  and what is needed to decide.

### 3.2 Every operation checked against Bogacz (2017)

**What counts as an operation.** Every generative map, prediction, error definition, free-energy
term, state update, error-unit update, parameter update, read-out, and initial condition, in both
the prose and the code. Numerical procedures that stand in for an operation (a closed-form fixed
point replacing integration, a stopping rule, a step-size rule) are checked too, as surrogates.

**Procedure, per operation.**

1. Write the operation as the code computes it, not only as the prose states it.
2. Find the Bogacz equation it should instantiate in `agent/Bogacz_2017_Free_Energy_Tutorial.md`, and write
   out the substitution that makes it an instance (e.g. Eq. (10) is his Eq. (42) with Θ = θ_u b,
   h = id; Eq. (19) is his Eq. (53) with Θ_L = −I).
3. Assign one verdict:
   - **Instance:** the substitution is exact.
   - **Instance under restriction:** exact after a restriction he also covers (e.g. Σ = I). Name it.
   - **Divergence:** no substitution works, or the operation has no counterpart in the tutorial.
   - **Surrogate:** a numerical stand-in. State the operation it replaces and the measured agreement
     with it.
4. **Every divergence goes into the Bogacz divergence register of `agent/decisions.md`** with: what
   differs; why the construction needs it; whether locality (composition guide Entry 1) survives it
   and by what argument; which results depend on it; who decided it.
5. Check locality at the same time: which quantities the update reads, and whether each is
   physically available at the unit or synapse that performs it.

**Traps already met.**

- Bogacz's §5 interneuron removes a **matrix inverse**. It is not a weight-sharing argument and does
  not license one. The relay of Appendix E is not his interneuron.
- The tutorial proves convergence of **inference at fixed parameters**. It does not prove that
  parameter learning converges; his own §4.1 model diverges with v_p fixed. Do not cite him for the
  convergence of θ_u.
- His Eq. (25) silently assumes v_p ≠ 0. Our μ_u ≠ 0 corresponds to it, but ours is necessary and
  not sufficient (Appendix B).
- Confirm every cited equation number against the file before writing it; his numbers and ours
  collide.

### 3.3 Every quantity traced to the prose

Applies to every quantity that `code cell 1`, Code Cells 2-4 and E1-E3 compute, store, print, plot,
or use as a default, and to every number the prose quotes.

**Each quantity must fall into exactly one class.**

| Class | Requirement |
|---|---|
| **(a) Model quantity** | A symbol in Text cell 3 §2's inventory, or defined by a numbered equation. The code name is mapped to the symbol, and the code value equals the value the prose states (σ = 1, m = 2, μ_u = 1, Λ = 8, n = 10, and so on). |
| **(b) Reported statistic** | Defined in Text cell 4 (Eqs. (25)-(27), (36)-(41)) as a summary of the read-out. The prose says it is not a model quantity. |
| **(c) Control** | A deliberate departure from the model (e.g. θ_u held fixed): a configuration the network is actually run in. Under decision **B4** its justification is stated in the prose where it is used, and it is labelled as a control in the output. A quantity built by algebra on settled fields, which no setting of the model produces, is not a control but a **counterfactual manipulation** (C8). |
| **(d) Implementation constant** | A numerical choice with no model meaning (grid size, tolerance, feasibility threshold, zero band). Recorded in `agent/decisions.md` with evidence that the results it supports do not depend on its exact value. |
| **(e) Does not follow** | None of the above. **Flag it to the user in the same turn, add it to the quantity trace register in `agent/decisions.md`, and neither keep it silently nor remove it silently.** |

**Rules.**

- **Every number quoted in prose is computed by explicit code and printed by a code cell**
  (decision C6). A number computed off-notebook, or only by a script in a change record, is class
  (e) until a cell prints it. **A number that WAS printed can stop being printed** — when a
  constant is re-keyed or a block rewritten, prose that quoted the old value is now class (e) and
  factually wrong besides. Sweep for it rather than trusting the change record: three such numbers
  survived into 2026-09-22 undetected, two quoting the fixed `1e-9` tolerance that I3 replaced, and
  one an E4a gap that had drifted 1.90e-15 → 1.84e-15. **Sweep the outline too, not only the
  notebooks.** The 2026-09-22 sweep covered `main.ipynb` and `appendix_E.ipynb` and stopped there;
  `thesis_outline/sections_3-6.md` §4.3 kept three more of the same I3 casualties — a closed-form
  agreement quoted as an absolute 6.0e-11 where Part A now reports 4.45e-09 = 1.00 × a tolerance
  that moves, and two grid-refinement figures, 1.6e-3 and 1.8e-6, against a printed 1.7e-03 and
  3.3e-06. They survived a further five commits of prose work before a readiness check found them.
  The outline quotes the same numbers as the notebooks and goes stale the same way.

- **A checklist certifies the list it was written against and nothing else.** The drafting
  checklist at the foot of `thesis_outline/background_sections.md` was audited item by item on
  2026-09-22 and every box ticked with its evidence, which is why the background was reported
  "complete as an outline". It audits the Revision-4 rewrite tiers of 2026-09-11. **Six items of
  `revisions.md` §6 — that file's own revision plan for the background — had never been applied**,
  and one of them, the §2.7 relay-speed close, is called stale in §6 in so many words. The same
  gap put three unapplied items in `sections_3-6.md` §3.4 past a readiness pass that checked C6,
  cross-references, equation tags, citations and the word table, and read no task block at all.
  **Before calling any outline draftable, read `revisions.md`'s §4 and §6 site by site.** The tasks
  are BG1–BG13, in that file's §10.

  ```python
  # C6 sweep: measured-looking numbers in a notebook's markdown that no cell prints
  import json, re
  nb = json.load(open(NOTEBOOK))
  out = "\n".join("".join("".join(o.get("text", [])) for o in c.get("outputs", [])
                           if o.get("output_type") == "stream") for c in nb["cells"])
  have = {abs(float(m.group())) for m in
          re.finditer(r"-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?", out.replace(",", ""))}
  ok = lambda v: any(abs(v - h) <= 2e-2 * max(abs(v), abs(h)) for h in have)
  for i, c in enumerate(nb["cells"]):
      if c["cell_type"] != "markdown": continue
      for line in "".join(c["source"]).splitlines():
          if re.search(r"Bogacz|\\tag|§", line): continue      # his numbers, tags, section refs
          for m in re.finditer(r"(?<![\w.])(\d*\.\d{3,}|\d+(?:\.\d+)?[eE][-+]?\d+)", line):
              v = abs(float(m.group(1)))
              if not ok(v): print(i, m.group(1), line.strip()[:90])
  ```

  Two things about that check, both learned by getting them wrong. **Keep the match tolerance
  loose** (2%, not 0.5%): prose legitimately rounds, and `4.76e-06` quoted as `4.8e-6` or
  `13377.69` as `13378` is correct practice, not a violation — a tight tolerance reports these and
  the real findings drown. And **`\times10^{-n}` must be read as part of the number**, or the
  mantissa is checked alone and every scientific-notation quote looks unsourced.
- **Three objects must never be conflated, in code names, labels, or prose:** q_lit, the literal
  listener (θ_u = 0 **and** σ_S → ∞, field ℓ₀ − φ_L); the tempered control (θ_u = 0 at the model's σ,
  field ½(ℓ₀ − φ_L), which is also the model's start); and the model (learned θ\*). "The control"
  unqualified is not allowed.
- A default argument is a quantity. A `theta_u=1.0` default that an evaluation silently inherits is
  class (e) unless it is a stated control.
- When a quantity's class changes (a control becomes the model, a constant becomes a parameter),
  that is a decision: §3.1.

---

## 4. Version control and backups

The folder is a git repository (§1). **A commit is the backup**: it records every tracked file
exactly and can be recovered at any time. Folder copies are needed only for files git does not
track.

### 4.1 High-risk changes

A checkpoint (§4.2) is required before:

- any edit to a code cell;
- any execution that overwrites stored outputs (E3 treats main's outputs as evidence);
- any scripted or bulk edit across cells: renumbering, find-and-replace, whitespace normalization,
  ToC regeneration;
- inserting, deleting, moving, or splitting cells;
- rewriting (not appending to) `agent/decisions.md`, `agent/composition guide.md`, or a change record;
- any edit to files outside the repository.

A single hand edit to one prose sentence is low-risk. When unsure, make a checkpoint: it is cheap.

### 4.2 Checkpoint before a high-risk change

1. Run `git status`.
2. **Clean tree:** the current commit is the checkpoint. Record `git rev-parse --short HEAD` in the
   change record, or in your report to the user if there is no record.
3. **Uncommitted changes you made in this session:** commit them first, as
   `Checkpoint before <label>` with the message body of §4.3, and record the hash.
4. **Uncommitted or untracked changes you did not make:** they are the user's. Do not fold them into
   your checkpoint and do not discard them. Stop and ask the user whether to commit them first.
5. **Files outside the repository** (for example anything on the Desktop): git cannot back them
   up. Copy them into a **new** folder `backups/YYYY-MM-DD-<label>/`, never into an existing one
   (F33: that destroyed the only pre-T8 snapshot). Add a `README.md` listing each file with its
   sha256, check the copies hash-equal, and commit the folder.

### 4.3 Commits

- **Stage explicit paths** (`git add main.ipynb appendix_E.ipynb agent/decisions.md`). Never run
  `git add -A` or `git add .` without reading `git status` first. Never commit credentials, tokens,
  `.venv/`, or scratch files.
- **One logical change per commit, and never half a coupling.** A commit that changes main's Code
  Cell 2 also contains the E2 mirror (§2, item 1). A commit that changes code contains the
  re-executed outputs of both notebooks, or its message says they were not re-executed. Do not
  commit a state in which E3 fails unless the message says so.
- **Notebook outputs are committed.** E3 reads them as evidence. Never add an output-stripping
  filter (nbstripout or similar), and never clear outputs to shrink a diff.
- **Verify the edits landed before writing the message that claims them.** A commit message is a
  claim about the diff, and three times on 2026-09-23 it was false: a script edited several sites,
  asserted each substitution **inside** its mutation loop, hit one pattern that had been rewrapped,
  raised, and never reached its single write at the end. Every earlier in-memory edit was discarded.
  The file is left untouched, nothing errors, and the commit goes out describing changes that are
  not in it. Once this happened inside the very commit that was correcting the previous instance.

  Two rules, and they are cheap:

  ```python
  # validate EVERY pattern first, mutate only after, write once
  for site, old, _ in EDITS:
      assert text[site].count(old) == 1, (site, old[:60], text[site].count(old))
  for site, old, new in EDITS:
      text[site] = text[site].replace(old, new)
  ```

  Then **read back what you just wrote** and check each edit is present, by a string that only the
  new text contains. `git diff --stat` is not enough: it shows that *something* changed, not that
  the thing you meant changed. Notebook sources are stored as line lists, so a pattern spanning a
  line break must be matched with flexible whitespace or against the exact wrapping; **a line you
  rewrapped earlier in the same session will not match the string you wrote before rewrapping it.**
- **Message format:**

  ```
  <area>: <what changed, in one line>

  Why: <decision, task, or finding IDs, e.g. A9, T3, F24; or "user request">
  Verified: main 0 errors, 8 figures, 15/15; appendix_E 0 errors, 5 figures, E2 19/19, E3 PASS
  ```

  Write `Verified: not run` when nothing was executed. Add any attribution line your own harness
  requires.
- **Commit when a task closes**, after its verification, and record the hash on the task's line in
  the change record.

### 4.4 Remote

- `origin` is the user's private GitHub repository. **Push only when the user asks.** Fetching is
  always allowed.
- **Never force-push.** If a push is rejected, stop and report it. Do not rebase, reset, or force
  past the rejection.

### 4.5 Operations that need the user's explicit approval in chat

Each of these can destroy work that no commit holds, or rewrite history the remote already has:

- `git reset --hard`, `git clean`, `git checkout -- <path>`, `git restore <path>` on a file with
  uncommitted changes, `git stash drop` or `git stash clear`;
- `git commit --amend`, `git rebase`, or any other rewrite of a commit that has been pushed;
- `git push --force` in any form; deleting a branch or a tag;
- changing `.gitignore` or `.gitattributes`.

Reading history is always safe: `git log`, `git show <hash>:main.ipynb`, `git diff <hash> -- <path>`.
To bring back an old version, first write it to a scratch location
(`git show <hash>:main.ipynb > <scratch>/main.ipynb`), compare, and ask before replacing the working
file.

### 4.6 Notebook diffs with nbdime

nbdime (4.0.4, installed in `.venv`) is git's diff and merge driver for `*.ipynb`, through
`.gitattributes`. Git calls it by name, so **`.venv/bin` must be on the PATH**. Checked 2026-09-13:
without it, `git diff` on a notebook stops with `external diff died` (exit 128).

- Cell-by-cell diff: `PATH="$PWD/.venv/bin:$PATH" git diff -- main.ipynb`, or activate the
  environment first with `source .venv/bin/activate`.
- Raw JSON diff, bypassing nbdime: `git diff --no-ext-diff -- main.ipynb`.
- `git diff --stat` works either way. Merges of notebooks need the same PATH.

### 4.7 `backups/`

The folder snapshots taken before the project was under git. They are history: never modify, move,
or delete them. New folder backups are made only under §4.2, step 5.

---

## 5. Procedures

### 5.1 Execution and verification

Run notebooks with nbclient, in place, **with the repository root as the working directory**,
`main.ipynb` first. The root is not a convenience: Code Cell F opens
`data/xiang_2022/xiang_items.csv` by a path relative to it, and `runnb.py` passes `"path": "."` to
the kernel.

```python
# runnb.py NOTEBOOK
import sys, time, nbformat
from nbclient import NotebookClient
path = sys.argv[1]; nb = nbformat.read(path, as_version=4); t0 = time.time()
client = NotebookClient(nb, timeout=3600, kernel_name="python3", resources={"metadata": {"path": "."}})
try:
    client.execute(); status = "OK"
except Exception as exc:
    status = f"FAILED: {type(exc).__name__}: {str(exc)[-600:]}"
nbformat.write(nb, path)
errors = sum(1 for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", []) if o.output_type == "error")
figures = sum(1 for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", [])
              if o.output_type in ("display_data", "execute_result") and "image/png" in o.get("data", {}))
print(f"RUNNER {status}  {path}: error outputs {errors}, figures {figures}, runtime {time.time() - t0:.0f} s")
```

- Use `.venv/bin/python`. **Never pipe the runner to `tail` or `head`**: the pipeline reports their
  exit status, so a failed run looks like success. Read the runner's own `RUNNER OK` line.
- **The runner writes the notebook back from the state it READ, so never edit a notebook while it
  is running.** `nbformat.read` happens at the first line and `nbformat.write` at the last; any edit
  made in between — including a markdown-only edit that needs no execution — is silently overwritten
  when the run finishes. Either wait, or stop the run, edit, and start again. **Verify the edit is
  still there afterwards**; the loss leaves no error and no trace in the runner's output.
  (Learned 2026-09-22, on Appendix B's cell 16.)
- **A stopped run leaves the notebook INCONSISTENT, not unchanged.** Killing the runner can still
  write, giving a file whose early cells carry fresh outputs, the interrupted cell none, and the
  later cells outputs stale from the previous run — with no error anywhere. After any interrupted
  run, check `execution_count` across the code cells and re-execute in full before trusting or
  committing anything. A full-file output diff against the last commit (§4.2) is what catches it.
- **Baseline as of 2026-09-22, after T0-T13:** `main.ipynb` 0 errors, 8 figures (2 in Code Cell 2,
  3 in Code Cell 2b, 3 in Code Cell 4), 14/14 specification checks, **about 855 s**;
  `appendix_E.ipynb` 0 errors, 5 figures, E2 18/18, E3 PASS on both cells (Code Cell 2: **220** lines
  identical, 0 deleted, 1 changed, 4 inserted; Code Cell 2b: **261** identical, nothing else),
  **about 1,860 s**. Any departure from the **counts** is a finding, reported with the output, not
  explained away.
  **E3's line counts grow with the cells they diff, and the 2026-09-14 figures (203 and 234) were
  left behind.** What E3 actually asserts is the *shape* — 0 deleted and 0 changed beyond the pass
  count, the 4 insertions being the checks the relay adds — and that shape has never moved.
  Re-measure the totals when Code Cell 2 or 2b gains a printed line; treat a change in the shape as
  the finding.
  **The runtime is not a check.** main's was "about 250 s" from 2026-09-14 until it was measured
  again on 2026-09-22 and came back 855 s, with the counts unchanged: the cells added since (Code
  Cell A's 80-row sweep, Code Cell B's ray report, Code Cell 4's grid caveat, Code Cell F) account
  for it, and so does whatever else the machine was doing. Re-measure it when the cell inventory
  changes and do not read a drift in it as a defect. Code Cell F itself costs 0.3 s.
- **Both notebooks are nbformat 4.5, and every cell carries an `id`.** Bumped from 4.0 on
  2026-09-23. They had declared 4.0 while carrying ids on 8 of main's 25 cells and 2 of
  appendix_E's 10 — ids are valid only from 4.5, so **neither file validated against the version it
  declared**. The installed `nbformat` (5.11.1) writes 4.5 by default, which is where the stray ids
  came from and why stripping them would not have held: the next save in VS Code or Jupyter puts
  them back. Bumping instead makes ids required-and-present, and gives the nbdime drivers in
  `.gitattributes` stable cell identity to match on. `normalize()` from `nbformat.validator`
  assigns the missing ones and leaves existing ids alone:

  ```python
  import nbformat
  from nbformat.validator import normalize
  nb = nbformat.read(path, as_version=4)
  nb.nbformat_minor = 5
  _, nb = normalize(nb, version=4, version_minor=5)
  nbformat.write(nb, path)
  ```

  The bump touches nothing else: 17 and 8 new `"id":` lines plus the version field, with sources and
  outputs byte-identical, so it needs **no re-execution**. The runner's read/write round-trip keeps
  4.5, and E3 is unaffected because it reads `main.ipynb` with plain `json.load` and matches cells by
  source prefix (`# === Code Cell 2:`, `# === Code Cell 2b:`), never by id. **Do not let a notebook
  fall back to 4.0**; check `nbformat_minor` after any tool other than `runnb.py` writes one.
- Report what was run and what it returned. If a step was skipped, say so.

### 5.2 Numerical reporting

- Step counts are quoted to three significant figures; the cells may print the exact integer.
- Wall-clock figures are printed behind `cost:` and are not quoted as exact.
- Sign counts over the plane use the 1e-12 zero band (F24).
- A fixed point from a closed form states that it is one, and names the configurations where the
  dynamics were actually integrated and how closely they agreed.
- Stopping tolerances sit above the roundoff floor (F34, decision I3), and **the floor is
  not a constant**: it is 4.547e-13 x lambda_max(H), so the tolerance is keyed to
  lambda_max(H) too (`DERIVATIVE_TOLERANCE_PER_RATE`). Any threshold checked against a
  quantity that the tolerance bounds is therefore expressed in MULTIPLES of the tolerance
  actually used, never as a constant of its own (`TOLERANCE_MARGIN`).

### 5.3 Change records for multi-step work

Any change spanning more than one cell or session gets a working record, on the pattern of
`agent/history.md` §3. **Write it as its own file in `agent/` while the change is open**, beside the
history it will join, and **fold it into `agent/history.md` when it closes**, keeping its findings,
because other files cite those by number. (2026-09-23: `procedure_records/` is gone and its sixteen
records are §§1-16 of `agent/history.md`.) A record holds:

1. the user's instructions, verbatim;
2. the decisions the change rests on, with pointers into `agent/decisions.md`;
3. tasks **in order**, the checkpoint first (§4.2, hash recorded), each closed as
   `[x] Tn (date): what changed; acceptance result; commit hash`;
4. a findings log, written the moment something unexpected appears, before moving on;
5. only after the code tasks close, the list of prose sites that must change, written against the
   executed outputs.

**Code before prose.** Prose is rewritten against outputs that exist, never against expected ones.

**Bookkeeping goes stale silently, and three kinds of it did by 2026-09-22.** None was a defect in
the work; all three misled about what was left to do, which is worse than it sounds when the next
session is deciding what to pick up.

- **Checklists in outline files.** `background_sections.md`'s 13-item drafting checklist stood
  entirely unticked while every item had been done — §1.7 was written, and then revised again at
  T11, with its box still open. **Tick the box in the same pass that lands the work**, and when
  auditing an old checklist, check each item against the file rather than against the change record.
- **Section word totals against the word table.** Three section headings in `sections_3-6.md`
  disagreed with the table they are kept in step with (§4 said 1,020 against 1,110; §5 1,250 against
  1,650; §6 165 against 185). A heading is a second copy of a number and drifts like any other.
  **Re-check every heading whenever a budget moves**; the table itself should also add up at
  section, subsection and total level.
- **"Not yet written" notes in plans.** `revisions.md` §5 item 2 said a divergence-register entry
  for the halting tolerance was "**Not yet written**" after it had been written as D12. **Before
  carrying a plan's gap into prose, check whether it is still a gap.**

The cheap general rule: **a plan describes what was true when it was written.** Verify its claims
about the repository's state before acting on them, exactly as `agent/decisions.md` entries are verified
before being cited.

### 5.4 Stop and ask the user

Stop, report, and wait when:

- a headline result changes: a sign flips, a condition becomes met or unmet, a count moves;
- a finding contradicts a settled decision;
- a new free, variational, or plastic parameter would enter the model;
- an operation diverges from Bogacz and no divergence entry exists;
- a quantity falls in class (e);
- the change would rewrite an **interpretive** argument (the reading of a result, a commitment, a
  position), as opposed to correcting a number inside it;
- the user's own phrasing of a technical point is inaccurate. Tell them; do not write the inaccurate
  version in, and do not silently write a corrected one either.

### 5.5 Reader-facing hygiene

- The notebooks are written for the reader. No changelog prose, no reference to earlier versions of
  a cell or to working documents.
- Code comments stay short and point to the markdown (Sec. N, Eq. (N), Appendix X) rather than
  restating the argument.
- Settled naming and framing conventions are in `agent/decisions.md` section C. The ones most often
  broken: no Gricean reference frame; θ_L, not β; F is maximized; the three objects of §3.3.
- **One quantity, one name.** Where two symbols would denote the same quantity, the dissertation
  keeps one. The scale's resolution is **n** and never δ (O1): a count where the predicate has
  atoms, the number of distinguishable steps where it has none. "Delta" is reserved for the delta
  read-out (A16, B7) and the delta-like prior.

---

## 6. Checklists

**Session start**

- [ ] Read this file, `agent/decisions.md`, and the relevant change record.
- [ ] Confirm the files named in §1 exist and the cell map still holds (count cells, check headers).
- [ ] Read the composition guide if prose will be touched.
- [ ] `git status`: the tree is clean, or every uncommitted change is accounted for (§4.2).
- [ ] Checkpoint (§4.2) before the first high-risk edit.

**Before closing any change**

- [ ] Every new or altered operation checked against Bogacz; divergences registered (§3.2).
- [ ] Every new or altered quantity classed (a)-(e); class (e) flagged to the user (§3.3).
- [ ] Every decision recorded with who made it; agent decisions named to the user (§3.1).
- [ ] Main's Code Cell 2 and E2 still mirror; E3 prefix intact (§2).
- [ ] Both notebooks executed; results match the baseline or the departure is reported (§5.1).
- [ ] Every number the prose quotes is printed by a cell or a recorded script (§3.3).
- [ ] Anchors, ToC, equation numbers, and references cell consistent (§2).
- [ ] Change record and `agent/decisions.md` updated, so the next agent does not depend on your memory.
- [ ] Committed under §4.3: explicit paths, the IDs and a verification line in the message, the hash
      in the change record. Pushed only if the user asked (§4.4).
