# Pneumatic Flow & Pressure Control — Siemens TIA Portal

## Objective

Industrial PLC control project for pneumatic pressure and flow handling using Siemens automation hardware and IO-Link-connected proportional-pressure components.

## Reviewed system elements

- Siemens TIA Portal project
- ET 200SP distributed I/O
- CM 4xIO-Link master
- Festo VPPM proportional-pressure devices
- analogue pressure / flow signals
- PID_Compact-based closed-loop control
- supporting WinCC Runtime Advanced HMI for setup and monitoring
- alarm, data-logging and diagnostic functionality

## Engineering contribution to showcase

The portfolio version focuses on the PLC/control architecture rather than the native TIA archive or full HMI implementation:

1. Acquire and scale pressure/flow measurements.
2. Map IO-Link and analogue process data into PLC structures.
3. Generate pressure/flow setpoints from the operating sequence.
4. Regulate the pneumatic process using PID-based logic.
5. Command proportional valves and supporting pneumatic actuators.
6. Supervise experiment state, sensor status, faults and control parameters.

## Recommended public artifacts

- simplified control architecture diagram
- selected SCL/LAD/FBD exports authored for the project
- sanitized PID-control overview
- IO-Link data-flow diagram

The HMI is part of the implemented system but is intentionally not a main portfolio artifact. If a visual is later useful, only a cropped and sanitized **Wire Floating Experiment (3_WFE)** screen should be considered.

## Excluded from public release

The native archive contains generated HMI runtime content, project databases, logs, vendor/device configuration and machine-specific details. Those are intentionally not copied into the public portfolio.

> Publication status: **documentation prepared; selected PLC logic / report material under review**.
