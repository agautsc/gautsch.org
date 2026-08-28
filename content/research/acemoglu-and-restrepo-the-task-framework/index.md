---
title: "Acemoglu and Restrepo - The Task Framework"
short_version: |
  Most economics treats technology as one thing that makes labor more productive. Acemoglu and Restrepo broke it into two opposing forces. **Automation** takes tasks away from workers and gives them to machines, which pushes wages and labor's share of income down. **New task creation** invents work that did not exist, which pushes them back up. Neither is guaranteed to dominate. That is the whole argument, and once you have it, "is technology good for workers?" stops being answerable in general and becomes a question about the *mix* in a particular period. This is the machinery running underneath every automation exchange in the conversation.
asked: "I'd love a rabbit hole specifically explaining the Acemoglu and Restrepo papers. What is the general thesis of these works. Provide some historic context towards the importance of them in economic thought and how have they evolved. They seem to be important to understanding this conversation.'* — and separately, *'Can you summarize and link to those papers"
transcript_anchor: "a11"
models: ["Claude"]
draft: false
---

**Adam asked:** *"I'd love a rabbit hole specifically explaining the Acemoglu and Restrepo papers. What is the general thesis of these works. Provide some historic context towards the importance of them in economic thought and how have they evolved. They seem to be important to understanding this conversation."* — and separately, *"Can you summarize and link to those papers"*

---

## The problem they were solving

Before this work, the dominant model was **skill-biased technical change** (SBTC). Technology raises the productivity of skilled workers more than unskilled ones; inequality rises because the skill premium rises; everyone's wages still rise, just unevenly. It fit the 1980s well.

It fit the 2000s badly. Real wages for non-college men fell. Employment polarized — growth at the top and bottom, hollowing in the middle. SBTC has no mechanism for a group's wages going *down* in absolute terms, because in that model technology always raises the marginal product of labor.

The task framework's core move: **technology does not augment workers, it reallocates tasks.** If a task moves from labor to capital, the workers who specialized in it lose the task itself — not merely relative standing. Their wages can fall absolutely. That is the thing SBTC could not produce and the data demanded.

## The three effects

```mermaid
flowchart TD
    A[New technology] --> B[Displacement effect<br/>tasks move from labor to capital]
    A --> C[Productivity effect<br/>output cheaper, demand for labor rises<br/>in remaining tasks]
    A --> D[Reinstatement effect<br/>new tasks created where<br/>labor has comparative advantage]
    B --> E{Net effect on<br/>wages and labor share}
    C --> E
    D --> E
    E --> F[Shared prosperity<br/>reinstatement keeps pace]
    E --> G[So-so automation<br/>displacement without much<br/>productivity gain or new tasks]
    style B fill:#c94f4f,color:#fff
    style D fill:#2f7d5f,color:#fff
    style G fill:#c94f4f,color:#fff
    style F fill:#2f7d5f,color:#fff
```

**"So-so automation"** is their term for the worst case and it is the key concept for the AI argument: technology just good enough to replace a worker, not good enough to generate much productivity gain. Self-checkout is the standard example. You get displacement with a small productivity effect and no new tasks — the mix Acemoglu fears AI is producing.

## The papers, in order

| Year | Paper | What it added |
|---|---|---|
| 2011 | Acemoglu & Autor, ["Skills, Tasks and Technologies"](https://economics.mit.edu/sites/default/files/publications/Skills%2C%20Tasks%20and%20Technologies%20-%20Implications%20for%20E.pdf) (*Handbook of Labor Economics*) | The framework itself. Tasks, not skills, are the unit. |
| 2018 | ["The Race Between Man and Machine"](https://www.aeaweb.org/articles?id=10.1257/aer.20160696) (*AER* 108:6) | The formal model. Automation vs. new tasks as a race; a balanced-growth path exists only if they stay in step. |
| 2019 | ["Automation and New Tasks"](https://www.aeaweb.org/articles?id=10.1257/jep.33.2.3) (*JEP* 33:2) | The readable one. **Start here if you read only one.** |
| 2020 | ["Robots and Jobs: Evidence from US Labor Markets"](https://www.journals.uchicago.edu/doi/abs/10.1086/705716) (*JPE* 128:6) | The empirical anchor. See numbers below. |
| 2022 | ["Tasks, Automation, and the Rise in US Wage Inequality"](https://economics.mit.edu/sites/default/files/2022-10/Tasks%20Automation%20and%20the%20Rise%20in%20US%20Wage%20Inequality.pdf) (*Econometrica* 90:5) | Attributes 50–70% of the change in US wage structure 1980–2016 to task displacement |
| 2022 | ["Demographics and Automation"](https://www.nber.org/papers/w24421) (*ReStud*) | The flip side: aging *causes* automation, and that's fine |
| 2024 | ["The Simple Macroeconomics of AI"](https://www.nber.org/papers/w32487) | Applies the framework to AI → see [[AI Growth Forecasts - Whose Timeline]] |
| 2026 | Acemoglu, Autor, Beirne & Scott, ["Baby Busts and Growth Booms"](https://www.nber.org/papers/w35401) | The optimistic turn Cowen presses him on |

### The robots number

The headline result from the 2020 *JPE* paper, using variation in robot adoption across US commuting zones 1990–2007:

> **One additional robot per thousand workers reduces the employment-to-population ratio by about 0.2 percentage points and wages by about 0.42%.**

Reported ranges across specifications: **−0.18 to −0.34 pp** on employment, **−0.25% to −0.5%** on wages. The identification rests on areas most exposed to robots after 1990 showing no differential trend before 1990.

## How the position evolved

This is the part worth noticing, because it is not a straight line.

1. **2011–2018 — building the machine.** Establish that tasks are the right unit and that displacement is real.
2. **2018–2022 — the pessimistic empirical phase.** Robots lower wages. Task displacement explains most of rising inequality. This is the Acemoglu most people know.
3. **2022 onward — the conditional turn.** *Demographics and Automation* shows automation triggered by labor scarcity is good. The 2026 *Baby Busts* paper finds falling birth rates associated with **higher** GDP growth per working-age adult, via labor-saving innovation. Cowen catches this and asks whether it contradicts the Restrepo work. Acemoglu says no, and he is right: both use the same framework. The framework was always conditional. **Automation responding to scarcity is a different animal from automation replacing available workers.**

That is why he can say "I am not, 100 percent not, against automation" without contradiction, and why he sounds pessimistic anyway. The model is neutral. His read of *current conditions* is not.

## Where Cowen attacks

Cowen's move in this conversation is to grant the micro and deny the macro: fine at the firm and sector level, but the aggregate labor share barely moved — "62 to 60" adjusting for equity compensation — and automation since the Industrial Revolution has plainly made workers richer. Acemoglu's reply is that the macro series is not a test of automation because it bundles automation with everything else, including new task creation, which he estimates accounts for **40–50%** of what the US labor market currently supports. Full treatment in [[Automation and the Labor Share]].

---

## Working notes

**Confidence.** The framework, the paper list, and the robots coefficients are solid and checkable. The 50–70% figure is from the *Econometrica* abstract. The 40–50% new-tasks figure is Acemoglu's spoken number in this interview, attributed partly to Autor's [*The Work of the Future*](https://mitpress.mit.edu/9780262547307/the-work-of-the-future/) — I have **not** verified it against a printed source and it should not be quoted as precise.

**⚠ Unverified: the Barany, Patel and Siegel paper.** Cowen cites [CEPR DP21700](https://cepr.org/publications/dp21700) on France through 2019 finding no labor-share harm. CEPR blocks automated fetching (HTTP 403) and the paper does not surface in search. There *is* a related January 2026 paper by Aseem Patel, ["Labour Market Power and Automation"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6075686), using French administrative data — **not the same paper**, and I should not pretend it is. Someone with CEPR access should pull DP21700 and check what it actually claims. Acemoglu's on-air response was "I don't know this new paper," so the exchange is unresolved on both sides.

**The most useful unasked question:** the framework says the automation/new-task mix is a *choice*, and Acemoglu gives a concrete example — Japanese, Korean and German carmakers redesigning jobs around robots while American firms did not. That example is doing enormous work in his argument and I have not verified it. If it holds up it is the strongest empirical support for the "choice" claim in the whole conversation. **Worth its own page in draft 2.**

**Related:** [[Automation and the Labor Share]] · [[AI Growth Forecasts - Whose Timeline]] · [[Induced Innovation and the Habakkuk Thesis]] · [[King and Plosser - Real Business Cycles]]
