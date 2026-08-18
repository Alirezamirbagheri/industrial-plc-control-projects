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

## Engineering contribution

The portfolio presentation focuses on the PLC/control architecture rather than the native TIA archive:

1. Map physical sensor channels into reusable PLC data structures.
2. Detect inconsistent sensor patterns and generate fault information.
3. Track wire/process position using selected sensors, target/tolerance logic and stability timing.
4. Coordinate experiment phases through a top-level state machine with stop/restart handling.
5. Generate and adapt pneumatic pressure commands using sensor feedback and timed pressure steps.
6. Keep diagnostics and operator interaction separate from the core control logic.

## Portfolio material

- [`ARCHITECTURE.md`](ARCHITECTURE.md) — control decomposition and data flow
- [`SELECTED_LOGIC.md`](SELECTED_LOGIC.md) — sanitized representations of the strongest PLC logic

The HMI is part of the implemented system but is intentionally **not** used as a main portfolio artifact. The reviewed `3_WFE` screen is retained only as optional internal reference; the public presentation remains focused on PLC engineering.

## Public-release boundary

The native archive contains generated HMI runtime content, project databases, logs, vendor/device configuration and machine-specific details. Siemens/vendor library implementations and raw project files are not copied into the portfolio.

> Publication status: **source report reviewed; architecture and selected sanitized logic prepared**.
