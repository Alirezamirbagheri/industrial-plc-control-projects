# Source Archive Review Status

Four source archives and the supporting offline trajectory-preprocessing workspace were reviewed for portfolio suitability.

## Siemens TIA Portal — Pneumatic Flow & Pressure Control

**Portfolio value:** high for PLC/process-control roles.

Reviewed engineering signals include distributed ET 200SP I/O, IO-Link, Festo proportional-pressure devices, pressure/flow handling, PID_Compact and WinCC HMI functionality.

**Native archive:** keep private. The archive contains generated runtime/project data, logs, device configuration and environment-specific metadata. The audit also found an external Windows-path reference inside a development log; that material is excluded from the portfolio release.

**Current status:** architecture and selected author-created PLC logic documented in sanitized form from the reviewed TIA report. Native project/vendor material remains excluded.

## Siemens TIA Portal — Robot Cell & Gripper Integration

**Portfolio value:** high for automation/robotics/system-integration roles.

Reviewed engineering signals include S7-1500-class control, FANUC robot interfaces, SCHUNK gripper control, Festo pneumatic hardware, ET 200SP, PROFINET/PROFIsafe and HMI integration.

**Native archive:** keep private. The archive carries third-party GSD/GSDML packages plus network/device configuration and generated TIA/HMI data.

**Current status:** architecture and selected integration logic documented in sanitized form. Vendor-owned blocks and native project material remain excluded.

## TwinCAT — Offline Spline External Setpoint Generation

**Portfolio value:** high for motion-control, automation and numerical trajectory-processing roles.

Reviewed engineering signals include offline Python trajectory preprocessing, duplicate-point cleanup, RDP reduction, arc-length resampling, deviation-bounded cubic B-spline fitting, per-segment coefficient/timing export, CSV spline import, parametric spline storage, cyclic spline evaluation, 1 ms point-generation logic, mover distribution and XPlanar execution.

**Native workspaces:** keep private. The Python workspace contains raw simulation data, archived development versions, generated outputs and a local environment. The TwinCAT workspace contains compiled/vendor libraries, TwinSAFE material, license files, generated configuration/build artifacts and target-system network identifiers.

**Current status:** sanitized/refactored Python preprocessing source, representative smoothing visual, Python-to-TwinCAT architecture, selected-logic documentation and Structured Text spline-generation excerpt are published in the portfolio repository. Raw trajectory data and native engineering projects remain excluded.

## TwinCAT — Online Python/Vision Motion Planning

**Portfolio value:** very high for robotics, AI/automation and solution-engineering roles.

Reviewed engineering signals include Python/PLC state coordination, global plan buffers, sequence-based acknowledgement, per-mover waypoint execution, local overrides, active-slot mapping, synchronized execution and motion tracing.

**Native workspace:** keep private. The audit identified target-system network/AMS information, TwinSAFE configuration, license material, compiled libraries and environment-specific paths; those remain excluded.

**Current status:** sanitized architecture plus Structured Text excerpts for global-plan acceptance and local-override priority have been prepared.

## Recommended public portfolio order

1. AI-Based Wire Harness Perception, Motion Planning & PLC Integration
2. Industrial Thin-Object Segmentation Benchmark
3. Industrial PLC Control Projects

Within this repository, the online TwinCAT and robot-cell TIA Portal case studies are the strongest recruiter-facing items, while the offline TwinCAT case now demonstrates a complete numerical-preprocessing-to-deterministic-execution pipeline and the pneumatic project demonstrates PLC process control, sensing and PID-related automation.

## License status

No open-source license is added at this stage. The portfolio includes only reviewed/sanitized source representations; native vendor projects and third-party libraries remain excluded. The repository stays under default copyright unless a license is deliberately selected later.
