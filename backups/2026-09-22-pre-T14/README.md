# 2026-09-22, before T14

`main.ipynb` as it stood at 12:38, immediately before T14 rewrote Code Cell A's granularity block.

**This is the only 2026-09-22 snapshot whose contents are not already in git.** It was taken from a
*working* state, not a committed one: the session opened with `main.ipynb` modified against
`7754cb5`, carrying an earlier, unfinished version of the same work.

What it holds that no commit does:

- `granularity_report` in its **first** form — two base priors under ad-hoc names (`N(0,1) in zeta
  (default)`, `Beta(3,1) in s`) rather than all four of `BASE_WORLD_PRIORS`; a **`mode step`**
  measured against the tempered fixed point rather than against `ell_0`, which disagreed with
  Code Cells 2 and 4; the q shift printed to four decimals, so a status change appeared between two
  numbers both shown as `0.0000`; and crossing language in the block's own header and docstring.
- Appendix A's **first** crossings prose, saying the criteria "**cross**" with n and quoting
  crossing points as if located rather than bracketed.

All of it was superseded deliberately, on the user's instruction of the same day that the four
criteria be printed per (n, Lambda, ell_0) and that flips be described in text rather than printed.
Commit `2068268` is the replacement and records why each part changed. Nothing here is a lost
change; it is kept because it is the state the corrections in that commit were made against.
