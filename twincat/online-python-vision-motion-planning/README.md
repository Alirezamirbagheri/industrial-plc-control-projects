# Online Python/Vision Motion Planning — TwinCAT 3

## Objective

Connect camera-based perception and Python motion planning to deterministic PLC-side execution for a multi-mover XPlanar system.

## Reviewed implementation

The final project extends the motion-control foundation with a dedicated Python/TwinCAT runtime interface. The reviewed PLC logic includes:

- command/status structures exchanged with Python
- sequence-ID-based global-plan acceptance
- per-mover waypoint buffers
- a PLC/Python planning state machine
- synchronized start / acknowledgement logic
- PLC-side global waypoint execution
- local override buffers and per-mover override execution
- priority handling between global motion and local corrective moves
- active mover / slot mapping
- fast status feedback
- motion-trace logging for runtime debugging

## Closed-loop architecture

```text
Camera
  ↓
Python perception
  ↓
Geometry / tracking
  ↓
Global + local motion planning
  ↓
Plan / override buffers + handshakes
  ↓
TwinCAT runtime state machine
  ↓
Global executor / local override executor
  ↓
XPlanar movers
  ↑
PLC status / acknowledgements / trace data
```

## Portfolio material

- [`ARCHITECTURE.md`](ARCHITECTURE.md) — Python/PLC responsibility split and data flow
- [`source-excerpts/global_plan_handshake.st`](source-excerpts/global_plan_handshake.st) — sequence-numbered global-plan acceptance
- [`source-excerpts/local_override_priority.st`](source-excerpts/local_override_priority.st) — simplified per-mover local-override priority logic
- [`source-excerpts/README.md`](source-excerpts/README.md) — source-excerpt scope and limitations

## Global-plan execution

Python provides a versioned global plan buffer containing mover IDs and waypoint data. The PLC consumes only a fresh sequence, copies it into an active execution buffer and acknowledges the accepted plan before coordinated motion begins.

## Local online correction

Local corrective commands are handled separately from the global plan. The reviewed implementation keeps per-mover pending/execution state and gives an accepted local override priority before global execution for that mover continues.

## PLC/Python state machine

The PLC-side planning state machine coordinates enable/init, layout remapping, global-plan construction, plan acknowledgement, synchronized start and runtime execution. This prevents the Python planner and PLC executor from advancing independently.

## Engineering relevance

This case study demonstrates the integration layer between non-deterministic AI/vision software and deterministic industrial motion control. The PLC is not used merely as an I/O bridge; it supervises plan acceptance, synchronization, mover execution, online corrections and runtime state.

## Relationship to the wire-harness project

This is the PLC execution architecture used in the final Version 3 wire-harness system. The system-level public overview is maintained separately in `wire-harness-ai-motion-planning`.

## Public-release scope

The native TwinCAT workspace includes Beckhoff/third-party compiled libraries, TwinSAFE configuration, license material, build outputs and machine-specific configuration. Those remain excluded. The source excerpts published here are intentionally simplified, author-focused architecture examples and are not a standalone TwinCAT project.

> Status: **final archive reviewed; sanitized architecture and source excerpts prepared**.
