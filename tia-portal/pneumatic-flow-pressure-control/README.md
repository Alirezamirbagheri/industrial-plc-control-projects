# Pneumatic Flow & Pressure Control — Siemens TIA Portal

## Objective

Industrial PLC/HMI control project for pneumatic pressure and flow handling using Siemens automation hardware and IO-Link-connected proportional-pressure components.

## Reviewed system elements

- Siemens TIA Portal project
- ET 200SP distributed I/O
- CM 4xIO-Link master
- Festo VPPM proportional-pressure devices
- analogue pressure / flow signals
- PID_Compact-based closed-loop control
- WinCC Runtime Advanced HMI
- alarm, data-logging and diagnostic functionality

## Engineering contribution to showcase

The portfolio version should focus on the control architecture rather than the native TIA archive:

1. Acquire and scale pressure/flow measurements.
2. Map IO-Link and analogue process data into PLC structures.
3. Generate pressure/flow setpoints from the operating sequence or HMI.
4. Regulate the pneumatic process using PID-based logic.
5. Command proportional valves and supporting pneumatic actuators.
6. Expose operating status, tuning values, alarms and diagnostics through the HMI.

## Recommended public artifacts

- simplified control architecture diagram
- selected SCL/LAD/FBD exports authored for the project
- sanitized PID-control overview
- IO-Link data-flow diagram
- sanitized HMI screenshots showing pressure/flow control and diagnostics

## Excluded from public release

The native archive contains generated HMI runtime content, project databases, logs, vendor/device configuration and machine-specific details. Those are intentionally not copied into the public portfolio.

> Publication status: **documentation prepared; source-code extraction pending ownership/redistribution review**.
