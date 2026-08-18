# Source Archive Review Status

Four source archives were reviewed for portfolio suitability.

## Siemens TIA Portal — Pneumatic Flow & Pressure Control

**Portfolio value:** high for PLC/process-control roles.

Reviewed engineering signals include distributed ET 200SP I/O, IO-Link, Festo proportional-pressure devices, pressure/flow handling, PID_Compact and WinCC HMI functionality.

**Do not publish the native archive.** It contains generated runtime/project data, logs, device configuration and machine-specific information.

## Siemens TIA Portal — Robot Cell & Gripper Integration

**Portfolio value:** high for automation/robotics/system-integration roles.

Reviewed engineering signals include S7-1500-class control, FANUC robot interfaces, SCHUNK gripper control, Festo pneumatic hardware, ET 200SP, PROFINET/PROFIsafe and HMI integration.

**Do not publish the native archive.** It also carries vendor GSD/GSDML packages and network/device configuration.

## TwinCAT — Offline Spline External Setpoint Generation

**Portfolio value:** high for motion-control roles.

Reviewed engineering signals include CSV spline import, parametric spline storage, cyclic spline evaluation, 1 ms point-generation logic, mover distribution and XPlanar execution.

**Do not publish the native workspace.** It contains compiled/vendor libraries, TwinSAFE material, license files and generated configuration/build artifacts.

## TwinCAT — Online Python/Vision Motion Planning

**Portfolio value:** very high for robotics, AI/automation and solution-engineering roles.

Reviewed engineering signals include Python/PLC state coordination, global plan buffers, sequence-based acknowledgement, per-mover waypoint execution, local overrides, active-slot mapping, synchronized execution and motion tracing.

**Do not publish the native workspace.** The public wire-harness repository already provides the safe system-level presentation; this case study should expose only selected PLC architecture and approved author-created logic.

## Recommended public portfolio order

1. AI-Based Wire Harness Perception, Motion Planning & PLC Integration
2. Industrial Thin-Object Segmentation Benchmark
3. Industrial PLC Control Projects

Within this repository, the online TwinCAT and robot-cell TIA Portal case studies are the strongest recruiter-facing items, followed by offline TwinCAT motion execution and pneumatic PID/IO-Link control.

## License status

No open-source license should be added until the exact source excerpts selected for publication have been verified as author-created and redistributable.
