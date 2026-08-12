# Fifth Force Simulation (I⁰ Informational Boson)

This document describes the simulation script `fifth_force_simulation.py`, which models a hypothetical informational boson **I⁰** as the carrier of a fifth fundamental force using a Yukawa-type interaction.

## Overview

The script:

1. Defines physical constants (Planck constant, speed of light, Newton constant, etc.).
2. Defines I⁰ boson parameters:
   - Mass: `10^-33 eV`
   - Compton wavelength: approximately `10^22 m`
   - Coupling constant: `γ = 10^-30`
3. Implements the Yukawa potential and corresponding force.
4. Compares informational force magnitude with gravity.
5. Simulates oscillations of a coherent I⁰ condensate field.
6. Visualizes a complexity-dependent interaction as an equivalence-principle-style deviation thought experiment.

## Implemented Equations

- Informational-force law (conceptual):
  - `F_info = −γ · ∇C(Φ)`
- Yukawa potential:
  - `V(r) = −(γ²/4π) · (e^(−r/λ) / r)`
- Radial force from the potential:
  - `F = −dV/dr`

## Main Components

### `InformationalBoson` class
Encapsulates boson properties and provides:
- `yukawa_potential(r, c1, c2)`
- `force(r, c1, c2)`

### `TestMass` class
Represents test objects with:
- physical mass (`mass_kg`)
- informational complexity (`complexity`, dimensionless 0–1)
- gravity comparison helper (`gravity_force`)

### Simulation functions
- `simulate_yukawa_potential(...)`
- `simulate_fifth_force_vs_gravity(...)`
- `simulate_condensate_oscillation(...)`
- `simulate_equivalence_principle_violation(...)`

### Plot functions
- `plot_yukawa_potential()`
- `plot_fifth_force_vs_gravity()`
- `plot_condensate_oscillation()`
- `plot_equivalence_violation()`

## Generated Output

Running the script produces four PNG figures in the working directory:

- `yukawa_potential.png`
- `fifth_force_vs_gravity.png`
- `condensate_oscillation.png`
- `equivalence_violation.png`

## How to Run

```bash
python fifth_force_simulation.py
```

## Dependencies

Install required Python packages:

```bash
pip install numpy matplotlib
```

## Notes

- This code is a theoretical/numerical exploration and not an experimentally validated physical model.
- Parameter values are chosen to illustrate behavior over cosmological-scale ranges.
