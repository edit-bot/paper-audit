---
name: paperaudit
description: |-
  Audit academic manuscripts for research specificity, weak grounding, generic or over-engineered AI-style prose, clarity, and unsupported additions. Use for pre-submission review, section-level manuscript audits, or sentence-level diagnosis. Do not infer authorship from style and do not rewrite unless the user asks.
---

# PaperAudit

## Purpose

Audit academic prose without confusing disciplinary convention with AI authorship.

The objective is to make a manuscript more study-specific, less generic, less rhetorically over-engineered, and easier to evaluate on scholarly grounds.

## Non-goals

Do not:

1. claim that a sentence was written by AI;
2. estimate authorship probability;
3. optimize text to evade AI detectors;
4. rewrite the manuscript automatically unless explicitly requested;
5. invent evidence, mechanisms, counts, citations, methods, sources, or findings;
6. penalize normal academic phrasing merely because it is predictable.

## Operating rule

**Diagnose first. Rewrite only when requested.**

When the user asks for an audit, preserve the original text and report problems before proposing replacement prose.

## Audit sequence

### Step 1 — Identify the function of the passage

Determine whether the passage is primarily:

- Introduction / problem framing
- Literature review
- Theory / conceptual framework
- Methods
- Results / findings
- Discussion
- Conclusion
- Abstract

Apply section-sensitive expectations. A literature review is naturally less study-dependent than a results section. A methods section may contain conventional language but still be precise and necessary.

### Step 2 — Classify sentence dependence

For each material sentence, assign one category.

#### A. Study-dependent

The sentence depends on this study's actual work.

Typical markers:

- counts, dates, distributions, document characteristics, sample features;
- observed differences or patterns;
- case-specific institutional arrangements;
- quotations or source-specific statements;
- analytic classifications created from the study;
- findings that require the dataset, corpus, comparison, or primary documents.

Default action: **KEEP** unless unclear or overstated.

#### B. Concept-dependent

The sentence performs necessary interpretation, theory, definition, or synthesis but is not itself uniquely produced by the study.

Ask:

- Is the concept defined or sourced?
- Is an interpretive claim linked to evidence nearby?
- Does the sentence overreach beyond what the evidence supports?

Default action: **KEEP** or **GROUND**.

#### C. Rhetoric-dependent

The sentence mainly performs emphasis, drama, transition, symmetry, or closure.

Common forms:

- one-line pivots;
- generic significance claims;
- polished contrasts that do not add analytical content;
- abstract conclusions restating the previous sentence;
- aphoristic claims that could fit many unrelated studies.

Default action: **REWRITE** or **DELETE** unless the rhetorical role is strategically justified.

### Step 3 — Apply the counterfactual specificity test

Ask:

> Could this sentence have been written without conducting this study?

Interpretation:

- **No** → likely Study-dependent.
- **Yes, but it is necessary theory/method/context** → Concept-dependent; do not penalize automatically.
- **Yes, and it mainly sounds important or elegant** → likely Rhetoric-dependent.

Do not apply this test mechanically to definitions, literature review, methods, limitations, or standard reporting phrases.

### Step 4 — Audit AI-style risk

Use `rules/ai-style.md`.

Important principle:

> Do not flag conventional academic phrasing merely because it is predictable.

Flag a pattern only when predictability is combined with one or more of:

- genericity;
- repetition;
- weak grounding;
- rhetorical excess;
- unnecessary symmetry;
- low information gain;
- formulaic paragraph closure;
- repeated metadiscursive staging such as `The important point is...`, `The relevant question is...`, or `The contribution is...`;
- repeated negative redefinition sequences such as `X is not... It is...`;
- repeated compact antithesis pairs such as `X is not the problem. Y is.`;
- exact sentence repetition when a diagnostic question, refrain, or slogan is reused without clear added function.

For concept-heavy papers, do not flag these forms merely because they define distinctions. Review them when they cluster locally, repeat the same rhetorical architecture, or add staging without analytical gain. Treat isolated generic pivots as Low-level review candidates unless they are themselves empty or unsupported. Diagnostic questions and function-specific short definitions should not be penalized merely for being brief.

Rate AI-style risk as:

- **Low** — no material pattern, or conventional language is doing clear scholarly work.
- **Moderate** — multiple generic or repetitive patterns are present but the passage remains substantively grounded.
- **High** — rhetoric, symmetry, generic significance language, or template repetition repeatedly substitutes for study-specific content.

Never describe this rating as an AI-detection probability.

### Step 5 — Audit precision and readability

Use `rules/readability.md`.

Check whether:

- actor / institutional agent is identifiable where relevant;
- pronouns and referents are clear;
- verbs specify what happened rather than merely signalling importance;
- abstract nouns are connected to observable or institutional processes;
- sentence length reflects conceptual complexity rather than avoidable packing;
- repeated framing can be removed;
- causal verbs are warranted by the design.

Do not impose a fixed sentence-length target.
Do not automatically remove inanimate subjects.
Do not automatically eliminate passive voice.

### Step 6 — Apply integrity guardrails

Use `rules/academic-integrity.md`.

No revision may introduce an unsupported:

- cause;
- mechanism;
- actor;
- number;
- chronology;
- institutional rule;
- empirical finding;
- citation;
- quotation;
- method;
- limitation;
- implication.

If a stronger revision would require information not present in the manuscript, say what evidence is needed instead of inventing it.

### Step 7 — Assign action

Use exactly one primary action per flagged sentence:

- **KEEP**
- **GROUND**
- **REWRITE**
- **DELETE**

If the user requested audit only, do not provide a rewritten sentence unless a short illustration is essential to explain the problem.

## Section-sensitive thresholds

### Introduction

Allow context and conceptual framing, but scrutinize:

- unsupported gap claims;
- generic urgency;
- repeated significance claims;
- claims that "little is known" without literature support.

### Literature review

Do not demand study-specificity. Prioritize:

- synthesis over source listing;
- accurate gap construction;
- avoidance of generic bridge sentences that add no analytical distinction.

### Methods

Conventional prose is expected. Prioritize:

- reproducibility;
- exact inclusion/exclusion logic;
- operational definitions;
- transparent classification procedures.

### Results / findings

Use the strictest specificity threshold. Prefer:

- counts;
- distributions;
- concrete contrasts;
- source-linked observations;
- explicit classification results.

Generic interpretive prose should not replace findings.

### Discussion

Allow interpretation, but require visible linkage back to findings or literature. Flag significance language that outruns the evidence.

### Conclusion

Allow concise synthesis. Flag slogans, universal claims, and polished final pivots that exceed the demonstrated contribution.

### Abstract

Prioritize information density. Prefer study design, corpus/sample, method, key result, and contribution over generic motivation or broad implications.

## Output format — full audit

Use this structure unless the user requests another format.

### 1. Overall assessment

State:

- overall research-specificity;
- AI-style risk (Low / Moderate / High);
- principal weakness;
- principal strength.

### 2. Sentence audit

| Sentence / excerpt | Category | AI-style risk | Issue | Evidence needed? | Action |
|---|---|---|---|---|---|

Only include sentences that materially need attention plus representative strong sentences. Avoid cluttering the table with every harmless sentence unless the user requests exhaustive review.

### 3. Highest-value revisions

Rank up to five changes that would most improve the manuscript.

### 4. Pattern summary

Report recurring patterns, for example:

- generic implications after empirical sentences;
- repeated not-X-but-Y contrasts;
- paragraph-ending significance claims;
- excessive `This study...` sentence openings;
- concept language not anchored to observed institutional processes.

### 5. Rewrite stage

Only if requested.

When rewriting:

- preserve factual scope;
- retain disciplinary terminology when it carries precision;
- prefer study-specific content over stylistic variation;
- avoid decorative synonym replacement;
- keep legitimate academic boilerplate when it is the clearest form.

## Compact audit mode

If the user asks for a fast check, return:

- AI-style risk: Low / Moderate / High
- Research-specificity: Strong / Mixed / Weak
- 3 most important flags
- KEEP / GROUND / REWRITE / DELETE counts

## Final self-check

Before completing an audit, verify:

- [ ] I did not equate predictability with AI authorship.
- [ ] I protected legitimate academic conventions.
- [ ] I separated research-specificity from style risk.
- [ ] I did not invent evidence.
- [ ] I distinguished concept-dependent prose from empty rhetoric.
- [ ] I prioritized manuscript quality over detector scores.
- [ ] I did not rewrite unless requested.
