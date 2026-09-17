---
title: "Automation and the Labor Share"
description: "Acemoglu's claim isn't mass unemployment. Automation moves displaced workers into lower-paid work and shrinks labor's share of income."
short_version: |
  Adam's reading is correct. Acemoglu is *not* claiming automation causes mass unemployment. He is claiming displaced workers land in other work at lower pay, and that the pie slice going to workers as a whole shrinks and does not come back. "First-order impact" is the technical way of saying: *the direct effect, before any offsetting reaction.* When a task moves from a person to a machine, labor's share of income falls by arithmetic. The offsetting channels — cheaper output and expanded demand for the tasks people still do, and wholly new tasks — are real and operate alongside it rather than in a later stage; his claim is that they do not add up to enough to undo it.
asked: "This might be too much to ask, but I'd really like to go down a rabbit hole on this. I'd love to see some chart showing this. If I understand what he's saying it's that people might get another job, but it's not as well paid. I'd love some references on that. Also, the 'first-order impact' is something I'd like to be explained more as well. What is he describing when he's saying that."
transcript_anchor: "a12"
models: ["Claude", "Codex"]
draft: false
---

**Adam asked:** *"This might be too much to ask, but I'd really like to go down a rabbit hole on this. I'd love to see some chart showing this. If I understand what he's saying it's that people might get another job, but it's not as well paid. I'd love some references on that. Also, the 'first-order impact' is something I'd like to be explained more as well. What is he describing when he's saying that."*

---

## What "first-order impact" means

"First order" names the *direct* effect: what follows by arithmetic when a task moves from labor to capital, before anything else adjusts. It is not stage one of a sequence in time. The other channels are not "higher orders" that arrive later — they can operate at the same time, and new-task creation has direct effects of its own.

**The labor share** is compensation to workers divided by total output. Suppose a factory produces $100 of output, pays $60 in wages and $40 to capital. Labor share is 60%.

Now automate a task that had been done by a worker earning $10.

- **Direct displacement** — the *displacement effect* in Acemoglu and Restrepo's terms. That $10 moves from the wage bill to the capital bill: $50 of $100 → labor share 50%. This is what Acemoglu means by *"That has a first-order impact on the labor share because fewer things are done by labor."* It is not a prediction; it is what the arithmetic gives you under the assumptions below.
- **Productivity response** — production is cheaper, so output can expand and demand rises for the tasks people still do. Some of the $10 comes back.
- **New-task creation** — the *reinstatement effect*: new products and new tasks appear where labor has the comparative advantage. More comes back, and this channel raises labor demand in its own right rather than only as an echo of the first.

⚠ **The fixed $100 is an assumption, not a proof.** Holding output constant is exactly what makes the first line pure arithmetic — and it is the assumption the other two channels break. The example shows what *first-order* means; it cannot establish that the labor share ends lower. That is an empirical claim, and it rests on the evidence below rather than on this bookkeeping. The [task-framework diagram](/research/acemoglu-and-restrepo-the-task-framework/) sets out the same three forces acting together, with the outcome depending on their relative strength rather than on moving from one box to the next.

His claim, in one sentence: *"there could be enough demand from nonautomated tasks for labor, but that would never come back to increase the wage enough to restore the labor share to where it is."* The offsetting channels are real; his claim is that they are not complete.

## Your reading, checked: do displaced workers earn less?

Yes — this is one of the better-established findings in labor economics, and it predates the automation debate.

| Finding | Magnitude | Source |
|---|---|---|
| Displaced workers' long-run earnings loss (high-tenure, mass layoff) | **~15–20% below** pre-displacement trajectory, persisting 15–20 years | Jacobson, LaLonde & Sullivan (1993); Davis & von Wachter (2011) |
| Robot exposure: local labor market effect | **−0.2 pp** employment-to-population, **−0.42%** wages per robot/1,000 workers | [Acemoglu & Restrepo, *JPE* 2020](https://www.journals.uchicago.edu/doi/abs/10.1086/705716) |
| Share of 1980–2016 US wage-structure change attributable to task displacement | **50–70%** | [Acemoglu & Restrepo, *Econometrica* 2022](https://economics.mit.edu/sites/default/files/2022-10/Tasks%20Automation%20and%20the%20Rise%20in%20US%20Wage%20Inequality.pdf) |
| Trade-displaced manufacturing workers (comparison case) | Persistent earnings losses, low reallocation out of affected areas | Autor, Dorn & Hanson, "The China Shock" (2013) |

The mechanism is specificity: a welder's wage reflected skill in welding. Remove welding and the general labor market does not value that history. The worker is re-employed — often quickly — at a wage set by whatever they can do next.

**Acemoglu's precise version in this conversation:** *"the wages of people who used to be in especially blue-collar heavy manual tasks that were the ones that robots of the 1990s and 2000s went after, like welding and painting… went down quite a bit"* — both in aggregate and in local labor markets.

## The chart you asked for — and why it is a fight, not a line

Here is the US labor share, nonfarm business sector. **Read the caveat below before using these numbers.**

| Period | Labor share (approx.) |
|---|---|
| 1947 Q1 | 65.8% |
| Late 1940s – early 2000s | ~63%, fluctuating, no trend |
| 2000 Q4 | 62.8% |
| 2005 | falls below 60% |
| 2011 Q4 | 56.0% (trough) |
| 2013 | ~56.7% |

*Source: BLS nonfarm business sector labor share, as reported in [BLS TED](https://www.bls.gov/opub/ted/2017/labor-share-of-output-has-declined-since-1947.htm) and the [FRBSF working paper](https://www.frbsf.org/wp-content/uploads/wp2013-27.pdf).*

**The caveat is the substance.** Cowen says "62 to 60"; the BLS headline series says roughly 66 to 57. Both are defensible, because the labor share is one of the most measurement-sensitive statistics in economics:

- **Proprietors' income.** A sole proprietor's income is part wage, part profit, and the split is a modeling assumption. Elsby, Hobijn & Şahin (2013) find **one-third of the measured BLS decline** comes from how this is handled.
- **Equity compensation.** Cowen's adjustment. Stock grants to employees are labor income economically but land oddly in the accounts. Including them raises the recent labor share materially.
- **Housing and depreciation.** Imputed rent on owner-occupied housing is all "capital." Rognlie (2015) showed much of the apparent capital-share rise is housing, not robots.
- **Sector vs. aggregate.** Acemoglu's claim is explicitly at the firm and sector level, where he says evidence and theory "are very well aligned." He concedes the macro series is contaminated: *"those are macro things"*, and there are *"composition effects between like Walmart effects."*

So the honest framing is: **Cowen and Acemoglu are not disagreeing about a number. They are disagreeing about which number is the right question.** Cowen points at an aggregate that barely moved and says the worry is overblown. Acemoglu says the aggregate bundles automation with new-task creation and therefore cannot test his claim, which is about automation held separately.

{{< research-figure "labor-share" >}}

## From the book — which series Acemoglu himself uses

The measurement fight above has an obvious tie-breaker that draft 1 did not reach for: **what number does Acemoglu print when he is not being interviewed?** Chapter 6 of *What Happened to Liberal Democracy?* answers it, and the answer is neither the BLS headline nor Cowen's.

> *"In 1980, the share of labour in US national income was 58%, with the rest going to capital. Since then, the national share of labour has fallen to 52%, and the share of capital has [risen]."*

**58 → 52, on national income, from 1980.** Six points, not the nine the BLS nonfarm series implies over its longer window, and not the two Cowen offers. Three things follow:

- **Cowen's "62 to 60" is not a straw man of Acemoglu's position, but it is not Acemoglu's number either.** The gap between them is 6 points against 2 — a real disagreement about magnitude, on top of the disagreement about which question the aggregate answers.
- **The start date is doing work.** Acemoglu begins at 1980, not 1947, which excludes the flat postwar stretch and starts the clock at the moment his own account says the industrial compact broke. That is a defensible choice and it is also an argumentative one — the same kind of endpoint choice flagged on [The Printing Press - How Long Was the Adjustment](/research/the-printing-press-how-long-was-the-adjustment/).
- **National income, not nonfarm business.** A different denominator again, which is exactly why the table above needs its caveat.

**The number he actually leans on is sectoral, and it is much larger:**

> *"The labour share in value added in the manufacturing sector declined from 74% in 1981 to 46% in the mid-2010s, much larger than the decline in the aggregate economy that I mentioned previously, which was from 58% to 52%."*

**74 → 46 in manufacturing.** He then decomposes it in the direction his framework predicts: *"While some manufacturing industries, such as apparel, had stable labour shares, the industries that were at the forefront of new robot installations, such as motor vehicles, chemical products, electrical equipment, and primary and fabricated metals, had sharper drops in their labour share and also cut down employment."*

That is the whole Cowen–Acemoglu exchange in miniature, and it clarifies who is arguing what. **Acemoglu is not defending the aggregate series.** He publishes it, calls it small, and then goes immediately to the sector where the effect is four times larger and where robot adoption and labor-share decline line up industry by industry. Cowen's move — point at the aggregate, note it barely moved — lands on a number Acemoglu has already conceded is not the one carrying his argument.

**For the chart.** This resolves the "which series" decision the working notes below hand back to Adam, at least for panel 1: if the page is about *Acemoglu's* claim, the honest series is the manufacturing labor share in value added, with the aggregate plotted beneath it for scale. That is two lines from published sources, it shows exactly why the two men are talking past each other, and it does not require anyone's replication files.

## Reading

- Acemoglu & Restrepo, ["Automation and New Tasks"](https://www.aeaweb.org/articles?id=10.1257/jep.33.2.3), *JEP* 2019 — the accessible statement
- Acemoglu & Restrepo, ["Robots and Jobs"](https://www.journals.uchicago.edu/doi/abs/10.1086/705716), *JPE* 2020 — the empirics
- Elsby, Hobijn & Şahin, ["The Decline of the U.S. Labor Share"](https://www.brookings.edu/bpea-articles/the-decline-of-the-u-s-labor-share/), *BPEA* 2013 — why the measurement fight is real
- Autor, ["The Work of the Future"](https://mitpress.mit.edu/9780262547307/the-work-of-the-future/) — the new-tasks accounting Acemoglu defers to
- Jacobson, LaLonde & Sullivan (1993), "Earnings Losses of Displaced Workers," *AER* — the origin of the scarring literature

---

## Working notes

**On the chart.** What Adam actually wants is a two-panel figure: labor share over time on top, and below it the wage path of workers in heavily-automated occupations versus everyone else. **Panel 1 I can source. Panel 2 does not exist as a clean public series** — it has to be constructed from the *Econometrica* paper's occupation-group decomposition, which means pulling their replication files. That is a real task, not a lookup. Flagging it rather than faking it.

The table above is the honest first draft: numbers with provenance, and the reason a single line would be misleading. If you want a rendered chart in draft 2, the decision to make is **which series** — and that decision is the argument, so it should be yours, not mine.

**Numbers I'd want double-checked before publication:** the 1947 Q1 65.8% and 2000 Q4 62.8% figures come through secondary sources quoting BLS, not from BLS directly. The Elsby/Hobijn/Şahin one-third result is from their abstract.

**What I could not resolve:** Cowen's "62 to 60, adjusting for equity compensation." I could not find the specific series he's using. It is plausibly Barkai (2020) or a Mercatus-adjacent calculation. Until that's identified, treat the 62→60 as a claim in an argument rather than a fact. **Still unresolved** — the book check settles what Acemoglu's number is, not what Cowen's is.

**What the book did settle:** which series Acemoglu himself publishes (58→52 on national income since 1980, and 74→46 in manufacturing value added since 1981), and therefore which line panel 1 of the chart should be. Written up above. It also means the "62 to 60" exchange is not two people disputing a measurement — it is Cowen testing an aggregate that Acemoglu's own book already sets aside as too small to carry the argument.

**Source and its limits.** Checked against the audiobook edition (Penguin Random House Audio, narrated by John Lee), machine-transcribed, so references are by chapter and the figures above are machine-transcribed numbers. **Confirm 74/46/58/52 against print before publication** — a transcript is exactly the wrong place to source a number to the percentage point, and these four are now load-bearing on this page.

**Related:** [Acemoglu and Restrepo - The Task Framework](/research/acemoglu-and-restrepo-the-task-framework/) · [AI Growth Forecasts - Whose Timeline](/research/ai-growth-forecasts-whose-timeline/)
