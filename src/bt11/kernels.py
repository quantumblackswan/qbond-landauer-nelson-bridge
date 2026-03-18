"""
Memory-kernel solutions and TICE closure factor.

Three kernels: Ohmic–Drude (exponential), algebraic (power-law), Gaussian.
All use dimensionless units where k_B T / ℏ = 1 unless SI arguments given.
"""

import numpy as np
from scipy.special import erf, erfinv


# ── Effective friction ──────────────────────────────────────────────

def geff_drude(t, gamma0, beta_A_over_Omega, Omega=1.0):
    """Ohmic–Drude kernel: K(τ) = A exp(-Ω|τ|)."""
    return gamma0 + beta_A_over_Omega * (1.0 - np.exp(-Omega * t))


def geff_algebraic(t, gamma0, beta_A, Omega=1.0, n=2):
    """Algebraic kernel: K(τ) = A (1 + Ω|τ|)^{-n}, n > 1."""
    return gamma0 + beta_A / (n - 1) * (1.0 - (1.0 + Omega * t) ** (1 - n))


def geff_gaussian(t, gamma0, beta_A, Omega=1.0):
    """Gaussian kernel: K(τ) = A exp(-Ω²τ²/2)."""
    return gamma0 + beta_A * np.sqrt(np.pi / 2) * erf(Omega * t / np.sqrt(2))


# ── TICE closure factor ────────────────────────────────────────────

def ctice(geff_val, gamma_star=1.0):
    """C_TICE = γ* / γ_eff  (dimensionless).  γ* = k_B T/ℏ."""
    return gamma_star / geff_val


def bridge_energy_tice(geff_val, T, gamma_star=None):
    """E_bridge^TICE(t) = k_B T ln(2 C_TICE)  [J or dimensionless]."""
    from .constants import kB, hbar
    if gamma_star is None:
        gamma_star = kB * T / hbar
    C = gamma_star / geff_val
    return kB * T * np.log(2.0 * C)


# ── Crossing times ─────────────────────────────────────────────────

def crossing_time_drude(gamma0, beta_A_over_Omega, Omega=1.0, gamma_star=1.0):
    """
    Crossing time t* for Ohmic–Drude kernel.
    Real & positive when γ0 < γ* < γ0 + βA/Ω.
    """
    denom = gamma0 + beta_A_over_Omega - gamma_star
    if denom <= 0 or beta_A_over_Omega <= 0:
        return float('nan')
    arg = beta_A_over_Omega / denom
    if arg <= 0:
        return float('nan')
    return np.log(arg) / Omega


def crossing_time_algebraic(gamma0, beta_A, Omega=1.0, n=2, gamma_star=1.0):
    """Crossing time t* for algebraic kernel (implicit solve)."""
    denom = gamma0 + beta_A / (n - 1) - gamma_star
    if denom <= 0:
        return float('nan')
    ratio = (beta_A / ((n - 1) * denom)) ** (1.0 / (n - 1))
    return (ratio - 1.0) / Omega


def crossing_time_gaussian(gamma0, beta_A, Omega=1.0, gamma_star=1.0):
    """Crossing time t* for Gaussian kernel (inverse erf)."""
    prefactor = beta_A * np.sqrt(np.pi / 2)
    arg = (gamma_star - gamma0) / prefactor
    if arg <= 0 or arg >= 1:
        return float('nan')
    return np.sqrt(2) * erfinv(arg) / Omega
