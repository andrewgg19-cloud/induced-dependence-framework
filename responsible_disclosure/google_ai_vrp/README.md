# Google AI VRP - Responsible Evaluation Package

## Purpose

This folder prepares a responsible vulnerability-report workflow for AI safety
and security programs.

German Gamma is used only as an auxiliary audit layer:

```text
reproducibility
support
selection effects
trajectory
entropy
context deformation
operational limits
```

It is not the vulnerability by itself.

## Boundary

Do not test against systems, accounts, users, data, plugins, websites or APIs
without authorization.

Do not attempt to extract private data, credentials, secrets, personal
information, proprietary model internals or harmful operational instructions.

Only submit through official disclosure channels.

## Candidate Scope

The most compatible categories for German Gamma-style evidence are:

```text
context manipulation
prompt injection in authorized agentic workflows
unauthorized action under controlled conditions
data exposure caused by a controlled test fixture
policy-boundary inconsistency with material safety impact
```

Avoid weak or likely out-of-scope reports:

```text
generic jailbreak with no material impact
model says rude content
ordinary hallucination
public information repeated by model
single anecdotal response
non-reproducible prompt trick
claims without logs
```

## Files

```text
01_scope_checklist.md
02_test_protocol.md
03_report_template.md
04_german_gamma_evidence_appendix.md
```

