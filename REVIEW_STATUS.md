# Source Archive Review Status

Four source archives were reviewed for portfolio suitability.

## Siemens TIA Portal — Pneumatic Flow & Pressure Control

**Portfolio value:** high for PLC/process-control roles.

Reviewed engineering signals include distributed ET 200SP I/O, IO-Link, Festo proportional-pressure devices, pressure/flow handling, PID_Compact and WinCC HMI functionality.

**Native archive:** keep private. The archive contains generated runtime/project data, logs, device configuration and environment-specific metadata. The audit also found an external Windows-path reference inside a development log; that material is excluded from the portfolio release.

**Current status:** documentation prepared. Selected author-created PLC blocks still need to be exported from TIA Portal in source/XML form and reviewed before publication.

## Siemens TIA Portal — Robot Cell & Gripper Integration

**Portfolio value:** high for automation/robotics/system-integration roles.

Reviewed engineering signals include S7-1500-class control, FANUC robot interfaces, SCHUNK gripper control, Festo pneumatic hardware, ET 200SP, PROFINET/PROFIsafe and HMI integration.

**Native archive:** keep private. The archive carries third-party GSD/GSDML packages plus network/device configuration and generated TIA/HMI data.

**Current status:** documentation prepared. Selected author-created robot/gripper handshake, sequence and HMI-interface blocks still need to be exported from TIA Portal and reviewed before publication.

## TwinCAT — Offline Spline External Setpoint Generation

**Portfolio value:** high for motion-control roles.

Reviewed engineering signals include CSV spline import, parametric spline storage, cyclic spline evaluation, 1 ms point-generation logic, mover distribution and XPlanar execution.

**Native workspace:** keep private. It contains compiled/vendor libraries, TwinSAFE material, license files, generated configuration/build artifacts and target-system network identifiers.

**Current status:** sanitized architecture and Structured Text spline-generation excerpt prepared in this repository. Native project files remain excluded.

## TwinCAT — Online Python/Vision Motion Planning

**Portfolio value:** very high for robotics, AI/automation and solution-engineering roles.

Reviewed engineering signals include Python/PLC state coordination, global plan buffers, sequence-based acknowledgement, per-mover waypoint execution, local overrides, active-slot mapping, synchronized execution and motion tracing.

**Native workspace:** keep private. The audit identified target-system network/AMS information, TwinSAFE configuration, license material, compiled libraries and environment-specific paths; those remain excluded.

**Current status:** sanitized architecture plus Structured Text excerpts for global-plan acceptance and local-override priority have been prepared.

## Recommended public portfolio order

1. AI-Based Wire Harness Perception, Motion Planning & PLC Integration
2. Industrial Thin-Object Segmentation Benchmark
3. Industrial PLC Control Projects

Within this repository, the online TwinCAT and robot-cell TIA Portal case studies are the strongest recruiter-facing items, followed by offline TwinCAT motion execution and pneumatic PID/IO-Link control.

## License status

No open-source license is added at this stage. The repository should remain under default copyright until the exact exported TIA source blocks and any other source intended for public redistribution have been confirmed as author-created and publishable.
