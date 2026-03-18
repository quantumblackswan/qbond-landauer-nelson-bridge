"""
Inversion formulas: solve for γ, T, or R given the others.
"""

import numpy as np
from .constants import kB, hbar


def friction_from_ratio(R: float, T: float) -> float:
    """Solve R = 2 k_B T / (γ ℏ)  for γ  [1/s]."""
    return 2.0 * kB * T / (R * hbar)


def temperature_from_ratio(R: float, gamma: float) -> float:
    """Solve R = 2 k_B T / (γ ℏ)  for T  [K]."""
    return R * gamma * hbar / (2.0 * kB)


def ratio_from_bridge(E_bridge: float, T: float) -> float:
    """Solve E_bridge = k_B T ln R  for R  (dimensionless)."""
    return np.exp(E_bridge / (kB * T))


def delta_from_deviation(Delta_E: float, T: float) -> float:
    """Solve ΔE = -k_B T ln(1+δ)  for δ."""
    return np.exp(-Delta_E / (kB * T)) - 1.0


def ctice_from_bridge(E_bridge: float, T: float) -> float:
    """Solve E_bridge = k_B T ln(2 C_TICE)  for C_TICE."""
    return np.exp(E_bridge / (kB * T)) / 2.0
