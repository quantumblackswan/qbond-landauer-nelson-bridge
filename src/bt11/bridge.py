"""
Bridge energy, diffusion ratio, and deviation formulas.

All functions use SI units unless noted otherwise.
"""

import numpy as np
from .constants import kB, hbar


def closure_friction(T: float) -> float:
    """Closure friction γ* = k_B T / ℏ  [1/s]."""
    return kB * T / hbar


def diffusion_ratio(gamma: float, T: float) -> float:
    """R = D_th / D_q = 2 k_B T / (γ ℏ).  Dimensionless."""
    return 2.0 * kB * T / (gamma * hbar)


def bridge_energy(gamma: float, T: float) -> float:
    """E_bridge = k_B T ln(R) = k_B T ln(2 k_B T / (γ ℏ))  [J]."""
    R = diffusion_ratio(gamma, T)
    return kB * T * np.log(R)


def landauer_energy(T: float) -> float:
    """E_Landauer = k_B T ln 2  [J]."""
    return kB * T * np.log(2)


def deviation(delta: float, T: float) -> float:
    """
    Exact deviation from Landauer:
        ΔE = E_bridge - E_Landauer = -k_B T ln(1 + δ)  [J]

    where γ = γ*(1 + δ).
    """
    return -kB * T * np.log(1.0 + delta)
