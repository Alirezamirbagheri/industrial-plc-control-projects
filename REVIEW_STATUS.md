# Source Archive Review Status

Four source archives/reports were reviewed for portfolio suitability.

## Siemens TIA Portal — Pneumatic Flow & Pressure Control

**Portfolio value:** high for PLC/process-control roles.

Reviewed engineering signals include distributed ET 200SP I/O, IO-Link, Festo proportional-pressure devices, pressure/flow handling, a multi-state experiment controller, sensor-array mapping, pattern-based sensor fault detection, position tracking with tolerance/stability logic and PID-related pressure control.

**Native archive:** keep private. It contains generated runtime/project data, logs, device configuration and environment-specific metadata. An external Windows-path reference was also present in development-log material; that content is excluded.

**Current status:** source report reviewed. A sanitized architecture document and selected logic representations have been prepared. Full native block export is no longer required for the portfolio version.

## Siemens TIA Portal — Robot Cell & Gripper Integration

**Portfolio value:** high for automation/robotics/system-integration roles.

Reviewed engineering signals include S7-1500-class control, FANUC robot interfaces, SCHUNK gripper integration, Festo pneumatic hardware, ET 200SP, PROFINET/PROFIsafe project context, valve-state logic, typed gripper process-data mapping, parameterized gripper operations and system-level fault aggregation.

**Native archive:** keep private. It contains third-party GSD/GSDML packages, vendor-owned function blocks, network/device configuration and generated TIA/HMI data.

**Current status:** source report reviewed. A sanitized architecture document and selected project-specific integration-logic representations have been prepared. Vendor code is not reproduced.

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

## HMI scope

HMI functionality exists in the TIA projects but is intentionally not a main public artifact. The control and integration logic is stronger portfolio material. The WFE screen can remain as an optional internal reference, but no HMI screenshot is required for the initial public release.

## Recommended public portfolio order

1. AI-Based Wire Harness Perception, Motion Planning & PLC Integration
2. Industrial Thin-Object Segmentation Benchmark
3. Industrial PLC Control Projects

Within this repository, the online TwinCAT and robot-cell TIA Portal case studies are the strongest recruiter-facing items, followed by offline TwinCAT motion execution and pneumatic control.

## License status

No open-source license is added. The portfolio excludes native vendor projects and third-party library implementations and remains under default copyright unless a license is deliberately selected later.
