# Simulation Results

This document records the current results from simulations in this directory.

## Minimal Induced Dependence

Script:

```text
simulations/minimal_induced_dependence.py
```

### Model

Two binary variables `X` and `Y` are sampled independently under baseline condition `B`.

An inducing condition `I` then imposes the shared constraint:

```text
X == Y
```

The dependency measure `D` is empirical mutual information in bits.

### Latest Run

Sample size under baseline:

```text
10000
```

Joint counts under baseline:

```text
(0, 0): 2487
(0, 1): 2530
(1, 0): 2519
(1, 1): 2464
```

Mutual information under baseline:

```text
0.0001 bits
```

Sample size under inducing condition:

```text
4951
```

Joint counts under inducing condition:

```text
(0, 0): 2487
(0, 1): 0
(1, 0): 0
(1, 1): 2464
```

Mutual information under inducing condition:

```text
1.0000 bits
```

### Interpretation

The dependency relation changes from approximately independent to fully dependent under the shared constraint.

In the notation of the master paper:

```text
D_B(X, Y) ~= 0
D_I(X, Y) ~= 1
```

This is a minimal computational example of induced dependence.

