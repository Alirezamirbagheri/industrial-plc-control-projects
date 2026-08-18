# Selected Logic — Online Python/Vision Motion Planning

This case study publishes selected, sanitized PLC-side logic from the reviewed final TwinCAT implementation rather than the native engineering workspace.

## 1. Versioned global-plan acceptance

Python provides a global motion plan together with a sequence identifier. TwinCAT accepts only a fresh sequence, copies the plan into the active PLC execution state and acknowledges the accepted version before motion proceeds.

Representative sanitized source:

- [`source-excerpts/global_plan_handshake.st`](source-excerpts/global_plan_handshake.st)

## 2. Per-mover waypoint execution

The PLC maintains mover-specific waypoint execution state and supervises coordinated progress through the accepted global plan.

## 3. Local override priority

Online corrective commands are maintained separately from the global plan. When a valid local command is pending for a mover, the local correction receives execution priority before that mover resumes its global trajectory.

Representative sanitized source:

- [`source-excerpts/local_override_priority.st`](source-excerpts/local_override_priority.st)

## 4. Python/PLC state coordination

The reviewed implementation coordinates initialization, layout/remap handling, global-plan construction, plan acknowledgement, synchronized start and runtime execution through explicit PLC/Python state and handshake variables.

## 5. Runtime supervision

Additional PLC-side functions cover active mover/slot mapping, fast status feedback and motion-trace data used for runtime debugging and verification.

## Why these parts were selected

These elements demonstrate the boundary between non-deterministic perception/planning software and deterministic PLC motion execution. The PLC is responsible for plan acceptance, synchronization, execution state and online correction priority rather than acting only as an I/O bridge.

The native TwinCAT workspace, compiled/vendor libraries, TwinSAFE configuration, license material, machine-specific network configuration and generated build artifacts are intentionally excluded.