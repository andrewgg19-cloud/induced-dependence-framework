# Project Status

This document summarizes the current state of the Induced Dependence scientific program repository.

## Current Version

Initial research package.

The repository now contains the first organized version of the program: conceptual structure, master paper draft, formal definition, minimal model, simulation, results, figure, bibliography, licensing, and manuscript outputs.

## Main Deliverables

- `manuscript/MASTER_PAPER.pdf` - Current PDF version of the master paper draft.
- `manuscript/MASTER_PAPER.txt` - Plain-text version of the master paper draft.
- `master_paper/DRAFT.md` - Editable integrated source draft.
- `figures/minimal_model_diagram.png` - Main conceptual figure for the minimal model.
- `simulations/minimal_induced_dependence.py` - First reproducible simulation.
- `simulations/RESULTS.md` - Recorded results from the minimal simulation.

## Scientific Core

The current master framework defines induced dependence as a dependency relation produced, amplified, revealed, or transformed by context, constraint, observation, intervention, or shared system conditions.

The minimal model demonstrates the core idea:

```text
D_B(X, Y) ~= 0
D_I(X, Y) ~= 1
```

Two binary variables begin approximately independent under baseline condition `B`. Under inducing condition `I`, the shared constraint `X == Y` produces a strong dependency relation.

## Repository Areas

- `master_paper/` - Core theory, definition, claims, minimal model, and integrated source draft.
- `derived_papers/` - Domain-specific paper outlines for Bell systems, ecology, AI observability, and mathematical foundations.
- `simulations/` - Computational experiments and recorded results.
- `notebooks/` - Reserved for exploratory analysis.
- `figures/` - Conceptual and generated visual materials.
- `references/` - Bibliography files.
- `manuscript/` - Exported manuscript versions.

## Licensing

This repository uses a mixed-license structure.

- Scientific writing, documentation, conceptual materials, and figures: CC BY 4.0.
- Code, simulations, notebooks, and software utilities: MIT License.

Copyright (c) 2026 Germán García.

See `LICENSE.md` and `LICENSE-CODE-MIT.txt` for details.

## Completed

- Repository structure created.
- README files added for all major sections.
- Scientific roadmap created.
- Glossary created.
- Master paper abstract, introduction, claims, formal definition, and minimal model created.
- First integrated master paper draft created.
- Minimal simulation implemented and executed.
- Simulation results recorded.
- Conceptual figure created.
- Bibliography initialized.
- Manuscript PDF and plain-text versions created.
- Licensing added.

## Next Scientific Milestones

1. Expand the bibliography with domain-specific references.
2. Refine the formal definition into a theorem-ready version.
3. Develop the mathematical foundations paper.
4. Build a second simulation using a less minimal shared constraint or network structure.
5. Add one developed domain case, preferably ecology or AI observability.
6. Convert the master draft into a fuller paper with citations and section-level argumentation.

## Immediate Recommended Next Step

Develop `derived_papers/mathematical_foundations/DEFINITIONS.md` to strengthen the formal basis of the program.

