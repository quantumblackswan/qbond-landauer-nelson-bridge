#!/usr/bin/env python3
"""
Reproduce all BT#11 figures.

Generates:
  - results/figures/bridge_energy_vs_x.pdf  (main figure)
  - results/figures/kernel_closure_examples.pdf  (supplement figure)
  - paper/figures/bridge_energy_vs_x.png
  - paper/figures/kernel_closure_examples.png
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── Setup paths ──
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from bt11.bridge import diffusion_ratio, bridge_energy, landauer_energy, closure_friction
from bt11.kernels import geff_drude, geff_algebraic, geff_gaussian, ctice
from bt11.constants import kB, hbar

PAPER_FIG = os.path.join(ROOT, "paper", "figures")
RESULTS_FIG = os.path.join(ROOT, "results", "figures")
os.makedirs(PAPER_FIG, exist_ok=True)
os.makedirs(RESULTS_FIG, exist_ok=True)

# ── Figure 1: Bridge energy vs x ──────────────────────────────────
T = 300.0
x = np.linspace(0.1, 5.0, 500)
gamma_vals = x * kB * T / hbar
E_br = np.array([bridge_energy(g, T) for g in gamma_vals])
E_L = landauer_energy(T)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, E_br / (kB * T), "b-", linewidth=2, label=r"$E_{\mathrm{bridge}}/k_BT$")
ax.axhline(np.log(2), color="r", linestyle="--", linewidth=1.5, label=r"$\ln 2$ (Landauer)")
ax.axvline(1.0, color="gray", linestyle=":", linewidth=1, label=r"$x = 1$ (closure)")
ax.fill_between(x, E_br / (kB * T), np.log(2),
                where=(E_br / (kB * T) > np.log(2)),
                alpha=0.15, color="blue", label="Super-Landauer")
ax.fill_between(x, E_br / (kB * T), np.log(2),
                where=(E_br / (kB * T) < np.log(2)),
                alpha=0.15, color="red", label="Sub-Landauer")
ax.set_xlabel(r"$x = \hbar\gamma / (k_BT)$", fontsize=12)
ax.set_ylabel(r"$E_{\mathrm{bridge}} / k_BT$", fontsize=12)
ax.set_title("Landauer–Nelson Bridge Energy", fontsize=13)
ax.legend(fontsize=9, loc="upper right")
ax.set_xlim(0.1, 5.0)
ax.set_ylim(-1.5, 3.5)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(PAPER_FIG, "bridge_energy_vs_x.png"), dpi=300)
fig.savefig(os.path.join(RESULTS_FIG, "bridge_energy_vs_x.pdf"))
print("[Fig 1] Saved: bridge_energy_vs_x.png / .pdf")
plt.close(fig)

# ── Figure S1: Three kernel closure examples ──────────────────────
g0 = 0.5
bA_Om = 1.5
Omega = 1.0
bA_alg = bA_Om
bA_gauss = bA_Om / np.sqrt(np.pi / 2)

t = np.linspace(0, 3, 500)
C_drude = np.array([1.0 / geff_drude(ti, g0, bA_Om, Omega) for ti in t])
C_alg = np.array([1.0 / geff_algebraic(ti, g0, bA_alg, Omega, n=2) for ti in t])
C_gauss = np.array([1.0 / geff_gaussian(ti, g0, bA_gauss, Omega) for ti in t])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, C_drude, "b-", linewidth=2, label="Ohmic–Drude")
ax.plot(t, C_alg, "r--", linewidth=2, label="Algebraic ($n=2$)")
ax.plot(t, C_gauss, "g-.", linewidth=2, label="Gaussian")
ax.axhline(1.0, color="k", linestyle=":", linewidth=1, label=r"$C_{\mathrm{TICE}} = 1$ (Landauer)")
ax.set_xlabel(r"$t$  [dimensionless]", fontsize=12)
ax.set_ylabel(r"$C_{\mathrm{TICE}}(t)$", fontsize=12)
ax.set_title("TICE Closure Factor — Three Kernel Examples", fontsize=13)
ax.legend(fontsize=9)
ax.set_xlim(0, 3)
ax.set_ylim(0.3, 2.2)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(PAPER_FIG, "kernel_closure_examples.png"), dpi=300)
fig.savefig(os.path.join(RESULTS_FIG, "kernel_closure_examples.pdf"))
print("[Fig S1] Saved: kernel_closure_examples.png / .pdf")
plt.close(fig)

# ── Figure extra: Ratio vs temperature ────────────────────────────
T_range = np.linspace(50, 1000, 200)
gamma_closure = np.array([closure_friction(Ti) for Ti in T_range])
R_vals = np.array([diffusion_ratio(closure_friction(Ti), Ti) for Ti in T_range])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(T_range, R_vals, "b-", linewidth=2)
ax.axhline(2.0, color="r", linestyle="--", linewidth=1.5, label="$R = 2$")
ax.set_xlabel("Temperature $T$ [K]", fontsize=12)
ax.set_ylabel("Diffusion ratio $R$", fontsize=12)
ax.set_title(r"$R = D_{\mathrm{th}}/D_q$ at closure ($\gamma = k_BT/\hbar$)", fontsize=13)
ax.legend(fontsize=10)
ax.set_ylim(1.5, 2.5)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(PAPER_FIG, "ratio_vs_temperature.png"), dpi=300)
fig.savefig(os.path.join(RESULTS_FIG, "ratio_vs_temperature.pdf"))
print("[Fig extra] Saved: ratio_vs_temperature.png / .pdf")
plt.close(fig)

print("\nAll figures generated.")
