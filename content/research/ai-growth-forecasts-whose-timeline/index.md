---
title: "AI Growth Forecasts - Whose Timeline"
short_version: |
  Adam's instinct is right: most of this conversation is a timeline argument wearing a theory costume. The useful thing is that the positions can be reduced to a single number — how many percentage points AI adds to annual productivity growth — and then compounded. Do that and the disagreement becomes legible. Acemoglu's published estimate adds about **$180 billion** to US GDP over a decade. Cowen's casual floor adds about **$1.8 trillion** — ten times more, and he calls it modest. Goldman Sachs adds **$5.7 trillion**. The explosive-growth scenarios add **$57 trillion**. These are not different opinions about the same forecast. They are different universes, and the gap between the two men in this room is smaller than the gap between either of them and the industry.
asked: "A good amount of this conversation is economists arguing over timelines… I would love to see a rabbit hole around timelines for some of these arguments. What I mean is like a timeline understanding what game-changer means over time. What does GDP growth look like with an OpenAI assumption versus Acemoglu assumption for example."
transcript_anchor: "a16"
models: ["Claude"]
draft: false
---

**Adam asked:** *"A good amount of this conversation is economists arguing over timelines… I would love to see a rabbit hole around timelines for some of these arguments. What I mean is like a timeline understanding what game-changer means over time. What does GDP growth look like with an OpenAI assumption versus Acemoglu assumption for example."*

---

## The scenarios, compounded

US GDP ≈ **$30 trillion** (2026, approximate). Baseline real growth assumed at **2.0%/yr**. Ten years, 2026 → 2036.

| Scenario | AI adds to annual growth | Growth rate | GDP in 2036 | Extra vs. baseline |
|---|---|---|---|---|
| **Baseline** — no AI effect | — | 2.00% | $36.6T | — |
| **Acemoglu (2024)** | +0.05 pp | 2.05% | $36.8T | **+$0.18T** |
| **Cowen's floor** ("half a percentage point") | +0.5 pp | 2.50% | $38.4T | **+$1.8T** |
| **Goldman Sachs (2023)** | +1.5 pp | 3.50% | $42.3T | **+$5.8T** |
| **Explosive growth** (transformative-AI literature) | +10 pp | 12.00% | $93.2T | **+$56.6T** |

*Arithmetic is mine and simple — constant growth rates compounded over ten years. It is a way of making the assumptions comparable, not a forecast. See working notes for what it hides.*

The ratio worth staring at: **Cowen's "modest, easily imaginable" number is ten times Acemoglu's published estimate.** When Cowen says "I would be shocked if what we have now didn't do at least as much for us" as the 1995–98 IT boom, he is proposing something Acemoglu's model treats as far out of range. And Acemoglu's reply is not a rebuttal — it is *"I think that would be an amazing thing. Our society would be so much better. I wish it were."*

## Where Acemoglu's number comes from

["The Simple Macroeconomics of AI"](https://www.nber.org/papers/w32487) (NBER w32487, 2024) does not forecast in the industry sense. It applies **Hulten's theorem**: the aggregate productivity gain equals the fraction of tasks affected × the average cost saving on those tasks. Feed in the published task-exposure estimates and out comes a small number.

| Quantity | Estimate | Per year |
|---|---|---|
| TFP gain over 10 years | **0.53% – 0.66%** | ~0.05–0.07% |
| GDP gain over 10 years | **~0.9% – 1.1%** | ~0.09–0.11% |

The paper's own hedge is important and Acemoglu repeats it on air: early task-level evidence comes from **easy-to-learn tasks**, so extrapolating it to hard tasks probably *overstates* the gain. That is why he lands at the low end.

**What he now concedes.** Asked directly whether he'd revise: *"Yes. If I were writing that today, I would revise my estimates, but the general point remains."* He separates the paper into three claims and updates only one:

1. The *framework* — gains come from new things plus cost savings. **Unchanged.**
2. The *numbers*. **Revised up** — models advanced faster than he expected.
3. The *rhetorical point* — industry estimates need grounding. **Unchanged.**

And he adds a genuine counterweight: applications built on the models "have been developing pretty sluggishly." His revision is up on capability, down on diffusion.

## What "game-changer" means — the definitional problem

Adam asked for this specifically, and it turns out to be where the argument actually lives. There is no shared threshold:

| Standard | Rough threshold | Who uses it |
|---|---|---|
| **Statistically visible** | +0.2 pp/yr | Economists; enough to detect in the data |
| **Historically normal boom** | +0.5 pp/yr | Cowen's benchmark, from IT 1995–98 |
| **Comparable to electrification** | +1.0–1.5 pp/yr sustained | Goldman; the "general purpose technology" case |
| **Regime change** | +5 pp/yr or more | Transformative-AI literature |
| **Acemoglu's actual position** | ~+0.1 pp/yr, arriving lumpy | This paper |

Note the last row carefully. Acemoglu does **not** predict a smooth trickle. His stated expectation is *"there will be one or two years of very rapid growth"* inside an otherwise ordinary decade. His model of the 1980–2008 period is the template: unimpressive on average, with bursts inside it.

This is why the two men talk past each other on timing. Cowen points at 1995–98 and says *look how fast it moved*. Acemoglu points at 1975–2008 and says *that boom took twenty years of prior investment to arrive*. **Both are describing the same history with different window sizes.** Neither is wrong about the data.

```mermaid
timeline
    title Whose clock is running?
    1975-1995 : Two decades of IT investment : Little measured productivity gain : "Computers everywhere but in the statistics"
    1995-1998 : The boom : Productivity growth up ~0.5 pp : Cowen's benchmark
    2004-2019 : Productivity slowdown : Despite continued IT investment
    2022-2026 : LLM capability rises fast : Application layer lags : Acemoglu's "sluggish diffusion"
    2026-2036 : The disputed decade : Acemoglu +0.05pp : Cowen +0.5pp : Industry +1.5pp or more
```

## The Solow paradox, which is the real precedent

Robert Solow, 1987: *"You can see the computer age everywhere but in the productivity statistics."* He was right for about eight more years, and then he was wrong. The productivity gain showed up in the late 1990s.

That episode is the single most useful precedent, and it cuts **both ways**:

- **For Cowen:** measured productivity lags real capability. Absence of evidence now is not evidence of absence.
- **For Acemoglu:** the lag was *twenty years*, and the eventual boom was +0.5 pp for a few years — not a regime change. If AI follows the IT template exactly, the industry forecasts are still wrong by an order of magnitude.

## Reading

- Acemoglu, ["The Simple Macroeconomics of AI"](https://www.nber.org/papers/w32487) (2024) — the source of the low number
- Briggs & Kodnani, "The Potentially Large Effects of AI on Economic Growth," Goldman Sachs (2023) — the +1.5 pp case
- Brynjolfsson, Rock & Syverson, "The Productivity J-Curve" (2021) — why gains lag investment; the best formal statement of the Solow-paradox mechanism
- Aghion, Jones & Jones, "Artificial Intelligence and Economic Growth" (2019) — the theoretical route to explosive growth
- Autor, ["The Work of the Future"](https://mitpress.mit.edu/9780262547307/the-work-of-the-future/) — the measured middle

---

## Working notes

**What the table hides, and it matters.** Constant compounding is the wrong shape for what anyone actually believes. Acemoglu explicitly predicts lumpiness — a couple of fast years inside a slow decade — and the transformative-AI scenarios are *accelerating*, not constant. A more honest version plots cumulative GDP paths with different curvature rather than five straight lines. **That's a real chart and I'd build it in draft 2 if you want it.** The numbers above are right for the assumptions stated and should be read as "what does each position imply if you take it literally and hold it fixed" — nothing more.

**Sourcing.** The Acemoglu figures are from the published paper and are solid. The $30T US GDP base is approximate and rounded. The Goldman +1.5 pp and the explosive-growth +10 pp are **stylized representatives of a range**, not quotations — Goldman's headline was a 7% global GDP uplift over a decade, which I've converted to a US annual-growth equivalent, and that conversion is mine. Do not attribute the +1.5 pp to Goldman as a direct quote without checking their report.

**The 2026 update problem.** Cowen's framing — "Anthropic is a trillion-dollar company, revenue through the ceiling" — is doing rhetorical work that the economics doesn't support. Firm valuation is not productivity. A company can be worth a trillion dollars by capturing existing surplus rather than creating new output, which is precisely the distinction Acemoglu's whole framework is built on. **Neither man says this out loud** and it's arguably the biggest unexamined move in the segment.

**Draft 2 should add:** actual measured US TFP growth 2022–2026 as a scoreboard row. If AI were already producing Goldman-scale gains we would be starting to see it. That is a checkable fact and it would date-stamp the argument rather than leaving it hypothetical.

**Related:** [[Acemoglu and Restrepo - The Task Framework]] · [[Automation and the Labor Share]] · [[Pro-Worker AI]]
