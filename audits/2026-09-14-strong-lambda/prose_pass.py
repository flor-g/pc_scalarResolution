r"""Prose pass for the strong-Lambda change (S-6, §5 of the change record). Scratch.

Every replacement is asserted to occur exactly once in the current text. After patching, every
decimal in the new prose is looked up in the notebooks' stored outputs, and misses are listed."""
import json, pathlib, re
import nbformat

ROOT = pathlib.Path("/Users/flog/Desktop/predictive coding")
main = nbformat.read(ROOT / "main.ipynb", as_version=4)
appx = nbformat.read(ROOT / "appendix_E.ipynb", as_version=4)
new_texts = []


def patch(cell, pairs):
    text = cell.source
    for old, new in pairs:
        assert text.count(old) == 1, (text[:40], old[:90], text.count(old))
        text = text.replace(old, new)
        new_texts.append(new)
    cell.source = text


# ------------------------------------------------------------------ Text cell 3
assert main.cells[4].source.startswith('## <a id="tc3"')
patch(main.cells[4], [(
    r"$p_0=\mathcal N(0,1)$, one of the five base priors Text cell 4 Part D runs.",
    r"$p_0=\mathcal N(0,1)$, one of the base priors Text cell 4 Part D and Text cell 4b run.",
)])

# ------------------------------------------------------------------ Text cell 4
assert main.cells[6].source.startswith('## <a id="tc4"')
patch(main.cells[6], [
(r"""it is measured against, and the dashed line in every panel of Part D, is $q_{\mathrm{lit}}$, the""",
 r"""it is measured against, and the dashed line in every panel of Part D and Text cell 4b, is
$q_{\mathrm{lit}}$, the"""),

(r"""construction itself, the delta at the settled state, is reported beside them in Part D. Eq. (37)""",
 r"""construction itself, the delta at the settled state, is reported beside them in Part D and Text
cell 4b. Eq. (37)"""),

(r"""$\theta_u^\ast$, which the closed form supplies rather than the flow. Under the delta-like prior of Part D, already concentrated on
the all-region, **both conditions are met**, $\Delta_{\textit{some}}=-0.5217$ with $q_H=0.4351$.
**Across Part D's five priors the conjunction holds under exactly one**, and the two conditions
separate the other four between them. The conjunction does not need that prior's whole
$\theta_u^\ast$: it turns on at $\lvert\theta_u\rvert=2.126$ and holds from there to
$\theta_u^\ast=1407.77$, which is why the verdict can be shown in the dynamics rather than only in
the closed form (*Integration cost and conditioning* below). It is not a solitary case either: Text cell 6 sweeps the same
prior family against $\Lambda$ and finds a band of $33$ cells where both hold at once, the
delta-like row among them.""",
 r"""$\theta_u^\ast$, which the closed form supplies rather than the flow. **Across Part D's four priors,
all at $\Lambda=8$, the conjunction holds under none**: the second condition holds under each and
the first under none. **With every prior at $\Lambda=512$ (Text cell 4b), it holds under three**:
the flat prior ($\Delta_{\textit{some}}=-0.0146$, $q_H=0.0357$), $\mathrm{Beta}(3,1)$ ($-0.0955$,
$0.0413$), and the delta-like prior concentrated on the all-region, which needs that $\Lambda$
($-0.5217$, $0.4351$). The conjunction does not need those priors' whole $\theta_u^\ast$: it turns
on at $\lvert\theta_u\rvert=3.078$, $1.021$ and $2.126$ respectively and holds from there to
$\theta_u^\ast$, which is why the verdict can be shown in the dynamics and not only in the closed
form (*Integration cost and conditioning* below). Text cell 6 sweeps the $\mathrm{Beta}(\alpha,1)$
family, which contains the flat and delta-like priors, against $\Lambda$ and finds a band of $33$
cells where both hold at once; the flat and delta-like rows of Text cell 4b are two of them."""),

(r"""*Nor is the first condition, where it is met, specific to* some. Under the Gaussian prior it is met
by *all* ($-0.4557$) and by neither *no* ($+0.0003$) nor *some*. Under the delta-like prior *no* and *all* are both saturated, holding
$0.0000$ and $1.0000$ of the all-region at baseline, so their zero shifts are saturation and not
restraint; only *some* had room to move, and moved.""",
 r"""*Nor is the first condition, where it is met, specific to* some. Under the Gaussian prior at
$\Lambda=8$ it is met by *all* ($-0.4557$) and by neither *no* ($+0.0003$) nor *some*. The entry
for *all* does not hold there: $0.6260$ of the settled belief given *all* lies in the region that
entry excludes. At $\Lambda=512$, where every entry holds, *no* and *all* are saturated under all
five priors, holding $0.0000$ and $1.0000$ of the all-region at baseline, so their zero shifts are
saturation and not restraint; only *some* had room to move, and it moved under three of the five.
Whether the verdict for *all* at $\Lambda=8$ should be read together with that leak is a fact we
note, and our position on it is reserved."""),

(r"""*Firstly, strengthening is prior-relative.* Part D's table carries the five shifts and the sign
follows the prior across them. And it is the prior doing that rather than the raised $\Lambda$ the
delta-like row has to carry: with the Gaussian prior restored at $\Lambda=512$, where the
configuration learns $\theta_u^\ast=+1580.81$ of its own, $\Delta_{\textit{some}}=+0.0071$, further
from the criterion than the $+0.0008$ at $\Lambda=8$ rather than nearer to it. So the effect is not a property of the entry for *some*; it is a property
of that entry against a particular world belief, and it appears exactly where the prior most
favours *all*. A reader who wants scalar strengthening to follow from the lexical scale alone
cannot have it here.""",
 r"""*Firstly, strengthening is relative to the prior and to the strength of the entry together.* At
Part D's $\Lambda=8$ the shift keeps one sign across the four priors and varies a hundredfold in
size, from $+0.0004$ to $+0.0421$. At $\Lambda=512$ its sign follows the prior: it is negative under
the three priors that put the most mass on the all-region, $0.0479$, $0.1367$ and $0.9568$ of it,
deepening with that mass from $-0.0146$ through $-0.0955$ to $-0.5217$, and positive under the two
that put the least, $+0.0071$ at $0.0016$ and $+0.0089$ at $0.0001$. Raising $\Lambda$, each
configuration at its own $\theta_u^\ast$, is what carries the flat and $\mathrm{Beta}(3,1)$ priors
across zero, from $+0.0295$ and $+0.0421$; it carries the Gaussian prior away from the criterion,
from $+0.0008$ to $+0.0071$ at a learned $\theta_u^\ast=+1580.81$. So the effect is a property of
the entry for *some* at a given strength against a particular world belief, and among the five
priors, at a strength where every entry holds, it appears exactly where the prior most favours
*all*. A reader who wants scalar strengthening to follow from the lexical scale alone cannot have
it here."""),

(r"""of either sign that Code Cell 2 sweeps,""",
 r"""of either sign that Code Cell 2b sweeps,"""),

(r"""architecture containing none produces it. It produces it under the one prior that gives the *all*
reading the most support, which is where standard RSA has the most to overcome, and produces it
nowhere else among Part D's five. The second condition is met alongside it there, $q_H$ holding
$0.4351$ of the all-region against the half the condition allows, so the conjunction holds under
that prior; it holds at $33$ of the $121$ cells Text cell 6 sweeps, where the same prior family is
paired with a stronger lexicon, and the delta-like row is a member of that band rather than its
neighbour. So the conjunction is reached in this architecture without an alternatives space, under
the prior Part C leans on and over a band of the plane, and not under the four diffuse priors.""",
 r"""architecture containing none produces it. At $\Lambda=512$ it produces it under the delta-like
prior, which gives the *all* reading the most support and is where standard RSA has the most to
overcome, and under the flat and $\mathrm{Beta}(3,1)$ priors; at Part D's $\Lambda=8$ it produces it
under none of the four. The second condition is met alongside it in all three, $q_H$ holding
$0.0357$, $0.0413$ and $0.4351$ of the all-region against the half the condition allows, and in all
three both conditions are also met off an integrated fixed point. Over the $121$ cells Text cell 6
sweeps, the conjunction holds at $33$, a band that contains the flat and delta-like rows. So the
conjunction is reached in this architecture without an alternatives space, under three of five
priors at a lexical strength where every entry holds and over a band of the plane, and not under
Part D's four priors at $\Lambda=8$."""),

(r"""**D** repeats the demonstration and the implicature probe under five base world priors: a
Gaussian in $\zeta$ (equivalently, $s$ logit-normal), a literal $\mathrm{Uniform}(0,1)$ over the
proportion, two skewed
$\mathrm{Beta}$ priors, and a delta-like $\mathrm{Beta}(64,1)$ concentrated on the all-region. The
last carries its own $\Lambda$ and is the case Part C leans on; the reason it needs one is given
with it below. The two beliefs""",
 r"""**D** repeats the demonstration and the implicature probe under four base world priors, all at
$\Lambda=8$: a Gaussian in $\zeta$ (equivalently, $s$ logit-normal), a literal
$\mathrm{Uniform}(0,1)$ over the proportion, and two skewed $\mathrm{Beta}$ priors. Text cell 4b
runs the same four, and a delta-like $\mathrm{Beta}(64,1)$ concentrated on the all-region, at
$\Lambda=512$. The two beliefs"""),

(r"""**The delta-like row, and why it needs its own $\Lambda$.** The other four priors are all diffuse
over the scale, so none of them puts the criterion under any pressure: hearing *some* under a belief
that is already spread out, there is little all-region mass to move away from. The sharp case is the
one worth testing. A literal $P_0(s{=}1)=1$ is not representable, since $s$ lies in the *open* interval,
$\zeta=\operatorname{logit}(1)$ is off the grid, and $\ell_0$ would be $-\infty$ almost everywhere, making
$r_S$ infinite. We therefore use the limit family $\mathrm{Beta}(\alpha,1)$ that Text cell 6 sweeps.
$\alpha=64$ puts the mode in $\zeta$ at $\log\alpha=4.16$, inside the all-region and clear of the
grid ceiling Text cell 6 describes; it carries $95.7\%$ of its prior mass in the all-region and only
$0.95\%$ on the top node, and the three utterances are still $0.0057$ apart in $\mathbb E[s]$ there,
whereas by $\alpha=1024$ they are $0.0003$ apart and the probe would be measuring the truncation. $\Lambda$ must rise with it, or the prior
simply overrides the entry and the probe measures the override instead of the criterion: Eq. (41)
puts the threshold at $\Lambda_{\mathrm{crit}}\approx\alpha\log2n=192$, and $\Lambda=8\alpha=512$,
about $2.7\times$ that, holds every leak below $1.1\times10^{-74}$. That row alone varies $\Lambda$,
which is why the figure below draws only the four that share $\Lambda=8$, since panels on a shared axis
have to be comparable.

""", ""),

(r"""$\ell_0$-invariant: across the five priors at a common $\Lambda$ they agree to
$3.6\times10^{-14}$.""",
 r"""$\ell_0$-invariant: across the four priors at a common $\Lambda$ they agree to
$5.3\times10^{-15}$."""),

(r"""Two of the five rows are integrated, the Gaussian and $\mathrm{Beta}(1,3)$, and there the settled
state agrees with Eqs. (15)–(16) to $1.0\times10^{-9}$ and $9.9\times10^{-10}$. The other three
carry $\theta_u^\ast$ of $5950.63$, $55.01$ and $1407.77$, which puts""",
 r"""Two of the four rows are integrated, the Gaussian and $\mathrm{Beta}(1,3)$, and there the settled
state agrees with Eqs. (15)–(16) to $1.0\times10^{-9}$ and $9.9\times10^{-10}$. The other two
carry $\theta_u^\ast$ of $5950.63$ and $55.01$, which puts"""),

(r"""$q_{\mathrm{lit}}$ runs $0.0016$, $0.0504$, $0.0001$, $0.1368$ and $0.9568$ down the five rows
below, against $0.0191$, $0.1357$, $0.0066$, $0.2356$ and $0.8982$ for the tempered belief, a
factor of twelve at the Gaussian row. Tempering flattens, and a flatter belief holds more mass at
the ends of the scale, which is where the all-region sits. The two coincide only where the prior
leaves the belief little room to flatten into, which is the delta-like row.""",
 r"""$q_{\mathrm{lit}}$ runs $0.0016$, $0.0504$, $0.0001$ and $0.1368$ down the four rows below, against
$0.0191$, $0.1357$, $0.0066$ and $0.2356$ for the tempered belief, a factor of twelve at the
Gaussian row. Tempering flattens, and a flatter belief holds more mass at the ends of the scale,
which is where the all-region sits."""),

(r"""What the sweep establishes is that $\Delta_{\textit{some}}$ is prior-relative:
$+0.0008$ (Gaussian), $+0.0295$ (flat), $+0.0004$ ($\mathrm{Beta}(1,3)$), $+0.0421$
($\mathrm{Beta}(3,1)$), $-0.5217$ (delta-like), each at that prior's own $\theta_u^\ast$, which is
the first of the two commitments Part C records. One
might expect the sign to be constant, on the ground that a quantity acting identically on every
utterance can move no contrast between them.""",
 r"""What the sweep establishes is that $\Delta_{\textit{some}}$ depends on the prior even where its sign
does not: $+0.0008$ (Gaussian), $+0.0295$ (flat), $+0.0004$ ($\mathrm{Beta}(1,3)$) and $+0.0421$
($\mathrm{Beta}(3,1)$), each at that prior's own $\theta_u^\ast$, a hundredfold range of one sign.
Text cell 4b has the case in which the sign follows the prior as well, and Part C records both as
the first of its two commitments. One might expect the shift to be the same under every prior, on
the ground that a quantity acting identically on every utterance can move no contrast between them."""),

(r"""direction: there an invariant contrast produces a drifting statistic, here it produces a change of
sign.""",
 r"""direction: there an invariant contrast produces a drifting statistic, here a hundredfold spread,
and in Text cell 4b a change of sign."""),

(r"""| $\mathrm{Beta}(3,1)$ | $+55.01$ | $0.1367$ | $0.1788$ | $+0.0421$ | not met | met |
| delta-like | $+1407.77$ | $0.9568$ | $0.4351$ | $-0.5217$ | **met** | **met** |""",
 r"""| $\mathrm{Beta}(3,1)$ | $+55.01$ | $0.1368$ | $0.1788$ | $+0.0421$ | not met | met |"""),

(r"""**The conjunction holds under the delta-like prior, and under it alone.** The first condition is
met by that prior and by no other, and the second is met there as well: $q_H$ leaves $0.4351$ of the
all-region in place, below the half the second condition allows. Under the other four the second
condition holds comfortably and the first fails, the settled belief holding more all-region mass
than the literal listener. So the conditions do not simply partition the sweep between them: four
rows meet the second alone, one meets both, and none meets the first alone.""",
 r"""**The conjunction holds under none of the four.** The second condition holds under each, $q_H$ at
most $0.1788$, and the first under none, the settled belief holding more all-region mass than the
literal listener in every row. Text cell 4b gives the same table at $\Lambda=512$, where three
priors meet both conditions and two meet the second alone."""),

(r"""The four rows where the first condition fails share a reading.""",
 r"""The four rows share a reading."""),

(r"""and not a utility level pushing mass toward the all-region. Only when the prior is already
concentrated there does the utility level move much mass at all, and there it moves it down hard,
by $-0.4631$, with the tempering itself turning slightly negative ($-0.0586$) because a prior that
sharp has nothing left to flatten into. So the sign of the shift is
a fact about the prior the entry is read against and not about the entry, which is Part C's first
commitment seen from the side of the prior.""",
 r"""and not a utility level pushing mass toward the all-region. How much the utility level undoes
depends on the prior and on $\Lambda$ together, which Text cell 4b measures."""),

(r"""each prior and utterance at that prior's $\theta_u^\ast$, and the delta-like row again at the
realizable $\theta_u=13.3749$ of *Integration cost and conditioning* below, integrated rather than
read from the closed form. $\varphi_u^\ast$""",
 r"""each prior and utterance at that prior's $\theta_u^\ast$. Code Cell 2b prints the same rows at
$\Lambda=512$, and again, integrated, at the realizable $\theta_u$ of each prior that meets the
conjunction there (*Integration cost and conditioning* below). $\varphi_u^\ast$"""),

(r"""$\theta_u$ and $\varphi_u$ only through their product (Eq. 10), so under *some* on the delta-like row
$\varphi_u^\ast$ moves""",
 r"""$\theta_u$ and $\varphi_u$ only through their product (Eq. 10), so under *some* on Text cell 4b's
delta-like row $\varphi_u^\ast$ moves"""),

(r"""$\varphi_S^\ast$ lies outside that cell under all five priors, at $s=0.5890$, $0.6726$, $0.3274$ and
$0.8429$ under the Gaussian, flat, $\mathrm{Beta}(1,3)$ and $\mathrm{Beta}(3,1)$ priors and at
$0.9468$ under the delta-like prior. Code Cell 2 prints each beside the **$\ell_0$ peak**, the $s$
at which the base world prior itself is largest; under *some* it is also where
$\ell_0-\varphi_L$ peaks, since $\varphi_L$ vanishes there under every prior. Under the four diffuse
priors the $\ell_0$ peak is outside the cell already, at $0.5000$, $0.5000$, $0.2535$ and $0.7465$,
and the peak of $\varphi_S^\ast$ lies above it on the scale, nearer the cell than the prior's. Only
under the delta-like prior is the $\ell_0$ peak inside the cell, at $0.9852$, while the peak of
$\varphi_S^\ast$ is outside it, at $\theta_u^\ast$ and at the realizable $\theta_u$ alike. That peak
is one grid node below $\theta_L$: the largest $\varphi_S^\ast$ inside the cell falls short of the
largest outside it by $0.081$ at $\theta_u^\ast$ and by $0.076$ at the realizable $\theta_u$. On grids
of $201$, $401$ and $801$ nodes the peak stays outside, by $0.114$, $0.053$ and $0.031$, and on the
finest it moves up to $s=0.9476$.""",
 r"""$\varphi_S^\ast$ lies outside that cell under all four priors, at $s=0.5890$, $0.6726$, $0.3274$ and
$0.8429$ under the Gaussian, flat, $\mathrm{Beta}(1,3)$ and $\mathrm{Beta}(3,1)$ priors. Code Cell 2
prints each beside the **$\ell_0$ peak**, the $s$ at which the base world prior itself is largest;
under *some* it is also where $\ell_0-\varphi_L$ peaks, since $\varphi_L$ vanishes there under every
prior. The $\ell_0$ peak is outside the cell already, at $0.5000$, $0.5000$, $0.2535$ and $0.7465$,
and the peak of $\varphi_S^\ast$ lies above it on the scale, nearer the cell than the prior's."""),

(r"""at $s=0.7465$. We note both and reserve our position on them.""",
 r"""at $s=0.7465$. They are the two rows whose largest leak is $0.91$, and Text cell 4b reports the
same peaks at a $\Lambda$ where every entry holds. We note both and reserve our position on them."""),

(r"""table says which it did. On the five priors of Part D that means the Gaussian and
$\mathrm{Beta}(1,3)$ are integrated and the flat, $\mathrm{Beta}(3,1)$ and delta-like rows are not;
on Text cell 6's plane,""",
 r"""table says which it did. On Part D's four priors that means the Gaussian and $\mathrm{Beta}(1,3)$
are integrated and the flat and $\mathrm{Beta}(3,1)$ rows are not; at Text cell 4b's $\Lambda=512$
no row is, $\lambda_{\max}(H)$ running from $1.98\times10^{6}$ to $2.53\times10^{6}$ at
$\theta_u^\ast$; on Text cell 6's plane,"""),

(r"""**How much of $\theta_u^\ast$ the criterion needs.** Much less, and the cell measures it rather than
assuming it. The conjunction of Part C turns on at $\lvert\theta_u\rvert=2.126$ under the delta-like
prior, where $\lambda_{\max}(H)$ is $6.5$, and it holds from there all the way to $\theta_u^\ast$;""",
 r"""**How much of $\theta_u^\ast$ the criterion needs.** Much less, and Code Cell 2b measures it rather
than assuming it. At $\Lambda=512$ the conjunction of Part C turns on at
$\lvert\theta_u\rvert=3.078$, $1.021$ and $2.126$ under the flat, $\mathrm{Beta}(3,1)$ and
delta-like priors, where $\lambda_{\max}(H)$ is $11.5$, $3.0$ and $6.5$, and under each it holds
from there all the way to $\theta_u^\ast$;"""),

(r"""updates. The cell therefore runs one such case end to end with nothing in closed form: one
integrated update of Eq. (20), then Eqs. (18)–(19) integrated at the $\theta_u=13.3749$ it reaches,
$39{,}035$ steps and under two seconds, giving $\Delta_{\textit{some}}=-0.5182$ and
$q_H=0.4386$ off the integrated fixed point, both conditions met.""",
 r"""updates. Code Cell 2b therefore runs each of its three such rows end to end with nothing in closed
form: one integrated update of Eq. (20), then Eqs. (18)–(19) integrated at the $\theta_u$ it
reaches, $7.8161$, $7.9926$ and $13.3749$, in about $13{,}600$, $14{,}200$ and $39{,}000$ steps.
Off those integrated fixed points $\Delta_{\textit{some}}$ is $-0.0119$, $-0.0925$ and $-0.5182$ and
$q_H$ is $0.0384$, $0.0442$ and $0.4386$, both conditions met in each."""),

(r"""which is $26$ at the
delta-like threshold and $7.9\times10^{6}$ at that prior's $\theta_u^\ast$.""",
 r"""which is $12$ to $46$ at the
three thresholds and $7.9\times10^{6}$ to $9.3\times10^{6}$ at those priors' $\theta_u^\ast$."""),
])

# ------------------------------------------------------------------ Text cell 4b
assert main.cells[8].source.startswith('## <a id="tc4b"')
text_4b = r"""## <a id="tc4b" name="tc4b"></a>Text cell 4b: Part D at a strong $\Lambda$

Code Cell 2b repeats the evaluations of Part D with $\Lambda=512$ for every base world prior and
every utterance, each configuration at its own learned $\theta_u^\ast$: Part D's four priors and a
delta-like $\mathrm{Beta}(64,1)$ concentrated on the all-region. The beliefs compared, the
$\theta_u$ control, the all-region and the two conditions are as Part C defines them, and the delta
read-out is as Part D defines it.

**Why a strong $\Lambda$.** At Part D's $\Lambda=8$ the diffuse priors override the entries for
*no* and *all*: the largest leak in a row is $0.63$ under the Gaussian prior and $0.91$ under both
skewed priors. Part of the settled belief given one of those utterances then lies in the region its
entry excludes, and those columns of Part D measure the prior overriding the entry as well as the
criterion. The delta-like prior needs a stronger lexicon still. A literal $P_0(s{=}1)=1$ is not
representable, since $s$ lies in the *open* interval, $\zeta=\operatorname{logit}(1)$ is off the
grid, and $\ell_0$ would be $-\infty$ almost everywhere, making $r_S$ infinite. We therefore use the
limit family $\mathrm{Beta}(\alpha,1)$ that Text cell 6 sweeps. $\alpha=64$ puts the mode in $\zeta$
at $\log\alpha=4.16$, inside the all-region and clear of the grid ceiling Text cell 6 describes; it
carries $95.7\%$ of its prior mass in the all-region and only $0.95\%$ on the top node, and the three
utterances are still $0.0057$ apart in $\mathbb E[s]$ there, whereas by $\alpha=1024$ they are
$0.0003$ apart and the probe would be measuring the truncation. $\Lambda$ must rise with $\alpha$, or
the prior simply overrides the entry: Eq. (41) puts the threshold at
$\Lambda_{\mathrm{crit}}\approx\alpha\log2n=192$, and $\Lambda=8\alpha=512$ is about $2.7\times$
that. This cell holds all five priors at that $\Lambda$, so that its rows share one lexical
strength, and under it every entry holds under every prior, the largest leak in any row being
$1.1\times10^{-74}$.

**Read the headroom first.** Under *no* and *all* the literal listener holds $0.0000$ and $1.0000$
of the all-region under all five priors, so the shifts of those two utterances are zero by
saturation, and only *some* has room to move either way. Code Cell 2b prints the headroom of every
row before its shifts.

**Where each of Part C's two conditions is met, at $\Lambda=512$.**

| prior | $\theta_u^\ast$ | $P_0(\text{all-region})$ | $q_{\mathrm{lit}}$ | $q_H$ | $\Delta_{\textit{some}}$ | first | second |
|---|---|---|---|---|---|---|---|
| Gaussian | $+1580.81$ | $0.0016$ | $0.0016$ | $0.0088$ | $+0.0071$ | not met | met |
| flat | $+1521.48$ | $0.0479$ | $0.0504$ | $0.0357$ | $-0.0146$ | **met** | **met** |
| $\mathrm{Beta}(1,3)$ | $+1589.49$ | $0.0001$ | $0.0001$ | $0.0091$ | $+0.0089$ | not met | met |
| $\mathrm{Beta}(3,1)$ | $+1499.37$ | $0.1367$ | $0.1368$ | $0.0413$ | $-0.0955$ | **met** | **met** |
| delta-like | $+1407.77$ | $0.9568$ | $0.9568$ | $0.4351$ | $-0.5217$ | **met** | **met** |

**The conjunction holds under three of the five**, the flat, $\mathrm{Beta}(3,1)$ and delta-like
priors. The second condition holds under all five and the first under those three, so no prior
meets the first alone. The three are the priors with the most prior mass on the all-region, and
across them the shift deepens with that mass. Set against Part D, raising $\Lambda$ from $8$ to
$512$ carries the flat and $\mathrm{Beta}(3,1)$ priors across zero, from $+0.0295$ and $+0.0421$,
and moves the Gaussian and $\mathrm{Beta}(1,3)$ priors away from the criterion, from $+0.0008$ and
$+0.0004$ to $+0.0071$ and $+0.0089$.

**What the shift is made of.** The tempering barely moves with $\Lambda$: $+0.0175$, $+0.0857$,
$+0.0065$, $+0.0989$ and $-0.0586$ down the five rows, against Part D's $+0.0175$, $+0.0854$,
$+0.0065$ and $+0.0988$. $\chi_{\textit{some}}$ is zero on the all-region, so $\Lambda$ reaches the
all-region mass of $q_{\mathrm{lit}}$ and of the $\theta_u$ control only through the normalizer,
over the bottom of the scale the entry excludes. The utility level's own contribution does move with
$\Lambda$: $-0.0104$, $-0.1003$, $+0.0024$, $-0.1943$ and $-0.4631$. Where the conjunction holds,
that contribution outweighs the tempering. Under the Gaussian prior it is smaller in magnitude than
at $\Lambda=8$ ($-0.0167$), and under $\mathrm{Beta}(1,3)$ it has turned positive.

**The prior matters less at this $\Lambda$.** Under *some* $\mathbb E[s]$ runs from $0.898$ to
$0.946$ across the five priors, and $\theta_u^\ast$ from $+1407.77$ to $+1589.49$. The $\varphi_S$
contrasts between utterances agree across the five priors to $1.1\times10^{-13}$ at a shared
$\theta_u=1$, a control, and to $0.0001$ at each prior's own $\theta_u^\ast$, against $0.058$ across
Part D's four. Every $\theta_u^\ast$ here lies deep in the saturation of Eq. (24), whose limit does
not depend on $\theta_u$, so the $\ell_0$-invariance that holds at a shared $\theta_u$ very nearly
carries across the rows.

**The figures.** Code Cell 2b draws the three utterances under the Gaussian prior, *some* under all
five priors, and the three utterances under the delta-like prior, all on a logarithmic vertical
axis: at this $\Lambda$ the settled densities pile against the ends of the scale and span several
orders of magnitude between panels. The comparison to read is the full network against the literal
listener within each panel.

**The delta read-out at this $\Lambda$.** Under *some* the peak of $\varphi_S^\ast$ lies outside the
cell of *all* under all five priors. Under the Gaussian, flat, $\mathrm{Beta}(1,3)$ and
$\mathrm{Beta}(3,1)$ priors it sits at $s=0.9072$, $0.9168$, $0.8966$ and $0.9168$, between five and
seven grid nodes below the cell and far above the $\ell_0$ peaks of $0.5000$, $0.5000$, $0.2535$ and
$0.7465$. Only under the delta-like prior is the $\ell_0$ peak inside the cell, at $0.9852$, while
the peak of $\varphi_S^\ast$ is outside it, at $s=0.9468$, both at $\theta_u^\ast$ and at the
realizable $\theta_u$ of Text cell 4's *Integration cost and conditioning*. That peak is one grid
node below $\theta_L$: the largest $\varphi_S^\ast$ inside the cell falls short of the largest
outside it by $0.081$ at $\theta_u^\ast$ and by $0.076$ at the realizable $\theta_u$. On grids of
$201$, $401$ and $801$ nodes the peak stays outside, by $0.114$, $0.053$ and $0.031$, and on the
finest it moves up to $s=0.9476$.

Under the flat and $\mathrm{Beta}(3,1)$ priors, then, the read-out $q$ meets both of Part C's
conditions while the peak of the delta read-out lies above the $\ell_0$ peak; under the delta-like
prior that peak lies below it. We note the difference and reserve our position on it. Under *no*
and *all* the peak sits at $s=0.0025$ and $0.9975$ under every prior, inside the cells of those two
entries, so neither of the two departures from an entry's own cell that Part D notes recurs at this
$\Lambda$.

<a id="code2b" name="code2b"></a>"""
main.cells[8].source = text_4b
new_texts.append(text_4b)

# ------------------------------------------------------------------ Text cell 6
assert main.cells[12].source.startswith('## <a id="tc6"')
patch(main.cells[12], [
(r"""a row of that table are the same measurement; the delta-like row, $\alpha=64$ and $\Lambda=512$,
is such a cell and reads $-0.5217$ in both places.""",
 r"""a row of that table are the same measurement; the delta-like row of Text cell 4b, $\alpha=64$ and
$\Lambda=512$, is such a cell and reads $-0.5217$ in both places."""),
(r"""which is the same point Part D makes for the delta-like row:""",
 r"""which is the same point Text cell 4b makes for its rows:"""),
(r"""Part D's delta-like configuration, $\alpha=64$ and $\Lambda=512$, is a cell of this""",
 r"""Text cell 4b's delta-like configuration, $\alpha=64$ and $\Lambda=512$, is a cell of this"""),
(r"""is also the number Part D's table carries,""",
 r"""is also the number Text cell 4b's table carries,"""),
(r"""**Four of Part D's rows sit outside that band and the delta-like row sits inside it.** Part D holds
$\Lambda=8$ for four of its priors, all diffuse enough that the first condition's floor sits far
above it; that floor drops below $\Lambda=8$ only at $\alpha\ge128$. The delta-like row raises
$\Lambda$ to $512$ at $\alpha=64$, which clears the first condition's floor of $16$ and the
second's of $512$ together, and it is the only one of the five to clear either. Holding that prior
and raising $\Lambda$ further deepens both:""",
 r"""**Part D's four rows sit outside that band, and at $\Lambda=512$ Text cell 4b's flat and
delta-like rows sit inside it.** Part D holds $\Lambda=8$, which clears the second condition's
floor of $2$ at $\alpha\le8$ but the first condition's floor only at $\alpha\ge128$; the flat prior,
$\mathrm{Beta}(1,1)$, is the cell $(1,8)$ and meets the second condition alone. At $\Lambda=512$
the flat prior meets the first condition's floor of $512$ and clears the second's, which puts it at
the band's corner, and the delta-like prior clears the first condition's floor of $16$ and meets
the second's of $512$. $\mathrm{Beta}(3,1)$ belongs to the family but falls between the plane's
$\alpha=2$ and $\alpha=4$, and the Gaussian and $\mathrm{Beta}(1,3)$ priors are not members of it.
Holding the delta-like prior and raising $\Lambda$ further deepens both:"""),
(r"""along the way. The row is at the
band's lower edge in $\Lambda$, not outside it.""",
 r"""along the way. The delta-like
row is at the band's lower edge in $\Lambda$, not outside it."""),
(r"""passes the threshold within one or two updates. Text cell 4's *Integration cost
and conditioning* runs one such case end to end without the closed form at any step.""",
 r"""passes the threshold within one or two updates. Code Cell 2b runs three rows of
this kind end to end, two of them cells of the band, without the closed form at any step (Text cell
4, *Integration cost and conditioning*)."""),
])

# ------------------------------------------------------------------ Code Cell 2b and E2b: F14
assert main.cells[9].source.startswith("# === Code Cell 2b:")
assert appx.cells[4].source.startswith("# === Code Cell E2b:")
code_pairs = [
(r'''def raised_lambda_control(net, rows):
    """The default Gaussian prior at the delta-like row's Lambda, against Part D's row."""''',
 r'''def raised_lambda_control(net, rows, strong_rows):
    """The default Gaussian prior at the delta-like row's Lambda, against Part D's row, and the
    priors under which raising Lambda alone carries the shift for "some" below zero."""'''),
(r'''          f"Lambda = {net.lexical_strength:.0f}. Raising Lambda alone moves the shift")
    print("  AWAY from the criterion, so the delta row's result is the prior's doing")
    print("  and not its Lambda's (Text cell 4 Part C).")
    print()''',
 r'''          f"Lambda = {net.lexical_strength:.0f}. Raising Lambda alone moves this shift")
    print("  AWAY from the criterion. At the same Lambda the delta-like row reads "
          f"{strong_rows['delta (all)']['utterances']['some']['shift']:+.4f}, so between")
    print("  those two rows the difference is the prior's (Text cell 4 Part C).")
    crossed = [name for name, entry in strong_rows.items() if name in rows
               and rows[name]["utterances"]["some"]["shift"] >= 0.0
               > entry["utterances"]["some"]["shift"]]
    print("  Raising Lambda alone carries the shift for \"some\" below zero under: "
          + (", ".join(crossed) if crossed else "no prior") + ".")
    print()'''),
("    raised_lambda_control(net, base_rows)\n",
 "    raised_lambda_control(net, base_rows, rows)\n"),
]
patch(main.cells[9], code_pairs)
patch(appx.cells[4], code_pairs)
assert appx.cells[4].source.split("\n", 5)[5] == main.cells[9].source   # E2b = header + 2b

# ------------------------------------------------------------------ Appendix E
patch(appx.cells[1], [(
r"""under the other priors of Part D it is $7.06\times10^{-9}$ (flat), $1.18\times10^{-3}$
($\mathrm{Beta}(1,3)$), $8.26\times10^{-5}$ ($\mathrm{Beta}(3,1)$) and $1.26\times10^{-7}$ (delta-like),
as Code Cell E4 prints:""",
r"""under the other priors of Part D it is $7.06\times10^{-9}$ (flat), $1.18\times10^{-3}$
($\mathrm{Beta}(1,3)$) and $8.26\times10^{-5}$ ($\mathrm{Beta}(3,1)$), and $1.26\times10^{-7}$ under
the delta-like prior of Text cell 4b, as Code Cell E4 prints:""")])
patch(appx.cells[8], [(
r"""cells 4, 5 and 6 and every number in Code cells 9 and 10. Code Cell E3 checks the last of these""",
r"""cells 4, 4b, 5 and 6, and every number in Code Cells 2 and 2b. Code Cell E3 checks the last of these""")])

nbformat.write(main, ROOT / "main.ipynb")
nbformat.write(appx, ROOT / "appendix_E.ipynb")
print("patched: main.ipynb and appendix_E.ipynb")

# ------------------------------------------------------------------ number check
outputs = ""
for nb in (main, appx):
    for c in nb.cells:
        if c.cell_type == "code":
            outputs += "".join(o.get("text", "") for o in c.get("outputs", []) if o.get("output_type") == "stream")
outputs += (pathlib.Path(__file__).parent / "test_out_2b.txt").read_text()   # 2b's pending print change
prose = "\n".join(t for t in new_texts if not t.startswith(("def ", "          f", "    raised")))
missing = set()
for mant, exp in re.findall(r"(\d+\.\d+)\\times10\^\{(-?\d+)\}", prose):
    token = f"{mant}e{int(exp):+03d}"
    if token not in outputs:
        missing.add(token)
plain = re.sub(r"\d+\.\d+\\times10\^\{-?\d+\}", "", prose)
for token in re.findall(r"\d+\.\d+", plain):
    if token not in outputs:
        missing.add(token)
print("decimals in the new prose not found in any stored output:", sorted(missing))
