# Python Offline Trajectory Preprocessing

This module prepares raw multi-mover trajectories from offline simulation for deterministic TwinCAT execution.

The simulation output can contain a large number of irregular or redundant points. The preprocessing stage reduces that data, smooths the path while limiting geometric deviation, and converts each mover trajectory into compact cubic-spline segments that can be reconstructed cyclically in the PLC.

## Pipeline

```text
Raw simulated XY points
        ↓
Duplicate-point cleanup
        ↓
RDP point reduction
        ↓
Arc-length parameterization + resampling
        ↓
Adaptive cubic B-spline smoothing
        ↓
Deviation check against original trajectory
        ↓
Piecewise cubic segment conversion
        ↓
Geometry + temporal weighting per segment
        ↓
ParametricSplineCoeff.csv
        ↓
TwinCAT cyclic spline evaluation
```

## Geometry processing

The portfolio implementation preserves the main logic of the project code:

- **Ramer-Douglas-Peucker (RDP)** simplification reduces unnecessary points while retaining the main path geometry.
- The reduced path is parameterized by normalized cumulative arc length.
- The path is resampled before cubic B-spline fitting.
- The smoothing factor is reduced iteratively until the maximum nearest-point deviation falls below the configured threshold.
- Start and end positions are preserved for the PLC handover.

## Motion-aware segment weighting

The original simulation point sequence also carries information about how motion progressed along the path. After smoothing, raw points are mapped back to the smoothed trajectory by normalized path progress.

For every spline segment the preprocessing records:

- segment length,
- number of mapped raw simulation points,
- accumulated raw-path distance,
- normalized raw-point weight,
- a normalized `Time_Scale_Factor`.

The project computes the relative time factor from the geometric change and original simulation-point distribution, then normalizes it per mover. TwinCAT can use the segment weighting together with the requested **total motion time** and PLC cycle time to determine how many cyclic points are generated in each spline segment.

## CSV handover

Each row of `ParametricSplineCoeff.csv` represents one spline segment and contains the data required for PLC-side reconstruction:

```text
Mover, Segment, U_Start, U_End,
Ax, Bx, Cx, Dx,
Ay, By, Cy, Dy,
Length_mm, Length_Weight, Time_Scale_Factor,
NumRawPoints, RawPointsWeight, RawDistanceSum
```

TwinCAT evaluates the segment as:

```text
x(u) = Ax + Bx*u + Cx*u² + Dx*u³
y(u) = Ay + By*u + Cy*u² + Dy*u³
```

This avoids transferring or storing the complete dense trajectory as a point list.

## Representative output

![Trajectory smoothing comparison](../assets/trajectory_smoothing_comparison.png)

Representative offline results: **black = original sampled trajectory, red = smoothed trajectory**. The figure shows several trajectory examples/parameter cases and illustrates how the smoothed path follows the original geometry while removing small irregularities and reducing the representation to spline segments.

## Source

- [`trajectory_preprocessing.py`](trajectory_preprocessing.py) — sanitized/refactored implementation of the project preprocessing pipeline
- [`requirements.txt`](requirements.txt) — Python dependencies

The original raw simulation CSV files, development environment, archived experimental versions and generated project artifacts are intentionally not included in the public repository.
