---
title: "Education Quality and Economic Performance - The Outliers"
short_version: |
  There is a strong cross-country relationship between how much students actually *know* (test scores) and how fast an economy grows. Hanushek and Woessmann call this "knowledge capital," and their central finding is that once you use test scores instead of years of schooling, most famous puzzles stop being puzzles — the East Asian miracle and the Latin American growth disappointment both fall onto the line. The countries left off the line divide into two clean groups: **resource-rich states that out-earn their skills** (the Gulf), and **states whose skills cannot reach a market** — landlocked, blockaded, or badly governed. Armenia, which prompted the question, is the second kind, and it is close to the archetype.
asked: "What are the outliers for education to economic performance? Meaning what countries are under and over performing economically compared to the educational quality."
transcript_anchor: "a22"
models: ["Claude", "Codex"]
draft: false
---

**Adam asked:** *"What are the outliers for education to economic performance? Meaning what countries are under and over performing economically compared to the educational quality."*

---

## The finding to know first

Eric Hanushek and Ludger Woessmann, *[The Knowledge Capital of Nations](https://mitpress.mit.edu/9780262548953/the-knowledge-capital-of-nations/)* (MIT Press, 2015):

- Substitute **cognitive skills measured by international tests** (PISA, TIMSS) for **years of schooling**, and the fit to long-run growth improves dramatically.
- Years of schooling turns out to be a poor proxy. Two countries can each average 11 years and differ enormously in what students learn — Armenia is a case in point, see below.
- Their headline claim: the "Latin American growth puzzle" and the "East Asian miracle" both **dissolve** once you condition on skills. Neither was mysterious; both regions grew about as fast as their knowledge capital predicted.

That last point reframes Adam's question. The interesting outliers are not "who over- and under-performs" in general — most countries are near the line. The interesting outliers are the ones that **stay** off it after conditioning.

## The two kinds of outlier

{{< research-figure "education-outliers" >}}

**Over-performers — income above what skills predict**

| Type | Examples | Mechanism |
|---|---|---|
| Resource rents | Gulf states (Qatar, Kuwait, Saudi Arabia, UAE) | Oil and gas income is unrelated to the schooling system. Several score poorly on PISA relative to income. |
| Financial and legal entrepôts | Luxembourg, Switzerland, Singapore (partly) | Institutions and location capture returns beyond domestic human capital. Singapore also genuinely tops the tests. |
| Historical capital stock | Italy, parts of southern Europe | Accumulated wealth and industrial base sustain income as measured skills soften |

**Under-performers — income below what skills predict**

| Type | Examples | Mechanism |
|---|---|---|
| Stranded human capital | **Armenia**, Georgia, Moldova | Educated populations, geographically or politically cut off from markets |
| Post-Soviet skills mismatch | Ukraine, Kyrgyzstan | Strong formal education inheritance, institutions that don't convert it |
| Institutional failure | Argentina is the canonical case | High literacy and universities, a century of relative decline |
| Brain drain | Much of the Caribbean, parts of the Balkans | The country pays to build the skills; another country gets the output |

## Armenia, which is where the question came from

Cowen asks whether Armenia can work, given Russia. Acemoglu — who is Armenian — gives a blunt answer: *"It has disappointed. Armenia has really disappointed. It has underperformed economically."* His explanation is almost entirely geographic and geopolitical, not educational:

> *"It's a landlocked country. It cannot export anything because, again, transport is not a possibility. It has to find a way of using its talent."*

The data complicate the story in an interesting way:

| Indicator | Value |
|---|---|
| GDP per capita | **~$8,900** (2025 est.), upper-middle income |
| TIMSS mathematics (grade 4) | Among the **lowest in its region**, though improving since 2011 |
| PISA | **First participation 2025** — no comparable historical scores |
| World Bank Human Capital Index | A child born today will be **58%** as productive as with full health and education |
| Expected years of schooling | 11.3 — falling to **8.0** when adjusted for learning quality |

**Sources:** [World Bank Armenia learning analysis](https://documents1.worldbank.org/curated/en/099165002012328951/pdf/P1749800007e7703509aac0261edaee2ee6.pdf) · [TIMSS 2023 Armenia](https://timss2023.org/wp-content/uploads/2024/10/Armenia.pdf) · [World Bank on Armenian education and growth](https://www.worldbank.org/en/news/opinion/2023/03/22/education-and-innovation-at-the-core-of-armenia-economic-growth)

**This is the nuance worth carrying.** Both Cowen and Acemoglu treat Armenian human capital as a given — *"the people are so smart," "the people are well educated."* That is the Soviet inheritance talking: Armenia was the USSR's engineering and technical hub, and the reputation is real. But the **measured learning of children in school today is weak**, and the 11.3 → 8.0 adjustment says most of the gap is quality, not access.

So Armenia may be a smaller outlier than it looks. Part of the underperformance is stranded geography, as Acemoglu says. Part of it is that the knowledge capital is a legacy stock that is not being replenished — which is exactly what the Hanushek–Woessmann framework would predict from those test scores. **Neither man raises this**, and it slightly undercuts the "smart people, bad geography" story they agree on.

## Reading

- Hanushek & Woessmann, *[The Knowledge Capital of Nations](https://mitpress.mit.edu/9780262548953/the-knowledge-capital-of-nations/)* (2015) — the core work
- Hanushek & Woessmann, ["Education and Economic Growth"](https://hanushek.stanford.edu/sites/default/files/publications/Hanushek+Woessmann%202021%20OxfResEncEcoFin.pdf) (2021) — a compact survey version, free
- Pritchett, "Where Has All the Education Gone?" (2001) — the paper that broke the years-of-schooling proxy
- Acemoglu, Gallego & Robinson, "Institutions, Human Capital and Development" (2014) — Acemoglu's own position: institutions dominate, and schooling's apparent effect is partly institutions in disguise

---

## Working notes

**The interesting tension, and I'd want your read on it.** Hanushek and Woessmann say cognitive skills drive growth. Acemoglu's own published work says **institutions** drive growth and human capital is substantially downstream of institutions. These are rival explanations of the same correlation, and Acemoglu is a principal in the fight. In this interview he answers the Armenia question in pure institutions-and-geography terms without mentioning schooling quality at all — which is exactly what you'd predict from his research program, and it's a nice illustration of how a scholar's framework shows up in an off-the-cuff answer. **That observation is mine and is worth a page of its own in draft 2.**

**⚠ What is not properly sourced here.** The over/under-performer tables are constructed from the general shape of this literature, not lifted from a specific published residual analysis. They are directionally right and individually defensible, but **there is no single table in Hanushek–Woessmann that looks like mine**. If you want this to be rigorous rather than orienting, the move is to reproduce their growth regression and rank the residuals — which is genuinely doable with public PISA and Penn World Table data, and would give real answers instead of archetypes.

**Also unverified:** the specific Gulf-state PISA-versus-income claim, and the Argentina characterization, are conventional wisdom in this literature rather than things I checked today.

**What draft 2 needs:** a scatter plot — test score on x, GDP per capita or growth on y, with the residual outliers labeled. That is the picture the question is really asking for, and it's buildable from public data. Armenia should be plotted on it.

**Checked against the book — and the tension above is confirmed by absence.** *What Happened to Liberal Democracy?* contains no PISA, no test-score data, no growth regression on cognitive skills, and no engagement with Hanushek and Woessmann. Armenia appears once, in an unrelated aside about inoculation. So the observation this page makes — that Acemoglu answers a schooling-quality question in pure institutions-and-geography terms — is not a quirk of an off-the-cuff interview answer. It is what his book does too: education enters Chapter 1 as a *public service failing to convert spending into outcomes* (see [NYC vs London - School Spending](/research/nyc-vs-london-school-spending/)) and never as a driver of growth. The rival-explanations framing stands, and the page can now say so about his stated position rather than inferring it from a research programme.

Checked against the audiobook edition (Penguin Random House Audio, narrated by John Lee), machine-transcribed; references are by chapter. A negative finding from a transcript is weaker than one from an index, though a literature engaged nowhere in twelve hours is not one being quietly relied on.

**Related:** [NYC vs London - School Spending](/research/nyc-vs-london-school-spending/) · [Acemoglu and Restrepo - The Task Framework](/research/acemoglu-and-restrepo-the-task-framework/)
