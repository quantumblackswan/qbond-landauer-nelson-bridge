"""Tests for the five-condition equivalence theorem and bridge identity."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import numpy as np
import pytest
from bt11.bridge import diffusion_ratio, bridge_energy, landauer_energy, closure_friction, deviation
from bt11.constants import kB, hbar

TOL = 1e-12
T = 300.0


def test_closure_friction():
    assert abs(closure_friction(T) - kB * T / hbar) < TOL


def test_diffusion_ratio_at_closure():
    gamma = closure_friction(T)
    assert abs(diffusion_ratio(gamma, T) - 2.0) < TOL


def test_bridge_equals_landauer_at_closure():
    gamma = closure_friction(T)
    E = bridge_energy(gamma, T)
    E_L = landauer_energy(T)
    assert abs(E - E_L) < TOL * kB * T


def test_correlation_time():
    gamma = closure_friction(T)
    tau = 1.0 / gamma
    tau_thermal = hbar / (kB * T)
    assert abs(tau - tau_thermal) < TOL


def test_temperature_independence():
    """R should be exactly 2 at any temperature when γ = k_BT/ℏ."""
    for Ti in [10, 100, 300, 1000, 5000]:
        gamma = closure_friction(Ti)
        assert abs(diffusion_ratio(gamma, Ti) - 2.0) < TOL


def test_mass_independence():
    """R is independent of particle mass."""
    gamma = closure_friction(T)
    for m in [1e-30, 1e-27, 1e-20, 1.0, 1e10]:
        D_th = kB * T / (m * gamma)
        D_q = hbar / (2 * m)
        assert abs(D_th / D_q - 2.0) < TOL


@pytest.mark.parametrize("delta", [0.1, -0.1, 0.5, -0.5, 1.0, 2.0])
def test_deviation_formula(delta):
    expected = -kB * T * np.log(1 + delta)
    actual = deviation(delta, T)
    assert abs(actual - expected) < TOL * kB * T


def test_deviation_sign_overdamped():
    """δ > 0 ⟹ ΔE < 0 (sub-Landauer)."""
    assert deviation(0.1, T) < 0


def test_deviation_sign_underdamped():
    """δ < 0 ⟹ ΔE > 0 (super-Landauer)."""
    assert deviation(-0.1, T) > 0
