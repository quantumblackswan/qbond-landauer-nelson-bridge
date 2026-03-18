# Q-Bond Landauer–Nelson–TICE Bridge

[![CI](https://github.com/quantumblackswan/qbond-landauer-nelson-bridge/actions/workflows/ci.yml/badge.svg)](https://github.com/quantumblackswan/qbond-landauer-nelson-bridge/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-pending-lightgrey.svg)]()

**Author:** Kevin Henry Miller — Founder & President, [Q-Bond Network DeSCI DAO, LLC](https://www.qbondnetwork.com)  
**Email:** Kevin@qbondnetwork.com  
**ORCID:** [0009-0007-7286-3373](https://orcid.org/0009-0007-7286-3373)

---

## Core Result

$$E_{\text{bridge}} = k_B T \ln\!\left(\frac{2k_B T}{\gamma\hbar}\right)$$

and

$$E_{\text{bridge}} = k_B T \ln 2 \quad\iff\quad \gamma = \frac{k_B T}{\hbar}$$

Five conditions — on the diffusion ratio, friction, correlation time, bridge energy, and temperature independence — are proven pairwise equivalent.  Under a single closure postulate ($D_{\text{th}} = 2D_q$), the bridge energy equals exactly one Landauer bit of erasure.

---

## What This Repository Contains

| Folder | Contents |
|--------|----------|
| `paper/` | Manuscript PDF, supplement PDF, LaTeX sources, bibliography, figures |
| `src/bt11/` | Reusable Python modules: bridge energy, kernels, inversions, constants |
| `scripts/` | Top-level reproducibility scripts |
| `tests/` | Verified test suite (28+ checks, all PASS) |
| `results/` | Pre-generated tables, figures, verification summary |
| `docs/` | Theorem statement, assumptions, referee notes |

---

## What Is Proved

- **Exact diffusion-ratio identity:** $R = D_{\text{th}}/D_q = 2k_BT/(\gamma\hbar)$
- **Five-way equivalence theorem** (conditions i–v, pairwise)
- **Exact deviation formula:** $\Delta E = -k_BT\ln(1+\delta)$
- **TICE closure factor:** $C_{\text{TICE}}(t) = k_BT/[\hbar\gamma_{\text{eff}}(t)]$
- **Three kernel solutions** (Ohmic–Drude, algebraic, Gaussian) with crossing times
- **Mass independence** of the bridge energy
- **Second-law consistency** of the deviation sign

---

## What Is Not Proved

- **Conjecture 1** ($D_{\text{th}} = 2D_q$) is a closure postulate, not derived from first principles.
- Bochner positivity guarantees kernel **admissibility**, not **uniqueness**.
- This is a **conditional** theorem, not an unconditional derivation of Landauer from Nelson stochastic mechanics.

---

## Reproduce

```bash
# Clone
git clone https://github.com/quantumblackswan/qbond-landauer-nelson-bridge.git
cd qbond-landauer-nelson-bridge

# Install
pip install -r requirements.txt

# Run full verification (28 checks)
python scripts/landauer_nelson_solved.py

# Reproduce figures
python scripts/reproduce_figures.py

# Run test suite
pytest tests/ -v
```

---

## Citation

See [CITATION.cff](CITATION.cff) or click **"Cite this repository"** on GitHub.

---

## License

[MIT](LICENSE)
