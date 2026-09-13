# agent.md

Working standard for any agent editing the paper or the code in this folder. Read it in full before
the first edit of a session. It covers where things are, the couplings that break silently, and the
procedures that protect the integrity of the architecture. The standard for prose is a separate
file, `composition guide.md`, and this file does not repeat it.

**Precedence.** The user's instructions in chat come first. After that, the settled entries of
`decisions.md`, then this file, then `composition guide.md` for prose. When two of these conflict,
stop and ask; do not pick one.

**Other agents' memory is invisible to you, and yours to them.** Anything a later agent needs goes
into a project file (`decisions.md`, the change record, this file), never only into private memory.

---

## 1. Where to look

### In this folder

| File | What it is | Read it when |
|---|---|---|
| `main.ipynb` | The primary text: prose, architecture code, evaluation code. | Always. |
| `appendix_E.ipynb` | Bonus notebook: the same model made fully local with a relay node. Read after `main.ipynb`. | Any change to main's code or to Eq. (20). |
| `Bogacz_2017_Free_Energy_Tutorial.md` | The tutorial the architecture is built against. The reference for §3.2 below. | Any claim about, or check against, Bogacz. Cite from this file, never from memory. |
| `composition guide.md` | The five-entry prose standard, applied in its stated order. | Before drafting or editing any prose or code comment. |
| `decisions.md` | Every architectural and implementation decision, who made it, why, and every open decision. Also the Bogacz divergence register and the quantity trace register. | Before any change that touches the architecture, an evaluation, or a quantity. |
| `theta_u_learned_reach.md` | The working record of the change that made θ_u learned everywhere: tasks T0-T11, findings F1-F34, and §5.C, the table of retained fixed-θ controls. | As the model for a change record (§5.3), and for the evidence behind decisions A9-A11 and I1-I5. |
| `backups/` | Dated snapshots. Read the README in a folder before trusting its name. | Before restoring anything. |

### `main.ipynb`, by cell index (17 cells)

| Index | Cell | Holds |
|---|---|---|
| 0 | Table of contents | Generated from the notebook. Regenerate it; do not hand-edit it. |
| 1-3 | Text cells 1-2, pseudocode | Background. The five quoted Bogacz equations here are unnumbered, by the user's choice. |
| 4 | **Text cell 3** | **The architecture's specification, and the authority for §3.3.** §2 inventory of quantities, §3 fixed quantities, §4 generative model Eqs. (7)-(12), §5 free energy Eq. (13), §6 targets Eqs. (14)-(17), §7 dynamics Eqs. (18)-(20), §8 convergence, §9 extensions. |
| 5 | Code cell 1 | Architecture: `LexicalPredictiveCodingNetwork` and the grid and prior builders. Header `# === code cell 1` (lowercase). |
| 6 | Text cell 4 | Evaluation, Parts A-D, reporting statistics Eqs. (25)-(27), integration cost. |
| 7 | Code Cell 2 | Evaluation. **Mirrored in appendix_E's Code Cell E2** (§2). |
| 8 | Text cell 5 | Notes after the evaluation: Part A (m), Part B (μ_u). |
| 9 | Code Cell 3 | Probes reported in Text cell 5. |
| 10 | Text cell 6 | The Λ×α sweep. |
| 11 | Code Cell 4 | The sweep. |
| 12-15 | Appendices A-D | θ_L and g_y; θ\*, locality, alternatives; how many utility directions; why emission is exclusion. |
| 16 | References | APA 7th, alphabetical. Add a work here whenever a new citation enters the text. |

### `appendix_E.ipynb` (8 cells)

Intro, E.1 equations (E1-E6), **Code Cell E1** (architecture with the relay), **Code Cell E2** (main's
Code Cell 2 plus four checks), **Code Cell E3** (diffs E2's output against main's stored output),
E.2 commitments, E.3 claims in main restated, references.

### Outside this folder

- `~/Desktop/sections_3-5_outline.md`, `~/Desktop/background_sections_outline.md`: the dissertation
  outline. The composition guide covers them. Do not edit the `_copy` versions.
- **Not maintained, do not edit or treat as current:** `~/Desktop/revision*.ipynb`,
  `revision2 copy.ipynb`, `scalar_implicature_PC_annotated-7*`, `cell7_rebuilt_spec.md`,
  `mu_u_probe_report.md`.

---

## 2. Couplings that break silently

Each of these has broken at least once.

1. **Code Cell E2 is a copy of main's Code Cell 2.** E3 diffs their printed output line by line.
   Any edit to main's Code Cell 2, a comment included if it is printed, must be mirrored into E2 in
   the same pass. Mirror by lifting the source verbatim out of main, never by retyping.
2. **E3 finds its baseline by the exact prefix `# === Code Cell 2`.** Renaming main's code cells
   breaks it with `StopIteration`.
3. **E3 drops lines that begin with `cost:`.** Anything run-dependent (wall-clock seconds) must be
   printed behind that prefix, or E3 fails on noise.
4. **E3 reads main's stored outputs**, so main must be executed before appendix_E, and main's
   outputs must be current when appendix_E runs.
5. **Equation numbers.** Body (Text cells 3-6) is one run, (1)-(41), no letter suffixes. Appendices
   restart with their letter (A1..., B1..., C1..., D1..., E1...). Bogacz is cited by his own numbers,
   which interleave with ours (6, 7, 11 collide). Inserting a numbered display into the body shifts
   every later number: ask the user first. Unnumbered displays are the established alternative.
6. **Anchors and the table of contents.** Every link target is an explicit inline anchor inside the
   heading (`### <a id="..." name="..."></a>Title`). Code cells cannot hold anchors, so `code1`..
   `code4` sit at the end of the markdown cell above. When a heading moves or is added, add its
   anchor and regenerate cell 0.
7. **Never replace `sys.stdout` with a tee under ipykernel.** It silently kills stream capture for
   the rest of the session. `contextlib.redirect_stdout` is safe.

---

## 3. Integrity of the architecture

The direction of authority is **prose defines, code implements**. Text cell 3 specifies the model;
the code cells are an implementation of it. When the two disagree, do not repair whichever is more
convenient. Record the disagreement (§3.3) and ask the user which side is wrong.

### 3.1 Recording decisions in `decisions.md`

**What counts as a decision.** Any choice that a different, defensible choice could have replaced
and that a result, an equation, or a sentence of the argument depends on. That includes:

- the form of a generative map, error, update rule, or free-energy term;
- what is fixed, what is variational, what is plastic, and each fixed value;
- a baseline, control, criterion, prior, or statistic of the evaluation;
- a numerical surrogate for the dynamics (closed forms, stopping rules, feasibility thresholds,
  zero bands, step sizes);
- a naming or framing convention that constrains what the prose may claim.

Choices of pure presentation (layout, variable spelling in a loop) are not decisions.

**Entry format** (the template is at the top of `decisions.md`). Every entry carries:

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
2. Find the Bogacz equation it should instantiate in `Bogacz_2017_Free_Energy_Tutorial.md`, and write
   out the substitution that makes it an instance (e.g. Eq. (10) is his Eq. (42) with Θ = θ_u b,
   h = id; Eq. (19) is his Eq. (53) with Θ_L = −I).
3. Assign one verdict:
   - **Instance:** the substitution is exact.
   - **Instance under restriction:** exact after a restriction he also covers (e.g. Σ = I). Name it.
   - **Divergence:** no substitution works, or the operation has no counterpart in the tutorial.
   - **Surrogate:** a numerical stand-in. State the operation it replaces and the measured agreement
     with it.
4. **Every divergence goes into the Bogacz divergence register of `decisions.md`** with: what
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
| **(c) Control** | A deliberate departure from the model (e.g. θ_u held fixed). Under decision E4 its justification is stated in the prose where it is used, and it is labelled as a control in the output. |
| **(d) Implementation constant** | A numerical choice with no model meaning (grid size, tolerance, feasibility threshold, zero band). Recorded in `decisions.md` with evidence that the results it supports do not depend on its exact value. |
| **(e) Does not follow** | None of the above. **Flag it to the user in the same turn, add it to the quantity trace register in `decisions.md`, and neither keep it silently nor remove it silently.** |

**Rules.**

- **Every number quoted in prose is printed by a cell**, or else by a script recorded verbatim in a
  change record, with the prose site listed there. Numbers computed off-notebook and typed in are
  class (e) until one of those holds.
- **Three objects must never be conflated, in code names, labels, or prose:** q_lit, the literal
  listener (θ_u = 0 **and** σ_S → ∞, field ℓ₀ − φ_L); the tempered control (θ_u = 0 at the model's σ,
  field ½(ℓ₀ − φ_L), which is also the model's start); and the model (learned θ\*). "The control"
  unqualified is not allowed.
- A default argument is a quantity. A `theta_u=1.0` default that an evaluation silently inherits is
  class (e) unless it is a stated control.
- When a quantity's class changes (a control becomes the model, a constant becomes a parameter),
  that is a decision: §3.1.

---

## 4. Backups before high-risk changes

The folder is not under version control, so backups are the only way back.

**High-risk, backup required first:**

- any edit to a code cell;
- any execution that overwrites stored outputs (E3 treats main's outputs as evidence);
- any scripted or bulk edit across cells: renumbering, find-and-replace, whitespace normalization,
  ToC regeneration;
- inserting, deleting, moving, or splitting cells;
- rewriting (not appending to) `decisions.md`, `composition guide.md`, or a change record;
- any edit to files outside this folder.

A single hand edit to one prose sentence is low-risk. When unsure, back up: it is cheap.

**Procedure.**

1. Make a **new** folder `backups/YYYY-MM-DD-<short-label>/`, where the label says what it precedes
   (`2026-09-14-before-part-c-rewrite`). **Never copy into an existing backup folder** (F33: this
   destroyed the only pre-T8 snapshot).
2. Copy every file the change may touch, plus `decisions.md`.
3. Write a `README.md` in that folder: the date, what change it precedes, the files, and the byte
   size and sha256 of each original and each copy.
4. Check the hashes are equal before making the change.
5. Never modify or delete a backup. A snapshot of the finished state goes in its own
   `-after-<label>` folder.

---

## 5. Procedures

### 5.1 Execution and verification

Run notebooks with nbclient, in place, from this folder, `main.ipynb` first:

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
- **Baseline as of 2026-09-13:** `main.ipynb` 0 errors, 6 figures, 14/14 specification checks,
  about 225 s; `appendix_E.ipynb` 0 errors, 3 figures, E2 18/18, E3 PASS, about 560 s. Any departure
  from this is a finding, reported with the output, not explained away.
- Report what was run and what it returned. If a step was skipped, say so.

### 5.2 Numerical reporting

- Step counts are quoted to three significant figures; the cells may print the exact integer.
- Wall-clock figures are printed behind `cost:` and are not quoted as exact.
- Sign counts over the plane use the 1e-12 zero band (F24).
- A fixed point from a closed form states that it is one, and names the configurations where the
  dynamics were actually integrated and how closely they agreed.
- Stopping tolerances sit above the roundoff floor (F34, decision I3).

### 5.3 Change records for multi-step work

Any change spanning more than one cell or session gets a working record in this folder, on the
pattern of `theta_u_learned_reach.md`:

1. the user's instructions, verbatim;
2. the decisions the change rests on, with pointers into `decisions.md`;
3. tasks **in order**, backup first, each closed as `[x] Tn (date): what changed; acceptance result`;
4. a findings log, written the moment something unexpected appears, before moving on;
5. only after the code tasks close, the list of prose sites that must change, written against the
   executed outputs.

**Code before prose.** Prose is rewritten against outputs that exist, never against expected ones.

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
- Settled naming and framing conventions are in `decisions.md` section C. The ones most often
  broken: no Gricean reference frame; θ_L, not β; F is maximized; the three objects of §3.3.

---

## 6. Checklists

**Session start**

- [ ] Read this file, `decisions.md`, and the relevant change record.
- [ ] Confirm the files named in §1 exist and the cell map still holds (count cells, check headers).
- [ ] Read the composition guide if prose will be touched.
- [ ] Back up (§4) before the first high-risk edit.

**Before closing any change**

- [ ] Every new or altered operation checked against Bogacz; divergences registered (§3.2).
- [ ] Every new or altered quantity classed (a)-(e); class (e) flagged to the user (§3.3).
- [ ] Every decision recorded with who made it; agent decisions named to the user (§3.1).
- [ ] Main's Code Cell 2 and E2 still mirror; E3 prefix intact (§2).
- [ ] Both notebooks executed; results match the baseline or the departure is reported (§5.1).
- [ ] Every number the prose quotes is printed by a cell or a recorded script (§3.3).
- [ ] Anchors, ToC, equation numbers, and references cell consistent (§2).
- [ ] Change record and `decisions.md` updated, so the next agent does not depend on your memory.
