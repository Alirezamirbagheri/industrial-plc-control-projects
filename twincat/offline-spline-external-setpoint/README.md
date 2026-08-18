# Offline Spline External Setpoint Generation — TwinCAT 3

## Objective

Execute precomputed multi-mover trajectories in TwinCAT by importing parametric spline data and generating the next motion point cyclically inside the PLC.

## Reviewed implementation

The project contains PLC logic for:

- reading parametric spline data from CSV
- storing spline coefficients and segment metadata
- tracking the active segment for each mover
- evaluating cubic X/Y spline polynomials during runtime
- allocating cyclic interpolation points according to segment timing
- generating a new setpoint on each PLC task cycle
- mover initialization, target assignment and distribution
- XPlanar runtime update / visualization support

The reviewed logic is designed around a **1 ms point-generation cycle**. Instead of sending a complete list of discrete points to the motion system, the PLC reconstructs the path online from the imported spline coefficients and advances through the spline cyclically.

## Data flow

```text
Offline path / smoothing
        ↓
Parametric spline coefficients (CSV)
        ↓
TwinCAT CSV import
        ↓
Spline parameter database
        ↓
Cyclic spline evaluation in PLC
        ↓
Next X/Y setpoint every PLC cycle
        ↓
External setpoint generation
        ↓
XPlanar mover motion
```

## Representative PLC modules

The reviewed project includes modules corresponding to:

- CSV spline-parameter import
- cyclic spline-point generation
- mover distribution / target assignment
- process sequencing
- initialization and hardware update
- HMI/visualization support

These module names are documented here as architectural evidence; native project files and compiled Beckhoff libraries are not copied into the portfolio repository.

## Engineering relevance

This case study demonstrates the PLC side of trajectory execution: converting compact mathematical path data into deterministic control-cycle setpoints suitable for industrial motion execution.

## Public-release scope

The original TwinCAT workspace contains compiled/vendor libraries, TwinSAFE material, license files, generated build/configuration artifacts and machine-specific project data. Those remain excluded. Selected author-created ST logic may be added later only after redistribution rights are confirmed.

> Status: **source archive reviewed; documentation ready; public source extraction intentionally pending**.
