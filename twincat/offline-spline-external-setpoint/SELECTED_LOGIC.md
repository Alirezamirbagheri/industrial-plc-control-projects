# Selected Logic — Offline Spline External Setpoint Generation

This case study combines selected, sanitized logic from both the Python offline preprocessing workflow and the TwinCAT runtime project rather than publishing either native development workspace.

## 1. Raw trajectory reduction

Offline wire-motion simulation produces dense mover trajectories. The Python preprocessing first removes repeated coordinates and applies **Ramer-Douglas-Peucker (RDP)** simplification to reduce unnecessary points while preserving the main path geometry.

Representative source:

- [`python-preprocessing/trajectory_preprocessing.py`](python-preprocessing/trajectory_preprocessing.py)

## 2. Arc-length resampling and spline smoothing

The reduced path is parameterized by normalized cumulative arc length and resampled before a cubic parametric B-spline is fitted.

The smoothing factor is adjusted iteratively: if the fitted trajectory exceeds the configured maximum nearest-point deviation from the original path, smoothing is reduced and the fit is repeated. This balances geometric smoothness with path fidelity.

## 3. Motion-aware spline segmentation

The final spline is converted to piecewise cubic polynomial coefficients for X and Y:

```text
x(u) = Ax + Bx*u + Cx*u² + Dx*u³
y(u) = Ay + By*u + Cy*u² + Dy*u³
```

The original simulation samples are mapped back to the smoothed path. For each segment the preprocessing records geometric and motion-related information such as:

- segment length,
- original sample count,
- accumulated raw trajectory distance,
- normalized raw-point weight,
- normalized segment time factor.

The resulting `ParametricSplineCoeff.csv` is the compact interface between Python preprocessing and TwinCAT execution.

## 4. Spline parameter import

TwinCAT imports the per-mover spline segments and stores the parameter interval, X/Y coefficients and segment metadata required for runtime path reconstruction.

## 5. Cyclic time allocation and cubic evaluation

For each segment, the PLC derives a segment duration from the requested total motion time and the imported segment weighting. The number of point-generation cycles is then calculated from the segment duration and PLC cycle time.

Representative sanitized source:

- [`source-excerpts/cyclic_spline_generation.st`](source-excerpts/cyclic_spline_generation.st)

On each point-generation cycle, the PLC advances `u` within the active segment and evaluates the cubic X/Y polynomials to obtain the next setpoint.

## 6. External setpoint generation

The generated point is passed to the XPlanar motion layer as the next external setpoint. The reviewed implementation uses a **1 ms point-generation cycle**, allowing the PLC to reconstruct the trajectory deterministically instead of replaying a large dense point list.

## 7. Mover execution and supervision

Supporting PLC logic handles mover initialization, active-segment tracking, target assignment, step-size checks, path progress and end-of-path handling.

## Why these parts were selected

Together these elements show the full engineering chain rather than only the PLC endpoint:

**offline simulation → geometric reduction → smooth parametric trajectory → motion-aware segment timing → CSV handover → deterministic cyclic PLC execution**.

Raw simulation data, development archives, local Python environments, native TwinCAT files, compiled/vendor libraries, TwinSAFE content, license material and target-specific configuration are intentionally excluded.
