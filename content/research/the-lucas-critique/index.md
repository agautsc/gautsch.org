---
title: "The Lucas Critique"
description: "The Lucas critique says estimated relationships can shift when policy and expectations change. Why Acemoglu's evidence from past labor shortages may not carry over."
short_version: |
  Robert Lucas's 1976 argument: relationships estimated from historical data reflect how people behaved *given the policy regime they expected*. Change the regime and expectations change, so behavior changes and the estimated relationship can shift — which means you cannot simply assume a correlation estimated under one policy will hold under another. It is not a claim that history teaches nothing; it is a demand to estimate what should stay fixed, such as preferences and technology, rather than relationships that depend on expectations. Applied here: Acemoglu found that past declines in young workers went with labor-saving innovation and higher growth. Cowen's objection is that **every one of those episodes was local and temporary, and the coming one is global, persistent and anticipated**. The anticipated, persistent part is a Lucas problem in the strict sense; the global part is a broader question of general-equilibrium effects and external validity. Either way, the historical relationship may not carry over.
asked: "Please explain what a Lucas critique objection to this would be. Start by explain the Lucas critique"
transcript_anchor: "a21"
models: ["Claude"]
draft: false
---

**Adam asked:** *"Please explain what a Lucas critique objection to this would be. Start by explain the Lucas critique"*

---

## The critique itself

Robert Lucas Jr., ["Econometric Policy Evaluation: A Critique"](https://www.sciencedirect.com/science/article/abs/pii/S0167223176800036) (1976). Nobel 1995, substantially for this.

The setting: 1960s macroeconomics had large statistical models fitted to historical data, used to answer questions like "what happens to unemployment if we accept 2% more inflation?" The Phillips curve seemed to give a stable menu.

Lucas's argument:

1. Those estimated relationships summarize how people behaved **given the policy regime they expected**.
2. People form expectations about policy and act on them.
3. Change the regime and expectations change, so behavior changes, so **the estimated relationship changes**.
4. Therefore using the old model to evaluate the new policy is invalid — the model's parameters are not policy-invariant.

The 1970s obliged by demonstrating it: exploit the Phillips curve deliberately, workers build inflation into wage demands, and you get stagflation — high inflation *and* high unemployment, which the old curve said was impossible.

The methodological consequence was enormous. It pushed macro toward "microfounded" models built on preferences and technology — things assumed to be deeper than policy — which is where DSGE modelling came from.

## The objection Cowen is making

The paper under discussion is [Acemoglu, Autor, Beirne & Scott, *Baby Busts and Growth Booms*](https://www.nber.org/papers/w35401) (NBER w35401, July 2026), which finds that falling birth rates are associated with **higher** GDP growth per working-age adult and higher wage growth, because technology responds to scarce young labor by becoming labor-saving. Identification comes partly from **World War II deaths** — historical variation in the size of younger cohorts.

Cowen's move:

> *"there's a lot of young labor missing after World War II, but right before us is this period of great population plenty, and to some extent, it's expected. No one thinks there'll be a 1.3 total fertility rate, whereas today, you have all these countries, some of them quite poor—Brazil, I think, is at 1.36 or so—and that just seems to be ongoing… Isn't there a Lucas critique objection to your lack of fear of the fertility crisis?"*

Unpacked, three distinct differences between the historical episodes and now:

| Historical episodes | The coming one |
|---|---|
| **Local** — one country loses young workers, others don't | **Global** — nearly every country except sub-Saharan Africa |
| **Temporary** — followed by a baby boom; everyone expected recovery | **Ongoing and expected to persist**, possibly to fall further |
| **Unanticipated** — a war shock | **Anticipated** — firms and governments can see it coming for decades |

Each breaks the extrapolation in its own way, and they are not all the same kind of problem:

- **Anticipated and persistent** (rows two and three) is the Lucas critique in its original sense. If firms, workers and governments see a lasting decline coming, investment and family behavior adjust in advance in ways the historical data never contained, so the estimated response was conditional on expectations that no longer hold.
- **Global** (row one) is a different problem: general equilibrium and external validity. If every country loses young workers at once there is no elsewhere to import labor or capital from, so a result estimated from one country's shock may not scale to the world. That would be true even if nobody's expectations changed.

Lucas's paper is about evaluating *policy* changes. Cowen borrows its name for the wider family, which is common usage and fair, but the distinction matters for what would answer him. A model built on parameters that do not shift with expectations answers the first problem. It does not by itself answer the second, which needs evidence or modelling of what happens when the shock is worldwide. Acemoglu's own concession, below, is mostly about the second.

## Acemoglu's answer — he concedes it

> *"Absolutely, 100 percent. Yes, that's a very good point. The last paragraph of that paper says that."*

He then lists the cases himself — China at a scale never seen, South Korea, Brazil, Turkey, Mexico, India — and grants that *"when the whole world goes through it… perhaps the general equilibrium, general world equilibrium effects are going to be different."*

His one counter is that another thing is changing simultaneously: people are living longer and healthier, so they can *"accumulate more and more relevant human capital throughout their lives."* Note that this is not a rebuttal — it is a second unmodelled change, which is arguably a *second* Lucas problem rather than an answer to the first.

**This is the most intellectually honest exchange in the interview.** Cowen finds the weak point of a paper Acemoglu just co-authored, and Acemoglu agrees without hedging and points at where he'd already written the caveat down.

## Reading
- Lucas, "Econometric Policy Evaluation: A Critique" (1976)
- Sargent & Wallace on policy ineffectiveness — the follow-on
- Acemoglu, Autor, Beirne & Scott, [*Baby Busts and Growth Booms*](https://www.nber.org/papers/w35401) — read the last paragraph, per his own pointer

---

## Working notes
**Corrected 2026-09-18.** The short version used to say the critique means "you cannot use historical correlations to predict what a genuinely new situation will do," and the body called Cowen's whole objection "a textbook Lucas critique." Lucas's argument is narrower — estimated relationships are not invariant to changes in policy regime and expectations — and part of Cowen's objection (global versus local) is a general-equilibrium and external-validity problem rather than an expectations one. Both are now separated. Checked against Lucas (1976) as cited above.

The framing of the three differences (local/global, temporary/permanent, unanticipated/anticipated) is my unpacking of a compressed question — Cowen gestures at all three but only states them loosely. I think it's a faithful expansion, but it's an expansion.

**Checked against the book: not there.** No Lucas critique, no rational-expectations discussion, no macroeconomic methodology at all. This exchange is two economists talking shop, and the book is not a macro book — its argument about technology runs through institutions and choices rather than through model stability. Nothing on this page needs revising against it, and nobody needs to search it again.

Checked against the audiobook edition (Penguin Random House Audio, narrated by John Lee), machine-transcribed; references are by chapter.

**Related:** [King and Plosser - Real Business Cycles](/research/king-and-plosser-real-business-cycles/) · [Induced Innovation and the Habakkuk Thesis](/research/induced-innovation-and-the-habakkuk-thesis/) · [Acemoglu and Restrepo - The Task Framework](/research/acemoglu-and-restrepo-the-task-framework/)
