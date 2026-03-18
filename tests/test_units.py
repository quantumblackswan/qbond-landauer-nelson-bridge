"""Dimensional / unit sanity checks."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import numpy as np
import pytest
from bt11.constants import kB, hbar, c, T_planck
from bt11.bridge import closure_friction, bridge_energy, landauer_energy, diffusion_ratio

TOL = 1e-12
T = 300.0


def test_kB_dimensions():
    """kB * T should be ~4.14e-21 J at 300 K."""
    E = kB * T
    assert 4e-21 < E < 5e-21


def test_friction_positive():
    gamma = closure_friction(T)
    assert gamma > 0


def test_bridge_equals_landauer():
    gamma = closure_friction(T)
    E_b = bridge_energy(gamma, T)
    E_l = landauer_energy(T)
    assert abs(E_b - E_l) < TOL


def test_ratio_exactly_two():
    gamma = closure_friction(T)
    R = diffusion_ratio(gamma, T)
    assert abs(R - 2.0) < TOL


def test_planck_temperature_positive():
    assert T_planck > 0
    assert T_planck > 1e30  # Planck temperature is ~1.4e32 K


def test_hbar_magnitude():
    """hbar should be ~1.055e-34 J·s."""
    assert 1e-35 < hbar < 2e-34


def test_c_magnitude():
    """Speed of light ~3e8 m/s."""
    assert 2.9e8 < c < 3.1e8


def test_bridge_energy_scales_with_T():
    g1 = closure_friction(300.0)
    g2 = closure_friction(600.0)
    E1 = bridge_energy(g1, 300.0)
    E2 = bridge_energy(g2, 600.0)
    assert abs(E2 / E1 - 2.0) < TOL
