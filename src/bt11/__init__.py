"""
bt11 — Landauer–Nelson Bridge with TICE Closure
================================================

Core library for computing bridge energies, deviation formulas,
kernel-dependent TICE closure factors, and inversion relations.

Author: Kevin Henry Miller
        Q-Bond Network DeSCI DAO, LLC
        Kevin@qbondnetwork.com
        ORCID: 0009-0007-7286-3373
"""

from .constants import kB, hbar, c
from .bridge import (
    diffusion_ratio,
    bridge_energy,
    landauer_energy,
    deviation,
    closure_friction,
)
from .kernels import (
    geff_drude,
    geff_algebraic,
    geff_gaussian,
    ctice,
    bridge_energy_tice,
    crossing_time_drude,
)
from .inversion import (
    friction_from_ratio,
    temperature_from_ratio,
    ratio_from_bridge,
)

__version__ = "1.0.0"
__author__ = "Kevin Henry Miller"
