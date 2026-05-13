# Formal Definition

This document gives a first formal working definition of induced dependence for the master paper. The notation is provisional and should remain compatible with the later mathematical foundations paper.

## 1. System

Let a system be represented as:

```text
S = (V, E, C)
```

where:

- `V` is a set of components, variables, agents, or observables.
- `E` is a set of relations, interactions, or possible dependency edges among elements of `V`.
- `C` is a set of contexts, constraints, observations, interventions, or operating conditions under which the system can be evaluated.

## 2. Components and Variables

Let:

```text
X, Y in V
```

represent two components or variables in the system.

The framework does not require `X` and `Y` to be physical objects. They may be random variables, ecological populations, measurement outcomes, model behaviors, latent states, or mathematical objects.

## 3. Baseline State

Let:

```text
B in C
```

represent a baseline condition.

The baseline state is the reference condition against which dependency transformation is evaluated. It may represent an unconstrained state, a pre-intervention state, a prior measurement context, or a known reference configuration.

## 4. Inducing Condition

Let:

```text
I in C
```

represent an inducing condition.

An inducing condition may be a context, constraint, observation, intervention, environmental change, measurement arrangement, or shared system condition that changes the dependency structure of the system.

## 5. Dependency Relation

Let:

```text
D_c(X, Y)
```

denote the dependency relation between `X` and `Y` under condition `c`.

The meaning of `D_c` depends on the domain and formalism. It may represent:

- statistical dependence,
- causal dependence,
- informational dependence,
- graph connectivity,
- dynamical coupling,
- contextual dependence,
- structural constraint.

At this stage, `D_c(X, Y)` should be read as a general dependency predicate or dependency measure.

## 6. Dependency Transformation

A dependency transformation occurs when the dependency relation between `X` and `Y` differs across conditions:

```text
D_B(X, Y) != D_I(X, Y)
```

This difference may involve:

- appearance of dependence,
- disappearance of dependence,
- strengthening of dependence,
- weakening of dependence,
- change in type of dependence,
- change in direction or structure of dependence.

## 7. Induced Dependence

`X` and `Y` exhibit induced dependence under condition `I` relative to baseline `B` when:

```text
D_B(X, Y) != D_I(X, Y)
```

and the change in dependency relation is attributable to the inducing condition `I`.

In words:

Induced dependence occurs when a dependency relation between components is produced, amplified, revealed, or transformed by a specified condition, relative to a defined baseline.

## 8. Minimal Criteria

A claim of induced dependence should specify:

1. the system `S`,
2. the components or variables `X` and `Y`,
3. the baseline condition `B`,
4. the inducing condition `I`,
5. the dependency relation or measure `D`,
6. the observed or formal transformation from `D_B(X, Y)` to `D_I(X, Y)`,
7. the reason the transformation is attributable to `I`.

## 9. Strong and Weak Forms

### Weak Induced Dependence

Weak induced dependence occurs when a dependency relation changes across conditions, but the mechanism of induction remains partially unspecified.

```text
D_B(X, Y) != D_I(X, Y)
```

Weak induced dependence is useful for exploratory analysis and hypothesis generation.

### Strong Induced Dependence

Strong induced dependence occurs when the inducing condition can be shown to produce or transform the dependency relation by a specified mechanism.

```text
I -> [D_B(X, Y) -> D_I(X, Y)]
```

Strong induced dependence is the preferred target for formal modeling and empirical validation.

## 10. Candidate General Form

A compact representation of induced dependence is:

```text
ID_S(X, Y | B, I, D)
```

read as:

`X` and `Y` exhibit induced dependence in system `S`, relative to baseline `B`, under inducing condition `I`, with respect to dependency relation `D`.

## 11. Distinctions

### Induced Dependence vs. Correlation

Correlation is an observed association. Induced dependence concerns the condition-driven transformation that produces, modifies, or reveals a dependency relation.

### Induced Dependence vs. Confounding

Confounding is one possible source of observed association. Induced dependence is broader: it includes structural, contextual, observational, and intervention-driven transformations of dependency.

### Induced Dependence vs. Direct Causation

Direct causation describes a relation in which one variable produces change in another. Induced dependence may arise without direct causation between `X` and `Y`, for example through a shared constraint or measurement context.

## 12. Open Formal Questions

- Should `D_c(X, Y)` be treated primarily as a predicate, measure, graph edge, operator, or relation in a category?
- What counts as sufficient attribution to the inducing condition `I`?
- Can induced dependence be decomposed into causal, informational, and structural components?
- Under what conditions is induced dependence detectable from observations alone?
- Can there be induced independence, where a condition removes or suppresses a prior dependency?

