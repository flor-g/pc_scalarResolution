# The introduction brought into line with C10 and C11 (opened 2026-09-24)

Working record under `agent/agent.md` §5.3. Fold into `agent/history.md` when it closes.

## 1. The user's instructions

> Then let's look at the introduction.

The agent's plan (five items; the fifth, a line on "is" against "need not be", ruled **out** by the
user), then:

> item 5 is out. Now draft it.

The introduction is the background's *Opening*; the draft also covers background §2.6's answer
line and the closing bridge, which the plan named with it.

## 2. What the draft must carry

- C10: the answers to the three questions are the thesis; scalar implicature is the main
  demonstration; question 2's answer is **no** (joint settlement of φ_S with φ_u given the clamped
  φ_L, not a single feedforward pass); the semantic/pragmatic division is posed and left open.
- C11: scalar resolution and scalar implicature defined before the questions use them;
  strengthening left to §1.1; "explicit competition", never "without alternatives".
- Composition guide 5a: "a single feedforward pass" is unsourced, so it is defined where the
  question first uses it — as the user defined it: it computes successive linguistic
  representations in sequence (lexical, situational, utility). The agent's first definition ("a
  semantic value and then a pragmatic one on it, once") was inaccurate (user) and is superseded.

## 3. The draft as first shown (superseded in one place; see §5)

### 3a. Replaces the *Opening* (background lines 36–80), budget 245 → 320

```
# Opening: three questions, and the level they are asked at (about 320 words)
 
- **Main claim to establish:** Scalar interpretation is a test case for theories of inference
  because the listener must integrate lexical meaning, alternatives, assumptions about the speaker,
  and prior world knowledge — and because the field disagrees not only about the answer but about
  what kind of answer is wanted. **The dissertation's thesis is its answer to three questions about
  scalar resolution, and scalar implicature is where that answer is demonstrated.**
- **Material to include, in three moves.**
  1. *The explanandum, and the two terms the questions need.* **Scalar resolution** is picking a
     value on a scale. Introduce *some* as semantically compatible with *all* but often interpreted
     as *some but not all*: that interpretation, **scalar implicature**, is a peculiarity of scalar
     resolution. Leave *strengthening*, the mechanism proposed to yield it, to §1.1, which keeps
     the two apart.
  2. *The three questions*, stated as questions and in this order, so the reader knows from the
     first page that their answers are the thesis and that scalar implicature, run through one
     implementation, is the main demonstration:
     - **What computational constraint(s) might scalar resolution obey?**
     - **Is scalar resolution a single feedforward pass?** Define the term in the same sentence: a
       single feedforward pass computes successive linguistic representations in sequence — the
       lexical, the situational and the utility representations.
     - **Can patterns observed in scalar resolution be understood as peculiarities arising at the
       algorithmic rather than the computational level?** — with the three sub-questions named:
       whether explicit competition among alternatives is necessary to produce scalar implicature,
       and whether it is a separate module from world-prior inference; what mechanism underlies
       extreme-favouring resolution for complete-scale inference; and how the semantic/pragmatic
       division is drawn to begin with. **Say in the same place that the last is posed and left
       open at this phase**: the architecture takes the lexical entry as given, and the division
       cannot be drawn until the entry is inferred rather than supplied.
  3. *The level distinction, fixed by contrast rather than by definition.* [unchanged]
- **Evidence and citations:** [unchanged]
- **Guard against overclaiming:** Do not announce that either literature proves neural predictive
  coding. Do not promise that the dissertation settles the semantic/pragmatic assignment question:
  it poses it and leaves it open at this phase (move 2), and what it argues is only that the
  question's *form* presupposes staging (§1.5).
- **Drafting note.** [unchanged]
```

Also the *Scale and argumentative shape* line: "**Opening (about 320 words).** The explanandum and
its two terms; the three questions whose answers are the thesis, the third's last sub-question left
open; and Marr's levels, fixed by contrast with RSA." Target length 4,160 → 4,235.

### 3b. Background §2.6, the italic line under the heading

```
*This is the dissertation's answer to the second question, and the answer is **no**: given the
clamped \(\varphi_L\), scalar resolution here is the joint settlement of \(\varphi_S\) with
\(\varphi_u\), not a single feedforward pass. Note the warrant: the claim is about **staging**, not
about message direction.*
```

### 3c. The closing bridge's first bullet (budget unchanged, 120)

```
- State the three questions once more, and that one architecture answers them together because the
  constraint generates the rest — the one sub-question it leaves open, the semantic/pragmatic
  division, named as open, because the entry is taken as given:
  > The architecture is built under locality; given the entry the utterance clamps, it settles the
  > world belief and the utility state jointly rather than in a single feedforward pass; and it
  > yields scalar implicature with no explicit competition among alternatives at any point.
```

## 4. Tasks

- [x] IN1 (2026-09-24): the plan set out; item 5 ruled out (user).
- [x] IN2 (2026-09-24): draft written (§3).
- [x] IN3 (2026-09-24): the definition of a single feedforward pass corrected by the user
      (successive linguistic representations in sequence: lexical, situational, utility).
- [x] IN4 (2026-09-24): the semantic/pragmatic sub-question moved from the third question to the
      second (user), in the draft and in the central claim; draft approved and applied to
      `thesis_outline/background_sections.md` (Opening, *Scale* line, target, §2.6, closing bridge);
      records; folded.

## 5. As applied

The draft of §3 with one change: question 2 carries the division sub-question ("Name its
sub-question, how the semantic/pragmatic division is drawn to begin with, and say in the same place
that it is posed and left open at this phase …"), and question 3 names two sub-questions. The
*Scale* line reads "the second's sub-question left open".
