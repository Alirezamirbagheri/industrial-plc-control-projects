# Offline Spline External Setpoint Generation

TwinCAT 3 motion-control case study for executing precomputed spline trajectories through cyclic external setpoint generation.

## Control concept

Trajectory geometry is generated offline and represented by spline parameters. Those parameters are imported into the TwinCAT project before execution. At runtime, the PLC evaluates the active spline segment and computes the next trajectory point on every control cycle. The resulting cyclic position setpoints are then used to move the system along the precomputed path.

## Engineering focus

- import of precomputed spline coefficients / trajectory parameters
- cyclic evaluation of spline segments
- control-cycle-based point generation
- external setpoint generation
- trajectory progress and segment transitions
- mover motion execution
- timing, bounds and runtime supervision

## Portfolio release

The public version will contain only sanitized logic and documentation that can be redistributed safely. Native TwinCAT project files, vendor libraries, compiled artifacts, licenses, certificates and machine-specific configuration are not included by default.

> Status: **private staging area — source extraction and review pending**.
