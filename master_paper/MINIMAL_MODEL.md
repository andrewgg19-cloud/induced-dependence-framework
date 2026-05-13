# Minimal Model

This document connects the formal definition of induced dependence to the first computational simulation in `simulations/minimal_induced_dependence.py`.

## 1. Purpose

The minimal model demonstrates how two variables that are independent under a baseline condition can become dependent under a shared constraint.

The model is intentionally simple. Its purpose is not to represent a specific physical, ecological, or AI system, but to show the core structure of induced dependence in the smallest possible setting.

## 2. Variables

Let:

```text
X, Y in {0, 1}
```

where `X` and `Y` are binary variables.

## 3. Baseline Condition

Under baseline condition `B`, `X` and `Y` are sampled independently:

```text
P_B(X, Y) = P_B(X) P_B(Y)
```

In this condition, the expected dependency relation is:

```text
D_B(X, Y) ~= 0
```

when `D` is measured by mutual information.

## 4. Inducing Condition

The inducing condition `I` imposes the shared constraint:

```text
X == Y
```

Only states satisfying this constraint are retained:

```text
(0, 0), (1, 1)
```

while the states:

```text
(0, 1), (1, 0)
```

are excluded.

## 5. Dependency Transformation

Under the baseline condition, all four joint states are possible and approximately equally likely.

Under the inducing condition, only two joint states remain possible. Knowing `X` now determines `Y`, and knowing `Y` determines `X`.

The dependency transformation is:

```text
D_B(X, Y) ~= 0
D_I(X, Y) ~= 1
```

when `D` is empirical mutual information measured in bits.

## 6. Interpretation

The dependence between `X` and `Y` is not introduced by a direct causal arrow from `X` to `Y` or from `Y` to `X`. Instead, the dependence is induced by the shared constraint `X == Y`.

This gives a minimal example of the general form:

```text
ID_S(X, Y | B, I, D)
```

where:

- `S` is the binary-variable system,
- `B` is the independent sampling condition,
- `I` is the shared equality constraint,
- `D` is mutual information,
- `X` and `Y` exhibit induced dependence under `I` relative to `B`.

## 7. Role in the Paper

This model can serve as the first formal illustration in the master paper. It should appear after the conceptual definition and before more complex domain-specific examples.

