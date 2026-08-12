#!/usr/bin/env python3
"""
Simulation Script: The Fifth Force Carrier (I⁰)
=================================================
Informational boson I⁰ – carrier of the fifth fundamental force.
Simulation according to Φ theory:
  F_info = −γ · ∇C(Φ)
  Yukawa potential: V(r) = −(γ²/4π) · (e^(−r/λ) / r)

Author: Chiméra (Michael Chodounsky)
Version: 1.0.0
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
import time

# ============================================================
# PHYSICAL CONSTANTS
# ============================================================

HBAR = 1.054571817e-34          # J·s (reduced Planck constant)
C_LIGHT = 299792458.0           # m/s (speed of light)
G_NEWTON = 6.67430e-11          # m³·kg⁻¹·s⁻² (gravitational constant)
K_BOLTZMANN = 1.380649e-23      # J/K (Boltzmann constant)
EV_TO_JOULE = 1.602176634e-19   # J/eV

# ============================================================
# PARAMETERS OF THE INFORMATIONAL BOSON I⁰
# ============================================================

M_I_EV = 1e-33                          # mass of I⁰ in eV
M_I = M_I_EV * EV_TO_JOULE / C_LIGHT**2 # mass in kg
COMPTON_WAVELENGTH = HBAR / (M_I * C_LIGHT)   # Compton wavelength [m]
COMPTON_FREQ = M_I * C_LIGHT**2 / HBAR       # Compton frequency [Hz]
GAMMA = 1e-30                        # coupling constant of the informational force (dimensionless)
GAMMA_SQ = GAMMA**2

# ============================================================
# CLASSES AND DATA STRUCTURES
# ============================================================

@dataclass
class InformationalBoson:
    """
    Informational boson I⁰ – quantum of the fifth force.
    Spin 0, ultralight mass ~10⁻³³ eV, zero charge.
    """
    name: str = "I⁰"
    mass_ev: float = M_I_EV
    mass_kg: float = M_I
    compton_wavelength: float = COMPTON_WAVELENGTH
    compton_frequency: float = COMPTON_FREQ
    spin: int = 0
    charge: int = 0
    coupling_constant: float = GAMMA

    def yukawa_potential(self, r: np.ndarray, c1: float, c2: float) -> np.ndarray:
        """
        Yukawa potential between two objects with internal complexity c1, c2.
        V(r) = −(γ²/4π) · (C₁·C₂) · e^(−r/λ) / r
        """
        return -(self.coupling_constant**2 / (4 * np.pi)) * c1 * c2 * np.exp(-r / self.compton_wavelength) / r

    def force(self, r: np.ndarray, c1: float, c2: float) -> np.ndarray:
        """
        Fifth force between two objects with internal complexity c1, c2.
        F = −dV/dr = (γ²/4π) · C₁·C₂ · e^(−r/λ) · (1/r² + 1/(λ·r))
        """
        lam = self.compton_wavelength
        return (self.coupling_constant**2 / (4 * np.pi)) * c1 * c2 * np.exp(-r / lam) * (1/r**2 + 1/(lam * r))


@dataclass
class TestMass:
    """
    Test object with internal computational complexity C.
    C is a dimensionless measure of information content.
    """
    name: str
    mass_kg: float
    complexity: float          # internal computational complexity C (0–1)
    description: str = ""

    def gravity_force(self, other: 'TestMass', r: float) -> float:
        """Gravitational force between two objects."""
        return G_NEWTON * self.mass_kg * other.mass_kg / r**2


# ============================================================
# SIMULATION FUNCTIONS
# ============================================================

def simulate_yukawa_potential(boson: InformationalBoson, c1: float, c2: float,
                               r_min: float = 1e18, r_max: float = 1e25,
                               num_points: int = 500):
    """
    Simulates the Yukawa potential of the informational force as a function of distance.
    """
    r = np.logspace(np.log10(r_min), np.log10(r_max), num_points)
    V = boson.yukawa_potential(r, c1, c2)
    return r, V


def simulate_fifth_force_vs_gravity(boson: InformationalBoson,
                                     object1: TestMass, object2: TestMass,
                                     r_min: float = 1e18, r_max: float = 1e25,
                                     num_points: int = 500):
    """
    Compares the fifth force with gravity for two test objects.
    """
    r = np.logspace(np.log10(r_min), np.log10(r_max), num_points)
    F_info = boson.force(r, object1.complexity, object2.complexity)
    F_grav = G_NEWTON * object1.mass_kg * object2.mass_kg / r**2
    return r, F_info, F_grav


def simulate_condensate_oscillation(boson: InformationalBoson,
                                     time_seconds: float = 1e20,
                                     num_points: int = 1000):
    """
    Simulates the time oscillation of the I⁰ condensate.
    The condensate is a coherent field with the Compton frequency.
    """
    t = np.linspace(0, time_seconds, num_points)
    # Oscillation phase
    omega = boson.compton_frequency
    phi = np.cos(omega * t)
    # Energy density of the condensate
    rho = 0.5 * (M_I * C_LIGHT**2) * phi**2
    return t, phi, rho


def simulate_equivalence_principle_violation(boson: InformationalBoson,
                                              mass: float = 1.0):
    """
    Simulates violation of the equivalence principle.
    Two objects with the same mass but different complexity C
    will have slightly different informational (fifth) force.
    """
    crystal = TestMass("Crystal", mass, 0.1, "Highly ordered, low C")
    glass = TestMass("Amorphous glass", mass, 0.9, "Disordered, high C")

    # Distance between test masses
    r = 1.0  # meter

    # Gravity (same for both)
    F_grav_crystal = crystal.gravity_force(glass, r)
    F_grav_glass = glass.gravity_force(crystal, r)

    # Informational force (different due to different C)
    F_info_crystal = boson.force(np.array([r]), crystal.complexity, glass.complexity)[0]
    F_info_glass = boson.force(np.array([r]), glass.complexity, crystal.complexity)[0]

    return crystal, glass, F_grav_crystal, F_info_crystal, F_info_glass


# ============================================================
# VISUALIZATION FUNCTIONS
# ============================================================

def plot_yukawa_potential():
    """Plots the Yukawa potential of the informational force."""
    boson = InformationalBoson()
    r, V = simulate_yukawa_potential(boson, c1=1.0, c2=1.0)

    fig, ax = plt.subplots(1, 2, figsize=(14, 5))

    # Linear scale
    ax[0].plot(r, np.abs(V), 'b-', linewidth=2)
    ax[0].axvline(boson.compton_wavelength, color='r', linestyle='--',
                  label='Compton wavelength')
    ax[0].set_xlabel('Distance r [m]')
    ax[0].set_ylabel('|V(r)| [J]')
    ax[0].set_title('Yukawa potential of the informational force (linear)')
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)

    # Logarithmic scale
    ax[1].loglog(r, np.abs(V), 'b-', linewidth=2)
    ax[1].axvline(boson.compton_wavelength, color='r', linestyle='--',
                  label='λ = 2×10²² m')
    ax[1].set_xlabel('Distance r [m] (log)')
    ax[1].set_ylabel('|V(r)| [J] (log)')
    ax[1].set_title('Yukawa potential (log‑log)')
    ax[1].legend()
    ax[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('yukawa_potential.png', dpi=150)
    plt.show()


def plot_fifth_force_vs_gravity():
    """Compares the fifth force with gravity."""
    boson = InformationalBoson()
    crystal = TestMass("Crystal", 1.0, 0.1, "Low C")
    glass = TestMass("Amorphous glass", 1.0, 0.9, "High C")

    r, F_info, F_grav = simulate_fifth_force_vs_gravity(boson, crystal, glass)

    fig, ax = plt.subplots(1, 2, figsize=(14, 5))

    # Linear scale
    ax[0].plot(r, F_grav, 'g--', linewidth=2, label='Gravity')
    ax[0].plot(r, F_info, 'b-', linewidth=2, label='Informational force')
    ax[0].set_xlabel('Distance r [m]')
    ax[0].set_ylabel('Force F [N]')
    ax[0].set_title('Informational force vs. gravity (linear)')
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)

    # Logarithmic scale
    ax[1].loglog(r, F_grav, 'g--', linewidth=2, label='Gravity')
    ax[1].loglog(r, F_info, 'b-', linewidth=2, label='Informational force')
    ax[1].set_xlabel('Distance r [m] (log)')
    ax[1].set_ylabel('Force F [N] (log)')
    ax[1].set_title('Informational force vs. gravity (log‑log)')
    ax[1].legend()
    ax[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('fifth_force_vs_gravity.png', dpi=150)
    plt.show()


def plot_condensate_oscillation():
    """Plots the oscillation of the I⁰ condensate."""
    boson = InformationalBoson()
    t, phi, rho = simulate_condensate_oscillation(boson)

    fig, ax = plt.subplots(2, 1, figsize=(12, 8))

    ax[0].plot(t, phi, 'b-', linewidth=1)
    ax[0].set_xlabel('Time [s]')
    ax[0].set_ylabel('Field amplitude φ')
    ax[0].set_title('Oscillation of the I⁰ condensate (Compton frequency)')
    ax[0].grid(True, alpha=0.3)

    ax[1].plot(t, rho, 'r-', linewidth=1)
    ax[1].set_xlabel('Time [s]')
    ax[1].set_ylabel('Energy density [J/m³]')
    ax[1].set_title('Energy density of the condensate')
    ax[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('condensate_oscillation.png', dpi=150)
    plt.show()


def plot_equivalence_violation():
    """Plots the violation of the equivalence principle."""
    boson = InformationalBoson()

    # Different levels of complexity C
    complexities = np.linspace(0.0, 1.0, 100)
    forces = []

    for c in complexities:
        test = TestMass("test", 1.0, c)
        F = boson.force(np.array([1.0]), test.complexity, 1.0)[0]
        forces.append(F)

    fig, ax = plt.subplots(1, 2, figsize=(14, 5))

    ax[0].plot(complexities, forces, 'b-', linewidth=2)
    ax[0].set_xlabel('Internal complexity C')
    ax[0].set_ylabel('Informational force F [N]')
    ax[0].set_title('Dependence of informational force on complexity C')
    ax[0].grid(True, alpha=0.3)

    # Example with specific objects
    objects = [
        TestMass("Crystal", 1.0, 0.1, "Low C"),
        TestMass("Glass", 1.0, 0.9, "High C"),
        TestMass("Living tissue", 1.0, 0.7, "Medium C"),
        TestMass("Supercomputer", 1.0, 0.95, "Very high C"),
    ]

    ax[1].bar([obj.name for obj in objects],
              [boson.force(np.array([1.0]), obj.complexity, 1.0)[0] for obj in objects],
              color=['gold', 'blue', 'green', 'purple'])
    ax[1].set_xlabel('Object')
    ax[1].set_ylabel('Informational force F [N]')
    ax[1].set_title('Informational force for different objects')
    ax[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('equivalence_violation.png', dpi=150)
    plt.show()


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():
    """Runs all simulations and displays results."""
    print("=" * 60)
    print("SIMULATION: Fifth Force and Informational Boson I⁰")
    print("=" * 60)

    boson = InformationalBoson()
    print("\nProperties of the informational boson I⁰:")
    print(f"  Mass: {boson.mass_ev:.0e} eV")
    print(f"  Compton wavelength: {boson.compton_wavelength:.2e} m")
    print(f"  Compton frequency: {boson.compton_frequency:.2e} Hz")
    print(f"  Spin: {boson.spin}")
    print(f"  Charge: {boson.charge}")
    print(f"  Coupling constant γ: {boson.coupling_constant:.0e}")

    print("\nStarting visualizations...")

    print("\n[1/4] Plotting Yukawa potential...")
    plot_yukawa_potential()

    print("\n[2/4] Comparing fifth force with gravity...")
    plot_fifth_force_vs_gravity()

    print("\n[3/4] Plotting oscillation of the I⁰ condensate...")
    plot_condensate_oscillation()

    print("\n[4/4] Plotting violation of the equivalence principle...")
    plot_equivalence_violation()

    print("\nSimulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
