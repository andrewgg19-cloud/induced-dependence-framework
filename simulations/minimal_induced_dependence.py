"""Minimal simulation of induced dependence under a shared constraint.

The baseline condition samples two independent binary variables X and Y.
The inducing condition keeps only cases where X and Y satisfy a shared
constraint. This makes the dependency structure change across conditions.
"""

from __future__ import annotations

import math
import random
from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class DependenceSummary:
    condition: str
    sample_size: int
    joint_counts: Counter[tuple[int, int]]
    mutual_information_bits: float


def sample_baseline(n: int, seed: int = 7) -> list[tuple[int, int]]:
    """Sample independent binary variables X and Y."""
    rng = random.Random(seed)
    return [(rng.randint(0, 1), rng.randint(0, 1)) for _ in range(n)]


def apply_shared_constraint(samples: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Inducing condition: retain only states satisfying X == Y."""
    return [(x, y) for x, y in samples if x == y]


def mutual_information(samples: list[tuple[int, int]]) -> float:
    """Compute empirical mutual information I(X;Y) in bits."""
    n = len(samples)
    if n == 0:
        return 0.0

    joint = Counter(samples)
    x_counts = Counter(x for x, _ in samples)
    y_counts = Counter(y for _, y in samples)

    mi = 0.0
    for (x, y), count in joint.items():
        p_xy = count / n
        p_x = x_counts[x] / n
        p_y = y_counts[y] / n
        mi += p_xy * math.log2(p_xy / (p_x * p_y))
    return mi


def summarize(condition: str, samples: list[tuple[int, int]]) -> DependenceSummary:
    return DependenceSummary(
        condition=condition,
        sample_size=len(samples),
        joint_counts=Counter(samples),
        mutual_information_bits=mutual_information(samples),
    )


def print_summary(summary: DependenceSummary) -> None:
    print(f"\n{summary.condition}")
    print("-" * len(summary.condition))
    print(f"sample_size: {summary.sample_size}")
    print("joint_counts:")
    for state in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(f"  {state}: {summary.joint_counts.get(state, 0)}")
    print(f"mutual_information_bits: {summary.mutual_information_bits:.4f}")


def main() -> None:
    baseline = sample_baseline(n=10_000)
    induced = apply_shared_constraint(baseline)

    baseline_summary = summarize("Baseline condition B: X and Y sampled independently", baseline)
    induced_summary = summarize("Inducing condition I: shared constraint X == Y", induced)

    print_summary(baseline_summary)
    print_summary(induced_summary)

    print("\nDependency transformation")
    print("-------------------------")
    print(
        "D_B(X, Y) differs from D_I(X, Y): "
        f"{baseline_summary.mutual_information_bits:.4f} bits -> "
        f"{induced_summary.mutual_information_bits:.4f} bits"
    )


if __name__ == "__main__":
    main()

