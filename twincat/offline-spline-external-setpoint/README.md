# Offline Spline External Setpoint Generation — TwinCAT 3

## Objective

Convert dense, irregular multi-mover trajectories from offline simulation into compact, smooth and motion-aware spline segments, then execute those trajectories deterministically in TwinCAT through cyclic external setpoint generation.

This case study contains two coupled engineering stages:

1. **Python offline preprocessing** reduces and smooths the simulated trajectories and exports spline/timing parameters to CSV.
2. **TwinCAT runtime execution** imports those parameters and reconstructs the next mover setpoint on each PLC point-generation cycle.

## End-to-end workflow

```text
Offline wire-motion simulation
        ↓
Dense / irregular XY points per mover
        ↓
Python point reduction + smoothing
        ↓
Deviation-bounded cubic spline fitting
        ↓
Per-segment geometry + timing weights
        ↓
ParametricSplineCoeff.csv
        ↓
TwinCAT spline parameter store
        ↓
Segment timing from requested total motion time
        ↓
Cyclic cubic-spline evaluation
        ↓
External XY setpoint each PLC cycle
        ↓
XPlanar mover execution
```

## Python trajectory preprocessing

The reviewed Python workflow was created because the offline simulation produced many points that were not suitable for direct deterministic execution. The preprocessing stage:

- removes repeated coordinates,
- reduces the point set using Ramer-Douglas-Peucker simplification,
- parameterizes the path by normalized arc length,
- resamples the trajectory,
- fits a cubic parametric B-spline,
- adaptively reduces smoothing until a maximum geometric-deviation limit is satisfied,
- converts the spline to piecewise cubic coefficients for X and Y,
- maps the original simulation samples back to spline segments,
- calculates segment length and temporal/sample-density information,
- exports normalized timing information together with the polynomial coefficients.

See [`python-preprocessing/`](python-preprocessing/) for the sanitized/refactored implementation.

## Representative smoothing output

![Trajectory smoothing comparison](assets/trajectory_smoothing_comparison.png)

Black shows original sampled trajectories and red shows the smoothed trajectories. The examples demonstrate that the optimized spline path follows the intended geometry while filtering small irregularities before PLC execution.

## TwinCAT execution

The TwinCAT project contains PLC logic for:

- importing parametric spline data from CSV,
- storing segment coefficients and metadata,
- tracking the active segment for each mover,
- allocating cyclic interpolation points from the requested total motion time and segment weighting,
- evaluating cubic X/Y spline polynomials during runtime,
- generating a new setpoint on each point-generation cycle,
- mover initialization, target assignment and distribution,
- runtime progress, step-size and completion supervision.

The reviewed logic is designed around a **1 ms point-generation cycle**. Instead of replaying a large precomputed point list, the PLC reconstructs the path from compact spline parameters and advances through the active segment cyclically.

## Portfolio material

- [`ARCHITECTURE.md`](ARCHITECTURE.md) — complete Python-to-TwinCAT architecture
- [`SELECTED_LOGIC.md`](SELECTED_LOGIC.md) — selected preprocessing and execution logic
- [`python-preprocessing/trajectory_preprocessing.py`](python-preprocessing/trajectory_preprocessing.py) — sanitized/refactored Python preprocessing source
- [`python-preprocessing/README.md`](python-preprocessing/README.md) — geometry and motion-aware timing pipeline
- [`source-excerpts/cyclic_spline_generation.st`](source-excerpts/cyclic_spline_generation.st) — sanitized Structured Text excerpt showing cyclic cubic-spline evaluation
- [`source-excerpts/README.md`](source-excerpts/README.md) — source-excerpt scope and limitations

## Engineering relevance

This case study demonstrates a complete offline-to-realtime motion pipeline: numerical trajectory processing in Python, compact parametric representation, CSV handover, and deterministic PLC-cycle trajectory reconstruction for industrial motion execution.

## Public-release scope

The original Python workspace contained archived development versions, raw simulation data, generated outputs and a local virtual environment. The original TwinCAT workspace contains compiled/vendor libraries, TwinSAFE material, license files, generated build/configuration artifacts and machine-specific project data. Those remain excluded.

The Python source in this repository is a sanitized/refactored portfolio version of the project algorithm. The Structured Text excerpt is intentionally reduced to the author-created execution concept and is not a standalone TwinCAT project.
