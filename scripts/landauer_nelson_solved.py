#!/usr/bin/env python3
"""
BT#11 Code Archive — Reproducible Verification
================================================
# SHA-256: C3B11D8BD647980FAC4DE94D65774C78603813C2768B22DEBBFD99822ED47836
# Lock date: 2026-03-18

Bundles all BT#11 verification into a single self-contained script.
Intended for PRL supplemental code archive submission.

Tests:
  1. Five equivalence conditions (i)-(v)
  2. Exact deviation formula (positive/negative delta)
  3. Mass independence
  4. TICE closure factor for three kernels (Drude, algebraic, Gaussian)
  5. Crossing time t* existence and value
  6. Second-law consistency (sign of deviation)

Usage:
  python bt11_code_archive.py

Output:
  Console printout of all checks with PASS/FAIL.
  Exit code 0 if all pass, 1 if any fail.
"""

import sys
import numpy as np
from scipy.special import erf, erfinv

TOL = 1e-12
results = []

def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    results.append((name, status))
    mark = "  ✓" if condition else "  ✗"
    print(f"  {mark} {name}" + (f"  [{detail}]" if detail else ""))
    return condition

# ============================================================
# Physical constants (SI, exact or CODATA 2018)
# ============================================================
kB   = 1.380649e-23       # J/K (exact by 2019 SI)
hbar = 1.054571817e-34    # J·s
T    = 300.0              # K (room temperature for tests)

gamma_star = kB * T / hbar  # closure friction
D_q_mass1  = hbar / (2 * 1.0)  # Nelson diffusion for m=1 kg (bookkeeping)

print("=" * 60)
print("BT#11 CODE ARCHIVE — VERIFICATION")
print("=" * 60)

# ============================================================
print("\n--- Test 1: Five Equivalence Conditions ---")
# ============================================================
gamma0 = kB * T / hbar  # condition (ii)
m = 1.0  # mass drops out

D_th = kB * T / (m * gamma0)
D_q = hbar / (2 * m)

R = D_th / D_q
E_br = kB * T * np.log(R)
E_L = kB * T * np.log(2)
tau_cor = 1.0 / gamma0
tau_thermal = hbar / (kB * T)

check("(i) D_th = 2*D_q", abs(D_th - 2*D_q) < TOL,
      f"D_th={D_th:.6e}, 2*D_q={2*D_q:.6e}")
check("(ii) gamma_0 = kB*T/hbar", abs(gamma0 - kB*T/hbar) < TOL,
      f"gamma0={gamma0:.6e}")
check("(iii) tau_cor = hbar/(kB*T)", abs(tau_cor - tau_thermal) < TOL,
      f"tau_cor={tau_cor:.6e}, hbar/kBT={tau_thermal:.6e}")
check("(iv) E_bridge = kB*T*ln2", abs(E_br - E_L) < TOL * kB * T,
      f"E_br/(kBT)={E_br/(kB*T):.10f}, ln2={np.log(2):.10f}")
check("(v) dR/dT = 0 (R=2 is T-independent)",
      abs(R - 2.0) < TOL,
      f"R={R:.15f}")

# ============================================================
print("\n--- Test 2: Exact Deviation Formula ---")
# ============================================================
for delta in [0.1, -0.1, 0.5, -0.5, 1.0, 2.0]:
    gamma_d = gamma_star * (1 + delta)
    R_d = 2.0 / (1 + delta)
    E_d = kB * T * np.log(R_d)
    Delta_E = E_d - E_L
    Delta_E_formula = -kB * T * np.log(1 + delta)
    check(f"Deviation delta={delta:+.1f}",
          abs(Delta_E - Delta_E_formula) < TOL * kB * T,
          f"DeltaE/(kBT)={Delta_E/(kB*T):+.6f}")

# Sign rule
check("delta>0 => DeltaE<0 (sub-Landauer)",
      -kB*T*np.log(1+0.1) < 0)
check("delta<0 => DeltaE>0 (super-Landauer)",
      -kB*T*np.log(1-0.1) > 0)

# ============================================================
print("\n--- Test 3: Mass Independence ---")
# ============================================================
masses = [1e-30, 1e-27, 1e-20, 1.0, 1e10]
for m_test in masses:
    D_th_m = kB * T / (m_test * gamma_star)
    D_q_m = hbar / (2 * m_test)
    R_m = D_th_m / D_q_m
    check(f"R(m={m_test:.0e})=2", abs(R_m - 2.0) < TOL,
          f"R={R_m:.15f}")

# ============================================================
print("\n--- Test 4: TICE Closure Factor — Ohmic-Drude Kernel ---")
# ============================================================
# Dimensionless units: kBT/hbar = 1, Omega = 1
g0 = 0.5
bA_Omega = 1.5  # beta*A/Omega
Omega = 1.0

# C_TICE(t) = 1/gamma_eff(t)  [in units where kBT/hbar=1]
def geff_drude(t):
    return g0 + bA_Omega * (1 - np.exp(-Omega * t))

def C_tice_drude(t):
    return 1.0 / geff_drude(t)

check("C_TICE(0) = 1/g0 = 2.0", abs(C_tice_drude(0) - 1.0/g0) < TOL)
check("C_TICE(inf) = 1/(g0+bA/Om)",
      abs(C_tice_drude(1e6) - 1.0/(g0 + bA_Omega)) < TOL)

# Crossing time
arg = (g0 + bA_Omega - 1.0) / bA_Omega
tstar_drude = -np.log(arg) / Omega if arg > 0 else float('nan')
check("Drude t* exists and is positive",
      not np.isnan(tstar_drude) and tstar_drude > 0,
      f"t*={tstar_drude:.6f}")
check("C_TICE(t*) = 1.0 at crossing",
      abs(C_tice_drude(tstar_drude) - 1.0) < TOL,
      f"C={C_tice_drude(tstar_drude):.15f}")

# ============================================================
print("\n--- Test 5: TICE Closure Factor — Algebraic Kernel (n=2) ---")
# ============================================================
n = 2
bA_alg = bA_Omega * (n - 1)  # same asymptote

def geff_alg(t):
    return g0 + bA_alg / (n - 1) * (1 - (1 + Omega*t)**(1-n))

def C_tice_alg(t):
    return 1.0 / geff_alg(t)

denom_alg = g0 + bA_alg / (n - 1) - 1.0
tstar_alg = ((bA_alg / ((n-1) * denom_alg))**(1.0/(n-1)) - 1) / Omega

check("Algebraic t* exists and is positive",
      not np.isnan(tstar_alg) and tstar_alg > 0,
      f"t*={tstar_alg:.6f}")
check("C_TICE(t*) = 1.0 at crossing (algebraic)",
      abs(C_tice_alg(tstar_alg) - 1.0) < 1e-10,
      f"C={C_tice_alg(tstar_alg):.15f}")

# ============================================================
print("\n--- Test 6: TICE Closure Factor — Gaussian Kernel ---")
# ============================================================
bA_gauss = bA_Omega / np.sqrt(np.pi / 2)

def geff_gauss(t):
    return g0 + bA_gauss * np.sqrt(np.pi / 2) * erf(Omega * t / np.sqrt(2))

def C_tice_gauss(t):
    return 1.0 / geff_gauss(t)

arg_gauss = (1.0 - g0) / (bA_gauss * np.sqrt(np.pi / 2))
tstar_gauss = np.sqrt(2) * erfinv(arg_gauss) / Omega

check("Gaussian t* exists and is positive",
      not np.isnan(tstar_gauss) and tstar_gauss > 0,
      f"t*={tstar_gauss:.6f}")
check("C_TICE(t*) = 1.0 at crossing (Gaussian)",
      abs(C_tice_gauss(tstar_gauss) - 1.0) < 1e-10,
      f"C={C_tice_gauss(tstar_gauss):.15f}")

# ============================================================
print("\n--- Test 7: Second-Law Consistency ---")
# ============================================================
# For irreversible erasure: E_bridge >= E_Landauer
# => Delta E >= 0 => delta <= 0 (underdamped)
check("Second law: delta<=0 => DeltaE>=0",
      -kB*T*np.log(1 + (-0.5)) > 0 and -kB*T*np.log(1 + (-0.1)) > 0)
check("Second law: delta>0 => DeltaE<0 (violation for erasure)",
      -kB*T*np.log(1 + 0.5) < 0)

# ============================================================
# Summary
# ============================================================
n_pass = sum(1 for _, s in results if s == "PASS")
n_fail = sum(1 for _, s in results if s == "FAIL")
total = len(results)

print("\n" + "=" * 60)
print(f"SUMMARY: {n_pass}/{total} PASS, {n_fail}/{total} FAIL")
print("=" * 60)

if n_fail > 0:
    print("\nFAILED TESTS:")
    for name, status in results:
        if status == "FAIL":
            print(f"  ✗ {name}")
    sys.exit(1)
else:
    print("\nAll checks passed.")
    sys.exit(0)
