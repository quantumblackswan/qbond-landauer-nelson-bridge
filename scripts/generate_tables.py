#!/usr/bin/env python3
"""
Generate verification summary tables as CSV files.

Outputs:
  results/tables/theorem_checks.csv
  results/tables/inversion_checks.csv
  results/verification_summary.txt
"""

import os
import sys
import csv
import numpy as np
from scipy.special import erf, erfinv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from bt11.bridge import diffusion_ratio, bridge_energy, landauer_energy, closure_friction, deviation
from bt11.kernels import geff_drude, ctice, crossing_time_drude
from bt11.inversion import friction_from_ratio, temperature_from_ratio, ratio_from_bridge
from bt11.constants import kB, hbar

TABLES = os.path.join(ROOT, "results", "tables")
RESULTS = os.path.join(ROOT, "results")
os.makedirs(TABLES, exist_ok=True)

TOL = 1e-12
T = 300.0
gamma_star = closure_friction(T)

# ── Theorem checks ────────────────────────────────────────────────
rows = []

def add(name, expected, actual, tol=TOL):
    passed = abs(actual - expected) < tol * max(abs(expected), 1)
    rows.append({"Test": name, "Expected": expected, "Actual": actual,
                 "Status": "PASS" if passed else "FAIL"})

R = diffusion_ratio(gamma_star, T)
add("R at closure", 2.0, R)
add("E_bridge / kBT", np.log(2), bridge_energy(gamma_star, T) / (kB * T))
add("gamma*hbar / kBT", 1.0, gamma_star * hbar / (kB * T))
add("tau_cor * kBT / hbar", 1.0, (1.0 / gamma_star) * kB * T / hbar)

for delta in [0.1, -0.1, 0.5, -0.5]:
    actual = deviation(delta, T) / (kB * T)
    expected = -np.log(1 + delta)
    add(f"Deviation delta={delta:+.1f}", expected, actual)

for m in [1e-30, 1e-27, 1.0, 1e10]:
    D_th_m = kB * T / (m * gamma_star)
    D_q_m = hbar / (2 * m)
    add(f"R mass-indep (m={m:.0e})", 2.0, D_th_m / D_q_m)

with open(os.path.join(TABLES, "theorem_checks.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["Test", "Expected", "Actual", "Status"])
    w.writeheader()
    w.writerows(rows)
print(f"Wrote {len(rows)} theorem checks → results/tables/theorem_checks.csv")

# ── Inversion checks ─────────────────────────────────────────────
inv_rows = []

gamma_inv = friction_from_ratio(2.0, T)
inv_rows.append({"Test": "friction_from_ratio(R=2)", "Expected": gamma_star,
                 "Actual": gamma_inv, "Status": "PASS" if abs(gamma_inv - gamma_star) < TOL else "FAIL"})

T_inv = temperature_from_ratio(2.0, gamma_star)
inv_rows.append({"Test": "temperature_from_ratio(R=2)", "Expected": T,
                 "Actual": T_inv, "Status": "PASS" if abs(T_inv - T) < TOL else "FAIL"})

R_inv = ratio_from_bridge(kB * T * np.log(2), T)
inv_rows.append({"Test": "ratio_from_bridge(E_L)", "Expected": 2.0,
                 "Actual": R_inv, "Status": "PASS" if abs(R_inv - 2.0) < TOL else "FAIL"})

with open(os.path.join(TABLES, "inversion_checks.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["Test", "Expected", "Actual", "Status"])
    w.writeheader()
    w.writerows(inv_rows)
print(f"Wrote {len(inv_rows)} inversion checks → results/tables/inversion_checks.csv")

# ── Summary ───────────────────────────────────────────────────────
all_rows = rows + inv_rows
n_pass = sum(1 for r in all_rows if r["Status"] == "PASS")
n_fail = sum(1 for r in all_rows if r["Status"] == "FAIL")

summary = f"""BT#11 VERIFICATION SUMMARY
==========================
Date: 2026-03-18
Total checks: {len(all_rows)}
PASS: {n_pass}
FAIL: {n_fail}
Status: {"ALL PASS" if n_fail == 0 else "FAILURES DETECTED"}
"""

with open(os.path.join(RESULTS, "verification_summary.txt"), "w") as f:
    f.write(summary)
print(summary)
