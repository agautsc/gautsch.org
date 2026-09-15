---
title: "AI Growth Forecasts - Whose Timeline"
short_version: |
  The disagreement is about size, timing, and what is being measured. Acemoglu's 2024 paper estimates ten-year gains in total-factor productivity and GDP. Cowen offers a half-point productivity-growth benchmark without a fixed horizon; Goldman's productivity estimate and global GDP headline measure different things again. They cannot be ranked by compounding all the numbers as annual US GDP growth. The source table separates those claims, and a clearly labeled arithmetic example shows how assumed GDP growth compounds.
asked: "A good amount of this conversation is economists arguing over timelines… I would love to see a rabbit hole around timelines for some of these arguments. What I mean is like a timeline understanding what game-changer means over time. What does GDP growth look like with an OpenAI assumption versus Acemoglu assumption for example."
transcript_anchor: "a16"
models: ["Claude", "Codex"]
draft: false
---

<!-- reader-review: 2026-09-15 -->

## What the sources actually measure

**A level gain is not an annual growth rate.** A 1% GDP gain after ten years means output in year ten is 1% above the counterfactual level. It does not mean an extra percentage point of growth every year, or the sum of additional output across the decade. **Total-factor productivity (TFP)** concerns output relative to combined inputs; labor productivity concerns output per worker or hour. Investment and labor supply affect how those gains translate into GDP.

| Source | Measure and geography | Estimate | Horizon and assumptions |
|---|---|---|---|
| Acemoglu, 2024 published paper | US TFP level | At most 0.66%; below 0.53% with the harder-task adjustment | Ten years from the 2024 exercise; task exposure and cost savings |
| Same paper, section 3.4 | US GDP level | 0.93–1.16% above baseline | Ten years, with its baseline investment response |
| Same paper, larger investment response | US GDP level | 1.4–1.56% above baseline | Alternative capital-accumulation assumptions, not a new annual rate |
| Cowen, episode 286 | Productivity growth; precise measure unspecified in this exchange | Half a percentage point | IT-boom analogy; no fixed ten-year projection |
| Goldman Sachs, April/June 2023 | Global GDP level; separately, productivity growth | About 7% global GDP; +1.5 percentage points per year in productivity | Adoption over ten years; these are separate measures, not interchangeable US GDP rates |

Sources: [Acemoglu's published paper, pp. 34, 38–39 and 42](https://economics.mit.edu/sites/default/files/2024-10/The%20Simple%20Macroeconomics%20of%20AI.pdf); [Cowen's conversation](https://conversationswithtyler.com/episodes/daron-acemoglu-2/); [Goldman's April account](https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent) and [June clarification](https://www.goldmansachs.com/insights/articles/how-much-could-ai-boost-us-stocks).

**The correction:** the earlier table used a roughly annualized TFP estimate as an annual GDP-growth increment. It also treated productivity benchmarks as GDP forecasts. That does not support either the $180 billion headline or the claim that Cowen's estimate is ten times Acemoglu's. Both are withdrawn.

**Versions matter.** The figures above use the published 2024 paper, rather than mixing its estimates with the April working draft. In the interview Acemoglu says he would raise the numerical estimates, but supplies no replacement number. The table records the 2024 exercise, not a quantified 2026 forecast.

## The scenarios, compounded

To see what sustained growth would mean, separate the arithmetic from the attribution. Suppose an **imaginary economy starts at $30 trillion**, in fixed purchasing-power units, and grows at 2% annually for ten years. This is a round input, not a measured 2026 US GDP value.

{{< growth-scenarios >}}

These increments are **chosen examples**, not forecasts attributed to Acemoglu, Cowen, Goldman, or an AI company. In particular, +1.5 percentage points of productivity growth is not automatically +1.5 percentage points of total GDP growth.

For a cumulative GDP gain, the appropriate illustration is different: multiply the year-ten baseline by that gain. For example, a hypothetical **1% endpoint uplift** on $36.57 trillion is about **$0.37 trillion extra output in year ten**. It is not $0.37 trillion accumulated over all ten years. The distribution of gains within the decade would be needed to calculate that total.

## What counts as a game-changer?

There is no agreed numerical threshold in the exchange. Three questions help expose the disagreement:

- **Size:** how much more output, and measured in which units?
- **Timing:** a temporary acceleration, a delayed level shift, or persistently faster growth?
- **Distribution:** higher aggregate output for whom, with what changes to working lives?

The IT analogy can support both patience about adoption and caution about assuming a permanent boom. It does not by itself establish how fast AI will diffuse.

{{< research-figure "ai-clocks" >}}

## Reading

- [Acemoglu, *The Simple Macroeconomics of AI*, published 2024 version](https://economics.mit.edu/sites/default/files/2024-10/The%20Simple%20Macroeconomics%20of%20AI.pdf) — separate TFP and GDP calculations
- [Goldman Sachs, April 2023](https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent) — the global GDP headline
- [Goldman Sachs, June 2023](https://www.goldmansachs.com/insights/articles/how-much-could-ai-boost-us-stocks) — annual productivity wording
- [The original interview](https://conversationswithtyler.com/episodes/daron-acemoglu-2/) — Cowen's benchmark and Acemoglu's qualitative update

## From the book

*What Happened to Liberal Democracy?* takes the same position and **prints no number for it.** Chapter 9 states it in words:

> *"My reading of the evidence is that the benefits from AI-based automation in the medium term, though non-trivial, are not huge. The rollout of AI will be slow, as is the rollout of any technology that requires major organizational changes."*

The quantitative estimates come from the paper. The book's qualitative account does not validate a particular GDP conversion or a tenfold comparison.

**The distribution argument is the one the book actually cares about,** and it is where he spends his words:

> *"Even if such benefits were realized, how would they be distributed? The most natural path to broad-based benefits from productivity improvements would be via shared prosperity, working through higher wages for all sorts of work, and skills. This is what the Industrial Compact achieved until its unravelling in the early 1980s. But if all the gains are from automation, without the pro-worker AI possibilities I discuss below, then wage increases will not follow, and in fact, mass-scale automation could lead to significant joblessness."*

He then closes the obvious escape hatch — broad AI ownership, or universal basic income — on two grounds. Political economy: *"Large tech companies would not be enthusiastic about redistributing all of their profits to the broader population."* And, more interestingly, a social objection that has nothing to do with money: *"A society in which a large fraction of the population does not contribute to production or other beneficial activities would create huge social status gaps between the makers and the takers… Communities are most vibrant when their members feel they are contributing to society at large."*

**This adds a separate question:** who gains? A larger GDP estimate alone does not settle the distribution of wages, ownership, bargaining power, or opportunities to contribute. The growth arithmetic cannot rank these social outcomes.

**On the AGI question underneath the timelines**, the book is more explicit than the interview: *"A quick transition to AGI seems unlikely, in part because existing models still do not show evidence of true comprehension or deep understanding, even in simple contexts"* — the illustration being that a model can explain how to repair a garage door while having *"no recognition of the social context of this problem,"* and that *"as far as they are concerned, there is no difference between repairing a garage door, summarizing an ancient text, and diagnosing cancer."* Whether that is a claim about current systems or about the architecture is left open, which is the same ambiguity the interview leaves.


---

## Working notes

**September 15 correction.** Removed the unsupported GDP conversions and tenfold comparison. The illustrative table is generated from committed inputs in `data/research/growth_scenarios.json`; the short version also feeds the transcript popover. Reading packs are built from the same page.

**Remaining limits.** These source estimates are conditional exercises, not a common forecast. The paper's introduction rounds one adjusted GDP result differently from its section 3.4 calculation; the table identifies the section used. No numeric replacement is inferred from the interview's qualitative update. A forecast of explosive growth would require its own source, definition, and assumptions; the old arbitrary +10-point row is removed.

**Source and its limits.** The book material above retains the previous check against the audiobook edition, machine-transcribed. Chapter references and transcribed quotations still need confirmation against print before publication. This pass verifies the paper-based comparisons, not every book quotation.

**Related:** [Acemoglu and Restrepo - The Task Framework](/research/acemoglu-and-restrepo-the-task-framework/) · [Automation and the Labor Share](/research/automation-and-the-labor-share/) · [Pro-Worker AI](/research/pro-worker-ai/)
