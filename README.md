# PaperAudit

**Academic manuscript auditing for study-specificity, AI-style patterns, and clarity.**

PaperAudit is a rule-based framework for reviewing academic prose before submission. It is designed to identify two different problems that are often conflated:

1. **Research weakness** — sentences that are generic, weakly grounded, or insufficiently tied to the study.
2. **AI-style risk** — prose that is over-regular, rhetorically over-engineered, repetitive, or generically polished.

PaperAudit does **not** attempt to determine whether a human or an AI wrote a manuscript. It does not optimize text to defeat AI detectors. Its purpose is to make academic prose more study-specific, precise, and readable while preserving legitimate disciplinary conventions.

## Core principle

> Academic boilerplate is not a problem by itself. Empty boilerplate is.

Conventional phrases such as `This study examines...`, `The findings suggest...`, or `Previous research has shown...` should not be flagged merely because they are predictable. A sentence is more concerning when predictability is combined with genericity, repetition, rhetorical excess, or weak connection to study-specific evidence.

## Example audit

The examples below are synthetic. They illustrate the distinction between legitimate academic convention and prose that is generic or rhetorically over-engineered.

| Sentence | PaperAudit reading | Action |
|---|---|---|
| `This study examines how formal attendance rules changed across six national policy revisions between 2010 and 2024.` | Conventional academic framing, but tied to a defined corpus and analytical task. Predictability alone is not a problem. | **KEEP** |
| `These findings highlight the complex and multifaceted nature of institutional change in contemporary education.` | Grammatically polished but weakly study-specific. The sentence mainly adds generic significance. | **GROUND** or **REWRITE** |
| `The policy added two new recognition routes while leaving assessment authority with the enrolled school.` | Study-dependent claim that reports a concrete institutional pattern. | **KEEP** |
| `What matters is not flexibility, but meaningful flexibility.` | Rhetorical contrast without enough analytical content. | **DELETE** or replace with the specific finding |

PaperAudit therefore does **not** ask whether prose sounds academic or predictable. It asks whether the sentence is doing evidentiary, conceptual, methodological, or necessary explanatory work.

## What PaperAudit checks

### Layer 1 — Research specificity

Each sentence can be classified as:

- **Study-dependent** — could not reasonably be written without conducting this study, analysing its data, reading its primary sources, or performing its comparison.
- **Concept-dependent** — necessary conceptual or interpretive prose that requires nearby empirical, documentary, theoretical, or methodological support.
- **Rhetoric-dependent** — prose whose main function is emphasis, elegance, transition, or conceptual drama rather than evidentiary work.

The central diagnostic question is:

> **Could this sentence have been written without conducting this study?**

A `Yes` answer is not automatically a defect. Definitions, literature review, theory, and methods often require non-study-specific prose. The question is used to identify where grounding may be needed.

### Layer 2 — AI-style patterns

PaperAudit looks for patterns such as:

- repeated `not X but Y` constructions;
- generic pivots such as `This highlights...`, `This reveals...`, or `What matters is...`;
- abstract implication sentences that add little beyond the previous sentence;
- overly symmetrical three-part lists;
- repeated paragraph-ending significance claims;
- excessive signposting;
- recurrent sentence templates;
- vague evaluative phrases such as `important role`, `complex interplay`, or `broader implications` when not made specific;
- rhetoric that is unusually polished relative to the evidentiary content.

These patterns are **signals, not verdicts**.

### Layer 3 — Precision and readability

PaperAudit also checks for:

- unclear agents or referents;
- abstract or metaphorical verbs where a more precise operation is available;
- excessive nominalisation;
- overlong or overloaded sentences;
- avoidable repetition;
- unnecessary framing language;
- unsupported causal or mechanistic claims.

### Layer 4 — Academic integrity guardrails

PaperAudit must not invent:

- data;
- counts;
- mechanisms;
- causal claims;
- institutional arrangements;
- citations;
- sources;
- findings;
- methods;
- quotations.

**Diagnose first. Rewrite only when requested.**

When rewriting is requested, preserve the author's meaning and evidence boundaries.

## Decision labels

PaperAudit uses four actions:

- **KEEP** — the sentence is doing useful evidentiary, conceptual, or methodological work.
- **GROUND** — retain the claim, but connect it more clearly to evidence, a source, a mechanism, or a study-specific observation.
- **REWRITE** — the content is useful but the form is vague, repetitive, over-engineered, or unclear.
- **DELETE** — the sentence contributes little beyond rhetoric or repeats information already established.

## Recommended output

For close manuscript review, use a table like this:

| Sentence | Category | AI-style risk | Problem | Evidence needed? | Action | Note |
|---|---|---:|---|---|---|---|
| ... | Study-dependent | Low | — | No | KEEP | ... |
| ... | Concept-dependent | Moderate | Generic implication | Yes | GROUND | ... |
| ... | Rhetoric-dependent | High | One-line pivot | No | DELETE | ... |

At section level, report:

- sentences reviewed;
- Study-dependent / Concept-dependent / Rhetoric-dependent counts;
- AI-style risk: Low / Moderate / High;
- number of KEEP / GROUND / REWRITE / DELETE recommendations;
- the five highest-value revisions.

## Quick start

PaperAudit has two complementary modes:

- **Contextual manuscript audit** — load `SKILL.md` and the files in `rules/` in a capable language-model or agent environment. This mode can assess study-specificity, conceptual grounding, and section-sensitive revision needs.
- **Static linter** — run `scripts/paperaudit_lint.py` for conservative, rule-based checks of observable English prose patterns.

The v1.0 static linter targets **English-language academic prose**. It requires Python 3.10 or later and accepts UTF-8 plain-text or Markdown input. DOCX and PDF files should be converted to text or Markdown before running the linter.

A lightweight static linter is included:

```bash
python scripts/paperaudit_lint.py manuscript.md
```

JSON output:

```bash
python scripts/paperaudit_lint.py manuscript.md --format json
```

Strict mode exits with status 1 when the overall static-linter risk rating is `High`:

```bash
python scripts/paperaudit_lint.py manuscript.md --strict
```

The static linter is deliberately conservative. It cannot determine authorship, scientific validity, or actual study dependence. Those require contextual review by a human or language model using `SKILL.md`.
### Risk calibration

The static linter does not treat four isolated flags in a long manuscript the same way as four flags in a short passage. Version 1.0.0 reports:

- total sentences reviewed;
- moderate-pattern density;
- local clusters of repeated contrastive rhetoric;
- density of metadiscursive conceptual pivots;
- repeated negative-redefinition pairs such as `X is not... It is...`;
- local clusters of generic significance pivots;
- manuscript-level density of compact antithesis pairs;
- exact repeated sentences as Low-level review candidates.

The linter also stops at a standalone `References`, `Bibliography`, or `Works Cited` heading so bibliographic repetition is not treated as prose style. A `High` rating therefore requires both repeated moderate patterns and sufficient density. Local clusters can still produce a `Moderate` rating even when manuscript-wide density is low. Isolated conceptual distinctions remain review-neutral unless they form a repeated rhetorical pattern.


## Repository structure

```text
PaperAudit/
├── README.md
├── SKILL.md
├── LICENSE
├── ACKNOWLEDGEMENTS.md
├── CHANGELOG.md
├── requirements-dev.txt
├── .github/
│   └── workflows/
│       └── tests.yml
├── rules/
│   ├── research-specificity.md
│   ├── ai-style.md
│   ├── readability.md
│   └── academic-integrity.md
├── examples/
│   ├── before-after.md
│   └── false-positives.md
├── example-report*.json
├── scripts/
│   └── paperaudit_lint.py
└── tests/
    └── test_lint.py
```

## Design position

PaperAudit deliberately avoids a single "AI probability" score. Academic prose is highly conventional, and predictable language is not evidence of AI authorship. The tool instead reports observable stylistic and evidentiary patterns.

The target transformation is:

> **generic academic prose → study-specific academic prose**

not:

> AI score 100% → AI score 0%

## Status

Version `1.0.0` is the first stable English release. It has been calibrated across four manuscript types:

- empirical policy/document analysis;
- concept-heavy assessment theory;
- family-responsibility and equity analysis;
- a blind assessment-governance policy manuscript.

The linter distinguishes isolated academic pivots from repeated local staging, detects manuscript-level compact antithesis density, surfaces exact sentence repetition as a Low-level review candidate, excludes reference lists from prose-style analysis, and avoids double-counting overlapping negative-redefinition chains. It remains deliberately conservative: isolated academic distinctions are not treated as evidence of AI authorship or as automatic revision targets.

### Static-linter limitations

The static linter is intentionally narrow. It does not:

- read DOCX or PDF files directly;
- determine whether a sentence was written by AI;
- determine scientific validity, factual accuracy, or actual study dependence;
- understand citations, tables, figures, or Markdown structural lines as full manuscript context;
- replace contextual review by a human or language model.

When soft-wrapped prose is joined before analysis, reported line numbers point to the start of the joined text block rather than necessarily to the exact original sentence line.

## License

MIT. See `LICENSE`.

## Development

Run the test suite locally:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

GitHub Actions runs the tests automatically on pushes and pull requests against Python 3.10–3.12.
