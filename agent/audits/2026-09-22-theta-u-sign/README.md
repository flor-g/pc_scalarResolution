# The θ_u\* "sign flip": a retraction, and what replaced it

Run 2026-09-22, after the O13 probes. `sign.py` / `output.txt`. **The result of this audit is now
printed by Appendix F block F.9**, so it is no longer class (e); this directory is kept as the
derivation and is not the source the prose cites.

## What was claimed, and why it was wrong

The previous turn reported that θ_u\* takes **opposite signs** in the two image conditions of the
minimum class — −871 under shapes, +1605 under artifacts — and offered that as the mechanism behind
the misfit. Both halves fail.

**1. Those were means of a quantity that has no usable mean here.** The sign varies item by item,
and |θ_u\*| diverges near Appendix B's degenerate ray, so one near-ray item dominates an average:

| | neg | pos | median | mean | max \|θ_u\*\| |
|---|---|---|---|---|---|
| min / shape | 11 | 0 | −720.9 | −871.0 | 2,025 |
| min / artifact | 11 | 1 | **−769.8** | **+1604.7** | **29,123** |

By median both conditions are negative and nearly equal. The "+1605" is one item at ⟨μ_u,Σc⟩ = 0.336.

**2. The sign could not have reached the belief anyway.** At these magnitudes the settled field is
within 4.9e-03 of Eq. (24)'s limit, and that limit is **the same from either sign** — the two-sided
convergence this project established in the Appendix B ray work. Scoring the limit in place of the
settled field changes no R² in the third decimal. The check was available and was not run.

## What survives, and is stronger

**Eq. (F3).** The ensemble is {χ, ker χ}, so χ + ker χ = **1**, Σ_y φ_L,y = Λ·**1**, and the Λ term
cancels against BᵀW**1** = 0 (Appendix C §2):

    Σ_y c_y = BᵀW(2ℓ₀ − Λ·1) = 2 BᵀW ℓ₀          exact to 7.4e-13

Eq. (B2) gives θ_u\* the sign of ⟨μ_u, Σ_y c_y⟩, so **that sign is fixed by the prior alone —
independent of Λ and of which entry was uttered.** Architectural, and new.

**The amplification's reach.** Eq. (24) doubles the span(B) component of ℓ₀ − φ_L, displacing the
read-out up the scale by **+1.12** (shapes) and **+1.39** (artifacts) — near-constant — while the
data are displaced **+0.16** and **+1.06**. In the maximum class both are within 0.02 of zero.

§5.2 states, in "we think" form and as a belief about this phase, that this near-constant
displacement is the cause of the minimum class's misfit (R28). The notebook does not: B10/C7 stands,
so Appendix F §6 describes the quantities and attributes nothing.

## The reporting lesson

**Never average θ_u\* over items.** Near the degenerate ray its magnitude diverges and its sign
turns, so a mean mixes signs and is dominated by whichever item sits closest to the ray. Medians and
sign counts; block F.9 prints both, and `agent/decisions.md` A5 records why.
