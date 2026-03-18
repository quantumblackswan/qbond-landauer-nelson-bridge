"""Tests for inversion formulas."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import numpy as np
import pytest
from bt11.inversion import (
    friction_from_ratio,
    temperature_from_ratio,
    ratio_from_bridge,
    delta_from_deviation,
    ctice_from_bridge,
)
from bt11.bridge import closure_friction, landauer_energy, deviation
from bt11.constants import kB, hbar

TOL = 1e-12
T = 300.0


def test_friction_roundtrip():
    gamma = friction_from_ratio(2.0, T)
    assert abs(gamma - closure_friction(T)) < TOL


def test_temperature_roundtrip():
    gamma = closure_friction(T)
    T_out = temperature_from_ratio(2.0, gamma)
    assert abs(T_out - T) < TOL


def test_ratio_from_landauer():
    E_L = landauer_energy(T)
    R = ratio_from_bridge(E_L, T)
    assert abs(R - 2.0) < TOL


def test_delta_roundtrip():
    for d in [0.1, -0.1, 0.5, -0.5]:
        dE = deviation(d, T)
        d_out = delta_from_deviation(dE, T)
        assert abs(d_out - d) < TOL * 10  # slightly wider tol for roundtrip


def test_ctice_from_landauer():
    E_L = landauer_energy(T)
    C = ctice_from_bridge(E_L, T)
    assert abs(C - 1.0) < TOL
