# Changelog

## 1.0.0 — 2026-10-01

First stable English release.

- Completed calibration across four manuscript types, including one blind assessment-governance manuscript.
- Documented the distinction between contextual agent-based audit and the conservative static linter.
- Declared the v1.0 static-linter scope as English-language academic prose.
- Documented UTF-8 text/Markdown input requirements and DOCX/PDF conversion requirements.
- Added public-facing static-linter limitations, including treatment of Markdown structural lines and soft-wrapped line locations.
- Updated repository structure documentation.
- Bumped the static-linter version to `1.0.0`.
- Retained the v0.5.1 detection logic unchanged after the final blind calibration.

## 0.5.1 — 2026-10-01

- Fixed an overlap edge case in negative-redefinition clustering discovered during blind calibration against an assessment-governance manuscript.
- A sequence such as `Policy does not... The problem is not... It is...` is now treated as one redefinition move rather than two overlapping pairs.
- Moderate escalation now requires two non-overlapping negative-redefinition pairs within the local window.
- Added a regression test for chained negative redefinitions.

## 0.5.0 — 2026-10-01

- Calibrated the English linter against a third manuscript type focused on family work, institutional responsibility, and educational equity.
- Recalibrated isolated generic pivots such as `What matters is...` as Low review candidates; local repetition remains eligible for Moderate escalation.
- Exempted diagnostic questions and bare function-specific modal statements from the short-standalone-pivot rule.
- Added manuscript-level detection of repeated compact antithesis pairs such as `X is not the problem. Y is.` and `Responsibility may move. It should not disappear.`
- Added Low-level reporting for exact sentence repetition so intentional refrains and repeated diagnostic questions can be reviewed without being treated as errors.
- Stopped static prose analysis at standalone `References`, `Bibliography`, or `Works Cited` headings so bibliographic repetition is not misclassified as manuscript style.
- Added richer excerpts to repeated-pattern findings for easier manual review.
- Expanded regression coverage from 12 to 20 tests.

## 0.4.0 — 2026-10-01

- Calibrated the English linter against a concept-heavy assessment paper.
- Added soft-wrap normalization so prose is analysed consistently whether paragraphs are stored on one line or wrapped across several lines.
- Added local-cluster detection for repeated metadiscursive conceptual pivots such as `The important point is...`, `The relevant question is...`, and `The contribution is...`.
- Added detection of repeated negative redefinition pairs such as `X is not... It is...`, while leaving isolated instances unpenalized.
- Preserved conceptual distinctions as legitimate academic prose when they occur in isolation or carry necessary analytical content.
- Expanded regression coverage to 12 tests.

## 0.3.0 — 2026-10-01

- Recalibrated isolated `not X but Y` constructions from Moderate to Low; local repetition clusters remain Moderate.
- Added density-aware Moderate-risk thresholds for long manuscripts.
- Added Low-level review candidates for evidence-summary pivots such as `This finding demonstrates...`.
- Added a Low-level check for unsupported beyond-case relevance claims.
- Added regression tests based on full-manuscript calibration.

## 0.2.0 — 2026-10-01

- Calibrated the linter against a full academic manuscript section.
- Added sentence-count and moderate-pattern-density metrics.
- Added local clustering detection for repeated `not X but Y` rhetoric.
- Changed risk scoring so long manuscripts are not penalized by raw flag counts alone.
- Added conservative detection of short standalone conceptual pivots.
- Preserved the rule that conventional academic boilerplate is not evidence of AI authorship.
- Added tests for density-aware risk and contrast clustering.

## 0.1.0 — 2026-10-01

Initial specification.

Added:

- Study-dependent / Concept-dependent / Rhetoric-dependent classification.
- KEEP / GROUND / REWRITE / DELETE action system.
- AI-style risk separated from research specificity.
- Protection for legitimate academic boilerplate.
- Section-sensitive audit rules.
- Academic-integrity guardrails.
- Conservative standard-library static linter.
- False-positive examples.
