# Offline Spline Execution Architecture

```mermaid
flowchart LR
    A[Offline path planning / smoothing] --> B[Spline coefficients]
    B --> C[Import into TwinCAT]
    C --> D[PLC spline parameter store]
    D --> E[Cyclic spline evaluation]
    E --> F[Next XY setpoint each PLC cycle]
    F --> G[External setpoint / mover execution]
    G --> H[Progress and segment supervision]
```

## Runtime sequence

1. Path geometry is calculated before machine execution.
2. Each spline segment is represented by a parameter interval and cubic coefficients for X and Y.
3. The parameters are imported into PLC-side storage.
4. The PLC allocates a number of cyclic interpolation steps to each segment.
5. On each control cycle, the active spline parameter `u` is evaluated.
6. The next XY point is generated from the cubic polynomial.
7. Segment counters advance until all mover paths are complete.
8. Runtime checks supervise path progress, step size and completion.

## Why this architecture matters

The approach separates expensive path preparation from deterministic PLC execution. The machine-side task only needs to evaluate compact spline coefficients and generate the next setpoint in the control cycle.

The reviewed implementation contains 1 ms cyclic point-generation logic. The public code excerpt is intentionally simplified and excludes machine identifiers, vendor libraries, native project files and safety configuration.
