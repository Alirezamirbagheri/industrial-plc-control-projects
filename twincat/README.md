# Beckhoff TwinCAT Case Studies

The reviewed TwinCAT material is best represented as **two distinct projects**, even though the later project builds on parts of the earlier XPlanar control foundation.

## 1. Offline Spline External Setpoint Generation

Trajectory geometry is generated offline, stored as parametric spline coefficients and imported into TwinCAT. The PLC evaluates the active spline segment cyclically and produces the next X/Y setpoint every task cycle for external-setpoint motion execution.

Reviewed concepts include CSV spline import, segment timing, cyclic spline evaluation, mover initialization/distribution and XPlanar motion execution.

See [`offline-spline-external-setpoint/README.md`](offline-spline-external-setpoint/README.md).

## 2. Online Python/Vision Motion Planning

The later project adds a dedicated Python/TwinCAT integration layer for camera-based perception and online planning. Python supplies global plan buffers and local corrections; TwinCAT supervises plan acceptance, synchronization, global execution, local-override priority and runtime state.

Reviewed concepts include Python command/status structures, sequence IDs, waypoint buffers, a PLC/Python state machine, global and local executors, active-mover mapping and motion tracing.

See [`online-python-vision-motion-planning/README.md`](online-python-vision-motion-planning/README.md).

## Why they are presented separately

The first case study demonstrates **deterministic PLC-side reconstruction of an offline mathematical trajectory**. The second demonstrates **closed-loop online coordination between AI/vision software and industrial motion control**. Those are sufficiently different engineering architectures to justify two portfolio case studies.

## Publication scope

The native TwinCAT archives contain many items that should not be transferred into a public GitHub repository: compiled/vendor libraries, TwinSAFE material, license/activation files, build artifacts, backup/configuration files and machine-specific data. Public release should consist only of sanitized documentation and selected author-created ST logic after redistribution rights are confirmed.

> Status: **both source archives reviewed; portfolio documentation prepared**.
