# 01. Scope Checklist

Use this checklist before running or reporting anything.

## Program Fit

```text
Program:
Product:
Feature:
Date tested:
Account/environment:
Official rules reviewed: yes/no
```

## Must Be True

```text
[ ] The product is in scope.
[ ] The tested behavior is in scope.
[ ] The test does not target third-party systems without permission.
[ ] The test does not use real private data.
[ ] The result is reproducible.
[ ] The impact is material, not cosmetic.
[ ] The report includes safe reproduction steps.
[ ] The report includes expected vs observed behavior.
[ ] The report includes mitigation suggestions.
```

## Likely In-Scope Candidate

```text
[ ] Context manipulation causes a meaningful unauthorized behavior.
[ ] Prompt injection reliably changes an agentic decision.
[ ] Controlled test data is exposed across a boundary.
[ ] A safety or abuse control fails with material impact.
[ ] A product action occurs that should have required user authorization.
```

## Likely Out of Scope

```text
[ ] Generic jailbreak only.
[ ] One-off hallucination.
[ ] Offensive language only.
[ ] Public information restated.
[ ] The model refuses most attempts.
[ ] No measurable impact.
[ ] No reproduction rate.
[ ] The evidence depends on unsafe or unauthorized testing.
```

## German Gamma Gate

Before report submission:

```text
support_count >= minimum valid attempts
reproduction_rate documented
logs preserved
uncertainty labeled
German Gamma output marked as appendix, not primary proof
```

