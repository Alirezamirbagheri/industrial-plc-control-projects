# Beckhoff TwinCAT Projects

This section contains two distinct TwinCAT case studies with different control architectures.

## 1. Offline Spline External Setpoint Generation

An offline trajectory-execution concept in which spline parameters are prepared outside the PLC and imported into TwinCAT. During runtime, the PLC evaluates the trajectory cyclically and generates the next motion setpoint on every control cycle through an external-setpoint-generation approach.

Portfolio focus:

- spline-parameter import
- cyclic trajectory evaluation
- point-by-point setpoint generation
- external setpoint generation
- mover/path execution
- PLC-side timing and motion logic

See [`offline-spline-external-setpoint/README.md`](offline-spline-external-setpoint/README.md).

## 2. Online Python/Vision Motion Planning

A closed-loop automation concept in which TwinCAT is coupled with Python. Camera-based perception and online motion planning run on the Python side, while the PLC manages synchronized machine execution, handshakes, state transitions and motion commands.

Portfolio focus:

- Python–TwinCAT communication
- camera/perception integration
- online path and motion generation
- synchronized multi-mover execution
- runtime state-machine logic
- command/acknowledgement handshakes
- fault and execution supervision

See [`online-python-vision-motion-planning/README.md`](online-python-vision-motion-planning/README.md).

## Publication scope

Only sanitized, author-created engineering content should be published. Native TwinCAT workspaces, Beckhoff/third-party libraries, compiled libraries, license or activation material, certificates, real AMS Net IDs, IP addresses and machine-specific configuration remain excluded unless redistribution rights are explicit.

> Status: **private staging area — source review pending**.
