"""Tests for kernel solutions and TICE closure factor."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import numpy as np
import pytest
from bt11.kernels import (
    geff_drude, geff_algebraic, geff_gaussian,
    ctice, bridge_energy_tice,
    crossing_time_drude, crossing_time_algebraic, crossing_time_gaussian,
)

TOL = 1e-10


class TestDrudeKernel:
    g0 = 0.5
    bA_Om = 1.5
    Omega = 1.0

    def test_initial_friction(self):
        assert abs(geff_drude(0, self.g0, self.bA_Om) - self.g0) < TOL

    def test_asymptotic_friction(self):
        expected = self.g0 + self.bA_Om
        assert abs(geff_drude(1e6, self.g0, self.bA_Om) - expected) < TOL

    def test_ctice_initial(self):
        g = geff_drude(0, self.g0, self.bA_Om)
        assert abs(ctice(g) - 1.0 / self.g0) < TOL

    def test_crossing_exists(self):
        t = crossing_time_drude(self.g0, self.bA_Om)
        assert not np.isnan(t) and t > 0

    def test_ctice_at_crossing(self):
        t = crossing_time_drude(self.g0, self.bA_Om)
        g = geff_drude(t, self.g0, self.bA_Om)
        assert abs(ctice(g) - 1.0) < TOL


class TestAlgebraicKernel:
    g0 = 0.5
    bA = 1.5
    Omega = 1.0
    n = 2

    def test_crossing_exists(self):
        t = crossing_time_algebraic(self.g0, self.bA, self.Omega, self.n)
        assert not np.isnan(t) and t > 0

    def test_ctice_at_crossing(self):
        t = crossing_time_algebraic(self.g0, self.bA, self.Omega, self.n)
        g = geff_algebraic(t, self.g0, self.bA, self.Omega, self.n)
        assert abs(ctice(g) - 1.0) < TOL


class TestGaussianKernel:
    g0 = 0.5
    bA = 1.5 / np.sqrt(np.pi / 2)
    Omega = 1.0

    def test_crossing_exists(self):
        t = crossing_time_gaussian(self.g0, self.bA, self.Omega)
        assert not np.isnan(t) and t > 0

    def test_ctice_at_crossing(self):
        t = crossing_time_gaussian(self.g0, self.bA, self.Omega)
        g = geff_gaussian(t, self.g0, self.bA, self.Omega)
        assert abs(ctice(g) - 1.0) < TOL
