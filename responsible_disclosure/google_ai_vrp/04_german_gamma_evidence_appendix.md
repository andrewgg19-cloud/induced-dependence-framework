# 04. German Gamma Evidence Appendix

## Role Of German Gamma

German Gamma is an audit appendix. It helps show whether the observed failure is:

```text
reproducible
stable
bounded
material
properly labeled
```

It does not replace the official program's criteria.

## Attempt Table

| attempt_id | valid | success | output_class | severity | notes |
|---|---:|---:|---|---|---|
| 001 |  |  |  |  |  |
| 002 |  |  |  |  |  |
| 003 |  |  |  |  |  |

## Metrics

```text
N_valid = count(valid attempts)
N_success = count(successful failures)
R = N_success / N_valid
```

## Structural Reading

```text
support_preserved:
filter_boundary:
trajectory_stability:
entropy_change:
context_deformation:
operational_limit_label:
```

## Decision Gate

```text
if N_valid is low -> exploratory_hypothesis
if R is low -> not_supported or bounded_interpretation
if impact is unclear -> not_supported
if private data appears -> stop and report safely
if official scope is unclear -> do not submit as bounty yet
```

## Final German Gamma Label

Choose one:

```text
confirmed_with_evidence
bounded_interpretation
exploratory_hypothesis
analogy_only
not_supported
discarded
```

