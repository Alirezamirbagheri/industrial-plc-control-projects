# Industrial PLC Control Projects

Portfolio repository for selected industrial-automation work using **Siemens TIA Portal** and **Beckhoff TwinCAT 3**.

The reviewed source material is represented as **four separate engineering case studies**: two Siemens PLC projects and two Beckhoff TwinCAT projects. Native vendor projects, proprietary libraries, license material, machine-specific configuration, raw logs and restricted assets remain excluded.

## Case studies

### 1. Siemens TIA Portal — Pneumatic Flow & Pressure Control

PLC control project for pneumatic process handling using distributed I/O, IO-Link devices, sensor-based experiment logic and PID-related pressure regulation.

**Portfolio focus:** state-machine sequencing, sensor-array abstraction, pattern-based sensor diagnostics, position tracking with tolerance/stability logic, pressure control and IO-Link-oriented automation.

Includes a sanitized architecture document and selected PLC-logic representations.

See [`tia-portal/pneumatic-flow-pressure-control/README.md`](tia-portal/pneumatic-flow-pressure-control/README.md).

### 2. Siemens TIA Portal — Robot Cell & Gripper Integration

Multi-device automation project integrating Siemens PLC control with FANUC robot interfaces, a SCHUNK gripper, pneumatic equipment and distributed I/O.

**Portfolio focus:** robot/equipment coordination, typed gripper command/status mapping, parameterized operations, pneumatic valve state handling, PROFINET/PROFIsafe integration context and system diagnostics.

Includes a sanitized architecture document and selected integration-logic representations. Vendor-owned blocks are intentionally excluded.

See [`tia-portal/robot-cell-profinet-integration/README.md`](tia-portal/robot-cell-profinet-integration/README.md).

### 3. Beckhoff TwinCAT — Offline Spline External Setpoint Generation

Offline trajectory-execution project in which parametric spline coefficients are generated externally and imported into TwinCAT. The PLC evaluates the spline cyclically, reconstructs the next trajectory point and drives XPlanar movers through an external-setpoint-generation concept.

**Portfolio focus:** spline import/evaluation, cyclic point generation, timing allocation, mover execution and deterministic motion logic.

Includes a sanitized architecture document and Structured Text source excerpt.

See [`twincat/offline-spline-external-setpoint/README.md`](twincat/offline-spline-external-setpoint/README.md).

### 4. Beckhoff TwinCAT — Online Python/Vision Motion Planning

Closed-loop automation project coupling TwinCAT with Python-based perception and online motion planning. Python produces global motion plans and local overrides from camera/perception data; TwinCAT manages command/acknowledgement handshakes, synchronized execution, mover state and PLC-side runtime supervision.

**Portfolio focus:** Python–PLC coupling, online global plans, local override priority, state-machine coordination, synchronized multi-mover execution and motion tracing.

Includes a sanitized architecture document and Structured Text excerpts for global-plan acceptance and local-override priority logic.

See [`twincat/online-python-vision-motion-planning/README.md`](twincat/online-python-vision-motion-planning/README.md).

## Engineering themes

- IEC 61131-3 PLC programming and state-machine design
- Siemens TIA Portal and Beckhoff TwinCAT 3
- PROFINET, PROFIsafe, IO-Link and ADS communication concepts
- sensor-driven process control and diagnostics
- PID-related pneumatic pressure control
- robot and gripper integration
- cyclic setpoint generation and XPlanar motion execution
- Python–PLC integration and online planning
- fault handling, synchronization and runtime supervision

## Current publication status

- **TIA pneumatic control:** reviewed; architecture and sanitized selected logic prepared
- **TIA robot cell:** reviewed; architecture and sanitized selected integration logic prepared
- **TwinCAT offline:** reviewed; sanitized architecture/source excerpt prepared
- **TwinCAT online:** reviewed; sanitized architecture/source excerpts prepared

The HMI implementations are part of the original systems but are intentionally not a main portfolio artifact. The public presentation focuses on control logic and system integration.

The native engineering archives are **not** published. The review identified vendor packages, compiled libraries, license files, project databases, target-system/network configuration, raw logs and other generated artifacts that should remain outside a public portfolio.

## Repository layout

```text
tia-portal/
  pneumatic-flow-pressure-control/
    ARCHITECTURE.md
    SELECTED_LOGIC.md
  robot-cell-profinet-integration/
    ARCHITECTURE.md
    SELECTED_LOGIC.md

twincat/
  offline-spline-external-setpoint/
    ARCHITECTURE.md
    source-excerpts/
  online-python-vision-motion-planning/
    ARCHITECTURE.md
    source-excerpts/

PUBLIC_RELEASE_CHECKLIST.md
REVIEW_STATUS.md
```

## License

No open-source license is assigned. Native vendor projects and third-party libraries are excluded, and the portfolio repository remains under default copyright unless a license is deliberately selected later.
