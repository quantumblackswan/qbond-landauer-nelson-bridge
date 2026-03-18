# Data Directory

This repository accompanies a **theoretical** result (BT#11: Conditional Landauer–Nelson Bridge).

There is no experimental or observational raw data. All numerical results are generated deterministically by the scripts in `scripts/` from closed-form equations.

## Reproducing outputs

```bash
python scripts/generate_tables.py      # → results/tables/, results/verification_summary.txt
python scripts/reproduce_figures.py     # → results/figures/
python scripts/landauer_nelson_solved.py  # → standalone 28-check verification
```

All outputs are fully reproducible from the source code alone.
