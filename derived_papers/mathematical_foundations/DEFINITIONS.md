# Definitions

This document develops a more formal vocabulary for the mathematical foundations of induced dependence.

The goal is to refine the master paper definition into a structure that can support propositions, examples, counterexamples, and eventual theorems.

## 1. System

Let a system be represented as:

```text
S = (V, Omega, C, D)
```

where:

- `V` is a set of variables, components, observables, or agents.
- `Omega` is the state space of the system.
- `C` is a set of admissible conditions.
- `D` is a dependency relation, predicate, or measure defined over elements of `V` under conditions in `C`.

This version separates the state space `Omega` from the condition set `C` so that constraints and observations can be treated as transformations of the possible states.

## 2. Variables

Let:

```text
X, Y in V
```

be two variables or components of the system.

Depending on the formal setting, `X` and `Y` may be:

- random variables,
- nodes in a graph,
- coordinates in a state space,
- observables,
- populations,
- model behaviors,
- events,
- morphisms or objects in a more abstract structure.

## 3. Conditions

A condition is any formal object that determines how the system is evaluated.

Let:

```text
c in C
```

be a condition.

A condition may represent:

- a context,
- a constraint,
- an observation regime,
- an intervention,
- a measurement setting,
- an environmental state,
- a selection rule,
- a partition of the state space,
- a transformation of available information.

## 4. Baseline Condition

Let:

```text
B in C
```

be the baseline condition.

The baseline condition is the reference state against which dependency transformation is evaluated.

It may represent:

- independence,
- prior dependency structure,
- unconstrained dynamics,
- pre-intervention state,
- pre-observation state,
- default measurement context.

The baseline does not have to be independent. It only has to be specified.

## 5. Inducing Condition

Let:

```text
I in C
```

be an inducing condition.

An inducing condition is a condition that produces, amplifies, reveals, suppresses, or transforms a dependency relation relative to the baseline.

Examples include:

- imposing a shared constraint,
- selecting a subspace of states,
- conditioning on an event,
- applying an intervention,
- changing the measurement context,
- introducing a shared resource limitation,
- monitoring a system,
- perturbing an environment.

## 6. Dependency Predicate

In the simplest formalization, dependence can be represented as a predicate:

```text
Dep_c(X, Y) in {true, false}
```

where `Dep_c(X, Y)` is true if `X` and `Y` are dependent under condition `c`.

Under this predicate form, a dependency transformation occurs when:

```text
Dep_B(X, Y) != Dep_I(X, Y)
```

This binary version is useful for definitions and theorem sketches, but it may be too coarse for empirical and simulation work.

## 7. Dependency Measure

Dependence can also be represented as a measure:

```text
D_c(X, Y) in R
```

where `D_c(X, Y)` quantifies the strength or degree of dependence between `X` and `Y` under condition `c`.

Examples of possible measures include:

- mutual information,
- correlation,
- conditional dependence,
- causal effect size,
- graph distance or connectivity,
- coupling strength,
- transfer entropy,
- covariance,
- constraint sensitivity.

Under this measure form, a dependency transformation occurs when:

```text
D_B(X, Y) != D_I(X, Y)
```

or, in empirical settings:

```text
|D_I(X, Y) - D_B(X, Y)| > epsilon
```

for a specified threshold `epsilon`.

## 8. Weak Induced Dependence

`X` and `Y` exhibit weak induced dependence under condition `I` relative to baseline `B` if:

```text
D_B(X, Y) != D_I(X, Y)
```

Weak induced dependence requires a detected or defined dependency transformation, but does not require a complete mechanism explaining why the transformation occurs.

Weak induced dependence is appropriate for:

- exploratory analysis,
- empirical detection,
- hypothesis generation,
- early simulation results.

## 9. Strong Induced Dependence

`X` and `Y` exhibit strong induced dependence under condition `I` relative to baseline `B` if:

```text
D_B(X, Y) != D_I(X, Y)
```

and there exists a specified mechanism `M_I` such that:

```text
M_I: D_B(X, Y) -> D_I(X, Y)
```

where `M_I` explains how the inducing condition transforms the dependency relation.

Strong induced dependence requires:

1. a baseline condition,
2. an inducing condition,
3. a dependency relation or measure,
4. a dependency transformation,
5. a mechanism attributing the transformation to the inducing condition.

## 10. Induced Independence

The framework also permits the opposite phenomenon: induced independence.

`X` and `Y` exhibit induced independence under condition `I` relative to baseline `B` when:

```text
D_B(X, Y) > D_I(X, Y)
```

and the decrease or disappearance of dependence is attributable to `I`.

In predicate form:

```text
Dep_B(X, Y) = true
Dep_I(X, Y) = false
```

Induced independence may occur when a condition blocks, screens off, partitions, masks, or suppresses a prior dependency.

## 11. Constraint-Induced Dependence

A central special case is constraint-induced dependence.

Let `K_I` be a constraint associated with inducing condition `I`.

If `K_I` restricts the state space:

```text
Omega_I subset Omega_B
```

and the restriction changes the dependency relation between `X` and `Y`, then `X` and `Y` exhibit constraint-induced dependence relative to `B`.

Minimal example:

```text
X, Y in {0, 1}
B: X and Y are independent
I: X == Y
```

Then:

```text
D_B(X, Y) ~= 0
D_I(X, Y) ~= 1
```

when `D` is mutual information in bits.

## 12. Selection-Induced Dependence

Selection-induced dependence occurs when an observation, filter, or selection rule changes the dependency structure of the observed system.

Let:

```text
F_I: Omega -> Omega_I
```

be a selection function associated with condition `I`.

If applying `F_I` changes the dependency relation between `X` and `Y`, then the observed dependence is selection-induced relative to baseline `B`.

This may be related to collider bias, conditioning, measurement selection, or restricted observation windows, but the induced dependence framework treats it as part of a broader class of dependency transformations.

## 13. Context-Induced Dependence

Context-induced dependence occurs when changing the evaluative, measurement, or operational context changes the dependency relation between `X` and `Y`.

In this case, `I` does not merely restrict states. It changes the meaning, accessibility, or comparability of the variables.

This form may be relevant to:

- Bell-type systems,
- contextuality,
- model evaluation,
- AI observability,
- social or ecological measurement regimes.

## 14. Candidate Proposition Schema

A general proposition may take the following form:

```text
If X and Y are independent under B,
and I imposes a shared constraint K_I on X and Y,
then X and Y may become dependent under I.
```

A stronger proposition would require specifying the class of constraints under which dependence necessarily appears.

## 15. Minimal Proof Target

A first proof target:

```text
Let X and Y be independent Bernoulli(1/2) variables under B.
Let I be the condition X == Y.
Then X and Y are dependent under I.
```

Sketch:

Under `B`:

```text
P_B(X, Y) = P_B(X)P_B(Y)
```

Under `I`, the possible states are restricted to:

```text
(0, 0), (1, 1)
```

Therefore:

```text
P_I(Y = 1 | X = 1) = 1
P_I(Y = 1) = 1/2
```

Since:

```text
P_I(Y = 1 | X = 1) != P_I(Y = 1)
```

`X` and `Y` are dependent under `I`.

## 16. Open Mathematical Questions

- What is the most general definition of a condition?
- Should conditions be modeled as operators, filters, constraints, interventions, or morphisms?
- When does state-space restriction necessarily induce dependence?
- When does conditioning produce induced dependence rather than merely reveal dependence?
- Can induced dependence be decomposed into causal, informational, and structural components?
- What is the relationship between induced dependence and conditional independence?
- Can there be a lattice or category of conditions ordered by their dependency transformations?
- What is the minimal theorem that distinguishes induced dependence from ordinary correlation?

