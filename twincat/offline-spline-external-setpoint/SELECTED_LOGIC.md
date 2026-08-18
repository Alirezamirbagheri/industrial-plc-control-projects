# Selected Logic — Offline Spline External Setpoint Generation

This case study uses selected, sanitized logic from the reviewed TwinCAT project rather than publishing the native engineering workspace.

## 1. Spline parameter import

The offline workflow begins with externally generated parametric spline data. TwinCAT stores the coefficients and segment metadata required for runtime reconstruction of the path.

## 2. Active-segment tracking

For each mover, PLC logic keeps track of the currently active spline segment and the corresponding timing/progress state.

## 3. Cyclic cubic-spline evaluation

At runtime, the PLC evaluates the active X/Y cubic spline polynomials and computes the next trajectory point on each point-generation cycle.

Representative sanitized source:

- [`source-excerpts/cyclic_spline_generation.st`](source-excerpts/cyclic_spline_generation.st)

## 4. External setpoint generation

The generated point is passed to the XPlanar motion layer as the next external setpoint. The reviewed implementation uses a 1 ms point-generation cycle, allowing the PLC to reconstruct and advance along the trajectory deterministically rather than replaying a large precomputed point list.

## 5. Mover execution

Supporting PLC logic handles mover initialization, target assignment, distribution and runtime updates around the cyclic setpoint-generation core.

## Why these parts were selected

These elements best demonstrate the engineering contribution of the project: converting compact offline spline parameters into deterministic PLC-cycle motion commands.

The native TwinCAT project, compiled/vendor libraries, TwinSAFE content, license material, target-specific configuration and generated build artifacts are intentionally excluded.