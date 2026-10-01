# Before / After Examples

These examples demonstrate the audit logic. They are not universal templates.

## Example 1 — Generic implication after a finding

### Before

> Eight of the eleven rule-change units expanded recognition of learning outside the school site. This highlights a broader transformation in the boundaries of schooling.

### Audit

- Sentence 1: **Study-dependent / KEEP**
- Sentence 2: **Rhetoric-dependent / GROUND or DELETE**
- AI-style risk: Moderate

### Safer revision

> Eight of the eleven rule-change units expanded recognition of learning outside the school site, while fewer transferred responsibility for instructional provision.

Why: the revision returns to the study's observed contrast instead of escalating immediately to a broad transformation claim.

---

## Example 2 — Legitimate academic boilerplate

### Before

> This study examines how responsibility for continuity is allocated across institutional boundaries.

### Audit

- **Concept-dependent / KEEP**
- AI-style risk: Low

Why: predictable wording is performing a clear research-question function. No revision is needed merely because the sentence is conventional.

---

## Example 3 — Repeated not-X-but-Y rhetoric

### Before

> The issue is not access but continuity. The problem is not provision but responsibility. The key question is not whether alternatives exist but whether pathways remain connected.

### Audit

- predominantly **Rhetoric-dependent**
- AI-style risk: High
- Action: **REWRITE**

### Possible revision

> The analysis separates three issues: access to an alternative, responsibility for sustaining participation, and connection to a subsequent educational pathway.

Why: the analytical distinctions are retained without stacking three contrastive slogans.

---

## Example 4 — Unsafe mechanism insertion

### Before

> The policy strengthened coordination.

### Bad rewrite

> The policy strengthened coordination by requiring monthly data sharing between schools and health services.

Problem: the mechanism was invented.

### Correct audit response

> **GROUND** — Specify the documented coordination requirement or observable procedural change. Do not infer a data-sharing mechanism unless the source establishes it.

---

## Example 5 — Conceptual sentence that should survive

### Before

> Formal availability and practical usability are analytically distinct.

### Audit

- **Concept-dependent / KEEP** if the distinction is defined and applied later.
- AI-style risk: Low.

The sentence is general, but generality is not itself a defect.
