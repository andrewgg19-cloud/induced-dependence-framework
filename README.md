# Induced Dependence Scientific Program

This repository organizes the core manuscript, derived papers, simulations, and exploratory notebooks for the Induced Dependence scientific program.

## Repository Structure

- `master_paper/` - Central manuscript developing the general theory of induced dependence.
- `derived_papers/bell_systems/` - Paper applying the framework to Bell-type systems and nonclassical correlations.
- `derived_papers/ecology/` - Paper applying induced dependence to ecological systems and interdependent dynamics.
- `derived_papers/ai_observability/` - Paper applying the framework to AI observability, monitoring, and latent dependency structures.
- `derived_papers/mathematical_foundations/` - Paper focused on formal definitions, theorems, and mathematical foundations.
- `simulations/` - Computational experiments, model implementations, and reproducible simulation scripts.
- `notebooks/` - Exploratory analyses, derivations, figures, and prototyping notebooks.
- `figures/` - Conceptual diagrams, manuscript figures, and generated visual outputs.
- `references/` - Bibliography files and citation sources.
- `manuscript/` - Exportable manuscript versions such as Word, PDF, or LaTeX outputs.
- `src/` - Operational diagnostic code and reusable framework scripts.
- `docs/` - Extended notes, appendices, and methodological documentation.
- `poster/` - Generated forensic reports and reproducible diagnostic outputs.

## Working Principle

The master paper should define the shared conceptual and mathematical language. Derived papers should reuse that language while developing domain-specific arguments, examples, and evidence.

## Current Draft

The first integrated draft of the master paper is available at `master_paper/DRAFT.md`.

## Citation

Citation metadata is provided in `CITATION.cff`. The initial planned release version is `v0.1.0`.

## One-Click Cloning and Forensic Replicability

This repository provides an automated validation engine designed to allow external laboratories to test datasets against filter-induced artifacts and autogenous model collapse.

### Execution Pipeline

Execute this terminal sequence to clone the codebase, verify the environment, and render the analytical figures:

```bash
# 1. Clone the verified open-science core repository
git clone https://github.com/andrewgg19-cloud/induced-dependence-framework.git

# 2. Open the operational repository directory
cd induced-dependence-framework

# 3. Install runtime dependencies if needed
pip install numpy pandas pillow

# 4. Execute the diagnostic pipeline and compile structural charts
python src/diagnostico_logs.py
```

### Compiled Evidence Artifacts

Upon successful execution, the core script automatically generates the following forensic files within the workspace:

- `poster/deformacion_observacional.png` - High-resolution scatter plot illustrating the shifting of the neutral point and emergent covariance.
- `poster/reporte_sensibilidad_forense.csv` - Chronological audit logs recording the generation where selection constraints trigger support truncation (`Delta_obs -> infinity`).

### Standardized Citation Profile

If this codebase, the standalone script `diagnostico_logs.py`, or the underlying propositions assist in corroborating data structures or certifying AI compliance under regulatory standards, please acknowledge the author via the following academic record:

```bibtex
@article{garcia2026filter,
  author    = {Garcia, German},
  title     = {The Filter Can Also Create Correlations: Invariance, Mathematical Homology, and the Induced Dependence Framework},
  journal   = {Zenodo Open Science Repository},
  year      = {2026},
  doi       = {10.5281/zenodo.20172257},
  url       = {https://doi.org/10.5281/zenodo.20172257},
  note      = {Version 1.1.0 -- Hard Sieve Validation Engine}
}
```

## License

Scientific writing, documentation, conceptual materials, and figures are licensed under CC BY 4.0. Code, simulations, notebooks, and software utilities are licensed under the MIT License.

See `LICENSE.md` for details.
