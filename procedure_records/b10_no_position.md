# B10: reporting the conditions without taking a position

Working record (agent.md §5.3). **Status 2026-09-14: the user gave the go-ahead with naming and wording (C7); revision in progress.**

## 0. Instruction (the user's, verbatim, 2026-09-14)

> your decisions are confirmed. Just remember that we do not take a position that both conditions
> need to be met to count as scalar strengthening. We are just reporting them so that the reader can
> make their own judgment. (Any positions we take would be left to the paper, not the notebook. )
> Execute next step.

> (2026-09-14, second instruction) criterion is kay. Calling it a criterion does not mean we commit to
> this criterion. Also, for clarity, call the first criterion/(a) "the shift criterion" and the second
> criterion/(b) "the position criterion".  When you need to specify which read-out the criterion is in
> terms of, say "the q/mode shift/position criterion Do not use the word "condition" or verdict"
> because we want to keep word choice consistent and avoid confusion.
> For old sentences like "we take", we can substitute with "the reader, in accordance with their own
> judgement, may take satisfaction of the disjunction, the conjunction, either one of the two alone,
> or even nether criteria as scalar strengthening. This notebook takes no position on how the criteria
> should be interpreted."

## 1. Decisions

- **B10** (user, 2026-09-14): the notebooks report Part C's two conditions (B2) and the delta
  read-out's two criteria (B8), each and together, as measurements, and take no position on what
  counts as scalar strengthening.
- B2 is superseded in part by B10; its definitions of the two conditions stand.

## 2. Sites that take the position, or read the conditions as a verdict

Found by searching both notebooks for criterion, verdict, scalar implicature, sufficient,
strengthen, stipulat, "we take / adopt", "counts as". Line wording is quoted in short.

### Text cell 4 Part C (the core)
- The opening: "**C** asks whether the network produces a scalar implicature. The question needs an
  operational form, and we adopt one."
- **The criterion** paragraph: "We take scalar strengthening to be the conjunction of two
  conditions", "Neither is sufficient alone", with the argument for each; "every verdict below is
  relative to it".
- "**The criterion is not met under the default Gaussian prior.**", "toward the criterion without
  reaching it", "the verdict can be shown in the dynamics".
- "commitments anyone reading that outcome as scalar implicature thereby takes on" and the two
  commitments' framing; "A reader who wants scalar strengthening to follow …".
- The closing section: "the conjunction is reached … without an alternatives space" reads the
  conjunction as the target. The user's sentence on alternative competition is the user's own and is
  not a site.

### Text cell 4, other parts
- *Integration cost*: "how much of it the criterion actually needs", "How much of θ_u\* the
  criterion needs", "the θ_u its verdict needs", "So Part C's verdict is demonstrated in the
  dynamics", "the verdict *at θ_u\**", "how much machinery a scalar implicature should need".
- Text cell 4b: "moves … away from the criterion"; "the prior overriding the entry as well as the
  criterion".

### Text cell 3
- "the θ_u\* the evaluation's criterion turns out to need"; "the criterion it is judged by is one";
  "the criterion Text cell 4 adopts is met at a …".

### Text cell 5
- "The criterion adopted in Text cell 4 Part C is not a contrast between …"; "an implicature under
  that criterion".

### Text cell 6
- "not a second criterion, since the criterion is stipulated on the raw …"; "both verdicts are …";
  "The cells where the criterion is met"; "the θ_u the criterion itself needs"; "the criterion it
  serves is a stipulation of …"; "the θ_u its verdict needs".

### Appendix B
- "the baseline the criterion is measured against"; "the criterion it is judged by is met at a …".
  (The literature summary on strengthening, Gazdar, Levinson, Sauerland, is description, not a site.)

### Appendix C
- §1 title "Two readings of the criterion"; "This is Part A's criterion" (Appendix C's own sense,
  to check); "This model's verdict is that the gap …" (Horn's gap; a different sense, to check).

### Printed lines, Code Cell 2 (mirrored in E2)
- `SCALAR IMPLICATURE PROBE` header.
- "Under the criterion of Text cell 4 Part C, the conjunction, the criterion is met / NOT met";
  "Whether the criterion is met is a measurement; what meeting it commits …"; "the same criterion is
  met by other utterances too".
- "(a scalar implicature for \"some\" requires a NEGATIVE shift)".
- "Whether it is met is therefore NOT a property of the model alone … criterion as much as about the
  model".
- "Ascending F~ moves the shift DOWN, toward the first condition …", "the criterion: raising
  |theta_u| amplifies …".
- "Part C's verdict does not wait for it."
- Function name `updates_to_criterion` (a name, not printed; decide whether it matters).

### Printed lines, Code Cell 2b (mirrored in E2b)
- "This is the case the criterion is under the most pressure in"; "AWAY from the criterion".

### Not sites
- "sufficient" in Text cell 3 (μ_u ≠ 0 necessary, not sufficient), Reporting statistics ("the
  nonlinearity is sufficient"), Text cell 5 and Appendix C (m = 2 sufficiency): unrelated senses.
- "stipulation" in Appendix A (Eq. 8 a consequence, not a stipulation): unrelated.
- References.

## 3. What a revision would do (proposal of 2026-09-14, SUPERSEDED by C7 and §4)

- Replace "criterion" by "the two conditions" (and "the delta read-out's two criteria" stays B8's
  name only if the user wants "criteria" kept for those), and "met/verdict" by "holds / does not hold".
- Part C's criterion paragraph becomes a definition of two reported conditions with what each
  measures, without "we take scalar strengthening to be" or "neither is sufficient alone"; the
  arguments for requiring both move to the paper.
- The commitments paragraph keeps its measurements (prior and strength dependence, the mechanism) and
  drops the framing that they are commitments of an implicature reading.
- Printed lines follow the same wording; E2/E2b mirror; both notebooks re-executed.

## 4. The wording pass (T1, 2026-09-14, under C7)

Checkpoint 7854b8f. Script `c7_rename.py` (every replacement asserted exactly once; main cells and
their appendix E mirrors patched together), filed with its run output in `audits/2026-09-14-no-position/`.
Executed together with `delta_criteria_printing.md` T1: main 0 errors, 8 figures, 14/14; appendix_E 0
errors, 5 figures, E2 18/18, E3 PASS (202 and 233 lines identical), E4 unchanged; ToC 72 links resolve.
Every changed output line is a C7 rename, the T1 block, or Code Cell 3's "requirement".

- [x] **Applied.**
  - **Names.** Every criterion-sense "condition" became the q shift / q position criterion (Part C,
    Part D, Text cell 4b, Text cell 6, *Integration cost*, Text cells 3 and 5, Appendix B), or
    "criteria"/"both q criteria" for the pair. Table headers "first | second" became "q shift | q
    position". Printed lines in Code Cells 2, 2b and 4 (and E2, E2b) follow.
  - **Stance.** Part C's "We take scalar strengthening to be the conjunction … Neither is sufficient
    alone" is replaced by definitions of the shift and position criteria, the facts about what each
    can be met by, and the user's sentence verbatim ("nether" read as "neither"). "we adopt one" became
    "Part C states two criteria"; "adopts" / "judged by" became "reports"; "every verdict below is
    relative to it" became "everything reported below is relative to them".
  - **Printed position line removed.** "(a scalar implicature for "some" requires a NEGATIVE shift)"
    now reads "(the q shift criterion for "some" is a NEGATIVE shift)"; the probe's "what meeting it
    commits the model to is argued in Text cell 4 Part C" now reads "this notebook takes no position on
    how they should be interpreted".
  - **The delta read-out's criteria defined in Part D** (new paragraph after the peak paragraph): the
    mode shift and mode position criteria, not assumed to agree with the q criteria, no position.
    T1's printed block uses the four names.
  - **"verdict"** removed everywhere: prose ("result", "what Part C reports", "the conjunction"),
    Appendix C ("This model's answer"), and the identifiers in Code Cell A (`outcome`) and E3
    (`passed`, `strong_passed`), none of which printed the word.
  - **Unrelated senses of "condition" renamed** where a reader could confuse them with the criteria:
    "standing condition" → "standing requirement" (Text cell 3 §9.1 heading and ToC, Appendix B,
    E.3); "stationarity condition" → "stationarity equation" (Code Cells 1, 2, E1, E2, Text cell 5,
    Appendix B); "fixed-point condition" → "fixed-point equation" (Appendix A); "the exact condition",
    "a condition on direction", "Appendix B's condition", "the full condition" → "requirement" (Text
    cells 3 and 5, Code Cells 1 and 3, E1); "three conditions" of §8's proofs → "three assumptions";
    "Two conditions can be asked of B" → "Two requirements" (Appendix C); "the flat condition" → "the
    flat prior" (Part D, Text cell 6, Code Cell 2); the pseudocode's "conditions how much" → "sets how
    much"; Code Cell 4's `floor(condition, …)` parameter → `holds`.
- **Kept, as fixed technical compounds** (agent, pending user confirmation): "condition number" (Text
  cells 3 and 4, Code Cell A), "boundary condition" (Code Cell 1, E1), "truth-conditional" (Text cell
  3), "a conditional" (Text cell 3 §8.6), "conditioning" (literal conditioning; the *Integration cost
  and conditioning* heading and its references), "precondition" (Code Cell 2b and E2b comments).
