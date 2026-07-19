# 03. Vulnerability Report Template

## Title

```text
[Product/Feature] Reproducible [category] under controlled [context/prompt/agent] condition
```

## Summary

```text
Briefly describe the issue, affected product, and material impact.
```

## Program And Scope

```text
Program:
Product:
Feature:
Scope category:
Reason this is in scope:
```

## Environment

```text
Date:
Region:
Account type:
Model/version if visible:
Browser/app/API version:
Relevant settings:
```

## Expected Behavior

```text
Describe the behavior the product should have shown.
```

## Observed Behavior

```text
Describe what actually happened.
Use exact logs where allowed.
Do not include private data, secrets or unsafe instructions.
```

## Steps To Reproduce

```text
1. Open authorized test environment.
2. Configure controlled test fixture.
3. Run the provided safe reproduction sequence.
4. Observe the boundary failure.
5. Repeat n times.
```

## Reproduction Statistics

```text
valid_attempts:
successful_failures:
reproduction_rate:
confidence_notes:
```

## Impact

```text
Explain the material harm or risk.
Tie it to the program's scope.
Avoid broad claims.
```

## German Gamma Appendix Summary

```text
support_count:
selection/filter condition:
trajectory reading:
entropy reading:
operational limit release level:
final evidence label:
```

## Mitigation Suggestions

```text
Add or strengthen boundary check.
Separate untrusted context from trusted instruction.
Require confirmation before sensitive action.
Improve refusal consistency for the specific scoped behavior.
Log and detect repeated boundary-crossing attempts.
```

## Disclosure

```text
Submitted only through the official channel.
No public disclosure before permission.
No third-party data included.
```

